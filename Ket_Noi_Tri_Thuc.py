# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Tích hợp Toàn diện Tiếng Anh (Từ điển + Từ của ngày) & Sửa lỗi NameError
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
    ds_ten_key = ["GEMINI_API_KEY", "GEMINI_API_KEY_1", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"]
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

def cap_nhat_nguoi_online():
    with GLOBALS["user_count_lock"]:
        if "user_id" not in st.session_state:
            st.session_state.user_id = str(uuid.uuid4())
        bo_nho = GLOBALS["online_users"]
        bo_nho[st.session_state.user_id] = time.time()
        now = time.time()
        ds_online = {uid: t for uid, t in bo_nho.items() if now - t < 300}
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
    if now - last_time < cooldown_seconds:
        return False, int(cooldown_seconds - (now - last_time)) + 1
    gioi_han = lay_gioi_han_toan_cuc()
    with GLOBALS["rate_lock"]:
        hang_doi = GLOBALS["ai_request_times"]
        while hang_doi and now - hang_doi[0] > 60:
            hang_doi.popleft()
        if len(hang_doi) >= gioi_han:
            return False, int(60 - (now - hang_doi[0])) + 1
        hang_doi.append(now)
    st.session_state["last_ai_request_time"] = now
    return True, 0

def tao_ma_hash_cau_hoi(mon_hoc, bai_hoc, che_do, cau_hoi):
    c_clean = re.sub(r'\s+', ' ', cau_hoi.strip().lower())
    return hashlib.md5(f"{mon_hoc.strip()}_{bai_hoc.strip()}_{che_do}_{c_clean}".encode("utf-8")).hexdigest()

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
        if re.sub(r'\s+', '', str(nd).lower()) == re.sub(r'\s+', '', str(d).lower()):
            return True
    return False

PHUONG_AN_CO_DINH = re.compile(r'\b(?:tất cả|cả hai|cả ba|cả [a-d]|đáp án|phương án)\b', re.IGNORECASE)

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
    st.session_state.lich_su_hoc_tap.insert(0, {"bai": tieu_de_bai, "diem": diem, "dung": dung, "tong": tong, "mon": mon})

def thanh_tich_mon(mon):
    ds = [x for x in st.session_state.get("lich_su_hoc_tap", []) if x.get("mon") == mon]
    if not ds:
        return 0, None
    return len(ds), sum(x["diem"] for x in ds) / len(ds)

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ').replace('^2', ' bình phương ').replace('^3', ' lập phương ')
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
        return "\n".join(["".join([t.text for t in p.iter(f"{ns}t") if t.text]) for p in tree.iter(f"{ns}p") if any(t.text for t in p.iter(f"{ns}t"))])
    except Exception as e:
        return f"[Lỗi đọc file Word: {e}]"

def ghi_log_loi(nguon, loi):
    try:
        thong_bao = str(loi)
        for k in GEMINI_KEYS + [DOLA_KEY]:
            if k:
                thong_bao = thong_bao.replace(k, "***")
        print(f"[LỖI] {nguon}: {type(loi).__name__}: {thong_bao[:500]}", flush=True)
    except Exception:
        pass

MODEL_UU_TIEN = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
TU_KHOA_MODEL_LOAI_TRU = ("tts", "image", "live", "embedding", "transcribe", "omni", "banana", "robotics", "audio")

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
            if "gemini" not in ten or any(k in ten for k in TU_KHOA_MODEL_LOAI_TRU):
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
        cac_phan = [types.Part.from_text(text=str(p)) for p in h.get("parts", []) if str(p).strip()]
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
    cau_hinh = types.GenerateContentConfig(system_instruction=system_instruction, response_mime_type="application/json") if tra_ve_json else types.GenerateContentConfig(system_instruction=system_instruction)
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
                        chat_s = client.chats.create(model=ten_m, config=cau_hinh, history=lich_su)
                        txt = chat_s.send_message(payload).text
                    else:
                        txt = client.models.generate_content(model=ten_m, contents=payload, config=cau_hinh).text
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

def tach_json_tu_van_ban(van_ban):
    s = str(van_ban).strip()
    s = re.sub(r'^```(?:json)?\s*|\s*```$', '', s)
    dau, cuoi = s.find("{"), s.rfind("}")
    if dau == -1 or cuoi <= dau:
        raise ValueError("Không tìm thấy dữ liệu JSON trong phản hồi của AI.")
    return json.loads(s[dau:cuoi + 1])

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
try:
    # Import toàn bộ tính năng từ data_anh.py
    from data_anh import ANH, KIEN_THUC_NEN, TU_DIEN_OFFLINE, DS_TU_CUA_NGAY
except ImportError:
    ANH, KIEN_THUC_NEN, TU_DIEN_OFFLINE, DS_TU_CUA_NGAY = {}, {}, {}, []

VAN_DEFAULT = {
    "Lớp 7": {
        "Bài 1: Bầu trời tuổi thơ (Truyện)": {
            "Văn bản 1: Bầy chim chìa vôi (Nguyễn Quang Thiều)": {
                "ly_thuyet": "Truyện kể về hai anh em Mon và Mên lo lắng cho bầy chim chìa vôi non.",
                "cau_hoi": [{"nd": "Truyện 'Bầy chim chìa vôi' là của tác giả nào?", "da": ["Đoàn Giỏi", "Nguyễn Quang Thiều", "Võ Quảng"], "d": 1}],
                "bt_co_ban": [{"de": "Chi tiết nào cho thấy sự lo lắng?", "dd": ["Thao thức giữa đêm"], "lg": "Chú ý hành động thao thức."}]
            }
        }
    }
}
try:
    from data_van import VAN
except ImportError:
    VAN = VAN_DEFAULT

DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA if HOA else {"Lớp 7": {"Chương 1: Đang cập nhật": {}}},
    "📖 Môn Ngữ Văn": VAN,
    "🔤 Môn Tiếng Anh": ANH
}

