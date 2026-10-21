# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản: 2.0 — Đã vá lỗi & Tối ưu cấu trúc
Cập nhật:
 ✅ Hoàn thiện code bị cắt ở cuối
 ✅ Khởi tạo biến an toàn, xử lý ngoại lệ đầy đủ
 ✅ Sửa regex nhận diện số
 ✅ Thêm giới hạn đăng nhập admin & kiểm tra dữ liệu
 ✅ Cấu trúc rõ ràng, tách logic thành các phần độc lập
"""
import streamlit as st
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
import google.generativeai as genai

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Xử lý nhảy trang từ tìm kiếm
if "search_jump" in st.session_state:
    item = st.session_state.pop("search_jump")
    st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
    st.session_state["mon_main"] = item["mon"]
    st.session_state["chuong_main"] = item["chuong"]
    st.session_state["bai_main"] = item["bai"]

# ==================== KHỞI TẠO LỖI & BIẾN TOÀN CỤC ====================
@st.cache_resource
def get_global_resources():
    return {
        "ai_api_lock": threading.Lock(),
        "user_count_lock": threading.Lock(),
        "ai_cache_lock": threading.Lock(),
        "online_users": {},
        "ai_cache": OrderedDict()
    }

GLOBALS = get_global_resources()

# ==================== ĐỌC BIẾN MÔI TRƯỜNG & SECRETS ====================
def get_secret(key_name, default_val=""):
    """An toàn lấy giá trị từ st.secrets hoặc biến môi trường"""
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

    for k_name in ["GEMINI_API_KEY", "GEMINI_API_KEY_1", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"]:
        k_val = get_secret(k_name)
        if k_val and str(k_val).strip() not in keys:
            keys.append(str(k_val).strip())
    return keys

# Tải cấu hình hệ thống
GEMINI_KEYS = lay_danh_sach_gemini_keys()
DOLA_ENDPOINT = str(get_secret("DOLA_API_ENDPOINT")).strip()
DOLA_KEY = str(get_secret("DOLA_API_KEY")).strip()
DOLA_PROJECT_TIER = str(get_secret("DOLA_PROJECT_TIER", "high_limit_edu")).strip()
ADMIN_PASS = str(get_secret("ADMIN_PASSWORD", "")).strip()

# ==================== HỆ THỐNG ĐẾM NGƯỜI DÙNG & RATE LIMIT ====================
def cap_nhat_nguoi_online():
    """Cập nhật và trả số người đang trực tuyến (hết hạn sau 5 phút không hoạt động)"""
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
    """Giới hạn tần suất gọi AI — Trả (cho_phép, thời gian_chờ)"""
    now = time.time()
    last_time = st.session_state.get("last_ai_request_time", 0.0)
    elapsed = now - last_time
    if elapsed < cooldown_seconds:
        return False, int(cooldown_seconds - elapsed) + 1
    st.session_state["last_ai_request_time"] = now
    return True, 0

# ==================== HỆ THỐNG CACHE AI ====================
def tao_ma_hash_cau_hoi(mon_hoc, bai_hoc, che_do, cau_hoi):
    """Tạo mã băm duy nhất cho mỗi cặp câu hỏi - ngữ cảnh"""
    c_clean = re.sub(r'\s+', ' ', cau_hoi.strip().lower())
    chuoi_chuan = f"{mon_hoc.strip()}_{bai_hoc.strip()}_{che_do}_{c_clean}"
    return hashlib.md5(chuoi_chuan.encode('utf-8')).hexdigest()

def luu_cache_ai(ma_hash, noi_dung):
    """Lưu vào cache, bỏ qua các thông báo lỗi hệ thống"""
    nd_lower = noi_dung.lower()
    bo_qua_tu_khoa = ["bận", "quá tải", "lỗi", "chuyển sang", "bảo trì"]
    if any(k in nd_lower for k in bo_qua_tu_khoa) or "⚠️" in noi_dung:
        return
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        cache[ma_hash] = noi_dung
        cache.move_to_end(ma_hash)
        if len(cache) > 100:  # Giữ tối đa 100 mục gần nhất
            cache.popitem(last=False)

def lay_cache_ai(ma_hash):
    """Lấy từ cache nếu có, cập nhật vị trí sử dụng gần nhất"""
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        if ma_hash in cache:
            cache.move_to_end(ma_hash)
            return cache[ma_hash]
    return None

# ==================== HÀM TIỆN ÍCH CHẤM ĐIỂM & SO SÁNH ====================
def ep_kieu_so_hoc(chuoi):
    """Chuyển chuỗi thành số — Hỗ trợ định dạng VN (1.000,5) và quốc tế (1,000.5)"""
    s = str(chuoi).strip().replace(" ", "")
    if not s:
        return None
    
    # Phân số a/b
    if '/' in s:
        parts = s.split('/')
        if len(parts) == 2:
            try:
                return float(parts[0]) / float(parts[1])
            except (ValueError, ZeroDivisionError):
                return None
    
    # Số định dạng Việt Nam: 1.234.567,89
    if re.fullmatch(r'-?\d{1,3}(?:\.\d{3})*(?:,\d+)?', s):
        s = s.replace('.', '').replace(',', '.')
    # Định dạng khác: chỉ thay dấu phẩy thành dấu chấm thập phân
    else:
        s = s.replace(',', '.')
        
    try:
        return float(s)
    except ValueError:
        return None

def so_sanh_so_hoc(nguoi_dung_nhap, danh_sach_dung):
    """So sánh đáp án — chấp nhận sai số nhỏ cho tính toán thập phân"""
    val_x = ep_kieu_so_hoc(nguoi_dung_nhap)
    for dap_an_dung in danh_sach_dung:
        val_d = ep_kieu_so_hoc(dap_an_dung)
        if val_x is not None and val_d is not None:
            if abs(val_x - val_d) < 1e-5:
                return True
        # So sánh chuỗi chính xác (dành cho biểu thức đại số)
        if re.sub(r'\s+', '', str(nguoi_dung_nhap).lower()) == re.sub(r'\s+', '', str(dap_an_dung).lower()):
            return True
    return False

def tron_dap_an_thong_minh(cau_hoi):
    """Trộn thứ tự đáp án, bỏ trộn nếu có đáp án đặc biệt như 'Tất cả'"""
    ds_dap_an = list(cau_hoi["da"])
    vi_tri_dung_goc = cau_hoi["d"]
    dap_an_dung = ds_dap_an[vi_tri_dung_goc]
    
    # Không trộn nếu có phương án tổng hợp
    for ans in ds_dap_an:
        txt = str(ans).lower()
        if "cả" in txt or "tất cả" in txt or "đáp án" in txt or "phương án" in txt or "a, b" in txt:
            return ds_dap_an, vi_tri_dung_goc
    
    # Trộn và tìm vị trí mới của đáp án đúng
    ds_moi = ds_dap_an.copy()
    random.shuffle(ds_moi)
    vi_tri_moi = ds_moi.index(dap_an_dung)
    return ds_moi, vi_tri_moi

def lam_sach_id(s):
    """Loại bỏ ký tự đặc biệt, chỉ giữ chữ-số-gạch"""
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))

def sap_xep_chuong(danh_sach_chuong):
    """Sắp xếp chương theo số thứ tự thay vì thứ tự từ điển"""
    def lay_so_thu_tu(ten_chuong):
        m = re.search(r'\d+', str(ten_chuong))
        return int(m.group(0)) if m else 999
    return sorted(danh_sach_chuong, key=lay_so_thu_tu)

def ghi_nhan_lich_su(tieu_de_bai, diem, so_cau_dung, tong_so_cau):
    """Lưu kết quả học tập vào lịch sử"""
    if 'lich_su_hoc_tap' not in st.session_state:
        st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {
        "bai": tieu_de_bai,
        "diem": diem,
        "dung": so_cau_dung,
        "tong": tong_so_cau
    })

# ==================== TÍCH HỢP AI ====================
def goi_dola_toi_uu(cau_hoi):
    """Gọi API Dola — trả None nếu không cấu hình hoặc lỗi"""
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
            timeout=5.0
        )
        if phan_hoi.status_code == 200:
            nd = phan_hoi.json().get("noi_dung_chuan", "")
            return nd.strip() if nd else None
        return None
    except Exception:
        return None

@st.cache_resource(ttl=3600, show_spinner=False)
def lay_danh_sach_model(api_key):
    """Lấy danh sách model khả dụng với khóa API, ưu tiên phiên bản mới nhất"""
    uu_tien = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
    try:
        genai.configure(api_key=api_key)
        ds_support = [
            m.name.replace("models/", "")
            for m in genai.list_models()
            if "generateContent" in getattr(m, "supported_generation_methods", [])
        ]
        if ds_support:
            return ([m for m in uu_tien if m in ds_support] +
                    [m for m in ds_support if "gemini" in m and m not in uu_tien])
    except Exception:
        pass
    return uu_tien

def goi_gemini_an_toan(noi_dung, system_prompt, lich_su=None):
    """
    Gọi Gemini với cơ chế:
     - ✅ Luân phiên nhiều khóa API khi gặp giới hạn
     - ✅ Khóa luồng tránh xung đột cấu hình toàn cục
     - ✅ Thử lại khi gặp lỗi tạm thời
    """
    if not GEMINI_KEYS:
        raise RuntimeError("Chưa cấu hình GEMINI_API_KEY — Vui lòng kiểm tra Secrets")
    
    if "key_index" not in st.session_state:
        st.session_state["key_index"] = 0
    
    so_key = len(GEMINI_KEYS)
    last_err = RuntimeError("Không thể kết nối đến AI — Vui lòng thử lại sau ít phút")

    with GLOBALS["ai_api_lock"]:
        for k_offset in range(so_key):
            idx_khoa_hien_tai = (st.session_state["key_index"] + k_offset) % so_key
            khoa_hien_hanh = GEMINI_KEYS[idx_khoa_hien_tai]
            
            genai.configure(api_key=khoa_hien_hanh)
            ds_model = lay_danh_sach_model(khoa_hien_hanh)
            
            for ten_model in ds_model:
                for lan_thu in range(2):
                    try:
                        model = genai.GenerativeModel(
                            model_name=ten_model,
                            system_instruction=system_prompt
                        )
                        
                        if lich_su is not None and len(lich_su) > 0:
                            chuyen_tiep = model.start_chat(history=lich_su)
                            ket_qua = chuyen_tiep.send_message(noi_dung).text
                        else:
                            ket_qua = model.generate_content(noi_dung).text
                        
                        st.session_state["key_index"] = idx_khoa_hien_tai
                        return ket_qua.strip()
                    
                    except Exception as e:
                        last_err = e
                        thong_bao_loi = str(e).lower()
                        
                        if "404" in thong_bao_loi or "not found" in thong_bao_loi:
                            break  # Model không tồn tại → thử model tiếp theo
                        elif "429" in thong_bao_loi or "quota" in thong_bao_loi or "resource exhausted" in thong_bao_loi:
                            if lan_thu == 0:
                                time.sleep(1.2)
                                continue  # Thử lại 1 lần với cùng khóa
                            else:
                                break  # Hết quota → chuyển khóa tiếp theo
                        else:
                            break  # Lỗi khác → thử khóa tiếp theo
    
    # Đã thử hết mọi cách vẫn lỗi
    raise last_err

# ==================== NẠP DỮ LIỆU CHƯƠNG TRÌNH ====================
def nap_du_lieu_mon_hoc():
    """Nạp module dữ liệu từ file riêng, thông báo nếu thiếu"""
    du_lieu = {}
    mon = [
        ("data_toan", "TOAN", "📐 Toán"),
        ("data_vatly", "VATLY", "🔬 Vật lý"),
        ("data_hoa", "HOA", "🧪 Hóa học")
    ]
    
    for module_name, var_name, ten_hien_thi in mon:
        try:
            module = __import__(module_name)
            du_lieu[var_name] = getattr(module, var_name, {})
        except ImportError:
            st.warning(f"⚠️ Chưa có file dữ liệu: `{module_name}.py` — {ten_hien_thi} tạm ẩn")
            du_lieu[var_name] = {}
    
    # Dữ liệu Ngữ Văn tích hợp sẵn
    du_lieu["VAN"] = {
        "Lớp 7": {
            "Chương 1: Bầu trời tuổi thơ (Truyện)": {
                "Văn bản 1: Bồng chanh đỏ (trích, Đỗ Chu)": {
                    "ly_thuyet": "Truyện ngắn kể về hai anh em Hoài và Ý với tình yêu thương loài vật, thiên nhiên.",
                    "cau_hoi": [
                        {"nd": "Truyện 'Bồng chanh đỏ' của tác giả nào?", "da": ["Đỗ Chu", "Tô Hoài", "Khánh Hoài"], "d": 0},
                        {"nd": "Nhân vật chính là ai?", "da": ["Anh em Hoài Ý", "Ông nội", "Thành và Thủy"], "d": 0}
                    ],
                    "bt_co_ban": [
                        {"de": "Ý nghĩa nhan đề?", "dd": ["Vẻ đẹp thiên nhiên"], "lg": "Biểu tượng tuổi thơ."}
                    ],
                    "bt_nang_cao": [
                        {"de": "Tâm trạng nhân vật Hoài?", "dd": ["Thấu hiểu và buông bỏ"], "lg": "Sự nhân hậu."}
                    ]
                }
            }
        }
    }
    return du_lieu

# Khởi tạo dữ liệu
DU_LIEU = nap_du_lieu_mon_hoc()
TOAN, VATLY, HOA, VAN = DU_LIEU["TOAN"], DU_LIEU["VATLY"], DU_LIEU["HOA"], DU_LIEU["VAN"]

DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA,
    "📖 Môn Ngữ Văn": VAN
}

# ==================== GIAO DIỆN SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    dark_mode = st.toggle("🌙 Chế độ tối", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")
    st.divider()
    
    che_do = st.radio(
        "⚙️ Chức năng:",
        [
            "🏠 Trang chủ / Hướng dẫn",
            "🔍 Tra cứu / Tìm kiếm",
            "📖 Học theo chuyên đề",
            "📝 Phòng thi / Kiểm tra",
            "🎪 Phòng thí nghiệm ảo",
            "⚙️ Trạm Nạp Dữ Liệu"
        ],
        key="che_do_sidebar"
    )
    
    if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = che_do
    
    # Hiển thị lịch sử học tập
    if 'lich_su_hoc_tap' in st.session_state and st.session_state.lich_su_hoc_tap:
        st.divider()
        st.markdown("### 📊 Lịch sử học tập")
        ds = st.session_state.lich_su_hoc_tap
        so_bai = len(ds)
        diem_tb = sum(i['diem'] for i in ds) / so_bai
        st.metric("Điểm TB", f"{diem_tb:.1f}", f"{so_bai} bài")

# ==================== GIAO DIỆN CHÍNH — CSS THEO CHẾ ĐỘ ====================
if dark_mode:
    st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #F1F5F9; }
    .main .block-container { padding-top: 1.2rem; max-width: 95%; }
    [data-testid="stToolbarActions"], footer { display: none !important; }
    .card-home { background-color: #1E293B; border: 1px solid #334155; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; }
    .khung-lythuyet { background-color: #1E293B; padding: 1.2rem; border-left: 6px solid #3B82F6; }
    .diem-thi { font-size: 1.6rem; color: #F87171; text-align: center; padding: 1.2rem; border: 2px dashed #EF4444; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .main .block-container { padding-top: 1.2rem; max-width: 95%; }
    [data-testid="stToolbarActions"], footer { display: none !important; }
    .card-home { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; }
    .khung-lythuyet { background-color: #EFF6FF; padding: 1.2rem; border-left: 6px solid #2563EB; }
    .diem-thi { font-size: 1.6rem; color: #E11D48; text-align: center; padding: 1.2rem; border: 2px dashed #F43F5E; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# ==================== BIẾN TOÀN CỤC CHO PHẦN HỌC BÀI ====================
bai_dang_hoc = ""
du_lieu_bai_hien_tai = {}

# ==================== TRANG CHỦ ====================
if che_do == "🏠 Trang chủ / Hướng dẫn":
    st.markdown("<h2>🎓 HỆ THỐNG HỌC TẬP THCS — KẾT NỐI TRI THỨC (LỚP 7)</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.markdown("""
    <div class='card-home'>
    <h3>🌟 Tính năng nổi bật</h3>
    <p>📖 Học theo chuyên đề • ✏️ Trắc nghiệm & Tự luận • 🔍 Tra cứu thông minh • 📊 Theo dõi tiến độ</p>
    </div>
    """, unsafe_allow_html=True)
    c2.markdown("""
    <div class='card-home'>
    <h3>💬 Gia Sư AI Thông Minh</h3>
    <p>Trợ lý AI giải đáp bài tập 24/7 • Bộ nhớ ngữ cảnh • Lưu kết quả vào cache • Luân phiên khóa API chống quá tải</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TÌM KIẾM / TRA CỨU ====================
