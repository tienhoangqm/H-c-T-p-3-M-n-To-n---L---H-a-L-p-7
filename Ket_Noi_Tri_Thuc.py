# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Toàn diện: Bài Học + Thí Nghiệm Ảo + Gia Sư AI + Trạm Nạp Dữ Liệu (Upfile & Auto-Parser)
"""
import streamlit as st
import google.generativeai as genai
import io
import random
import re
import zipfile
import xml.etree.ElementTree as ET

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
    if not x:
        return False
    for d in ds_dung:
        y = chuan_hoi(d)
        if not y:
            continue
        if x == y:
            return True
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

def lam_sach_van_ban_doc(text):
    """Làm sạch Emoji, ký hiệu Toán LaTeX và Markdown để giọng đọc AI mượt mà 100%"""
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\mathbb{Q}', 'Q').replace(r'\mathbb{Z}', 'Z').replace(r'\mathbb{N}', 'N').replace(r'\mathbb{R}', 'R')
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ').replace(r'\div', ' chia ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    s = re.sub(
        r'[^\w\s,.?!:;()+\-*/=<>%àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]',
        '',
        s
    )
    return re.sub(r'\s+', ' ', s).strip()

def trich_xuat_word_docx(file_bytes):
    """Đọc toàn bộ văn bản từ file Word (.docx) bằng thư viện chuẩn Python (không cần cài python-docx)"""
    try:
        with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
            xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        doan_van = []
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                doan_van.append(''.join(texts))
        return '\n'.join(doan_van)
    except Exception as e:
        return f"[Lỗi đọc file Word: {e}]"

def goi_gemini_an_toan(payload, system_instruction, history=None):
    """Hàm gọi Gemini ưu tiên dòng 3.5 và tự động chuyển đổi dự phòng nếu gặp lỗi ResourceExhausted"""
    ds_models = [
        "gemini-3.5-flash",
        "gemini-3.5-pro",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash"
    ]
    last_err = None
    for ten_m in ds_models:
        try:
            m = genai.GenerativeModel(model_name=ten_m, system_instruction=system_instruction)
            if history is not None:
                chat_s = m.start_chat(history=history)
                return chat_s.send_message(payload).text
            else:
                return m.generate_content(payload).text
        except Exception as e:
            last_err = e
            continue
    raise last_err

# ==================== HÀM HIỂN THỊ PHÒNG THÍ NGHIỆM ====================
def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    st.markdown("#### 🎪 Phòng Thí Nghiệm & Mô Phỏng Tương Tác (PhET Colorado)")
    ds_tn_mon = DANH_MUC_THI_NGHIEM.get(mon_hien_tai, {})
    if not ds_tn_mon:
        ds_tn_mon = DANH_MUC_THI_NGHIEM["🔬 Môn Vật lý (KHTN)"]
    ten_tn = st.selectbox(
        f"🔬 Chọn mô phỏng thực hành cho {mon_hien_tai}:",
        list(ds_tn_mon.keys()),
        key=f"select_tn_{key_prefix}_{lam_sach_id(mon_hien_tai)}"
    )
    st.components.v1.iframe(ds_tn_mon[ten_tn], height=580, scrolling=True)
    st.info("💡 **Mẹo thực hành:** Dùng chuột kéo thả trực tiếp trên màn hình, sau đó kéo xuống hỏi Gia sư AI để hiểu rõ bản chất nhé!")

# ==================== HÀM AUTO-PARSER (TRẠM NẠP DỮ LIỆU + UPFILE) ====================
def hien_thi_tram_nap_du_lieu():
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">⚙️ Trạm Nạp Dữ Liệu Tự Động (Auto-Parser)</p>
        <p class="hero-sub">Dành cho Admin: Tải trực tiếp file đề bài (Word, PDF, Ảnh, TXT) hoặc dán văn bản thô để biến thành cấu trúc Code Python chuẩn 100%.</p>
    </div>
    """, unsafe_allow_html=True)

    tab_upfile, tab_paste = st.tabs([
        "📁 Cách 1: Tải File Lên (Word, PDF, Ảnh, TXT — Không cần Copy)",
        "📝 Cách 2: Dán Nội Dung Thô Trực Tiếp"
    ])

    danh_sach_files = []
    with tab_upfile:
        st.markdown("### 📤 1. Tải file bài giảng / đề cương / đề thi lên hệ thống")
        uploaded_files = st.file_uploader(
            "Chọn hoặc kéo thả 1 hoặc nhiều file từ máy tính vào đây (Hỗ trợ: .docx, .pdf, .png, .jpg, .jpeg, .txt, .md, .py):",
            type=["docx", "pdf", "png", "jpg", "jpeg", "webp", "txt", "md", "py"],
            accept_multiple_files=True,
            key="parser_file_uploader"
        )
        if uploaded_files:
            st.success(f"✅ Đã nhận **{len(uploaded_files)} file**: " + ", ".join([f.name for f in uploaded_files]))
            danh_sach_files = uploaded_files

    with tab_paste:
        st.markdown("### 📝 1. Dán nội dung thô vào đây (Tùy chọn)")
        raw_text = st.text_area(
            "Copy bài giảng, danh sách câu hỏi trắc nghiệm, bài tập từ Word, PDF hoặc web dán vào đây:",
            height=220,
            key="parser_raw_text"
        )

    ghi_chu_them = st.text_input(
        "💡 Yêu cầu bổ sung cho AI (không bắt buộc):",
        placeholder="Ví dụ: Tạo thêm 5 câu trắc nghiệm từ lý thuyết trong file, hoặc chỉ lấy các bài tập nâng cao..."
    )

    PROMPT_PARSER = """
    Bạn là một kỹ sư dữ liệu giáo dục xuất sắc. Hãy đọc toàn bộ nội dung từ file hoặc văn bản thô do người dùng cung cấp và chuyển đổi CẤU TRÚC TOÀN BỘ NỘI DUNG ĐÓ thành một Dictionary Python duy nhất theo đúng chuẩn của hệ thống sau:

    {
        "ly_thuyet": "Nội dung lý thuyết trọng tâm (định dạng Markdown, công thức dùng $latex$).",
        "vi_du": "Các ví dụ minh họa có trong tài liệu (nếu có).",
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

    Yêu cầu TỐI THƯỢNG:
    1. Chỉ in ra đúng cấu trúc Dictionary Python, KHÔNG in ra dòng chữ giải thích nào khác ở đầu hay cuối.
    2. Chú ý ngoặc kép `"`, dấu phẩy `,` phải chuẩn xác định dạng Python Dict.
    3. Ở phần `"cau_hoi"`, thuộc tính `"d"` là vị trí index của đáp án đúng (0 là A, 1 là B, 2 là C, 3 là D). Tự động giải và xác định đáp án đúng nếu tài liệu gốc chưa khoanh đáp án.
    4. Tự sinh ra lời giải thích / hướng dẫn giải chi tiết cho các câu bài tập nếu tài liệu gốc không có.
    """

    st.markdown("### 🚀 2. Xử lý & Tạo Code Tự Động")
    if st.button("⚡ Bóc tách dữ liệu & Tạo Code Python", type="primary", use_container_width=True):
        if not danh_sach_files and not raw_text.strip():
            st.warning("⚠️ Anh Tiến vui lòng tải lên ít nhất 1 file (ở Tab 1) hoặc dán văn bản (ở Tab 2) trước khi bấm nút nhé!")
        else:
            with st.spinner("🤖 AI Gemini (ưu tiên 3.5) đang đọc tài liệu, giải đáp án và đóng gói Code Python... (Mất khoảng 5-15 giây)"):
                try:
                    payload = []
                    if ghi_chu_them.strip():
                        payload.append(f"Yêu cầu đặc biệt từ Admin: {ghi_chu_them.strip()}\n")

                    # Xử lý từng file được tải lên
                    for f in danh_sach_files:
                        ten_f = f.name.lower()
                        file_bytes = f.read()
                        if ten_f.endswith(".docx"):
                            text_docx = trich_xuat_word_docx(file_bytes)
                            payload.append(f"\n--- NỘI DUNG TỪ FILE WORD ({f.name}) ---\n{text_docx}\n")
                        elif ten_f.endswith(".pdf"):
                            payload.append({"mime_type": "application/pdf", "data": file_bytes})
                        elif ten_f.endswith((".png", ".jpg", ".jpeg", ".webp")) and HAS_PIL:
                            img_doc = Image.open(io.BytesIO(file_bytes))
                            payload.append(img_doc)
                        else:
                            text_txt = file_bytes.decode("utf-8", errors="ignore")
                            payload.append(f"\n--- NỘI DUNG TỪ FILE ({f.name}) ---\n{text_txt}\n")

                    # Gộp thêm văn bản dán tay (nếu có)
                    if raw_text.strip():
                        payload.append(f"\n--- NỘI DUNG VĂN BẢN DÁN TRỰC TIẾP ---\n{raw_text.strip()}\n")

                    payload.append("\nHãy chuyển đổi toàn bộ dữ liệu trên thành cấu trúc Dictionary Python chuẩn:")

                    ket_qua = goi_gemini_an_toan(payload, system_instruction=PROMPT_PARSER)
                    clean_code = ket_qua.replace("```python", "").replace("```json", "").replace("```", "").strip()
                    st.session_state["parsed_code_result"] = clean_code
                except Exception as e:
                    st.error(f"❌ Có lỗi xảy ra trong quá trình xử lý: {e}")

    # Hiển thị kết quả nếu đã tạo thành công
    if "parsed_code_result" in st.session_state and st.session_state["parsed_code_result"]:
        code_out = st.session_state["parsed_code_result"]
        st.success("✅ Thành công! Dữ liệu từ file đã được bóc tách và định dạng chuẩn Python.")
        
        col_dl1, col_dl2 = st.columns([1, 2])
        with col_dl1:
            st.download_button(
                label="💾 Tải đoạn Code này về máy (.py)",
                data=code_out.encode("utf-8"),
                file_name="du_lieu_bai_hoc_moi.py",
                mime="text/x-python",
                use_container_width=True
            )
        with col_dl2:
            st.info("💡 Hoặc bấm biểu tượng **Copy** (2 hình vuông chồng nhau) ở góc trên bên phải khung code bên dưới để dán vào `data_toan.py`, `data_vatly.py` hoặc `data_hoa.py`.")

        st.code(code_out, language="python")

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

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📚 Lý thuyết & Ví dụ", 
        "✏️ Bài tập cơ bản", 
        "🔥 Bài tập nâng cao", 
        "📝 Trắc nghiệm bài học",
        "🎪 Thí nghiệm & Mô phỏng"
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
        else:
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

    with tab5:
        hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

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