# KHỞI TẠO BIẾN 'mon' AN TOÀN TOÀN CỤC CHỐNG LỖI NAMEERROR
mon_mac_dinh = list(DATABASE.keys())[0] if DATABASE else "📐 Môn Toán"
mon = mon_mac_dinh

CHU_DE_GIAO_DIEN = {
    "toan": {"icon": "📐", "ten": "Môn Toán", "sang": ("#1E3A8A", "#2563EB", "#0284C7"), "toi": ("#172554", "#1E40AF", "#075985"), "nhan": "#FDE047", "chinh": "#2563EB", "khau_hieu": "Tư duy logic", "ky_hieu": ["π", "√"], "loi_nhan": ["Mỗi bài toán khó là một câu đố đang chờ em giải mã!"]},
    "vatly": {"icon": "🔬", "ten": "Vật lý", "sang": ("#1E1B4B", "#4C1D95", "#7C3AED"), "toi": ("#0F0A2E", "#2E1065", "#5B21B6"), "nhan": "#FACC15", "chinh": "#7C3AED", "khau_hieu": "Khám phá thế giới", "ky_hieu": ["⚡", "🔭"], "loi_nhan": ["Mọi hiện tượng quanh em đều có lời giải thích khoa học."]},
    "hoa": {"icon": "🧪", "ten": "Hóa học", "sang": ("#064E3B", "#047857", "#0D9488"), "toi": ("#022C22", "#065F46", "#115E59"), "nhan": "#A3E635", "chinh": "#059669", "khau_hieu": "Thế giới nguyên tử", "ky_hieu": ["⚛", "H₂O"], "loi_nhan": ["Thí nghiệm hôm nay, phát minh ngày mai!"]},
    "van": {"icon": "📖", "ten": "Ngữ văn", "sang": ("#881337", "#BE123C", "#C2410C"), "toi": ("#4C0519", "#881337", "#9A3412"), "nhan": "#FDE68A", "chinh": "#E11D48", "khau_hieu": "Chân trời sách", "ky_hieu": ["✒️", "🌸"], "loi_nhan": ["Đọc chậm một chút, em sẽ nghe thấy tiếng lòng của nhân vật."]},
    "anh": {"icon": "🔤", "ten": "Môn Tiếng Anh", "sang": ("#0F766E", "#0D9488", "#14B8A6"), "toi": ("#042F2E", "#115E59", "#0F766E"), "nhan": "#FDE047", "chinh": "#0D9488", "khau_hieu": "Global Success – Chinh phục ngoại ngữ", "ky_hieu": ["abc", "🎧"], "loi_nhan": ["Practice makes perfect! Đừng ngại nói sai."]},
    "home": {"icon": "🎓", "ten": "Trang chủ", "sang": ("#3730A3", "#6D28D9", "#DB2777"), "toi": ("#1E1B4B", "#4C1D95", "#831843"), "nhan": "#FDE047", "chinh": "#6D28D9", "khau_hieu": "Hệ thống Học tập Kết nối tri thức", "ky_hieu": ["🎓"], "loi_nhan": ["Mỗi ngày học một chút, cả năm tiến một đoạn dài!"]},
    "search": {"icon": "🔍", "ten": "Tìm kiếm", "sang": ("#0C4A6E", "#0369A1", "#0E7490"), "toi": ("#082F49", "#0C4A6E", "#164E63"), "nhan": "#FDE047", "chinh": "#0369A1", "khau_hieu": "Tra cứu bài học & Từ điển Offline", "ky_hieu": ["🔎"], "loi_nhan": ["Biết cách tìm kiếm là đã đi được nửa đường tới câu trả lời."]},
    "admin": {"icon": "⚙️", "ten": "Admin", "sang": ("#1F2937", "#334155", "#475569"), "toi": ("#030712", "#111827", "#1F2937"), "nhan": "#38BDF8", "chinh": "#0284C7", "khau_hieu": "Quản trị Dữ liệu", "ky_hieu": ["⚙️"], "loi_nhan": ["Dữ liệu được kiểm tra kĩ – bài học đến tay học sinh mới chuẩn."]}
}

