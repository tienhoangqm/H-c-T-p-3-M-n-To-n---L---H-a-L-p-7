# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Tổng hợp Hoàn chỉnh (Full Production):
  - 5 môn học: Toán, Vật lý (KHTN), Hóa học (KHTN), Ngữ Văn, Tiếng Anh (Global Success)
  - Giao diện đồng bộ theo chủ đề từng môn, 5 thẻ môn học cân đối tuyệt đối (Equal Height)
  - Tích hợp trọn vẹn data_anh.py: KIEN_THUC_NEN (30% ôn tập), Nghe từ vựng, Từ điển Offline, Từ của ngày
  - Phòng thực hành Ngôn ngữ (Language Lab): Flashcard, Luyện phát âm AI, Nhập vai giao tiếp (Role-play)
  - Gia sư AI 24/7 (SDK google-genai), Trạm nạp dữ liệu chuẩn hóa JSON, Chống đoán mật khẩu Admin
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

# Không để cả trang sập nếu server chưa cài google-genai
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

# === ĐOẠN CODE THÊM VÀO ĐỂ ẨN MENU MẶC ĐỊNH CHỨA CHỮ "Ket Noi Tri Thuc" ===
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none !important;}
        
        /* Chỉnh lại khoảng cách lề trên của sidebar cho gọn gàng hơn sau khi ẩn menu */
        [data-testid="stSidebar"] {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

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

# ==================== BỘ ĐỆM AI (LRU CACHE) ====================
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
        s1 = re.sub(r'[.?!]+$', '', re.sub(r'\s+', ' ', str(nd).strip().lower()))
        s2 = re.sub(r'[.?!]+$', '', re.sub(r'\s+', ' ', str(d).strip().lower()))
        if s1 == s2 or s1.replace(" ", "") == s2.replace(" ", ""):
            return True
    return False

PHUONG_AN_CO_DINH = re.compile(
    r'\b(?:tất cả|cả hai|cả ba|các đáp án|các phương án|all of the above|both a and b)\b',
    re.IGNORECASE
)
PHUONG_AN_DINH_DANH = re.compile(
    r'\b(?:cả [a-d]|[a-d] và [a-d]|[a-d],\s*[a-d])\b',
    re.IGNORECASE
)

def tron_dap_an_thong_minh(ch):
    da_goc = list(ch["da"])
    d_dung = da_goc[ch["d"]]
    if any(PHUONG_AN_DINH_DANH.search(str(x)) for x in da_goc):
        return da_goc, ch["d"]
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

def doc_to_an_toan(text, autoplay=True, lang="vi"):
    if not HAS_TTS or not text:
        return
    try:
        clean_text = lam_sach_van_ban_doc(text)
        if clean_text:
            afp = io.BytesIO()
            gTTS(text=clean_text, lang=lang).write_to_fp(afp)
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

# ==================== GỌI AI (SDK google-genai) ====================
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
    "gemini-2.5-flash-lite",
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

# ==================== KIỂM TRA DỮ LIỆU BÀI HỌC (TRẠM NẠP) ====================
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

# ==================== NẠP DỮ LIỆU 5 MÔN HỌC ====================
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
try:
    from data_anh import ANH, KIEN_THUC_NEN, TU_DIEN_OFFLINE, DS_TU_CUA_NGAY, TRA_TU_CACHE
except ImportError:
    ANH, KIEN_THUC_NEN, TU_DIEN_OFFLINE, DS_TU_CUA_NGAY, TRA_TU_CACHE = {}, {}, {}, [], {}

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
                        "lg": "Liên hệ với cách hai văn bản truyện thể hiện thế giới qua đôi mắt trẻ thơ."
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
    "📖 Môn Ngữ Văn": VAN,
    "🔤 Môn Tiếng Anh": ANH if ANH else {"Lớp 7": {"Unit 1: Đang cập nhật": {}}}
}

# Khởi tạo biến mon an toàn toàn cục chống lỗi NameError
MON_MAC_DINH = list(DATABASE.keys())[0]
mon = st.session_state.get("mon_main", MON_MAC_DINH)
if mon not in DATABASE:
    mon = MON_MAC_DINH

# ==================== TIỆN ÍCH RIÊNG CHO MÔN TIẾNG ANH ====================
def lay_cau_hoi_kem_on_tap(data_bai):
    """Lấy danh sách câu hỏi của bài và tự động trộn thêm ~30% câu ôn tập từ KIEN_THUC_NEN."""
    ds_chinh = list(data_bai.get("cau_hoi", []))
    ds_on_tap_keys = data_bai.get("on_tap", [])
    if not ds_on_tap_keys or not KIEN_THUC_NEN:
        return ds_chinh

    ngan_hang_phu = []
    for k in ds_on_tap_keys:
        if k in KIEN_THUC_NEN:
            ten_cd = KIEN_THUC_NEN[k].get("ten", "Ôn tập")
            for ch_phu in KIEN_THUC_NEN[k].get("cau_hoi", []):
                ban_sao = dict(ch_phu)
                ban_sao["nd"] = f"🔄 [{ten_cd}] {ban_sao['nd']}"
                ngan_hang_phu.append(ban_sao)

    if ngan_hang_phu:
        so_them = max(1, round(len(ds_chinh) * 0.4)) if ds_chinh else min(3, len(ngan_hang_phu))
        so_them = min(so_them, len(ngan_hang_phu))
        ds_chinh.extend(random.sample(ngan_hang_phu, so_them))
    return ds_chinh

def tra_cuu_tu_anh_viet(tu_can_tra, cho_phep_ai=False):
    """Tra từ trong TU_DIEN_OFFLINE hoặc TRA_TU_CACHE; nếu cho_phep_ai=True thì hỏi thêm Gemini."""
    t = tu_can_tra.strip().lower()
    if not t:
        return None
    if TU_DIEN_OFFLINE and t in TU_DIEN_OFFLINE:
        return TU_DIEN_OFFLINE[t]
    if t in TRA_TU_CACHE:
        return TRA_TU_CACHE[t]
    if cho_phep_ai and HAS_GENAI and GEMINI_KEYS:
        prompt_td = (
            f"Giải nghĩa từ/cụm từ tiếng Anh '{t}' cho học sinh lớp 7 dưới dạng JSON với các khóa: "
            '{"pa": "phiên âm IPA", "loai": "từ loại tiếng Việt", "nghia": "nghĩa tiếng Việt ngắn gọn", '
            '"vi_du": "1 câu ví dụ tiếng Anh ngắn", "vi_du_dich": "dịch câu ví dụ sang tiếng Việt"}.'
        )
        try:
            kq_json = goi_gemini_an_toan(t, system_instruction=prompt_td, tra_ve_json=True)
            obj = tach_json_tu_van_ban(kq_json)
            if isinstance(obj, dict) and obj.get("nghia"):
                TRA_TU_CACHE[t] = obj
                return obj
        except Exception as e:
            ghi_log_loi("Tra từ AI", e)
    return None

# ==================== DANH MỤC THÍ NGHIỆM & MÔ PHỎNG ====================
DANH_MUC_THI_NGHIEM = {
    "📐 Môn Toán": {
        "⚖️ Cân bằng phương trình & Biểu thức đại số": "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_vi.html"
    },
    "🔬 Môn Vật lý (KHTN)": {
        "🔊 Sóng âm – độ to và độ cao của âm": "https://phet.colorado.edu/sims/html/waves-intro/latest/waves-intro_vi.html",
        "💡 Phản xạ ánh sáng (mô phỏng có thêm khúc xạ – kiến thức lớp 9)": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_vi.html",
        "🧲 Nam châm & từ trường (dùng màn hình Nam châm thẳng)": "https://phet.colorado.edu/sims/html/faradays-electromagnetic-lab/latest/faradays-electromagnetic-lab_vi.html"
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
    },
    "🔤 Môn Tiếng Anh": {
        "🗂️ Trạm Flashcard Từ vựng": "anh_flashcard",
        "🎙️ Trạm Luyện Phát Âm": "anh_phat_am",
        "🤝 Trạm Giao Tiếp AI (Role-play)": "anh_roleplay"
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
        "chu_de": "Biện pháp tu từ (ví dụ minh họa)",
        "cau_hoi_mau": [
            {"cau": "Bầy chim non bay vút lên như những mũi tên nhỏ.", "loai": "So sánh", "phan_tich": "Làm nổi bật sự nhanh nhẹn, mạnh mẽ của bầy chim non."},
            {"cau": "Những ngôi sao thức suốt đêm, chăm chỉ làm việc trên bầu trời.", "loai": "Nhân hóa", "phan_tich": "Làm các vì sao trở nên gần gũi, sinh động như con người."}
        ]
    },
    "📝 Trạm Lập dàn ý bài văn": {
        "the_loai": "Phân tích đặc điểm nhân vật trong một tác phẩm văn học",
        "dan_y": [
            {"buoc": "Mở bài", "noi_dung": "Giới thiệu tác phẩm, tác giả, nhân vật và nêu nhận xét khái quát về nhân vật."},
            {"buoc": "Thân bài", "noi_dung": "Lần lượt phân tích từng đặc điểm của nhân vật; mỗi đặc điểm có bằng chứng từ văn bản (lời nói, hành động, suy nghĩ)."},
            {"buoc": "Kết bài", "noi_dung": "Khẳng định ý nghĩa của nhân vật và nêu cảm nghĩ của em."}
        ]
    }
}

