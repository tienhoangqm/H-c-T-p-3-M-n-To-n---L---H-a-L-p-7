# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Hoàn thiện Nhóm 1 & Nhóm 2: Trộn đáp án trắc nghiệm, Chấm số chính xác, Sửa Cache AI & Xử lý ảnh độc lập
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

# ==================== CẤU HÌNH TRANG (PHẢI ĐẶT ĐẦU TIÊN) ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7 - Kết Nối Tri Thức",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# ==================== CẤU HÌNH XOAY VÒNG ĐA KHÓA API (MULTI-KEY) ====================
def lay_danh_sach_gemini_keys():
    keys = []
    try:
        if "GEMINI_API_KEYS" in st.secrets:
            val = st.secrets["GEMINI_API_KEYS"]
            if isinstance(val, list):
                keys.extend([k.strip() for k in val if str(k).strip()])
            elif isinstance(val, str):
                keys.extend([k.strip() for k in val.split(",") if k.strip()])
        
        for k_name in ["GEMINI_API_KEY", "GEMINI_API_KEY_1", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"]:
            if k_name in st.secrets and str(st.secrets[k_name]).strip():
                k_val = str(st.secrets[k_name]).strip()
                if k_val not in keys:
                    keys.append(k_val)
    except Exception:
        pass

    for k_name in ["GEMINI_API_KEY", "GEMINI_API_KEY_2"]:
        env_val = os.getenv(k_name, "").strip()
        if env_val and env_val not in keys:
            keys.append(env_val)

    return keys

GEMINI_KEYS = lay_danh_sach_gemini_keys()
if GEMINI_KEYS:
    genai.configure(api_key=GEMINI_KEYS[0])

try:
    DOLA_ENDPOINT = str(st.secrets.get("DOLA_API_ENDPOINT", os.getenv("DOLA_API_ENDPOINT", ""))).strip()
    DOLA_KEY = str(st.secrets.get("DOLA_API_KEY", os.getenv("DOLA_API_KEY", ""))).strip()
    DOLA_PROJECT_TIER = str(st.secrets.get("DOLA_PROJECT_TIER", "high_limit_edu")).strip()
except Exception:
    DOLA_ENDPOINT = ""
    DOLA_KEY = ""
    DOLA_PROJECT_TIER = "high_limit_edu"

# ==================== HỆ THỐNG ĐẾM NGƯỜI DÙNG TRỰC TUYẾN (CÓ THREADING LOCK) ====================
@st.cache_resource
def lay_bo_nho_truy_cap():
    return {"dict": {}, "lock": threading.Lock()}

def cap_nhat_nguoi_online():
    bo_nho_obj = lay_bo_nho_truy_cap()
    bo_nho = bo_nho_obj["dict"]
    lock = bo_nho_obj["lock"]
    
    with lock:
        if 'user_id' not in st.session_state:
            st.session_state.user_id = str(uuid.uuid4())
            
        bo_nho[st.session_state.user_id] = time.time()
        thoi_gian_hien_tai = time.time()
        danh_sach_online = {uid: t for uid, t in bo_nho.items() if thoi_gian_hien_tai - t < 300}
        bo_nho.clear()
        bo_nho.update(danh_sach_online)
        return len(bo_nho)

# ==================== BỘ ĐỆM AI THÔNG MINH & GIỚI HẠN TẦN SUẤT ====================
@st.cache_resource
def lay_bo_nho_cache_ai():
    return {}

def kiem_tra_gioi_han_tan_suat(cooldown_seconds=3):
    now = time.time()
    last_time = st.session_state.get("last_ai_request_time", 0.0)
    elapsed = now - last_time
    if elapsed < cooldown_seconds:
        return False, int(cooldown_seconds - elapsed) + 1
    st.session_state["last_ai_request_time"] = now
    return True, 0

# ==================== IMPORT DỮ LIỆU TOÁN, LÝ, HÓA, VĂN ====================
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
        "🗺️ 1. Bản đồ Cấu trúc & Bối cảnh Tác phẩm": "van_hoc_cau_truc",
        "🎭 2. Biểu đồ Tương tác & Phân tích Nhân vật": "van_hoc_nhan_vat",
        "🕸️ 3. Sơ đồ Quan hệ Nhân vật": "van_hoc_quan_he",
        "✍️ 4. Phòng thực hành Luyện từ & Ngữ pháp": "van_hoc_ngu_phap",
        "📝 5. Trạm Lập dàn ý & Cấu trúc bài văn": "van_hoc_dan_y"
    }
}