MON_SANG_CHU_DE = {
    "📐 Môn Toán": "toan",
    "🔬 Môn Vật lý (KHTN)": "vatly",
    "🧪 Môn Hóa học (KHTN)": "hoa",
    "📖 Môn Ngữ Văn": "van",
    "🔤 Môn Tiếng Anh": "anh"
}

MO_TA_MON_TRANG_CHU = {
    "toan": "Số hữu tỉ, số thực, hình học.",
    "vatly": "Tốc độ, âm thanh, ánh sáng.",
    "hoa": "Nguyên tử, phân tử.",
    "van": "Truyện, thơ, tùy bút.",
    "anh": "12 Unit Global Success, từ điển."
}

VI_TRI_KY_HIEU = [
    (8, 62, 2.2, 0), (40, 74, 1.6, 1.2), (10, 86, 2.8, 2.4), (52, 90, 1.9, 0.6),
    (30, 54, 1.3, 3.0), (22, 70, 1.4, 1.8), (5, 42, 1.2, 4.0), (44, 60, 1.1, 2.8),
]

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
        ".hb-than{position:relative;z-index:1;display:flex;align-items:center;gap:1.1rem;flex-wrap:wrap;}"
        ".hb-icon{flex:0 0 76px;width:76px;height:76px;border-radius:22px;display:flex;"
        "align-items:center;justify-content:center;font-size:2.6rem;background:rgba(255,255,255,.16);"
        "border:2px solid rgba(255,255,255,.38);}"
        ".hb-chu{flex:1 1 280px;min-width:0;}"
        ".hb-nhan{display:inline-block;font-size:.72rem;font-weight:800;letter-spacing:.06em;"
        "text-transform:uppercase;padding:3px 10px;border-radius:999px;background:var(--nhan);"
        "color:#1F2937;margin-bottom:.4rem;}"
        ".hb-tieu-de{margin:0;font-size:2rem;font-weight:800;line-height:1.15;color:#FFFFFF !important;}"
        ".hb-phu{margin:.3rem 0 0;font-size:1rem;color:#FFFFFF !important;opacity:.95;}"
        ".hb-loi-nhan{position:relative;z-index:1;margin-top:1rem;padding:.6rem .9rem;border-radius:12px;"
        "font-size:.93rem;background:rgba(0,0,0,.26);border-left:4px solid var(--nhan);color:#FFFFFF;}"
        ".hb-loi-nhan b{color:var(--nhan);}"
        ".om{"
            "position:relative;overflow:hidden;border-radius:18px;padding:1.2rem;"
            "height:210px;display:flex;flex-direction:column;justify-content:space-between;"
            "color:#fff;margin-bottom:.5rem;"
            "background:linear-gradient(150deg,var(--c1) 0%,var(--c2) 60%,var(--c3) 100%);"
            "box-shadow:0 12px 26px -14px var(--c2);"
        "}"
        ".om-icon{font-size:2.2rem;line-height:1;}"
        ".om-ten{font-size:1.15rem;font-weight:800;margin:.4rem 0 .2rem;color:#FFFFFF !important;}"
        ".om-mo-ta{font-size:.85rem;margin:0;color:#F1F5F9 !important;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;}"
        ".om-so{display:inline-block;font-size:.75rem;font-weight:700;padding:3px 9px;border-radius:999px;background:rgba(255,255,255,.2);color:#FFFFFF;width:fit-content;}"
        "</style>"
    )

