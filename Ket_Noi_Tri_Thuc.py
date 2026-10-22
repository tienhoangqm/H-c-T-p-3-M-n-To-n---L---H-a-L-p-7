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

# ==================== TƯƠNG THÍCH KÉP THƯ VIỆN GEMINI ====================
HAS_NEW_GENAI = False
HAS_LEGACY_GENAI = False
genai = types = genai_errors = legacy_genai = None

try:
    from google import genai
    from google.genai import types
    from google.genai import errors as genai_errors
    HAS_NEW_GENAI = True
except Exception:
    pass

try:
    import google.generativeai as legacy_genai
    HAS_LEGACY_GENAI = True
except Exception:
    pass

HAS_GENAI = HAS_NEW_GENAI or HAS_LEGACY_GENAI

# ==================== CẤU HÌNH TRANG & ĐIỀU HƯỚNG SỚM ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "home_jump" in st.session_state:
    st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
    st.session_state["mon_main"] = st.session_state.pop("home_jump")

if "search_jump" in st.session_state:
    item = st.session_state.pop("search_jump")
    st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
    st.session_state["mon_main"] = item["mon"]
    if "lop" in item:
        st.session_state["s_lop"] = item["lop"]
    st.session_state["s_chuong"] = item["chuong"]
    st.session_state["s_bai"] = item["bai"]

# ==================== KHỞI TẠO LOCK & CACHE TOÀN CỤC ====================
@st.cache_resource
def get_global_locks():
    return {
        "ai_api_lock": threading.Lock(),
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
    nd_lower = noi_dung.lower()
    tu_khoa_loi = ["bận", "quá tải", "lỗi", "chuyển sang", "bảo trì"]
    if any(k in nd_lower for k in tu_khoa_loi):
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
    if co_dinh:
        return da_goc, ch["d"]
    tu_do = list(da_goc)
    random.shuffle(tu_do)
    return tu_do, tu_do.index(d_dung)

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
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro",
]
TU_KHOA_MODEL_LOAI_TRU = (
    "tts", "image", "live", "embedding", "transcribe",
    "omni", "banana", "robotics", "audio"
)

@st.cache_resource(show_spinner=False)
def lay_client_gemini(api_key):
    if HAS_NEW_GENAI:
        return genai.Client(api_key=api_key)
    return None

@st.cache_resource(ttl=3600, show_spinner=False)
def lay_ds_model_kha_dung(api_key):
    try:
        if HAS_NEW_GENAI:
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
        elif HAS_LEGACY_GENAI:
            legacy_genai.configure(api_key=api_key)
            ds_hien_co = [
                m.name.replace("models/", "")
                for m in legacy_genai.list_models()
                if "generateContent" in getattr(m, "supported_generation_methods", [])
                and not any(k in m.name for k in TU_KHOA_MODEL_LOAI_TRU)
            ]
            if ds_hien_co:
                kq = [m for m in MODEL_UU_TIEN if m in ds_hien_co]
                kq += [m for m in ds_hien_co if "gemini" in m and m not in MODEL_UU_TIEN]
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
        raise RuntimeError("Server chưa cài thư viện google-genai hoặc google-generativeai.")
    if not GEMINI_KEYS:
        raise RuntimeError("Chưa cấu hình GEMINI_API_KEY.")
    if "key_index" not in st.session_state:
        st.session_state["key_index"] = 0
    so_luong_key = len(GEMINI_KEYS)
    last_err = None

    if HAS_NEW_GENAI:
        if tra_ve_json:
            cau_hinh = types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json"
            )
        else:
            cau_hinh = types.GenerateContentConfig(system_instruction=system_instruction)
        lich_su = chuyen_lich_su_gemini(history) if history is not None else None

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
                    except Exception as e:
                        last_err = e
                        ghi_log_loi(f"Gemini [{ten_m}] key#{idx}", e)
                        err_code = getattr(e, "code", None)
                        if (err_code == 429 or "429" in str(e)) and attempt == 0:
                            time.sleep(1.0)
                            continue
                        break

    if HAS_LEGACY_GENAI:
        with GLOBALS["ai_api_lock"]:
            for k_offset in range(so_luong_key):
                idx = (st.session_state["key_index"] + k_offset) % so_luong_key
                current_key = GEMINI_KEYS[idx]
                legacy_genai.configure(api_key=current_key)
                ds_models = lay_ds_model_kha_dung(current_key)
                for ten_m in ds_models:
                    for attempt in range(2):
                        try:
                            m = legacy_genai.GenerativeModel(
                                model_name=ten_m,
                                system_instruction=system_instruction
                            )
                            if history is not None:
                                chat_s = m.start_chat(history=history)
                                txt = chat_s.send_message(payload).text
                            else:
                                txt = m.generate_content(payload).text
                            if not txt:
                                raise RuntimeError("Model trả về phản hồi rỗng.")
                            st.session_state["key_index"] = idx
                            return txt
                        except Exception as e:
                            last_err = e
                            ghi_log_loi(f"Legacy Gemini [{ten_m}] key#{idx}", e)
                            if "429" in str(e) and attempt == 0:
                                time.sleep(1.0)
                                continue
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

