# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Hoàn Chỉnh: Đã xử lý trọn vẹn 4 hạng mục tối ưu (Regex, Thư viện, Bọc lỗi API, Kiểm tra tồn tại bài học)
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
    page_title="Hệ Thống Học Tập Lớp 7 - Kết Nối Tri Thức",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# ==================== ĐỌC SECRETS & CẤU HÌNH AN TOÀN (MỤC 3) ====================
def get_secret(key_name, default_val=""):
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
        try:
            k_val = get_secret(k_name)
            if k_val and str(k_val).strip() not in keys:
                keys.append(str(k_val).strip())
        except Exception:
            pass
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

# ==================== TẢI THƯ VIỆN NGOẠI VI AN TOÀN ====================
with st.spinner("🚀 Hệ thống đang khởi động..."):
    try:
        from streamlit_mic_recorder import speech_to_text
        HAS_MIC = True
    except Exception:
        HAS_MIC = False
    try:
        from gtts import gTTS
        HAS_TTS = True
    except Exception:
        HAS_TTS = False
    try:
        from PIL import Image
        HAS_PIL = True
    except Exception:
        HAS_PIL = False

# ==================== HỆ THỐNG ĐẾM NGƯỜI DÙNG & RATE LIMIT ====================
def cap_nhat_nguoi_online():
    try:
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
    except Exception:
        return 1

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
    if not ma_hash or not noi_dung:
        return
    nd_lower = noi_dung.lower()
    if any(k in nd_lower for k in ["bận", "quá tải", "lỗi", "chuyển sang", "bảo trì"]) or "⚠️" in noi_dung:
        return
    try:
        with GLOBALS["ai_cache_lock"]:
            cache = GLOBALS["ai_cache"]
            cache[ma_hash] = noi_dung
            cache.move_to_end(ma_hash)
            if len(cache) > 100:
                cache.popitem(last=False)
    except Exception:
        pass

def lay_cache_ai(ma_hash):
    if not ma_hash:
        return None
    try:
        with GLOBALS["ai_cache_lock"]:
            cache = GLOBALS["ai_cache"]
            if ma_hash in cache:
                cache.move_to_end(ma_hash)
                return cache[ma_hash]
    except Exception:
        pass
    return None

# ==================== HÀM TIỆN ÍCH CHẤM SỐ HỌC (MỤC 1) & TRẮC NGHIỆM ====================
def ep_kieu_so_hoc(chuoi):
    s = str(chuoi).strip().replace(" ", "")
    if not s:
        return None
    if '/' in s:
        parts = s.split('/')
        if len(parts) == 2:
            try:
                return float(parts[0]) / float(parts[1])
            except (ValueError, TypeError, ZeroDivisionError):
                return None
    # Đã cập nhật Regex mới theo đúng yêu cầu (Mục 1)
    if re.fullmatch(r'-?\d{1,3}(?:\.\d{3})*(?:,\d+)?', s):
        s = s.replace('.', '').replace(',', '.')
    else:
        s = s.replace(',', '.')
    try:
        return float(s)
    except ValueError:
        return None

def so_sanh_so_hoc(nd, ds_dung):
    if not ds_dung:
        return False
    val_x = ep_kieu_so_hoc(nd)
    for d in ds_dung:
        val_d = ep_kieu_so_hoc(d)
        if val_x is not None and val_d is not None:
            if abs(val_x - val_d) < 1e-5:
                return True
        if re.sub(r'\s+', '', str(nd).lower()) == re.sub(r'\s+', '', str(d).lower()):
            return True
    return False

def tron_dap_an_thong_minh(ch):
    da_goc = list(ch.get("da", []))
    if not da_goc:
        return [], 0
    idx_dung = ch.get("d", 0)
    if idx_dung >= len(da_goc):
        idx_dung = 0
    d_dung = da_goc[idx_dung]
    for ans in da_goc:
        txt = str(ans).lower()
        if "cả" in txt or "tất cả" in txt or "đáp án" in txt or "phương án" in txt or "a, b" in txt:
            return da_goc, idx_dung
    random.shuffle(da_goc)
    return da_goc, da_goc.index(d_dung)

def lam_sach_id(s):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))

def sap_xep_chuong(ds_chuong):
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)

def luu_tien_do(mon, lop, chuong, ten_bai, dung, tong):
    if "tien_do_chi_tiet" not in st.session_state:
        st.session_state["tien_do_chi_tiet"] = {}
    st.session_state["tien_do_chi_tiet"][f"{mon}_{lop}_{chuong}_{ten_bai}"] = {"dung": dung, "tong": tong}

