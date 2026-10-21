# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Toàn diện: Bài Học + Thí Nghiệm Ảo + Gia Sư AI + Trạm Nạp Dữ Liệu (Auto-Parser)
"""
import streamlit as st
import google.generativeai as genai
import io
import random
import re

# Import an toàn các thư viện bổ trợ Đa Giác Quan
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

# ==================== DANH MỤC MÔ PHỎNG THÍ NGHIỆM PHET (CHUẨN .EDU) ====================
DANH_MUC_THI_NGHIEM = {
    "📐 Môn Toán": {
        "⚖️ Cân bằng phương trình & Biểu thức đại số": "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_vi.html",
        "📈 Vẽ đồ thị đường thẳng & Tỉ lệ thuận": "https://phet.colorado.edu/sims/html/graphing-lines/latest/graphing-lines_vi.html",
        "🍕 Khám phá Phân số & Số hữu tỉ Q": "https://phet.colorado.edu/sims/html/fractions-intro/latest/fractions-intro_vi.html",
        "📐 Xây dựng Diện tích & Chu vi hình học": "https://phet.colorado.edu/sims/html/area-builder/latest/area-builder_vi.html",
    },
    "🔬 Môn Vật lý (KHTN)": {
        "💡 Khúc xạ & Phản xạ ánh sáng (Quang học 7)": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_vi.html",
        "🔊 Sóng âm, Biên độ & Tần số âm thanh": "https://phet.colorado.edu/sims/html/waves-intro/latest/waves-intro_vi.html",
        "⚡ Lắp ráp Mạch điện một chiều (Đèn, Pin, Công tắc)": "https://phet.colorado.edu/sims/html/circuit-construction-kit-dc/latest/circuit-construction-kit-dc_vi.html",
        "🚀 Lực, Chuyển động & Tốc độ": "https://phet.colorado.edu/sims/html/forces-and-motion-basics/latest/forces-and-motion-basics_vi.html",
    },
    "🧪 Môn Hóa học (KHTN)": {
        "⚛️ Xây dựng cấu tạo Nguyên tử (Proton, Neutron, Electron)": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_vi.html",
        "🧬 Lắp ghép Phân tử Hóa học (H2O, CO2, O2...)": "https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_vi.html",
        "⚖️ Cân bằng Phương trình Hóa học": "https://phet.colorado.edu/sims/html/balancing-chemical-equations/latest/balancing-chemical-equations_vi.html",
        "🧪 Pha chế & Đo nồng độ dung dịch": "https://phet.colorado.edu/sims/html/concentration/latest/concentration_vi.html",
    }
}

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7 - Kết Nối Tri Thức",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS chuẩn hóa: Ẩn nút Cây bút chì (Edit) & GitHub nhưng BẢO VỆ 100% nút mở Sidebar
CSS = """
<style>
    .main .block-container { padding-top: 1.2rem; max-width: 95%; }
    
    /* Ẩn chính xác biểu tượng Cây bút chì (Edit), GitHub, Menu phụ và Footer mà không làm mất nút mở Sidebar */
    [data-testid="stToolbarActions"] { display: none !important; }
    [data-testid="stHeaderActionElements"] { display: none !important; }
    .stAppDeployButton { display: none !important; }
    #MainMenu { visibility: hidden !important; }
    footer { visibility: hidden !important; }
    .viewerBadge_container__1QSob { display: none !important; }
    
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
        if x == y: return True
        if len(x) >= 2 and (x in y or y in x): return True
        try:
            if abs(float(x) - float(y)) < 0.01: return True
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
        so_bai = len(st.session_state.tien_do)
        if tc > 0:
            diem_tb = td / tc * 10
            st.sidebar.metric("Điểm trung bình", f"{diem_tb:.1f} / 10", f"Đã làm {so_bai} bài")
            st.sidebar.progress(min(td / tc, 1.0))

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\mathbb{Q}', 'Q').replace(r'\mathbb{Z}', 'Z').replace(r'\mathbb{N}', 'N').replace(r'\mathbb{R}', 'R')
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ').replace(r'\div', ' chia ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    s = re.sub(
        r'[^\w\s,.?!:;()+\-*/=<>%àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]',
        '', s)
    return re.sub(r'\s+', ' ', s).strip()

