# -*- coding: utf-8 -*-
"""
PHẦN MỀM HỌC TẬP THCS — BỘ SÁCH KẾT NỐI TRI THỨC (GDPT 2018)
Phiên bản Chống Gãy Dòng Mobile + Lock Đa Luồng + Đầy Đủ Tính Năng
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

# ==================== CẤU HÌNH TRANG & ĐIỀU HƯỚNG SỚM ====================
st.set_page_config(
    page_title="Hệ Thống Học Tập Lớp 7",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "search_jump" in st.session_state:
    item = st.session_state.pop("search_jump")
    st.session_state["che_do_sidebar"] = "📖 Học theo chuyên đề"
    st.session_state["mon_main"] = item["mon"]
    st.session_state["chuong_main"] = item["chuong"]
    st.session_state["bai_main"] = item["bai"]

# ==================== KHỞI TẠO LOCK & CACHE TOÀN CỤC ====================
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

# ==================== ĐỌC SECRETS AN TOÀN ====================
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

    ds_ten_key = [
        "GEMINI_API_KEY",
        "GEMINI_API_KEY_1",
        "GEMINI_API_KEY_2",
        "GEMINI_API_KEY_3"
    ]
    for k_name in ds_ten_key:
        k_val = get_secret(k_name)
        if k_val and str(k_val).strip() not in keys:
            keys.append(str(k_val).strip())
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

# ==================== TẢI THƯ VIỆN BỔ TRỢ ====================
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

# ==================== ĐẾM NGƯỜI DÙNG & GIỚI HẠN TẦN SUẤT ====================
def cap_nhat_nguoi_online():
    with GLOBALS["user_count_lock"]:
        if "user_id" not in st.session_state:
            st.session_state.user_id = str(uuid.uuid4())
        bo_nho = GLOBALS["online_users"]
        bo_nho[st.session_state.user_id] = time.time()
        now = time.time()
        ds_online = {
            uid: t for uid, t in bo_nho.items() if now - t < 300
        }
        bo_nho.clear()
        bo_nho.update(ds_online)
        return len(bo_nho)

def kiem_tra_gioi_han_tan_suat(cooldown_seconds=4):
    now = time.time()
    last_time = st.session_state.get("last_ai_request_time", 0.0)
    elapsed = now - last_time
    if elapsed < cooldown_seconds:
        return False, int(cooldown_seconds - elapsed) + 1
    st.session_state["last_ai_request_time"] = now
    return True, 0

# ==================== BỘ ĐỆM AI (LRU CACHE) ====================
def tao_ma_hash_cau_hoi(mon_hoc, bai_hoc, che_do, cau_hoi):
    c_clean = re.sub(r'\s+', ' ', cau_hoi.strip().lower())
    chuoi_chuan = f"{mon_hoc.strip()}_{bai_hoc.strip()}_{che_do}_{c_clean}"
    return hashlib.md5(chuoi_chuan.encode("utf-8")).hexdigest()

def luu_cache_ai(ma_hash, noi_dung):
    nd_lower = noi_dung.lower()
    tu_khoa_loi = ["bận", "quá tải", "lỗi", "chuyển sang", "bảo trì"]
    if any(k in nd_lower for k in tu_khoa_loi) or "⚠️" in noi_dung:
        return
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        cache[ma_hash] = noi_dung
        cache.move_to_end(ma_hash)
        if len(cache) > 100:
            cache.popitem(last=False)

def lay_cache_ai(ma_hash):
    with GLOBALS["ai_cache_lock"]:
        cache = GLOBALS["ai_cache"]
        if ma_hash in cache:
            cache.move_to_end(ma_hash)
            return cache[ma_hash]
    return None

# ==================== CHẤM SỐ HỌC & TRỘN TRẮC NGHIỆM ====================
def ep_kieu_so_hoc(chuoi):
    s = str(chuoi).strip().replace(" ", "")
    if not s:
        return None
    if "/" in s:
        parts = s.split("/")
        if len(parts) == 2:
            try:
                return float(parts[0]) / float(parts[1])
            except Exception:
                return None
    if re.fullmatch(r'-?\d{1,3}(?:\.\d{3})*(?:,\d+)?', s):
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None

def so_sanh_so_hoc(nd, ds_dung):
    val_x = ep_kieu_so_hoc(nd)
    for d in ds_dung:
        val_d = ep_kieu_so_hoc(d)
        if val_x is not None and val_d is not None:
            if abs(val_x - val_d) < 1e-5:
                return True
        s1 = re.sub(r'\s+', '', str(nd).lower())
        s2 = re.sub(r'\s+', '', str(d).lower())
        if s1 == s2:
            return True
    return False

def tron_dap_an_thong_minh(ch):
    da_goc = list(ch["da"])
    d_dung = da_goc[ch["d"]]
    tu_khoa_co_dinh = ["cả", "tất cả", "đáp án", "phương án", "a, b"]
    for ans in da_goc:
        txt = str(ans).lower()
        if any(k in txt for k in tu_khoa_co_dinh):
            return da_goc, ch["d"]
    random.shuffle(da_goc)
    return da_goc, da_goc.index(d_dung)

def lam_sach_id(s):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', str(s))

def sap_xep_chuong(ds_chuong):
    def lay_so(ten):
        m = re.search(r'\d+', str(ten))
        return int(m.group(0)) if m else 999
    return sorted(ds_chuong, key=lay_so)

def ghi_nhan_lich_su(tieu_de_bai, diem, dung, tong):
    if "lich_su_hoc_tap" not in st.session_state:
        st.session_state.lich_su_hoc_tap = []
    st.session_state.lich_su_hoc_tap.insert(0, {
        "bai": tieu_de_bai,
        "diem": diem,
        "dung": dung,
        "tong": tong
    })

def lam_sach_van_ban_doc(text):
    s = str(text)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 phần \2', s)
    s = s.replace(r'\times', ' nhân ').replace(r'\cdot', ' nhân ')
    s = s.replace('^2', ' bình phương ').replace('^3', ' lập phương ')
    s = re.sub(r'[$*#_`~\\{}]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def doc_to_an_toan(text, autoplay=True):
    if not HAS_TTS or not text:
        return
    try:
        clean_text = lam_sach_van_ban_doc(text)
        if clean_text:
            afp = io.BytesIO()
            gTTS(text=clean_text, lang="vi").write_to_fp(afp)
            afp.seek(0)
            st.audio(afp, format="audio/mp3", autoplay=autoplay)
    except Exception:
        pass

def trich_xuat_word_docx(file_bytes):
    try:
        with zipfile.ZipFile(io.BytesIO(file_bytes)) as z:
            xml_content = z.read("word/document.xml")
        tree = ET.fromstring(xml_content)
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        doan_van = [
            "".join([t.text for t in p.iter(f"{ns}t") if t.text])
            for p in tree.iter(f"{ns}p")
        ]
        return "\n".join([p for p in doan_van if p])
    except Exception as e:
        return f"[Lỗi đọc file Word: {e}]"

# ==================== GỌI AI AN TOÀN (CÓ THREAD LOCK) ====================
def goi_dola_toi_uu(cau_hoi):
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
            timeout=4.0
        )
        if phan_hoi.status_code == 200:
            nd = phan_hoi.json().get("noi_dung_chuan", "")
            return nd.strip() if nd else None
        return None
    except Exception:
        return None

@st.cache_resource(ttl=3600, show_spinner=False)
def lay_ds_model_kha_dung(api_key):
    uu_tien = [
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-flash",
        "gemini-1.5-pro"
    ]
    try:
        genai.configure(api_key=api_key)
        ds_hien_co = [
            m.name.replace("models/", "")
            for m in genai.list_models()
            if "generateContent" in getattr(m, "supported_generation_methods", [])
        ]
        if ds_hien_co:
            kq = [m for m in uu_tien if m in ds_hien_co]
            kq += [m for m in ds_hien_co if "gemini" in m and m not in uu_tien]
            return kq
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
            genai.configure(api_key=current_key)
            ds_models = lay_ds_model_kha_dung(current_key)

            for ten_m in ds_models:
                for attempt in range(2):
                    try:
                        m = genai.GenerativeModel(
                            model_name=ten_m,
                            system_instruction=system_instruction
                        )
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
    raise last_err

# ==================== NẠP DỮ LIỆU CÁC MÔN ====================
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

VAN_DEFAULT = {
    "Lớp 7": {
        "Chương 1: Bầu trời tuổi thơ (Truyện)": {
            "Văn bản 1: Bồng chanh đỏ (trích, Đỗ Chu)": {
                "ly_thuyet": "Truyện ngắn kể về hai anh em Hoài và Ý với tình yêu thương loài vật, thiên nhiên và những rung cảm tinh tế của tuổi thơ.",
                "vi_du": "Chi tiết thả chim bồng chanh đỏ về tự nhiên thể hiện sự thức tỉnh nhân cách và lòng nhân ái.",
                "cau_hoi": [
                    {
                        "nd": "Truyện 'Bồng chanh đỏ' của tác giả nào?",
                        "da": ["Đỗ Chu", "Tô Hoài", "Khánh Hoài", "Duy Khán"],
                        "d": 0
                    },
                    {
                        "nd": "Nhân vật chính trong truyện là ai?",
                        "da": ["Hai anh em Hoài và Ý", "Ông nội", "Côn và Bản", "Thành và Thủy"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Nêu ý nghĩa nhan đề 'Bồng chanh đỏ'?",
                        "dd": ["Biểu tượng cho vẻ đẹp thiên nhiên"],
                        "lg": "Hình ảnh trung tâm khơi gợi những cảm xúc trong trẻo."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Phân tích sự biến đổi tâm trạng của nhân vật Hoài?",
                        "dd": ["Thấu hiểu và buông bỏ"],
                        "lg": "Thể hiện sự nhân hậu, tôn trọng tự nhiên."
                    }
                ]
            },
            "Văn bản 2: Bố cục và mạch ngầm trong văn bản": {
                "ly_thuyet": "Tìm hiểu cách xây dựng cốt truyện và các lớp ý nghĩa ẩn giấu trong tác phẩm truyện.",
                "cau_hoi": [
                    {
                        "nd": "Mạch ngầm văn bản là gì?",
                        "da": ["Những suy nghĩ, cảm xúc ẩn giấu dưới lời văn", "Cốt truyện chính", "Lời thoại nhân vật"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Mạch ngầm thường được bộc lộ qua đâu?",
                        "dd": ["Chi tiết nghệ thuật"],
                        "lg": "Thông qua các chi tiết miêu tả và hành động."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Tác dụng của mạch ngầm trong truyện ngắn?",
                        "dd": ["Tăng chiều sâu"],
                        "lg": "Giúp người đọc suy ngẫm nhiều hơn."
                    }
                ]
            }
        },
        "Chương 2: Khúc tâm tình của đất nước (Thơ)": {
            "Văn bản 1: Tia nắng đầu tiên (Đức Lợi)": {
                "ly_thuyet": "Bài thơ ca ngợi vẻ đẹp thiên nhiên buổi sáng và tình cảm gia đình ấm áp.",
                "cau_hoi": [
                    {
                        "nd": "Bài thơ thuộc thể thơ nào?",
                        "da": ["Thơ tự do / 5 chữ", "Thơ lục bát", "Thơ 7 chữ", "Tất cả phương án trên"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Tia nắng đầu tiên tượng trưng cho điều gì?",
                        "dd": ["Niềm hy vọng"],
                        "lg": "Mang ý nghĩa biểu tượng sâu sắc."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Phân tích cảm xúc của nhân vật trữ tình?",
                        "dd": ["Rung động tinh tế"],
                        "lg": "Gắn kết thiên nhiên với gia đình."
                    }
                ]
            },
            "Văn bản 2: Mẹ (Đỗ Bạch Nga)": {
                "ly_thuyet": "Bài thơ khắc họa hình ảnh người mẹ tần tảo, hy sinh vì con cái.",
                "cau_hoi": [
                    {
                        "nd": "Biện pháp tu từ nổi bật trong bài thơ 'Mẹ' là gì?",
                        "da": ["Ẩn dụ / So sánh", "Nói quá", "Liệt kê"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Tình cảm của người con đối với mẹ?",
                        "dd": ["Biết ơn sâu sắc"],
                        "lg": "Thể hiện đạo lý uống nước nhớ nguồn."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Ý nghĩa hình ảnh người mẹ?",
                        "dd": ["Biểu tượng của sự hy sinh"],
                        "lg": "Là nguồn cội nuôi dưỡng tâm hồn."
                    }
                ]
            }
        },
        "Chương 3: Hành trình tri thức (Nghị luận & Thông tin)": {
            "Văn bản 1: Tự học - một cuộc du thú trường chinh": {
                "ly_thuyet": "Văn bản nghị luận bàn về tầm quan trọng và phương pháp tự học.",
                "cau_hoi": [
                    {
                        "nd": "Vấn đề nghị luận chính là gì?",
                        "da": ["Tầm quan trọng của việc tự học", "Cách đọc sách hiệu quả", "Phương pháp học ngoại ngữ"],
                        "d": 0
                    }
                ],
                "bt_co_ban": [
                    {
                        "de": "Vì sao gọi tự học là 'cuộc du thú trường chinh'?",
                        "dd": ["Khám phá tri thức dài lâu"],
                        "lg": "Phép ẩn dụ độc đáo."
                    }
                ],
                "bt_nang_cao": [
                    {
                        "de": "Rút ra bài học cho bản thân?",
                        "dd": ["Chủ động, kiên trì"],
                        "lg": "Tự học quyết định thành công."
                    }
                ]
            }
        }
    }
}

try:
    from data_van import VAN as VAN_EXT
    if VAN_EXT and "Lớp 7" in VAN_EXT:
        for ch_k, ch_v in VAN_DEFAULT["Lớp 7"].items():
            if ch_k not in VAN_EXT["Lớp 7"]:
                VAN_EXT["Lớp 7"][ch_k] = ch_v
        VAN = VAN_EXT
    else:
        VAN = VAN_DEFAULT
except ImportError:
    VAN = VAN_DEFAULT

DATABASE = {
    "📐 Môn Toán": TOAN,
    "🔬 Môn Vật lý (KHTN)": VATLY,
    "🧪 Môn Hóa học (KHTN)": HOA if HOA else {"Lớp 7": {"Chương 1: Đang cập nhật": {}}},
    "📖 Môn Ngữ Văn": VAN
}

DANH_MUC_THI_NGHIEM = {
    "📐 Môn Toán": {
        "⚖️ Cân bằng phương trình & Biểu thức đại số": "https://phet.colorado.edu/sims/html/equality-explorer/latest/equality-explorer_vi.html"
    },
    "🔬 Môn Vật lý (KHTN)": {
        "💡 Khúc xạ & Phản xạ ánh sáng (Quang học 7)": "https://phet.colorado.edu/sims/html/bending-light/latest/bending-light_vi.html"
    },
    "🧪 Môn Hóa học (KHTN)": {
        "⚛️ Xây dựng cấu tạo Nguyên tử": "https://phet.colorado.edu/sims/html/build-an-atom/latest/build-an-atom_vi.html",
        "🧬 Lắp ghép Phân tử": "https://phet.colorado.edu/sims/html/build-a-molecule/latest/build-a-molecule_vi.html",
        "⚖️ Cân bằng Phương trình": "https://phet.colorado.edu/sims/html/balancing-chemical-equations/latest/balancing-chemical-equations_vi.html",
        "🧪 Đo nồng độ dung dịch": "https://phet.colorado.edu/sims/html/concentration/latest/concentration_vi.html"
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
        "bo_cuc": [
            {"phan": "Mở đầu", "noi_dung": "Giới thiệu tổ chim bồng chanh đỏ."},
            {"phan": "Diễn biến", "noi_dung": "Cuộc mạo hiểm leo lên bờ vực."},
            {"phan": "Cao trào", "noi_dung": "Quyết định thả chim về tự nhiên."}
        ],
        "y_nghia": "Bồi dưỡng tình yêu thiên nhiên và ý thức bảo vệ môi trường."
    },
    "🎭 Biểu đồ Tương tác Nhân vật": {
        "nhan_vat": "Nhân vật Hoài",
        "dac_diem": "Giàu tình cảm, ham khám phá, nhân hậu.",
        "hanh_vi_tieu_bieu": "Trèo cây xem chim; ngăn em bắt chim.",
        "dien_bien_tam_ly": [
            {"giai_doan": "Đầu truyện", "tam_trang": "Tò mò, háo hức."},
            {"giai_doan": "Cuối truyện", "tam_trang": "Thức tỉnh, buông bỏ."}
        ]
    },
    "🕸️ Sơ đồ Quan hệ Nhân vật": {
        "tac_pham": "Quan hệ trong 'Bồng chanh đỏ'",
        "quan_he": [
            {"tu_khoa": "Anh Hoài ↔️ Em Ý", "loai": "Đồng hành", "mo_ta": "Cùng chia sẻ bí mật tuổi thơ."},
            {"tu_khoa": "Con người ↔️ Thiên nhiên", "loai": "Thấu hiểu", "mo_ta": "Sự hòa hợp với tự nhiên."}
        ]
    },
    "✍️ Thực hành Luyện từ & Ngữ pháp": {
        "chu_de": "Biện pháp tu từ lớp 7",
        "cau_hoi_mau": [
            {"cau": "Đôi cánh chim đỏ rực như ngọn lửa.", "loai": "So sánh", "phan_tich": "Làm hình ảnh thêm sinh động, rực rỡ."}
        ]
    },
    "📝 Trạm Lập dàn ý bài văn": {
        "the_loai": "Biểu cảm về tác phẩm văn học",
        "dan_y": [
            {"buoc": "Mở bài", "noi_dung": "Giới thiệu tác phẩm và tác giả."},
            {"buoc": "Thân bài", "noi_dung": "Trình bày cảm xúc về nội dung và nghệ thuật."},
            {"buoc": "Kết bài", "noi_dung": "Khẳng định giá trị tác phẩm."}
        ]
    }
}

# ==================== GIAO DIỆN SIDEBAR ====================
with st.sidebar:
    st.markdown("## 🎓 KẾT NỐI TRI THỨC")
    dark_mode = st.toggle("🌙 Chế độ tối", key="dark_mode_toggle")
    st.markdown(f"🟢 **Đang trực tuyến: {cap_nhat_nguoi_online()}**")

    if not GEMINI_KEYS:
        st.warning("⚠️ Chưa có API Key, chạy ở chế độ Mẫu.")

    st.divider()

    ds_che_do = [
        "🏠 Trang chủ / Hướng dẫn",
        "🔍 Tra cứu / Tìm kiếm",
        "📖 Học theo chuyên đề",
        "📝 Phòng thi / Kiểm tra",
        "🎪 Phòng thí nghiệm ảo",
        "⚙️ Trạm Nạp Dữ Liệu"
    ]
    che_do = st.radio("⚙️ Chức năng:", ds_che_do, key="che_do_sidebar")

    if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra"]:
        mon = st.radio("👉 Chọn môn học:", list(DATABASE.keys()), key="mon_main")
    else:
        mon = che_do

    if "lich_su_hoc_tap" in st.session_state and st.session_state.lich_su_hoc_tap:
        st.divider()
        st.markdown("### 📊 Lịch sử học tập")
        so_bai = len(st.session_state.lich_su_hoc_tap)
        tb = sum(i["diem"] for i in st.session_state.lich_su_hoc_tap) / so_bai
        st.metric("Điểm TB", f"{tb:.1f}", f"{so_bai} bài")

# ==================== CẤU HÌNH CSS ====================
if dark_mode:
    st.markdown("""
    <style>
        .stApp { background-color: #0F172A; color: #F1F5F9; }
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], footer { display: none !important; }
        .hero-banner {
            background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
            color: #F8FAFC; padding: 1.5rem; border-radius: 12px;
            margin-bottom: 1.5rem;
        }
        .hero-title { font-size: 1.5rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 0.95rem; opacity: 0.9; margin-top: 0.3rem; color: #CBD5E1 !important; }
        .card-home {
            background-color: #1E293B; border: 1px solid #334155;
            padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem; color: #F1F5F9;
        }
        .khung-lythuyet {
            background-color: #1E293B; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #3B82F6; margin-bottom: 1rem;
        }
        .khung-vidu {
            background-color: #27272A; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #F59E0B; margin-bottom: 1rem;
        }
        .dung { color: #34D399; font-weight: bold; }
        .sai { color: #F87171; font-weight: bold; }
        .diem-thi {
            font-size: 1.6rem; color: #F87171; text-align: center;
            padding: 1.2rem; border: 2px dashed #EF4444; border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .main .block-container { padding-top: 1.2rem; max-width: 95%; }
        [data-testid="stToolbarActions"], footer { display: none !important; }
        .hero-banner {
            background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
            color: white; padding: 1.5rem; border-radius: 12px;
            margin-bottom: 1.5rem;
        }
        .hero-title { font-size: 1.5rem; font-weight: 700; margin: 0; color: #FFFFFF !important; }
        .hero-sub { font-size: 0.95rem; opacity: 0.9; margin-top: 0.3rem; color: #E2E8F0 !important; }
        .card-home {
            background-color: #F8FAFC; border: 1px solid #E2E8F0;
            padding: 1.4rem; border-radius: 12px; margin-bottom: 1rem;
        }
        .khung-lythuyet {
            background-color: #EFF6FF; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #2563EB; margin-bottom: 1rem;
        }
        .khung-vidu {
            background-color: #FFFBEB; padding: 1.2rem; border-radius: 10px;
            border-left: 6px solid #F59E0B; margin-bottom: 1rem;
        }
        .dung { color: #059669; font-weight: bold; }
        .sai { color: #DC2626; font-weight: bold; }
        .diem-thi {
            font-size: 1.6rem; color: #E11D48; text-align: center;
            padding: 1.2rem; border: 2px dashed #F43F5E; border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# ==================== HIỂN THỊ PHÒNG THÍ NGHIỆM & BÀI HỌC ====================
def hien_thi_phong_thi_nghiem(mon_hien_tai, key_prefix="lab"):
    if mon_hien_tai == "📖 Môn Ngữ Văn":
        ds_modul = list(DANH_MUC_THI_NGHIEM["📖 Môn Ngữ Văn"].keys())
        chon_modul = st.selectbox(
            "📚 Chọn Mô-đun Tương tác Ngữ Văn:",
            ds_modul,
            key=f"select_modul_{key_prefix}"
        )
        st.divider()
        if "Bản đồ Cấu trúc" in chon_modul:
            data = DATA_LAB_NGU_VAN["🗺️ Bản đồ Cấu trúc & Bối cảnh"]
            st.markdown(f"### 🗺️ {data['tieu_de']}")
            st.info(f"⏳ **Hoàn cảnh sáng tác:** {data['hoan_canh']}")
            for item in data["bo_cuc"]:
                with st.expander(f"🔹 {item['phan']}"):
                    st.write(item["noi_dung"])
            st.success(f"💡 **Ý nghĩa nhân văn:** {data['y_nghia']}")
        elif "Biểu đồ Tương tác" in chon_modul:
            data = DATA_LAB_NGU_VAN["🎭 Biểu đồ Tương tác Nhân vật"]
            st.markdown(f"### 🎭 {data['nhan_vat']}")
            st.markdown(f"⭐ **Đặc điểm:** {data['dac_diem']}")
            st.markdown(f"🎯 **Hành vi:** {data['hanh_vi_tieu_bieu']}")
            st.markdown("#### 📈 Diễn biến tâm lý:")
            for stage in data["dien_bien_tam_ly"]:
                st.markdown(f"* **{stage['giai_doan']}:** {stage['tam_trang']}")
        elif "Sơ đồ Quan hệ" in chon_modul:
            data = DATA_LAB_NGU_VAN["🕸️ Sơ đồ Quan hệ Nhân vật"]
            st.markdown(f"### 🕸️ {data['tac_pham']}")
            for idx, rel in enumerate(data["quan_he"], 1):
                with st.expander(f"{idx}. {rel['tu_khoa']} — [{rel['loai']}]"):
                    st.write(rel["mo_ta"])
        elif "Luyện từ & Ngữ pháp" in chon_modul:
            data = DATA_LAB_NGU_VAN["✍️ Thực hành Luyện từ & Ngữ pháp"]
            st.markdown(f"### ✍️ {data['chu_de']}")
            for idx, bai in enumerate(data["cau_hoi_mau"], 1):
                st.markdown(f"**Câu {idx}:** `{bai['cau']}`")
                st.markdown(f"👉 **Phân loại:** **{bai['loai']}**")
                st.info(f"💡 **Giải thích:** {bai['phan_tich']}")
        elif "Lập dàn ý" in chon_modul:
            data = DATA_LAB_NGU_VAN["📝 Trạm Lập dàn ý bài văn"]
            st.markdown(f"### 📝 Lập dàn ý: {data['the_loai']}")
            for buoc in data["dan_y"]:
                with st.expander(f"📋 {buoc['buoc']}"):
                    st.text(buoc["noi_dung"])
    else:
        st.markdown("#### 🎪 Phòng Thí Nghiệm & Mô Phỏng (PhET Colorado)")
        ds_tn_mon = DANH_MUC_THI_NGHIEM.get(mon_hien_tai, {})
        if not ds_tn_mon:
            ds_tn_mon = DANH_MUC_THI_NGHIEM["🔬 Môn Vật lý (KHTN)"]
        ten_tn = st.selectbox(
            "🔬 Chọn mô phỏng thực hành:",
            list(ds_tn_mon.keys()),
            key=f"select_tn_{key_prefix}"
        )
        url_tn = ds_tn_mon[ten_tn]
        if url_tn:
            st.components.v1.iframe(url_tn, height=580, scrolling=True)

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

    ds_tabs = [
        "📚 Lý thuyết",
        "✏️ Cơ bản",
        "🔥 Nâng cao",
        "📝 Trắc nghiệm",
        "🎪 Phòng thí nghiệm"
    ]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(ds_tabs)

    with tab1:
        if lt:
            st.markdown(
                f"""<div class="khung-lythuyet">{lt}</div>""",
                unsafe_allow_html=True
            )
        if vd:
            st.markdown(
                f"""<div class="khung-vidu">{vd}</div>""",
                unsafe_allow_html=True
            )

    with tab2:
        if not bt_cb:
            st.info("Chưa có bài tập.")
        else:
            for i, bt in enumerate(bt_cb, 1):
                with st.expander(f"Bài {i}: {bt['de']}"):
                    if "Ngữ Văn" in mon:
                        if st.button("💡 Xem gợi ý", key=f"btn_goiy_cb_{sid}_{i}"):
                            goi_y = bt.get("lg", bt.get("dd", [""])[0])
                            st.info(f"📝 **Gợi ý:** {goi_y}")
                    else:
                        ans = st.text_input("Nhập kết quả:", key=f"cb_{sid}_{i}")
                        if st.button("Kiểm tra", key=f"btn_cb_{sid}_{i}"):
                            if not ans.strip():
                                st.warning("⚠️ Nhập đáp án trước!")
                            elif so_sanh_so_hoc(ans, bt["dd"]):
                                st.markdown(
                                    """<p class="dung">✅ Chính xác!</p>""",
                                    unsafe_allow_html=True
                                )
                            else:
                                da_mau = bt["dd"][0]
                                st.markdown(
                                    f"""<p class="sai">❌ Sai. Gợi ý: {da_mau}</p>""",
                                    unsafe_allow_html=True
                                )

    with tab3:
        if not bt_nc:
            st.info("Chưa có bài tập nâng cao.")
        else:
            for i, nc in enumerate(bt_nc, 1):
                with st.expander(f"Bài nâng cao {i}: {nc['de'][:60]}..."):
                    st.markdown(f"**Đề bài:** {nc['de']}")
                    if "Ngữ Văn" in mon:
                        if st.button("💡 Xem gợi ý", key=f"btn_goiy_nc_{sid}_{i}"):
                            goi_y = nc.get("lg", nc.get("dd", [""])[0])
                            st.info(f"📝 **Gợi ý:** {goi_y}")
                    else:
                        ans = st.text_input("Nhập kết quả:", key=f"nc_{sid}_{i}")
                        if st.button("Kiểm tra", key=f"btn_nc_{sid}_{i}"):
                            if so_sanh_so_hoc(ans, nc["dd"]):
                                st.success("🎉 Chính xác!")
                            else:
                                st.error(f"❌ Gợi ý: {nc['dd'][0]}")
                        if st.checkbox("📖 Xem lời giải", key=f"lg_{sid}_{i}"):
                            st.success(f"**Lời giải:** {nc.get('lg', '')}")

    with tab4:
        if len(ch_list) == 0:
            st.info("Chưa có trắc nghiệm.")
        else:
            if st.button("🔄 Làm mới đề", key=f"btn_rf_{sid}"):
                st.session_state[f"de_{sid}"] = None
            if f"de_{sid}" not in st.session_state or st.session_state[f"de_{sid}"] is None:
                de_tron = []
                for ch in ch_list:
                    da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                    nd_ch = ch.get("nd") or ch.get("de")
                    de_tron.append({"nd": nd_ch, "da": da_moi, "d": vt_moi})
                st.session_state[f"de_{sid}"] = de_tron

            with st.form(f"f_{sid}"):
                tl = {}
                for i, ch in enumerate(st.session_state[f"de_{sid}"], 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl[i] = st.radio(
                        "Chọn:",
                        ch["da"],
                        key=f"r_{sid}_{i}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    st.markdown("---")
                if st.form_submit_button("🚀 Nộp bài", type="primary"):
                    de_hien_tai = st.session_state[f"de_{sid}"]
                    dung = sum(
                        1 for i, ch in enumerate(de_hien_tai, 1)
                        if tl[i] == ch["da"][ch["d"]]
                    )
                    diem = dung / len(ch_list) * 10
                    ghi_nhan_lich_su(f"Trắc nghiệm: {ten_bai}", diem, dung, len(ch_list))
                    st.markdown(
                        f"""<div class="diem-thi">🏆 ĐIỂM: {diem:.1f} / 10</div>""",
                        unsafe_allow_html=True
                    )
                    for i, ch in enumerate(de_hien_tai, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl[i] != da_dung:
                            st.error(f"Câu {i} sai. Đúng là: {da_dung}")
                        else:
                            st.success(f"Câu {i}: Đúng")

    with tab5:
        hien_thi_phong_thi_nghiem(mon, key_prefix=f"tab_{sid}")

# ==================== ĐIỀU HƯỚNG MÀN HÌNH CHÍNH ====================
bai_dang_hoc = ""
du_lieu_bai_hien_tai = {}

if che_do == "🏠 Trang chủ / Hướng dẫn":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🎓 HỆ THỐNG HỌC TẬP THCS — KẾT NỐI TRI THỨC (LỚP 7)</p>
        <p class="hero-sub">Không gian ôn luyện thông minh đa môn học</p>
    </div>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.markdown("""
    <div class="card-home">
        <h3>🌟 Tính năng nổi bật</h3>
        <p>Học tập chuyên đề, Tra cứu thông minh, Mô phỏng tương tác.</p>
    </div>
    """, unsafe_allow_html=True)
    c2.markdown("""
    <div class="card-home">
        <h3>💬 Gia Sư AI An Toàn</h3>
        <p>Bộ đệm tốc độ cao, luân phiên khóa API chống sập.</p>
    </div>
    """, unsafe_allow_html=True)

elif che_do == "🔍 Tra cứu / Tìm kiếm":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🔍 Tra Cứu & Tìm Kiếm Tri Thức</p>
    </div>
    """, unsafe_allow_html=True)
    tu_khoa = st.text_input("🔎 Nhập từ khóa:")
    if tu_khoa.strip():
        kw = tu_khoa.strip().lower()
        ket_qua_tim = []
        for t_mon, l_dict in DATABASE.items():
            for lop, c_dict in l_dict.items():
                for chuong, b_dict in c_dict.items():
                    for t_bai, data in b_dict.items():
                        lt_txt = data.get("ly_thuyet", "").lower()
                        if kw in t_bai.lower() or kw in lt_txt:
                            ket_qua_tim.append({
                                "mon": t_mon,
                                "chuong": chuong,
                                "bai": t_bai
                            })
        st.markdown(f"### 📋 Kết quả: {len(ket_qua_tim)}")
        for idx, item in enumerate(ket_qua_tim, 1):
            tieu_de_exp = f"{idx}. [{item['mon']}] {item['chuong']} - {item['bai']}"
            with st.expander(tieu_de_exp):
                if st.button("Mở bài học", key=f"btn_jump_{idx}"):
                    st.session_state["search_jump"] = item
                    st.rerun()

elif che_do == "⚙️ Trạm Nạp Dữ Liệu":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">⚙️ Trạm Nạp Dữ Liệu Tự Động (Auto-Parser)</p>
    </div>
    """, unsafe_allow_html=True)
    mk = st.text_input("🔑 Mật khẩu Admin:", type="password")

    if not ADMIN_PASS:
        st.error("⚠️ Hệ thống chưa thiết lập ADMIN_PASSWORD trong Secrets.")
    elif mk and hmac.compare_digest(mk, ADMIN_PASS):
        st.success("Xác thực thành công. Tính năng nạp file đang mở...")
        tab_upfile, tab_paste = st.tabs(["📁 Tải File Lên", "📝 Dán Văn Bản Thô"])
        danh_sach_files = []
        with tab_upfile:
            uploaded_files = st.file_uploader(
                "Chọn file (docx, pdf, ảnh, txt):",
                type=["docx", "pdf", "png", "jpg", "jpeg", "txt"],
                accept_multiple_files=True
            )
            if uploaded_files:
                danh_sach_files = uploaded_files
        with tab_paste:
            raw_text = st.text_area("Dán nội dung văn bản gốc vào đây:", height=220)

        PROMPT_PARSER = (
            'Chuyển nội dung thành Dictionary Python chuẩn gồm '
            '"ly_thuyet", "vi_du", "cau_hoi", "bt_co_ban", "bt_nang_cao". '
            'Chỉ in code Python.'
        )
        if st.button("⚡ Bóc tách dữ liệu", type="primary", use_container_width=True):
            if not danh_sach_files and not raw_text.strip():
                st.warning("⚠️ Vui lòng tải file hoặc dán văn bản!")
            else:
                with st.spinner("🤖 Trợ lý AI đang phân tích cấu trúc..."):
                    try:
                        payload = []
                        for f in danh_sach_files:
                            if f.name.endswith(".docx"):
                                payload.append(trich_xuat_word_docx(f.read()))
                            elif f.name.endswith(".pdf"):
                                payload.append({"mime_type": "application/pdf", "data": f.read()})
                            elif f.name.endswith((".png", ".jpg", ".jpeg")) and HAS_PIL:
                                payload.append(Image.open(io.BytesIO(f.read())))
                            else:
                                payload.append(f.read().decode("utf-8", errors="ignore"))
                        if raw_text.strip():
                            payload.append(raw_text.strip())
                        ket_qua = goi_gemini_an_toan(payload, system_instruction=PROMPT_PARSER)
                        kq_clean = ket_qua.replace("```python", "").replace("```json", "").replace("```", "").strip()
                        st.session_state["parsed_code_result"] = kq_clean
                    except Exception as e:
                        st.error(f"❌ Lỗi xử lý: {e}")

        if st.session_state.get("parsed_code_result"):
            code_out = st.session_state["parsed_code_result"]
            st.success("✅ Bóc tách dữ liệu thành công!")
            st.download_button(
                "💾 Tải Code về máy (.py)",
                data=code_out.encode("utf-8"),
                file_name="data_moi.py",
                mime="text/x-python"
            )
            st.code(code_out, language="python")
    elif mk:
        st.error("Sai mật khẩu!")

elif che_do == "🎪 Phòng thí nghiệm ảo":
    st.markdown("""
    <div class="hero-banner">
        <p class="hero-title">🎪 Phòng Thí Nghiệm & Mô Phỏng Tương Tác</p>
    </div>
    """, unsafe_allow_html=True)
    ds_mon_lab = [
        "📖 Môn Ngữ Văn",
        "🔬 Môn Vật lý (KHTN)",
        "🧪 Môn Hóa học (KHTN)",
        "📐 Môn Toán"
    ]
    mon_lab = st.selectbox("🔬 Chọn môn học thực hành:", ds_mon_lab)
    hien_thi_phong_thi_nghiem(mon_lab, key_prefix="main_lab")

elif che_do == "📖 Học theo chuyên đề":
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">{mon} — Chương trình GDPT 2018 (Kết Nối Tri Thức)</p>
        <p class="hero-sub">Hệ thống học tập thông minh lớp 7</p>
    </div>
    """, unsafe_allow_html=True)

    lop_dict = DATABASE[mon]
    if not lop_dict:
        st.warning("⚠️ Dữ liệu đang được cập nhật...")
    else:
        c_lop, c_chuong, c_bai = st.columns([1, 2, 2])
        lop = c_lop.selectbox("Khối:", list(lop_dict.keys()), key="s_lop")
        chuong_dict = lop_dict[lop]
        ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))
        ch_saved = st.session_state.get("chuong_main")
        idx_c = ds_chuong.index(ch_saved) if ch_saved in ds_chuong else 0
        chuong = c_chuong.selectbox("Chương:", ds_chuong, index=idx_c, key="s_chuong")

        bai_dict = chuong_dict[chuong]
        ds_bai = list(bai_dict.keys())
        b_saved = st.session_state.get("bai_main")
        idx_b = ds_bai.index(b_saved) if b_saved in ds_bai else 0
        bai = c_bai.selectbox("Bài:", ds_bai, index=idx_b, key="s_bai")

        bai_dang_hoc = f"{chuong} - {bai}"
        du_lieu_bai_hien_tai = bai_dict[bai]

        st.markdown("---")
        hien_thi_bai(mon, lop, chuong, bai, du_lieu_bai_hien_tai)

elif che_do == "📝 Phòng thi / Kiểm tra":
    st.markdown(f"""
    <div class="hero-banner">
        <p class="hero-title">⏱️ Phòng Thi Thử & Kiểm Tra Định Kì — {mon}</p>
    </div>
    """, unsafe_allow_html=True)
    lop_dict = DATABASE[mon]
    if lop_dict:
        lop = st.selectbox("Khối:", list(lop_dict.keys()), key="s_lop_thi")
        chuong_dict = lop_dict[lop]
        ds_chuong = sap_xep_chuong(list(chuong_dict.keys()))

        col1, col2 = st.columns([1, 2])
        ds_loai_de = [
            "Kiểm tra 15 phút (10 câu)",
            "Giữa kì (20 câu)",
            "Học kì (40 câu)"
        ]
        with col1:
            loai_de = st.selectbox("Cấu trúc đề:", ds_loai_de)
        with col2:
            chuong_chon = st.multiselect("Chọn chương:", ds_chuong, default=ds_chuong)

        mapping_cau = {
            "Kiểm tra 15 phút (10 câu)": 10,
            "Giữa kì (20 câu)": 20,
            "Học kì (40 câu)": 40
        }
        if st.button("🚀 TẠO ĐỀ THI LẠI / MỚI", type="primary"):
            st.session_state[f"dethi_{mon}_{lop}"] = None

        if st.session_state.get(f"dethi_{mon}_{lop}") is None:
            all_questions = []
            for c in chuong_chon:
                for b, data in chuong_dict[c].items():
                    all_questions.extend(data.get("cau_hoi", []))
            if not all_questions:
                st.error("❌ Chưa có câu hỏi trong chương này!")
            else:
                so_luong = min(mapping_cau[loai_de], len(all_questions))
                ds_chon = random.sample(all_questions, so_luong)
                de_tron_thi = []
                for ch in ds_chon:
                    da_moi, vt_moi = tron_dap_an_thong_minh(ch)
                    nd_ch = ch.get("nd") or ch.get("de")
                    de_tron_thi.append({"nd": nd_ch, "da": da_moi, "d": vt_moi})
                st.session_state[f"dethi_{mon}_{lop}"] = de_tron_thi

        if st.session_state.get(f"dethi_{mon}_{lop}"):
            de_thi = st.session_state[f"dethi_{mon}_{lop}"]
            with st.form(f"form_thi_{mon}_{lop}"):
                tl_thi = {}
                for i, ch in enumerate(de_thi, 1):
                    st.markdown(f"**Câu {i}:** {ch['nd']}")
                    tl_thi[i] = st.radio(
                        f"Đ/á {i}:",
                        ch["da"],
                        key=f"thi_{mon}_{lop}_{i}",
                        index=None,
                        label_visibility="collapsed"
                    )
                    st.markdown("---")
                if st.form_submit_button("🎯 NỘP BÀI", type="primary"):
                    dung = sum(
                        1 for i, ch in enumerate(de_thi, 1)
                        if tl_thi[i] == ch["da"][ch["d"]]
                    )
                    diem = dung / len(de_thi) * 10
                    ghi_nhan_lich_su(f"Thi thử ({mon})", diem, dung, len(de_thi))
                    st.markdown(
                        f"""<div class="diem-thi">🏆 ĐIỂM: {diem:.1f} / 10</div>""",
                        unsafe_allow_html=True
                    )
                    for i, ch in enumerate(de_thi, 1):
                        da_dung = ch["da"][ch["d"]]
                        if tl_thi[i] != da_dung:
                            st.error(f"❌ Câu {i}: Sai (Đúng: **{da_dung}**)")

# ==================== KHU VỰC GIA SƯ AI ====================
if che_do in ["📖 Học theo chuyên đề", "📝 Phòng thi / Kiểm tra", "🎪 Phòng thí nghiệm ảo"]:
    st.divider()
    st.header("💬 Gia sư AI 24/7")

    col1, col2, col3, col4 = st.columns([2.2, 1, 1.8, 1])
    with col1:
        mon_ai = st.radio(
            "Môn:",
            ["Toán", "Vật Lý", "Hóa Học", "Ngữ Văn"],
            horizontal=True,
            label_visibility="collapsed"
        )
    with col2:
        tu_dong_doc = st.checkbox("🔊 Đọc to", value=True)
    with col3:
        nguon_ai = st.selectbox(
            "Nguồn:",
            ["⚡ Gemini", "🤝 Dola -> Gemini"],
            label_visibility="collapsed"
        )
    with col4:
        if st.button("🗑️ Xóa chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    sys_prompt = (
        f"Bạn là gia sư {mon_ai} lớp 7 sách Kết Nối Tri Thức. "
        f"Đang học: {bai_dang_hoc}. Gợi mở từng bước, không giải hộ hoàn toàn."
    )
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    img_pil, btn_gui_anh = None, False
    if HAS_PIL:
        with st.expander("📸 Mắt thần AI — Gửi ảnh chụp đề bài", expanded=False):
            file_anh = st.file_uploader(
                "Tải ảnh:",
                type=["png", "jpg", "jpeg"],
                key="uploader_anh_giasu"
            )
            if file_anh:
                img_pil = Image.open(file_anh)
                st.image(img_pil, width=280)
                btn_gui_anh = st.button("🔍 Gửi ảnh cho Gia sư", type="primary")

    img_gui = img_pil if btn_gui_anh else None
    text_mic = (
        speech_to_text(language="vi-VN", start_prompt="🔴 NÓI", stop_prompt="⏹️ DỪNG", just_once=True, key="STT")
        if HAS_MIC else None
    )
    prompt = (
        "Thầy/cô xem giúp em bài tập trong ảnh với ạ!"
        if btn_gui_anh else (text_mic or st.chat_input("Hỏi gia sư..."))
    )

    if prompt:
        if not GEMINI_KEYS:
            st.error("⚠️ Hệ thống chưa được cấu hình API Key trong phần Secrets.")
        else:
            ok, giay = kiem_tra_gioi_han_tan_suat()
            if not ok:
                st.warning(f"⏳ Chờ {giay}s rồi hỏi tiếp. Câu hỏi chưa gửi: '{prompt}'")
            else:
                with st.chat_message("user"):
                    if img_gui:
                        st.image(img_gui, width=250)
                    st.markdown(prompt)
                st.session_state.chat_history.append({"role": "user", "content": prompt})

                with st.chat_message("assistant"):
                    is_first = (len(st.session_state.chat_history) <= 2) and not img_gui
                    h_key = tao_ma_hash_cau_hoi(mon_ai, bai_dang_hoc, nguon_ai, prompt) if is_first else None
                    ans_cached = lay_cache_ai(h_key) if h_key else None

                    if ans_cached:
                        st.markdown(ans_cached)
                        st.session_state.chat_history.append({"role": "assistant", "content": ans_cached})
                        doc_to_an_toan(ans_cached, autoplay=tu_dong_doc)
                    else:
                        g_hist = [
                            {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]}
                            for m in st.session_state.chat_history[:-1]
                        ]
                        luu_kq = ""
                        try:
                            with st.spinner("🤖 Gia sư AI đang suy nghĩ..."):
                                payload = [prompt, img_gui] if img_gui else prompt
                                if "Dola" in nguon_ai and not img_gui:
                                    d_nd = goi_dola_toi_uu(prompt)
                                    if d_nd:
                                        cau_truyen = f"Chuẩn SGK: {d_nd}\nDiễn giải câu: {prompt}"
                                        luu_kq = goi_gemini_an_toan(cau_truyen, sys_prompt, g_hist)
                                    else:
                                        luu_kq = goi_gemini_an_toan(payload, sys_prompt, g_hist)
                                else:
                                    luu_kq = goi_gemini_an_toan(payload, sys_prompt, g_hist)
                                st.markdown(luu_kq)
                        except Exception:
                            luu_kq = "⚠️ Đường truyền AI đang bận xử lý, em thử lại câu hỏi sau vài giây nhé."
                            st.error(luu_kq)

                        st.session_state.chat_history.append({"role": "assistant", "content": luu_kq})
                        if h_key:
                            luu_cache_ai(h_key, luu_kq)
                        if luu_kq and "⚠️" not in luu_kq:
                            doc_to_an_toan(luu_kq, autoplay=tu_dong_doc)