# ==================== BỘ GIAO DIỆN THEO MÔN HỌC (ĐÃ SỬA LỖI NGOẶC) ====================
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
        "khau_hieu": "Kết nối tri thức với cuộc sống · Chương trình GDPT 2018",
        "ky_hieu": ["🎓", "📐", "🔬", "🧪", "📖", "⭐", "🚀", "💡"],
        "loi_nhan": [
            "Chào mừng em đến với không gian học tập thông minh lớp 7!",
            "Học tập chủ động mỗi ngày giúp em tiến bộ vượt bậc.",
        ],
    },
}

def lay_chu_de_theo_mon(mon_str):
    s = str(mon_str).lower()
    if "toán" in s:
        return CHU_DE_GIAO_DIEN["toan"]
    if "vật lý" in s:
        return CHU_DE_GIAO_DIEN["vatly"]
    if "hóa" in s:
        return CHU_DE_GIAO_DIEN["hoa"]
    if "văn" in s:
        return CHU_DE_GIAO_DIEN["van"]
    return CHU_DE_GIAO_DIEN["home"]

# ==================== GIAO DIỆN SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    st.caption("Hệ thống Ôn luyện THCS — Lớp 7")
    dark_mode = st.toggle("🌙 Chế độ tối (Dark Mode)", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()} học sinh**")

    if not GEMINI_KEYS:
        st.warning("⚠️ Chưa cấu hình API Key, chạy ở chế độ Mẫu.")

    st.divider()

    ds_che_do = [
        "🏠 Trang chủ / Hướng dẫn",
        "🔍 Tra cứu / Tìm kiếm",
        "📖 Học theo chuyên đề",
        "📝 Phòng thi / Kiểm tra",
        "🎪 Phòng thí nghiệm ảo",
        "⚙️ Trạm Nạp Dữ Liệu"
    ]
    che_do = st.radio("⚙️ Chức năng:", ds_che_do, key="che_do_sidebar")

    if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
        st.divider()
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = che_do

    if "lich_su_hoc_tap" in st.session_state and st.session_state.lich_su_hoc_tap:
        st.divider()
        st.markdown("### 📊 Lịch sử học tập")
        so_bai = len(st.session_state.lich_su_hoc_tap)
        tb = sum(i["diem"] for i in st.session_state.lich_su_hoc_tap) / so_bai
        st.metric("Điểm Trung Bình", f"{tb:.1f} / 10", f"Đã luyện {so_bai} bài")

# ==================== CẤU HÌNH CSS ĐỘNG THEO CHỦ ĐỀ MÔN HỌC ====================
chu_de_hien_tai = lay_chu_de_theo_mon(mon)
mau_nen_gradient = chu_de_hien_tai["toi"] if dark_mode else chu_de_hien_tai["sang"]
mau_chinh = chu_de_hien_tai["chinh"]