# ==================== GIAO DIỆN CHÍNH (SIDEBAR) ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    st.caption("Hệ thống Ôn luyện & Kiểm tra THCS")
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
    if che_do != "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)":
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
        hien_thi_tien_do()
    else:
        mon = "⚙️ Trạm Nạp Dữ Liệu"
        st.success("✨ Chế độ Admin: Tải file hoặc dán văn bản để tạo code tự động.")

# ==================== ĐIỀU HƯỚNG MÀN HÌNH CHÍNH ====================
bai_dang_hoc = ""

if che_do == "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)":
    hien_thi_tram_nap_du_lieu()
elif che_do == "🎪 Phòng thí nghiệm ảo":
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">🎪 Phòng Thí Nghiệm Ảo — {mon}</p>
        <p class="hero-sub">Mô phỏng tương tác trực quan chuẩn PhET (Đại học Colorado) kết hợp Gia sư AI giải đáp hiện tượng</p>
    </div>
    """, unsafe_allow_html=True)
    hien_thi_phong_thi_nghiem(mon, key_prefix="sidebar_mode")
else:
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">{mon} — Chương trình GDPT 2018 (Kết Nối Tri Thức)</p>
        <p class="hero-sub">Hệ thống lý thuyết trọng tâm, bài tập phân hóa cơ bản - nâng cao, phòng thí nghiệm ảo và Gia sư AI 24/7</p>
    </div>
    """, unsafe_allow_html=True)

    lop_dict = DATABASE[mon]
    if not lop_dict:
        st.warning(f"⚠️ Đang cập nhật dữ liệu cho môn **{mon}**...")
    else:
        ds_lop = list(lop_dict.keys())
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
                    bai_dang_hoc = f"{chuong} - {bai}"
                    st.markdown("---")
                    hien_thi_bai(mon, lop, chuong, bai, bai_dict[bai])
        else:
            lop = st.selectbox("🏫 Chọn khối lớp dự thi:", ds_lop, index=idx_lop, key="lop_thi")
            chuong_dict = lop_dict[lop]
            if chuong_dict:
                hien_thi_che_do_thi(mon, lop, chuong_dict)

