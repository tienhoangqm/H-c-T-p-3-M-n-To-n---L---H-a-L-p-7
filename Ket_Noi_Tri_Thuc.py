# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Khởi Động An Toàn: Chống sập App tuyệt đối khi mất file Secrets
"""
import streamlit as st
import google.generativeai as genai
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
from collections import OrderedDict

# ==================== CẤU HÌNH TRANG (PHẢI ĐẶT ĐẦU TIÊN) ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7 - Kết Nối Tri Thức",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Xử lý nhảy trang từ tính năng Tìm kiếm trước khi Sidebar render
if "search_jump" in st.session_state:
    item = st.session_state.pop("search_jump")
    st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
    st.session_state["mon_main"] = item["mon"]
    st.session_state["chuong_main"] = item["chuong"]
    st.session_state["bai_main"] = item["bai"]

# Tải khởi động mượt mà chống ngủ đông
with st.spinner("🚀 Hệ thống đang khởi động cỗ máy học tập, bạn chờ chút nhé..."):
    try:
        from streamlit_mic_recorder import speech_to_text
        HAS_MIC = True
    except ImportError:
        HAS_MIC = False

    try:
        from gtts import gTTS
        HAS_TTS = True
    except ImportError:
        HAS_TTS = False

    try:
        from PIL import Image
        HAS_PIL = True
    except ImportError:
        HAS_PIL = False

# ==================== KHỞI TẠO LOCK & CACHE TOÀN CỤC (GLOBAL) ====================
@st.cache_resource
def get_global_locks():
    return {
        "ai_api_lock": threading.Lock(),
        "user_count_lock": threading.Lock(),
        "ai_cache_lock": threading.Lock(),
        "online_users": {},
        "ai_cache": OrderedDict()
    }

GLOBALS = get_global_locks()

# ==================== ĐỌC SECRETS AN TOÀN (CHỐNG SẬP APP) ====================
def get_secret(key_name, default_val=""):
    """Hàm lấy key an toàn, nếu không có file secrets.toml thì không bị sập"""
    try:
        # Bọc an toàn tuyệt đối khi gọi st.secrets
        if key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    return os.getenv(key_name, default_val)

def lay_danh_sach_gemini_keys():
    keys = []
    try:
        val = get_secret("GEMINI_API_KEYS")
        if isinstance(val, list): keys.extend([k.strip() for k in val if str(k).strip()])
        elif isinstance(val, str) and val: keys.extend([k.strip() for k in val.split(",") if k.strip()])
    except Exception: pass

    for k_name in ["GEMINI_API_KEY", "GEMINI_API_KEY_1", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"]:
        k_val = get_secret(k_name)
        if k_val and str(k_val).strip() not in keys: keys.append(str(k_val).strip())
    return keys

GEMINI_KEYS = lay_danh_sach_gemini_keys()
if GEMINI_KEYS:
    try:
        genai.configure(api_key=GEMINI_KEYS[0])
    except Exception:
        pass

DOLA_ENDPOINT = str(get_secret("DOLA_API_ENDPOINT")).strip()
DOLA_KEY = str(get_secret("DOLA_API_KEY")).strip()
DOLA_PROJECT_TIER = str(get_secret("DOLA_PROJECT_TIER", "high_limit_edu")).strip()
ADMIN_PASS = str(get_secret("ADMIN_PASSWORD", "")).strip()

# ==================== HỆ THỐNG ĐẾM NGƯỜI DÙNG & RATE LIMIT ====================
def cap_nhat_nguoi_online():
    with GLOBALS["user_count_lock"]:
        if 'user_id' not in st.session_state:
            st.session_state.user_id = str(uuid.uuid4())
        bo_nho = GLOBALS["online_users"]
        bo_nho[st.session_state.user_id] = time.time()
        now = time.time()
        danh_sach_online = {uid: t for uid, t in bo_nho.items() if now - t < 300}
        bo_nho.clear()
        bo_nho.update(danh_sach_online)
        return len(bo_nho)

def kiem_tra_gioi_han_tan_suat(cooldown_seconds=4):
    now = time.time()
    last_time = st.session_state.get("last_ai_request_time", 0.0)
    elapsed = now - last_time
    if elapsed < cooldown_seconds:
        return False, int(cooldown_seconds - elapsed) + 1
    st.session_state["last_ai_request_time"] = now
    return True, 0

# ==================== CACHE AI THÔNG MINH ====================
def tao_ma_hash_cau_hoi(mon_hoc, bai_hoc, che_do, cau_hoi):
    c_clean = re.sub(r'\s+', ' ', cau_hoi.strip().lower())
    chuoi_chuan = f"{mon_hoc.strip()}_{bai_hoc.strip()}_{che_do}_{c_clean}"
    return hashlib.md5(chuoi_chuan.encode('utf-8')).hexdigest()

def luu_cache_ai(ma_hash, noi_dung):
    nd_lower = noi_dung.lower()
    if any(k in nd_lower for k in ["bận", "quá tải", "lỗi", "chuyển sang", "bảo trì"]) or "⚠️" in noi_dung:
        return
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        cache[ma_hash] = noi_dung
        cache.move_to_end(ma_hash)
        if len(cache) > 100: cache.popitem(last=False)

def lay_cache_ai(ma_hash):
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        if ma_hash in cache:
            cache.move_to_end(ma_hash)
            return cache[ma_hash]
    return None

# ==================== HÀM TIỆN ÍCH CHẤM SỐ HỌC & TRẮC NGHIỆM ====================
def ep_kieu_so_hoc(chuoi):
    s = str(chuoi).strip().replace(" ", "")
    if not s: return None
    if '/' in s:
        parts = s.split('/')
        if len(parts) == 2:
            try: return float(parts[0]) / float(parts[1])
            except: return None
    if re.fullmatch(r'-?\d{1,3}(\.\d{3})+(,\d+)?', s):
        s = s.replace('.', '').replace(',', '.')
    else:
        s = s.replace(',', '.')
    try: return float(s)
    except ValueError: return None

def so_sanh_so_hoc(nd, ds_dung):
    val_x = ep_kieu_so_hoc(nd)
    for d in ds_dung:
        val_d = ep_kieu_so_hoc(d)
        if val_x is not None and val_d is not None:
            if abs(val_x - val_d) < 1e-5: return True
        if re.sub(r'\s+', '', str(nd).lower()) == re.sub(r'\s+', '', str(d).lower()): return True
    return False

def tron_dap_an_thong_minh(ch):
    da_goc = list(ch["da"])
    d_dung = da_goc[ch["d"]]
    for ans in da_goc:
        txt = str(ans).lower()
        if "cả" in txt or "tất cả" in txt or "đáp án" in txt or "phương án" in txt or "a, b" in txt:
            return da_goc, ch["d"]
    random.shuffle(da_goc)
    return da_goc, da_goc.index(d_dung)

def lam_sach_id(s): return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))
def sap_xep_chuong(ds_chuong):
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)

def ghi_nhan_lich_su(tieu_de_bai, diem, dung, tong):
    if 'lich_su_hoc_tap' not in st.session_state: st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {"bai": tieu_de_bai, "diem": diem, "dung": dung, "tong": tong})

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\mathbb{Q}', 'Q').replace(r'\mathbb{Z}', 'Z').replace(r'\mathbb{N}', 'N').replace(r'\mathbb{R}', 'R')
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ').replace(r'\div', ' chia ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    s = re.sub(r'[^\w\s,.?!:;()+\-*/=<>%àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]', '', s)
    return re.sub(r'\s+', ' ', s).strip()

def doc_to_an_toan(text, autoplay=True):
    if not HAS_TTS or not text: return
    try:
        clean_text = lam_sach_van_ban_doc(text)
        if clean_text:
            afp = io.BytesIO()
            gTTS(text=clean_text, lang='vi').write_to_fp(afp)
            afp.seek(0)
            st.audio(afp, format='audio/mp3', autoplay=autoplay)
    except Exception:
        pass

# ==================== MÔ-ĐUN AI (CÓ LOCK) ====================
def goi_dola_toi_uu(cau_hoi):
    if not DOLA_ENDPOINT or not DOLA_KEY: return None
    try:
        phan_hoi = requests.post(
            DOLA_ENDPOINT,
            headers={"Authorization": f"Bearer {DOLA_KEY}", "X-Project-Quota-Tier": DOLA_PROJECT_TIER},
            json={"cau_hoi": cau_hoi, "chuong_trinh": "ket_noi_tri_thuc_lop7", "che_do": "chuan_sgk"},
            timeout=4.0
        )
        if phan_hoi.status_code == 200:
            nd = phan_hoi.json().get("noi_dung_chuan", "")
            return nd.strip() if nd else None
        return None
    except: return None

@st.cache_resource(ttl=3600, show_spinner=False)
def lay_ds_model_kha_dung(api_key):
    uu_tien = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
    try:
        genai.configure(api_key=api_key)
        ds_hien_co = [m.name.replace("models/", "") for m in genai.list_models() if "generateContent" in getattr(m, "supported_generation_methods", [])]
        if ds_hien_co: return [m for m in uu_tien if m in ds_hien_co] + [m for m in ds_hien_co if "gemini" in m and m not in uu_tien]
    except: pass
    return uu_tien

def goi_gemini_an_toan(payload, system_instruction, history=None):
    if not GEMINI_KEYS: raise RuntimeError("Chưa cấu hình GEMINI_API_KEY. Vui lòng thêm vào Secrets.")
    if "key_index" not in st.session_state: st.session_state["key_index"] = 0
    so_luong_key = len(GEMINI_KEYS)
    last_err = None

    with GLOBALS["ai_api_lock"]:
        for k_offset in range(so_luong_key):
            idx = (st.session_state["key_index"] + k_offset) % so_luong_key
            current_key = GEMINI_KEYS[idx]
            genai.configure(api_key=current_key)
            ds_models = lay_ds_model_kha_dung(current_key)

            for ten_m in ds_models:
                for attempt in range(2):
                    try:
                        m = genai.GenerativeModel(model_name=ten_m, system_instruction=system_instruction)
                        if history is not None:
                            chat_s = m.start_chat(history=history)
                            txt = chat_s.send_message(payload).text
                        else:
                            txt = m.generate_content(payload).text
                        st.session_state["key_index"] = idx
                        return txt
                    except Exception as e:
                        last_err = e
                        err_str = str(e).lower()
                        if "404" in err_str or "not found" in err_str: break
                        elif "429" in err_str or "quota" in err_str:
                            if attempt == 0: time.sleep(1.0); continue
                            else: break
                        else: break
    raise last_err

# ==================== DATA & GIAO DIỆN CHÍNH ====================
try: from data_toan import TOAN
except ImportError: TOAN = {}
try: from data_vatly import VATLY
except ImportError: VATLY = {}
try: from data_hoa import HOA
except ImportError: HOA = {}

VAN = {
    "Lớp 7": {
        "Chương 1: Bầu trời tuổi thơ (Truyện)": {
            "Văn bản 1: Bồng chanh đỏ (trích, Đỗ Chu)": {
                "ly_thuyet": "Truyện ngắn kể về hai anh em Hoài và Ý với tình yêu thương loài vật, thiên nhiên.",
                "cau_hoi": [
                    {"nd": "Truyện 'Bồng chanh đỏ' của tác giả nào?", "da": ["Đỗ Chu", "Tô Hoài", "Khánh Hoài"], "d": 0},
                    {"nd": "Nhân vật chính là ai?", "da": ["Anh em Hoài Ý", "Ông nội", "Thành và Thủy"], "d": 0}
                ],
                "bt_co_ban": [{"de": "Ý nghĩa nhan đề?", "dd": ["Vẻ đẹp thiên nhiên"], "lg": "Biểu tượng tuổi thơ."}],
                "bt_nang_cao": [{"de": "Tâm trạng nhân vật Hoài?", "dd": ["Thấu hiểu và buông bỏ"], "lg": "Sự nhân hậu."}]
            }
        }
    }
}
DATABASE = {"📐 Môn Toán": TOAN, "🔬 Môn Vật lý (KHTN)": VATLY, "🧪 Môn Hóa học (KHTN)": HOA, "📖 Môn Ngữ Văn": VAN}

# Sidebar
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    dark_mode = st.toggle("🌙 Chế độ tối", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")
    
    if not GEMINI_KEYS:
        st.warning("⚠️ Ứng dụng chưa có API Key, đang chạy ở chế độ giao diện Mẫu.")
        
    st.divider()
    
    che_do = st.radio("⚙️ Chức năng:", ["🏠 Trang chủ / Hướng dẫn", "🔍 Tra cứu / Tìm kiếm", "📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra", "🎪 Phòng thí nghiệm ảo", "⚙️ Trạm Nạp Dữ Liệu"], key="che_do_sidebar")
    
    if che_do == "📖 Học theo chuyên đề" or che_do == "📝 Phòng thi / Kiểm tra":
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = che_do

    if 'lich_su_hoc_tap' in st.session_state and st.session_state.lich_su_hoc_tap:
        st.divider()
        st.markdown("### 📊 Lịch sử học tập")
        so_bai = len(st.session_state.lich_su_hoc_tap)
        st.metric("Điểm TB", f"{sum(i['diem'] for i in st.session_state.lich_su_hoc_tap) / so_bai:.1f}", f"{so_bai} bài")

# CSS Tiêm sau khi khai báo biến dark_mode
if dark_mode:
    st.markdown("""<style>.stApp { background-color: #0F172A; color: #F1F5F9; } .main .block-container { padding-top: 1.2rem; max-width: 95%; } [data-testid="stToolbarActions"], footer { display: none !important; } .card-home { background-color: #1E293B; border: 1px solid #334155; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; color: #F1F5F9; } .khung-lythuyet { background-color: #1E293B; padding: 1.2rem; border-left: 6px solid #3B82F6; } .diem-thi { font-size: 1.6rem; color: #F87171; text-align: center; padding: 1.2rem; border: 2px dashed #EF4444; }</style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>.main .block-container { padding-top: 1.2rem; max-width: 95%; } [data-testid="stToolbarActions"], footer { display: none !important; } .card-home { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; } .khung-lythuyet { background-color: #EFF6FF; padding: 1.2rem; border-left: 6px solid #2563EB; } .diem-thi { font-size: 1.6rem; color: #E11D48; text-align: center; padding: 1.2rem; border: 2px dashed #F43F5E; }</style>""", unsafe_allow_html=True)

# Hiển thị tính năng
bai_dang_hoc = ""
du_lieu_bai_hien_tai = {}

if che_do == "🏠 Trang chủ / Hướng dẫn":
    st.markdown("""<h2>🎓 HỆ THỐNG HỌC TẬP THCS — KẾT NỐI TRI THỨC (LỚP 7)</h2>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.markdown("<div class='card-home'><h3>🌟 Tính năng nổi bật</h3><p>Học tập chuyên đề, Tra cứu thông minh, Mô phỏng tương tác.</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='card-home'><h3>💬 Gia Sư AI An Toàn</h3><p>Bộ đệm tốc độ cao, luân phiên khóa API chống sập.</p></div>", unsafe_allow_html=True)

elif che_do == "🔍 Tra cứu / Tìm kiếm":
    tu_khoa = st.text_input("🔎 Nhập từ khóa:")
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        for t_mon, l_dict in DATABASE.items():
            for lop, c_dict in l_dict.items():
                for chuong, b_dict in c_dict.items():
                    for t_bai, data in b_dict.items():
                        if kw in t_bai.lower() or kw in data.get("ly_thuyet", "").lower():
                            with st.expander(f"[{t_mon}] {chuong} - {t_bai}"):
                                if st.button("Mở bài học", key=f"btn_{t_bai}"):
                                    st.session_state["search_jump"] = {"mon": t_mon, "chuong": chuong, "bai": t_bai}
                                    st.rerun()

elif che_do == "⚙️ Trạm Nạp Dữ Liệu":
    mk = st.text_input("🔑 Mật khẩu Admin:", type="password")
    if not ADMIN_PASS:
        st.error("⚠️ Hệ thống chưa thiết lập ADMIN_PASSWORD trong Secrets. Tính năng bị khóa.")
    elif mk and hmac.compare_digest(mk, ADMIN_PASS):
        st.success("Xác thực thành công. Tính năng nạp file đang mở...")
    elif mk: st.error("Sai mật khẩu!")

elif che_do == "🎪 Phòng thí nghiệm ảo":
    st.markdown("### 🎪 Phòng Thí Nghiệm PhET Colorado")
    st.info("Mô phỏng Khoa học tự nhiên & Toán học.")

elif che_do == "📖 Học theo chuyên đề":
    lop_dict = DATABASE[mon]
    if lop_dict:
        c_lop, c_chuong, c_bai = st.columns([1, 2, 2])
        lop = c_lop.selectbox("Khối:", list(lop_dict.keys()), key="s_lop")
        chuong_dict = lop_dict[lop]
        ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
        idx_c = ds_chuong.index(st.session_state.get("chuong_main")) if st.session_state.get("chuong_main") in ds_chuong else 0
        chuong = c_chuong.selectbox("Chương:", ds_chuong, index=idx_c, key="s_chuong")
        
        bai_dict = chuong_dict[chuong]
        ds_bai = list(bai_dict.keys())
        idx_b = ds_bai.index(st.session_state.get("bai_main")) if st.session_state.get("bai_main") in ds_bai else 0
        bai = c_bai.selectbox("Bài:", ds_bai, index=idx_b, key="s_bai")
        
        bai_dang_hoc = f"{chuong} - {bai}"
        du_lieu_bai_hien_tai = bai_dict[bai]
        
        lt, vd = du_lieu_bai_hien_tai.get("ly_thuyet", ""), du_lieu_bai_hien_tai.get("vi_du", "")
        t1, t2, t3 = st.tabs(["📚 Lý thuyết", "✏️ Bài tập", "📝 Trắc nghiệm"])
        
        with t1:
            st.markdown(f"<div class='khung-lythuyet'>{lt}</div>", unsafe_allow_html=True)
            
        with t2:
            for i, bt in enumerate(du_lieu_bai_hien_tai.get("bt_co_ban", []), 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    if "Ngữ Văn" in mon:
                        if st.button("💡 Xem gợi ý", key=f"g_{i}"): st.info(bt.get('lg', bt['dd'][0]))
                    else:
                        ans = st.text_input("Kết quả:", key=f"kq_{i}")
                        if st.button("Chấm", key=f"c_{i}"):
                            if so_sanh_so_hoc(ans, bt["dd"]): st.success("✅ Đúng")
                            else: st.error("❌ Sai")
                            
        with t3:
            ch_list = du_lieu_bai_hien_tai.get("cau_hoi", [])
            if ch_list:
                if st.button("🔄 Làm mới đề"): st.session_state[f"de_{bai}"] = None
                if f"de_{bai}" not in st.session_state or st.session_state[f"de_{bai}"] is None:
                    de_tron = []
                    for ch in ch_list:
                        da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                        de_tron.append({"nd": ch["nd"], "da": da_moi, "d": vt_moi})
                    st.session_state[f"de_{bai}"] = de_tron
                
                with st.form(f"f_{bai}"):
                    tl = {}
                    for i, ch in enumerate(st.session_state[f"de_{bai}"], 1):
                        st.markdown(f"**Câu {i}:** {ch['nd']}")
                        tl[i] = st.radio("Chọn:", ch["da"], key=f"r_{i}", index=None, label_visibility="collapsed")
                    if st.form_submit_button("Nộp bài"):
                        dung = sum(1 for i, ch in enumerate(st.session_state[f"de_{bai}"], 1) if tl[i] == ch["da"][ch["d"]])
                        st.markdown(f"<div class='diem-thi'>🏆 ĐIỂM: {dung/len(ch_list)*10:.1f}</div>", unsafe_allow_html=True)
                        for i, ch in enumerate(st.session_state[f"de_{bai}"], 1):
                            if tl[i] != ch["da"][ch["d"]]: st.error(f"Câu {i} sai. Đúng là: {ch['da'][ch['d']]}")

# ==================== KHU VỰC GIA SƯ AI ====================
if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
    st.divider()
    st.header("💬 Gia sư AI")
    
    col1, col2, col3 = st.columns([2, 2, 1])
    mon_ai = col1.radio("Môn:", ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn"], horizontal=True, label_visibility="collapsed")
    nguon_ai = col2.selectbox("Nguồn:", ["⚡ Gemini", "🤝 Dola -> Gemini"], label_visibility="collapsed")
    if col3.button("🗑️ Xóa chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    sys_prompt = f"Gia sư {mon_ai}. Học sinh đang học: {bai_dang_hoc}. Socratic, ngắn gọn."
    if "chat_history" not in st.session_state: st.session_state.chat_history = []
    
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    prompt = st.chat_input("Hỏi gia sư...")
    if prompt:
        if not GEMINI_KEYS:
            st.error("⚠️ Hệ thống chưa được cấu hình API Key. Vui lòng báo thầy cô thêm khóa API để sử dụng tính năng này.")
        else:
            ok, giay = kiem_tra_gioi_han_tan_suat()
            if not ok:
                st.warning(f"⏳ Chờ {giay}s rồi hỏi tiếp. Lần này AI chưa nhận câu hỏi của em: '{prompt}'")
            else:
                with st.chat_message("user"): st.markdown(prompt)
                st.session_state.chat_history.append({"role": "user", "content": prompt})
                
                with st.chat_message("assistant"):
                    is_first = (len(st.session_state.chat_history) <= 2)
                    h_key = tao_ma_hash_cau_hoi(mon_ai, bai_dang_hoc, nguon_ai, prompt) if is_first else None
                    ans_cached = lay_cache_ai(h_key) if h_key else None
                    
                    if ans_cached:
                        st.markdown(ans_cached)
                        st.session_state.chat_history.append({"role": "assistant", "content": ans_cached})
                    else:
                        g_hist = [{"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} for m in st.session_state.chat_history[:-1]]
                        luu_kq = ""
                        try:
                            with st.spinner("AI đang nghĩ..."):
                                if "Dola" in nguon_ai:
                                    d_nd = goi_dola_toi_uu(prompt)
                                    if d_nd: luu_kq = goi_gemini_an_toan(f"Chuẩn SGK: {d_nd}\nDiễn giải câu: {prompt}", sys_prompt, g_hist)
                                    else: luu_kq = goi_gemini_an_toan(prompt, sys_prompt, g_hist)
                                else:
                                    luu_kq = goi_gemini_an_toan(prompt, sys_prompt, g_hist)
                                st.markdown(luu_kq)
                        except Exception as e:
                            luu_kq = "⚠️ AI đang bận xử lý, em thử lại câu hỏi nhé."
                            st.error(luu_kq)
                            
                        st.session_state.chat_history.append({"role": "assistant", "content": luu_kq})
                        if h_key: luu_cache_ai(h_key, luu_kq)