if dark_mode:
    st.markdown(f"""
    <style>
        .stApp {{ background-color: #0F172A; color: #F1F5F9; }}
        .main .block-container {{ padding-top: 1.2rem; max-width: 95%; }}
        [data-testid="stToolbarActions"], footer {{ display: none !important; }}
        .hero-banner {{
            background: linear-gradient(135deg, {mau_nen_gradient[0]} 0%, {mau_nen_gradient[1]} 55%, {mau_nen_gradient[2]} 100%);
            color: #F8FAFC; padding: 1.5rem; border-radius: 14px;
            margin-bottom: 1.5rem; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.35);
        }}
        .hero-title {{ font-size: 1.55rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }}
        .hero-sub {{ font-size: 0.95rem; opacity: 0.92; margin-top: 0.35rem; color: #E2E8F0 !important; }}
        .card-home {{
            background-color: #1E293B; border: 1px solid #334155;
            padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; color: #F1F5F9;
        }}
        .khung-lythuyet {{
            background-color: #1E293B; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid {mau_chinh}; margin-bottom: 1rem;
        }}
        .khung-vidu {{
            background-color: #27272A; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #F59E0B; margin-bottom: 1rem;
        }}
        .dung {{ color: #34D399; font-weight: bold; }}
        .sai {{ color: #F87171; font-weight: bold; }}
        .diem-thi {{
            font-size: 1.6rem; color: #F87171; text-align: center;
            padding: 1.2rem; border: 2px dashed #EF4444; border-radius: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <style>
        .main .block-container {{ padding-top: 1.2rem; max-width: 95%; }}
        [data-testid="stToolbarActions"], footer {{ display: none !important; }}
        .hero-banner {{
            background: linear-gradient(135deg, {mau_nen_gradient[0]} 0%, {mau_nen_gradient[1]} 55%, {mau_nen_gradient[2]} 100%);
            color: white; padding: 1.5rem; border-radius: 14px;
            margin-bottom: 1.5rem; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.12);
        }}
        .hero-title {{ font-size: 1.55rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }}
        .hero-sub {{ font-size: 0.95rem; opacity: 0.95; margin-top: 0.35rem; color: #F1F5F9 !important; }}
        .card-home {{
            background-color: #F8FAFC; border: 1px solid #E2E8F0;
            padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem;
        }}
        .khung-lythuyet {{
            background-color: #EFF6FF; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid {mau_chinh}; margin-bottom: 1rem; color: #1E293B;
        }}
        .khung-vidu {{
            background-color: #FFFBEB; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #F59E0B; margin-bottom: 1rem; color: #1E293B;
        }}
        .dung {{ color: #059669; font-weight: bold; }}
        .sai {{ color: #DC2626; font-weight: bold; }}
        .diem-thi {{
            font-size: 1.6rem; color: #E11D48; text-align: center;
            padding: 1.2rem; border: 2px dashed #F43F5E; border-radius: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)

# ==================== HIỂN THỊ PHÒNG THÍ NGHIỆM & BÀI HỌC ====================
def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    if mon_hien_tai == "📖 Môn Ngữ Văn":
        ds_modul = list(DANH_MUC_THI_NGHIEM["📖 Môn Ngữ Văn"].keys())
        chon_modul = st.selectbox(
            "📚 Chọn Mô-đun Tương tác Ngữ Văn:",
            ds_modul,
            key=f"select_modul_{key_prefix}"
        )
        st.divider()
        if "Bản đồ Cấu trúc" in chon_modul:
            data = DATA_LAB_NGU_VAN["🗺️ Bản đồ Cấu trúc & Bối cảnh"]
            st.markdown(f"### 🗺️ {data['tieu_de']}")
            st.info(f"⏳ **Khái quát:** {data.get('khai_quat', '')}")
            for item in data["bo_cuc"]:
                with st.expander(f"🔹 {item['phan']}"):
                    st.write(item["noi_dung"])
            st.success(f"💡 **Ý nghĩa nhân văn:** {data['y_nghia']}")
        elif "Biểu đồ Tương tác" in chon_modul:
            data = DATA_LAB_NGU_VAN["🎭 Biểu đồ Tương tác Nhân vật"]
            st.markdown(f"### 🎭 {data['nhan_vat']}")
            st.markdown(f"⭐ **Đặc điểm:** {data['dac_diem']}")
            st.markdown(f"🎯 **Hành vi tiêu biểu:** {data['hanh_vi_tieu_bieu']}")
            st.markdown("#### 📈 Diễn biến tâm lý:")
            for stage in data["dien_bien_tam_ly"]:
                st.markdown(f"* **{stage['giai_doan']}:** {stage['tam_trang']}")
        elif "Sơ đồ Quan hệ" in chon_modul:
            data = DATA_LAB_NGU_VAN["🕸️ Sơ đồ Quan hệ Nhân vật"]
            st.markdown(f"### 🕸️ {data['tac_pham']}")
            for idx, rel in enumerate(data["quan_he"], 1):
                with st.expander(f"{idx}. {rel['tu_khoa']} — [{rel['loai']}]"):
                    st.write(rel["mo_ta"])
        elif "Luyện từ & Ngữ pháp" in chon_modul:
            data = DATA_LAB_NGU_VAN["✍️ Thực hành Luyện từ & Ngữ pháp"]
            st.markdown(f"### ✍️ {data['chu_de']}")
            for idx, bai in enumerate(data["cau_hoi_mau"], 1):
                st.markdown(f"**Câu {idx}:** `{bai['cau']}`")
                st.markdown(f"👉 **Phân loại:** **{bai['loai']}**")
                st.info(f"💡 **Giải thích:** {bai['phan_tich']}")
        elif "Lập dàn ý" in chon_modul:
            data = DATA_LAB_NGU_VAN["📝 Trạm Lập dàn ý bài văn"]
            st.markdown(f"### 📝 Lập dàn ý: {data['the_loai']}")
            for buoc in data["dan_y"]:
                with st.expander(f"📋 {buoc['buoc']}"):
                    st.text(buoc["noi_dung"])
    else:
        st.markdown("#### 🎪 Phòng Thí Nghiệm & Mô Phỏng (PhET Colorado)")
        ds_tn_mon = DANH_MUC_THI_NGHIEM.get(mon_hien_tai, {})
        if not ds_tn_mon:
            ds_tn_mon = DANH_MUC_THI_NGHIEM["🔬 Môn Vật lý (KHTN)"]
        ten_tn = st.selectbox(
            "🔬 Chọn mô phỏng thực hành:",
            list(ds_tn_mon.keys()),
            key=f"select_tn_{key_prefix}"
        )
        url_tn = ds_tn_mon[ten_tn]
        if url_tn:
            components.iframe(url_tn, height=580, scrolling=True)

def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    st.markdown(f"### 📖 {ten_bai}")
    lt = data.get("ly_thuyet", "").strip()
    vd = data.get("vi_du", "").strip()
    ch_list = data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Trắc nghiệm", f"{len(ch_list)} câu")
    c2.metric("✏️ Cơ bản", f"{len(bt_cb)} bài")
    c3.metric("🔥 Nâng cao", f"{len(bt_nc)} bài")

    ds_tabs = [
        "📚 Lý thuyết",
        "✏️ Cơ bản",
        "🔥 Nâng cao",
        "📝 Trắc nghiệm",
        "🎪 Phòng thí nghiệm"
    ]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(ds_tabs)

    with tab1:
        if lt:
            st.markdown(
                f"""<div class="khung-lythuyet">{lt}</div>""",
                unsafe_allow_html=True
            )
        if vd:
            st.markdown(
                f"""<div class="khung-vidu">{vd}</div>""",
                unsafe_allow_html=True
            )

    with tab2:
        if not bt_cb:
            st.info("Chưa có bài tập.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    if "Ngữ Văn" in mon or bt.get("kieu") == "tu_luan":
                        if st.button("💡 Xem gợi ý", key=f"btn_goiy_cb_{sid}_{i}"):
                            goi_y = bt.get("lg") or bt.get("dd", [""])[0]
                            st.info(f"📝 **Gợi ý:** {goi_y}")
                    else:
                        ans = st.text_input("Nhập kết quả:", key=f"cb_{sid}_{i}")
                        if st.button("Kiểm tra", key=f"btn_cb_{sid}_{i}"):
                            if not ans.strip():
                                st.warning("⚠️ Nhập đáp án trước!")
                            elif so_sanh_so_hoc(ans, bt["dd"]):
                                st.markdown(
                                    """<p class="dung">✅ Chính xác!</p>""",
                                    unsafe_allow_html=True
                                )
                            else:
                                da_mau = bt["dd"][0]
                                st.markdown(
                                    f"""<p class="sai">❌ Sai. Gợi ý: {da_mau}</p>""",
                                    unsafe_allow_html=True
                                )

    with tab3:
        if not bt_nc:
            st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                with st.expander(f"Bài nâng cao {i}: {nc['de'][:60]}..."):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    if "Ngữ Văn" in mon or nc.get("kieu") == "tu_luan":
                        if st.button("💡 Xem gợi ý", key=f"btn_goiy_nc_{sid}_{i}"):
                            goi_y = nc.get("lg") or nc.get("dd", [""])[0]
                            st.info(f"📝 **Gợi ý:** {goi_y}")
                    else:
                        ans = st.text_input("Nhập kết quả:", key=f"nc_{sid}_{i}")
                        if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                            if so_sanh_so_hoc(ans, nc["dd"]):
                                st.success("🎉 Chính xác!")
                            else:
                                st.error(f"❌ Gợi ý: {nc['dd'][0]}")
                        if st.checkbox("📖 Xem lời giải", key=f"lg_{sid}_{i}"):
                            st.success(f"**Lời giải:** {nc.get('lg', '')}")

    with tab4:
        if len(ch_list) == 0:
            st.info("Chưa có trắc nghiệm.")
        else:
            if st.button("🔄 Làm mới đề", key=f"btn_rf_{sid}"):
                st.session_state[f"de_{sid}"] = None
            if f"de_{sid}" not in st.session_state or st.session_state[f"de_{sid}"] is None:
                de_tron = []
                for ch in ch_list:
                    da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                    nd_ch = ch.get("nd") or ch.get("de")
                    de_tron.append({"nd": nd_ch, "da": da_moi, "d": vt_moi})
                st.session_state[f"de_{sid}"] = de_tron

            with st.form(f"f_{sid}"):
                tl = {}
                for i, ch in enumerate(st.session_state[f"de_{sid}"], 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl[i] = st.radio(
                        "Chọn:",
                        ch["da"],
                        key=f"r_{sid}_{i}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    st.markdown("---")
                if st.form_submit_button("🚀 Nộp bài", type="primary"):
                    de_hien_tai = st.session_state[f"de_{sid}"]
                    dung = sum(
                        1 for i, ch in enumerate(de_hien_tai, 1)
                        if tl[i] == ch["da"][ch["d"]]
                    )
                    diem = dung / len(ch_list) * 10
                    ghi_nhan_lich_su(f"Trắc nghiệm: {ten_bai}", diem, dung, len(ch_list), mon=mon)
                    st.markdown(
                        f"""<div class="diem-thi">🏆 ĐIỂM: {diem:.1f} / 10</div>""",
                        unsafe_allow_html=True
                    )
                    for i, ch in enumerate(de_hien_tai, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl[i] != da_dung:
                            st.error(f"Câu {i} sai. Đúng là: {da_dung}")
                        else:
                            st.success(f"Câu {i}: Đúng")

    with tab5:
        hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

# ==================== ĐIỀU HƯỚNG MÀN HÌNH CHÍNH ====================
bai_dang_hoc = ""
du_lieu_bai_hien_tai = {}

if che_do == "🏠 Trang chủ / Hướng dẫn":
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">🎓 HỆ THỐNG HỌC TẬP THCS — KẾT NỐI TRI THỨC (LỚP 7)</p>
        <p class="hero-sub">{CHU_DE_GIAO_DIEN["home"]["khau_hieu"]}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c1.markdown("""
    <div class="card-home">
        <h3>🌟 Không gian học tập đa môn</h3>
        <p>Tích hợp đầy đủ lý thuyết trọng tâm, bài tập cơ bản, nâng cao và phòng thí nghiệm tương tác cho Toán, Vật lý, Hóa học và Ngữ Văn lớp 7.</p>
    </div>
    """, unsafe_allow_html=True)
    c2.markdown("""
    <div class="card-home">
        <h3>💬 Trợ lý Gia Sư AI 24/7</h3>
        <p>Gợi mở tư duy theo phương pháp Socratic, hỗ trợ nhận diện ảnh bài tập và đọc giọng nói tiếng Việt tự nhiên.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 Chọn nhanh môn học")
    cols_mon = st.columns(4)
    for idx_m, ten_m in enumerate(DATABASE.keys()):
        with cols_mon[idx_m]:
            so_lan, diem_tb_m = thanh_tich_mon(ten_m)
            phu_de = f"Đã làm {so_lan} bài (TB: {diem_tb_m:.1f}đ)" if diem_tb_m is not None else "Bắt đầu ôn luyện ngay"
            st.info(f"**{ten_m}**\n\n{phu_de}")
            if st.button(f"Vào học {ten_m}", key=f"quick_jump_{idx_m}", use_container_width=True):
                st.session_state["home_jump"] = ten_m
                st.rerun()

elif che_do == "🔍 Tra cứu / Tìm kiếm":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🔍 Tra Cứu & Tìm Kiếm Tri Thức</p>
        <p class="hero-sub">Gõ từ khóa bất kỳ để tìm nhanh bài học trong toàn bộ hệ thống</p>
    </div>
    """, unsafe_allow_html=True)
    tu_khoa = st.text_input("🔎 Nhập từ khóa cần tìm:")
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        ket_qua_tim = []
        for t_mon, l_dict in DATABASE.items():
            for lop, c_dict in l_dict.items():
                for chuong, b_dict in c_dict.items():
                    for t_bai, data in b_dict.items():
                        lt_txt = data.get("ly_thuyet", "").lower()
                        if kw in t_bai.lower() or kw in lt_txt:
                            ket_qua_tim.append({
                                "mon": t_mon,
                                "lop": lop,
                                "chuong": chuong,
                                "bai": t_bai
                            })
        st.markdown(f"### 📋 Kết quả tìm kiếm: {len(ket_qua_tim)} bài học")
        for idx, item in enumerate(ket_qua_tim, 1):
            tieu_de_exp = f"{idx}. [{item['mon']}] {item['chuong']} — {item['bai']}"
            with st.expander(tieu_de_exp):
                if st.button("📖 Mở ngay bài học này", key=f"btn_jump_{idx}"):
                    st.session_state["search_jump"] = item
                    st.rerun()

elif che_do == "⚙️ Trạm Nạp Dữ Liệu":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">⚙️ Trạm Nạp Dữ Liệu Tự Động (Auto-Parser)</p>
        <p class="hero-sub">Công cụ dành riêng cho Quản trị viên bóc tách học liệu chuẩn hóa</p>
    </div>
    """, unsafe_allow_html=True)
    mk = st.text_input("🔑 Nhập mật khẩu Admin:", type="password")

    if not ADMIN_PASS:
        st.error("⚠️ Hệ thống chưa thiết lập ADMIN_PASSWORD trong Secrets.")
    elif mk:
        now_ts = time.time()
        with GLOBALS["admin_fail_lock"]:
            q_fail = GLOBALS["admin_fail_times"]
            while q_fail and now_ts - q_fail[0] > 300:
                q_fail.popleft()
            bi_khoa = len(q_fail) >= 5

        if bi_khoa:
            st.error("🚫 Nhập sai mật khẩu quá 5 lần. Vui lòng thử lại sau 5 phút.")
        elif hmac.compare_digest(mk, ADMIN_PASS):
            st.success("✅ Xác thực thành công. Hệ thống nạp file đã mở!")
            tab_upfile, tab_paste = st.tabs(["📁 Tải File Lên", "📝 Dán Văn Bản Thô"])
            danh_sach_files = []
            with tab_upfile:
                uploaded_files = st.file_uploader(
                    "Chọn file (docx, pdf, ảnh, txt):",
                    type=["docx", "pdf", "png", "jpg", "jpeg", "txt"],
                    accept_multiple_files=True
                )
                if uploaded_files:
                    danh_sach_files = uploaded_files
            with tab_paste:
                raw_text = st.text_area("Dán nội dung văn bản gốc vào đây:", height=220)

            PROMPT_PARSER = (
                'Chuyển đổi nội dung thành JSON chuẩn gồm các khóa: '
                '"ly_thuyet", "vi_du", "cau_hoi", "bt_co_ban", "bt_nang_cao".'
            )
            if st.button("⚡ Bóc tách & Chuẩn hóa dữ liệu", type="primary", use_container_width=True):
                if not danh_sach_files and not raw_text.strip():
                    st.warning("⚠️ Vui lòng tải file hoặc dán văn bản!")
                else:
                    with st.spinner("🤖 Trợ lý AI đang phân tích và kiểm định cấu trúc..."):
                        try:
                            payload = []
                            for f in danh_sach_files:
                                if f.name.endswith(".docx"):
                                    payload.append(trich_xuat_word_docx(f.read()))
                                elif f.name.endswith((".png", ".jpg", ".jpeg")) and HAS_PIL:
                                    payload.append(Image.open(io.BytesIO(f.read())))
                                else:
                                    payload.append(f.read().decode("utf-8", errors="ignore"))
                            if raw_text.strip():
                                payload.append(raw_text.strip())
                            ket_qua = goi_gemini_an_toan(
                                payload,
                                system_instruction=PROMPT_PARSER,
                                tra_ve_json=True
                            )
                            du_lieu_json = tach_json_tu_van_ban(ket_qua)
                            bai_chuan, ds_canh_bao = chuan_hoa_bai_hoc(du_lieu_json)
                            st.session_state["parsed_code_result"] = json.dumps(
                                bai_chuan, ensure_ascii=False, indent=4
                            )
                            st.session_state["parsed_warnings"] = ds_canh_bao
                        except Exception as e:
                            st.error(f"❌ Lỗi xử lý: {e}")

            if st.session_state.get("parsed_warnings"):
                for cb in st.session_state["parsed_warnings"]:
                    st.warning(f"⚠️ {cb}")

            if st.session_state.get("parsed_code_result"):
                code_out = st.session_state["parsed_code_result"]
                st.success("✅ Bóc tách dữ liệu thành công!")
                st.download_button(
                    "💾 Tải Dữ liệu về máy (.py)",
                    data=code_out.encode("utf-8"),
                    file_name="data_moi.py",
                    mime="text/x-python"
                )
                st.code(code_out, language="python")
        else:
            with GLOBALS["admin_fail_lock"]:
                GLOBALS["admin_fail_times"].append(now_ts)
            st.error("❌ Sai mật khẩu!")

