# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Toàn diện: Toán, Lý, Hóa & Ngữ Văn + Tìm Kiếm + Dark/Light Mode + AI Đa Giác Quan
"""
import streamlit as st
import google.generativeai as genai
import io
import random
import re
import time
import zipfile
import xml.etree.ElementTree as ET

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

# Mở "két sắt" lấy chìa khóa kết nối AI
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

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

# ==================== DANH MỤC MÔ PHỎNG THÍ NGHIỆM PHET (ĐÃ CẬP NHẬT ĐỦ HÓA HỌC) ====================
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

# ==================== CẤU HÌNH TRANG ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7 - Kết Nối Tri Thức",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

dark_mode = st.sidebar.checkbox("🌙 Chế độ Ban đêm (Dark Mode)", value=False)

# ==================== CẤU HÌNH CSS ====================
if dark_mode:
    CSS = """
    <style>
        .stApp { background-color: #0F172A; color: #F1F5F9; }
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"] { display: none !important; }
        [data-testid="stHeaderActionElements"] { display: none !important; }
        .stAppDeployButton { display: none !important; }
        #MainMenu { visibility: hidden !important; }
        footer { visibility: hidden !important; }
        
        .hero-banner {
            background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
            color: #F8FAFC; padding: 1.2rem 1.5rem; border-radius: 12px; margin-bottom: 1.2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        }
        .hero-title { font-size: 1.4rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 0.9rem; opacity: 0.9; margin-top: 0.3rem; color: #CBD5E1 !important; }
        
        .card-home {
            background-color: #1E293B; border: 1px solid #334155;
            padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem;
            color: #F1F5F9; display: flex; flex-direction: column; height: 100%;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
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
        [data-testid="stToolbarActions"] { display: none !important; }
        [data-testid="stHeaderActionElements"] { display: none !important; }
        .stAppDeployButton { display: none !important; }
        #MainMenu { visibility: hidden !important; }
        footer { visibility: hidden !important; }
        
        .hero-banner {
            background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
            color: white; padding: 1.2rem 1.5rem; border-radius: 12px; margin-bottom: 1.2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .hero-title { font-size: 1.4rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 0.9rem; opacity: 0.9; margin-top: 0.3rem; color: #E2E8F0 !important; }
        
        .card-home {
            background-color: #F8FAFC; border: 1px solid #E2E8F0;
            padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem;
            display: flex; flex-direction: column; height: 100%;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
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

# ==================== HÀM TIỆN ÍCH & GỌI AI THÔNG MINH ====================
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

def ghi_nhan_lich_su(tieu_de_bai, diem, dung, tong, chi_tiet_sai=None):
    if 'lich_su_hoc_tap' not in st.session_state:
        st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {
        "bai": tieu_de_bai,
        "diem": diem,
        "dung": dung,
        "tong": tong,
        "sai": chi_tiet_sai or []
    })

def hien_thi_tien_do():
    if 'lich_su_hoc_tap' in st.session_state and st.session_state.lich_su_hoc_tap:
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Lịch sử học tập gần đây")
        tong_diem = sum(item["diem"] for item in st.session_state.lich_su_hoc_tap)
        so_bai = len(st.session_state.lich_su_hoc_tap)
        diem_tb = tong_diem / so_bai
        st.sidebar.metric("Điểm trung bình", f"{diem_tb:.1f} / 10", f"Đã luyện {so_bai} bài")
        
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
    s = re.sub(
        r'[^\w\s,.?!:;()+\-*/=<>%àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]',
        '',
        s
    )
    return re.sub(r'\s+', ' ', s).strip()

def trich_xuat_word_docx(file_bytes):
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
    ds_models = [
        "gemini-3.5-flash",
        "gemini-3.5-pro",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash"
    ]
    max_retries = 3
    last_err = None

    for ten_m in ds_models:
        for attempt in range(max_retries):
            try:
                m = genai.GenerativeModel(model_name=ten_m, system_instruction=system_instruction)
                if history is not None:
                    chat_s = m.start_chat(history=history)
                    return chat_s.send_message(payload).text
                else:
                    return m.generate_content(payload).text
            except Exception as e:
                last_err = e
                error_str = str(e).lower()
                if "429" in error_str or "resource_exhausted" in error_str or "quota" in error_str:
                    time.sleep(2 * (attempt + 1))
                    continue
                else:
                    break
    raise last_err

# ==================== TÍNH NĂNG TÌM KIẾM THÔNG MINH ====================
def hien_thi_tim_kiem_toan_dien():
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🔍 Tra Cứu & Tìm Kiếm Tri Thức Thông Minh</p>
        <p class="hero-sub">Gõ từ khóa bất kỳ để tìm nhanh bài học trong toàn bộ hệ thống</p>
    </div>
    """, unsafe_allow_html=True)

    tu_khoa = st.text_input("🔎 Nhập từ khóa cần tìm kiếm:", placeholder="Gõ tên bài học hoặc khái niệm...")
    
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        ket_qua_tim = []
        
        for ten_mon, lop_dict in DATABASE.items():
            for lop, chuong_dict in lop_dict.items():
                for chuong, bai_dict in chuong_dict.items():
                    for ten_bai, data in bai_dict.items():
                        lt = data.get("ly_thuyet", "").lower()
                        vd = data.get("vi_du", "").lower()
                        if kw in ten_bai.lower() or kw in lt or kw in vd:
                            ket_qua_tim.append({
                                "mon": ten_mon,
                                "lop": lop,
                                "chuong": chuong,
                                "bai": ten_bai,
                                "data": data
                            })
        
        st.markdown(f"### 📋 Kết quả tìm kiếm cho từ khóa: *'{tu_khoa}'* ({len(ket_qua_tim)} kết quả)")
        if not ket_qua_tim:
            st.info("⚠️ Không tìm thấy bài học phù hợp.")
        else:
            for idx, item in enumerate(ket_qua_tim, 1):
                with st.expander(f"{idx}. [{item['mon']} - {item['chuong']}] — {item['bai']}"):
                    st.markdown(f"**Môn:** {item['mon']} | **Khối:** {item['lop']} | **{item['chuong']}**")
                    if st.button(f"📖 Mở ngay bài này", key=f"btn_go_to_{idx}"):
                        st.session_state["search_jump"] = item
                        st.rerun()

# ==================== HÀM TRANG CHỦ ====================
def hien_thi_trang_chu():
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🎓 HỆ THỐNG HỌC TẬP THCS — KẾT NỐI TRI THỨC (LỚP 7)</p>
        <p class="hero-sub">Toàn diện các môn: Toán, Vật lý, Hóa học & Ngữ Văn lớp 7</p>
    </div>
    """, unsafe_allow_html=True)

    col_h1, col_h2 = st.columns(2, gap="medium")
    with col_h1:
        st.markdown("""
        <div class="card-home">
            <h3>🌟 Giới thiệu Hệ thống</h3>
            <p>Không gian học tập trực tuyến bám sát sách <b>Kết Nối Tri Thức</b> lớp 7 gồm đầy đủ Toán, Lý, Hóa và Ngữ Văn.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card-home">
            <h3>🌙 Chế độ Ban đêm (Dark Mode)</h3>
            <p>Bật công tắc chế độ ban đêm ở menu bên trái để bảo vệ mắt khi ôn tập vào buổi tối.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_h2:
        st.markdown("""
        <div class="card-home">
            <h3>💬 Trợ lý Gia sư AI 24/7 (Đa môn)</h3>
            <p>Hỗ trợ giải đáp thông minh, phương pháp Socratic, tự động thử lại khi quá tải, đồng hành cùng học sinh mọi lúc mọi nơi.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card-home">
            <h3>📱 Tối ưu thiết bị di động</h3>
            <p>Giao diện co giãn mượt mà trên mọi thiết bị điện thoại, máy tính bảng và laptop.</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== HÀM PHÒNG THÍ NGHIỆM ẢO ====================
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
    url_tn = ds_tn_mon[ten_tn]
    
    if not url_tn:
        st.warning("🚧 **Tính năng đang phát triển:** Phòng thí nghiệm cho môn học này đang được cập nhật thêm mô phỏng chuẩn bị ra mắt học sinh!")
    else:
        st.components.v1.iframe(url_tn, height=580, scrolling=True)
        st.info("💡 **Mẹo thực hành:** Dùng chuột kéo thả trực tiếp trên màn hình, sau đó kéo xuống hỏi Gia sư AI để hiểu rõ bản chất nhé!")

# ==================== HÀM TRẠM NẠP DỮ LIỆU ====================
def hien_thi_tram_nap_du_lieu():
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">⚙️ Trạm Nạp Dữ Liệu Tự Động (Auto-Parser)</p>
        <p class="hero-sub">Dành cho Admin: Tải file đề bài để tạo Code Python chuẩn.</p>
    </div>
    """, unsafe_allow_html=True)

    tab_upfile, tab_paste = st.tabs(["📁 Tải File Lên", "📝 Dán Văn Bản Thô"])
    danh_sach_files = []
    with tab_upfile:
        uploaded_files = st.file_uploader("Chọn file:", type=["docx", "pdf", "png", "jpg", "jpeg", "txt"], accept_multiple_files=True, key="parser_file_uploader")
        if uploaded_files: danh_sach_files = uploaded_files
    with tab_paste:
        raw_text = st.text_area("Dán nội dung:", height=220, key="parser_raw_text")

    PROMPT_PARSER = 'Hãy chuyển đổi toàn bộ nội dung thành Dictionary Python chuẩn gồm "ly_thuyet", "vi_du", "cau_hoi", "bt_co_ban", "bt_nang_cao". Chỉ in ra code Python.'

    if st.button("⚡ Bóc tách dữ liệu", type="primary", use_container_width=True):
        if not danh_sach_files and not raw_text.strip():
            st.warning("⚠️ Vui lòng tải file hoặc dán văn bản!")
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

# ==================== HÀM HIỂN THỊ NỘI DUNG BÀI HỌC ====================
def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    st.markdown(f"### 📖 {ten_bai}")
    lt = data.get("ly_thuyet", "").strip()
    vd = data.get("vi_du", "").strip()
    ch_list = data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Trắc nghiệm", f"{len(ch_list)} câu")
    c2.metric("✏️ Cơ bản", f"{len(bt_cb)} bài")
    c3.metric("🔥 Nâng cao", f"{len(bt_nc)} bài")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Lý thuyết", "✏️ Cơ bản", "🔥 Nâng cao", "📝 Trắc nghiệm", "🎪 Thí nghiệm"])

    with tab1:
        if lt: st.markdown(f"<div class='khung-lythuyet'>{lt}</div>", unsafe_allow_html=True)
        if vd: st.markdown(f"<div class='khung-vidu'>{vd}</div>", unsafe_allow_html=True)

    with tab2:
        if not bt_cb: st.info("Chưa có bài tập.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    ans = st.text_input("Nhập kết quả:", key=f"cb_{sid}_{i}")
                    if st.button("Kiểm tra", key=f"btn_cb_{sid}_{i}"):
                        if not ans.strip(): st.warning("⚠️ Nhập đáp án trước!")
                        elif so_sanh(ans, bt["dd"]): st.markdown("<p class='dung'>✅ Chính xác!</p>", unsafe_allow_html=True)
                        else: st.markdown(f"<p class='sai'>❌ Sai. Đáp án: {bt['dd'][0]}</p>", unsafe_allow_html=True)
                        st.info(f"💡 Giải thích: {bt.get('gt') or bt.get('lg', '')}")

    with tab3:
        if not bt_nc: st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                with st.expander(f"Bài nâng cao {i}: {nc['de'][:60]}..."):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    if nc.get('hd'): st.info(f"💡 **Hướng dẫn:** {nc['hd']}")
                    ans = st.text_input("Nhập kết quả:", key=f"nc_{sid}_{i}")
                    if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                        if so_sanh(ans, nc["dd"]): st.success("🎉 Chính xác!")
                        else: st.error(f"❌ Gợi ý: {nc['dd'][0]}")
                    if st.checkbox("📖 Xem lời giải", key=f"lg_{sid}_{i}"):
                        st.success(f"**Lời giải:** {nc['lg']}")

    with tab4:
        tong = len(ch_list)
        if tong == 0: st.info("Chưa có trắc nghiệm.")
        else:
            options = sorted(list(set([n for n in [10, 15, 20, 30] if n <= tong] + [tong])))
            so_cau = st.selectbox("Chọn số lượng câu:", options, key=f"sl_{sid}")
            key_de = f"de_{sid}_{so_cau}"
            if key_de not in st.session_state: st.session_state[key_de] = random.sample(ch_list, min(so_cau, tong))
            de = st.session_state[key_de]

            with st.form(f"form_{sid}"):
                tl = {}
                for i, ch in enumerate(de, 1):
                    st.markdown(f"**Câu {i}:** {ch.get('nd') or ch.get('de')}")
                    tl[i] = st.radio(f"Câu {i}:", ch["da"], key=f"radio_{sid}_{so_cau}_{i}", index=None, label_visibility="collapsed")
                    st.divider()
                if st.form_submit_button("🚀 Nộp bài", type="primary", use_container_width=True):
                    if None in tl.values(): st.warning("⚠️ Còn câu chưa chọn!")
                    else:
                        dung = sum(1 for i, ch in enumerate(de, 1) if tl[i] == ch["da"][ch["d"]])
                        diem = dung / len(de) * 10
                        luu_tien_do(mon, lop, chuong, ten_bai, dung, len(de))
                        ghi_nhan_lich_su(f"Trắc nghiệm: {ten_bai}", diem, dung, len(de))
                        st.markdown(f"<div class='diem-thi'>🏆 KẾT QUẢ: {diem:.1f} / 10</div>", unsafe_allow_html=True)
                        for i, ch in enumerate(de, 1):
                            da_dung = ch["da"][ch["d"]]
                            if tl[i] == da_dung: st.markdown(f"✅ Câu {i}: Đúng")
                            else: st.markdown(f"❌ Câu {i}: Sai (Đúng: **{da_dung}**)")

    with tab5: hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

# ==================== HIỂN THỊ CHẾ ĐỘ THI THỬ ====================
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
            st.session_state[f"dethi_{mon}_{lop}"] = random.sample(all_questions, min(mapping_cau[loai_de], len(all_questions)))
            st.session_state[f"ten_dethi_{mon}_{lop}"] = loai_de

    if f"dethi_{mon}_{lop}" in st.session_state:
        de_thi = st.session_state[f"dethi_{mon}_{lop}"]
        with st.form(f"form_thi_{mon}_{lop}"):
            tl_thi = {}
            for i, ch in enumerate(de_thi, 1):
                st.markdown(f"**Câu {i}:** {ch.get('nd') or ch.get('de')}")
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
    st.divider()
    che_do = st.radio(
        "⚙️ Chế độ & Công cụ:", 
        [
            "🏠 Trang chủ / Hướng dẫn",
            "🔍 Tra cứu / Tìm kiếm",
            "📖 Học theo chuyên đề", 
            "📝 Phòng thi / Kiểm tra",
            "🎪 Phòng thí nghiệm ảo",
            "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"
        ]
    )
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

if che_do == "🏠 Trang chủ / Hướng dẫn": hien_thi_trang_chu()
elif che_do == "🔍 Tra cứu / Tìm kiếm": hien_thi_tim_kiem_toan_dien()
elif che_do == "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)": hien_thi_tram_nap_du_lieu()
elif che_do == "🎪 Phòng thí nghiệm ảo":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🎪 Phòng Thí Nghiệm Ảo — Khoa Học Tự Nhiên</p>
        <p class="hero-sub">Mô phỏng tương tác trực quan chuẩn PhET (Đại học Colorado, Mỹ)</p>
    </div>
    """, unsafe_allow_html=True)
    hien_thi_phong_thi_nghiem("🔬 Môn Vật lý (KHTN)", key_prefix="sidebar_mode")
else:
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">{mon} — Chương trình GDPT 2018 (Kết Nối Tri Thức)</p>
        <p class="hero-sub">Hệ thống học tập thông minh lớp 7</p>
    </div>
    """, unsafe_allow_html=True)

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
                    st.markdown("---")
                    hien_thi_bai(mon, lop, chuong, bai, bai_dict[bai])
        else:
            lop = st.selectbox("🏫 Khối lớp:", ds_lop, index=idx_lop, key="lop_thi")
            chuong_dict = lop_dict[lop]
            if chuong_dict: hien_thi_che_do_thi(mon, lop, chuong_dict)

# ==========================================================
# KHU VỰC GIA SƯ AI ĐA GIÁC QUAN (HỖ TRỢ ĐA MÔN TOÁN, LÝ, HÓA, VĂN)
# ==========================================================
if che_do not in ["🏠 Trang chủ / Hướng dẫn", "🔍 Tra cứu / Tìm kiếm", "⚙️ Trạm Nạp Dữ Liệu (Auto-Parser)"]:
    st.divider()
    st.header("💬 Trợ lý AI 24/7 - Hỏi đáp cùng Gia sư")

    idx_mon_ai = 1 if "Vật lý" in mon else (2 if "Hóa học" in mon else (3 if "Ngữ Văn" in mon else 0))
    col_ai1, col_ai2, col_ai3 = st.columns([2.5, 1.2, 1])
    with col_ai1:
        mon_hoc_ai = st.radio("Ngữ cảnh môn:", ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn", "Chuyện ngoài lề"], index=idx_mon_ai, horizontal=True, label_visibility="collapsed")
    with col_ai2:
        tu_dong_doc = st.checkbox("🔊 Đọc to", value=True)
    with col_ai3:
        if st.button("🗑️ Xóa chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    if mon_hoc_ai == "Ngữ Văn":
        SYSTEM_PROMPT = f"Bạn là giáo viên Ngữ Văn AI nhiệt tình, sâu sắc chuyên kèm môn Ngữ Văn lớp 7 sách Kết Nối Tri Thức. Học sinh đang học: '{mon}' ({bai_dang_hoc}). Hướng dẫn học sinh phân tích tác phẩm, cảm thụ văn học và lập dàn ý đoạn văn, không viết văn mẫu hộ."
    else:
        SYSTEM_PROMPT = f"Bạn là gia sư AI môn {mon_hoc_ai} lớp 7 sách Kết Nối Tri Thức. Dùng phương pháp Socratic gợi mở từng bước, không giải bài hộ. Trình bày ngắn gọn, chuẩn xác."

    if "chat_history" not in st.session_state: st.session_state.chat_history = []
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    img_pil, btn_gui_anh = None, False
    if HAS_PIL:
        with st.expander("📸 Mắt thần AI — Gửi ảnh chụp đề bài / đoạn văn", expanded=False):
            file_anh = st.file_uploader("Tải ảnh:", type=["png", "jpg", "jpeg"])
            if file_anh:
                img_pil = Image.open(file_anh)
                st.image(img_pil, width=300)
                btn_gui_anh = st.button("🔍 Gửi ảnh cho Gia sư", type="primary")

    text_from_mic = speech_to_text(language='vi-VN', start_prompt="🔴 NÓI", stop_prompt="⏹️ DỪNG", just_once=True, key='STT') if HAS_MIC else None
    prompt = "Chị xem giúp em bài tập trong ảnh với ạ!" if btn_gui_anh else (text_from_mic or st.chat_input("Em đang mắc kẹt bài nào..."))

    if prompt:
        with st.chat_message("user"):
            if img_pil: st.image(img_pil, width=250)
            st.markdown(prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            gemini_history = [{"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} for m in st.session_state.chat_history[:-1]]
            try:
                ans_text = goi_gemini_an_toan([prompt, img_pil] if img_pil else prompt, system_instruction=SYSTEM_PROMPT, history=gemini_history)
                st.markdown(ans_text)
                st.session_state.chat_history.append({"role": "assistant", "content": ans_text})
                if HAS_TTS:
                    clean_text = lam_sach_van_ban_doc(ans_text)
                    if clean_text:
                        afp = io.BytesIO()
                        gTTS(text=clean_text, lang='vi').write_to_fp(afp)
                        afp.seek(0)
                        st.audio(afp, format='audio/mp3', autoplay=tu_dong_doc)
            except Exception as e:
                st.error(f"⚠️ Hệ thống AI đang có nhiều học sinh truy cập cùng lúc (Giới hạn Free Tier). Đang tự động thử lại hoặc em chờ vài giây rồi gửi lại câu hỏi nhé! (Lỗi: {e})")