# ==================== GIAO DIỆN SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    dark_mode = st.toggle("🌙 Chế độ tối", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")

    if not HAS_GENAI:
        st.error(
            "⚠️ Gia sư AI đang tắt: server chưa cài thư viện **google-genai**. "
            "Quản trị viên thêm dòng `google-genai` vào file requirements.txt rồi khởi động lại app."
        )
    elif not GEMINI_KEYS:
        st.warning("⚠️ Chưa có API Key, chạy ở chế độ Mẫu.")

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
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = st.session_state.get("mon_main", MON_MAC_DINH)
        if mon not in DATABASE:
            mon = MON_MAC_DINH

    if "lich_su_hoc_tap" in st.session_state and st.session_state.lich_su_hoc_tap:
        st.divider()
        st.markdown("### 📊 Lịch sử học tập")
        so_bai = len(st.session_state.lich_su_hoc_tap)
        tb = sum(i["diem"] for i in st.session_state.lich_su_hoc_tap) / so_bai
        st.metric("Điểm TB", f"{tb:.1f}", f"{so_bai} bài")

# ==================== CẤU HÌNH CSS NỀN SÁNG / TỐI ====================
if dark_mode:
    st.markdown("""
    <style>
        .stApp { background-color: #0F172A; color: #F1F5F9; }
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], footer { display: none !important; }
        .khung-lythuyet {
            background-color: #1E293B; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #3B82F6; margin-bottom: 1rem; color: #F1F5F9;
        }
        .khung-vidu {
            background-color: #27272A; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #F59E0B; margin-bottom: 1rem; color: #F1F5F9;
        }
        .dung { color: #34D399; font-weight: bold; }
        .sai { color: #F87171; font-weight: bold; }
        .diem-thi {
            font-size: 1.6rem; color: #F87171; text-align: center;
            padding: 1.2rem; border: 2px dashed #EF4444; border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], footer { display: none !important; }
        .khung-lythuyet {
            background-color: #EFF6FF; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #2563EB; margin-bottom: 1rem; color: #0F172A;
        }
        .khung-vidu {
            background-color: #FFFBEB; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #F59E0B; margin-bottom: 1rem; color: #0F172A;
        }
        .dung { color: #059669; font-weight: bold; }
        .sai { color: #DC2626; font-weight: bold; }
        .diem-thi {
            font-size: 1.6rem; color: #E11D48; text-align: center;
            padding: 1.2rem; border: 2px dashed #F43F5E; border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

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
    "anh": {
        "icon": "🔤", "ten": "Môn Tiếng Anh",
        "sang": ("#0F766E", "#0D9488", "#0284C7"),
        "toi": ("#042F2E", "#115E59", "#0369A1"),
        "nhan": "#FDE047", "chinh": "#0D9488",
        "khau_hieu": "Global Success – Chinh phục ngoại ngữ toàn cầu",
        "ky_hieu": ["Aa", "🎧", "🗣️", "📖", "✍️", "🔤", "💡", "⭐"],
        "loi_nhan": [
            "Practice makes perfect – Mỗi ngày học vài từ mới nhé!",
            "Đừng ngại nói tiếng Anh, sai ở đâu mình sửa ở đó!",
            "Ngôn ngữ là chìa khóa mở cửa thế giới.",
            "Nghe nhiều, đọc to, em sẽ nhớ từ vựng rất lâu!",
        ],
    },
    "home": {
        "icon": "🎓", "ten": "Hệ thống học tập lớp 7",
        "sang": ("#3730A3", "#6D28D9", "#DB2777"),
        "toi": ("#1E1B4B", "#4C1D95", "#831843"),
        "nhan": "#FDE047", "chinh": "#6D28D9",
        "khau_hieu": "Kết nối tri thức với cuộc sống · Chương trình GDPT 2018",
        "ky_hieu": ["📐", "⚡", "🧪", "📖", "🔤", "🏆", "💡", "🎯"],
        "loi_nhan": [
            "Mỗi ngày học một chút, cả năm tiến một đoạn dài!",
            "Không có câu hỏi nào là ngớ ngẩn – cứ hỏi gia sư AI nhé!",
            "Học là để hiểu, không phải để sợ điểm.",
        ],
    },
    "search": {
        "icon": "🔍", "ten": "Tra cứu bài học & Từ điển",
        "sang": ("#0C4A6E", "#0369A1", "#0E7490"),
        "toi": ("#082F49", "#0C4A6E", "#164E63"),
        "nhan": "#FDE047", "chinh": "#0369A1",
        "khau_hieu": "Gõ từ tiếng Anh để tra từ điển hoặc nhập từ khóa tìm bài học",
        "ky_hieu": ["🔎", "📚", "🗂️", "💡", "?", "📌", "🧭", "✨"],
        "loi_nhan": ["Biết cách tìm kiếm là đã đi được nửa đường tới câu trả lời."],
    },
    "admin": {
        "icon": "⚙️", "ten": "Trạm nạp dữ liệu",
        "sang": ("#1F2937", "#334155", "#475569"),
        "toi": ("#030712", "#111827", "#1F2937"),
        "nhan": "#38BDF8", "chinh": "#0284C7",
        "khau_hieu": "Bóc tách tài liệu bài học thành dữ liệu chuẩn cho hệ thống",
        "ky_hieu": ["⚙️", "🗄️", "📄", "🔧", "{ }", "📥", "🤖", "✅"],
        "loi_nhan": ["Dữ liệu được kiểm tra kĩ – bài học đến tay học sinh mới chuẩn."],
    },
}

MON_SANG_CHU_DE = {
    "📐 Môn Toán": "toan",
    "🔬 Môn Vật lý (KHTN)": "vatly",
    "🧪 Môn Hóa học (KHTN)": "hoa",
    "📖 Môn Ngữ Văn": "van",
    "🔤 Môn Tiếng Anh": "anh",
}

MO_TA_MON_TRANG_CHU = {
    "toan": "Số hữu tỉ, số thực và hình học.",
    "vatly": "Tốc độ, âm thanh, ánh sáng, từ.",
    "hoa": "Nguyên tử, phân tử và liên kết.",
    "van": "Truyện, thơ, tùy bút và tập làm văn.",
    "anh": "12 Unit Global Success & từ điển.",
}

VI_TRI_KY_HIEU = [
    (8, 62, 2.2, 0), (40, 74, 1.6, 1.2), (10, 86, 2.8, 2.4), (52, 90, 1.9, 0.6),
    (30, 54, 1.3, 3.0), (22, 70, 1.4, 1.8), (5, 42, 1.2, 4.0), (44, 60, 1.1, 2.8),
]

def tron_mau(mau, nen, ti_le):
    a = [int(mau[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(nen[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x * ti_le + y * (1 - ti_le)):02X}" for x, y in zip(a, b))

def lay_chu_de(mon_hoac_khoa):
    khoa = MON_SANG_CHU_DE.get(mon_hoac_khoa, mon_hoac_khoa)
    return khoa if khoa in CHU_DE_GIAO_DIEN else "home"

def loi_nhan_hom_nay(khoa):
    ds = CHU_DE_GIAO_DIEN[khoa]["loi_nhan"]
    return ds[datetime.date.today().toordinal() % len(ds)]

def bien_mau(khoa, che_do_toi):
    cd = CHU_DE_GIAO_DIEN[khoa]
    c1, c2, c3 = cd["toi"] if che_do_toi else cd["sang"]
    return f"--c1:{c1};--c2:{c2};--c3:{c3};--nhan:{cd['nhan']};"

def css_giao_dien_chung():
    return (
        "<style>"
        ".hb{position:relative;overflow:hidden;border-radius:20px;padding:1.4rem 1.5rem;"
        "margin:.2rem 0 1.3rem;color:#fff;"
        "background:linear-gradient(135deg,var(--c1) 0%,var(--c2) 55%,var(--c3) 100%);"
        "box-shadow:0 14px 30px -12px var(--c2);}"
        ".hb-kh{position:absolute;font-weight:800;color:#fff;opacity:.17;pointer-events:none;"
        "user-select:none;line-height:1;white-space:nowrap;animation:hb-troi 7s ease-in-out infinite;}"
        ".hb-than{position:relative;z-index:1;display:flex;align-items:center;gap:1.1rem;flex-wrap:wrap;}"
        ".hb-icon{flex:0 0 76px;width:76px;height:76px;border-radius:22px;display:flex;"
        "align-items:center;justify-content:center;font-size:2.6rem;background:rgba(255,255,255,.16);"
        "border:2px solid rgba(255,255,255,.38);animation:hb-lac 4s ease-in-out infinite;}"
        ".hb-chu{flex:1 1 280px;min-width:0;}"
        ".hb-nhan{display:inline-block;font-size:.72rem;font-weight:800;letter-spacing:.06em;"
        "text-transform:uppercase;padding:3px 10px;border-radius:999px;background:var(--nhan);"
        "color:#1F2937;margin-bottom:.4rem;}"
        ".hb-tieu-de{margin:0;font-size:2rem;font-weight:800;line-height:1.15;color:#fff !important;}"
        ".hb-phu{margin:.3rem 0 0;font-size:1rem;color:rgba(255,255,255,.94) !important;}"
        ".hb-chips{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:.8rem;}"
        ".hb-chip{font-size:.82rem;font-weight:600;padding:4px 11px;border-radius:999px;"
        "background:rgba(255,255,255,.17);border:1px solid rgba(255,255,255,.3);white-space:nowrap;color:#fff;}"
        ".hb-loi-nhan{position:relative;z-index:1;margin-top:1rem;padding:.6rem .9rem;border-radius:12px;"
        "font-size:.93rem;background:rgba(0,0,0,.26);border-left:4px solid var(--nhan);color:#fff;}"
        ".hb-loi-nhan b{color:var(--nhan);}"
        ".bh{border-radius:16px;padding:1rem 1.2rem;margin:.4rem 0 1rem;"
        "background:var(--bh-nen);border:1px solid var(--bh-vien);border-left:6px solid var(--bh-c);}"
        ".bh-duong{font-size:.82rem;color:var(--bh-phu) !important;margin:0 0 .25rem;}"
        ".bh-tieu-de{font-size:1.35rem;font-weight:800;margin:0 0 .8rem;line-height:1.3;"
        "color:var(--bh-chu) !important;}"
        ".bh-o{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.6rem;}"
        ".bh-so{border-radius:12px;padding:.6rem .75rem;background:var(--bh-o);}"
        ".bh-so .so{font-size:1.5rem;font-weight:800;line-height:1.1;color:var(--bh-c);}"
        ".bh-so .nhan{font-size:.8rem;color:var(--bh-phu);}"
        ".bh-loi{margin:0;font-size:.93rem;color:var(--bh-chu) !important;}"
        ".om{position:relative;overflow:hidden;border-radius:18px;padding:1.1rem;"
        "height:210px;display:flex;flex-direction:column;justify-content:space-between;"
        "color:#fff;margin-bottom:.5rem;"
        "background:linear-gradient(150deg,var(--c1) 0%,var(--c2) 60%,var(--c3) 100%);"
        "box-shadow:0 12px 26px -14px var(--c2);transition:transform .2s ease;}"
        ".om:hover{transform:translateY(-3px);}"
        ".om-icon{font-size:2.1rem;line-height:1;}"
        ".om-ten{font-size:1.08rem;font-weight:800;margin:.45rem 0 .2rem;color:#fff !important;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}"
        ".om-mo-ta{font-size:.84rem;line-height:1.35;margin:0;color:rgba(255,255,255,.92) !important;"
        "display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}"
        ".om-so{display:inline-block;width:fit-content;font-size:.75rem;font-weight:700;"
        "padding:3px 10px;border-radius:999px;background:rgba(255,255,255,.22);color:#fff;}"
        ".om-kh{position:absolute;right:-4px;bottom:-12px;font-size:4.2rem;font-weight:800;"
        "opacity:.14;pointer-events:none;line-height:1;color:#fff;}"
        ".buoc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.7rem;margin:.6rem 0 1rem;}"
        ".buoc-o{border-radius:14px;padding:.8rem .9rem;background:var(--bh-nen);border:1px solid var(--bh-vien);}"
        ".buoc-so{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;"
        "border-radius:50%;font-weight:800;color:#fff;background:var(--bh-c);margin-bottom:.35rem;}"
        ".buoc-o p{margin:0;font-size:.9rem;color:var(--bh-chu) !important;}"
        "@keyframes hb-troi{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-8px) rotate(6deg)}}"
        "@keyframes hb-lac{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(4deg) scale(1.04)}}"
        "@media (max-width:640px){.hb{padding:1.1rem}.hb-tieu-de{font-size:1.45rem}"
        ".hb-icon{flex-basis:58px;width:58px;height:58px;font-size:2rem;border-radius:16px}"
        ".hb-kh:nth-of-type(n+5){display:none}.bh-so .so{font-size:1.2rem}"
        ".buoc{grid-template-columns:1fr}}"
        "@media (prefers-reduced-motion:reduce){.hb-kh,.hb-icon{animation:none}.om{transition:none}}"
        "</style>"
    )

def bien_the_nhe(khoa, che_do_toi):
    c = CHU_DE_GIAO_DIEN[khoa]["chinh"]
    if che_do_toi:
        return (f"--bh-c:{tron_mau(c, '#FFFFFF', .75)};--bh-nen:{tron_mau(c, '#0F172A', .16)};"
                f"--bh-vien:{tron_mau(c, '#0F172A', .35)};--bh-o:{tron_mau(c, '#0F172A', .26)};"
                "--bh-chu:#F1F5F9;--bh-phu:#CBD5E1;")
    return (f"--bh-c:{c};--bh-nen:{tron_mau(c, '#FFFFFF', .06)};"
            f"--bh-vien:{tron_mau(c, '#FFFFFF', .22)};--bh-o:#FFFFFF;"
            "--bh-chu:#0F172A;--bh-phu:#475569;")

def css_widget_theo_mon(khoa):
    c = CHU_DE_GIAO_DIEN[khoa]["chinh"]
    nut = ("[data-testid='stBaseButton-primary'],[data-testid='stBaseButton-primaryFormSubmit'],"
           "button[kind='primary'],button[kind='primaryFormSubmit']")
    return (
        "<style>"
        f"{nut}{{background:{c} !important;border-color:{c} !important;color:#fff !important;}}"
        f"{nut.replace(',', ':hover,')}:hover{{filter:brightness(1.1);}}"
        f"span[data-baseweb='tag']{{background-color:{c} !important;}}"
        f"button[data-baseweb='tab'][aria-selected='true'] p{{color:{c} !important;font-weight:700;}}"
        f"div[data-baseweb='tab-highlight']{{background-color:{c} !important;}}"
        "</style>"
    )

def tao_hero(khoa, che_do_toi, nhan, tieu_de=None, phu_de=None, chips=None, hien_loi_nhan=True):
    cd = CHU_DE_GIAO_DIEN[khoa]
    ky_hieu = "".join(
        f'<span class="hb-kh" style="top:{t}%;left:{l}%;font-size:{s}rem;animation-delay:{d}s">'
        f'{html.escape(k)}</span>'
        for k, (t, l, s, d) in zip(cd["ky_hieu"], VI_TRI_KY_HIEU)
    )
    the_chip = "".join(f'<span class="hb-chip">{html.escape(c)}</span>' for c in (chips or []))
    khoi_chip = f'<div class="hb-chips">{the_chip}</div>' if the_chip else ""
    loi = ""
    if hien_loi_nhan:
        loi = f'<div class="hb-loi-nhan"><b>💬 Lời nhắn hôm nay:</b> {html.escape(loi_nhan_hom_nay(khoa))}</div>'
    return (
        f'<div class="hb" style="{bien_mau(khoa, che_do_toi)}">{ky_hieu}'
        '<div class="hb-than">'
        f'<div class="hb-icon">{cd["icon"]}</div>'
        '<div class="hb-chu">'
        f'<span class="hb-nhan">{html.escape(nhan)}</span>'
        f'<p class="hb-tieu-de">{html.escape(tieu_de or cd["ten"])}</p>'
        f'<p class="hb-phu">{html.escape(phu_de or cd["khau_hieu"])}</p>'
        f'{khoi_chip}'
        '</div></div>'
        f'{loi}</div>'
    )

def tao_the_bai_hoc(khoa, che_do_toi, lop, chuong, ten_bai, so_tn, so_cb, so_nc):
    o = (
        f'<div class="bh-so"><div class="so">{so_tn}</div><div class="nhan">📝 câu trắc nghiệm</div></div>'
        f'<div class="bh-so"><div class="so">{so_cb}</div><div class="nhan">✏️ bài cơ bản</div></div>'
        f'<div class="bh-so"><div class="so">{so_nc}</div><div class="nhan">🔥 bài nâng cao</div></div>'
    )
    return (
        f'<div class="bh" style="{bien_the_nhe(khoa, che_do_toi)}">'
        f'<p class="bh-duong">{html.escape(str(lop))} › {html.escape(str(chuong))}</p>'
        f'<p class="bh-tieu-de">{CHU_DE_GIAO_DIEN[khoa]["icon"]} {html.escape(str(ten_bai))}</p>'
        f'<div class="bh-o">{o}</div></div>'
    )

def tao_dai_de_thi(khoa, che_do_toi, loai_de, so_cau):
    return (
        f'<div class="bh" style="{bien_the_nhe(khoa, che_do_toi)}">'
        f'<p class="bh-tieu-de" style="margin-bottom:.3rem">📝 {html.escape(loai_de)} · {so_cau} câu</p>'
        '<p class="bh-loi">Đọc kĩ từng câu, chọn đáp án em thấy đúng nhất rồi bấm Nộp bài. '
        'Chúc em làm bài thật tốt! 🍀</p></div>'
    )

def tao_o_mon(khoa, che_do_toi, so_bai):
    cd = CHU_DE_GIAO_DIEN[khoa]
    return (
        f'<div class="om" style="{bien_mau(khoa, che_do_toi)}">'
        f'<span class="om-kh">{html.escape(cd["ky_hieu"][0])}</span>'
        '<div>'
        f'<div class="om-icon">{cd["icon"]}</div>'
        f'<p class="om-ten">{html.escape(cd["ten"])}</p>'
        f'<p class="om-mo-ta">{html.escape(MO_TA_MON_TRANG_CHU.get(khoa, ""))}</p>'
        '</div>'
        f'<span class="om-so">{"📚 " + str(so_bai) + " bài học" if so_bai else "🛠️ Đang cập nhật"}</span>'
        '</div>'
    )

def chip_thanh_tich(mon):
    so, tb = thanh_tich_mon(mon)
    return f"⭐ Đã làm {so} bài · Điểm TB {tb:.1f}" if so else "🚀 Làm bài đầu tiên nào!"

def dem_chuong_bai(mon):
    lop_dict = DATABASE.get(mon) or {}
    so_chuong = sum(len(c) for c in lop_dict.values())
    so_bai = sum(len(b) for c in lop_dict.values() for b in c.values())
    return so_chuong, so_bai

# ==================== BANNER GIA SƯ AI ====================
def tao_banner_gia_su(che_do_toi, bai_hien_tai="", ai_san_sang=True, co_anh=True, co_mic=True):
    LINH_VAT = "🦉"
    if che_do_toi:
        NEN = "linear-gradient(135deg, #312E81 0%, #6D28D9 55%, #9D174D 100%)"
        BONG = "0 10px 28px rgba(0,0,0,0.45)"
    else:
        NEN = "linear-gradient(135deg, #4F46E5 0%, #7C3AED 55%, #EC4899 100%)"
        BONG = "0 10px 28px rgba(124,58,237,0.30)"

    if ai_san_sang:
        trang_thai, mau_cham, hieu_ung = "Sẵn sàng trả lời", "#34D399", "gs-pulse 1.8s infinite"
    else:
        trang_thai, mau_cham, hieu_ung = "Đang tạm nghỉ", "#FBBF24", "none"

    the_tinh_nang = ["📚 Bám sát sách Kết nối tri thức", "🪜 Gợi ý từng bước"]
    if co_anh:
        the_tinh_nang.append("📸 Gửi ảnh đề bài")
    if co_mic:
        the_tinh_nang.append("🎤 Hỏi bằng giọng nói")
    chips = "".join(f'<span class="gs-chip">{t}</span>' for t in the_tinh_nang)

    dong_bai = ""
    if bai_hien_tai:
        dong_bai = f'<div class="gs-bai">📖 Em đang học: <b>{html.escape(bai_hien_tai)}</b></div>'

    css = (
        "<style>"
        ".gs-banner{position:relative;overflow:hidden;display:flex;align-items:center;gap:1rem;"
        "flex-wrap:wrap;padding:1.15rem 1.3rem;margin:.4rem 0 1.1rem;border-radius:18px;"
        f"background:{NEN};box-shadow:{BONG};color:#fff;}}"
        ".gs-banner::before,.gs-banner::after{content:'';position:absolute;border-radius:50%;"
        "background:rgba(255,255,255,.12);pointer-events:none;}"
        ".gs-banner::before{width:180px;height:180px;right:-50px;top:-70px;}"
        ".gs-banner::after{width:110px;height:110px;right:90px;bottom:-60px;}"
        ".gs-avatar{position:relative;z-index:1;flex:0 0 64px;width:64px;height:64px;border-radius:50%;"
        "display:flex;align-items:center;justify-content:center;font-size:2.1rem;"
        "background:rgba(255,255,255,.18);border:2px solid rgba(255,255,255,.5);"
        "animation:gs-float 3s ease-in-out infinite;}"
        ".gs-noi-dung{position:relative;z-index:1;flex:1 1 260px;min-width:0;}"
        ".gs-tieu-de{display:flex;align-items:center;flex-wrap:wrap;gap:.5rem;margin:0;"
        "font-size:1.5rem;font-weight:800;line-height:1.25;color:#fff !important;}"
        ".gs-247{font-size:.8rem;font-weight:800;padding:2px 9px;border-radius:999px;"
        "background:#FDE047;color:#4C1D95;}"
        ".gs-phu{margin:.3rem 0 .6rem;font-size:.95rem;color:#F5F3FF !important;opacity:.95;}"
        ".gs-chips{display:flex;flex-wrap:wrap;gap:.4rem;}"
        ".gs-chip{font-size:.8rem;padding:3px 10px;border-radius:999px;white-space:nowrap;"
        "background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.32);color:#fff;}"
        ".gs-bai{margin-top:.6rem;font-size:.85rem;padding:4px 10px;border-radius:6px;"
        "background:rgba(255,255,255,.14);border-left:3px solid #FDE047;color:#fff;}"
        ".gs-trang-thai{position:relative;z-index:1;display:inline-flex;align-items:center;gap:.45rem;"
        "padding:6px 12px;border-radius:999px;font-size:.85rem;font-weight:600;white-space:nowrap;"
        "background:rgba(15,23,42,.28);color:#fff;}"
        f".gs-cham{{width:10px;height:10px;border-radius:50%;background:{mau_cham};animation:{hieu_ung};}}"
        "@keyframes gs-float{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}"
        "@keyframes gs-pulse{0%{box-shadow:0 0 0 0 rgba(52,211,153,.7)}"
        "70%{box-shadow:0 0 0 9px rgba(52,211,153,0)}100%{box-shadow:0 0 0 0 rgba(52,211,153,0)}}"
        "@media (max-width:640px){.gs-tieu-de{font-size:1.2rem}"
        ".gs-avatar{flex-basis:52px;width:52px;height:52px;font-size:1.7rem}}"
        "@media (prefers-reduced-motion:reduce){.gs-avatar,.gs-cham{animation:none}}"
        "</style>"
    )
    noi_dung = (
        '<div class="gs-banner">'
        f'<div class="gs-avatar">{LINH_VAT}</div>'
        '<div class="gs-noi-dung">'
        '<p class="gs-tieu-de">Gia sư AI <span class="gs-247">24/7</span></p>'
        '<p class="gs-phu">Em cứ hỏi nhé! Thầy cô AI sẽ gợi mở từng bước để em tự tìm ra đáp án.</p>'
        f'<div class="gs-chips">{chips}</div>'
        f'{dong_bai}'
        '</div>'
        f'<div class="gs-trang-thai"><span class="gs-cham"></span>{trang_thai}</div>'
        '</div>'
    )
    return css + noi_dung

# ==================== PHÒNG THỰC HÀNH NGÔN NGỮ TIẾNG ANH (LANGUAGE LAB) ====================
def hien_thi_lab_tieng_anh(key_prefix="eng_lab"):
    st.markdown("#### 🔤 Trạm Thực Hành Kỹ Năng Tiếng Anh (Global Success)")
    tab_tu, tab_noi, tab_chat, tab_td = st.tabs([
        "🗂️ Trạm Flashcard",
        "🎙️ Trạm Phát Âm",
        "🤝 Đóng Vai Giao Tiếp AI",
        "📖 Tra Từ Điển Nhanh"
    ])

    ds_tu_goc = list(TU_DIEN_OFFLINE.keys()) if TU_DIEN_OFFLINE else ["hello"]

    with tab_tu:
        st.caption("Lật thẻ để ôn từ vựng ngẫu nhiên trong ngân hàng từ vựng lớp 7.")
        khoa_fc = f"fc_word_{key_prefix}"
        if khoa_fc not in st.session_state:
            st.session_state[khoa_fc] = random.choice(ds_tu_goc)
        if st.button("🔄 Rút thẻ từ mới", key=f"btn_fc_{key_prefix}"):
            st.session_state[khoa_fc] = random.choice(ds_tu_goc)

        fc_word = st.session_state[khoa_fc]
        tu_info = TU_DIEN_OFFLINE.get(fc_word, {"pa": "", "loai": "", "nghia": "", "vi_du": "", "vi_du_dich": ""})

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                f"<div style='padding:1.8rem;background:linear-gradient(135deg,#0F766E,#0284C7);"
                f"color:white;border-radius:16px;text-align:center;'>"
                f"<h2 style='color:#FDE047;font-size:2.4rem;margin:0;'>{html.escape(fc_word)}</h2>"
                f"<p style='font-size:1.05rem;margin:.4rem 0 0;color:#E0F2FE;'>"
                f"{html.escape(tu_info.get('pa', ''))} · {html.escape(tu_info.get('loai', ''))}</p></div>",
                unsafe_allow_html=True
            )
            if st.button("🔊 Nghe phát âm chuẩn", key=f"btn_nghe_fc_{key_prefix}", use_container_width=True):
                doc_to_an_toan(fc_word, autoplay=True, lang="en")
        with c2:
            if st.checkbox("👁️ Lật mặt sau (Xem nghĩa & ví dụ)", key=f"chk_fc_{key_prefix}"):
                st.success(f"**Nghĩa:** {tu_info.get('nghia', '')}")
                if tu_info.get("vi_du"):
                    st.info(f"💬 **Ví dụ:** *{tu_info['vi_du']}*\n\n👉 **Dịch:** {tu_info.get('vi_du_dich', '')}")
                    if st.button("🔊 Nghe câu ví dụ", key=f"btn_nghe_vd_{key_prefix}"):
                        doc_to_an_toan(tu_info["vi_du"], autoplay=True, lang="en")

    with tab_noi:
        st.caption("Nghe máy đọc mẫu, sau đó bấm nút thu âm và đọc lại từ đó bằng tiếng Anh.")
        khoa_pa = f"pa_word_{key_prefix}"
        if khoa_pa not in st.session_state:
            st.session_state[khoa_pa] = random.choice(ds_tu_goc)
        if st.button("🎯 Đổi từ luyện phát âm", key=f"btn_pa_{key_prefix}"):
            st.session_state[khoa_pa] = random.choice(ds_tu_goc)

        pa_word = st.session_state[khoa_pa]
        pa_info = TU_DIEN_OFFLINE.get(pa_word, {})
        st.markdown(
            f"##### Từ cần đọc: <span style='color:#0D9488;font-size:1.5rem;font-weight:800'>{html.escape(pa_word)}</span> "
            f"`{pa_info.get('pa', '')}` — *{pa_info.get('nghia', '')}*",
            unsafe_allow_html=True
        )
        if st.button("🔊 Nghe mẫu phát âm", key=f"btn_nghe_pa_{key_prefix}"):
            doc_to_an_toan(pa_word, autoplay=True, lang="en")

        if HAS_MIC:
            text_spoken = speech_to_text(
                language="en-US",
                start_prompt="🔴 Bấm để NÓI tiếng Anh",
                stop_prompt="⏹️ DỪNG thu âm",
                just_once=True,
                key=f"STT_Eng_{key_prefix}"
            )
            if text_spoken:
                st.write(f"🎧 Hệ thống nghe được: **{text_spoken}**")
                clean_spoken = re.sub(r'[^\w\s]', '', text_spoken).strip().lower()
                if clean_spoken == pa_word.lower():
                    st.success("🎉 Xuất sắc! Em phát âm rất chuẩn xác!")
                elif pa_word.lower() in clean_spoken.split():
                    st.info("👍 Khá tốt! Hệ thống đã nhận ra đúng từ của em.")
                else:
                    st.error("❌ Chưa khớp lắm, em nghe lại mẫu và đọc to, rõ hơn nhé!")
        else:
            st.info("💡 Thiết bị chưa bật quyền Micro hoặc thiếu thư viện thu âm.")

    with tab_chat:
        st.caption("Thực hành hội thoại ngắn bằng tiếng Anh với AI (AI sẽ nhẹ nhàng sửa lỗi ngữ pháp bằng tiếng Việt ở cuối câu).")
        tinh_huong = st.selectbox(
            "🎭 Chọn chủ đề hội thoại:",
            [
                "⚽ Talking about hobbies & leisure activities (Unit 1)",
                "🥗 Keeping fit & healthy habits (Unit 2)",
                "🤝 Community service & volunteer work (Unit 3)",
                "🍜 Ordering Vietnamese food & drink (Unit 5)",
                "🚀 Travelling in the future (Unit 11)"
            ],
            key=f"sel_rp_{key_prefix}"
        )
        khoa_rp = f"roleplay_chat_{key_prefix}"
        if st.button("🔄 Làm mới cuộc trò chuyện", key=f"btn_reset_rp_{key_prefix}"):
            st.session_state[khoa_rp] = []
        if khoa_rp not in st.session_state:
            st.session_state[khoa_rp] = []

        for msg in st.session_state[khoa_rp]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_reply = st.chat_input("Gõ câu tiếng Anh của em vào đây...", key=f"inp_rp_{key_prefix}")
        if user_reply:
            if not HAS_GENAI or not GEMINI_KEYS:
                st.error("⚠️ Cần cấu hình GEMINI_API_KEY để trò chuyện cùng AI.")
            else:
                ok_r, cho_r = kiem_tra_gioi_han_tan_suat()
                if not ok_r:
                    st.warning(f"⏳ Chờ {cho_r} giây rồi gửi tiếp nhé.")
                else:
                    with st.chat_message("user"):
                        st.markdown(user_reply)
                    st.session_state[khoa_rp].append({"role": "user", "content": user_reply})

                    rp_prompt = (
                        f"You are a friendly English speaking partner for a 7th-grade Vietnamese student. "
                        f"Topic: {tinh_huong}. Keep your English response short (1-2 simple sentences, A2 level) "
                        "and ask ONE follow-up question. If the student made a grammar/spelling mistake, "
                        "add a polite correction in Vietnamese inside brackets [Góp ý: ...] at the very end."
                    )
                    g_hist = [
                        {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                        for m in st.session_state[khoa_rp][:-1]
                    ]
                    with st.chat_message("assistant"):
                        try:
                            with st.spinner("🤖 Partner is typing..."):
                                rp_ans = goi_gemini_an_toan(user_reply, rp_prompt, history=g_hist)
                                st.markdown(rp_ans)
                                st.session_state[khoa_rp].append({"role": "assistant", "content": rp_ans})
                                phan_tieng_anh = rp_ans.split("[")[0].strip()
                                doc_to_an_toan(phan_tieng_anh, autoplay=False, lang="en")
                        except Exception as e:
                            ghi_log_loi("Roleplay English", e)
                            st.error("⚠️ AI đang bận, em thử lại sau vài giây nhé.")

    with tab_td:
        tu_tra = st.text_input("🔎 Nhập từ tiếng Anh cần tra:", key=f"td_inp_{key_prefix}", placeholder="VD: hobby, healthy, delicious...")
        if tu_tra.strip():
            kq_td = tra_cuu_tu_anh_viet(tu_tra, cho_phep_ai=True)
            if kq_td:
                st.success(f"**{tu_tra.strip().lower()}** {kq_td.get('pa', '')} ({kq_td.get('loai', '')}) — **{kq_td.get('nghia', '')}**")
                if kq_td.get("vi_du"):
                    st.info(f"📝 **Ví dụ:** *{kq_td['vi_du']}*\n\n👉 **Dịch:** {kq_td.get('vi_du_dich', '')}")
                if st.button("🔊 Phát âm từ này", key=f"btn_tts_td_{key_prefix}"):
                    doc_to_an_toan(tu_tra.strip(), autoplay=True, lang="en")
            else:
                st.warning("Chưa tìm thấy từ này trong từ điển offline.")

# ==================== HIỂN THỊ PHÒNG THÍ NGHIỆM & BÀI HỌC ====================
def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    if mon_hien_tai == "🔤 Môn Tiếng Anh":
        hien_thi_lab_tieng_anh(key_prefix=key_prefix)
    elif mon_hien_tai == "📖 Môn Ngữ Văn":
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
            st.info(f"📌 **Khái quát:** {data['khai_quat']}")
            for item in data["bo_cuc"]:
                with st.expander(f"🔹 {item['phan']}"):
                    st.write(item["noi_dung"])
            st.success(f"💡 **Ý nghĩa nhân văn:** {data['y_nghia']}")
        elif "Biểu đồ Tương tác" in chon_modul:
            data = DATA_LAB_NGU_VAN["🎭 Biểu đồ Tương tác Nhân vật"]
            st.markdown(f"### 🎭 {data['nhan_vat']}")
            st.markdown(f"⭐ **Đặc điểm:** {data['dac_diem']}")
            st.markdown(f"🎯 **Hành vi:** {data['hanh_vi_tieu_bieu']}")
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
            if key_prefix == "main_lab" or st.toggle("🚀 Bật màn hình mô phỏng tương tác", key=f"load_phet_{key_prefix}"):
                components.iframe(url_tn, height=580, scrolling=True)

def dinh_dang_doan_van(van_ban):
    cac_dong = html.escape(str(van_ban).strip(), quote=False).split("\n")
    ket_qua = []
    for dong in cac_dong:
        so_cach = len(dong) - len(dong.lstrip(" "))
        ket_qua.append("&nbsp;" * so_cach + dong.lstrip(" "))
    return "<br>".join(ket_qua)

def la_bai_tu_luan(bt):
    if bt.get("kieu") == "tu_luan":
        return True
    dap_an = [str(x).strip() for x in bt.get("dd", []) if str(x).strip()]
    return not any(len(x) <= 30 for x in dap_an)

def hien_thi_mot_bai_tap(bt, khoa, mon):
    dap_an = bt.get("dd") or [""]
    goi_y = bt.get("hd", "")
    giai_thich = bt.get("gt", "")
    loi_giai = bt.get("lg", "")

    if "Ngữ Văn" in mon:
        if st.button("💡 Xem gợi ý", key=f"btn_goiy_{khoa}"):
            st.info(f"📝 **Gợi ý:** {loi_giai or dap_an[0]}")
        return

    if goi_y and st.checkbox("💡 Gợi ý cách làm", key=f"hd_{khoa}"):
        st.info(goi_y)

    if la_bai_tu_luan(bt):
        st.text_area("✍️ Bài làm của em:", key=f"tl_{khoa}", height=110,
                     placeholder="Em viết câu trả lời ở đây, sau đó bấm xem đáp án để tự đối chiếu.")
        if st.checkbox("📖 Xem đáp án mẫu để đối chiếu", key=f"xem_{khoa}"):
            st.success(f"**Đáp án gợi ý:** {dap_an[0]}")
            if giai_thich:
                st.caption(f"💡 {giai_thich}")
            if loi_giai:
                st.markdown(f"**Lời giải chi tiết:** {loi_giai}")
        return

    ans = st.text_input("Nhập kết quả / đáp án:", key=f"nhap_{khoa}")
    if st.button("Kiểm tra", key=f"kt_{khoa}"):
        if not ans.strip():
            st.warning("⚠️ Em nhập đáp án trước nhé!")
        elif so_sanh_so_hoc(ans, dap_an):
            st.markdown("""<p class="dung">✅ Chính xác! Giỏi lắm!</p>""", unsafe_allow_html=True)
            if giai_thich:
                st.caption(f"💡 {giai_thich}")
        else:
            st.markdown(
                """<p class="sai">❌ Chưa đúng rồi. Em kiểm tra lại hoặc mở xem đáp án nhé!</p>""",
                unsafe_allow_html=True
            )
    if st.checkbox("📖 Xem đáp án và lời giải", key=f"lg_{khoa}"):
        st.success(f"**Đáp án:** {dap_an[0]}")
        if giai_thich:
            st.caption(f"💡 {giai_thich}")
        if loi_giai:
            st.markdown(f"**Lời giải chi tiết:** {loi_giai}")

def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    lt = data.get("ly_thuyet", "").strip()
    vd = data.get("vi_du", "").strip()
    ds_nghe = data.get("nghe", [])
    ds_on_tap = data.get("on_tap", [])
    ch_list = lay_cau_hoi_kem_on_tap(data) if "Tiếng Anh" in mon else data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    st.markdown(
        tao_the_bai_hoc(
            lay_chu_de(mon), dark_mode, lop, chuong, ten_bai,
            len(ch_list), len(bt_cb), len(bt_nc)
        ),
        unsafe_allow_html=True
    )

    ten_tab5 = "🎧 Luyện Nghe - Nói" if "Tiếng Anh" in mon else "🎪 Phòng thí nghiệm"
    ds_tabs = [
        "📚 Lý thuyết",
        "✏️ Cơ bản",
        "🔥 Nâng cao",
        "📝 Trắc nghiệm",
        ten_tab5
    ]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(ds_tabs)

    with tab1:
        if lt:
            mau_mon = CHU_DE_GIAO_DIEN[lay_chu_de(mon)]["chinh"]
            nen_lt = tron_mau(mau_mon, "#0F172A" if dark_mode else "#FFFFFF", .16 if dark_mode else .07)
            st.markdown(
                f"""<div class="khung-lythuyet" style="border-left-color:{mau_mon};background-color:{nen_lt}">"""
                f"""<b style="color:{mau_mon}">📚 Kiến thức trọng tâm</b><br>{dinh_dang_doan_van(lt)}</div>""",
                unsafe_allow_html=True
            )
        if vd:
            st.markdown(
                f"""<div class="khung-vidu"><b>💡 Ví dụ minh họa:</b><br>{dinh_dang_doan_van(vd)}</div>""",
                unsafe_allow_html=True
            )
            if "Tiếng Anh" in mon and st.button("🔊 Nghe câu ví dụ", key=f"tts_vd_{sid}"):
                doc_to_an_toan(vd, autoplay=True, lang="en")

        if ds_nghe:
            st.markdown("#### 🎧 Từ vựng & Phát âm trong bài")
            cols_nghe = st.columns(min(3, len(ds_nghe)))
            for idx_n, item_n in enumerate(ds_nghe):
                with cols_nghe[idx_n % len(cols_nghe)]:
                    tu_n = item_n.get("tu", "")
                    pa_n = item_n.get("phi_en_am", "")
                    nghia_n = item_n.get("nghia", "")
                    st.info(f"**{tu_n}** `{pa_n}`\n\n👉 {nghia_n}")
                    if st.button(f"🔊 Nghe '{tu_n}'", key=f"nghe_{sid}_{idx_n}", use_container_width=True):
                        doc_to_an_toan(tu_n, autoplay=True, lang="en")

        if "Tiếng Anh" in mon and ds_on_tap and KIEN_THUC_NEN:
            with st.expander("🔄 Kiến thức nền (Lớp 4–6) bổ trợ cho bài học này", expanded=False):
                for ma_ot in ds_on_tap:
                    if ma_ot in KIEN_THUC_NEN:
                        ot_obj = KIEN_THUC_NEN[ma_ot]
                        st.markdown(f"- **{ot_obj.get('ten', ma_ot)}:** {ot_obj.get('ly_thuyet', 'Ôn tập qua câu hỏi trắc nghiệm.')}")

    with tab2:
        if not bt_cb:
            st.info("Chưa có bài tập.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                nhan_tl = " ✍️" if ("Ngữ Văn" not in mon and la_bai_tu_luan(bt)) else ""
                with st.expander(f"Bài {i}{nhan_tl}: {bt['de']}"):
                    hien_thi_mot_bai_tap(bt, f"cb_{sid}_{i}", mon)

    with tab3:
        if not bt_nc:
            st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                de_ngan = nc['de'] if len(nc['de']) <= 60 else nc['de'][:60] + "..."
                nhan_tl = " ✍️" if ("Ngữ Văn" not in mon and la_bai_tu_luan(nc)) else ""
                with st.expander(f"Bài nâng cao {i}{nhan_tl}: {de_ngan}"):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    hien_thi_mot_bai_tap(nc, f"nc_{sid}_{i}", mon)

    with tab4:
        if len(ch_list) == 0:
            st.info("Chưa có trắc nghiệm.")
        else:
            if "Tiếng Anh" in mon and ds_on_tap:
                st.caption("🔄 Đề trắc nghiệm đã tự động đan xen thêm câu hỏi ôn tập kiến thức nền lớp 4–6.")
            if st.button("🔄 Làm mới đề", key=f"btn_rf_{sid}"):
                st.session_state[f"de_{sid}"] = None
            if f"de_{sid}" not in st.session_state or st.session_state[f"de_{sid}"] is None:
                moj = lay_cau_hoi_kem_on_tap(data) if "Tiếng Anh" in mon else ch_list
                de_tron = []
                for ch in moj:
                    da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                    nd_ch = ch.get("nd") or ch.get("de")
                    de_tron.append({"nd": nd_ch, "da": da_moi, "d": vt_moi, "gt": ch.get("gt", "")})
                st.session_state[f"de_{sid}"] = de_tron
                st.session_state[f"nonce_{sid}"] = uuid.uuid4().hex[:8]
            nonce = st.session_state.setdefault(f"nonce_{sid}", "0")

            de_hien_tai = st.session_state[f"de_{sid}"]
            with st.form(f"f_{sid}"):
                tl = {}
                for i, ch in enumerate(de_hien_tai, 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl[i] = st.radio(
                        "Chọn:",
                        ch["da"],
                        key=f"r_{sid}_{nonce}_{i}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    st.markdown("---")
                if st.form_submit_button("🚀 Nộp bài", type="primary"):
                    dung = sum(
                        1 for i, ch in enumerate(de_hien_tai, 1)
                        if tl[i] == ch["da"][ch["d"]]
                    )
                    diem = dung / len(de_hien_tai) * 10
                    ghi_nhan_lich_su(f"Trắc nghiệm: {ten_bai}", diem, dung, len(de_hien_tai), mon=mon)
                    st.markdown(
                        f"""<div class="diem-thi">🏆 ĐIỂM: {diem:.1f} / 10 ({dung}/{len(de_hien_tai)} câu)</div>""",
                        unsafe_allow_html=True
                    )
                    for i, ch in enumerate(de_hien_tai, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl[i] != da_dung:
                            st.error(f"Câu {i} sai. Đúng là: {da_dung}")
                            if ch.get("gt"):
                                st.caption(f"💡 {ch['gt']}")
                        else:
                            st.success(f"Câu {i}: Đúng")

    with tab5:
        hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

# ==================== ĐIỀU HƯỚNG MÀN HÌNH CHÍNH ====================
bai_dang_hoc = ""
du_lieu_bai_hien_tai = {}

st.markdown(css_giao_dien_chung(), unsafe_allow_html=True)

if che_do == "🏠 Trang chủ / Hướng dẫn":
    st.markdown(css_widget_theo_mon("home"), unsafe_allow_html=True)
    st.markdown(
        tao_hero(
            "home", dark_mode,
            nhan="Chào mừng em!",
            chips=["📚 5 môn học", "🎪 Phòng thí nghiệm & Language Lab", "📝 Thi thử", "🦉 Gia sư AI 24/7"],
        ),
        unsafe_allow_html=True
    )

    if DS_TU_CUA_NGAY:
        tu_hn, pa_hn, nghia_hn = DS_TU_CUA_NGAY[datetime.date.today().toordinal() % len(DS_TU_CUA_NGAY)]
        c_w1, c_w2 = st.columns([4, 1])
        with c_w1:
            st.info(f"🌟 **Word of the Day (Từ vựng Tiếng Anh hôm nay):** **{tu_hn}** `{pa_hn}` — *{nghia_hn}*")
        with c_w2:
            if st.button(f"🔊 Nghe '{tu_hn}'", key="btn_wotd_home", use_container_width=True):
                doc_to_an_toan(tu_hn, autoplay=True, lang="en")

    st.markdown("#### 👇 Hôm nay em muốn học môn nào?")
    cot_mon = st.columns(len(MON_SANG_CHU_DE))
    ten_ngan_map = {
        "toan": "Toán",
        "vatly": "Vật lý",
        "hoa": "Hóa học",
        "van": "Ngữ văn",
        "anh": "Tiếng Anh"
    }
    for cot, (mon_o, khoa_o) in zip(cot_mon, MON_SANG_CHU_DE.items()):
        with cot:
            st.markdown(tao_o_mon(khoa_o, dark_mode, dem_chuong_bai(mon_o)[1]), unsafe_allow_html=True)
            ten_ngan = ten_ngan_map.get(khoa_o, "Môn học")
            if st.button(
                f"Vào học {ten_ngan} →",
                key=f"vao_hoc_{khoa_o}",
                use_container_width=True
            ):
                st.session_state["home_jump"] = mon_o
                st.rerun()

    st.markdown("#### 🧭 Học thế nào cho hiệu quả?")
    st.markdown(
        f'<div class="buoc" style="{bien_the_nhe("home", dark_mode)}">'
        '<div class="buoc-o"><span class="buoc-so">1</span>'
        '<p><b>Đọc lý thuyết</b> và ví dụ trong mục “Học theo chuyên đề”.</p></div>'
        '<div class="buoc-o"><span class="buoc-so">2</span>'
        '<p><b>Luyện bài tập</b> cơ bản, nâng cao và trắc nghiệm, xem gợi ý khi cần.</p></div>'
        '<div class="buoc-o"><span class="buoc-so">3</span>'
        '<p><b>Thi thử & Thực hành</b> – chỗ nào chưa hiểu thì hỏi Gia sư AI.</p></div>'
        '</div>',
        unsafe_allow_html=True
    )

elif che_do == "🔍 Tra cứu / Tìm kiếm":
    st.markdown(css_widget_theo_mon("search"), unsafe_allow_html=True)
    st.markdown(
        tao_hero(
            "search", dark_mode,
            nhan="Tra cứu & Từ điển",
            chips=["📐 Toán", "🔬 Vật lý", "🧪 Hóa học", "📖 Ngữ văn", "🔤 Từ điển Anh-Việt"],
            hien_loi_nhan=False,
        ),
        unsafe_allow_html=True
    )
    tu_khoa = st.text_input(
        "🔎 Nhập từ vựng tiếng Anh hoặc từ khóa bài học:",
        placeholder="Ví dụ: hobby, delicious, Bầy chim chìa vôi, số hữu tỉ, nguyên tử..."
    )
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()

        kq_tu_dien = tra_cuu_tu_anh_viet(kw, cho_phep_ai=False)
        if kq_tu_dien:
            st.markdown("### 🔤 Kết quả Từ điển Anh - Việt (Offline):")
            st.success(f"**{kw}** `{kq_tu_dien.get('pa', '')}` ({kq_tu_dien.get('loai', '')}) — **{kq_tu_dien.get('nghia', '')}**")
            if kq_tu_dien.get("vi_du"):
                st.info(f"💬 **Ví dụ:** *{kq_tu_dien['vi_du']}*\n\n👉 **Dịch:** {kq_tu_dien.get('vi_du_dich', '')}")
            if st.button(f"🔊 Phát âm '{kw}'", key="btn_tts_search_dict"):
                doc_to_an_toan(kw, autoplay=True, lang="en")
            st.divider()
        elif re.fullmatch(r"[a-zA-Z\s\-]{2,30}", kw) and HAS_GENAI and GEMINI_KEYS:
            if st.button(f"🤖 Tra từ '{kw}' bằng Từ điển AI", key="btn_ai_dict_search"):
                with st.spinner("Đang tra cứu..."):
                    kq_ai_td = tra_cuu_tu_anh_viet(kw, cho_phep_ai=True)
                    if kq_ai_td:
                        st.success(f"**{kw}** `{kq_ai_td.get('pa', '')}` ({kq_ai_td.get('loai', '')}) — **{kq_ai_td.get('nghia', '')}**")
                        if kq_ai_td.get("vi_du"):
                            st.info(f"💬 **Ví dụ:** *{kq_ai_td['vi_du']}*\n\n👉 **Dịch:** {kq_ai_td.get('vi_du_dich', '')}")

        ket_qua_tim = []
        for t_mon, l_dict in DATABASE.items():
            for lop, c_dict in l_dict.items():
                for chuong, b_dict in c_dict.items():
                    for t_bai, data in b_dict.items():
                        lt_txt = data.get("ly_thuyet", "").lower()
                        if kw in t_bai.lower() or kw in chuong.lower() or kw in lt_txt:
                            ket_qua_tim.append({
                                "mon": t_mon,
                                "lop": lop,
                                "chuong": chuong,
                                "bai": t_bai
                            })
        st.markdown(f"### 📋 Bài học liên quan: {len(ket_qua_tim)}")
        for idx, item in enumerate(ket_qua_tim, 1):
            tieu_de_exp = f"{idx}. [{item['mon']}] {item['chuong']} - {item['bai']}"
            with st.expander(tieu_de_exp):
                if st.button("Mở bài học", key=f"btn_jump_{idx}"):
                    st.session_state["search_jump"] = item
                    st.rerun()

elif che_do == "⚙️ Trạm Nạp Dữ Liệu":
    st.markdown(css_widget_theo_mon("admin"), unsafe_allow_html=True)
    st.markdown(
        tao_hero(
            "admin", dark_mode,
            nhan="Dành cho giáo viên",
            chips=["📄 Word · PDF · Ảnh · Văn bản", "🤖 AI bóc tách", "✅ Tự kiểm tra cấu trúc"],
            hien_loi_nhan=False,
        ),
        unsafe_allow_html=True
    )
    mk = st.text_input("🔑 Mật khẩu Admin:", type="password")

    SO_LAN_SAI_TOI_DA = 5
    THOI_GIAN_KHOA = 600
    now_ad = time.time()
    with GLOBALS["admin_fail_lock"]:
        ds_sai = GLOBALS["admin_fail_times"]
        while ds_sai and now_ad - ds_sai[0] > THOI_GIAN_KHOA:
            ds_sai.popleft()
        bi_khoa = len(ds_sai) >= SO_LAN_SAI_TOI_DA
        con_lai = int(THOI_GIAN_KHOA - (now_ad - ds_sai[0])) + 1 if bi_khoa else 0

    dang_nhap_dung = False
    if ADMIN_PASS and mk and not bi_khoa:
        dang_nhap_dung = hmac.compare_digest(mk, ADMIN_PASS)
        if not dang_nhap_dung and st.session_state.get("admin_mk_da_kiem") != mk:
            st.session_state["admin_mk_da_kiem"] = mk
            with GLOBALS["admin_fail_lock"]:
                GLOBALS["admin_fail_times"].append(now_ad)

    if not ADMIN_PASS:
        st.error("⚠️ Hệ thống chưa thiết lập ADMIN_PASSWORD trong Secrets.")
    elif bi_khoa:
        st.error(f"🔒 Nhập sai mật khẩu quá nhiều lần. Vui lòng thử lại sau khoảng {con_lai // 60 + 1} phút.")
    elif dang_nhap_dung:
        st.success("Xác thực thành công. Tính năng nạp file đang mở...")
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
            "Bạn chuyển tài liệu bài học thành MỘT đối tượng JSON duy nhất, không kèm lời giải thích, "
            "với đúng các khóa sau:\n"
            '- "ly_thuyet": chuỗi, tóm tắt lý thuyết.\n'
            '- "vi_du": chuỗi, ví dụ minh họa (có thể rỗng).\n'
            '- "cau_hoi": danh sách câu trắc nghiệm, mỗi câu dạng '
            '{"nd": "đề", "da": ["phương án 1", "phương án 2", ...], "d": chỉ số đáp án đúng, đếm từ 0, '
            '"gt": "giải thích ngắn vì sao đúng", "md": "biet" | "hieu" | "van_dung"}.\n'
            '- "bt_co_ban" và "bt_nang_cao": danh sách bài tập, mỗi bài dạng '
            '{"de": "đề bài", "dd": ["đáp án"], "hd": "gợi ý cách làm", "lg": "lời giải chi tiết", '
            '"kieu": "tu_luan" nếu đáp án là câu văn cần trình bày}. '
            'Với đáp án là số hoặc từ ngắn, "dd" chỉ ghi con số/từ đó (có thể ghi nhiều cách viết).\n'
            "Chỉ dùng nội dung có trong tài liệu, không tự bịa thêm. Viết bằng tiếng Việt."
        )
        if not HAS_GENAI:
            st.error("⚠️ Chức năng cần thư viện google-genai. Hãy thêm `google-genai` vào requirements.txt.")
        elif st.button("⚡ Bóc tách dữ liệu", type="primary", use_container_width=True):
            if not danh_sach_files and not raw_text.strip():
                st.warning("⚠️ Vui lòng tải file hoặc dán văn bản!")
            else:
                with st.spinner("🤖 Trợ lý AI đang phân tích cấu trúc..."):
                    try:
                        payload = []
                        for f in danh_sach_files:
                            if f.name.endswith(".docx"):
                                payload.append(trich_xuat_word_docx(f.read()))
                            elif f.name.endswith(".pdf"):
                                payload.append(types.Part.from_bytes(
                                    data=f.read(),
                                    mime_type="application/pdf"
                                ))
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
                        bai_moi, canh_bao = chuan_hoa_bai_hoc(tach_json_tu_van_ban(ket_qua))
                        st.session_state["parsed_lesson"] = bai_moi
                        st.session_state["parsed_warnings"] = canh_bao
                    except Exception as e:
                        ghi_log_loi("Trạm nạp dữ liệu", e)
                        st.error(f"❌ Không bóc tách được dữ liệu: {e}")

        if st.session_state.get("parsed_lesson"):
            bai_moi = st.session_state["parsed_lesson"]
            canh_bao = st.session_state.get("parsed_warnings", [])
            st.success(
                f"✅ Bóc tách xong: {len(bai_moi['cau_hoi'])} câu trắc nghiệm, "
                f"{len(bai_moi['bt_co_ban'])} bài cơ bản, {len(bai_moi['bt_nang_cao'])} bài nâng cao."
            )
            if canh_bao:
                with st.expander(f"⚠️ {len(canh_bao)} cảnh báo cần giáo viên xem lại", expanded=True):
                    for cb in canh_bao:
                        st.markdown(f"- {cb}")
            st.info("📌 Nội dung do AI bóc tách — giáo viên cần kiểm tra lại trước khi đưa vào dữ liệu chính thức.")

            json_out = json.dumps(bai_moi, ensure_ascii=False, indent=2)
            py_out = (
                "# -*- coding: utf-8 -*-\n"
                "# Dữ liệu bài học do Trạm nạp dữ liệu sinh ra. Dán vào đúng Môn > Lớp > Chương > Bài.\n"
                f"BAI_MOI = {json_out}\n"
            )
            c_tai1, c_tai2 = st.columns(2)
            c_tai1.download_button(
                "💾 Tải dữ liệu (.json)",
                data=json_out.encode("utf-8"),
                file_name="bai_moi.json",
                mime="application/json",
                use_container_width=True
            )
            c_tai2.download_button(
                "💾 Tải dữ liệu (.py)",
                data=py_out.encode("utf-8"),
                file_name="data_moi.py",
                mime="text/x-python",
                use_container_width=True
            )
            st.json(bai_moi)
    elif mk:
        st.error("Sai mật khẩu!")

elif che_do == "🎪 Phòng thí nghiệm ảo":
    cho_banner_lab = st.empty()
    ds_mon_lab = [
        "🔤 Môn Tiếng Anh",
        "📖 Môn Ngữ Văn",
        "🔬 Môn Vật lý (KHTN)",
        "🧪 Môn Hóa học (KHTN)",
        "📐 Môn Toán"
    ]
    mon_lab = st.selectbox("🔬 Chọn môn học thực hành:", ds_mon_lab)
    mon = mon_lab
    bai_dang_hoc = f"Phòng thí nghiệm — {mon_lab}"
    khoa_lab = lay_chu_de(mon_lab)
    if khoa_lab == "anh":
        chip_lab = ["🗂️ Flashcard", "🎙️ Luyện phát âm", "🤝 Đóng vai giao tiếp AI", "📖 Từ điển"]
        phu_de_lab = "Trạm thực hành Nghe - Nói và Trau dồi vốn từ vựng"
    elif khoa_lab == "van":
        chip_lab = ["🗺️ Sơ đồ tác phẩm", "🎭 Thế giới nhân vật", "📝 Lập dàn ý"]
        phu_de_lab = "Khám phá tác phẩm qua sơ đồ, nhân vật và dàn ý"
    else:
        chip_lab = ["🧪 Mô phỏng tương tác", "🌐 PhET – ĐH Colorado", "🖱️ Kéo, thả, tự thử nghiệm"]
        phu_de_lab = "Tự tay làm thí nghiệm – quan sát, thay đổi, rút ra kết luận"

    cho_banner_lab.markdown(
        css_widget_theo_mon(khoa_lab) + tao_hero(
            khoa_lab, dark_mode,
            nhan="Phòng thí nghiệm ảo / Thực hành",
            phu_de=phu_de_lab,
            chips=chip_lab,
        ),
        unsafe_allow_html=True
    )
    hien_thi_phong_thi_nghiem(mon_lab, key_prefix="main_lab")

elif che_do == "📖 Học theo chuyên đề":
    khoa_mon = lay_chu_de(mon)
    so_chuong, so_bai_mon = dem_chuong_bai(mon)
    st.markdown(css_widget_theo_mon(khoa_mon), unsafe_allow_html=True)
    st.markdown(
        tao_hero(
            khoa_mon, dark_mode,
            nhan="Học theo chuyên đề · Lớp 7",
            chips=[
                "📚 Kết nối tri thức",
                f"📂 {so_chuong} chương · {so_bai_mon} bài" if so_bai_mon else "🛠️ Đang cập nhật bài học",
                chip_thanh_tich(mon),
            ],
        ),
        unsafe_allow_html=True
    )

    lop_dict = DATABASE.get(mon) or {}
    if not lop_dict:
        st.warning("⚠️ Dữ liệu đang được cập nhật...")
    else:
        c_lop, c_chuong, c_bai = st.columns([1, 2, 2])
        ds_lop = list(lop_dict.keys())
        giu_lua_chon_hop_le("s_lop", ds_lop)
        lop = c_lop.selectbox("Khối:", ds_lop, key="s_lop")
        chuong_dict = lop_dict[lop]
        ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
        giu_lua_chon_hop_le("s_chuong", ds_chuong)
        chuong = c_chuong.selectbox("Chương / Unit:", ds_chuong, key="s_chuong")

        bai_dict = chuong_dict[chuong]
        ds_bai = list(bai_dict.keys())
        if not ds_bai:
            st.info("📌 Chương này đang được cập nhật bài học.")
            bai_dang_hoc = chuong
        else:
            giu_lua_chon_hop_le("s_bai", ds_bai)
            bai = c_bai.selectbox("Bài học / Lesson:", ds_bai, key="s_bai")

            bai_dang_hoc = f"{chuong} - {bai}"
            du_lieu_bai_hien_tai = bai_dict[bai]

            hien_thi_bai(mon, lop, chuong, bai, du_lieu_bai_hien_tai)

elif che_do == "📝 Phòng thi / Kiểm tra":
    khoa_mon = lay_chu_de(mon)
    st.markdown(css_widget_theo_mon(khoa_mon), unsafe_allow_html=True)
    st.markdown(
        tao_hero(
            khoa_mon, dark_mode,
            nhan="Phòng thi thử · Kiểm tra định kì",
            chips=["⏱️ 15 phút · Giữa kì · Học kì", "🔀 Đề trộn ngẫu nhiên", chip_thanh_tich(mon)],
        ),
        unsafe_allow_html=True
    )
    lop_dict = DATABASE.get(mon) or {}
    if lop_dict:
        ds_lop_thi = list(lop_dict.keys())
        giu_lua_chon_hop_le("s_lop_thi", ds_lop_thi)
        lop = st.selectbox("Khối:", ds_lop_thi, key="s_lop_thi")
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
            chuong_chon = st.multiselect("Chọn chương / Unit:", ds_chuong, default=ds_chuong)

        mapping_cau = {
            "Kiểm tra 15 phút (10 câu)": 10,
            "Giữa kì (20 câu)": 20,
            "Học kì (40 câu)": 40
        }
        khoa_de = f"dethi_{mon}_{lop}"
        khoa_nonce = f"nonce_thi_{mon}_{lop}"
        khoa_cau_hinh = f"cauhinh_thi_{mon}_{lop}"

        cau_hinh_hien_tai = (loai_de, tuple(chuong_chon))
        if st.session_state.get(khoa_cau_hinh) != cau_hinh_hien_tai:
            st.session_state[khoa_cau_hinh] = cau_hinh_hien_tai
            st.session_state[khoa_de] = None

        if st.button("🚀 TẠO ĐỀ THI LẠI / MỚI", type="primary"):
            st.session_state[khoa_de] = None

        if st.session_state.get(khoa_de) is None:
            all_questions = []
            tap_on_tap = set()
            for c in chuong_chon:
                for b, data in chuong_dict[c].items():
                    all_questions.extend(data.get("cau_hoi", []))
                    for k_ot in data.get("on_tap", []):
                        tap_on_tap.add(k_ot)

            if "Tiếng Anh" in mon and tap_on_tap and KIEN_THUC_NEN:
                cau_on_tap = []
                for k_ot in tap_on_tap:
                    if k_ot in KIEN_THUC_NEN:
                        ten_cd = KIEN_THUC_NEN[k_ot].get("ten", "Ôn tập")
                        for ch_p in KIEN_THUC_NEN[k_ot].get("cau_hoi", []):
                            bs = dict(ch_p)
                            bs["nd"] = f"🔄 [{ten_cd}] {bs['nd']}"
                            cau_on_tap.append(bs)
                if cau_on_tap:
                    so_luong_muc_tieu = mapping_cau[loai_de]
                    so_on = min(len(cau_on_tap), max(1, round(so_luong_muc_tieu * 0.3)))
                    so_chinh = min(len(all_questions), max(0, so_luong_muc_tieu - so_on))
                    all_questions = random.sample(all_questions, so_chinh) + random.sample(cau_on_tap, so_on)
                    random.shuffle(all_questions)

            if not all_questions:
                st.error("❌ Chưa có câu hỏi trong chương này!")
            else:
                so_luong = min(mapping_cau[loai_de], len(all_questions))
                ds_chon = random.sample(all_questions, so_luong)
                de_tron_thi = []
                for ch in ds_chon:
                    da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                    nd_ch = ch.get("nd") or ch.get("de")
                    de_tron_thi.append({"nd": nd_ch, "da": da_moi, "d": vt_moi, "gt": ch.get("gt", "")})
                st.session_state[khoa_de] = de_tron_thi
                st.session_state[khoa_nonce] = uuid.uuid4().hex[:8]

        if st.session_state.get(khoa_de):
            de_thi = st.session_state[khoa_de]
            nonce_thi = st.session_state.setdefault(khoa_nonce, "0")
            st.markdown(
                tao_dai_de_thi(khoa_mon, dark_mode, loai_de.split(" (")[0], len(de_thi)),
                unsafe_allow_html=True
            )
            with st.form(f"form_thi_{mon}_{lop}"):
                tl_thi = {}
                for i, ch in enumerate(de_thi, 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl_thi[i] = st.radio(
                        f"Đ/á {i}:",
                        ch["da"],
                        key=f"thi_{mon}_{lop}_{nonce_thi}_{i}",
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
                        f"""<div class="diem-thi">🏆 ĐIỂM: {diem:.1f} / 10 ({dung}/{len(de_thi)} câu)</div>""",
                        unsafe_allow_html=True
                    )
                    for i, ch in enumerate(de_thi, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl_thi[i] != da_dung:
                            st.error(f"❌ Câu {i}: Sai (Đúng: **{da_dung}**)")
                            if ch.get("gt"):
                                st.caption(f"💡 {ch['gt']}")
                        else:
                            st.success(f"✅ Câu {i}: Đúng")
    else:
        st.warning("⚠️ Môn này chưa có dữ liệu câu hỏi, đang được cập nhật...")

# ==================== KHU VỰC GIA SƯ AI ====================
if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra", "🎪 Phòng thí nghiệm ảo"]:
    st.divider()
    st.markdown(
        tao_banner_gia_su(
            che_do_toi=dark_mode,
            bai_hien_tai=bai_dang_hoc,
            ai_san_sang=bool(HAS_GENAI and GEMINI_KEYS),
            co_anh=HAS_PIL,
            co_mic=HAS_MIC,
        ),
        unsafe_allow_html=True
    )

    DS_MON_AI = ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn", "Tiếng Anh"]
    MON_SANG_MON_AI = {
        "📐 Môn Toán": "Toán",
        "🔬 Môn Vật lý (KHTN)": "Vật Lý",
        "🧪 Môn Hóa học (KHTN)": "Hóa Học",
        "📖 Môn Ngữ Văn": "Ngữ Văn",
        "🔤 Môn Tiếng Anh": "Tiếng Anh",
    }
    mon_mac_dinh_ai = MON_SANG_MON_AI.get(mon, "Toán")

    col1, col2, col3, col4 = st.columns([2.5, 0.9, 1.6, 1])
    with col1:
        mon_ai = st.radio(
            "Môn:",
            DS_MON_AI,
            index=DS_MON_AI.index(mon_mac_dinh_ai),
            horizontal=True,
            label_visibility="collapsed"
        )
    with col2:
        tu_dong_doc = st.checkbox("🔊 Đọc to", value=False)
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
        f"Bạn là gia sư {mon_ai} lớp 7 sách Kết Nối Tri Thức (Global Success nếu là Tiếng Anh). "
        f"Đang học: {bai_dang_hoc}. Gợi mở từng bước ngắn gọn, dễ hiểu, không giải hộ hoàn toàn."
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
        if not HAS_GENAI:
            st.error("⚠️ Gia sư AI đang tắt vì server chưa cài thư viện google-genai.")
        elif not GEMINI_KEYS:
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
                        g_hist = []
                        for m in st.session_state.chat_history[:-1]:
                            if m.get("loi"):
                                if g_hist and g_hist[-1]["role"] == "user":
                                    g_hist.pop()
                                continue
                            g_hist.append({
                                "role": "user" if m["role"] == "user" else "model",
                                "parts": [m["content"]]
                            })
                        luu_kq = ""
                        la_loi = False
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
                        except Exception as e:
                            ghi_log_loi("Gia sư AI", e)
                            la_loi = True
                            luu_kq = "⚠️ Đường truyền AI đang bận xử lý, em thử lại câu hỏi sau vài giây nhé."
                            st.error(luu_kq)

                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": luu_kq,
                            "loi": la_loi
                        })
                        if h_key and not la_loi:
                            luu_cache_ai(h_key, luu_kq)
                        if luu_kq and not la_loi:
                            doc_to_an_toan(luu_kq, autoplay=tu_dong_doc)