DATA_LAB_NGU_VAN = {
    "🗺️ 1. Bản đồ Cấu trúc & Bối cảnh Tác phẩm": {
        "tieu_de": "Bản đồ Cấu trúc Tác phẩm: Bồng chanh đỏ (Đỗ Chu)",
        "hoan_canh": "Truyện ngắn xuất sắc viết về tình yêu thương loài vật, thiên nhiên và những rung cảm tinh tế của tuổi thơ.",
        "bo_cuc": [
            {"phan": "Phần 1: Mở đầu", "noi_dung": "Giới thiệu không gian ven sông quen thuộc và tổ chim bồng chanh đỏ đầy bí ẩn của hai anh em Hoài và Ý."},
            {"phan": "Phần 2: Diễn biến", "noi_dung": "Cuộc mạo hiểm leo lên bờ vực cao để quan sát tổ chim bồng chanh đỏ nở con."},
            {"phan": "Phần 3: Cao trào", "noi_dung": "Quyết định thả chim về với tự nhiên sau khi nhận ra tình mẫu tử thiêng liêng của loài vật."},
            {"phan": "Phần 4: Kết thúc", "noi_dung": "Bài học sâu sắc về sự tôn trọng tự do và tình yêu thương muôn loài."}
        ],
        "y_nghia": "Bồi dưỡng tình yêu thiên nhiên, ý thức bảo vệ môi trường sống và sự trân trọng những vẻ đẹp trong ngần của tuổi thơ."
    },
    "🎭 2. Biểu đồ Tương tác & Phân tích Nhân vật": {
        "nhan_vat": "Nhân vật Hoài trong truyện 'Bồng chanh đỏ'",
        "dac_diem": "Giàu tình cảm, ham khám phá, biết trân trọng sự sống và có nội tâm nhân hậu.",
        "hanh_vi_tieu_bieu": "Trèo cây leo vực tìm tổ chim; say sưa ngắm nhìn chim bố mẹ mớm mồi; quyết định ngăn không cho em bắt chim.",
        "dien_bien_tam_ly": [
            {"giai_doan": "Đầu truyện", "tam_trang": "Tò mò, khao khát sở hữu tổ chim bồng chanh đỏ tuyệt đẹp."},
            {"giai_doan": "Giữa truyện", "tam_trang": "Xúc động trước tình cảm gia đình chim bồng chanh."},
            {"giai_doan": "Cuối truyện", "tam_trang": "Thức tỉnh, hạnh phúc và buông bỏ ý định bắt chim để trả lại tự do cho chúng."}
        ]
    },
    "🕸️ 3. Sơ đồ Quan hệ Nhân vật": {
        "tac_pham": "Mối quan hệ trong 'Bồng chanh đỏ'",
        "quan_he": [
            {"tu_khoa": "Anh Hoài ↔️ Em Ý", "loai": "Đồng hành khám phá", "mo_ta": "Hai anh em cùng chia sẻ những bí mật tuổi thơ, cùng leo trèo và cùng thay đổi nhận thức qua sự việc chú chim bồng chanh."},
            {"tu_khoa": "Con người ↔️ Thiên nhiên (Chim bồng chanh)", "loai": "Từ chinh phục đến thấu hiểu", "mo_ta": "Sự chuyển biến từ ý định săn bắt sang bảo vệ, thể hiện sự hòa hợp giữa con người và tự nhiên."}
        ]
    },
    "✍️ 4. Phòng thực hành Luyện từ & Ngữ pháp": {
        "chu_de": "Phòng thực hành Từ vựng & Biện pháp tu từ lớp 7",
        "cau_hoi_mau": [
            {"cau": "Đôi cánh bồng chanh đỏ chói rực rỡ như một đốm lửa nhỏ.", "loai": "Biện pháp tu từ: So sánh", "phan_tich": "Tác dụng: Làm cho hình ảnh chim bồng chanh trở nên sinh động, nổi bật và giàu sức gợi hình."},
            {"cau": "Tiếng chim hót vang lừng / chào đón bình minh.", "loai": "Biện pháp tu từ: Nhân hóa", "phan_tich": "Tác dụng: Gắn cho chim hoạt động của con người, tăng tính biểu cảm."}
        ]
    },
    "📝 5. Trạm Lập dàn ý & Cấu trúc bài văn": {
        "the_loai": "Viết bài văn biểu cảm về một tác phẩm văn học",
        "dan_y": [
            {"buoc": "1. Mở bài", "noi_dung": "Giới thiệu tên tác phẩm, tác giả và cảm xúc chung chi phối người đọc."},
            {"buoc": "2. Thân bài", "noi_dung": "- Nêu ấn tượng về nội dung (cốt truyện, chi tiết đắt giá).\n- Nêu cảm xúc về nhân vật hoặc bức tranh thiên nhiên trong tác phẩm.\n- Ý nghĩa sâu xa mà tác phẩm gửi gắm."},
            {"buoc": "3. Kết bài", "noi_dung": "Khẳng định giá trị trường tồn của tác phẩm và bài học rút ra cho bản thân."}
        ]
    }
}

# ==================== CẤU HÌNH CSS ====================
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
        .card-home { background-color: #1E293B; border: 1px solid #334155; padding: 1.4rem; border-radius: 12px; margin-bottom: 1.0rem; color: #F1F5F9; display: flex; flex-direction: column; height: 100%; box-shadow: 0 2px 4px rgba(0,0,0,0.2); }
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
        .card-home { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.4rem; border-radius: 12px; margin-bottom: 1.0rem; display: flex; flex-direction: column; height: 100%; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
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

# ==================== HÀM TIỆN ÍCH CHẤM ĐIỂM SỐ CHÍNH XÁC ====================
def lam_sach_id(s): return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))
def sap_xep_chuong(ds_chuong):
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)

def so_sanh_so_hoc(nd, ds_dung):
    """Chấm điểm nghiêm ngặt cho bài tập số học (chỉ đúng khi giá trị số trùng khớp, không dùng chung chuỗi)"""
    x_raw = str(nd).strip().replace(',', '.')
    try:
        val_x = float(x_raw)
    except (ValueError, TypeError):
        # Nếu học sinh nhập phân số hoặc ký hiệu, so sánh tuyệt đối chuỗi đã chuẩn hóa
        x_clean = re.sub(r'\s+', '', x_raw.lower())
        for d in ds_dung:
            if x_clean == re.sub(r'\s+', '', str(d).strip().lower().replace(',', '.')):
                return True
        return False

    for d in ds_dung:
        d_raw = str(d).strip().replace(',', '.')
        try:
            val_d = float(d_raw)
            if abs(val_x - val_d) < 1e-5:
                return True
        except (ValueError, TypeError):
            if x_raw.lower() == d_raw.lower():
                return True
    return False

def luu_tien_do(mon, lop, chuong, ten_bai, dung, tong):
    if "tien_do_chi_tiet" not in st.session_state:
        st.session_state["tien_do_chi_tiet"] = {}
    st.session_state["tien_do_chi_tiet"][f"{mon}_{lop}_{chuong}_{ten_bai}"] = {"dung": dung, "tong": tong}

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

def doc_to_an_toan(text, autoplay=True):
    """Bọc gTTS bằng try/except để tránh sập web khi mất mạng hoặc quá tải"""
    if not HAS_TTS or not text:
        return
    try:
        clean_text = lam_sach_van_ban_doc(text)
        if clean_text:
            afp = io.BytesIO()
            gTTS(text=clean_text, lang='vi').write_to_fp(afp)
            afp.seek(0)
            st.audio(afp, format='audio/mp3', autoplay=autoplay)
    except Exception:
        pass