def tao_hero(khoa, che_do_toi, nhan, tieu_de=None, phu_de=None, hien_loi_nhan=True):
    cd = CHU_DE_GIAO_DIEN[khoa]
    loi = f'<div class="hb-loi-nhan"><b>💬 Lời nhắn:</b> {html.escape(cd["loi_nhan"][0])}</div>' if hien_loi_nhan else ""
    return (
        f'<div class="hb" style="{bien_mau(khoa, che_do_toi)}">'
        '<div class="hb-than">'
        f'<div class="hb-icon">{cd["icon"]}</div>'
        '<div class="hb-chu">'
        f'<span class="hb-nhan">{html.escape(nhan)}</span>'
        f'<p class="hb-tieu-de">{html.escape(tieu_de or cd["ten"])}</p>'
        f'<p class="hb-phu">{html.escape(phu_de or cd["khau_hieu"])}</p>'
        '</div></div>'
        f'{loi}</div>'
    )

def tao_o_mon(khoa, che_do_toi, so_bai):
    cd = CHU_DE_GIAO_DIEN[khoa]
    return (
        f'<div class="om" style="{bien_mau(khoa, che_do_toi)}">'
        f'<div>'
        f'<div class="om-icon">{cd["icon"]}</div>'
        f'<p class="om-ten">{html.escape(cd["ten"])}</p>'
        f'<p class="om-mo-ta">{html.escape(MO_TA_MON_TRANG_CHU.get(khoa, ""))}</p>'
        f'</div>'
        f'<span class="om-so">{"📚 " + str(so_bai) + " bài học" if so_bai else "🛠️ Đang cập nhật"}</span>'
        '</div>'
    )

def dem_chuong_bai(mon):
    lop_dict = DATABASE.get(mon) or {}
    so_chuong = sum(len(c) for c in lop_dict.values())
    so_bai = sum(len(b) for c in lop_dict.values() for b in c.values())
    return so_chuong, so_bai

