# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Tối thượng: Đếm User Online + Tích hợp Dola & Gemini (Auto-Fallback chống sập)
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

# ==================== CẤU HÌNH API KEYS ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

try:
    DOLA_ENDPOINT = st.secrets.get("DOLA_API_ENDPOINT", os.getenv("DOLA_API_ENDPOINT", ""))
    DOLA_KEY = st.secrets.get("DOLA_API_KEY", os.getenv("DOLA_API_KEY", ""))
except Exception:
    DOLA_ENDPOINT = ""
    DOLA_KEY = ""

# ==================== HỆ THỐNG ĐẾM NGƯỜI DÙNG TRỰC TUYẾN ====================
@st.cache_resource
def lay_bo_nho_truy_cap():
    return {}

def cap_nhat_nguoi_online():
    bo_nho = lay_bo_nho_truy_cap()
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())
        
    bo_nho[st.session_state.user_id] = time.time()
    thoi_gian_hien_tai = time.time()
    danh_sach_online = {uid: t for uid, t in bo_nho.items() if thoi_gian_hien_tai - t < 300}
    bo_nho.clear()
    bo_nho.update(danh_sach_online)
    return len(bo_nho)

# ==================== IMPORT DỮ LIỆU TỪ CÁC FILE ====================
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
    from data_van import VAN
except ImportError:
    VAN = {}

DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA if HOA else {"Lớp 7": {"Chương 1: Đang cập nhật dữ liệu Hóa": {}}},
    "📖 Môn Ngữ Văn": VAN if VAN else {"Lớp 7": {"Chương 1: Đang cập nhật dữ liệu Văn": {}}},
}

DANH_MUC_THI_NGHIEM = {
    "📐 Môn Toán": {
        "⚖️ Cân bằng phương trình & Biểu thức đại số": "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_vi.html",
    },
    "🔬 Môn Vật lý (KHTN)": {
        "💡 Khúc xạ & Phản xạ ánh sáng (Quang học 7)": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_vi.html",
    },
    "🧪 Môn Hóa học (KHTN)": {
        "⚛️ Xây dựng cấu tạo Nguyên tử": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_vi.html",
        "🧬 Lắp ghép Phân tử (H2O, CO2...)": "https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_vi.html",
        "⚖️ Cân bằng Phương trình Hóa học": "https://phet.colorado.edu/sims/html/balancing-chemical-equations/latest/balancing-chemical-equations_vi.html",
        "🧪 Pha chế & Đo nồng độ dung dịch": "https://phet.colorado.edu/sims/html/concentration/latest/concentration_vi.html",
    },
    "📖 Môn Ngữ Văn": {
        "📖 Sơ đồ tư duy Tác phẩm & Phân tích văn học": "",
    }
}

# ==================== CẤU HÌNH TRANG & CSS ====================
st.set_page_config(page_title="Hệ Thống Học Tập Lớp 7", page_icon="🎓", layout="wide", initial_sidebar_state="expanded")
dark_mode = st.sidebar.checkbox("🌙 Chế độ Ban đêm (Dark Mode)", value=False)

if dark_mode:
    CSS = """
    <style>
        .stApp { background-color: #0F172A; color: #F1F5F9; }
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], [data-testid="stHeaderActionElements"], .stAppDeployButton, #MainMenu, footer { display: none !important; visibility: hidden !important; }
        .hero-banner { background: linear-gradient(135deg, #1E293B 0%, #334155 100%); color: #F8FAFC; padding: 1.2rem 1.5rem; border-radius: 12px; margin-bottom: 1.2rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3); }
        .hero-title { font-size: 1.4rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 0.9rem; opacity: 0.9; margin-top: 0.3rem; color: #CBD5E1 !important; }
        .card-home { background-color: #1E293B; border: 1px solid #334155; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; color: #F1F5F9; display: flex; flex-direction: column; height: 100%; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
        .card-home h3 { margin-top: 0; font-size: 1.15rem; margin-bottom: 0.6rem; color: #60A5FA; }
        .card-home p { margin: 0; font-size: 0.92rem; line-height: 1.5; color: #94A3B8; }
        .khung-lythuyet { background-color: #1E293B; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #3B82F6; color: #F1F5F9 !important; }
        .khung-vidu { background-color: #27272A; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #F59E0B; color: #F1F5F9 !important; }
        .dung { color: #34D399; font-weight: 700; }
        .sai { color: #F87171; font-weight: 700; }
        .diem-thi { background-color: #451A03; font-size: 1.6rem; color: #F87171 !important; font-weight: 800; text-align: center; padding: 1.2rem; border: 2px dashed #EF4444; border-radius: 12px; }
    </style>
    """