# ==================== TỐI ƯU GỌI DOLA (KHÔNG CACHE LỖI) ====================
def goi_dola_toi_uu(cau_hoi):
    if not DOLA_ENDPOINT or not DOLA_KEY:
        return None
    try:
        session = requests.Session()
        phan_hoi = session.post(
            DOLA_ENDPOINT,
            headers={
                "Authorization": f"Bearer {DOLA_KEY}",
                "X-Project-Quota-Tier": DOLA_PROJECT_TIER,
                "X-Request-Priority": "education-production",
                "Content-Type": "application/json"
            },
            json={
                "cau_hoi": cau_hoi,
                "chuong_trinh": "ket_noi_tri_thuc_lop7",
                "che_do": "chuan_sgk",
                "yeu_cau_nang_cap_gioi_han": True
            },
            timeout=4.0
        )
        if phan_hoi.status_code == 200:
            data_json = phan_hoi.json()
            nd = data_json.get("noi_dung_chuan") or data_json.get("answer") or data_json.get("text") or ""
            return nd.strip() if nd else None
        return None
    except Exception:
        return None

# ==================== TỐI ƯU GỌI GEMINI ====================
@st.cache_data(ttl=3600, show_spinner=False)
def lay_danh_sach_model_kha_dung(api_key):
    uu_tien = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro"
    ]
    try:
        genai.configure(api_key=api_key)
        ds_hien_co = []
        for m in genai.list_models():
            if "generateContent" in getattr(m, "supported_generation_methods", []):
                ten_ngan = m.name.replace("models/", "")
                ds_hien_co.append(ten_ngan)
        if ds_hien_co:
            ket_qua = [m for m in uu_tien if m in ds_hien_co]
            for m in ds_hien_co:
                if m not in ket_qua and "gemini" in m:
                    ket_qua.append(m)
            return ket_qua if ket_qua else uu_tien
    except Exception:
        pass
    return uu_tien

def goi_gemini_an_toan(payload, system_instruction, history=None):
    if not GEMINI_KEYS:
        raise RuntimeError("Chưa cấu hình GEMINI_API_KEY trong phần Secrets của Streamlit.")

    if "key_index" not in st.session_state:
        st.session_state["key_index"] = 0

    so_luong_key = len(GEMINI_KEYS)
    last_err = None

    for k_offset in range(so_luong_key):
        idx_hien_tai = (st.session_state["key_index"] + k_offset) % so_luong_key
        current_key = GEMINI_KEYS[idx_hien_tai]
        genai.configure(api_key=current_key)

        ds_models = lay_danh_sach_model_kha_dung(current_key)

        for ten_m in ds_models:
            for attempt in range(2):
                try:
                    m = genai.GenerativeModel(model_name=ten_m, system_instruction=system_instruction)
                    if history is not None:
                        chat_s = m.start_chat(history=history)
                        ket_qua_text = chat_s.send_message(payload).text
                    else:
                        ket_qua_text = m.generate_content(payload).text

                    st.session_state["key_index"] = idx_hien_tai
                    return ket_qua_text

                except Exception as e:
                    last_err = e
                    error_str = str(e).lower()

                    if "404" in error_str or "not found" in error_str or "not supported" in error_str:
                        break
                    elif "429" in error_str or "resource_exhausted" in error_str or "quota" in error_str:
                        if attempt == 0:
                            time.sleep(1.2)
                            continue
                        else:
                            break
                    else:
                        break

    raise last_err

