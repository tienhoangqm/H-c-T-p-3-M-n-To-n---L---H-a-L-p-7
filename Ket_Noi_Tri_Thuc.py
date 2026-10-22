# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Đã vá lỗi và tối ưu hóa cấu trúc
"""
import streamlit as st
import uuid
import time
import re
import hashlib
import os
import threading
from collections import OrderedDict
import html

# 1. Cấu hình trang (phải là dòng lệnh Streamlit đầu tiên)
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Xử lý Dữ liệu (Dùng Mock data nếu không có file thực tế)
def get_mock_data():
    return {"Lớp 7": {"Chương 1": {"Bài 1": {"ly_thuyet": "Đang cập nhật nội dung...", "cau_hoi": []}}}}

try:
    from data_toan import TOAN
except ImportError: TOAN = get_mock_data()
try:
    from data_vatly import VATLY
except ImportError: VATLY = get_mock_data()
try:
    from data_hoa import HOA
except ImportError: HOA = get_mock_data()
try:
    from data_anh import ANH
except ImportError: ANH = get_mock_data()

# Database chính
DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA,
    "📖 Môn Ngữ Văn": {"Lớp 7": {"Chương 1": {"Bài 1": {"ly_thuyet": "Văn bản mẫu", "cau_hoi": []}}}},
    "🇬🇧 Môn Tiếng Anh": ANH
}

MON_SANG_CHU_DE = {
    "📐 Môn Toán": "toan",
    "🔬 Môn Vật lý (KHTN)": "vatly",
    "🧪 Môn Hóa học (KHTN)": "hoa",
    "📖 Môn Ngữ Văn": "van",
    "🇬🇧 Môn Tiếng Anh": "anh"
}

# 3. Các hàm hỗ trợ (Fix các lỗi thiếu hàm)
def lay_chu_de(mon):
    return MON_SANG_CHU_DE.get(mon, "home")

def get_secret(key_name, default_val=""):
    return st.secrets.get(key_name, os.getenv(key_name, default_val))

@st.cache_resource
def get_global_locks():
    return {
        "user_count_lock": threading.Lock(),
        "online_users": {},
    }
GLOBALS = get_global_locks()

def cap_nhat_nguoi_online():
    with GLOBALS["user_count_lock"]:
        if "user_id" not in st.session_state:
            st.session_state.user_id = str(uuid.uuid4())
        bo_nho = GLOBALS["online_users"]
        bo_nho[st.session_state.user_id] = time.time()
        now = time.time()
        # Xóa user quá 5 phút
        ds_online = {uid: t for uid, t in bo_nho.items() if now - t < 300}
        GLOBALS["online_users"] = ds_online
        return len(ds_online)

def dem_chuong_bai(mon):
    lop_dict = DATABASE.get(mon, {})
    so_chuong = sum(len(c) for c in lop_dict.values())
    so_bai = sum(len(b) for c in lop_dict.values() for b in c.values())
    return so_chuong, so_bai

# 4. Giao diện (CSS)
def css_giao_dien_chung():
    return """
    <style>
    .hb{position:relative;overflow:hidden;border-radius:20px;padding:1.4rem 1.5rem;margin:.2rem 0 1.3rem;color:#fff;background:linear-gradient(135deg,#3730A3 0%,#6D28D9 55%,#DB2777 100%);box-shadow:0 14px 30px -12px #6D28D9;}
    .hb-than{position:relative;z-index:1;display:flex;align-items:center;gap:1.1rem;}
    .hb-tieu-de{margin:0;font-size:2rem;font-weight:800;color:#FFFFFF !important;}
    </style>
    """

# 5. Sidebar
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")
    st.divider()
    
    ds_che_do = ["🏠 Trang chủ", "📖 Học theo chuyên đề"]
    che_do = st.radio("⚙️ Chức năng:", ds_che_do, key="che_do_sidebar")
    
    mon = None
    if che_do == "📖 Học theo chuyên đề":
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")

# 6. Main Logic
st.markdown(css_giao_dien_chung(), unsafe_allow_html=True)

if che_do == "🏠 Trang chủ":
    st.markdown('<div class="hb"><div class="hb-than"><p class="hb-tieu-de">Chào mừng đến với Hệ thống học tập</p></div></div>', unsafe_allow_html=True)
    st.write("Chọn chức năng ở bên trái để bắt đầu học tập.")

elif che_do == "📖 Học theo chuyên đề" and mon:
    st.markdown(f"### Đang học: {mon}")
    lop_dict = DATABASE.get(mon, {})
    
    if lop_dict:
        # Sử dụng các khóa session_state ổn định để tránh lỗi mất dữ liệu khi rerender
        lop = st.selectbox("Khối:", list(lop_dict.keys()), key="s_lop")
        chuong_dict = lop_dict.get(lop, {})
        chuong = st.selectbox("Chương:", list(chuong_dict.keys()), key="s_chuong")
        bai_dict = chuong_dict.get(chuong, {})
        bai = st.selectbox("Bài học:", list(bai_dict.keys()), key="s_bai")
        
        st.markdown(f"### 📖 {bai}")
        noi_dung = bai_dict.get(bai, {})
        st.info(f"Lý thuyết: {noi_dung.get('ly_thuyet', 'Chưa có nội dung')}")
    else:
        st.warning("Dữ liệu môn này đang được cập nhật.")

else:
    st.write("Vui lòng chọn chức năng.")