elif che_do == "🔍 Tra cứu / Tìm kiếm":
    tu_khoa = st.text_input("🔎 Nhập từ khóa:")
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        tim_thay = False
        for t_mon, l_dict in DATABASE.items():
            if not l_dict:
                continue
            for lop, c_dict in l_dict.items():
                for chuong, b_dict in c_dict.items():
                    for t_bai, data in b_dict.items():
                        if (kw in t_bai.lower() or 
                            kw in data.get("ly_thuyet", "").lower() or
                            any(kw in str(c.get("nd","")).lower() for c in data.get("cau_hoi",[]))):
                            tim_thay = True
                            with st.expander(f"[{t_mon}] {chuong} — {t_bai}"):
                                if st.button("📖 Mở bài học", key=f"btn_{lam_sach_id(t_bai)}"):
                                    st.session_state["search_jump"] = {
                                        "mon": t_mon, "chuong": chuong, "bai": t_bai
                                    }
                                    st.rerun()
        if not tim_thay:
            st.info("🔍 Không tìm thấy nội dung phù hợp với từ khóa")

# ==================== TRẠM NẠP DỮ LIỆU (QUẢN TRỊ) ====================
elif che_do == "⚙️ Trạm Nạp Dữ Liệu":
    st.markdown("### ⚙️ Trạm Nạp Dữ Liệu Quản Trị")
    
    # Khởi tạo biến đếm lần thử đăng nhập
    if 'admin_login_attempt' not in st.session_state:
        st.session_state.admin_login_attempt = 0
    
    mk = st.text_input("🔑 Mật khẩu quản trị:", type="password", key="admin_pass_input")
    
    if not ADMIN_PASS:
        st.warning("⚠️ Chưa thiết lập `ADMIN_PASSWORD` trong Secrets — Tính năng bị khóa")
    elif st.session_state.admin_login_attempt >= 3:
        st.error("🚫 Đã vượt quá số lần thử. Tải lại trang để thử lại.")
    elif mk:
        if hmac.compare_digest(mk, ADMIN_PASS):
            st.session_state.admin_login_attempt = 0
            st.success("✅ Xác thực thành công — Chào mừng Quản trị viên")
            # === NỘI DUNG CHỨC NĂNG QUẢN TRỊ ===
            st.info("📁 Chức năng nạp dữ liệu đang hoạt động...")
            # TODO: Thêm logic nạp file dữ liệu tại đây
        else:
            st.session_state.admin_login_attempt += 1
            con_lai = 3 - st.session_state.admin_login_attempt
            st.error(f"❌ Sai mật khẩu! Còn {con_lai} lần thử")