# ==================== HÀM HIỂN THỊ PHÒNG THÍ NGHIỆM ====================
def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    st.markdown("#### 🎪 Phòng Thí Nghiệm & Mô Phỏng Tương Tác (PhET Colorado)")
    ds_tn_mon = DANH_MUC_THI_NGHIEM.get(mon_hien_tai, {})
    if not ds_tn_mon: ds_tn_mon = DANH_MUC_THI_NGHIEM["🔬 Môn Vật lý (KHTN)"]
    ten_tn = st.selectbox(
        f"🔬 Chọn mô phỏng thực hành cho {mon_hien_tai}:",
        list(ds_tn_mon.keys()),
        key=f"select_tn_{key_prefix}_{lam_sach_id(mon_hien_tai)}"
    )
    st.components.v1.iframe(ds_tn_mon[ten_tn], height=580, scrolling=True)
    st.info("💡 **Mẹo thực hành:** Dùng chuột kéo thả trực tiếp trên màn hình, sau đó kéo xuống hỏi Gia sư AI để hiểu rõ bản chất nhé!")

# ==================== HÀM AUTO-PARSER (TRẠM NẠP DỮ LIỆU) ====================
def hien_thi_tram_nap_du_lieu():
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">⚙️ Trạm Nạp Dữ Liệu Tự Động (Auto-Parser)</p>
        <p class="hero-sub">Dành cho Admin: Biến văn bản thô, đề bài lộn xộn thành cấu trúc Code Python siêu tốc chuẩn 100%.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📝 1. Dán nội dung thô vào đây")
    raw_text = st.text_area("Copy bài giảng, danh sách câu hỏi trắc nghiệm, bài tập từ Word, PDF hoặc web dán vào đây:", height=250)
    
    PROMPT_PARSER = """
    Bạn là một kỹ sư dữ liệu xuất sắc. Hãy đọc đoạn văn bản thô do người dùng cung cấp và chuyển đổi CẤU TRÚC TOÀN BỘ NỘI DUNG ĐÓ thành một Dictionary Python duy nhất theo đúng chuẩn của hệ thống sau:

    ```python
    {
        "ly_thuyet": "Nội dung lý thuyết trọng tâm (định dạng Markdown, công thức dùng $latex$).",
        "vi_du": "Các ví dụ minh họa có trong văn bản (nếu có).",
        "cau_hoi": [
            {"de": "Câu hỏi trắc nghiệm 1?", "da": ["Đáp án A", "Đáp án B", "Đáp án C", "Đáp án D"], "d": 0, "gt": "Giải thích tại sao lại chọn đáp án A"},
            {"de": "Câu hỏi trắc nghiệm 2?", "da": ["A", "B", "C", "D"], "d": 2, "gt": "Giải thích chi tiết"}
        ],
        "bt_co_ban": [
            {"de": "Đề bài tự luận cơ bản 1", "dd": ["15", "15 cm", "x=15"], "lg": "Lời giải chi tiết"}
        ],
        "bt_nang_cao": [
            {"de": "Đề bài tự luận khó/nâng cao", "hd": "Gợi ý cách tư duy", "dd": ["kết quả"], "lg": "Lời giải chi tiết"}
        ]
    }
    ```
    Yêu cầu TỐI THƯỢNG:
    1. Chỉ in ra đúng cấu trúc Dictionary Python, KHÔNG in ra dòng chữ giải thích nào khác ở đầu hay cuối.
    2. Chú ý ngoặc kép `"`, dấu phẩy `,` phải chuẩn xác định dạng JSON/Dict.
    3. Ở phần `"cau_hoi"`, thuộc tính `"d"` là vị trí index của đáp án đúng (0 là A, 1 là B, 2 là C, 3 là D). AI tự nhận diện và tìm đáp án đúng.
    4. Tự sinh ra lời giải thích / hướng dẫn giải chi tiết cho các câu bài tập nếu văn bản gốc không có.
    """
    
    st.markdown("### 🚀 2. Xử lý & Tạo Code")
    if st.button("Trích xuất thành Code Python", type="primary", use_container_width=True):
        if not raw_text.strip():
            st.warning("⚠️ Vui lòng dán văn bản thô vào ô phía trên trước!")
        else:
            with st.spinner("🤖 AI đang đọc hiểu, bóc tách câu hỏi và viết cấu trúc code... (Mất khoảng 5-10 giây)"):
                try:
                    parser_model = genai.GenerativeModel("gemini-3.5-flash", system_instruction=PROMPT_PARSER)
                    ket_qua = parser_model.generate_content(raw_text).text
                    
                    # Cắt bỏ các ký hiệu markdown code block nếu có
                    clean_code = ket_qua.replace("```python", "").replace("```", "").strip()
                    
                    st.success("✅ Thành công! Dữ liệu đã được bóc tách và định dạng chuẩn Python.")
                    st.markdown("**Bấm vào biểu tượng Copy ở góc trên bên phải khung xám dưới đây để sao chép:**")
                    st.code(clean_code, language="python")
                    
                    st.info("💡 **Hướng dẫn dán:** Anh Tiến mở file `data_toan.py` (hoặc lý, hóa) trên GitHub, tìm đến đúng Bài Học tương ứng, xóa ngoặc nhọn `{...}` cũ của bài đó và **Paste** đoạn code mới này vào!")
                except Exception as e:
                    st.error(f"❌ Có lỗi xảy ra trong quá trình xử lý: {e}")