def ghi_nhan_lich_su(tieu_de_bai, diem, dung, tong):
    if 'lich_su_hoc_tap' not in st.session_state:
        st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {"bai": tieu_de_bai, "diem": diem, "dung": dung, "tong": tong})

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ').replace(r'\div', ' chia ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    s = re.sub(r'[^\w\s,.?!:;()+\-*/=<>%àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]', '', s)
    return re.sub(r'\s+', ' ', s).strip()

def doc_to_an_toan(text, autoplay=True):
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

def trich_xuat_word_docx(file_bytes):
    try:
        with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
            xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        doan_van = [''.join([t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]) for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')]
        return '\n'.join([p for p in doan_van if p])
    except Exception as e:
        return f"[Lỗi đọc file Word: {e}]"

# ==================== MÔ-ĐUN AI (BỌC LỖI TOÀN DIỆN - MỤC 3) ====================
def goi_dola_toi_uu(cau_hoi):
    if not DOLA_ENDPOINT or not DOLA_KEY:
        return None
    try:
        phan_hoi = requests.post(
            DOLA_ENDPOINT,
            headers={"Authorization": f"Bearer {DOLA_KEY}", "X-Project-Quota-Tier": DOLA_PROJECT_TIER},
            json={"cau_hoi": cau_hoi, "chuong_trinh": "ket_noi_tri_thuc_lop7", "che_do": "chuan_sgk"},
            timeout=4.0
        )
        if phan_hoi.status_code == 200:
            data_json = phan_hoi.json()
            nd = data_json.get("noi_dung_chuan") or data_json.get("answer") or data_json.get("text") or ""
            return nd.strip() if nd else None
        return None
    except Exception:
        return None

@st.cache_resource(ttl=3600, show_spinner=False)
def lay_ds_model_kha_dung(api_key):
    uu_tien = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
    try:
        genai.configure(api_key=api_key)
        ds_hien_co = [m.name.replace("models/", "") for m in genai.list_models() if "generateContent" in getattr(m, "supported_generation_methods", [])]
        if ds_hien_co:
            return [m for m in uu_tien if m in ds_hien_co] + [m for m in ds_hien_co if "gemini" in m and m not in uu_tien]
    except Exception:
        pass
    return uu_tien

def goi_gemini_an_toan(payload, system_instruction, history=None):
    if not GEMINI_KEYS:
        raise RuntimeError("Chưa cấu hình GEMINI_API_KEY.")
    if "key_index" not in st.session_state:
        st.session_state["key_index"] = 0
    so_luong_key = len(GEMINI_KEYS)
    last_err = None

    with GLOBALS["ai_api_lock"]:
        for k_offset in range(so_luong_key):
            idx = (st.session_state["key_index"] + k_offset) % so_luong_key
            current_key = GEMINI_KEYS[idx]
            try:
                genai.configure(api_key=current_key)
                ds_models = lay_ds_model_kha_dung(current_key)
            except Exception as e:
                last_err = e
                continue

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
                        if "404" in err_str or "not found" in err_str:
                            break
                        elif "429" in err_str or "quota" in err_str:
                            if attempt == 0:
                                time.sleep(1.0)
                                continue
                            else:
                                break
                        else:
                            break
    raise last_err if last_err else RuntimeError("Không thể kết nối Gemini AI.")

# ==================== DATA TOÁN, LÝ, HÓA, VĂN ====================
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

VAN = {
    "Lớp 7": {
        "Chương 1: Bầu trời tuổi thơ (Truyện)": {
            "Văn bản 1: Bồng chanh đỏ (trích, Đỗ Chu)": {
                "ly_thuyet": "Truyện ngắn kể về hai anh em Hoài và Ý với tình yêu thương loài vật, thiên nhiên và những rung cảm tinh tế của tuổi thơ.",
                "vi_du": "Chi tiết thả chim bồng chanh đỏ về tự nhiên thể hiện sự thức tỉnh nhân cách và lòng nhân ái.",
                "cau_hoi": [
                    {"nd": "Truyện 'Bồng chanh đỏ' của tác giả nào?", "da": ["Đỗ Chu", "Tô Hoài", "Khánh Hoài", "Duy Khán"], "d": 0},
                    {"nd": "Nhân vật chính trong truyện là ai?", "da": ["Hai anh em Hoài và Ý", "Ông nội", "Côn và Bản", "Thành và Thủy"], "d": 0}
                ],
                "bt_co_ban": [{"de": "Nêu ý nghĩa nhan đề 'Bồng chanh đỏ'?", "dd": ["Biểu tượng cho vẻ đẹp thiên nhiên"], "lg": "Đó là hình ảnh trung tâm khơi gợi những cảm xúc trong trẻo."}],
                "bt_nang_cao": [{"de": "Phân tích sự biến đổi tâm trạng của nhân vật Hoài?", "dd": ["Thấu hiểu và buông bỏ"], "lg": "Thể hiện sự nhân hậu, tôn trọng tự nhiên."}]
            },
            "Văn bản 2: Bố cục và mạch ngầm trong văn bản": {
                "ly_thuyet": "Tìm hiểu cách xây dựng cốt truyện và các lớp ý nghĩa ẩn giấu trong tác phẩm truyện.",
                "cau_hoi": [{"nd": "Mạch ngầm văn bản là gì?", "da": ["Những suy nghĩ, cảm xúc ẩn giấu dưới lời văn", "Cốt truyện chính", "Lời thoại của nhân vật"], "d": 0}],
                "bt_co_ban": [{"de": "Mạch ngầm thường được bộc lộ qua đâu?", "dd": ["Chi tiết nghệ thuật"], "lg": "Thông qua các chi tiết miêu tả và hành động."}],
                "bt_nang_cao": [{"de": "Tác dụng của mạch ngầm trong truyện ngắn?", "dd": ["Tăng chiều sâu"], "lg": "Giúp người đọc suy ngẫm nhiều hơn."}]
            }
        },
        "Chương 2: Khúc tâm tình của đất nước (Thơ)": {
            "Văn bản 1: Tia nắng đầu tiên (Đức Lợi)": {
                "ly_thuyet": "Bài thơ ca ngợi vẻ đẹp thiên nhiên buổi sáng và tình cảm gia đình ấm áp.",
                "cau_hoi": [{"nd": "Bài thơ thuộc thể thơ nào?", "da": ["Thơ tự do / 5 chữ", "Thơ lục bát", "Thơ 7 chữ", "Tất cả phương án trên"], "d": 0}],
                "bt_co_ban": [{"de": "Tia nắng đầu tiên tượng trưng cho điều gì?", "dd": ["Niềm hy vọng"], "lg": "Mang ý nghĩa biểu tượng sâu sắc."}],
                "bt_nang_cao": [{"de": "Phân tích cảm xúc của nhân vật trữ tình?", "dd": ["Rung động tinh tế"], "lg": "Gắn kết thiên nhiên với gia đình."}]
            },
            "Văn bản 2: Mẹ (Đỗ Bạch Nga)": {
                "ly_thuyet": "Bài thơ khắc họa hình ảnh người mẹ tần tảo, hy sinh vì con cái.",
                "cau_hoi": [{"nd": "Biện pháp tu từ nổi bật trong bài thơ 'Mẹ' là gì?", "da": ["Ẩn dụ / So sánh", "Nói quá", "Liệt kê"], "d": 0}],
                "bt_co_ban": [{"de": "Tình cảm của người con đối với mẹ?", "dd": ["Biết ơn sâu sắc"], "lg": "Thể hiện đạo lý uống nước nhớ nguồn."}],
                "bt_nang_cao": [{"de": "Ý nghĩa hình ảnh người mẹ?", "dd": ["Biểu tượng của sự hy sinh"], "lg": "Là nguồn cội nuôi dưỡng tâm hồn."}]
            }
        },
        "Chương 3: Hành trình tri thức (Nghị luận & Thông tin)": {
            "Văn bản 1: Tự học - một cuộc du thú trường chinh": {
                "ly_thuyet": "Văn bản nghị luận bàn về tầm quan trọng và phương pháp tự học.",
                "cau_hoi": [{"nd": "Vấn đề nghị luận chính là gì?", "da": ["Tầm quan trọng của việc tự học", "Cách đọc sách hiệu quả", "Phương pháp học ngoại ngữ"], "d": 0}],
                "bt_co_ban": [{"de": "Vì sao gọi tự học là 'cuộc du thú trường chinh'?", "dd": ["Khám phá tri thức dài lâu"], "lg": "Phép ẩn dụ độc đáo."}],
                "bt_nang_cao": [{"de": "Rút ra bài học cho bản thân?", "dd": ["Chủ động, kiên trì"], "lg": "Tự học quyết định thành công."}]
            }
        }
    }
}

DATABASE = {
    "📐 Môn Toán": TOAN if TOAN else {"Lớp 7": {"Chương 1: Đang cập nhật dữ liệu Toán": {}}},
    "🔬 Môn Vật lý (KHTN)": VATLY if VATLY else {"Lớp 7": {"Chương 1: Đang cập nhật dữ liệu Lý": {}}},
    "🧪 Môn Hóa học (KHTN)": HOA if HOA else {"Lớp 7": {"Chương 1: Đang cập nhật dữ liệu Hóa": {}}},
    "📖 Môn Ngữ Văn": VAN
}

# ==================== KIỂM TRA TỒN TẠI BÀI HỌC KHI NHẢY TRANG (MỤC 4) ====================
if "search_jump" in st.session_state:
    item = st.session_state.pop("search_jump")
    j_mon = item.get("mon")
    j_lop = item.get("lop", "Lớp 7")
    j_chuong = item.get("chuong")
    j_bai = item.get("bai")
    if (j_mon in DATABASE and 
        j_lop in DATABASE[j_mon] and 
        j_chuong in DATABASE[j_mon][j_lop] and 
        j_bai in DATABASE[j_mon][j_lop][j_chuong]):
        st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
        st.session_state["mon_main"] = j_mon
        st.session_state["s_lop"] = j_lop
        st.session_state["s_chuong"] = j_chuong
        st.session_state["s_bai"] = j_bai

DANH_MUC_THI_NGHIEM = {
    "📐 Môn Toán": {"⚖️ Cân bằng phương trình & Biểu thức đại số": "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_vi.html"},
    "🔬 Môn Vật lý (KHTN)": {"💡 Khúc xạ & Phản xạ ánh sáng (Quang học 7)": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_vi.html"},
    "🧪 Môn Hóa học (KHTN)": {
        "⚛️ Xây dựng cấu tạo Nguyên tử": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_vi.html",
        "🧬 Lắp ghép Phân tử": "https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_vi.html",
        "⚖️ Cân bằng Phương trình": "https://phet.colorado.edu/sims/html/balancing-chemical-equations/latest/balancing-chemical-equations_vi.html",
        "🧪 Đo nồng độ dung dịch": "https://phet.colorado.edu/sims/html/concentration/latest/concentration_vi.html",
    },
    "📖 Môn Ngữ Văn": {
        "🗺️ Bản đồ Cấu trúc & Bối cảnh": "van_hoc_cau_truc",
        "🎭 Biểu đồ Tương tác Nhân vật": "van_hoc_nhan_vat",
        "🕸️ Sơ đồ Quan hệ Nhân vật": "van_hoc_quan_he",
        "✍️ Thực hành Luyện từ & Ngữ pháp": "van_hoc_ngu_phap",
        "📝 Trạm Lập dàn ý bài văn": "van_hoc_dan_y"
    }
}

DATA_LAB_NGU_VAN = {
    "🗺️ Bản đồ Cấu trúc & Bối cảnh": {
        "tieu_de": "Bản đồ Cấu trúc: Bồng chanh đỏ",
        "hoan_canh": "Truyện ngắn viết về tình yêu loài vật, thiên nhiên.",
        "bo_cuc": [{"phan": "Mở đầu", "noi_dung": "Tổ chim bồng chanh đỏ."}, {"phan": "Diễn biến", "noi_dung": "Cuộc mạo hiểm leo lên bờ vực."}, {"phan": "Cao trào", "noi_dung": "Quyết định thả chim."}],
        "y_nghia": "Bảo vệ môi trường sống."
    },
    "🎭 Biểu đồ Tương tác Nhân vật": {
        "nhan_vat": "Nhân vật Hoài",
        "dac_diem": "Giàu tình cảm, ham khám phá.",
        "hanh_vi_tieu_bieu": "Trèo cây; ngăn em bắt chim.",
        "dien_bien_tam_ly": [{"giai_doan": "Đầu truyện", "tam_trang": "Tò mò."}, {"giai_doan": "Cuối truyện", "tam_trang": "Thức tỉnh."}]
    },
    "🕸️ Sơ đồ Quan hệ Nhân vật": {
        "tac_pham": "Quan hệ trong 'Bồng chanh đỏ'",
        "quan_he": [{"tu_khoa": "Anh Hoài ↔️ Em Ý", "loai": "Đồng hành", "mo_ta": "Cùng chia sẻ bí mật."}, {"tu_khoa": "Con người ↔️ Thiên nhiên", "loai": "Thấu hiểu", "mo_ta": "Sự hòa hợp."}]
    },
    "✍️ Thực hành Luyện từ & Ngữ pháp": {
        "chu_de": "Biện pháp tu từ",
        "cau_hoi_mau": [{"cau": "Cánh chim đỏ như lửa.", "loai": "So sánh", "phan_tich": "Làm sinh động."}]
    },
    "📝 Trạm Lập dàn ý bài văn": {
        "the_loai": "Biểu cảm tác phẩm",
        "dan_y": [{"buoc": "Mở bài", "noi_dung": "Giới thiệu tác phẩm."}, {"buoc": "Thân bài", "noi_dung": "Cảm xúc nội dung."}, {"buoc": "Kết bài", "noi_dung": "Khẳng định giá trị."}]
    }
}

# ==================== SIDEBAR ĐIỀU HƯỚNG ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    dark_mode = st.toggle("🌙 Chế độ tối", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")
    
    if not GEMINI_KEYS:
        st.warning("⚠️ Chưa có API Key, chạy ở chế độ Mẫu.")
        
    st.divider()
    
    che_do = st.radio(
        "⚙️ Chức năng:",
        ["🏠 Trang chủ / Hướng dẫn", "🔍 Tra cứu / Tìm kiếm", "📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra", "🎪 Phòng thí nghiệm ảo", "⚙️ Trạm Nạp Dữ Liệu"],
        key="che_do_sidebar"
    )
    
    if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = che_do

    if 'lich_su_hoc_tap' in st.session_state and st.session_state.lich_su_hoc_tap:
        st.divider()
        st.markdown("### 📊 Lịch sử học tập")
        so_bai = len(st.session_state.lich_su_hoc_tap)
        st.metric("Điểm TB", f"{sum(i['diem'] for i in st.session_state.lich_su_hoc_tap) / so_bai:.1f}", f"{so_bai} bài")

# ==================== CSS TIÊM ĐỂ HIỂN THỊ GIAO DIỆN ĐẸP MẮT ====================
if dark_mode:
    st.markdown("""
    <style>
        .stApp { background-color: #0F172A; color: #F1F5F9; }
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], footer { display: none !important; }
        .hero-banner { background: linear-gradient(135deg, #1E293B 0%, #334155 100%); color: #F8FAFC; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3); }
        .hero-title { font-size: 1.6rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 1rem; opacity: 0.9; margin-top: 0.3rem; color: #CBD5E1 !important; }
        .card-home { background-color: #1E293B; border: 1px solid #334155; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; color: #F1F5F9; }
        .khung-lythuyet { background-color: #1E293B; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #3B82F6; margin-bottom: 1rem;}
        .khung-vidu { background-color: #27272A; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #F59E0B; margin-bottom: 1rem;}
        .dung { color: #34D399; font-weight: bold; }
        .sai { color: #F87171; font-weight: bold; }
        .diem-thi { font-size: 1.6rem; color: #F87171; text-align: center; padding: 1.2rem; border: 2px dashed #EF4444; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], footer { display: none !important; }
        .hero-banner { background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); color: white; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .hero-title { font-size: 1.6rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 1rem; opacity: 0.9; margin-top: 0.3rem; color: #E2E8F0 !important; }
        .card-home { background-color: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; }
        .khung-lythuyet { background-color: #EFF6FF; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #2563EB; margin-bottom: 1rem;}
        .khung-vidu { background-color: #FFFBEB; padding: 1.2rem; border-radius: 10px; border-left: 6px solid #F59E0B; margin-bottom: 1rem;}
        .dung { color: #059669; font-weight: bold; }
        .sai { color: #DC2626; font-weight: bold; }
        .diem-thi { font-size: 1.6rem; color: #E11D48; text-align: center; padding: 1.2rem; border: 2px dashed #F43F5E; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

# ==================== CÁC HÀM HIỂN THỊ UI CHI TIẾT ====================
def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    if mon_hien_tai == "📖 Môn Ngữ Văn":
        ds_modul = list(DANH_MUC_THI_NGHIEM["📖 Môn Ngữ Văn"].keys())
        chon_modul = st.selectbox("📚 Chọn Mô-đun Tương tác Ngữ Văn:", ds_modul, key=f"select_modul_{key_prefix}")
        st.divider()
        if "Bản đồ Cấu trúc" in chon_modul:
            data = DATA_LAB_NGU_VAN["🗺️ Bản đồ Cấu trúc & Bối cảnh"]
            st.markdown(f"### 🗺️ {data['tieu_de']}")
            st.info(f"⏳ **Hoàn cảnh sáng tác:** {data['hoan_canh']}")
            for item in data["bo_cuc"]:
                with st.expander(f"🔹 {item['phan']}"):
                    st.write(item['noi_dung'])
            st.success(f"💡 **Ý nghĩa nhân văn:** {data['y_nghia']}")
        elif "Biểu đồ Tương tác" in chon_modul:
            data = DATA_LAB_NGU_VAN["🎭 Biểu đồ Tương tác Nhân vật"]
            st.markdown(f"### 🎭 {data['nhan_vat']}")
            st.markdown(f"⭐ **Đặc điểm:** {data['dac_diem']}\n\n🎯 **Hành vi:** {data['hanh_vi_tieu_bieu']}")
            st.markdown("#### 📈 Diễn biến tâm lý:")
            for stage in data["dien_bien_tam_ly"]:
                st.markdown(f"* **{stage['giai_doan']}:** {stage['tam_trang']}")
        elif "Sơ đồ Quan hệ" in chon_modul:
            data = DATA_LAB_NGU_VAN["🕸️ Sơ đồ Quan hệ Nhân vật"]
            st.markdown(f"### 🕸️ {data['tac_pham']}")
            for idx, rel in enumerate(data["quan_he"], 1):
                with st.expander(f"{idx}. {rel['tu_khoa']} — *[{rel['loai']}]*"):
                    st.write(rel['mo_ta'])
        elif "Luyện từ & Ngữ pháp" in chon_modul:
            data = DATA_LAB_NGU_VAN["✍️ Thực hành Luyện từ & Ngữ pháp"]
            st.markdown(f"### ✍️ {data['chu_de']}")
            for idx, bai in enumerate(data["cau_hoi_mau"], 1):
                st.markdown(f"**Câu {idx}:** `{bai['cau']}`\n\n👉 **Phân loại:** **{bai['loai']}**")
                st.info(f"💡 **Giải thích:** {bai['phan_tich']}")
        elif "Lập dàn ý" in chon_modul:
            data = DATA_LAB_NGU_VAN["📝 Trạm Lập dàn ý bài văn"]
            st.markdown(f"### 📝 Lập dàn ý: {data['the_loai']}")
            for buoc in data["dan_y"]:
                with st.expander(f"📋 {buoc['buoc']}"):
                    st.text(buoc['noi_dung'])
    else:
        st.markdown("#### 🎪 Phòng Thí Nghiệm & Mô Phỏng Tương Tác (PhET Colorado)")
        ds_tn_mon = DANH_MUC_THI_NGHIEM.get(mon_hien_tai, {})
        if not ds_tn_mon:
            ds_tn_mon = DANH_MUC_THI_NGHIEM["🔬 Môn Vật lý (KHTN)"]
        ten_tn = st.selectbox("🔬 Chọn mô phỏng thực hành:", list(ds_tn_mon.keys()), key=f"select_tn_{key_prefix}")
        url_tn = ds_tn_mon.get(ten_tn, "")
        if url_tn:
            try:
                st.components.v1.iframe(url_tn, height=580, scrolling=True)
            except Exception:
                st.warning("⚠️ Không thể tải khung mô phỏng lúc này.")

def hien_thi_bai(mon, lop, chuong, ten_bai, data):
    if not isinstance(data, dict):
        st.warning("⚠️ Dữ liệu bài học chưa đúng định dạng.")
        return

    st.markdown(f"### 📖 {ten_bai}")
    lt, vd = str(data.get("ly_thuyet", "")).strip(), str(data.get("vi_du", "")).strip()
    ch_list = data.get("cau_hoi", [])
    bt_cb = data.get("bt_co_ban", [])
    bt_nc = data.get("bt_nang_cao", [])
    sid = lam_sach_id(f"{mon}_{lop}_{chuong}_{ten_bai}")

    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Trắc nghiệm", f"{len(ch_list)} câu")
    c2.metric("✏️ Cơ bản", f"{len(bt_cb)} bài")
    c3.metric("🔥 Nâng cao", f"{len(bt_nc)} bài")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Lý thuyết", "✏️ Cơ bản", "🔥 Nâng cao", "📝 Trắc nghiệm", "🎪 Phòng thí nghiệm"])
    
    with tab1:
        if lt:
            st.markdown(f"<div class='khung-lythuyet'>{lt}</div>