# ==================== PHÒNG THÍ NGHIỆM ẢO ====================
elif che_do == "🎪 Phòng thí nghiệm ảo":
    st.markdown("### 🎪 Phòng Thí Nghiệm PhET — Đại học Colorado")
    st.info("🔬 Mô phỏng trực quan các hiện tượng Vật lý, Hóa học, Toán học và Địa lý.")
    st.markdown("👉 Truy cập tại: **[phet.colorado.edu](https://phet.colorado.edu/)**")

# ==================== HỌC THEO CHUYÊN ĐỀ / PHÒNG THI ====================
elif che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
    lop_dict = DATABASE.get(mon, {})
    
    if not lop_dict:
        st.warning(f"⚠️ Dữ liệu môn {mon} đang được cập nhật, vui lòng quay lại sau")
        st.stop()
    
    # Chọn lớp → chương → bài
    c_lop, c_chuong, c_bai = st.columns([1, 2, 2])
    ds_lop = list(lop_dict.keys())
    lop = c_lop.selectbox("Khối:", ds_lop, key="s_lop")
    
    chuong_dict = lop_dict.get(lop, {})
    if not chuong_dict:
        st.warning("⚠️ Chưa có dữ liệu chương cho khối này")
        st.stop()
    
    ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
    idx_c = (ds_chuong.index(st.session_state.get("chuong_main")) 
             if st.session_state.get("chuong_main") in ds_chuong else 0)
    chuong = c_chuong.selectbox("Chương:", ds_chuong, index=idx_c, key="s_chuong")
    
    bai_dict = chuong_dict.get(chuong, {})
    if not bai_dict:
        st.warning("⚠️ Chưa có bài học trong chương này")
        st.stop()
    
    ds_bai = list(bai_dict.keys())
    idx_b = (ds_bai.index(st.session_state.get("bai_main"))
             if st.session_state.get("bai_main") in ds_bai else 0)
    bai = c_bai.selectbox("Bài:", ds_bai, index=idx_b, key="s_bai")
    
    # Lưu thông tin bài đang học
    bai_dang_hoc = f"{chuong} — {bai}"
    du_lieu_bai_hien_tai = bai_dict[bai]
    
    # Tabs nội dung bài học
    lt_tab, bt_tab, tn_tab = st.tabs(["📚 Lý thuyết", "✏️ Bài tập", "📝 Trắc nghiệm"])
    
    with lt_tab:
        noi_dung_lt = du_lieu_bai_hien_tai.get("ly_thuyet", "")
        if noi_dung_lt:
            st.markdown(f"<div class='khung-lythuyet'>{noi_dung_lt}</div>", unsafe_allow_html=True)
        else:
            st.info("📖 Nội dung lý thuyết đang được cập nhật")
    
    with bt_tab:
        ds_bt = du_lieu_bai_hien_tai.get("bt_co_ban", [])
        if not ds_bt:
            st.info("✏️ Chưa có bài tập cho bài này")
        else:
            for so_bt, bt in enumerate(ds_bt, 1):
                with st.expander(f"Bài {so_bt}: {bt['de']}"):
                    if "Ngữ Văn" in mon:
                        if st.button("💡 Xem gợi ý", key=f"g_{so_bt}"):
                            st.info(bt.get('lg', bt.get('dd', [''])[0]))
                    else:
                        cau_tra_loi = st.text_input("Kết quả:", key=f"kq_{so_bt}")
                        if st.button("✅ Chấm điểm", key=f"c_{so_bt}"):
                            ds_dung = bt.get("dd", [])
                            if so_sanh_so_hoc(cau_tra_loi, ds_dung):
                                st.success("✅ Chính xác! Tuyệt vời 🎉")
                            else:
                                st.error(f"❌ Chưa đúng. Gợi ý đáp án: {', '.join(ds_dung)}")
    
    with tn_tab:
        ds_cau_hoi = du_lieu_bai_hien_tai.get("cau_hoi", [])
        if not ds_cau_hoi:
            st.info("📝 Chưa có câu hỏi trắc nghiệm cho bài này")
        else:
            if st.button("🔄 Tạo bộ đề mới", use_container_width=True):
                st.session_state.pop(f"de_{lam_sach_id(bai)}", None)
                st.rerun()
            
            key_de = f"de_{lam_sach_id(bai)}"
            if key_de not in st.session_state or st.session_state[key_de] is None:
                de_tron = []
                for ch in ds_cau_hoi:
                    dap_an_moi, vi_tri_dung_moi = tron_dap_an_thong_minh(ch)
                    de_tron.append({
                        "nd": ch["nd"],
                        "da": dap_an_moi,
                        "d": vi_tri_dung_moi
                    })
                st.session_state[key_de] = de_tron
            
            with st.form(f"form_{lam_sach_id(bai)}"):
                cau_tra_loi = {}
                de_hien_tai = st.session_state[key_de]
                for so_cau, cau in enumerate(de_hien_tai, 1):
                    st.markdown(f"**Câu {so_cau}:** {cau['nd']}")
                    cau_tra_loi[so_cau] = st.radio(
                        f"Chọn đáp án cho câu {so_cau}",
                        cau["da"],
                        key=f"rad_{lam_sach_id(bai)}_{so_cau}",
                        index=None,
                        label_visibility="collapsed"
                    )
                
                if st.form_submit_button("📩 Nộp bài & Chấm điểm", type="primary", use_container_width=True):
                    tong = len(de_hien_tai)
                    dung = 0
                    for so_cau, cau in enumerate(de_hien_tai, 1):
                        if cau_tra_loi.get(so_cau) == cau["da"][cau["d"]]:
                            dung += 1
                        else:
                            st.error(f"❌ Câu {so_cau} sai. Đáp án đúng: **{cau['da'][cau['d']]}**")
                    
                    diem_so = (dung / tong) * 10 if tong > 0 else 0
                    st.markdown(
                        f"<div class='diem-thi'>🏆 ĐIỂM: {diem_so:.1f}/10<br>"
                        f"<small>Đúng {dung}/{tong} câu</small></div>",
                        unsafe_allow_html=True
                    )
                    ghi_nhan_lich_su(bai_dang_hoc, diem_so, dung, tong)

    # ==================== GIA SƯ AI — TÍCH HỢP Ở CUỐI TRANG HỌC ====================
    st.divider()
    st.header("💬 Gia sư AI — Hỏi đáp bài tập")
    
    col1, col2, col3 = st.columns([2, 2, 1])
    mon_ai = col1.radio(
        "Môn học:",
        ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn"],
        horizontal=True,
        label_visibility="collapsed"
    )
    nguon_ai = col2.selectbox(
        "Nguồn AI:",
        ["⚡ Gemini", "🤝 Dola → Gemini"],
        label_visibility="collapsed"
    )
    if col3.button("🗑️ Xóa lịch sử", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    # Khởi tạo lịch sử hội thoại
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Hiển thị lịch sử hội thoại
    for tin_nhan in st.session_state.chat_history:
        with st.chat_message(tin_nhan["role"]):
            st.markdown(tin_nhan["content"])

    # Nhập câu hỏi mới
    cau_hoi_nguoi_dung = st.chat_input("💡 Đặt câu hỏi cho gia sư AI...")
    if cau_hoi_nguoi_dung:
        # Kiểm tra giới hạn tần suất
        duoc_goi, thoi_gian_cho = kiem_tra_gioi_han_tan_suat()
        if not duoc_goi:
            st.warning(f"⏳ Vui lòng chờ {thoi_gian_cho} giây rồi hỏi tiếp nhé!")
        else:
            # Hiển thị câu hỏi người dùng
            with st.chat_message("user"):
                st.markdown(cau_hoi_nguoi_dung)
            st.session_state.chat_history.append({"role": "user", "content": cau_hoi_nguoi_dung})
            
            # Tạo khóa cache
            la_cau_dau_tien = len(st.session_state.chat_history) <= 2
            ma_cache = tao_ma_hash_cau_hoi(mon_ai, bai_dang_hoc, nguon_ai, cau_hoi_nguoi_dung) if la_cau_dau_tien else None
            cau_tra_loi_cache = lay_cache_ai(ma_cache) if ma_cache else None
            
            if cau_tra_loi_cache:
                # Dùng dữ liệu có sẵn trong cache
                with st.chat_message("assistant"):
                    st.markdown(cau_tra_loi_cache)
                st.session_state.chat_history.append({"role": "assistant", "content": cau_tra_loi_cache})
            else:
                # Gọi AI tạo câu trả lời mới
                with st.chat_message("assistant"):
                    with st.spinner("🤖 AI đang suy nghĩ..."):
                        # Chuẩn bị lịch sử hội thoại cho AI
                        lich_su_dinh_dang = []
                        for msg in st.session_state.chat_history[:-1]:
                            vai_tro = "user" if msg["role"] == "user" else "model"
                            lich_su_dinh_dang.append({
                                "role": vai_tro,
                                "parts": [msg["content"]]
                            })
                        
                        # Hướng dẫn hệ thống cho AI
                        sys_prompt = (
                            f"Bạn là gia sư {mon_ai} cho học sinh lớp 7. "
                            f"Học sinh đang học bài: {bai_dang_hoc}. "
                            "Giải thích ngắn gọn, dễ hiểu. Hướng dẫn tư duy thay vì đưa đáp án ngay. "
                            "Dùng ví dụ đơn giản phù hợp trình độ THCS."
                        )
                        
                        cau_tra_loi = ""
                        try:
                            if "Dola" in nguon_ai:
                                cau_tra_loi = goi_dola_toi_uu(cau_hoi_nguoi_dung)
                                if not cau_tra_loi:
                                    cau_tra_loi = goi_gemini_an_toan(
                                        cau_hoi_nguoi_dung,
                                        sys_prompt,
                                        lich_su_dinh_dang
                                    )
                            else:
                                cau_tra_loi = goi_gemini_an_toan(
                                    cau_hoi_nguoi_dung,
                                    sys_prompt,
                                    lich_su_dinh_dang
                                )
                            
                            st.markdown(cau_tra_loi)
                            st.session_state.chat_history.append({
                                "role": "assistant",
                                "content": cau_tra_loi
                            })
                            
                            # Lưu vào cache
                            if ma_cache and cau_tra_loi:
                                luu_cache_ai(ma_cache, cau_tra_loi)
                        
                        except Exception as loi:
                            thong_bao_loi = f"⚠️ Xin lỗi, gặp lỗi: {str(loi)}\n\nVui lòng thử lại sau ít phút nhé!"
                            st.error(thong_bao_loi)
                            st.session_state.chat_history.append({
                                "role": "assistant",
                                "content": thong_bao_loi
                            })