else:
    CSS = """
    <style>
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], [data-testid="stHeaderActionElements"], .stAppDeployButton, #MainMenu, footer { display: none !important; visibility: hidden !important; }
        .hero-banner { background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); color: white; padding: 1.2rem 1.5rem; border-radius: 12px; margin-bottom: 1.2rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .hero-title { font-size: 1.4rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 0.9rem; opacity: 0.9; margin-top: 0.3rem; color: #E2E8F0 !important; }
        .card-home { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; display: flex; flex-direction: column; height: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        .card-home h3 { margin-top: 0; font-size: 1.15rem; margin-bottom: 0.6rem; color: #1D4ED8; }
        .card-home p { margin: 0; font-size: 0.92rem; line-height: 1.5; color: #475569; }
        .khung-lythuyet { background-color: #EFF6FF; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #2563EB; color: #1E293B !important; }
        .khung-vidu { background-color: #FFFBEB; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #F59E0B; color: #1E293B !important; }
        .dung { color: #059669; font-weight: 700; }
        .sai { color: #DC2626; font-weight: 700; }
        .diem-thi { background-color: #FFF1F2; font-size: 1.6rem; color: #E11D48 !important; font-weight: 800; text-align: center; padding: 1.2rem; border: 2px dashed #F43F5E; border-radius: 12px; }
    </style>
    """
st.markdown(CSS, unsafe_allow_html=True)

# ==================== HÀM TIỆN ÍCH ====================
def lam_sach_id(s): return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))
def sap_xep_chuong(ds_chuong):
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)
def chuan_hoi(s):
    d = str(s).strip().lower().replace(',', '.').replace(';', '.')
    return re.sub(r'\s+', '', d)
def so_sanh(nd, ds_dung):
    x = chuan_hoi(nd)
    if not x: return False
    for d in ds_dung:
        y = chuan_hoi(d)
        if not y: continue
        if x == y or (len(x) >= 2 and (x in y or y in x)): return True
        try:
            if abs(float(x) - float(y)) < 0.01: return True
        except (ValueError, TypeError): pass
    return False

def ghi_nhan_lich_su(tieu_de_bai, diem, dung, tong, chi_tiet_sai=None):
    if 'lich_su_hoc_tap' not in st.session_state: st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {"bai": tieu_de_bai, "diem": diem, "dung": dung, "tong": tong, "sai": chi_tiet_sai or []})

def hien_thi_tien_do():
    if 'lich_su_hoc_tap' in st.session_state and st.session_state.lich_su_hoc_tap:
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Lịch sử học tập gần đây")
        tong_diem = sum(item["diem"] for item in st.session_state.lich_su_hoc_tap)
        so_bai = len(st.session_state.lich_su_hoc_tap)
        st.sidebar.metric("Điểm trung bình", f"{tong_diem / so_bai:.1f} / 10", f"Đã luyện {so_bai} bài")
        with st.sidebar.expander("📜 Xem chi tiết các bài gần nhất"):
            for idx, ls in enumerate(st.session_state.lich_su_hoc_tap[:5], 1):
                st.markdown(f"**{idx}. {ls['bai']}**")
                st.caption(f"🏆 Kết quả: {ls['diem']:.1f}đ (Đúng {ls['dung']}/{ls['tong']})")
                st.divider()

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\mathbb{Q}', 'Q').replace(r'\mathbb{Z}', 'Z').replace(r'\mathbb{N}', 'N').replace(r'\mathbb{R}', 'R')
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ').replace(r'\div', ' chia ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    s = re.sub(r'[^\w\s,.?!:;()+\-*/=<>%àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]', '', s)
    return re.sub(r'\s+', ' ', s).strip()

def trich_xuat_word_docx(file_bytes):
    try:
        with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
            xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        doan_van = [''.join([t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]) for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')]
        return '\n'.join([p for p in doan_van if p])
    except Exception as e:
        return f"[Lỗi đọc file Word: {e}]"

# --- HÀM GỌI DOLA VÀ GEMINI ---
def goi_dola(cau_hoi):
    """Gọi Dola lấy nội dung chuẩn"""
    if not DOLA_ENDPOINT or not DOLA_KEY: return None
    try:
        phan_hoi = requests.post(
            DOLA_ENDPOINT,
            headers={"Authorization": f"Bearer {DOLA_KEY}"},
            json={"cau_hoi": cau_hoi, "chuong_trinh": "ket_noi_tri_thuc_lop7", "che_do": "chuan_sgk"},
            timeout=15
        )
        if phan_hoi.status_code == 200: return phan_hoi.json().get("noi_dung_chuan", "")
        return None
    except Exception:
        return None

def goi_gemini_an_toan(payload, system_instruction, history=None):
    """Hàm AI tự động rẽ nhánh bỏ qua model chết (404) và thử lại model bận (429)"""
    ds_models = [
        "gemini-3.5-flash",
        "gemini-2.5-flash",
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-2.0-flash"
    ]
    max_retries = 3
    last_err = None

    for ten_m in ds_models:
        for attempt in range(max_retries):
            try:
                m = genai.GenerativeModel(model_name=ten