elif che_do == "🎪 Phòng thí nghiệm ảo":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🎪 Phòng Thí Nghiệm & Mô Phỏng Tương Tác</p>
        <p class="hero-sub">Trực quan hóa kiến thức Khoa học Tự nhiên, Toán học & Ngữ Văn</p>
    </div>
    """, unsafe_allow_html=True)
    ds_mon_lab = [
        "📖 Môn Ngữ Văn",
        "🔬 Môn Vật lý (KHTN)",
        "🧪 Môn Hóa học (KHTN)",
        "📐 Môn Toán"
    ]
    mon_lab = st.selectbox("🔬 Chọn môn học thực hành:", ds_mon_lab)
    hien_thi_phong_thi_nghiem(mon_lab, key_prefix="main_lab")

elif che_do == "📖 Học theo chuyên đề":
    loi_nhan_ngau_nhien = random.choice(chu_de_hien_tai["loi_nhan"])
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">{chu_de_hien_tai["icon"]} {mon} — Kết Nối Tri Thức Lớp 7</p>
        <p class="hero-sub">💡 {loi_nhan_ngau_nhien}</p>
    </div>
    """, unsafe_allow_html=True)

    lop_dict = DATABASE[mon]
    if not lop_dict:
        st.warning("⚠️ Dữ liệu đang được cập nhật...")
    else:
        c_lop, c_chuong, c_bai = st.columns([1, 2, 2])
        ds_lop = list(lop_dict.keys())
        giu_lua_chon_hop_le("s_lop", ds_lop)
        lop = c_lop.selectbox("🏫 Khối:", ds_lop, key="s_lop")

        chuong_dict = lop_dict[lop]
        ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
        giu_lua_chon_hop_le("s_chuong", ds_chuong)
        chuong = c_chuong.selectbox("📂 Chương:", ds_chuong, key="s_chuong")

        bai_dict = chuong_dict[chuong]
        ds_bai = list(bai_dict.keys())
        giu_lua_chon_hop_le("s_bai", ds_bai)
        bai = c_bai.selectbox("📘 Bài học:", ds_bai, key="s_bai")

        bai_dang_hoc = f"{chuong} - {bai}"
        du_lieu_bai_hien_tai = bai_dict[bai]

        st.markdown("---")
        hien_thi_bai(mon, lop, chuong, bai, du_lieu_bai_hien_tai)