# ==================== HIỂN THỊ NỘI DUNG BÀI HỌC ====================
def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    st.markdown(f"### 📖 {ten_bai}")
    lt = data.get("ly_thuyet", "").strip()
    vd = data.get("vi_du", "").strip()
    ch_list = data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Câu hỏi Trắc nghiệm", f"{len(ch_list)} câu")
    c2.metric("✏️ Bài tập Cơ bản", f"{len(bt_cb)} bài")
    c3.metric("🔥 Bài tập Nâng cao", f"{len(bt_nc)} bài")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📚 Lý thuyết & Ví dụ", 
        "✏️ Bài tập cơ bản", 
        "🔥 Bài tập nâng cao", 
        "📝 Trắc nghiệm bài học",
        "🎪 Thí nghiệm & Mô phỏng"
    ])

    with tab1:
        if lt: st.markdown(f"#### 📌 Lý thuyết trọng tâm\n<div class='khung-lythuyet'>{lt}</div>", unsafe_allow_html=True)
        if vd: st.markdown(f"#### 💡 Ví dụ minh họa\n<div class='khung-vidu'>{vd}</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("#### ✏️ Bài tập cơ bản — Tự luyện")
        if not bt_cb: st.info("Chưa có bài tập cơ bản.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    ans = st.text_input("Nhập kết quả của bạn:", key=f"cb_{sid}_{i}")
                    if st.button("Kiểm tra đáp án", key=f"btn_cb_{sid}_{i}"):
                        if not ans.strip(): st.warning("⚠️ Vui lòng nhập đáp án!")
                        elif so_sanh(ans, bt["dd"]):
                            st.markdown("<p class='dung'>✅ Chính xác!</p>", unsafe_allow_html=True)
                            st.info(f"💡 Giải thích: {bt.get('gt') or bt.get('lg', '')}")
                        else:
                            st.markdown(f"<p class='sai'>❌ Chưa đúng. Đáp án: {bt['dd'][0]}</p>", unsafe_allow_html=True)
                            st.info(f"💡 Giải thích: {bt.get('gt') or bt.get('lg', '')}")

    with tab3:
        st.markdown("#### 🔥 Bài tập nâng cao — Vận dụng & Phát triển tư duy")
        if not bt_nc: st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                tieu_de = nc['de'][:85] + ("..." if len(nc['de']) > 85 else "")
                with st.expander(f"Bài nâng cao {i}: {tieu_de}"):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    if nc.get('hd'): st.info(f"💡 **Hướng dẫn:** {nc['hd']}")
                    ans = st.text_input("Nhập kết quả:", key=f"nc_{sid}_{i}")
                    c_btn1, c_btn2 = st.columns(2)
                    with c_btn1:
                        if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                            if not ans.strip(): st.warning("⚠️ Vui lòng nhập đáp án!")
                            elif so_sanh(ans, nc["dd"]): st.success("🎉 Chính xác!")
                            else: st.error(f"❌ Chưa đúng. Gợi ý: {nc['dd'][0]}")
                    with c_btn2:
                        if st.checkbox("📖 Xem lời giải", key=f"lg_{sid}_{i}"):
                            st.success(f"**Lời giải:** {nc['lg']}")

    with tab4:
        st.markdown("#### 📝 Luyện tập trắc nghiệm")
        tong = len(ch_list)
        if tong == 0: st.info("Chưa có câu hỏi trắc nghiệm.")
        else:
            options = sorted(list(set([n for n in [10, 15, 20, 30, 50] if n <= tong] + [tong])))
            col_sl, col_btn = st.columns([2, 1])
            with col_sl: so_cau = st.selectbox("📋 Chọn số lượng câu:", options, key=f"sl_{sid}")
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
                    st.markdown(f"**Câu {i}:** {ch.get('nd') or ch.get('de')}")
                    tl[i] = st.radio(f"Câu {i}:", ch["da"], key=f"radio_{sid}_{so_cau}_{i}", index=None, label_visibility="collapsed")
                    st.divider()
                if st.form_submit_button("🚀 Nộp bài & Chấm điểm", type="primary", use_container_width=True):
                    chua_lam = [str(i) for i, v in tl.items() if v is None]
                    if chua_lam: st.warning(f"⚠️ Quên chọn đáp án câu: {', '.join(chua_lam)}!")
                    else:
                        dung = sum(1 for i, ch in enumerate(de, 1) if tl[i] == ch["da"][ch["d"]])
                        diem = dung / len(de) * 10
                        luu_tien_do(mon, lop, chuong, ten_bai, dung, len(de))
                        if diem >= 8.0: st.balloons()
                        st.markdown(f"<div class='diem-thi'>🏆 ĐIỂM: {diem:.1f} / 10 <br><span style='font-size:1rem;font-weight:normal;'>(Đúng {dung}/{len(de)} câu)</span></div>", unsafe_allow_html=True)
                        for i, ch in enumerate(de, 1):
                            da_dung = ch["da"][ch["d"]]
                            if tl[i] == da_dung: st.markdown(f"✅ **Câu {i}: Đúng** — {da_dung}")
                            else: st.markdown(f"❌ **Câu {i}: Sai** — Bạn chọn: *{tl[i]}* · Đáp án: **{da_dung}**")
                            st.info(f"💡 Giải thích: {ch['gt']}")

    with tab5:
        hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

# ==================== HIỂN THỊ CHẾ ĐỘ THI THỬ ====================
def hien_thi_che_do_thi(mon, lop, chuong_dict):
    st.markdown("### ⏱️ PHÒNG THI THỬ & KIỂM TRA ĐỊNH KÌ")
    ds_chuong_sorted = sap_xep_chuong(list(chuong_dict.keys()))
    col1, col2 = st.columns([1, 2])
    with col1:
        loai_de = st.selectbox("📌 Cấu trúc đề:", ["Kiểm tra 15 phút (10 câu)", "Giữa kì (20 câu)", "Học kì (40 câu)", "HSG (50 câu)"])
        mapping_cau = {"Kiểm tra 15 phút (10 câu)": 10, "Giữa kì (20 câu)": 20, "Học kì (40 câu)": 40, "HSG (50 câu)": 50}
    with col2:
        chuong_chon = st.multiselect("📚 Chọn chương:", ds_chuong_sorted, default=ds_chuong_sorted)

    if st.button("🚀 TẠO ĐỀ THI", type="primary", use_container_width=True):
        all_questions = []
        for c in chuong_chon:
            for b, data in chuong_dict[c].items():
                all_questions.extend(data.get("cau_hoi", []))
        if len(all_questions) == 0: st.error("❌ Chương chưa có câu hỏi!")
        else:
            st.session_state[f"dethi_{mon}_{lop}"] = random.sample(all_questions, min(mapping_cau[loai_de], len(all_questions)))
            st.session_state[f"ten_dethi_{mon}_{lop}"] = loai_de

    if f"dethi_{mon}_{lop}" in st.session_state:
        de_thi = st.session_state[f"dethi_{mon}_{lop}"]
        st.markdown(f"#### 📜 {st.session_state.get(f'ten_dethi_{mon}_{lop}', loai_de).upper()} — ({len(de_thi)} Câu)")
        with st.form(f"form_thi_{mon}_{lop}"):
            tl_thi = {}
            for i, ch in enumerate(de_thi, 1):
                st.markdown(f"**Câu {i}:** {ch.get('nd') or ch.get('de')}")
                tl_thi[i] = st.radio(f"Đ/á {i}:", ch["da"], key=f"thi_{mon}_{lop}_{i}", index=None, label_visibility="collapsed")
                st.divider()
            if st.form_submit_button("🎯 NỘP BÀI CHẤM ĐIỂM", type="primary"):
                if None in tl_thi.values(): st.warning("⚠️ Còn câu chưa chọn đáp án!")
                else:
                    dung = sum(1 for i, ch in enumerate(de_thi, 1) if tl_thi[i] == ch["da"][ch["d"]])
                    diem = dung / len(de_thi) * 10
                    if diem >= 8.0: st.balloons()
                    st.markdown(f"<div class='diem-thi'>🏆 ĐIỂM BÀI THI: {diem:.1f} / 10</div>", unsafe_allow_html=True)
                    with st.expander("🔍 XEM ĐÁP ÁN VÀ LỜI GIẢI", expanded=True):
                        for i, ch in enumerate(de_thi, 1):
                            d_dung = ch["da"][ch["d"]]
                            if tl_thi[i] == d_dung: st.markdown(f"✅ **Câu {i}: Đúng** — {d_dung}")
                            else: st.markdown(f"❌ **Câu {i}: Sai** — Chọn: *{tl_thi[i]}* · Đúng: **{d_dung}**")
                            st.info(f"💡 {ch['gt']}")

# ==================== GIAO DIỆN CHÍNH (SIDEBAR) ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    st.divider()
    che_do = st.radio(
        "⚙️ Chế độ & Công cụ:", 
        [
            "📖 Học theo chuyên đề", 
            "📝 Phòng thi / Kiểm tra",
            "🎪 Phòng thí nghiệm ảo",
            "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"
        ]
    )
    st.divider()
    if che_do not in ["🎪 Phòng thí nghiệm ảo", "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"]:
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
        hien_thi_tien_do()
    elif che_do == "🎪 Phòng thí nghiệm ảo":
        mon = "🎪 Phòng Thí Nghiệm Khoa Học"
        st.success("✨ Đang mở Phòng Thí Nghiệm Khoa Học!")
    else:
        mon = "⚙️ Trạm Nạp Dữ Liệu"
        st.success("✨ Chế độ Admin: Nạp dữ liệu vào Database.")

# ==================== ĐIỀU HƯỚNG MÀN HÌNH CHÍNH ====================
bai_dang_hoc = ""

if che_do == "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)":
    hien_thi_tram_nap_du_lieu()
elif che_do == "🎪 Phòng thí nghiệm ảo":
    hien_thi_phong_thi_nghiem("🔬 Môn Vật lý (KHTN)", key_prefix="sidebar_mode")
else:
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">{mon}</p>
        <p class="hero-sub">Hệ thống lý thuyết trọng tâm, bài tập phân hóa cơ bản - nâng cao, phòng thí nghiệm ảo và Gia sư AI 24/7</p>
    </div>
    """, unsafe_allow_html=True)

    lop_dict = DATABASE[mon]
    if not lop_dict:
        st.warning(f"⚠️ Chưa có dữ liệu cho môn **{mon}**.")
    else:
        ds_lop = list(lop_dict.keys())
        idx_lop = ds_lop.index("Lớp 7") if "Lớp 7" in ds_lop else 0
        
        if che_do == "📖 Học theo chuyên đề":
            col_l, col_c, col_b = st.columns([1, 2, 2])
            with col_l: lop = st.selectbox("🏫 Khối lớp:", ds_lop, index=idx_lop, key="lop_main")
            chuong_dict = lop_dict[lop]
            if not chuong_dict: st.warning("Chưa có dữ liệu chương.")
            else:
                with col_c: chuong = st.selectbox("📂 Chọn Chương:", sap_xep_chuong(list(chuong_dict.keys())), key="chuong_main")
                bai_dict = chuong_dict[chuong]
                if not bai_dict: st.warning("Chưa có dữ liệu bài học.")
                else:
                    with col_b: bai = st.selectbox("📘 Chọn Chuyên đề:", list(bai_dict.keys()), key="bai_main")
                    bai_dang_hoc = f"{chuong} - {bai}"
                    st.markdown("---")
                    hien_thi_bai(mon, lop, chuong, bai, bai_dict[bai])
        else:
            lop = st.selectbox("🏫 Chọn khối lớp dự thi:", ds_lop, index=idx_lop, key="lop_thi")
            chuong_dict = lop_dict[lop]
            if chuong_dict: hien_thi_che_do_thi(mon, lop, chuong_dict)

# ==========================================================
# KHU VỰC GIA SƯ AI ĐA GIÁC QUAN & MẮT THẦN
# ==========================================================
if che_do != "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)":
    st.divider()
    st.header("💬 Trợ lý AI 24/7 - Hỏi đáp cùng Gia sư")

    idx_mon_ai = 0
    if "Vật lý" in mon: idx_mon_ai = 1
    elif "Hóa học" in mon: idx_mon_ai = 2

    col_ai1, col_ai2, col_ai3 = st.columns([2.5, 1.2, 1])
    with col_ai1:
        mon_hoc_ai = st.radio("Ngữ cảnh môn:", ["Toán", "Vật Lý", "Hóa Học", "Chuyện ngoài lề"], index=idx_mon_ai, horizontal=True)
    with col_ai2:
        st.write("")
        tu_dong_doc = st.checkbox("🔊 Tự động đọc to", value=True)
    with col_ai3:
        st.write("")
        if st.button("🗑️ Xóa lịch sử chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    ten_mon_ai_hien_tai = "Khoa học Tự nhiên và Toán học" if che_do == "🎪 Phòng thí nghiệm ảo" else mon

    if mon_hoc_ai == "Chuyện ngoài lề":
        SYSTEM_PROMPT = """Bạn là người anh/chị AI tâm lý (Gen Z). Đồng cảm áp lực học tập, khuyên về kỹ năng sống, quản lý thời gian. Giải đáp kiến thức xã hội, vũ trụ. Xưng hô "Chị/Anh" - "Em". KHÔNG viết kéo dài chữ."""
    else:
        SYSTEM_PROMPT = f"""Gia sư AI môn {mon_hoc_ai} lớp 7. Học sinh đang học: "{ten_mon_ai_hien_tai}" ({bai_dang_hoc}).
        1. KHÔNG giải bài hộ hoặc đưa đáp án cuối.
        2. Dùng phương pháp Socratic đặt câu hỏi gợi mở từng bước.
        3. CHỈ DÙNG kiến thức {mon_hoc_ai} lớp 7.
        4. Trình bày công thức Toán/Hóa rõ ràng. KHÔNG viết kéo dài chữ."""

    model = genai.GenerativeModel(model_name="gemini-3.5-flash", system_instruction=SYSTEM_PROMPT)

    if "chat_history" not in st.session_state: st.session_state.chat_history = []
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    img_pil, btn_gui_anh = None, False
    if HAS_PIL:
        with st.expander("📸 Mắt thần AI — Gửi ảnh bài tập / hình vẽ", expanded=False):
            t1, t2 = st.tabs(["📁 Tải ảnh", "📷 Camera"])
            with t1: file_anh = st.file_uploader("Chọn ảnh (JPG, PNG):", type=["png", "jpg", "jpeg"])
            with t2: cam_anh = st.camera_input("Chụp ảnh:")
            anh_chon = cam_anh or file_anh
            if anh_chon:
                img_pil = Image.open(anh_chon)
                st.image(img_pil, width=320)
                btn_gui_anh = st.button("🔍 Nhờ Gia sư xem giải bài trong ảnh", type="primary")

    text_from_mic = None
    if HAS_MIC:
        st.markdown("🎙️ **Bấm vào đây để đọc câu hỏi:**")
        text_from_mic = speech_to_text(language='vi-VN', start_prompt="🔴 NÓI", stop_prompt="⏹️ DỪNG", just_once=True, key='STT')

    prompt_from_keyboard = st.chat_input("Em đang mắc kẹt bài nào...")
    prompt = "Chị xem giúp em bài tập trong ảnh với ạ!" if btn_gui_anh else (text_from_mic or prompt_from_keyboard)

    if prompt:
        with st.chat_message("user"):
            if img_pil: st.image(img_pil, width=250)
            st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            gemini_history = [{"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} for m in st.session_state.chat_history[:-1]]
            chat_session = model.start_chat(history=gemini_history)
            response = chat_session.send_message([prompt, img_pil] if img_pil else prompt)
            st.markdown(response.text)
            
            if HAS_TTS:
                try:
                    clean_text = lam_sach_van_ban_doc(response.text)
                    if clean_text:
                        tts = gTTS(text=clean_text, lang='vi')
                        afp = io.BytesIO()
                        tts.write_to_fp(afp)
                        afp.seek(0)
                        st.audio(afp, format='audio/mp3', autoplay=tu_dong_doc)
                except Exception: st.caption("🔇 (Chưa tạo được âm thanh)")
            
        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
