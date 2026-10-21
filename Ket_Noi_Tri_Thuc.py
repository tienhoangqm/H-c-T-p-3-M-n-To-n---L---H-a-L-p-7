# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản chuẩn hóa UI/UX & Vá lỗi toàn diện
"""
import streamlit as st
import google.generativeai as genai
import random
import re

# Mở "két sắt" lấy chìa khóa kết nối AI
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ==================== IMPORT DỮ LIỆU TỪ 3 FILE ====================
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

DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA,
}

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7 - Kết Nối Tri Thức",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS chuẩn hóa: Tương thích tốt cả chế độ Sáng/Tối và bảo vệ 100% Icon Streamlit
CSS = """
<style>
    .main .block-container { padding-top: 1.2rem; max-width: 95%; }
    
    /* Banner Header */
    .hero-banner {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white;
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .hero-title { font-size: 1.5rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
    .hero-sub { font-size: 0.95rem; opacity: 0.9; margin-top: 0.3rem; color: #E2E8F0 !important; }
    
    /* Khung Lý thuyết & Ví dụ */
    .khung-lythuyet {
        background-color: #EFF6FF;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 6px solid #2563EB;
        margin: 0.8rem 0;
        color: #1E293B !important;
        font-size: 1rem;
        line-height: 1.65;
        white-space: pre-wrap;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .khung-vidu {
        background-color: #FFFBEB;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 6px solid #F59E0B;
        margin: 0.8rem 0;
        color: #1E293B !important;
        font-size: 1rem;
        line-height: 1.65;
        white-space: pre-wrap;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Trạng thái Đúng / Sai */
    .dung { color: #059669; font-weight: 700; font-size: 1.05rem; }
    .sai { color: #DC2626; font-weight: 700; font-size: 1.05rem; }
    
    /* Khung Điểm Thi */
    .diem-thi {
        background-color: #FFF1F2;
        font-size: 1.6rem;
        color: #E11D48 !important;
        font-weight: 800;
        text-align: center;
        padding: 1.2rem;
        border: 2px dashed #F43F5E;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ==================== HÀM TIỆN ÍCH ====================
def lam_sach_id(s):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))

def sap_xep_chuong(ds_chuong):
    """Tự động sắp xếp Chương 1 -> Chương 10 theo đúng thứ tự số học"""
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)

def chuan_hoi(s):
    d = str(s).strip().lower().replace(',', '.').replace(';', '.')
    return re.sub(r'\s+', '', d)

def so_sanh(nd, ds_dung):
    x = chuan_hoi(nd)
    # Vá lỗi: Nếu học sinh để trống không nhập gì thì trả về False ngay
    if not x:
        return False
    for d in ds_dung:
        y = chuan_hoi(d)
        if not y:
            continue
        if x == y:
            return True
        # Chỉ cho phép khớp chuỗi con nếu người dùng nhập đủ dài (>= 2 ký tự)
        if len(x) >= 2 and (x in y or y in x):
            return True
        try:
            if abs(float(x) - float(y)) < 0.01:
                return True
        except (ValueError, TypeError):
            pass
    return False

def luu_tien_do(mon, lop, chuong, bai, dung, tong):
    if 'tien_do' not in st.session_state:
        st.session_state.tien_do = {}
    st.session_state.tien_do[f"{mon}|{lop}|{chuong}|{bai}"] = {"dung": dung, "tong": tong}

def hien_thi_tien_do():
    if 'tien_do' in st.session_state and st.session_state.tien_do:
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Tiến độ học tập")
        td = sum(v["dung"] for v in st.session_state.tien_do.values())
        tc = sum(v["tong"] for v in st.session_state.tien_do.values())
        so_bai = len(st.session_state.tien_do)
        if tc > 0:
            diem_tb = td / tc * 10
            st.sidebar.metric("Điểm trung bình", f"{diem_tb:.1f} / 10", f"Đã làm {so_bai} bài")
            st.sidebar.progress(min(td / tc, 1.0))

# ==================== HIỂN THỊ NỘI DUNG BÀI HỌC ====================
def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    st.markdown(f"### 📖 {ten_bai}")
    lt = data.get("ly_thuyet", "").strip()
    vd = data.get("vi_du", "").strip()
    ch_list = data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    # Thẻ thống kê nhanh đầu bài
    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Câu hỏi Trắc nghiệm", f"{len(ch_list)} câu")
    c2.metric("✏️ Bài tập Cơ bản", f"{len(bt_cb)} bài")
    c3.metric("🔥 Bài tập Nâng cao", f"{len(bt_nc)} bài")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📚 Lý thuyết & Ví dụ", 
        "✏️ Bài tập cơ bản", 
        "🔥 Bài tập nâng cao", 
        "📝 Trắc nghiệm bài học"
    ])

    with tab1:
        if lt:
            st.markdown("#### 📌 Lý thuyết trọng tâm")
            st.markdown(f"<div class='khung-lythuyet'>{lt}</div>", unsafe_allow_html=True)
        if vd:
            st.markdown("#### 💡 Ví dụ minh họa")
            st.markdown(f"<div class='khung-vidu'>{vd}</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("#### ✏️ Bài tập cơ bản — Tự luyện")
        if not bt_cb: 
            st.info("Chưa có bài tập cơ bản.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    ans = st.text_input("Nhập kết quả của bạn:", placeholder="Gõ đáp án vào đây...", key=f"cb_{sid}_{i}")
                    if st.button("Kiểm tra đáp án", key=f"btn_cb_{sid}_{i}"):
                        if not ans.strip():
                            st.warning("⚠️ Bạn vui lòng nhập đáp án trước khi bấm Kiểm tra nhé!")
                        elif so_sanh(ans, bt["dd"]):
                            st.markdown("<p class='dung'>✅ Chính xác! Tuyệt vời!</p>", unsafe_allow_html=True)
                            st.info(f"💡 Giải thích: {bt.get('gt') or bt.get('lg', '')}")
                        else:
                            st.markdown(f"<p class='sai'>❌ Chưa đúng. Đáp án chuẩn: {bt['dd'][0]}</p>", unsafe_allow_html=True)
                            st.info(f"💡 Giải thích: {bt.get('gt') or bt.get('lg', '')}")

    with tab3:
        st.markdown("#### 🔥 Bài tập nâng cao — Vận dụng & Phát triển tư duy")
        if not bt_nc: 
            st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                tieu_de_ngan = nc['de'][:85] + ("..." if len(nc['de']) > 85 else "")
                with st.expander(f"Bài nâng cao {i}: {tieu_de_ngan}"):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    if nc.get('hd'):
                        st.info(f"💡 **Hướng dẫn tư duy:** {nc['hd']}")
                    ans = st.text_input("Nhập kết quả của bạn:", placeholder="Gõ đáp án vào đây...", key=f"nc_{sid}_{i}")
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                            if not ans.strip():
                                st.warning("⚠️ Bạn hãy nhập đáp án trước khi kiểm tra nhé!")
                            elif so_sanh(ans, nc["dd"]): 
                                st.success("🎉 Chính xác! Tư duy rất sắc bén!")
                            else: 
                                st.error(f"❌ Chưa chính xác. Đáp án gợi ý: {nc['dd'][0]}")
                    with col_btn2:
                        if st.checkbox("📖 Xem lời giải chi tiết", key=f"lg_{sid}_{i}"):
                            st.success(f"**Lời giải:** {nc['lg']}")

    with tab4:
        st.markdown("#### 📝 Luyện tập trắc nghiệm")
        tong = len(ch_list)
        if tong == 0:
            st.info("Chưa có câu hỏi trắc nghiệm.")
            return
        options = [n for n in [10, 15, 20, 30, 50] if n <= tong]
        if tong not in options:
            options.append(tong)
        options = sorted(list(set(options)))
        
        col_sl, col_btn = st.columns([2, 1])
        with col_sl:
            so_cau = st.selectbox("📋 Chọn số lượng câu hỏi muốn làm:", options=options, key=f"sl_{sid}")
        with col_btn:
            st.write("")
            st.write("")
            tao_moi = st.button("🔄 Đổi bộ câu hỏi khác", key=f"new_{sid}", use_container_width=True)
            
        key_de = f"de_{sid}_{so_cau}"
        if tao_moi or key_de not in st.session_state:
            st.session_state[key_de] = random.sample(ch_list, min(so_cau, tong))
        de = st.session_state[key_de]

        with st.form(f"form_{sid}"):
            tl = {}
            for i, ch in enumerate(de, 1):
                noi_dung_cau = ch.get('nd') or ch.get('de', 'Câu hỏi')
                st.markdown(f"**Câu {i}:** {noi_dung_cau}")
                tl[i] = st.radio(f"Chọn đáp án câu {i}:", ch["da"], key=f"radio_{sid}_{so_cau}_{i}", index=None, label_visibility="collapsed")
                st.divider()
            if st.form_submit_button("🚀 Nộp bài & Chấm điểm", type="primary", use_container_width=True):
                chua_lam = [str(i) for i, v in tl.items() if v is None]
                if chua_lam: 
                    st.warning(f"⚠️ Bạn còn quên chưa chọn đáp án ở câu: {', '.join(chua_lam)}!")
                else:
                    dung = sum(1 for i, ch in enumerate(de, 1) if tl[i] == ch["da"][ch["d"]])
                    diem = dung / len(de) * 10
                    luu_tien_do(mon, lop, chuong, ten_bai, dung, len(de))
                    if diem >= 8.0:
                        st.balloons()
                    st.markdown(f"<div class='diem-thi'>🏆 KẾT QUẢ: {diem:.1f} / 10 ĐIỂM <br><span style='font-size:1.1rem;font-weight:normal;'>(Trả lời đúng {dung}/{len(de)} câu)</span></div>", unsafe_allow_html=True)
                    for i, ch in enumerate(de, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl[i] == da_dung: 
                            st.markdown(f"✅ **Câu {i}: Chính xác** — {da_dung}")
                        else: 
                            st.markdown(f"❌ **Câu {i}: Sai** — Bạn chọn: *{tl[i]}* · Đáp án đúng: **{da_dung}**")
                        st.info(f"💡 Giải thích: {ch['gt']}")

# ==================== HIỂN THỊ CHẾ ĐỘ THI THỬ ====================
def hien_thi_che_do_thi(mon, lop, chuong_dict):
    st.markdown("### ⏱️ PHÒNG THI THỬ & KIỂM TRA ĐỊNH KÌ")
    
    ds_chuong_sorted = sap_xep_chuong(list(chuong_dict.keys()))
    col1, col2 = st.columns([1, 2])
    with col1:
        loai_de = st.selectbox("📌 Chọn cấu trúc đề thi:", [
            "Kiểm tra 15 phút (10 câu)", 
            "Kiểm tra Giữa kì / 1 Tiết (20 câu)", 
            "Thi Học kì (40 câu)", 
            "Thử thách Học sinh giỏi (50 câu)"
        ])
        mapping_cau = {
            "Kiểm tra 15 phút (10 câu)": 10, 
            "Kiểm tra Giữa kì / 1 Tiết (20 câu)": 20, 
            "Thi Học kì (40 câu)": 40, 
            "Thử thách Học sinh giỏi (50 câu)": 50
        }
        so_cau_can_tao = mapping_cau[loai_de]
        
    with col2:
        chuong_chon = st.multiselect(
            "📚 Chọn các chương muốn kiểm tra:", 
            ds_chuong_sorted, 
            default=ds_chuong_sorted
        )

    if st.button("🚀 TẠO ĐỀ THI MỚI TỪ NGÂN HÀNG CÂU HỎI", type="primary", use_container_width=True):
        all_questions = []
        for c in chuong_chon:
            for b, data in chuong_dict[c].items():
                all_questions.extend(data.get("cau_hoi", []))
        
        if len(all_questions) == 0:
            st.error("❌ Vui lòng chọn ít nhất 1 chương có câu hỏi!")
        else:
            so_cau_thuc = min(so_cau_can_tao, len(all_questions))
            st.session_state[f"dethi_{mon}_{lop}"] = random.sample(all_questions, so_cau_thuc)
            st.session_state[f"ten_dethi_{mon}_{lop}"] = loai_de

    key_thi = f"dethi_{mon}_{lop}"
    if key_thi in st.session_state:
        de_thi = st.session_state[key_thi]
        ten_de = st.session_state.get(f"ten_dethi_{mon}_{lop}", loai_de)
        st.markdown("---")
        st.markdown(f"#### 📜 ĐỀ CHÍNH THỨC: {ten_de.upper()} — ({len(de_thi)} Câu)")
        
        with st.form(f"form_thi_tong_hop_{mon}_{lop}"):
            tl_thi = {}
            for i, ch in enumerate(de_thi, 1):
                noi_dung_cau = ch.get('nd') or ch.get('de', 'Câu hỏi')
                st.markdown(f"**Câu {i}:** {noi_dung_cau}")
                tl_thi[i] = st.radio(f"Đáp án câu {i}:", ch["da"], key=f"thi_radio_{mon}_{lop}_{i}", index=None, label_visibility="collapsed")
                st.divider()
                
            if st.form_submit_button("🎯 NỘP BÀI & CHẤM ĐIỂM", type="primary", use_container_width=True):
                chua_lam = [str(i) for i, v in tl_thi.items() if v is None]
                if chua_lam:
                    st.warning(f"⚠️ Bạn chưa chọn đáp án cho các câu: {', '.join(chua_lam)}. Hãy hoàn thành hết trước khi nộp bài!")
                else:
                    dung = sum(1 for i, ch in enumerate(de_thi, 1) if tl_thi[i] == ch["da"][ch["d"]])
                    diem = dung / len(de_thi) * 10
                    if diem >= 8.0: 
                        st.balloons()
                    st.markdown(f"<div class='diem-thi'>🏆 ĐIỂM BÀI THI: {diem:.1f} / 10 ĐIỂM <br><span style='font-size:1.1rem;font-weight:normal;'>(Đúng {dung}/{len(de_thi)} câu)</span></div>", unsafe_allow_html=True)
                    
                    with st.expander("🔍 XEM ĐÁP ÁN VÀ LỜI GIẢI CHI TIẾT", expanded=True):
                        for i, ch in enumerate(de_thi, 1):
                            da_dung = ch["da"][ch["d"]]
                            if tl_thi[i] == da_dung:
                                st.markdown(f"✅ **Câu {i}: Đúng** — {da_dung}")
                            else:
                                st.markdown(f"❌ **Câu {i}: Sai** — Bạn chọn: *{tl_thi[i]}* · Đáp án đúng: **{da_dung}**")
                            st.info(f"💡 Giải thích: {ch['gt']}")

# ==================== GIAO DIỆN CHÍNH ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    st.caption("Hệ thống Ôn luyện & Kiểm tra THCS")
    st.divider()
    che_do = st.radio("⚙️ Chế độ học tập:", ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"])
    st.divider()
    mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    hien_thi_tien_do()

# Banner đầu trang
st.markdown(f"""
<div class="hero-banner">
    <p class="hero-title">{mon} — Chương trình GDPT 2018 (Kết Nối Tri Thức)</p>
    <p class="hero-sub">Hệ thống lý thuyết trọng tâm, bài tập phân hóa cơ bản - nâng cao và ngân hàng đề thi trắc nghiệm</p>
</div>
""", unsafe_allow_html=True)

lop_dict = DATABASE[mon]
if not lop_dict:
    st.warning("Đang cập nhật dữ liệu cho môn học này...")
else:
    ds_lop = list(lop_dict.keys())
    # Mặc định ưu tiên chọn Lớp 7 nếu có nhiều lớp
    idx_lop = ds_lop.index("Lớp 7") if "Lớp 7" in ds_lop else 0
    
    if che_do == "📖 Học theo chuyên đề":
        col_l, col_c, col_b = st.columns([1, 2, 2])
        with col_l:
            lop = st.selectbox("🏫 Khối lớp:", ds_lop, index=idx_lop, key="lop_main")
        chuong_dict = lop_dict[lop]
        
        if not chuong_dict:
            st.warning("Chưa có dữ liệu chương.")
        else:
            ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
            with col_c:
                chuong = st.selectbox("📂 Chọn Chương:", ds_chuong, key="chuong_main")
            bai_dict = chuong_dict[chuong]
            
            if not bai_dict:
                st.warning("Chưa có dữ liệu bài học.")
            else:
                with col_b:
                    bai = st.selectbox("📘 Chọn Chuyên đề:", list(bai_dict.keys()), key="bai_main")
                st.markdown("---")
                hien_thi_bai(mon, lop, chuong, bai, bai_dict[bai])
    else:
        lop = st.selectbox("🏫 Chọn khối lớp dự thi:", ds_lop, index=idx_lop, key="lop_thi")
        chuong_dict = lop_dict[lop]
        if chuong_dict:
            hien_thi_che_do_thi(mon, lop, chuong_dict)
            # ==========================================
# ==========================================
# KHU VỰC GIA SƯ AI (ĐẶT Ở CUỐI FILE CÙNG)
# ==========================================
st.divider()
st.header("💬 Trợ lý AI 24/7 - Hỏi đáp cùng Gia sư")

# 1. Cài đặt tính cách cho Gia sư AI
SYSTEM_PROMPT = """
Bạn là một gia sư AI trẻ trung, năng động, hài hước (Gen Z) dạy môn Toán, Lý, Hóa lớp 7 (sách Kết Nối Tri Thức).
Nguyên tắc:
1. Tuyệt đối KHÔNG BAO GIỜ giải bài hộ hoặc đưa ra đáp án cuối cùng ngay lập tức.
2. Sử dụng phương pháp gợi mở từng bước để học sinh tự tính toán.
3. Xưng hô: "Anh/Chị" và "Em", dùng nhiều icon thân thiện.
4. Trình bày công thức Toán/Hóa rõ ràng.
"""

# Khởi tạo bộ não AI (Đã kiểm tra kỹ cú pháp và dấu ngoặc)
model = genai.GenerativeModel(
    model_name="gemini-3.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# 2. Tạo bộ nhớ để AI nhớ các câu chat trước đó
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Hiển thị lại lịch sử chat trên màn hình
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Khung cho học sinh nhập câu hỏi
if prompt := st.chat_input("Em đang mắc kẹt ở bài nào, gõ vào đây anh/chị gợi ý cho nhé..."):
    # Hiển thị câu hỏi của học sinh
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Gọi AI trả lời
    with st.chat_message("assistant"):
        # Gom các câu chuyện cũ để AI hiểu ngữ cảnh
        gemini_history = [
            {"role": "user" if msg["role"] == "user" else "model", "parts": [msg["content"]]}
            for msg in st.session_state.chat_history[:-1]
        ]
        
        # Gửi câu hỏi và nhận câu trả lời
        chat_session = model.start_chat(history=gemini_history)
        response = chat_session.send_message(prompt)
        
        # In câu trả lời ra màn hình web
        st.markdown(response.text)
        
    # Lưu câu trả lời của AI vào lịch sử
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
    # ==========================================
# KHU VỰC GIA SƯ AI (ĐẶT Ở CUỐI FILE CÙNG)
# ==========================================
from streamlit_mic_recorder import speech_to_text # Thêm bộ thu âm

st.divider()
st.header("💬 Trợ lý AI 24/7 - Hỏi đáp cùng Gia sư")

# 1. Cài đặt tính cách cho Gia sư AI
SYSTEM_PROMPT = """
Bạn là một gia sư AI trẻ trung, năng động, hài hước (Gen Z) dạy môn Toán, Lý, Hóa lớp 7 (sách Kết Nối Tri Thức).
Nguyên tắc:
1. Tuyệt đối KHÔNG BAO GIỜ giải bài hộ hoặc đưa ra đáp án cuối cùng ngay lập tức.
2. Sử dụng phương pháp gợi mở từng bước để học sinh tự tính toán.
3. Xưng hô: "Anh/Chị" và "Em", dùng nhiều icon thân thiện.
4. Trình bày công thức Toán/Hóa rõ ràng.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    system_instruction=SYSTEM_PROMPT
)

# 2. Tạo bộ nhớ để AI nhớ các câu chat trước đó
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Khung cho học sinh nhập câu hỏi (Tích hợp Voice)
st.markdown("🎙️ **Lười gõ phím? Bấm vào nút bên dưới để đọc câu hỏi nhé:**")

# Hiển thị nút Micro thu âm
text_from_mic = speech_to_text(
    language='vi-VN',
    start_prompt="🔴 Bấm vào đây để NÓI",
    stop_prompt="⏹️ Bấm vào đây để DỪNG",
    just_once=True,
    key='STT'
)

# Ô gõ chữ truyền thống
prompt_from_keyboard = st.chat_input("Hoặc gõ câu hỏi vào đây...")

# Nhận lệnh từ Micro hoặc từ Bàn phím
prompt = text_from_mic or prompt_from_keyboard

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        gemini_history = [
            {"role": "user" if msg["role"] == "user" else "model", "parts": [msg["content"]]}
            for msg in st.session_state.chat_history[:-1]
        ]
        chat_session = model.start_chat(history=gemini_history)
        response = chat_session.send_message(prompt)
        st.markdown(response.text)
        
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
