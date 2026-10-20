# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
"""
import streamlit as st
import random
import re

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
    "🔬 Môn Vật lý": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA,
}

# ==================== CẤU HÌNH ====================
st.set_page_config(page_title="Kết Nối Tri Thức", page_icon="📚", layout="wide")

CSS = """
<style>
    .main .block-container { padding-top: 1.5rem; max-width: 96%; }
    .tieu-de-mon { font-size: 1.5rem; font-weight: 700; color: #1E40AF; margin-bottom: 0.5rem; text-transform: uppercase; }
    .khung-lythuyet { background-color:#EFF6FF; padding:1.1rem; border-radius:0.5rem; border-left:5px solid #1E40AF; margin:0.8rem 0; color:#1F2937; font-size:0.98rem; line-height:1.6; white-space:pre-wrap; }
    .khung-vidu { background-color:#FFFBEB; padding:1.1rem; border-radius:0.5rem; border-left:5px solid #F59E0B; margin:0.8rem 0; color:#1F2937; font-size:0.98rem; line-height:1.6; white-space:pre-wrap; }
    .dung { color:#10B981; font-weight:600; }
    .sai { color:#EF4444; font-weight:600; }
    .diem-thi { font-size: 2rem; color: #E11D48; font-weight: bold; text-align: center; padding: 1rem; border: 2px dashed #E11D48; border-radius: 10px; margin-bottom: 1rem;}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ==================== HÀM TIỆN ÍCH ====================
def lam_sach_id(s):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))

def chuan_hoi(s):
    d = str(s).strip().lower().replace(',', '.').replace(';', '.')
    return re.sub(r'\s+', '', d)

def so_sanh(nd, ds_dung):
    x = chuan_hoi(nd)
    for d in ds_dung:
        y = chuan_hoi(d)
        if x == y or x in y or y in x:
            return True
        try:
            if abs(float(x) - float(y)) < 0.01:
                return True
        except (ValueError, TypeError): pass
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
        if tc > 0:
            st.sidebar.markdown(f"**Điểm TB:** {td/tc*10:.1f}/10")
            st.sidebar.progress(td/tc)

# ==================== HIỂN THỊ NỘI DUNG BÀI HỌC ====================
def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    st.markdown(f"### 📖 Bài: {ten_bai}")
    lt = data.get("ly_thuyet", "").strip()
    vd = data.get("vi_du", "").strip()
    ch_list = data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    tab1, tab2, tab3, tab4 = st.tabs(["📚 Lý thuyết & Ví dụ", "✏️ Bài tập cơ bản", "🔥 Bài tập nâng cao", "📝 Trắc nghiệm bài học"])

    with tab1:
        if lt:
            st.markdown("#### 📌 Lý thuyết trọng tâm")
            st.markdown(f"<div class='khung-lythuyet'>{lt}</div>", unsafe_allow_html=True)
        if vd:
            st.markdown("#### 💡 Ví dụ minh họa")
            st.markdown(f"<div class='khung-vidu'>{vd}</div>", unsafe_allow_html=True)
        st.info(f"📊 Cấu trúc: {len(ch_list)} câu trắc nghiệm · {len(bt_cb)} bài cơ bản · {len(bt_nc)} bài nâng cao")

    with tab2:
        st.markdown("#### ✏️ Bài tập cơ bản — Tự luyện")
        if not bt_cb: 
            st.info("Chưa có bài tập cơ bản.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    ans = st.text_input("Nhập đáp án:", key=f"cb_{sid}_{i}")
                    if st.button("Kiểm tra", key=f"btn_cb_{sid}_{i}"):
                        if so_sanh(ans, bt["dd"]):
                            st.markdown("<p class='dung'>✅ Chính xác! Tuyệt vời!</p>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<p class='sai'>❌ Chưa đúng. Đáp án gợi ý: {bt['dd'][0]}</p>", unsafe_allow_html=True)
                        st.info(f"💡 Giải thích: {bt['gt']}")

    with tab3:
        st.markdown("#### 🔥 Bài tập nâng cao — Vận dụng")
        if not bt_nc: 
            st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                with st.expander(f"Nâng cao {i}: {nc['de'][:70]}..."):
                    st.markdown(f"**Đề:** {nc['de']}")
                    st.info(f"💡 Gợi ý: {nc['hd']}")
                    ans = st.text_input("Nhập đáp án:", key=f"nc_{sid}_{i}")
                    c1, c2 = st.columns(2)
                    with c1:
                        if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                            if so_sanh(ans, nc["dd"]): 
                                st.success("🎉 Chính xác! Giỏi lắm!")
                            else: 
                                st.error("❌ Chưa đúng. Xem lời giải bên cạnh.")
                    with c2:
                        if st.checkbox("Xem lời giải", key=f"lg_{sid}_{i}"):
                            st.success(f"**Lời giải:** {nc['lg']}")

    with tab4:
        st.markdown("#### 📝 Luyện tập trắc nghiệm bài học")
        tong = len(ch_list)
        if tong == 0:
            st.info("Chưa có câu hỏi trắc nghiệm.")
            return
        options = [n for n in [5, 10, 15, 20, 30, 50] if n <= tong] or [tong]
        so_cau = st.selectbox("📋 Số câu hỏi:", options=options, key=f"sl_{sid}")
        key_de = f"de_{sid}"
        if st.button("🔄 Tạo đề luyện tập mới", key=f"new_{sid}") or key_de not in st.session_state:
            st.session_state[key_de] = random.sample(ch_list, min(so_cau, tong))
        de = st.session_state[key_de]

        with st.form(f"form_{sid}"):
            tl = {}
            for i, ch in enumerate(de, 1):
                st.markdown(f"**Câu {i}:** {ch['nd']}")
                tl[i] = st.radio(f"Đáp án câu {i}:", ch["da"], key=f"radio_{sid}_{i}", index=None)
                st.divider()
            if st.form_submit_button("🚀 Nộp bài & Chấm điểm"):
                if None in tl.values(): 
                    st.warning("⚠️ Bạn chưa chọn đủ đáp án!")
                else:
                    dung = sum(1 for i, ch in enumerate(de, 1) if tl[i] == ch["da"][ch["d"]])
                    diem = dung / len(de) * 10
                    luu_tien_do(mon, lop, chuong, ten_bai, dung, len(de))
                    st.balloons()
                    st.markdown(f"<div class='diem-thi'>🏆 Điểm: {diem:.1f}/10 (Đúng {dung}/{len(de)})</div>", unsafe_allow_html=True)
                    for i, ch in enumerate(de, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl[i] == da_dung: 
                            st.markdown(f"✅ **Câu {i}: Đúng** — {da_dung}")
                        else: 
                            st.markdown(f"❌ **Câu {i}: Sai** — Chọn: {tl[i]} · Đáp án: **{da_dung}**")
                        st.info(f"Giải thích: {ch['gt']}")

# ==================== HIỂN THỊ CHẾ ĐỘ THI THỬ ====================
def hien_thi_che_do_thi(mon, lop, chuong_dict):
    st.markdown(f"### ⏱️ TẠO ĐỀ KIỂM TRA / THI HỌC KÌ")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        loai_de = st.selectbox("📌 Dạng đề kiểm tra:", 
                               ["Kiểm tra 15 phút (10 câu)", "Kiểm tra 1 tiết (20 câu)", "Thi Học kì (40 câu)", "Thử thách (50 câu)"])
        mapping_cau = {"Kiểm tra 15 phút (10 câu)": 10, "Kiểm tra 1 tiết (20 câu)": 20, "Thi Học kì (40 câu)": 40, "Thử thách (50 câu)": 50}
        so_cau_can_tao = mapping_cau[loai_de]
        
    with col2:
        chuong_chon = st.multiselect("📚 Phạm vi kiến thức (Chọn 1 hoặc nhiều chương):", 
                                     list(chuong_dict.keys()), default=list(chuong_dict.keys()))

    if st.button("🚀 BỐC ĐỀ THI NGẪU NHIÊN TỪ NGÂN HÀNG", type="primary", use_container_width=True):
        all_questions = []
        for c in chuong_chon:
            for b, data in chuong_dict[c].items():
                all_questions.extend(data.get("cau_hoi", []))
        
        if len(all_questions) == 0:
            st.error("❌ Không có câu hỏi nào trong các chương đã chọn!")
        else:
            so_cau_thuc = min(so_cau_can_tao, len(all_questions))
            if so_cau_thuc < so_cau_can_tao:
                st.warning(f"⚠️ Ngân hàng dữ liệu hiện tại chỉ có {len(all_questions)} câu trong phạm vi này. Đang tạo đề với toàn bộ số câu hiện có.")
            
            st.session_state[f"dethi_{mon}_{lop}"] = random.sample(all_questions, so_cau_thuc)

    key_thi = f"dethi_{mon}_{lop}"
    if key_thi in st.session_state:
        de_thi = st.session_state[key_thi]
        st.markdown("---")
        st.markdown(f"#### 📜 ĐỀ THI ĐANG MỞ: {loai_de.upper()} ({len(de_thi)} Câu)")
        
        with st.form(f"form_thi_tong_hop_{mon}_{lop}"):
            tl_thi = {}
            for i, ch in enumerate(de_thi, 1):
                st.markdown(f"**Câu {i}:** {ch['nd']}")
                tl_thi[i] = st.radio(f"Đáp án câu {i}:", ch["da"], key=f"thi_radio_{mon}_{lop}_{i}", index=None)
                st.divider()
                
            if st.form_submit_button("NỘP BÀI & XEM ĐIỂM SỐ", use_container_width=True):
                if None in tl_thi.values():
                    st.warning("⚠️ Bạn chưa làm hết các câu hỏi! Hãy kiểm tra lại.")
                else:
                    dung = sum(1 for i, ch in enumerate(de_thi, 1) if tl_thi[i] == ch["da"][ch["d"]])
                    diem = dung / len(de_thi) * 10
                    if diem >= 8: st.balloons()
                    st.markdown(f"<div class='diem-thi'>🏆 ĐIỂM SỐ CỦA BẠN: {diem:.1f} / 10 <br> (Đúng {dung}/{len(de_thi)} câu)</div>", unsafe_allow_html=True)
                    
                    with st.expander("🔍 XEM ĐÁP ÁN CHI TIẾT"):
                        for i, ch in enumerate(de_thi, 1):
                            da_dung = ch["da"][ch["d"]]
                            if tl_thi[i] == da_dung:
                                st.markdown(f"✅ **Câu {i}: Đúng** — {da_dung}")
                            else:
                                st.markdown(f"❌ **Câu {i}: Sai** — Chọn: {tl_thi[i]} · Đáp án đúng: **{da_dung}**")
                            st.info(f"Giải thích: {ch['gt']}")

# ==================== GIAO DIỆN CHÍNH ====================
with st.sidebar:
    st.markdown("### 📚 KẾT NỐI TRI THỨC")
    st.divider()
    che_do = st.radio("⚙️ Chọn chế độ:", ["📖 Học theo từng bài", "📝 Thi thử / Kiểm tra"])
    st.divider()
    mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    st.divider()
    hien_thi_tien_do()

st.markdown(f"<h2 class='tieu-de-mon'>{mon}</h2>", unsafe_allow_html=True)

lop_dict = DATABASE[mon]
if not lop_dict:
    st.warning("Đang cập nhật dữ liệu cho môn học này...")
else:
    lop = st.selectbox("Chọn khối lớp:", list(lop_dict.keys()), key="lop_main")
    chuong_dict = lop_dict[lop]
    
    if not chuong_dict:
        st.warning("Chưa có dữ liệu chương.")
    else:
        st.markdown("---")
        if che_do == "📖 Học theo từng bài":
            chuong = st.selectbox("Chọn chương:", list(chuong_dict.keys()), key="chuong_main")
            bai_dict = chuong_dict[chuong]
            
            if not bai_dict:
                st.warning("Chưa có dữ liệu bài học.")
            else:
                bai = st.selectbox("Chọn bài học:", list(bai_dict.keys()), key="bai_main")
                hien_thi_bai(mon, lop, chuong, bai, bai_dict[bai])
        else:
            hien_thi_che_do_thi(mon, lop, chuong_dict)