elif che_do == "📝 Phòng thi / Kiểm tra":
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">⏱️ Phòng Thi Thử & Kiểm Tra Định Kì — {mon}</p>
        <p class="hero-sub">{chu_de_hien_tai["khau_hieu"]}</p>
    </div>
    """, unsafe_allow_html=True)
    lop_dict = DATABASE[mon]
    if lop_dict:
        lop = st.selectbox("🏫 Khối:", list(lop_dict.keys()), key="s_lop_thi")
        chuong_dict = lop_dict[lop]
        ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))

        col1, col2 = st.columns([1, 2])
        ds_loai_de = [
            "Kiểm tra 15 phút (10 câu)",
            "Giữa kì (20 câu)",
            "Học kì (40 câu)"
        ]
        with col1:
            loai_de = st.selectbox("Cấu trúc đề:", ds_loai_de)
        with col2:
            chuong_chon = st.multiselect("Chọn chương:", ds_chuong, default=ds_chuong)

        mapping_cau = {
            "Kiểm tra 15 phút (10 câu)": 10,
            "Giữa kì (20 câu)": 20,
            "Học kì (40 câu)": 40
        }
        if st.button("🚀 TẠO ĐỀ THI LẠI / MỚI", type="primary"):
            st.session_state[f"dethi_{mon}_{lop}"] = None

        if st.session_state.get(f"dethi_{mon}_{lop}") is None:
            all_questions = []
            for c in chuong_chon:
                for b, data in chuong_dict[c].items():
                    all_questions.extend(data.get("cau_hoi", []))
            if not all_questions:
                st.error("❌ Chưa có câu hỏi trong chương này!")
            else:
                so_luong = min(mapping_cau[loai_de], len(all_questions))
                ds_chon = random.sample(all_questions, so_luong)
                de_tron_thi = []
                for ch in ds_chon:
                    da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                    nd_ch = ch.get("nd") or ch.get("de")
                    de_tron_thi.append({"nd": nd_ch, "da": da_moi, "d": vt_moi})
                st.session_state[f"dethi_{mon}_{lop}"] = de_tron_thi

        if st.session_state.get(f"dethi_{mon}_{lop}"):
            de_thi = st.session_state[f"dethi_{mon}_{lop}"]
            with st.form(f"form_thi_{mon}_{lop}"):
                tl_thi = {}
                for i, ch in enumerate(de_thi, 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl_thi[i] = st.radio(
                        f"Đ/á {i}:",
                        ch["da"],
                        key=f"thi_{mon}_{lop}_{i}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    st.markdown("---")
                if st.form_submit_button("🎯 NỘP BÀI", type="primary"):
                    dung = sum(
                        1 for i, ch in enumerate(de_thi, 1)
                        if tl_thi[i] == ch["da"][ch["d"]]
                    )
                    diem = dung / len(de_thi) * 10
                    ghi_nhan_lich_su(f"Thi thử ({mon})", diem, dung, len(de_thi), mon=mon)
                    st.markdown(
                        f"""<div class="diem-thi">🏆 ĐIỂM: {diem:.1f} / 10</div>""",
                        unsafe_allow_html=True
                    )
                    for i, ch in enumerate(de_thi, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl_thi[i] != da_dung:
                            st.error(f"❌ Câu {i}: Sai (Đúng: **{da_dung}**)")
                        else:
                            st.success(f"✅ Câu {i}: Đúng")

# ==================== KHU VỰC GIA SƯ AI ====================
if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra", "🎪 Phòng thí nghiệm ảo"]:
    st.divider()
    st.header("💬 Gia sư AI 24/7")

    col1, col2, col3, col4 = st.columns([2.2, 1, 1.8, 1])
    with col1:
        mon_ai = st.radio(
            "Môn:",
            ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn"],
            horizontal=True,
            label_visibility="collapsed"
        )
    with col2:
        tu_dong_doc = st.checkbox("🔊 Đọc to", value=True)
    with col3:
        nguon_ai = st.selectbox(
            "Nguồn:",
            ["⚡ Gemini", "🤝 Dola -> Gemini"],
            label_visibility="collapsed"
        )
    with col4:
        if st.button("🗑️ Xóa chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    sys_prompt = (
        f"Bạn là gia sư {mon_ai} lớp 7 sách Kết Nối Tri Thức. "
        f"Đang học: {bai_dang_hoc}. Gợi mở từng bước theo phương pháp Socratic, không giải hộ hoàn toàn."
    )
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    img_pil, btn_gui_anh = None, False
    if HAS_PIL:
        with st.expander("📸 Mắt thần AI — Gửi ảnh chụp đề bài", expanded=False):
            file_anh = st.file_uploader(
                "Tải ảnh:",
                type=["png", "jpg", "jpeg"],
                key="uploader_anh_giasu"
            )
            if file_anh:
                img_pil = Image.open(file_anh)
                st.image(img_pil, width=280)
                btn_gui_anh = st.button("🔍 Gửi ảnh cho Gia sư", type="primary")

    img_gui = img_pil if btn_gui_anh else None
    text_mic = (
        speech_to_text(language="vi-VN", start_prompt="🔴 NÓI", stop_prompt="⏹️ DỪNG", just_once=True, key="STT")
        if HAS_MIC else None
    )
    prompt = (
        "Thầy/cô xem giúp em bài tập trong ảnh với ạ!"
        if btn_gui_anh else (text_mic or st.chat_input("Hỏi gia sư..."))
    )

    if prompt:
        if not GEMINI_KEYS:
            st.error("⚠️ Hệ thống chưa được cấu hình API Key trong phần Secrets.")
        else:
            ok, giay = kiem_tra_gioi_han_tan_suat()
            if not ok:
                st.warning(f"⏳ Chờ {giay}s rồi hỏi tiếp. Câu hỏi chưa gửi: '{prompt}'")
            else:
                with st.chat_message("user"):
                    if img_gui:
                        st.image(img_gui, width=250)
                    st.markdown(prompt)
                st.session_state.chat_history.append({"role": "user", "content": prompt})

                with st.chat_message("assistant"):
                    is_first = (len(st.session_state.chat_history) <= 2) and not img_gui
                    h_key = tao_ma_hash_cau_hoi(mon_ai, bai_dang_hoc, nguon_ai, prompt) if is_first else None
                    ans_cached = lay_cache_ai(h_key) if h_key else None

                    if ans_cached:
                        st.markdown(ans_cached)
                        st.session_state.chat_history.append({"role": "assistant", "content": ans_cached})
                        doc_to_an_toan(ans_cached, autoplay=tu_dong_doc)
                    else:
                        g_hist = [
                            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                            for m in st.session_state.chat_history[:-1]
                        ]
                        luu_kq = ""
                        try:
                            with st.spinner("🤖 Gia sư AI đang suy nghĩ..."):
                                payload = [prompt, img_gui] if img_gui else prompt
                                if "Dola" in nguon_ai and not img_gui:
                                    d_nd = goi_dola_toi_uu(prompt)
                                    if d_nd:
                                        cau_truyen = f"Chuẩn SGK: {d_nd}\nDiễn giải câu: {prompt}"
                                        luu_kq = goi_gemini_an_toan(cau_truyen, sys_prompt, g_hist)
                                    else:
                                        luu_kq = goi_gemini_an_toan(payload, sys_prompt, g_hist)
                                else:
                                    luu_kq = goi_gemini_an_toan(payload, sys_prompt, g_hist)
                                st.markdown(luu_kq)
                        except Exception:
                            luu_kq = "⚠️ Đường truyền AI đang bận xử lý, em thử lại câu hỏi sau vài giây nhé."
                            st.error(luu_kq)

                        st.session_state.chat_history.append({"role": "assistant", "content": luu_kq})
                        if h_key:
                            luu_cache_ai(h_key, luu_kq)
                        if luu_kq and "⚠️" not in luu_kq:
                            doc_to_an_toan(luu_kq, autoplay=tu_dong_doc)