with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    dark_mode = st.toggle("🌙 Chế độ tối", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")
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
    
    # Ghi đè biến mon nếu người dùng đang ở trong chế độ cần chọn môn
    if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = mon_mac_dinh  # An toàn 100%, không bao giờ NameError

st.markdown(css_giao_dien_chung(), unsafe_allow_html=True)

def lay_chu_de(mon_hoac_khoa):
    khoa = MON_SANG_CHU_DE.get(mon_hoac_khoa, mon_hoac_khoa)
    return khoa if khoa in CHU_DE_GIAO_DIEN else "home"

if che_do == "🏠 Trang chủ / Hướng dẫn":
    st.markdown(tao_hero("home", dark_mode, "Chào mừng!", tieu_de="Hệ Thống Học Tập Lớp 7"), unsafe_allow_html=True)
    
    # TÍCH HỢP TỪ CỦA NGÀY TỪ DATA_ANH.PY
    if DS_TU_CUA_NGAY:
        tu_hom_nay = DS_TU_CUA_NGAY[datetime.date.today().toordinal() % len(DS_TU_CUA_NGAY)]
        st.success(f"🌟 **Từ vựng Tiếng Anh của ngày:** **{tu_hom_nay[0]}** {tu_hom_nay[1]} — *{tu_hom_nay[2]}*")
        
    cot_mon = st.columns(5)
    for cot, (mon_o, khoa_o) in zip(cot_mon, MON_SANG_CHU_DE.items()):
        with cot:
            st.markdown(tao_o_mon(khoa_o, dark_mode, dem_chuong_bai(mon_o)[1]), unsafe_allow_html=True)
            if st.button(f"Vào học", key=f"vao_{khoa_o}", use_container_width=True):
                st.session_state["home_jump"] = mon_o
                st.rerun()

elif che_do == "🔍 Tra cứu / Tìm kiếm":
    st.markdown(tao_hero("search", dark_mode, "Tra cứu bài học & Từ điển", hien_loi_nhan=False), unsafe_allow_html=True)
    tu_khoa = st.text_input("🔎 Nhập tên bài học hoặc từ vựng tiếng Anh cần tra:", placeholder="Ví dụ: Bầy chim chìa vôi, hello, beautiful...")
    
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        
        # TÍCH HỢP TỪ ĐIỂN OFFLINE TỪ DATA_ANH.PY
        if TU_DIEN_OFFLINE and kw in TU_DIEN_OFFLINE:
            tu_info = TU_DIEN_OFFLINE[kw]
            st.markdown(f"### 🔤 Kết quả tra từ điển:")
            st.success(f"**{kw}** {tu_info['pa']} ({tu_info['loai']}): {tu_info['nghia']}")
            st.info(f"💡 Ví dụ: *{tu_info['vi_du']}* ➔ {tu_info['vi_du_dich']}")
            st.divider()

        ket_qua_tim = []
        for t_mon, l_dict in DATABASE.items():
            for lop, c_dict in l_dict.items():
                for chuong, b_dict in c_dict.items():
                    for t_bai, data in b_dict.items():
                        lt_txt = data.get("ly_thuyet", "").lower()
                        if kw in t_bai.lower() or kw in lt_txt:
                            ket_qua_tim.append({"mon": t_mon, "lop": lop, "chuong": chuong, "bai": t_bai})
                            
        st.markdown(f"### 📋 Tìm thấy {len(ket_qua_tim)} bài học liên quan:")
        for idx, item in enumerate(ket_qua_tim, 1):
            with st.expander(f"{idx}. [{item['mon']}] {item['chuong']} - {item['bai']}"):
                if st.button("Mở bài học này", key=f"btn_jump_{idx}"):
                    st.session_state["search_jump"] = item
                    st.rerun()

elif che_do == "📖 Học theo chuyên đề":
    khoa_mon = lay_chu_de(mon)
    st.markdown(tao_hero(khoa_mon, dark_mode, "Học chuyên đề"), unsafe_allow_html=True)
    lop_dict = DATABASE.get(mon) or {}
    if lop_dict:
        lop = st.selectbox("Khối:", list(lop_dict.keys()), key="s_lop")
        chuong_dict = lop_dict[lop]
        chuong = st.selectbox("Chương / Unit:", list(chuong_dict.keys()), key="s_chuong")
        bai_dict = chuong_dict[chuong]
        bai = st.selectbox("Bài học / Lesson:", list(bai_dict.keys()), key="s_bai")
        st.markdown(f"### 📖 {bai}")
        st.markdown(f"<div style='padding:1.2rem;background:#EFF6FF;border-left:6px solid #2563EB;border-radius:10px;color:#1E293B'><b>Lý thuyết:</b><br>{bai_dict[bai].get('ly_thuyet','')}</div>", unsafe_allow_html=True)
        if "Ngữ Văn" not in mon and "Tiếng Anh" not in mon:
            st.info("📌 Mở tab 'Phòng thí nghiệm ảo' để thực hành các thí nghiệm trực quan liên quan đến bài học này.")

elif che_do == "🎪 Phòng thí nghiệm ảo":
    mon_lab = st.selectbox("Chọn môn:", list(DATABASE.keys()))
    st.markdown(tao_hero(lay_chu_de(mon_lab), dark_mode, "Thực hành"), unsafe_allow_html=True)
    st.info(f"Khu vực phòng thí nghiệm mô phỏng cho {mon_lab} đang được chuẩn bị.")

elif che_do == "📝 Phòng thi / Kiểm tra":
    khoa_mon = lay_chu_de(mon)
    st.markdown(tao_hero(khoa_mon, dark_mode, "Phòng thi thử"), unsafe_allow_html=True)
    st.info(f"Tính năng thi thử môn {mon} với đề trộn ngẫu nhiên.")

else:
    st.markdown(tao_hero("admin", dark_mode, "Quản trị"), unsafe_allow_html=True)