# ==================== GIAO DIỆN PHÒNG THÍ NGHIỆM NGỮ VĂN TƯƠNG TÁC ====================
def hien_thi_phong_thi_nghiem_ngu_van(key_prefix="van"):
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🎭 Phòng Thí Nghiệm & Mô Phỏng Tương Tác Ngữ Văn</p>
        <p class="hero-sub">Khám phá cấu trúc tác phẩm, phân tích nhân vật và sơ đồ tư duy trực quan</p>
    </div>
    """, unsafe_allow_html=True)

    ds_modul = list(DANH_MUC_THI_NGHIEM["📖 Môn Ngữ Văn"].keys())
    chon_modul = st.selectbox("📚 Chọn Mô-đun Tương tác Ngữ Văn:", ds_modul, key=f"select_modul_{key_prefix}")

    st.divider()

    if "Bản đồ Cấu trúc" in chon_modul:
        data = DATA_LAB_NGU_VAN["🗺️ 1. Bản đồ Cấu trúc & Bối cảnh Tác phẩm"]
        st.markdown(f"### 🗺️ {data['tieu_de']}")
        st.info(f"⏳ **Hoàn cảnh sáng tác:** {data['hoan_canh']}")
        st.markdown("#### 📂 Sơ đồ Phân bố Bố cục:")
        for idx, item in enumerate(data["bo_cuc"], 1):
            with st.expander(f"🔹 {item['phan']}"):
                st.write(item['noi_dung'])
        st.success(f"💡 **Ý nghĩa nhân văn:** {data['y_nghia']}")

    elif "Biểu đồ Tương tác" in chon_modul:
        data = DATA_LAB_NGU_VAN["🎭 2. Biểu đồ Tương tác & Phân tích Nhân vật"]
        st.markdown(f"### 🎭 {data['nhan_vat']}")
        st.markdown(f"⭐ **Đặc điểm nổi bật:** {data['dac_diem']}")
        st.markdown(f"🎯 **Hành vi tiêu biểu:** {data['hanh_vi_tieu_bieu']}")
        st.markdown("---")
        st.markdown("#### 📈 Diễn biến tâm lý nhân vật qua các chặng:")
        for stage in data["dien_bien_tam_ly"]:
            st.markdown(f"* **{stage['giai_doan']}:** {stage['tam_trang']}")

    elif "Sơ đồ Quan hệ" in chon_modul:
        data = DATA_LAB_NGU_VAN["🕸️ 3. Sơ đồ Quan hệ Nhân vật"]
        st.markdown(f"### 🕸️ {data['tac_pham']}")
        st.markdown("*(Nhấp vào các mục bên dưới để xem phân tích chi tiết mối quan hệ)*")
        for idx, rel in enumerate(data["quan_he"], 1):
            with st.expander(f"{idx}. {rel['tu_khoa']} — *[{rel['loai']}]*"):
                st.write(rel['mo_ta'])

    elif "Luyện từ & Ngữ pháp" in chon_modul:
        data = DATA_LAB_NGU_VAN["✍️ 4. Phòng thực hành Luyện từ & Ngữ pháp"]
        st.markdown(f"### ✍️ {data['chu_de']}")
        for idx, bai in enumerate(data["cau_hoi_mau"], 1):
            st.markdown(f"**Câu mẫu {idx}:** `{bai['cau']}`")
            st.markdown(f"👉 **Phân loại:** **{bai['loai']}**")
            st.info(f"💡 **Giải thích:** {bai['phan_tich']}")
            st.divider()

    elif "Lập dàn ý" in chon_modul:
        data = DATA_LAB_NGU_VAN["📝 5. Trạm Lập dàn ý & Cấu trúc bài văn"]
        st.markdown(f"### 📝 Hướng dẫn Lập dàn ý: {data['the_loai']}")
        for buoc in data["dan_y"]:
            with st.expander(f"📋 {buoc['buoc']}"):
                st.text(buoc['noi_dung'])

# ==================== CÁC HÀM HIỂN THỊ CHỨC NĂNG KHÁC ====================
def hien_thi_tim_kiem_toan_dien():
    st.markdown("""<div class="hero-banner"><p class="hero-title">🔍 Tra Cứu & Tìm Kiếm Tri Thức Thông Minh</p><p class="hero-sub">Gõ từ khóa bất kỳ để tìm nhanh bài học trong toàn bộ hệ thống</p></div>""", unsafe_allow_html=True)
    tu_khoa = st.text_input("🔎 Nhập từ khóa cần tìm kiếm:", placeholder="Gõ tên bài học hoặc khái niệm...")
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        ket_qua_tim = []
        for ten_mon, lop_dict in DATABASE.items():
            for lop, chuong_dict in lop_dict.items():
                for chuong, bai_dict in chuong_dict.items():
                    for ten_bai, data in bai_dict.items():
                        lt, vd = data.get("ly_thuyet", "").lower(), data.get("vi_du", "").lower()
                        if kw in ten_bai.lower() or kw in lt or kw in vd:
                            ket_qua_tim.append({"mon": ten_mon, "lop": lop, "chuong": chuong, "bai": ten_bai, "data": data})
        st.markdown(f"### 📋 Kết quả tìm kiếm cho từ khóa: *'{tu_khoa}'* ({len(ket_qua_tim)} kết quả)")
        if not ket_qua_tim: st.info("⚠️ Không tìm thấy bài học phù hợp.")
        else:
            for idx, item in enumerate(ket_qua_tim, 1):
                with st.expander(f"{idx}. [{item['mon']} - {item['chuong']}] — {item['bai']}"):
                    st.markdown(f"**Môn:** {item['mon']} | **Khối:** {item['lop']} | **{item['chuong']}**")
                    if st.button(f"📖 Mở ngay bài này", key=f"btn_go_to_{idx}"):
                        st.session_state["search_jump"] = item
                        st.rerun()

def hien_thi_trang_chu():
    st.markdown("""<div class="hero-banner"><p class="hero-title">🎓 HỆ THỐNG HỌC TẬP THCS — KẾT NỐI TRI THỨC (LỚP 7)</p><p class="hero-sub">Toàn diện các môn: Toán, Vật lý, Hóa học & Ngữ Văn lớp 7</p></div>""", unsafe_allow_html=True)
    col_h1, col_h2 = st.columns(2, gap="medium")
    with col_h1:
        st.markdown("""<div class="card-home"><h3>🌟 Giới thiệu Hệ thống</h3><p>Không gian học tập trực tuyến bám sát sách <b>Kết Nối Tri Thức</b> lớp 7 gồm đầy đủ Toán, Lý, Hóa và Ngữ Văn.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="card-home"><h3>🌙 Chế độ Ban đêm (Dark Mode)</h3><p>Bật công tắc chế độ ban đêm ở menu bên trái để bảo vệ mắt khi ôn tập vào buổi tối.</p></div>""", unsafe_allow_html=True)
    with col_h2:
        st.markdown("""<div class="card-home"><h3>💬 Trợ lý AI Phân Tải Thông Minh</h3><p>Tích hợp bộ đệm câu hỏi, tự động luân phiên khóa API và điều phối tuần tự giúp hệ thống luôn ổn định.</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="card-home"><h3>📱 Tối ưu thiết bị di động</h3><p>Giao diện co giãn mượt mà trên mọi thiết bị điện thoại, máy tính bảng và laptop.</p></div>""", unsafe_allow_html=True)

def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    if mon_hien_tai == "📖 Môn Ngữ Văn":
        hien_thi_phong_thi_nghiem_ngu_van(key_prefix=key_prefix)
    else:
        st.markdown("#### 🎪 Phòng Thí Nghiệm & Mô Phỏng Tương Tác (PhET Colorado)")
        ds_tn_mon = DANH_MUC_THI_NGHIEM.get(mon_hien_tai, {})
        if not ds_tn_mon: ds_tn_mon = DANH_MUC_THI_NGHIEM["🔬 Môn Vật lý (KHTN)"]
        ten_tn = st.selectbox(f"🔬 Chọn mô phỏng thực hành cho {mon_hien_tai}:", list(ds_tn_mon.keys()), key=f"select_tn_{key_prefix}_{lam_sach_id(mon_hien_tai)}")
        url_tn = ds_tn_mon[ten_tn]
        if not url_tn: st.warning("🚧 **Tính năng đang phát triển:** Phòng thí nghiệm cho môn học này đang được cập nhật!")
        else:
            st.components.v1.iframe(url_tn, height=580, scrolling=True)
            st.info("💡 **Mẹo thực hành:** Dùng chuột kéo thả trực tiếp trên màn hình, sau đó kéo xuống hỏi Gia sư AI để hiểu rõ bản chất nhé!")

def hien_thi_tram_nap_du_lieu():
    st.markdown("""<div class="hero-banner"><p class="hero-title">⚙️ Trạm Nạp Dữ Liệu Tự Động (Auto-Parser)</p><p class="hero-sub">Dành cho Admin: Tải file đề bài để tạo Code Python chuẩn.</p></div>""", unsafe_allow_html=True)
    tab_upfile, tab_paste = st.tabs(["📁 Tải File Lên", "📝 Dán Văn Bản Thô"])
    danh_sach_files = []
    with tab_upfile:
        uploaded_files = st.file_uploader("Chọn file:", type=["docx", "pdf", "png", "jpg", "jpeg", "txt"], accept_multiple_files=True, key="parser_file_uploader")
        if uploaded_files: danh_sach_files = uploaded_files
    with tab_paste:
        raw_text = st.text_area("Dán nội dung:", height=220, key="parser_raw_text")

    PROMPT_PARSER = 'Hãy chuyển đổi toàn bộ nội dung thành Dictionary Python chuẩn gồm "ly_thuyet", "vi_du", "cau_hoi", "bt_co_ban", "bt_nang_cao". Chỉ in ra code Python.'
    if st.button("⚡ Bóc tách dữ liệu", type="primary", use_container_width=True):
        if not danh_sach_files and not raw_text.strip(): st.warning("⚠️ Vui lòng tải file hoặc dán văn bản!")
        else:
            with st.spinner("🤖 AI đang xử lý..."):
                try:
                    payload = []
                    for f in danh_sach_files:
                        if f.name.endswith(".docx"): payload.append(trich_xuat_word_docx(f.read()))
                        elif f.name.endswith(".pdf"): payload.append({"mime_type": "application/pdf", "data": f.read()})
                        elif f.name.endswith((".png", ".jpg", ".jpeg")) and HAS_PIL: payload.append(Image.open(io.BytesIO(f.read())))
                        else: payload.append(f.read().decode('utf-8', errors='ignore'))
                    if raw_text.strip(): payload.append(raw_text.strip())
                    ket_qua = goi_gemini_an_toan(payload, system_instruction=PROMPT_PARSER)
                    st.session_state["parsed_code_result"] = ket_qua.replace("```python", "").replace("```json", "").replace("```", "").strip()
                except Exception as e: st.error(f"❌ Lỗi: {e}")

    if "parsed_code_result" in st.session_state and st.session_state["parsed_code_result"]:
        code_out = st.session_state["parsed_code_result"]
        st.success("✅ Thành công!")
        st.download_button("💾 Tải Code về máy (.py)", data=code_out.encode("utf-8"), file_name="data_moi.py", mime="text/x-python", use_container_width=True)
        st.code(code_out, language="python")

# ==================== HÀM HIỂN THỊ BÀI HỌC (ĐÃ TRỘN ĐÁP ÁN TRẮC NGHIỆM & SỬA CHẤM TỰ LUẬN VĂN) ====================
def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    st.markdown(f"### 📖 {ten_bai}")
    lt, vd = data.get("ly_thuyet", "").strip(), data.get("vi_du", "").strip()
    ch_list, bt_cb, bt_nc = data.get("cau_hoi", []), data.get("bt_co_ban", []), data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Trắc nghiệm", f"{len(ch_list)} câu")
    c2.metric("✏️ Cơ bản", f"{len(bt_cb)} bài")
    c3.metric("🔥 Nâng cao", f"{len(bt_nc)} bài")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Lý thuyết", "✏️ Cơ bản", "🔥 Nâng cao", "📝 Trắc nghiệm", "🎪 Phòng thí nghiệm"])

    with tab1:
        if lt: st.markdown(f"<div class='khung-lythuyet'>{lt}</div>", unsafe_allow_html=True)
        if vd: st.markdown(f"<div class='khung-vidu'>{vd}</div>", unsafe_allow_html=True)

    with tab2:
        if not bt_cb: st.info("Chưa có bài tập.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    ans = st.text_input("Nhập kết quả (số học):", key=f"cb_{sid}_{i}")
                    if st.button("Kiểm tra", key=f"btn_cb_{sid}_{i}"):
                        if not ans.strip(): st.warning("⚠️ Nhập đáp án trước!")
                        elif so_sanh_so_hoc(ans, bt["dd"]): st.markdown("<p class='dung'>✅ Chính xác!</p>", unsafe_allow_html=True)
                        else: st.markdown(f"<p class='sai'>❌ Sai. Đáp án: {bt['dd'][0]}</p>", unsafe_allow_html=True)
                        st.info(f"💡 Giải thích: {bt.get('gt') or bt.get('lg', '')}")

    with tab3:
        if not bt_nc: st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                with st.expander(f"Bài nâng cao {i}: {nc['de'][:60]}..."):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    if nc.get('hd') or nc.get('goi_y'): st.info(f"💡 **Hướng dẫn:** {nc.get('hd') or nc.get('goi_y')}")
                    
                    # Nếu là môn Văn (tự luận), bỏ nút kiểm tra so khớp chuỗi lỏng lẻo, thay bằng Gợi ý / Gửi Gia sư AI
                    if "Ngữ Văn" in mon:
                        if st.button(f"💡 Xem gợi ý đáp án", key=f"btn_goiy_nc_{sid}_{i}"):
                            st.info(f"📝 **Gợi ý hướng dẫn:** {nc.get('lg', nc.get('dd', [''])[0])}")
                    else:
                        ans = st.text_input("Nhập kết quả:", key=f"nc_{sid}_{i}")
                        if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                            if so_sanh_so_hoc(ans, nc["dd"]): st.success("🎉 Chính xác!")
                            else: st.error(f"❌ Gợi ý: {nc['dd'][0]}")
                        if st.checkbox("📖 Xem lời giải", key=f"lg_{sid}_{i}"): st.success(f"**Lời giải:** {nc.get('lg', '')}")

    with tab4:
        tong = len(ch_list)
        if tong == 0: st.info("Chưa có trắc nghiệm.")
        else:
            options = sorted(list(set([n for n in [10, 15, 20, 30] if n <= tong] + [tong])))
            so_cau = st.selectbox("Chọn số lượng câu:", options, key=f"sl_{sid}")
            key_de = f"de_{sid}_{so_cau}"
            
            # TRỘN PHƯƠNG ÁN TRẮC NGHIỆM ĐỂ CHỐNG CHỌN BỪA Ô ĐẦU TIÊN
            if key_de not in st.session_state:
                ds_chon = random.sample(ch_list, min(so_cau, tong))
                de_tron = []
                for ch in ds_chon:
                    danh_sach_da = list(ch["da"])
                    d_dung_goc = danh_sach_da[ch["d"]]
                    random.shuffle(danh_sach_da)
                    vi_tri_moi = danh_sach_da.index(d_dung_goc)
                    de_tron.append({
                        "nd": ch.get("nd") or ch.get("de"),
                        "da": danh_sach_da,
                        "d": vi_tri_moi
                    })
                st.session_state[key_de] = de_tron
            de = st.session_state[key_de]

            with st.form(f"form_{sid}"):
                tl = {}
                for i, ch in enumerate(de, 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl[i] = st.radio(f"Câu {i}:", ch["da"], key=f"radio_{sid}_{so_cau}_{i}", index=None, label_visibility="collapsed")
                    st.divider()
                if st.form_submit_button("🚀 Nộp bài", type="primary", use_container_width=True):
                    if None in tl.values(): st.warning("⚠️ Còn câu chưa chọn!")
                    else:
                        dung = sum(1 for i, ch in enumerate(de, 1) if tl[i] == ch["da"][ch["d"]])
                        diem = dung / len(de) * 10
                        ghi_nhan_lich_su(f"Trắc nghiệm: {ten_bai}", diem, dung, len(de))
                        st.markdown(f"<div class='diem-thi'>🏆 KẾT QUẢ: {diem:.1f} / 10</div>", unsafe_allow_html=True)
                        for i, ch in enumerate(de, 1):
                            da_dung = ch["da"][ch["d"]]
                            if tl[i] == da_dung: st.markdown(f"✅ Câu {i}: Đúng")
                            else: st.markdown(f"❌ Câu {i}: Sai (Đúng: **{da_dung}**)")

    with tab5: hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

def hien_thi_che_do_thi(mon, lop, chuong_dict):
    st.markdown("### ⏱️ PHÒNG THI THỬ & KIỂM TRA ĐỊNH KÌ")
    ds_chuong_sorted = sap_xep_chuong(list(chuong_dict.keys()))
    col1, col2 = st.columns([1, 2])
    with col1: loai_de = st.selectbox("Cấu trúc đề:", ["Kiểm tra 15 phút (10 câu)", "Giữa kì (20 câu)", "Học kì (40 câu)"])
    with col2: chuong_chon = st.multiselect("Chọn chương:", ds_chuong_sorted, default=ds_chuong_sorted)

    mapping_cau = {"Kiểm tra 15 phút (10 câu)": 10, "Giữa kì (20 câu)": 20, "Học kì (40 câu)": 40}
    if st.button("🚀 TẠO ĐỀ THI", type="primary", use_container_width=True):
        all_questions = []
        for c in chuong_chon:
            for b, data in chuong_dict[c].items(): all_questions.extend(data.get("cau_hoi", []))
        if not all_questions: st.error("❌ Chưa có câu hỏi!")
        else:
            ds_chon = random.sample(all_questions, min(mapping_cau[loai_de], len(all_questions)))
            de_tron_thi = []
            for ch in ds_chon:
                danh_sach_da = list(ch["da"])
                d_dung_goc = danh_sach_da[ch["d"]]
                random.shuffle(danh_sach_da)
                vi_tri_moi = danh_sach_da.index(d_dung_goc)
                de_tron_thi.append({
                    "nd": ch.get("nd") or ch.get("de"),
                    "da": danh_sach_da,
                    "d": vi_tri_moi
                })
            st.session_state[f"dethi_{mon}_{lop}"] = de_tron_thi

    if f"dethi_{mon}_{lop}" in st.session_state:
        de_thi = st.session_state[f"dethi_{mon}_{lop}"]
        with st.form(f"form_thi_{mon}_{lop}"):
            tl_thi = {}
            for i, ch in enumerate(de_thi, 1):
                st.markdown(f"**Câu {i}:** {ch['nd']}")
                tl_thi[i] = st.radio(f"Đ/á {i}:", ch["da"], key=f"thi_{mon}_{lop}_{i}", index=None, label_visibility="collapsed")
                st.divider()
            if st.form_submit_button("🎯 NỘP BÀI", type="primary"):
                if None in tl_thi.values(): st.warning("⚠️ Còn câu chưa chọn!")
                else:
                    dung = sum(1 for i, ch in enumerate(de_thi, 1) if tl_thi[i] == ch["da"][ch["d"]])
                    diem = dung / len(de_thi) * 10
                    ghi_nhan_lich_su(f"Thi thử ({mon})", diem, dung, len(de_thi))
                    st.markdown(f"<div class='diem-thi'>🏆 ĐIỂM: {diem:.1f} / 10</div>", unsafe_allow_html=True)

# ==================== GIAO DIỆN CHÍNH (SIDEBAR) ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    st.caption("Hệ thống Ôn luyện THCS")
    
    so_nguoi_online = cap_nhat_nguoi_online()
    st.markdown(f"🟢 **Đang trực tuyến: {so_nguoi_online} học sinh**")
    st.divider()
    
    che_do = st.radio("⚙️ Chế độ & Công cụ:", ["🏠 Trang chủ / Hướng dẫn", "🔍 Tra cứu / Tìm kiếm", "📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra", "🎪 Phòng thí nghiệm ảo", "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"])
    st.divider()
    
    if che_do not in ["🏠 Trang chủ / Hướng dẫn", "🔍 Tra cứu / Tìm kiếm", "🎪 Phòng thí nghiệm ảo", "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"]:
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
        hien_thi_tien_do()
    elif che_do == "🔍 Tra cứu / Tìm kiếm":
        mon = "🔍 Tra cứu"
        hien_thi_tien_do()
    elif che_do == "🎪 Phòng thí nghiệm ảo":
        mon = "🎪 Phòng Thí Nghiệm"
        hien_thi_tien_do()
    elif che_do == "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)":
        mon = "⚙️ Trạm Nạp"
        hien_thi_tien_do()
    else:
        mon = "🏠 Trang chủ"
        hien_thi_tien_do()

if "search_jump" in st.session_state:
    jump_item = st.session_state["search_jump"]
    del st.session_state["search_jump"]
    che_do = "📖 Học theo chuyên đề"
    mon = jump_item["mon"]
    st.session_state["mon_main"] = mon

# ==================== ĐIỀU HƯỚNG MÀN HÌNH CHÍNH ====================
bai_dang_hoc = ""
du_lieu_bai_hien_tai = {}

if che_do == "🏠 Trang chủ / Hướng dẫn": hien_thi_trang_chu()
elif che_do == "🔍 Tra cứu / Tìm kiếm": hien_thi_tim_kiem_toan_dien()
elif che_do == "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)": hien_thi_tram_nap_du_lieu()
elif che_do == "🎪 Phòng thí nghiệm ảo":
    hien_thi_phong_thi_nghiem("📖 Môn Ngữ Văn", key_prefix="sidebar_mode")
else:
    st.markdown(f"""<div class="hero-banner"><p class="hero-title">{mon} — Chương trình GDPT 2018 (Kết Nối Tri Thức)</p><p class="hero-sub">Hệ thống học tập thông minh lớp 7</p></div>""", unsafe_allow_html=True)
    lop_dict = DATABASE[mon]
    if not lop_dict: st.warning(f"⚠️ Đang cập nhật dữ liệu cho môn **{mon}**...")
    else:
        ds_lop = list(lop_dict.keys())
        idx_lop = ds_lop.index("Lớp 7") if "Lớp 7" in ds_lop else 0
        if che_do == "📖 Học theo chuyên đề":
            col_l, col_c, col_b = st.columns([1, 2, 2])
            with col_l: lop = st.selectbox("🏫 Khối lớp:", ds_lop, index=idx_lop, key="lop_main")
            chuong_dict = lop_dict[lop]
            if chuong_dict:
                ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
                with col_c: chuong = st.selectbox("📂 Chọn Chương:", ds_chuong, key="chuong_main")
                bai_dict = chuong_dict[chuong]
                if bai_dict:
                    with col_b: bai = st.selectbox("📘 Chọn Chuyên đề:", list(bai_dict.keys()), key="bai_main")
                    bai_dang_hoc = f"{chuong} - {bai}"
                    du_lieu_bai_hien_tai = bai_dict[bai]
                    st.markdown("---")
                    hien_thi_bai(mon, lop, chuong, bai, bai_dict[bai])
        else:
            lop = st.selectbox("🏫 Khối lớp:", ds_lop, index=idx_lop, key="lop_thi")
            chuong_dict = lop_dict[lop]
            if chuong_dict: hien_thi_che_do_thi(mon, lop, chuong_dict)

# ==========================================================
# KHU VỰC GIA SƯ AI (ĐÃ SỬA CACHE & TÁCH BIỆT ẢNH ĐỘC LẬP)
# ==========================================================
if che_do not in ["🏠 Trang chủ / Hướng dẫn", "🔍 Tra cứu / Tìm kiếm", "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"]:
    st.divider()
    st.header("💬 Trợ lý AI 24/7 - Hỏi đáp cùng Gia sư")

    idx_mon_ai = 1 if "Vật lý" in mon else (2 if "Hóa học" in mon else (3 if "Ngữ Văn" in mon else 0))
    col_ai1, col_ai2, col_ai3, col_ai4 = st.columns([2.2, 1, 1.8, 1])
    with col_ai1:
        mon_hoc_ai = st.radio("Ngữ cảnh môn:", ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn", "Chuyện ngoài lề"], index=idx_mon_ai, horizontal=True, label_visibility="collapsed")
    with col_ai2:
        tu_dong_doc = st.checkbox("🔊 Đọc to", value=True)
    with col_ai3:
        che_do_nguon = st.selectbox(
            "Nguồn AI ưu tiên:",
            ["⚡ Ưu tiên Gemini (Nhanh)", "📚 Ưu tiên Dola (Chuẩn SGK)", "🤝 Kết hợp tuần tự (Dola -> Gemini)"],
            index=0,
            label_visibility="collapsed"
        )
    with col_ai4:
        if st.button("🗑️ Xóa chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    if mon_hoc_ai == "Ngữ Văn":
        SYSTEM_PROMPT = f"Bạn là giáo viên Ngữ Văn AI nhiệt tình, sâu sắc chuyên kèm môn Ngữ Văn lớp 7 sách Kết Nối Tri Thức. Học sinh đang học: '{mon}' ({bai_dang_hoc}). Hướng dẫn học sinh phân tích tác phẩm, cảm thụ văn học và lập dàn ý đoạn văn, không viết văn mẫu hộ."
    else:
        SYSTEM_PROMPT = f"Bạn là gia sư AI môn {mon_hoc_ai} lớp 7 sách Kết Nối Tri Thức. Đang học bài: {bai_dang_hoc}. Dùng phương pháp Socratic gợi mở từng bước, giải thích dễ hiểu, không giải bài hộ hoàn toàn."

    if "chat_history" not in st.session_state: st.session_state.chat_history = []
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    # XỬ LÝ ẢNH ĐỘC LẬP: Chỉ nạp ảnh khi người dùng bấm nút gửi ảnh, tránh dính ảnh cũ ở các câu sau
    img_pil, btn_gui_anh = None, False
    if HAS_PIL:
        with st.expander("📸 Mắt thần AI — Gửi ảnh chụp đề bài / đoạn văn", expanded=False):
            file_anh = st.file_uploader("Tải ảnh:", type=["png", "jpg", "jpeg"], key="uploader_anh_giasu")
            if file_anh:
                img_pil = Image.open(file_anh)
                st.image(img_pil, width=300)
                btn_gui_anh = st.button("🔍 Gửi ảnh cho Gia sư", type="primary")

    img_gui = img_pil if btn_gui_anh else None

    text_from_mic = speech_to_text(language='vi-VN', start_prompt="🔴 NÓI", stop_prompt="⏹️ DỪNG", just_once=True, key='STT') if HAS_MIC else None
    prompt = "Chị xem giúp em bài tập trong ảnh với ạ!" if btn_gui_anh else (text_from_mic or st.chat_input("Em đang mắc kẹt bài nào..."))

    if prompt:
        duoc_phep, giay_cho = kiem_tra_gioi_han_tan_suat(cooldown_seconds=3)
        if not duoc_phep:
            st.warning(f"⏳ Em thao tác hơi nhanh! Vui lòng chờ **{giay_cho} giây** nữa rồi gửi câu hỏi tiếp theo để hệ thống phân bổ tốt nhất nhé.")
        else:
            with st.chat_message("user"):
                if img_gui: st.image(img_gui, width=250)
                st.markdown(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                bo_nho_cache = lay_bo_nho_cache_ai()
                
                # SỬA CACHE: Chỉ lưu cache khi là câu đầu tiên của cuộc trò chuyện và có kèm bài đang học để không bị nhầm lẫn
                la_cau_dau = (len(st.session_state.chat_history) == 2)
                ma_hash = None
                if la_cau_dau and not img_gui:
                    chuoi_cache_key = f"{bai_dang_hoc}_{mon_hoc_ai}_{prompt.strip().lower()}"
                    ma_hash = hashlib.md5(chuoi_cache_key.encode('utf-8')).hexdigest()

                if ma_hash and ma_hash in bo_nho_cache:
                    ans_cached = bo_nho_cache[ma_hash]
                    st.markdown(ans_cached)
                    st.caption("⚡ *Phản hồi tức thì từ Bộ nhớ đệm tri thức*")
                    st.session_state.chat_history.append({"role": "assistant", "content": ans_cached})
                    doc_to_an_toan(ans_cached, autoplay=tu_dong_doc)
                else:
                    gemini_history = [{"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} for m in st.session_state.chat_history[:-1]]
                    ans_text_for_tts = ""
                    luu_history = ""

                    if che_do_nguon == "⚡ Ưu tiên Gemini (Nhanh)" or img_gui:
                        try:
                            with st.spinner("🤖 Gia sư Gemini đang suy nghĩ..."):
                                payload = [prompt, img_gui] if img_gui else prompt
                                ans_text = goi_gemini_an_toan(payload, system_instruction=SYSTEM_PROMPT, history=gemini_history)
                                st.markdown(ans_text)
                                luu_history = ans_text
                                ans_text_for_tts = ans_text
                        except Exception as err_gemini:
                            nd_dola = goi_dola_toi_uu(prompt) if not img_gui else None
                            if nd_dola:
                                luu_history = f"📚 **Nội dung chuẩn SGK (Từ Dola dự phòng):**\n\n{nd_dola}"
                                st.info(luu_history)
                                ans_text_for_tts = nd_dola
                            elif du_lieu_bai_hien_tai.get("ly_thuyet"):
                                lt_noi_bo = du_lieu_bai_hien_tai.get("ly_thuyet", "")
                                luu_history = (
                                    f"💡 *Hệ thống đang chuyển sang kho tri thức cục bộ của bài học:*\n\n"
                                    f"{lt_noi_bo}"
                                )
                                st.info(luu_history)
                                ans_text_for_tts = lt_noi_bo
                            else:
                                st.error("⚠️ Hệ thống AI đang bận. Em vui lòng thử lại sau vài giây nhé!")

                    elif che_do_nguon == "📚 Ưu tiên Dola (Chuẩn SGK)":
                        with st.spinner("📚 Đang tra cứu nhanh Dola..."):
                            nd_dola = goi_dola_toi_uu(prompt)
                        if nd_dola:
                            luu_history = f"✅ **Nội dung chuẩn theo SGK (Dola):**\n\n{nd_dola}"
                            st.info(luu_history)
                            ans_text_for_tts = nd_dola
                        else:
                            try:
                                with st.spinner("⚡ Dola đang bận, chuyển ngay sang Gia sư Gemini..."):
                                    ans_text = goi_gemini_an_toan(prompt, system_instruction=SYSTEM_PROMPT, history=gemini_history)
                                    st.markdown(ans_text)
                                    luu_history = ans_text
                                    ans_text_for_tts = ans_text
                            except Exception:
                                st.error("⚠️ Tạm thời chưa kết nối được hệ thống AI.")

                    else:
                        with st.spinner("🔍 Đang tra cứu dữ liệu chuẩn..."):
                            nd_dola = goi_dola_toi_uu(prompt)
                        try:
                            with st.spinner("🤖 Gia sư Gemini đang diễn giải..."):
                                if nd_dola:
                                    cau_truyen = f"Nội dung chuẩn SGK:\n{nd_dola}\n\nHãy diễn giải thật dễ hiểu cho học sinh lớp 7 câu hỏi: {prompt}"
                                    ans_text = goi_gemini_an_toan(cau_truyen, system_instruction=SYSTEM_PROMPT, history=gemini_history)
                                    c1, c2 = st.columns(2)
                                    with c1:
                                        st.markdown("✅ **Nội dung chuẩn (Dola)**")
                                        st.info(nd_dola)
                                    with c2:
                                        st.markdown("💡 **Gia sư giải thích (Gemini)**")
                                        st.success(ans_text)
                                    luu_history = f"**✅ NỘI DUNG CHUẨN (Dola):**\n\n> {nd_dola}\n\n---\n**💡 GIA SƯ GIẢI THÍCH (Gemini):**\n\n{ans_text}"
                                    ans_text_for_tts = ans_text
                                else:
                                    ans_text = goi_gemini_an_toan(prompt, system_instruction=SYSTEM_PROMPT, history=gemini_history)
                                    st.markdown(ans_text)
                                    luu_history = ans_text
                                    ans_text_for_tts = ans_text
                        except Exception:
                            if nd_dola:
                                luu_history = f"✅ **Nội dung chuẩn SGK (Dola):**\n\n{nd_dola}"
                                st.info(luu_history)
                                ans_text_for_tts = nd_dola
                            else:
                                st.error("⚠️ Đường truyền AI đang bận, em thử lại nhé.")

                    if luu_history:
                        st.session_state.chat_history.append({"role": "assistant", "content": luu_history})
                        # Giới hạn kích thước bộ nhớ đệm tối đa 100 mục để không bị phình RAM
                        if ma_hash and len(bo_nho_cache) < 100:
                            bo_nho_cache[ma_hash] = luu_history

                if HAS_TTS and ans_text_for_tts:
                    doc_to_an_toan(ans_text_for_tts, autoplay=tu_dong_doc)