# ==========================================================
# KHU VỰC GIA SƯ AI ĐA GIÁC QUAN & MẮT THẦN
# ==========================================================
if che_do != "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)":
    st.divider()
    st.header("💬 Trợ lý AI 24/7 - Hỏi đáp cùng Gia sư")

    idx_mon_ai = 0
    if "Vật lý" in mon:
        idx_mon_ai = 1
    elif "Hóa học" in mon:
        idx_mon_ai = 2

    col_ai1, col_ai2, col_ai3 = st.columns([2.5, 1.2, 1])
    with col_ai1:
        st.markdown("**📌 Em đang muốn hỏi Gia sư về môn nào?**")
        mon_hoc_ai = st.radio(
            "Ngữ cảnh môn học:", 
            ["Toán", "Vật Lý", "Hóa Học", "Chuyện ngoài lề"], 
            index=idx_mon_ai, 
            horizontal=True,
            label_visibility="collapsed"
        )
    with col_ai2:
        st.write("")
        tu_dong_doc = st.checkbox("🔊 Tự động đọc to", value=True)
    with col_ai3:
        st.write("")
        if st.button("🗑️ Xóa lịch sử chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    if mon_hoc_ai == "Chuyện ngoài lề":
        SYSTEM_PROMPT = """
        Bạn là một người anh/người chị AI tâm lý, hài hước (Gen Z) đang trò chuyện thư giãn cùng học sinh lớp 7.
        Nguyên tắc:
        1. Lắng nghe, đồng cảm với những áp lực học tập và tâm lý tuổi mới lớn của các em.
        2. Đưa ra lời khuyên về phương pháp học tập, cách quản lý thời gian hoặc kĩ năng sống.
        3. Giải đáp các câu hỏi kiến thức xã hội, vũ trụ, khoa học ngoài lề một cách thú vị, truyền cảm hứng.
        4. Xưng hô: "Chị" (hoặc "Anh") và "Em", dùng nhiều icon thân thiện.
        5. TUYỆT ĐỐI KHÔNG viết kéo dài chữ để bộ phát giọng nói tiếng Việt đọc chuẩn xác.
        """
    else:
        SYSTEM_PROMPT = f"""
        Bạn là một gia sư AI trẻ trung, năng động, hài hước (Gen Z) chuyên kèm môn {mon_hoc_ai} lớp 7 (bám sát sách Kết Nối Tri Thức).
        Thông tin thêm: Trên màn hình học sinh đang mở mục "{mon}" ({bai_dang_hoc}).
        Nguyên tắc SƯ PHẠM TỐI THƯỢNG:
        1. TUYỆT ĐỐI KHÔNG BAO GIỜ giải bài hộ hoặc đưa ra đáp án cuối cùng ngay lập tức.
        2. Sử dụng phương pháp Socratic: Đặt câu hỏi gợi mở từng bước nhỏ để học sinh tự suy nghĩ và tính toán. Nếu học sinh thảo luận về Phòng thí nghiệm ảo hoặc gửi ảnh, hãy hướng dẫn các em quan sát từng bước.
        3. HIỆN TẠI HỌC SINH ĐANG HỎI MÔN {mon_hoc_ai}: CHỈ ĐƯỢC DÙNG phương pháp và kiến thức của môn {mon_hoc_ai} lớp 7 để giải thích. TUYỆT ĐỐI KHÔNG dùng kiến thức vượt cấp.
        4. Xưng hô: "Chị" (hoặc "Anh") và "Em", dùng icon thân thiện.
        5. Trình bày công thức rõ ràng, giải thích ngắn gọn. KHÔNG viết kéo dài chữ để bộ phát giọng nói tiếng Việt đọc chuẩn xác.
        """

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    img_pil, btn_gui_anh = None, False
    if HAS_PIL:
        with st.expander("📸 Mắt thần AI — Gửi ảnh chụp đề bài / hình vẽ cho Gia sư", expanded=False):
            t1, t2 = st.tabs(["📁 Tải ảnh từ máy / điện thoại", "📷 Mở Camera chụp trực tiếp"])
            with t1:
                file_anh = st.file_uploader("Chọn ảnh chụp bài tập hoặc hình vẽ (JPG, PNG):", type=["png", "jpg", "jpeg"], key="upload_anh")
            with t2:
                cam_anh = st.camera_input("Đưa vở hoặc đề bài vào khung hình để chụp:", key="cam_anh")
            anh_chon = cam_anh or file_anh
            if anh_chon:
                img_pil = Image.open(anh_chon)
                st.image(img_pil, caption="📌 Ảnh đề bài đang đính kèm cho Gia sư", width=320)
                btn_gui_anh = st.button("🔍 Nhờ Gia sư xem và gợi ý giải bài trong ảnh này", type="primary")

    text_from_mic = None
    if HAS_MIC:
        st.markdown("🎙️ **Lười gõ phím? Bấm vào nút bên dưới để đọc câu hỏi nhé:**")
        text_from_mic = speech_to_text(
            language='vi-VN',
            start_prompt="🔴 Bấm vào đây để NÓI",
            stop_prompt="⏹️ Bấm vào đây để DỪNG",
            just_once=True,
            key='STT'
        )

    prompt_from_keyboard = st.chat_input("Em đang mắc kẹt ở bài nào, gõ vào đây anh/chị gợi ý cho nhé...")
    prompt = "Chị xem giúp em bài tập trong bức ảnh đính kèm này và gợi ý từng bước cách làm cho em với ạ!" if btn_gui_anh else (text_from_mic or prompt_from_keyboard)

    if prompt:
        with st.chat_message("user"):
            if img_pil:
                st.image(img_pil, width=250)
            st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            gemini_history = [
                {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                for m in st.session_state.chat_history[:-1]
            ]
            try:
                ans_text = goi_gemini_an_toan(
                    [prompt, img_pil] if img_pil else prompt,
                    system_instruction=SYSTEM_PROMPT,
                    history=gemini_history
                )
                st.markdown(ans_text)
                st.session_state.chat_history.append({"role": "assistant", "content": ans_text})

                if HAS_TTS:
                    try:
                        clean_text = lam_sach_van_ban_doc(ans_text)
                        if clean_text:
                            tts = gTTS(text=clean_text, lang='vi')
                            afp = io.BytesIO()
                            tts.write_to_fp(afp)
                            afp.seek(0)
                            st.audio(afp, format='audio/mp3', autoplay=tu_dong_doc)
                    except Exception:
                        st.caption("🔇 (Hiện chưa tạo được âm thanh cho câu trả lời này)")
            except Exception as e:
                st.error(f"⚠️ Gia sư AI đang bận hoặc hết lượt gọi miễn phí trong phút này. Em đợi khoảng 30 giây rồi hỏi lại nhé! (Chi tiết: {e})")
