# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản nâng cấp giao diện:
  - Thanh bên giống hệt thiết kế: logo, trạng thái trực tuyến, danh sách chức năng
  - Tối ưu hiển thị chế độ tối/sáng, màu sắc thống nhất theo từng môn
  - Hiệu ứng tương tác, đánh dấu mục đang chọn rõ ràng
  - Thông tin trực tuyến cập nhật real-time
"""
import streamlit as st
import streamlit.components.v1 as components
import io
import random
import re
import time
import zipfile
import xml.etree.ElementTree as ET
import uuid
import requests
import os
import hashlib
import threading
import hmac
import html
import json
import datetime
from collections import OrderedDict, deque

# [VÁ 2] Không để cả trang sập nếu server chưa cài google-genai:
try:
    from google import genai
    from google.genai import types
    from google.genai import errors as genai_errors
    HAS_GENAI = True
except Exception:
    genai = types = genai_errors = None
    HAS_GENAI = False

# ==================== CẤU HÌNH TRANG & ĐIỀU HƯỚNG SỚM ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "home_jump" in st.session_state:
    st.session_state["che_do_sidebar"] = "🏠 Trang chủ / Hướng dẫn"
    st.session_state["mon_main"] = st.session_state.pop("home_jump")

if "search_jump" in st.session_state:
    item = st.session_state.pop("search_jump")
    st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
    st.session_state["mon_main"] = item["mon"]
    st.session_state["s_lop"] = item["lop"]
    st.session_state["s_chuong"] = item["chuong"]
    st.session_state["s_bai"] = item["bai"]

# ==================== KHỞI TẠO LOCK & CACHE TOÀN CỤC ====================
@st.cache_resource
def get_global_locks():
    return {
        "user_count_lock": threading.Lock(),
        "ai_cache_lock": threading.Lock(),
        "rate_lock": threading.Lock(),
        "online_users": {},
        "ai_cache": OrderedDict(),
        "ai_request_times": deque(),
        "admin_fail_lock": threading.Lock(),
        "admin_fail_times": deque(),
    }
GLOBALS = get_global_locks()

# ==================== ĐỌC SECRETS AN TOÀN ====================
def get_secret(key_name, default_val=""):
    try:
        if key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    return os.getenv(key_name, default_val)

def lay_danh_sach_gemini_keys():
    keys = []
    try:
        val = get_secret("GEMINI_API_KEYS")
        if isinstance(val, list):
            keys.extend([k.strip() for k in val if str(k).strip()])
        elif isinstance(val, str) and val:
            keys.extend([k.strip() for k in val.split(",") if k.strip()])
    except Exception:
        pass
    ds_ten_key = [
        "GEMINI_API_KEY",
        "GEMINI_API_KEY_1",
        "GEMINI_API_KEY_2",
        "GEMINI_API_KEY_3"
    ]
    for k_name in ds_ten_key:
        k_val = get_secret(k_name)
        if k_val and str(k_val).strip() not in keys:
            keys.append(str(k_val).strip())
    return keys

GEMINI_KEYS = lay_danh_sach_gemini_keys()
DOLA_ENDPOINT = str(get_secret("DOLA_API_ENDPOINT")).strip()
DOLA_KEY = str(get_secret("DOLA_API_KEY")).strip()
DOLA_PROJECT_TIER = str(get_secret("DOLA_PROJECT_TIER", "high_limit_edu")).strip()
ADMIN_PASS = str(get_secret("ADMIN_PASSWORD", "")).strip()

# ==================== TẢI THƯ VIỆN BỔ TRỢ ====================
with st.spinner("🚀 Hệ thống đang khởi động..."):
    try:
        from streamlit_mic_recorder import speech_to_text
        HAS_MIC = True
    except Exception:
        HAS_MIC = False
    try:
        from gtts import gTTS
        HAS_TTS = True
    except Exception:
        HAS_TTS = False
    try:
        from PIL import Image
        HAS_PIL = True
    except Exception:
        HAS_PIL = False

# ==================== ĐẾM NGƯỜI DÙNG & GIỚI HẠN TẦN SUẤT ====================
def cap_nhat_nguoi_online():
    with GLOBALS["user_count_lock"]:
        if "user_id" not in st.session_state:
            st.session_state.user_id = str(uuid.uuid4())
        bo_nho = GLOBALS["online_users"]
        bo_nho[st.session_state.user_id] = time.time()
        now = time.time()
        ds_online = {
            uid: t for uid, t in bo_nho.items() if now - t < 300
        }
        bo_nho.clear()
        bo_nho.update(ds_online)
        return len(bo_nho)

def lay_gioi_han_toan_cuc():
    try:
        return max(1, int(get_secret("AI_MAX_PER_MINUTE", 30)))
    except Exception:
        return 30

def kiem_tra_gioi_han_tan_suat(cooldown_seconds=4):
    now = time.time()
    last_time = st.session_state.get("last_ai_request_time", 0.0)
    elapsed = now - last_time
    if elapsed < cooldown_seconds:
        return False, int(cooldown_seconds - elapsed) + 1
    gioi_han = lay_gioi_han_toan_cuc()
    with GLOBALS["rate_lock"]:
        hang_doi = GLOBALS["ai_request_times"]
        while hang_doi and now - hang_doi[0] > 60:
            hang_doi.popleft()
        if len(hang_doi) >= gioi_han:
            cho = int(60 - (now - hang_doi[0])) + 1
            return False, cho
        hang_doi.append(now)
    st.session_state["last_ai_request_time"] = now
    return True, 0

# ==================== BỘ ĐỆM AI ====================
def tao_ma_hash_cau_hoi(mon_hoc, bai_hoc, che_do, cau_hoi):
    c_clean = re.sub(r'\s+', ' ', cau_hoi.strip().lower())
    chuoi_chuan = f"{mon_hoc.strip()}_{bai_hoc.strip()}_{che_do}_{c_clean}"
    return hashlib.md5(chuoi_chuan.encode("utf-8")).hexdigest()

def luu_cache_ai(ma_hash, noi_dung):
    if not noi_dung or "⚠️" in noi_dung:
        return
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        cache[ma_hash] = noi_dung
        cache.move_to_end(ma_hash)
        if len(cache) > 100:
            cache.popitem(last=False)

def lay_cache_ai(ma_hash):
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        if ma_hash in cache:
            cache.move_to_end(ma_hash)
            return cache[ma_hash]
    return None

# ==================== CHẤM SỐ HỌC & TRỘN TRẮC NGHIỆM ====================
def ep_kieu_so_hoc(chuoi):
    s = str(chuoi).strip().replace(" ", "")
    if not s:
        return None
    if "/" in s:
        parts = s.split("/")
        if len(parts) == 2:
            try:
                return float(parts[0]) / float(parts[1])
            except Exception:
                return None
    if re.fullmatch(r'-?\d{1,3}(?:\.\d{3})*(?:,\d+)?', s):
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None

def so_sanh_so_hoc(nd, ds_dung):
    val_x = ep_kieu_so_hoc(nd)
    for d in ds_dung:
        val_d = ep_kieu_so_hoc(d)
        if val_x is not None and val_d is not None:
            if abs(val_x - val_d) < 1e-5:
                return True
        s1 = re.sub(r'\s+', '', str(nd).lower())
        s2 = re.sub(r'\s+', '', str(d).lower())
        if s1 == s2:
            return True
    return False

PHUONG_AN_CO_DINH = re.compile(
    r'\b(?:tất cả|cả hai|cả ba|cả [a-d]|đáp án|phương án)\b',
    re.IGNORECASE
)

def tron_dap_an_thong_minh(ch):
    da_goc = list(ch["da"])
    d_dung = da_goc[ch["d"]]
    co_dinh = [x for x in da_goc if PHUONG_AN_CO_DINH.search(str(x))]
    tu_do = [x for x in da_goc if x not in co_dinh]
    random.shuffle(tu_do)
    da_moi = tu_do + co_dinh
    return da_moi, da_moi.index(d_dung)

def giu_lua_chon_hop_le(key, ds_lua_chon):
    if key in st.session_state and st.session_state[key] not in ds_lua_chon:
        del st.session_state[key]

def lam_sach_id(s):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))

def sap_xep_chuong(ds_chuong):
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)

def ghi_nhan_lich_su(tieu_de_bai, diem, dung, tong, mon=None):
    if "lich_su_hoc_tap" not in st.session_state:
        st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {
        "bai": tieu_de_bai,
        "diem": diem,
        "dung": dung,
        "tong": tong,
        "mon": mon
    })

def thanh_tich_mon(mon):
    ds = [x for x in st.session_state.get("lich_su_hoc_tap", []) if x.get("mon") == mon]
    if not ds:
        return 0, None
    return len(ds), sum(x["diem"] for x in ds) / len(ds)

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def doc_to_an_toan(text, autoplay=True):
    if not HAS_TTS or not text:
        return
    try:
        clean_text = lam_sach_van_ban_doc(text)
        if clean_text:
            afp = io.BytesIO()
            gTTS(text=clean_text, lang="vi").write_to_fp(afp)
            afp.seek(0)
            st.audio(afp, format="audio/mp3", autoplay=autoplay)
    except Exception:
        pass

def trich_xuat_word_docx(file_bytes):
    try:
        with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
            xml_content = z.read("word/document.xml")
        tree = ET.fromstring(xml_content)
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        doan_van = [
            "".join([t.text for t in p.iter(f"{ns}t") if t.text])
            for p in tree.iter(f"{ns}p")
        ]
        return "\n".join([p for p in doan_van if p])
    except Exception as e:
        return f"[Lỗi đọc file Word: {e}]"

# ==================== GHI LOG LỖI ====================
def ghi_log_loi(nguon, loi):
    try:
        thong_bao = str(loi)
        for k in GEMINI_KEYS + [DOLA_KEY]:
            if k:
                thong_bao = thong_bao.replace(k, "***")
        print(f"[LỖI] {nguon}: {type(loi).__name__}: {thong_bao[:500]}", flush=True)
    except Exception:
        pass

# ==================== GỌI AI ====================
def goi_dola_toi_uu(cau_hoi):
    if not DOLA_ENDPOINT or not DOLA_KEY:
        return None
    try:
        phan_hoi = requests.post(
            DOLA_ENDPOINT,
            headers={
                "Authorization": f"Bearer {DOLA_KEY}",
                "X-Project-Quota-Tier": DOLA_PROJECT_TIER
            },
            json={
                "cau_hoi": cau_hoi,
                "chuong_trinh": "ket_noi_tri_thuc_lop7",
                "che_do": "chuan_sgk"
            },
            timeout=4.0
        )
        if phan_hoi.status_code == 200:
            nd = phan_hoi.json().get("noi_dung_chuan", "")
            return nd.strip() if nd else None
        return None
    except Exception:
        return None

MODEL_UU_TIEN = [
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-pro-preview",
]
TU_KHOA_MODEL_LOAI_TRU = (
    "tts", "image", "live", "embedding", "transcribe",
    "omni", "banana", "robotics", "audio"
)

@st.cache_resource(show_spinner=False)
def lay_client_gemini(api_key):
    return genai.Client(api_key=api_key)

@st.cache_resource(ttl=3600, show_spinner=False)
def lay_ds_model_kha_dung(api_key):
    try:
        client = lay_client_gemini(api_key)
        ds_hien_co = []
        for m in client.models.list():
            ten = (getattr(m, "name", "") or "").replace("models/", "")
            if "gemini" not in ten:
                continue
            if any(k in ten for k in TU_KHOA_MODEL_LOAI_TRU):
                continue
            hanh_dong = getattr(m, "supported_actions", None) or []
            if hanh_dong and "generateContent" not in hanh_dong:
                continue
            ds_hien_co.append(ten)
        if ds_hien_co:
            kq = [m for m in MODEL_UU_TIEN if m in ds_hien_co]
            kq += [m for m in ds_hien_co if m not in MODEL_UU_TIEN]
            return kq
    except Exception as e:
        ghi_log_loi("Liệt kê model Gemini", e)
    return list(MODEL_UU_TIEN)

def chuyen_lich_su_gemini(history):
    ds = []
    for h in history or []:
        cac_phan = [
            types.Part.from_text(text=str(p))
            for p in h.get("parts", []) if str(p).strip()
        ]
        if cac_phan:
            ds.append(types.Content(role=h["role"], parts=cac_phan))
    return ds

def goi_gemini_an_toan(payload, system_instruction, history=None, tra_ve_json=False):
    if not HAS_GENAI:
        raise RuntimeError("Server chưa cài thư viện google-genai.")
    if not GEMINI_KEYS:
        raise RuntimeError("Chưa cấu hình GEMINI_API_KEY.")
    if "key_index" not in st.session_state:
        st.session_state["key_index"] = 0
    so_luong_key = len(GEMINI_KEYS)
    if tra_ve_json:
        cau_hinh = types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json"
        )
    else:
        cau_hinh = types.GenerateContentConfig(system_instruction=system_instruction)
    lich_su = chuyen_lich_su_gemini(history) if history is not None else None
    last_err = None
    for k_offset in range(so_luong_key):
        idx = (st.session_state["key_index"] + k_offset) % so_luong_key
        current_key = GEMINI_KEYS[idx]
        client = lay_client_gemini(current_key)
        ds_models = lay_ds_model_kha_dung(current_key)
        for ten_m in ds_models:
            for attempt in range(2):
                try:
                    if lich_su is not None:
                        chat_s = client.chats.create(
                            model=ten_m,
                            config=cau_hinh,
                            history=lich_su
                        )
                        txt = chat_s.send_message(payload).text
                    else:
                        txt = client.models.generate_content(
                            model=ten_m,
                            contents=payload,
                            config=cau_hinh
                        ).text
                    if not txt:
                        raise RuntimeError("Model trả về phản hồi rỗng.")
                    st.session_state["key_index"] = idx
                    return txt
                except genai_errors.APIError as e:
                    last_err = e
                    ghi_log_loi(f"Gemini [{ten_m}] key#{idx}", e)
                    if getattr(e, "code", None) == 429 and attempt == 0:
                        time.sleep(1.0)
                        continue
                    break
                except Exception as e:
                    last_err = e
                    ghi_log_loi(f"Gemini [{ten_m}] key#{idx}", e)
                    break
    raise last_err or RuntimeError("Không có model Gemini khả dụng.")

# ==================== KIỂM TRA DỮ LIỆU BÀI HỌC ====================
def tach_json_tu_van_ban(van_ban):
    s = str(van_ban).strip()
    s = re.sub(r'^```(?:json)?\s*|\s*```$', '', s)
    dau, cuoi = s.find("{"), s.rfind("}")
    if dau == -1 or cuoi <= dau:
        raise ValueError("Không tìm thấy dữ liệu JSON trong phản hồi của AI.")
    return json.loads(s[dau:cuoi + 1])

def chuan_hoa_bai_hoc(du_lieu):
    if not isinstance(du_lieu, dict):
        raise ValueError("Dữ liệu phải là một đối tượng (dictionary).")
    canh_bao = []
    bai = {
        "ly_thuyet": str(du_lieu.get("ly_thuyet", "")).strip(),
        "vi_du": str(du_lieu.get("vi_du", "")).strip(),
        "cau_hoi": [],
        "bt_co_ban": [],
        "bt_nang_cao": [],
    }
    if not bai["ly_thuyet"]:
        canh_bao.append("Thiếu phần lý thuyết.")
    for i, ch in enumerate(du_lieu.get("cau_hoi") or [], 1):
        if not isinstance(ch, dict):
            canh_bao.append(f"Câu trắc nghiệm {i}: sai định dạng, đã bỏ qua.")
            continue
        nd = str(ch.get("nd", "")).strip()
        da = [str(x).strip() for x in (ch.get("da") or []) if str(x).strip()]
        try:
            d = int(ch.get("d", -1))
        except (TypeError, ValueError):
            d = -1
        if not nd or len(da) < 2 or not (0 <= d < len(da)):
            canh_bao.append(f"Câu trắc nghiệm {i}: thiếu đề, thiếu phương án hoặc sai chỉ số đáp án, đã bỏ qua.")
            continue
        if len(set(da)) != len(da):
            canh_bao.append(f"Câu trắc nghiệm {i}: có phương án trùng nhau, đã bỏ qua.")
            continue
        cau = {"nd": nd, "da": da, "d": d}
        if str(ch.get("gt", "")).strip():
            cau["gt"] = str(ch["gt"]).strip()
        md = str(ch.get("md", "")).strip()
        if md in ("biet", "hieu", "van_dung"):
            cau["md"] = md
        elif md:
            canh_bao.append(f"Câu trắc nghiệm {i}: mức độ '{md}' không hợp lệ, đã bỏ trường này.")
        bai["cau_hoi"].append(cau)
    for nhom in ("bt_co_ban", "bt_nang_cao"):
        for i, bt in enumerate(du_lieu.get(nhom) or [], 1):
            if not isinstance(bt, dict) or not str(bt.get("de", "")).strip():
                canh_bao.append(f"{nhom} {i}: thiếu đề bài, đã bỏ qua.")
                continue
            dd = bt.get("dd", [])
            if isinstance(dd, (str, int, float)):
                dd = [dd]
            dd = [str(x).strip() for x in dd if str(x).strip()]
            if not dd:
                canh_bao.append(f"{nhom} {i}: thiếu đáp án/gợi ý (dd).")
            bai_tap = {
                "de": str(bt["de"]).strip(),
                "dd": dd or [""],
                "lg": str(bt.get("lg", "")).strip(),
            }
            for truong in ("gt", "hd"):
                if str(bt.get(truong, "")).strip():
                    bai_tap[truong] = str(bt[truong]).strip()
            if bt.get("kieu") == "tu_luan":
                bai_tap["kieu"] = "tu_luan"
            bai[nhom].append(bai_tap)
    return bai, canh_bao

# ==================== NẠP DỮ LIỆU CÁC MÔN ====================
try:
    from data_toan import TOAN
except ImportError:
    TOAN = {}
try:
    from data_vatly import VATLY
except ImportError:
    VATLY = {}
try:
    from data_hoa import HOA
except ImportError:
    HOA = {}

VAN_DEFAULT = {
    "Lớp 7": {
        "Bài 1: Bầu trời tuổi thơ (Truyện)": {
            "Văn bản 1: Bầy chim chìa vôi (Nguyễn Quang Thiều)": {
                "ly_thuyet": (
                    "Truyện kể về hai anh em Mon và Mên. Giữa đêm mưa, nước sông dâng lên, "
                    "hai anh em thao thức lo cho bầy chim chìa vôi non làm tổ trên bãi cát giữa sông. "
                    "Các em chèo đò ra bãi và được chứng kiến khoảnh khắc bầy chim non bay lên "
                    "khỏi mặt nước. Truyện được kể theo ngôi thứ ba, thể hiện tình yêu thương loài vật "
                    "và tâm hồn trong sáng, nhân hậu của trẻ thơ."
                ),
                "vi_du": (
                    "Chi tiết hai anh em không ngủ được, lo bầy chim non bị nước cuốn trôi, "
                    "cho thấy sự quan tâm chân thành của trẻ em với những sinh linh nhỏ bé."
                ),
                "cau_hoi": [
                    {
                        "nd": "Truyện 'Bầy chim chìa vôi' là của tác giả nào?",
                        "da": ["Đoàn Giỏi", "Nguyễn Quang Thiều", "Võ Quảng", "Tô Hoài"],
                        "d": 1
                    },
                    {
                        "nd": "Hai nhân vật chính trong truyện là ai?",
                        "da": ["An và Cò", "Hoài và Ý", "Mon và Mên", "Dế Mèn và Dế Choắt"],
                        "d": 2
                    },
                    {
                        "nd": "Truyện 'Bầy chim chìa vôi' được kể theo ngôi thứ mấy?",
                        "da": ["Ngôi thứ ba", "Ngôi thứ nhất", "Ngôi thứ hai", "Kết hợp ngôi thứ nhất và thứ hai"],
                        "d": 0
                    },
                    {
                        "nd": "Điều gì khiến hai anh em lo lắng giữa đêm?",
                        "da": [
                            "Trời sắp sáng mà chưa làm xong việc nhà",
                            "Con đò bị nước cuốn trôi",
                            "Nước sông dâng, bầy chim chìa vôi non có thể bị chết đuối",
                            "Bố mẹ đi vắng chưa về"
                        ],
                        "d": 2
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Tìm những chi tiết cho thấy hai anh em lo lắng cho bầy chim chìa vôi.",
                        "dd": ["Thao thức giữa đêm, bàn cách cứu bầy chim, chèo đò ra bãi sông"],
                        "lg": "Chú ý lời đối thoại giữa đêm của hai anh em và hành động chèo đò ra bãi sông."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Em có nhận xét gì về tính cách của Mon và Mên qua câu chuyện?",
                        "dd": ["Hồn nhiên, giàu tình yêu thương, biết quan tâm đến loài vật"],
                        "lg": "So sánh cách nói, cách hành động của người anh và người em; cả hai đều có tấm lòng nhân hậu."
                    }
                ]
            },
            "Văn bản 2: Đi lấy mật (trích 'Đất rừng phương Nam' – Đoàn Giỏi)": {
                "ly_thuyet": (
                    "Đoạn trích kể về chuyến đi lấy mật ong trong rừng U Minh của An cùng tía nuôi "
                    "và thằng Cò. Truyện kể theo ngôi thứ nhất qua lời của An, giúp người đọc cảm nhận "
                    "vẻ đẹp hoang sơ của rừng phương Nam, nghề lấy mật bằng cách gác kèo ong của người dân "
                    "và tình cảm gắn bó trong gia đình nuôi của An."
                ),
                "vi_du": (
                    "Qua cái nhìn tò mò, hồn nhiên của An, cảnh rừng và công việc lấy mật hiện lên "
                    "sinh động, gần gũi."
                ),
                "cau_hoi": [
                    {
                        "nd": "Đoạn trích 'Đi lấy mật' được trích từ tác phẩm nào?",
                        "da": ["Dế Mèn phiêu lưu kí", "Đất rừng phương Nam", "Tuổi thơ dữ dội", "Quê nội"],
                        "d": 1
                    },
                    {
                        "nd": "Người kể chuyện trong đoạn trích 'Đi lấy mật' là ai?",
                        "da": ["Thằng Cò", "Tía nuôi", "Má nuôi", "An"],
                        "d": 3
                    },
                    {
                        "nd": "Chuyến đi lấy mật diễn ra ở đâu?",
                        "da": ["Rừng U Minh", "Rừng Cúc Phương", "Tây Nguyên", "Rừng Sác"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Đoạn trích được kể theo ngôi thứ mấy? Tác dụng của ngôi kể đó là gì?",
                        "dd": ["Ngôi thứ nhất"],
                        "lg": "An xưng 'tôi', kể lại trực tiếp những điều mình thấy, nghe, cảm nhận, giúp câu chuyện chân thực, gần gũi."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Qua đoạn trích, em hiểu gì về thiên nhiên và con người vùng rừng U Minh?",
                        "dd": ["Thiên nhiên hoang sơ, giàu có; con người am hiểu rừng, gắn bó với thiên nhiên"],
                        "lg": "Chú ý cảnh rừng qua cái nhìn của An và cách người dân gác kèo để nuôi ong, lấy mật."
                    }
                ]
            },
            "Văn bản 3: Ngàn sao làm việc (Võ Quảng)": {
                "ly_thuyet": (
                    "Bài thơ của Võ Quảng mở rộng chủ đề tuổi thơ. Qua trí tưởng tượng hồn nhiên, "
                    "những vì sao trên bầu trời đêm hiện lên như đang làm việc, gợi niềm vui "
                    "và vẻ đẹp của thế giới quanh ta."
                ),
                "cau_hoi": [
                    {
                        "nd": "Bài thơ 'Ngàn sao làm việc' là của tác giả nào?",
                        "da": ["Thanh Thảo", "Nguyễn Khoa Điềm", "Võ Quảng", "Nguyễn Quang Thiều"],
                        "d": 2
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Biện pháp tu từ nào giúp những vì sao trong bài thơ trở nên sinh động như con người?",
                        "dd": ["Nhân hóa"],
                        "lg": "Các vì sao được gán cho hoạt động của con người: làm việc."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Vì sao bài thơ được xếp chung chủ đề 'Bầu trời tuổi thơ'?",
                        "dd": ["Cái nhìn hồn nhiên, giàu tưởng tượng của tuổi thơ"],
                        "lg": "Liên hệ với cách hai văn bản thể hiện thế giới qua đôi mắt trẻ thơ."
                    }
                ]
            }
        },
        "Bài 2: Khúc nhạc tâm hồn (Thơ bốn chữ, năm chữ)": {
            "Văn bản 1: Đồng dao mùa xuân (Nguyễn Khoa Điềm)": {
                "ly_thuyet": (
                    "Bài thơ viết theo thể thơ bốn chữ, mang âm hưởng đồng dao, kể về cuộc đời "
                    "một người lính trẻ đã hi sinh. Hình ảnh người lính hiện lên bình dị, trong sáng "
                    "và trở nên bất tử, trẻ mãi trong lòng quê hương, nhân dân."
                ),
                "vi_du": (
                    "Nhan đề gắn 'đồng dao' với 'mùa xuân': mùa xuân gợi tuổi trẻ và niềm hi vọng, "
                    "đồng dao gợi sự hồn nhiên, giản dị."
                ),
                "cau_hoi": [
                    {
                        "nd": "Bài thơ 'Đồng dao mùa xuân' được viết theo thể thơ nào?",
                        "da": ["Thơ năm chữ", "Thơ bốn chữ", "Thơ lục bát", "Thơ tự do"],
                        "d": 1
                    },
                    {
                        "nd": "Bài thơ 'Đồng dao mùa xuân' viết về ai?",
                        "da": ["Người mẹ quê", "Người thầy giáo", "Người lính trẻ", "Em bé chăn trâu"],
                        "d": 2
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Nhan đề 'Đồng dao mùa xuân' có ý nghĩa gì?",
                        "dd": ["Khúc hát hồn nhiên về tuổi xuân bất tử của người lính"],
                        "lg": "Mùa xuân gợi tuổi trẻ, hi vọng; đồng dao gợi sự trong trẻo, giản dị."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Viết đoạn văn 5–7 câu nêu cảm nghĩ của em về người lính trong bài thơ.",
                        "dd": ["Trân trọng, biết ơn sự hi sinh của người lính"],
                        "lg": "Nêu ấn tượng về vẻ đẹp giản dị, trẻ trung và sự hi sinh thầm lặng của người lính."
                    }
                ]
            },
            "Văn bản 2: Gặp lá cơm nếp (Thanh Thảo)": {
                "ly_thuyet": (
                    "Bài thơ viết theo thể thơ năm chữ. Người con là người lính xa nhà, tình cờ gặp "
                    "lá cơm nếp mà nhớ mẹ, nhớ nồi xôi và hương vị quê nhà. Tình yêu mẹ hòa quyện "
                    "với tình yêu quê hương, đất nước."
                ),
                "cau_hoi": [
                    {
                        "nd": "Bài thơ 'Gặp lá cơm nếp' được viết theo thể thơ nào?",
                        "da": ["Thơ bốn chữ", "Thơ bảy chữ", "Thơ năm chữ", "Thơ song thất lục bát"],
                        "d": 2
                    },
                    {
                        "nd": "Hình ảnh lá cơm nếp khơi gợi trong người con nỗi nhớ về ai?",
                        "da": ["Người mẹ", "Người bạn", "Người thầy", "Đồng đội"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Em có nhận xét gì về cách dùng từ 'gặp' trong nhan đề bài thơ?",
                        "dd": ["Gợi sự tình cờ, thân thiết như gặp lại người thân"],
                        "lg": "Từ 'gặp' khiến chiếc lá như một người quen cũ, gợi cả nỗi nhớ quê nhà."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Phân tích sự hòa quyện giữa tình yêu mẹ và tình yêu đất nước trong bài thơ.",
                        "dd": ["Nhớ mẹ gắn liền với nhớ quê hương, đất nước"],
                        "lg": "Từ kỉ niệm riêng về mẹ, người con mở rộng thành tình cảm với quê hương, đất nước."
                    }
                ]
            },
            "Văn bản 3: Trở gió (Nguyễn Ngọc Tư)": {
                "ly_thuyet": (
                    "Tùy bút viết về mùa gió chướng ở miền Tây Nam Bộ. Gió chướng về báo hiệu cuối năm, "
                    "Tết đến gần, gợi niềm vui, nỗi nhớ và tình cảm gắn bó của tác giả với quê hương."
                ),
                "cau_hoi": [
                    {
                        "nd": "'Trở gió' thuộc thể loại nào?",
                        "da": ["Truyện ngắn", "Thơ năm chữ", "Tùy bút", "Truyện ngụ ngôn"],
                        "d": 2
                    },
                    {
                        "nd": "Loại gió được nói đến trong văn bản 'Trở gió' là gió gì?",
                        "da": ["Gió mùa đông bắc", "Gió chướng", "Gió Lào", "Gió heo may"],
                        "d": 1
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Gió chướng được tác giả miêu tả qua những chi tiết, hình ảnh nào?",
                        "dd": ["Qua cảnh vật, con người và không khí cuối năm"],
                        "lg": "Tìm các chi tiết về cây cối, mặt sông, con người khi gió chướng về."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Qua 'Trở gió', em cảm nhận được tình cảm gì của tác giả với quê hương?",
                        "dd": ["Yêu thương, gắn bó sâu nặng với quê hương"],
                        "lg": "Chú ý những cảm xúc của tác giả khi gió chướng về và nỗi nhớ gắn với quê nhà."
                    }
                ]
            }
        }
    }
}
try:
    from data_van import VAN as VAN_EXT
    if VAN_EXT and "Lớp 7" in VAN_EXT:
        for ch_k, ch_v in VAN_DEFAULT["Lớp 7"].items():
            if ch_k not in VAN_EXT["Lớp 7"]:
                VAN_EXT["Lớp 7"][ch_k] = ch_v
        VAN = VAN_EXT
    else:
        VAN = VAN_DEFAULT
except ImportError:
    VAN = VAN_DEFAULT

DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA if HOA else {"Lớp 7": {"Chương 1: Đang cập nhật": {}}},
    "📖 Môn Ngữ Văn": VAN
}

DANH_MUC_THI_NGHIEM = {
    "📐 Môn Toán": {
        "⚖️ Cân bằng phương trình & Biểu thức đại số": "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_vi.html"
    },
    "🔬 Môn Vật lý (KHTN)": {
        "🔊 Sóng âm – độ to và độ cao của âm": "https://phet.colorado.edu/sims/html/waves-intro/latest/waves-intro_vi.html",
        "💡 Phản xạ ánh sáng": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_vi.html",
        "🧲 Nam châm & từ trường": "https://phet.colorado.edu/sims/html/faradays-electromagnetic-lab/latest/faradays-electromagnetic-lab_vi.html"
    },
    "🧪 Môn Hóa học (KHTN)": {
        "⚛️ Xây dựng cấu tạo Nguyên tử": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_vi.html",
        "🧬 Lắp ghép Phân tử": "https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_vi.html"
    },
    "📖 Môn Ngữ Văn": {
        "🗺️ Bản đồ Cấu trúc & Bối cảnh": "van_hoc_cau_truc",
        "🎭 Biểu đồ Tương tác Nhân vật": "van_hoc_nhan_vat",
        "🕸️ Sơ đồ Quan hệ Nhân vật": "van_hoc_quan_he",
        "✍️ Thực hành Luyện từ & Ngữ pháp": "van_hoc_ngu_phap",
        "📝 Trạm Lập dàn ý bài văn": "van_hoc_dan_y"
    }
}

DATA_LAB_NGU_VAN = {
    "🗺️ Bản đồ Cấu trúc & Bối cảnh": {
        "tieu_de": "Bản đồ Cấu trúc: Bầy chim chìa vôi",
        "khai_quat": "Truyện ngắn của Nguyễn Quang Thiều về tuổi thơ ở làng quê ven sông, kể theo ngôi thứ ba.",
        "bo_cuc": [
            {"phan": "Phần 1", "noi_dung": "Giữa đêm, hai anh em thức giấc, trò chuyện và lo lắng cho bầy chim chìa vôi non khi nước sông dâng."},
            {"phan": "Phần 2", "noi_dung": "Hai anh em quyết định chèo đò ra bãi sông."},
            {"phan": "Phần 3", "noi_dung": "Hai anh em chứng kiến bầy chim non bay lên khỏi mặt nước."}
        ],
        "y_nghia": "Ngợi ca tâm hồn trong sáng, nhân hậu của trẻ thơ và tình yêu thương đối với loài vật, thiên nhiên."
    },
    "🎭 Biểu đồ Tương tác Nhân vật": {
        "nhan_vat": "Hai anh em Mon và Mên",
        "dac_diem": "Hồn nhiên, giàu tình yêu thương, biết quan tâm đến những sinh linh nhỏ bé.",
        "hanh_vi_tieu_bieu": "Thao thức giữa đêm vì lo cho bầy chim; cùng nhau chèo đò ra bãi sông.",
        "dien_bien_tam_ly": [
            {"giai_doan": "Giữa đêm", "tam_trang": "Bồn chồn, lo lắng cho bầy chim non."},
            {"giai_doan": "Trên đường ra bãi sông", "tam_trang": "Hồi hộp, quyết tâm."},
            {"giai_doan": "Khi bầy chim bay lên", "tam_trang": "Vỡ òa xúc động, vui mừng."}
        ]
    },
    "🕸️ Sơ đồ Quan hệ Nhân vật": {
        "tac_pham": "Quan hệ trong 'Bầy chim chìa vôi'",
        "quan_he": [
            {"tu_khoa": "Mon ↔️ Mên", "loai": "Anh em", "mo_ta": "Cùng chung nỗi lo, cùng hành động để giúp bầy chim."},
            {"tu_khoa": "Hai anh em ↔️ Bầy chim chìa vôi", "loai": "Yêu thương, che chở", "mo_ta": "Tình cảm hồn nhiên, nhân hậu của trẻ thơ với loài vật."}
        ]
    },
    "✍️ Thực hành Luyện từ & Ngữ pháp": {
        "chu_de": "Biện pháp tu từ",
        "cau_hoi_mau": [
            {"cau": "Bầy chim non bay vút lên như những mũi tên nhỏ.", "loai": "So sánh", "phan_tich": "Làm nổi bật sự nhanh nhẹn, mạnh mẽ của bầy chim non."},
            {"cau": "Những ngôi sao thức suốt đêm, chăm chỉ làm việc trên bầu trời.", "loai": "Nhân hóa", "phan_tich": "Làm các vì sao trở nên gần gũi, sinh động như con người."}
        ]
    },
    "📝 Trạm Lập dàn ý bài văn": {
        "the_loai": "Phân tích đặc điểm nhân vật trong một tác phẩm văn học",
        "dan_y": [
            {"buoc": "Mở bài", "noi_dung": "Giới thiệu tác phẩm, tác giả, nhân vật và nêu nhận xét khái quát về nhân vật."},
            {"buoc": "Thân bài", "noi_dung": "Lần lượt phân tích từng đặc điểm của nhân vật; mỗi đặc điểm có bằng chứng từ văn bản."},
            {"buoc": "Kết bài", "noi_dung": "Khẳng định ý nghĩa của nhân vật và nêu cảm nghĩ của em."}
        ]
    }
}

# ==================== BỘ GIAO DIỆN THEO MÔN HỌC ====================
CHU_DE_GIAO_DIEN = {
    "toan": {
        "icon": "📐", "ten": "Môn Toán",
        "sang": ("#1E3A8A", "#2563EB", "#0284C7"),
        "toi": ("#172554", "#1E40AF", "#075985"),
        "nhan": "#FDE047", "chinh": "#2563EB",
        "khau_hieu": "Tư duy logic – Giải mã những con số",
        "ky_hieu": ["π", "√", "∑", "÷", "×", "∞", "△", "x²"],
        "loi_nhan": [
            "Mỗi bài toán khó là một câu đố đang chờ em giải mã!",
            "Sai một bước không sao – tìm ra vì sao sai là em đã tiến thêm một bước.",
            "Toán không phải để học thuộc, mà để hiểu và suy luận.",
            "Kiên nhẫn từng dòng tính, đáp án sẽ tự hiện ra.",
        ],
    },
    "vatly": {
        "icon": "🔬", "ten": "Vật lý (KHTN)",
        "sang": ("#1E1B4B", "#4C1D95", "#7C3AED"),
        "toi": ("#0F0A2E", "#2E1065", "#5B21B6"),
        "nhan": "#FACC15", "chinh": "#7C3AED",
        "khau_hieu": "Khám phá quy luật của thế giới quanh em",
        "ky_hieu": ["⚡", "🔭", "🧲", "💡", "∿", "v = s/t", "🔊", "☀️"],
        "loi_nhan": [
            "Mọi hiện tượng quanh em đều có một lời giải thích khoa học.",
            "Hãy hỏi “Tại sao?” – đó là bước đầu của mọi nhà khoa học.",
            "Quan sát kĩ, đo cẩn thận, kết luận trung thực.",
            "Âm thanh, ánh sáng, nam châm… thế giới đang chờ em khám phá!",
        ],
    },
    "hoa": {
        "icon": "🧪", "ten": "Hóa học (KHTN)",
        "sang": ("#064E3B", "#047857", "#0D9488"),
        "toi": ("#022C22", "#065F46", "#115E59"),
        "nhan": "#A3E635", "chinh": "#059669",
        "khau_hieu": "Bước vào thế giới của nguyên tử và phân tử",
        "ky_hieu": ["⚛", "H₂O", "O₂", "CO₂", "⚗️", "🧬", "NaCl", "🔬"],
        "loi_nhan": [
            "Mọi vật quanh em đều được tạo nên từ những nguyên tử bé xíu.",
            "Thí nghiệm hôm nay, phát minh ngày mai!",
            "Hiểu cấu tạo nguyên tử là nắm chìa khóa của Hóa học.",
            "An toàn trước, tò mò sau – nhà hóa học nhí luôn cẩn thận.",
        ],
    },
    "van": {
        "icon": "📖", "ten": "Môn Ngữ văn",
        "sang": ("#881337", "#BE123C", "#C2410C"),
        "toi": ("#4C0519", "#881337", "#9A3412"),
        "nhan": "#FDE68A", "chinh": "#E11D48",
        "khau_hieu": "Mỗi trang sách mở ra một chân trời",
        "ky_hieu": ["✒️", "❝", "❞", "📜", "🌸", "Aa", "🍃", "✍️"],
        "loi_nhan": [
            "Mỗi trang sách mở ra một chân trời mới.",
            "Đọc chậm một chút, em sẽ nghe thấy tiếng lòng của nhân vật.",
            "Viết bằng cả trái tim, em sẽ chạm tới trái tim người đọc.",
            "Một câu văn hay bắt đầu từ một cảm xúc thật.",
        ],
    },
    "home": {
        "icon": "🎓", "ten": "Hệ thống học tập lớp 7",
        "sang": ("#3730A3", "#6D28D9", "#DB2777"),
        "toi": ("#1E1B4B", "#4C1D95", "#831843"),
        "nhan": "#FDE047", "chinh": "#6D28D9",
   "khau_hieu": "Kết nối tri thức với cuộc sống · Chương trình GDPT",
    "ten_khac": "Giá trị khác"
}
