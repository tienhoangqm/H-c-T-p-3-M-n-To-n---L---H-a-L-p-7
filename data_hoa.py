# -*- coding: utf-8 -*-
"""
NGÂN HÀNG DỮ LIỆU MÔN HÓA HỌC (KHTN 7) — Bộ sách Kết nối tri thức với cuộc sống
Cấu trúc bám theo SGK KHTN 7:
  Chương 1: Nguyên tử. Sơ lược về bảng tuần hoàn các nguyên tố hóa học (Bài 2, 3, 4)
  Chương 2: Phân tử. Liên kết hóa học (Bài 5, 6, 7)
  + Mỗi chương có một bài "Ôn tập & nâng cao" dành cho học sinh khá giỏi.

Nội dung do giáo viên biên soạn lại bằng lời của mình (không chép nguyên văn SGK).

HƯỚNG DẪN NHẬP LIỆU CHO GIÁO VIÊN
- Câu trắc nghiệm: TN(đề, [các phương án], chỉ số đáp án đúng (đếm từ 0), giải thích, mức độ)
    mức độ: "biet" (Biết) | "hieu" (Hiểu) | "van_dung" (Vận dụng)
- Bài tập:        BT(đề, [đáp án chấp nhận], giải thích=..., goi_y=..., loi_giai=..., tu_luan=...)
    + Đáp án là số hoặc từ ngắn (vd: "16", "Na") -> app tự chấm khi học sinh nhập.
    + Có thể ghi nhiều cách viết được chấp nhận: ["Na", "Sodium", "Natri"].
    + Đáp án là câu dài hoặc cần trình bày -> đặt tu_luan=True: học sinh tự viết rồi
      bấm "Xem đáp án" để đối chiếu.
- Khối lượng nguyên tử dùng trong bài: H=1, C=12, N=14, O=16, Na=23, Mg=24, Al=27,
  P=31, S=32, Cl=35,5, K=39, Ca=40, Fe=56, Cu=64 (amu).
"""


def TN(nd, da, d, gt="", md="biet"):
    """Một câu trắc nghiệm nhiều lựa chọn."""
    return {"nd": nd, "da": da, "d": d, "gt": gt, "md": md}


def BT(de, dd, giai_thich="", goi_y="", loi_giai="", tu_luan=False):
    """Một bài tập (cơ bản hoặc nâng cao)."""
    bai = {"de": de, "dd": dd if isinstance(dd, list) else [dd]}
    if giai_thich:
        bai["gt"] = giai_thich
    if goi_y:
        bai["hd"] = goi_y
    if loi_giai:
        bai["lg"] = loi_giai
    if tu_luan:
        bai["kieu"] = "tu_luan"
    return bai


HOA = {}
H7 = {}

# ======================================================================
# CHƯƠNG 1: NGUYÊN TỬ. SƠ LƯỢC VỀ BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC
# ======================================================================
C1 = {}

# ---------------------------- BÀI 2 ----------------------------------
C1["Bài 2: Nguyên tử"] = {
    "ly_thuyet": """📌 1. NGUYÊN TỬ LÀ GÌ?
- Mọi vật quanh ta đều được tạo nên từ những hạt vô cùng nhỏ gọi là nguyên tử.
- Nguyên tử trung hòa về điện.

📌 2. MÔ HÌNH NGUYÊN TỬ RUTHERFORD – BOHR (Rơ-dơ-pho – Bo)
- Ở tâm là hạt nhân mang điện tích dương.
- Xung quanh hạt nhân là các electron mang điện tích âm, chuyển động theo từng lớp (quỹ đạo) xác định, tạo thành lớp vỏ nguyên tử.

📌 3. CẤU TẠO NGUYÊN TỬ
- Hạt nhân gồm: proton (kí hiệu p, điện tích +1) và neutron (kí hiệu n, không mang điện).
- Vỏ nguyên tử gồm: các electron (kí hiệu e, điện tích –1).
- Trong một nguyên tử: số p = số e  ⇒  nguyên tử trung hòa về điện.

📌 4. SỰ SẮP XẾP ELECTRON VÀO CÁC LỚP
- Electron được xếp lần lượt từ lớp trong (gần hạt nhân) ra lớp ngoài.
- Lớp thứ nhất chứa tối đa 2 electron; lớp thứ hai chứa tối đa 8 electron.
- Với 20 nguyên tố đầu tiên: lớp thứ ba nhận tối đa 8 electron rồi mới xếp sang lớp thứ tư.
  Ví dụ: Oxygen (8e): 2, 6 — Sodium (11e): 2, 8, 1 — Calcium (20e): 2, 8, 8, 2.

📌 5. KHỐI LƯỢNG NGUYÊN TỬ
- Đơn vị: amu (atomic mass unit). 1 amu ≈ 1,6605 × 10⁻²⁴ gam.
- Khối lượng proton ≈ 1 amu; neutron ≈ 1 amu; electron ≈ 0,00055 amu (rất nhỏ, có thể bỏ qua).
- Vì vậy: Khối lượng nguyên tử ≈ số p + số n (amu). Khối lượng nguyên tử tập trung chủ yếu ở hạt nhân.""",

    "vi_du": """💡 VÍ DỤ 1: Xác định số hạt trong nguyên tử
Nguyên tử Sodium (Na) có 11 proton, khối lượng nguyên tử ≈ 23 amu. Tính số electron và số neutron.
- Số e = số p = 11 (nguyên tử trung hòa về điện).
- Khối lượng ≈ p + n ⇒ 23 = 11 + n ⇒ n = 12.

💡 VÍ DỤ 2: Sắp xếp electron
Nguyên tử Oxygen có 8 electron. Hãy cho biết số lớp electron và số electron lớp ngoài cùng.
- Lớp 1: 2 electron (đã đầy). Còn 8 – 2 = 6 electron xếp vào lớp 2.
- Oxygen có 2 lớp electron, lớp ngoài cùng có 6 electron.""",

    "cau_hoi": [
        TN("Nguyên tử mang điện tích gì?",
           ["Điện tích dương", "Điện tích âm", "Trung hòa về điện", "Phụ thuộc vào nhiệt độ"], 2,
           "Nguyên tử luôn có số p = số e nên trung hòa về điện.", "biet"),
        TN("Hạt nhân nguyên tử được cấu tạo bởi những loại hạt nào?",
           ["Chỉ có hạt proton", "Hạt proton và hạt electron", "Hạt proton và hạt neutron", "Hạt electron và hạt neutron"], 2,
           "Hạt nhân nằm ở tâm nguyên tử, chứa proton và neutron.", "biet"),
        TN("Hạt nào sau đây mang điện tích âm?",
           ["Proton", "Neutron", "Electron", "Hạt nhân"], 2,
           "Electron mang điện tích –1.", "biet"),
        TN("Hạt neutron mang điện tích gì?",
           ["Điện tích dương", "Điện tích âm", "Không mang điện", "Lúc dương lúc âm"], 2,
           "Neutron là hạt không mang điện.", "biet"),
        TN("Theo mô hình Rutherford – Bohr, các electron chuyển động như thế nào?",
           ["Đứng yên bên trong hạt nhân", "Xung quanh hạt nhân theo từng lớp xác định",
            "Hỗn loạn ở bên ngoài nguyên tử", "Nằm xen giữa các proton"], 1,
           "Electron chuyển động quanh hạt nhân theo những lớp (quỹ đạo) xác định.", "biet"),
        TN("Lớp electron thứ nhất (gần hạt nhân nhất) chứa tối đa bao nhiêu electron?",
           ["2", "8", "18", "32"], 0,
           "Lớp thứ nhất chỉ chứa tối đa 2 electron.", "biet"),
        TN("Lớp electron thứ hai chứa tối đa bao nhiêu electron?",
           ["2", "8", "18", "32"], 1,
           "Lớp thứ hai chứa tối đa 8 electron.", "biet"),
        TN("Đơn vị dùng để đo khối lượng nguyên tử được kí hiệu là gì?",
           ["kg", "gam", "amu", "mL"], 2,
           "amu là viết tắt của atomic mass unit (đơn vị khối lượng nguyên tử).", "biet"),
        TN("Vì sao nguyên tử trung hòa về điện?",
           ["Vì số proton bằng số electron", "Vì số proton bằng số neutron",
            "Vì hạt nhân không mang điện", "Vì electron không mang điện"], 0,
           "Mỗi proton mang +1, mỗi electron mang –1; số p = số e nên tổng điện tích bằng 0.", "hieu"),
        TN("Khối lượng của nguyên tử tập trung chủ yếu ở đâu?",
           ["Lớp vỏ electron", "Hạt nhân", "Khoảng trống giữa hạt nhân và vỏ", "Chia đều cho vỏ và hạt nhân"], 1,
           "Electron có khối lượng rất nhỏ (≈ 0,00055 amu) nên khối lượng nguyên tử gần bằng khối lượng hạt nhân.", "hieu"),
        TN("Hạt nhân nguyên tử Helium có 2 proton. Lớp vỏ của nguyên tử Helium có bao nhiêu electron?",
           ["1", "2", "3", "4"], 1,
           "Nguyên tử trung hòa về điện nên số e = số p = 2.", "hieu"),
        TN("Nguyên tử Oxygen có 8 electron. Cách sắp xếp electron vào các lớp nào đúng?",
           ["8", "2, 6", "6, 2", "4, 4"], 1,
           "Lớp 1 tối đa 2e, còn lại 6e ở lớp 2.", "hieu"),
        TN("Một nguyên tử có 8 proton, 8 electron và 8 neutron. Khối lượng nguyên tử này xấp xỉ bao nhiêu?",
           ["8 amu", "16 amu", "24 amu", "0 amu"], 1,
           "Khối lượng ≈ p + n = 8 + 8 = 16 amu (bỏ qua khối lượng electron).", "van_dung"),
        TN("Nguyên tử Aluminium có 13 electron. Lớp ngoài cùng của nguyên tử này có bao nhiêu electron?",
           ["1", "2", "3", "5"], 2,
           "13 electron xếp thành 3 lớp: 2, 8, 3 ⇒ lớp ngoài cùng có 3 electron.", "van_dung"),
        TN("Nguyên tử Nitrogen có 7 proton và 7 neutron. Tổng số hạt (p, n, e) trong nguyên tử là bao nhiêu?",
           ["14", "7", "21", "28"], 2,
           "Số e = số p = 7. Tổng = 7 + 7 + 7 = 21 hạt.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Hãy cho biết trong nguyên tử, hạt nào mang điện tích dương, hạt nào mang điện tích âm, hạt nào không mang điện?",
           "Proton mang điện dương, electron mang điện âm, neutron không mang điện.",
           giai_thich="Xem mục 3 – Cấu tạo nguyên tử.", tu_luan=True),
        BT("Nguyên tử Magnesium có 12 proton. Nguyên tử này có bao nhiêu electron?",
           ["12"], giai_thich="Số e = số p = 12."),
        BT("Nguyên tử X có 8 proton và 8 neutron. Khối lượng nguyên tử X bằng bao nhiêu amu?",
           ["16"], giai_thich="Khối lượng ≈ p + n = 8 + 8 = 16 amu."),
        BT("Nguyên tử Sodium có 11 electron. Lớp ngoài cùng của nguyên tử Sodium có bao nhiêu electron?",
           ["1"], giai_thich="11 electron xếp thành 3 lớp: 2, 8, 1."),
        BT("Nguyên tử Chlorine có 17 proton và 18 neutron. Tính tổng số hạt p, n, e trong nguyên tử.",
           ["52"], giai_thich="Số e = 17. Tổng = 17 + 18 + 17 = 52 hạt."),
    ],

    "bt_nang_cao": [
        BT("Tổng số hạt p, n, e trong nguyên tử X là 40. Số hạt mang điện nhiều hơn số hạt không mang điện là 12. Tìm số proton của X.",
           ["13"],
           goi_y="Hạt mang điện gồm p và e (p = e). Lập: 2p + n = 40 và 2p – n = 12.",
           loi_giai="Cộng hai phương trình: 4p = 52 ⇒ p = 13; n = 40 – 26 = 14. X có 13 proton (Aluminium)."),
        BT("Tổng số hạt trong nguyên tử X là 34. Trong hạt nhân, số proton ít hơn số neutron 1 hạt. Tìm số proton của X.",
           ["11"],
           goi_y="2p + n = 34 và n = p + 1.",
           loi_giai="2p + (p + 1) = 34 ⇒ 3p = 33 ⇒ p = 11 (Sodium)."),
        BT("Khối lượng nguyên tử Oxygen là 16 amu. Biết 1 amu ≈ 1,66 × 10⁻²⁴ gam. Tính khối lượng thực của một nguyên tử Oxygen theo gam.",
           "≈ 2,656 × 10⁻²³ gam",
           goi_y="Nhân khối lượng (amu) với giá trị 1 amu tính bằng gam.",
           loi_giai="m = 16 × 1,66 × 10⁻²⁴ = 26,56 × 10⁻²⁴ = 2,656 × 10⁻²³ (gam).", tu_luan=True),
    ],
}

# ---------------------------- BÀI 3 ----------------------------------
C1["Bài 3: Nguyên tố hóa học"] = {
    "ly_thuyet": """📌 1. NGUYÊN TỐ HÓA HỌC LÀ GÌ?
- Nguyên tố hóa học là tập hợp những nguyên tử cùng loại, có cùng số proton trong hạt nhân.
- Số proton là số đặc trưng của một nguyên tố: các nguyên tử có cùng số proton thì thuộc cùng một nguyên tố.
- Các nguyên tử của cùng một nguyên tố có thể có số neutron khác nhau.

📌 2. CÓ BAO NHIÊU NGUYÊN TỐ?
- Hiện nay con người đã biết 118 nguyên tố hóa học. Phần lớn có trong tự nhiên, một số do con người tạo ra trong phòng thí nghiệm.
- Trong vỏ Trái Đất, oxygen là nguyên tố chiếm tỉ lệ khối lượng lớn nhất (gần một nửa), tiếp theo là silicon.

📌 3. TÊN GỌI VÀ KÍ HIỆU HÓA HỌC
- Tên nguyên tố được gọi theo IUPAC, ví dụ: Hydrogen, Oxygen, Sodium (natri), Potassium (kali), Iron (sắt), Copper (đồng).
- Kí hiệu hóa học gồm 1 hoặc 2 chữ cái: chữ cái đầu viết HOA, chữ cái thứ hai (nếu có) viết thường.
  Ví dụ: H, C, N, O, Na, Mg, Al, Cl, Ca, Fe, Cu.
- Một số kí hiệu lấy từ tên Latin: Na (Natrium), K (Kalium), Fe (Ferrum), Cu (Cuprum), Ag (Argentum).

📌 4. 20 NGUYÊN TỐ ĐẦU TIÊN (số hiệu – kí hiệu – tên – khối lượng nguyên tử, amu)
1 H Hydrogen 1 · 2 He Helium 4 · 3 Li Lithium 7 · 4 Be Beryllium 9 · 5 B Boron 11
6 C Carbon 12 · 7 N Nitrogen 14 · 8 O Oxygen 16 · 9 F Fluorine 19 · 10 Ne Neon 20
11 Na Sodium 23 · 12 Mg Magnesium 24 · 13 Al Aluminium 27 · 14 Si Silicon 28 · 15 P Phosphorus 31
16 S Sulfur 32 · 17 Cl Chlorine 35,5 · 18 Ar Argon 40 · 19 K Potassium 39 · 20 Ca Calcium 40

📌 5. VAI TRÒ VỚI SỰ SỐNG
- Oxygen cần cho hô hấp; calcium giúp xương, răng chắc khỏe; iron tham gia tạo máu; iodine giúp phòng bệnh bướu cổ.""",

    "vi_du": """💡 VÍ DỤ 1: Nhận ra nguyên tử cùng nguyên tố
Nguyên tử A có 6 proton, 6 neutron. Nguyên tử B có 6 proton, 8 neutron. A và B có thuộc cùng một nguyên tố không?
- Cả hai đều có 6 proton ⇒ cùng thuộc nguyên tố Carbon (dù số neutron khác nhau).

💡 VÍ DỤ 2: Viết đúng kí hiệu hóa học
Bạn An viết kí hiệu của Calcium là "CA" và của Copper là "cu". Hãy sửa lại.
- Chữ đầu viết hoa, chữ thứ hai viết thường ⇒ Calcium: Ca; Copper: Cu.""",

    "cau_hoi": [
        TN("Nguyên tố hóa học là tập hợp những nguyên tử có cùng:",
           ["Số neutron", "Số proton", "Khối lượng nguyên tử", "Số lớp electron"], 1,
           "Số proton là số đặc trưng của một nguyên tố hóa học.", "biet"),
        TN("Kí hiệu hóa học của nguyên tố Iron (sắt) là gì?",
           ["I", "Ir", "Fe", "S"], 2,
           "Iron có kí hiệu Fe (từ tên Latin Ferrum).", "biet"),
        TN("Nguyên tố Calcium có kí hiệu hóa học là gì?",
           ["C", "Ca", "Cu", "Cl"], 1,
           "Calcium (canxi) có kí hiệu Ca.", "biet"),
        TN("Kí hiệu O biểu diễn nguyên tố nào?",
           ["Osmium", "Oxygen", "Oganesson", "Vàng"], 1,
           "O là kí hiệu của Oxygen.", "biet"),
        TN("Kí hiệu Na biểu diễn nguyên tố nào?",
           ["Nitrogen", "Neon", "Sodium", "Nickel"], 2,
           "Na là kí hiệu của Sodium (natri), lấy từ tên Latin Natrium.", "biet"),
        TN("Kí hiệu K biểu diễn nguyên tố nào?",
           ["Calcium", "Potassium", "Krypton", "Carbon"], 1,
           "K là kí hiệu của Potassium (kali), lấy từ tên Latin Kalium.", "biet"),
        TN("Kí hiệu hóa học của nguyên tố Silver (bạc) là gì?",
           ["Au", "Ag", "Cu", "Al"], 1,
           "Bạc có kí hiệu Ag (Argentum). Au là vàng.", "biet"),
        TN("Nguyên tố nào chiếm tỉ lệ khối lượng lớn nhất trong vỏ Trái Đất?",
           ["Silicon", "Oxygen", "Iron", "Aluminium"], 1,
           "Oxygen chiếm gần một nửa khối lượng vỏ Trái Đất.", "biet"),
        TN("Cách viết kí hiệu hóa học của Calcium nào sau đây là ĐÚNG?",
           ["CA", "ca", "Ca", "cA"], 2,
           "Chữ cái đầu viết hoa, chữ cái thứ hai viết thường.", "hieu"),
        TN("Khẳng định nào SAI khi nói về nguyên tố hóa học?",
           ["Nguyên tố là tập hợp các nguyên tử cùng loại",
            "Các nguyên tử của cùng một nguyên tố có cùng số proton",
            "Các nguyên tử của cùng một nguyên tố bắt buộc phải có cùng số neutron",
            "Hiện nay đã biết 118 nguyên tố hóa học"], 2,
           "Nguyên tử cùng nguyên tố có thể có số neutron khác nhau.", "hieu"),
        TN("Nguyên tử A có 6 proton, 6 neutron; nguyên tử B có 6 proton, 8 neutron. Nhận xét nào đúng?",
           ["A và B thuộc cùng một nguyên tố", "A và B thuộc hai nguyên tố khác nhau",
            "A và B có cùng khối lượng", "B không phải là nguyên tử"], 0,
           "Cùng 6 proton ⇒ cùng nguyên tố Carbon.", "hieu"),
        TN("Nguyên tố nào cần thiết giúp xương và răng chắc khỏe?",
           ["Calcium", "Sodium", "Chlorine", "Neon"], 0,
           "Calcium là thành phần chính của xương và răng.", "hieu"),
        TN("Một nguyên tử có 17 proton. Nguyên tử đó thuộc nguyên tố nào?",
           ["Chlorine (Cl)", "Sulfur (S)", "Argon (Ar)", "Potassium (K)"], 0,
           "Nguyên tố có 17 proton là Chlorine.", "van_dung"),
        TN("Nguyên tử X có số proton gấp đôi số proton của nguyên tử Oxygen (8 proton). X là nguyên tố nào?",
           ["Silicon (Si)", "Sulfur (S)", "Phosphorus (P)", "Neon (Ne)"], 1,
           "X có 2 × 8 = 16 proton ⇒ Sulfur.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Viết kí hiệu hóa học của nguyên tố Nitrogen.", ["N"], giai_thich="Nitrogen: N."),
        BT("Viết kí hiệu hóa học của nguyên tố Magnesium.", ["Mg"], giai_thich="Magnesium: Mg (M hoa, g thường)."),
        BT("Nguyên tố nào có nguyên tử nhẹ nhất (chỉ có 1 proton)? Ghi kí hiệu hoặc tên.",
           ["H", "Hydrogen", "Hidro", "Hiđro"], giai_thich="Hydrogen (H) ở ô số 1."),
        BT("Nguyên tử có 20 proton thuộc nguyên tố nào? Ghi kí hiệu hoặc tên.",
           ["Ca", "Calcium", "Canxi"], giai_thich="Nguyên tố có 20 proton là Calcium (Ca)."),
        BT("Đọc tên các nguyên tố có kí hiệu: K, Ca, Fe, Cu.",
           "Potassium (kali), Calcium (canxi), Iron (sắt), Copper (đồng).", tu_luan=True),
    ],

    "bt_nang_cao": [
        BT("Trong bài kiểm tra, một bạn viết kí hiệu của Calcium là cA và của Iron là fE. Hãy sửa lại và nêu quy tắc viết kí hiệu hóa học.",
           "Ca, Fe.",
           goi_y="Chú ý chữ cái nào viết hoa, chữ cái nào viết thường.",
           loi_giai="Kí hiệu hóa học gồm 1 hoặc 2 chữ cái; chữ cái đầu luôn viết hoa, chữ cái thứ hai (nếu có) viết thường. Sửa: Ca, Fe.",
           tu_luan=True),
        BT("Nguyên tử X nặng gấp 2 lần nguyên tử Carbon (12 amu). X là nguyên tố nào? Ghi kí hiệu hoặc tên.",
           ["Mg", "Magnesium", "Magie"],
           goi_y="Tính khối lượng nguyên tử X rồi tra bảng 20 nguyên tố đầu tiên.",
           loi_giai="Khối lượng X = 2 × 12 = 24 amu ⇒ X là Magnesium (Mg)."),
        BT("(Mở rộng) Những nguyên tử có cùng số proton nhưng khác số neutron được gọi là gì? Cho ví dụ với nguyên tố Carbon.",
           "Gọi là các đồng vị của cùng một nguyên tố.",
           goi_y="Chúng vẫn thuộc cùng một nguyên tố vì cùng số proton.",
           loi_giai="Đó là các đồng vị. Ví dụ: Carbon-12 (6p, 6n) và Carbon-14 (6p, 8n) đều là nguyên tố Carbon nhưng khối lượng khác nhau.",
           tu_luan=True),
    ],
}

# ---------------------------- BÀI 4 ----------------------------------
C1["Bài 4: Sơ lược về bảng tuần hoàn các nguyên tố hóa học"] = {
    "ly_thuyet": """📌 1. LỊCH SỬ
- Năm 1869, nhà hóa học người Nga Dmitri Mendeleev (Men-đê-lê-ép) công bố bảng tuần hoàn đầu tiên.

📌 2. NGUYÊN TẮC SẮP XẾP
- Các nguyên tố được xếp theo chiều tăng dần của điện tích hạt nhân (số proton).
- Các nguyên tố có cùng số lớp electron được xếp vào cùng một hàng.
- Các nguyên tố có tính chất hóa học tương tự nhau được xếp vào cùng một cột.

📌 3. Ô NGUYÊN TỐ
- Mỗi ô cho biết: số hiệu nguyên tử, kí hiệu hóa học, tên nguyên tố, khối lượng nguyên tử.
- Số hiệu nguyên tử = số thứ tự của ô = số proton = số electron.

📌 4. CHU KÌ (hàng ngang)
- Gồm các nguyên tố có cùng số lớp electron, xếp theo chiều số hiệu tăng dần.
- Số thứ tự chu kì = số lớp electron.
- Có 7 chu kì: chu kì 1, 2, 3 là chu kì nhỏ; chu kì 4, 5, 6, 7 là chu kì lớn.

📌 5. NHÓM (cột dọc)
- Gồm các nguyên tố có tính chất hóa học tương tự nhau.
- Bảng tuần hoàn có 18 cột, chia thành các nhóm A (từ IA đến VIIIA) và các nhóm B.
- Với các nguyên tố nhóm A: số thứ tự nhóm = số electron lớp ngoài cùng.

📌 6. KIM LOẠI – PHI KIM – KHÍ HIẾM
- Kim loại: chiếm phần lớn bảng tuần hoàn, nằm ở bên trái và ở giữa (nhóm IA trừ hydrogen, nhóm IIA, phần lớn nhóm IIIA và các nhóm B).
- Phi kim: tập trung ở phía trên, bên phải bảng.
- Khí hiếm: nhóm VIIIA (cột cuối cùng), rất bền, hầu như không tham gia phản ứng.
- Nhóm IA (trừ H) gọi là kim loại kiềm; nhóm VIIA gọi là halogen.""",

    "vi_du": """💡 VÍ DỤ 1: Xác định vị trí nguyên tố
Phosphorus (P) có 15 electron. Xác định ô, chu kì, nhóm của P.
- 15 electron ⇒ số hiệu 15 ⇒ ô số 15.
- Sắp xếp electron: 2, 8, 5 ⇒ 3 lớp electron ⇒ chu kì 3.
- Lớp ngoài cùng có 5 electron ⇒ nhóm VA.

💡 VÍ DỤ 2: Từ vị trí suy ra cấu tạo
Nguyên tố X ở chu kì 3, nhóm IIA. Tìm số hiệu nguyên tử của X.
- Chu kì 3 ⇒ 3 lớp electron; nhóm IIA ⇒ lớp ngoài cùng có 2 electron.
- Sắp xếp: 2, 8, 2 ⇒ 12 electron ⇒ X ở ô 12 (Magnesium).""",

    "cau_hoi": [
        TN("Nhà khoa học nào công bố bảng tuần hoàn các nguyên tố hóa học đầu tiên (năm 1869)?",
           ["Isaac Newton", "Albert Einstein", "Dmitri Mendeleev", "Marie Curie"], 2,
           "Mendeleev (người Nga) công bố bảng tuần hoàn đầu tiên năm 1869.", "biet"),
        TN("Các nguyên tố trong bảng tuần hoàn hiện nay được sắp xếp theo chiều tăng dần của:",
           ["Khối lượng nguyên tử", "Điện tích hạt nhân (số proton)", "Số neutron", "Số lớp electron"], 1,
           "Nguyên tắc sắp xếp: theo chiều tăng dần của điện tích hạt nhân.", "biet"),
        TN("Số thứ tự của ô nguyên tố bằng đại lượng nào?",
           ["Số hiệu nguyên tử (số proton)", "Số lớp electron", "Số neutron", "Khối lượng nguyên tử"], 0,
           "Số thứ tự ô = số hiệu nguyên tử = số p = số e.", "biet"),
        TN("Chu kì là dãy các nguyên tố mà nguyên tử của chúng có cùng:",
           ["Số electron lớp ngoài cùng", "Số proton", "Số neutron", "Số lớp electron"], 3,
           "Các nguyên tố cùng số lớp electron được xếp thành một chu kì.", "biet"),
        TN("Bảng tuần hoàn có bao nhiêu chu kì?",
           ["7", "8", "18", "10"], 0,
           "Bảng tuần hoàn có 7 chu kì.", "biet"),
        TN("Các nguyên tố khí hiếm nằm ở nhóm nào?",
           ["Nhóm IA", "Nhóm VIIA", "Nhóm VIIIA", "Nhóm IIA"], 2,
           "Khí hiếm nằm ở cột cuối cùng – nhóm VIIIA.", "biet"),
        TN("Nhóm VIIA trong bảng tuần hoàn gồm các nguyên tố được gọi là:",
           ["Kim loại kiềm", "Khí hiếm", "Halogen", "Kim loại kiềm thổ"], 2,
           "Nhóm VIIA là nhóm halogen (phi kim hoạt động mạnh).", "biet"),
        TN("Các nguyên tố trong cùng một nhóm A có cùng:",
           ["Số lớp electron", "Số electron lớp ngoài cùng", "Số proton", "Số neutron"], 1,
           "Cùng số electron lớp ngoài cùng nên có tính chất hóa học tương tự.", "hieu"),
        TN("Phần lớn các nguyên tố phi kim nằm ở khu vực nào của bảng tuần hoàn?",
           ["Bên trái", "Ở giữa", "Phía trên, bên phải", "Hàng dưới cùng"], 2,
           "Phi kim tập trung ở phía trên, bên phải bảng tuần hoàn.", "hieu"),
        TN("Các kim loại kiềm (như Li, Na, K) có bao nhiêu electron ở lớp ngoài cùng?",
           ["1", "2", "3", "7"], 0,
           "Kim loại kiềm thuộc nhóm IA nên có 1 electron lớp ngoài cùng.", "hieu"),
        TN("Nguyên tố Hydrogen (H) nằm ở vị trí nào trong bảng tuần hoàn?",
           ["Ô 1, chu kì 1, nhóm IA", "Ô 2, chu kì 1, nhóm VIIIA", "Ô 1, chu kì 2, nhóm IA", "Ô 1, chu kì 1, nhóm VIIA"], 0,
           "H có 1 electron, 1 lớp electron ⇒ ô 1, chu kì 1, nhóm IA.", "hieu"),
        TN("Nguyên tử X có 12 electron. X nằm ở chu kì mấy?",
           ["Chu kì 1", "Chu kì 2", "Chu kì 3", "Chu kì 4"], 2,
           "12 electron xếp thành 3 lớp (2, 8, 2) ⇒ chu kì 3.", "van_dung"),
        TN("Một nguyên tử có 3 lớp electron, lớp ngoài cùng có 7 electron. Nguyên tố đó là:",
           ["Kim loại", "Phi kim", "Khí hiếm", "Không xác định được"], 1,
           "Có 7 electron lớp ngoài cùng (nhóm VIIA) ⇒ phi kim (đây là Chlorine).", "van_dung"),
        TN("Nguyên tố ở chu kì 3, nhóm IIA có số hiệu nguyên tử là bao nhiêu?",
           ["10", "12", "20", "2"], 1,
           "3 lớp electron, lớp ngoài cùng 2e ⇒ 2, 8, 2 ⇒ 12 electron.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Nguyên tố Chlorine ở ô số 17. Nguyên tử Chlorine có bao nhiêu lớp electron?",
           ["3"], giai_thich="17 electron xếp thành 2, 8, 7 ⇒ 3 lớp."),
        BT("Nguyên tố Chlorine ở ô số 17. Lớp ngoài cùng của nguyên tử Chlorine có bao nhiêu electron?",
           ["7"], giai_thich="Sắp xếp 2, 8, 7 ⇒ lớp ngoài cùng có 7 electron."),
        BT("Ô số 8 trong bảng tuần hoàn là của nguyên tố nào? Ghi kí hiệu hoặc tên.",
           ["O", "Oxygen", "Oxi"], giai_thich="Ô số 8 là Oxygen (O)."),
        BT("Xác định chu kì và nhóm của nguyên tố có 3 lớp electron, trong đó lớp ngoài cùng có 1 electron.",
           "Chu kì 3, nhóm IA.",
           giai_thich="3 lớp electron ⇒ chu kì 3; 1 electron lớp ngoài cùng ⇒ nhóm IA (đây là Sodium).",
           tu_luan=True),
        BT("Dựa vào số electron lớp ngoài cùng, hãy phân loại: nguyên tử X (1e), Y (7e), Z (8e).",
           "X là kim loại; Y là phi kim; Z là khí hiếm.",
           giai_thich="1, 2, 3 electron lớp ngoài cùng thường là kim loại; 5, 6, 7 thường là phi kim; 8 là khí hiếm.",
           tu_luan=True),
    ],

    "bt_nang_cao": [
        BT("Hai nguyên tố A và B đứng kế tiếp nhau trong cùng một chu kì. Tổng số proton của chúng là 25. Xác định A và B.",
           "A là Magnesium (Z = 12), B là Aluminium (Z = 13).",
           goi_y="Đứng kế tiếp nhau trong một chu kì ⇒ số hiệu hơn kém nhau 1.",
           loi_giai="Z_A + Z_B = 25 và Z_B – Z_A = 1 ⇒ Z_B = 13 (Al), Z_A = 12 (Mg).", tu_luan=True),
        BT("Hai nguyên tố X, Y thuộc cùng một nhóm A, ở hai chu kì nhỏ liên tiếp. Tổng số proton của X và Y là 32. Xác định X, Y.",
           "X là Magnesium (Z = 12), Y là Calcium (Z = 20).",
           goi_y="Hai nguyên tố cùng nhóm A ở chu kì 2 – 3 hoặc 3 – 4 có số hiệu hơn kém nhau 8.",
           loi_giai="Z_X + Z_Y = 32 và Z_Y – Z_X = 8 ⇒ Z_Y = 20 (Ca), Z_X = 12 (Mg). Cả hai thuộc nhóm IIA.", tu_luan=True),
        BT("Vì sao chu kì 1 chỉ có 2 nguyên tố, còn chu kì 2 và chu kì 3 mỗi chu kì có 8 nguyên tố?",
           "Do số electron tối đa ở lớp ngoài cùng của các nguyên tố trong chu kì đó.",
           goi_y="Nhớ lại số electron tối đa của lớp 1 và lớp ngoài cùng.",
           loi_giai="Chu kì 1 chỉ có 1 lớp electron, lớp này chứa tối đa 2 electron nên chỉ có 2 nguyên tố (H, He). "
                    "Ở chu kì 2 và 3, lớp ngoài cùng được điền dần từ 1 đến 8 electron, nên mỗi chu kì có 8 nguyên tố: "
                    "mở đầu là một kim loại kiềm và kết thúc là một khí hiếm.", tu_luan=True),
        BT("Vì sao các khí hiếm (nhóm VIIIA) hầu như không tham gia phản ứng hóa học?",
           "Vì lớp electron ngoài cùng của chúng đã bền vững.",
           goi_y="Quan sát số electron lớp ngoài cùng của khí hiếm.",
           loi_giai="Khí hiếm có 8 electron ở lớp ngoài cùng (riêng Helium có 2 electron) – đây là cấu trúc rất bền, "
                    "nên nguyên tử khí hiếm không có xu hướng nhường, nhận hay dùng chung electron.", tu_luan=True),
    ],
}

# ---------------------- ÔN TẬP CHƯƠNG 1 --------------------------------
C1["Ôn tập Chương 1 – Nâng cao"] = {
    "ly_thuyet": """📌 TÓM TẮT KIẾN THỨC CHƯƠNG 1
- Nguyên tử: hạt nhân (p, n) + vỏ (e). Số p = số e. Khối lượng ≈ p + n (amu).
- Nguyên tố hóa học: tập hợp nguyên tử cùng số proton. Kí hiệu: chữ đầu hoa, chữ sau thường.
- Bảng tuần hoàn: số thứ tự ô = Z = p = e; số thứ tự chu kì = số lớp e; số thứ tự nhóm A = số e lớp ngoài cùng.

📌 PHƯƠNG PHÁP GIẢI BÀI TOÁN "TỔNG SỐ HẠT"
- Gọi số proton là p (= số e), số neutron là n.
- Tổng số hạt: 2p + n = S.
- Hạt mang điện nhiều hơn hạt không mang điện: 2p – n = D.
- Giải hệ hai phương trình để tìm p và n, rồi tra số hiệu để biết tên nguyên tố.""",

    "vi_du": """💡 VÍ DỤ: Nguyên tử M có tổng số hạt là 58; số hạt mang điện nhiều hơn số hạt không mang điện là 18. Xác định vị trí của M.
- 2p + n = 58 và 2p – n = 18 ⇒ 4p = 76 ⇒ p = 19; n = 20.
- 19 electron xếp thành 2, 8, 8, 1 ⇒ 4 lớp electron, lớp ngoài cùng 1 electron.
- M ở ô 19, chu kì 4, nhóm IA – đó là Potassium (K).""",

    "cau_hoi": [
        TN("Nguyên tử Sodium có 11 proton và khối lượng nguyên tử 23 amu. Tổng số hạt p, n, e trong nguyên tử là:",
           ["23", "34", "45", "12"], 1,
           "n = 23 – 11 = 12; tổng = 11 + 12 + 11 = 34.", "van_dung"),
        TN("Nguyên tử X có tổng số hạt mang điện là 26. X là nguyên tố nào?",
           ["Magnesium", "Aluminium", "Silicon", "Sodium"], 1,
           "Hạt mang điện = p + e = 2p = 26 ⇒ p = 13 ⇒ Aluminium.", "van_dung"),
        TN("Nguyên tố Y ở chu kì 2, nhóm VIA. Số hiệu nguyên tử của Y là:",
           ["6", "8", "16", "10"], 1,
           "2 lớp electron, lớp ngoài cùng 6e ⇒ 2, 6 ⇒ 8 electron (Oxygen).", "van_dung"),
        TN("Nguyên tử nào sau đây có cùng số lớp electron với nguyên tử Sodium (Na, Z = 11)?",
           ["Lithium (Z = 3)", "Potassium (Z = 19)", "Chlorine (Z = 17)", "Fluorine (Z = 9)"], 2,
           "Na và Cl cùng ở chu kì 3 (3 lớp electron).", "van_dung"),
        TN("Nguyên tố nào có tính chất hóa học tương tự Sodium (Na)?",
           ["Magnesium", "Potassium", "Chlorine", "Neon"], 1,
           "Na và K cùng nhóm IA (kim loại kiềm) nên tính chất tương tự.", "hieu"),
        TN("Nguyên tử X có 12 neutron; số hạt mang điện nhiều hơn số hạt không mang điện là 10. X là:",
           ["Sodium", "Magnesium", "Neon", "Fluorine"], 0,
           "2p – 12 = 10 ⇒ p = 11 ⇒ Sodium.", "van_dung"),
        TN("Trong các loại hạt p, n, e, hạt nào quyết định tính chất hóa học của nguyên tử?",
           ["Proton", "Neutron", "Electron (đặc biệt là electron lớp ngoài cùng)", "Cả ba loại hạt như nhau"], 2,
           "Phản ứng hóa học liên quan đến việc nhường, nhận hoặc dùng chung electron lớp ngoài cùng.", "hieu"),
    ],

    "bt_co_ban": [
        BT("Nguyên tử Magnesium có 12 proton và 12 neutron. Tính tổng số hạt trong nguyên tử.",
           ["36"], giai_thich="Số e = 12. Tổng = 12 + 12 + 12 = 36."),
        BT("Nguyên tử X có tổng số hạt mang điện là 34. Tìm số proton của X.",
           ["17"], giai_thich="2p = 34 ⇒ p = 17 (Chlorine)."),
    ],

    "bt_nang_cao": [
        BT("Tổng số hạt trong nguyên tử A là 28, trong đó số hạt không mang điện chiếm khoảng 35,7%. Tìm số proton của A.",
           ["9"],
           goi_y="Tính số neutron trước: n ≈ 35,7% × 28.",
           loi_giai="n ≈ 0,357 × 28 ≈ 10. Ta có 2p + 10 = 28 ⇒ p = 9 (Fluorine)."),
        BT("Trong nguyên tử nguyên tố R, tổng số hạt là 115; số hạt mang điện nhiều hơn số hạt không mang điện là 25. Tìm số electron của R.",
           ["35"],
           goi_y="2p + n = 115 và 2p – n = 25.",
           loi_giai="Cộng hai phương trình: 4p = 140 ⇒ p = e = 35 (Bromine)."),
        BT("Nguyên tử Y có tổng số hạt là 52; số hạt không mang điện gấp khoảng 1,06 lần số hạt mang điện dương. Tính khối lượng nguyên tử Y (amu).",
           ["35"],
           goi_y="2p + n = 52 và n ≈ 1,06p.",
           loi_giai="2p + 1,06p = 52 ⇒ p ≈ 17; n = 52 – 34 = 18. Khối lượng ≈ 17 + 18 = 35 amu (Chlorine)."),
        BT("Nguyên tử nguyên tố A nặng gấp 2 lần nguyên tử Nitrogen (14 amu). Biết số proton bằng số neutron. Tìm số proton của A.",
           ["14"],
           goi_y="Khối lượng A = 28 amu và p = n.",
           loi_giai="p + n = 28, p = n ⇒ p = 14 (Silicon)."),
        BT("Hợp chất AB₂ có tổng số proton là 22. Biết A ở chu kì 2, nhóm IVA. Xác định nguyên tố B và công thức hợp chất.",
           "B là Oxygen; hợp chất là CO₂.",
           goi_y="Chu kì 2, nhóm IVA ⇒ A có 2 lớp e, lớp ngoài cùng 4e.",
           loi_giai="A: 2, 4 ⇒ Z_A = 6 (Carbon). 6 + 2·Z_B = 22 ⇒ Z_B = 8 (Oxygen). Hợp chất là CO₂.", tu_luan=True),
        BT("Nguyên tố X có số hiệu nguyên tử 20. Viết sự sắp xếp electron và cho biết X có xu hướng nhường hay nhận electron.",
           "2, 8, 8, 2 – X có xu hướng nhường 2 electron.",
           goi_y="Lớp 1: 2e, lớp 2: 8e, lớp 3: 8e, lớp 4: phần còn lại.",
           loi_giai="Z = 20: 2, 8, 8, 2. X có 2 electron lớp ngoài cùng (kim loại Calcium) nên có xu hướng nhường 2 electron để có lớp ngoài cùng giống khí hiếm.",
           tu_luan=True),
        BT("(Bồi dưỡng HSG) Nguyên tử X có tổng số hạt là 21. Biết với các nguyên tử nhẹ: p ≤ n ≤ 1,5p. Tìm số proton có thể có của X.",
           "p = 6 hoặc p = 7.",
           goi_y="Từ 2p + n = 21 ⇒ n = 21 – 2p, thay vào p ≤ n ≤ 1,5p.",
           loi_giai="p ≤ 21 – 2p ⇒ p ≤ 7; 21 – 2p ≤ 1,5p ⇒ p ≥ 6. Vậy p = 6 (Carbon, n = 9) hoặc p = 7 (Nitrogen, n = 7).",
           tu_luan=True),
    ],
}

H7["Chương 1: Nguyên tử. Sơ lược về bảng tuần hoàn các nguyên tố hóa học"] = C1


# ======================================================================
# CHƯƠNG 2: PHÂN TỬ. LIÊN KẾT HÓA HỌC
# ======================================================================
C2 = {}

# ---------------------------- BÀI 5 ----------------------------------
C2["Bài 5: Phân tử – Đơn chất – Hợp chất"] = {
    "ly_thuyet": """📌 1. PHÂN TỬ
- Phân tử là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau và thể hiện đầy đủ tính chất hóa học của chất.
- Khối lượng phân tử (đơn vị amu) bằng tổng khối lượng các nguyên tử có trong phân tử.
  Ví dụ: H₂O = 2 × 1 + 16 = 18 amu.

📌 2. ĐƠN CHẤT (tạo nên từ MỘT nguyên tố hóa học)
- Đơn chất kim loại (Fe, Cu, Al…): thường ở thể rắn (riêng thủy ngân Hg ở thể lỏng), dẫn điện, dẫn nhiệt, có ánh kim.
- Đơn chất phi kim: có thể ở thể khí (O₂, N₂, H₂, Cl₂), thể rắn (S, P, C) hoặc thể lỏng (Br₂); thường không dẫn điện (trừ than chì).
- Đơn chất khí hiếm (He, Ne, Ar…): tồn tại ở dạng các nguyên tử riêng rẽ.
- Một nguyên tố có thể tạo nên nhiều đơn chất khác nhau. Ví dụ: oxygen (O₂) và ozone (O₃); kim cương và than chì đều được tạo nên từ carbon.

📌 3. HỢP CHẤT (tạo nên từ HAI hay nhiều nguyên tố hóa học)
- Ví dụ: nước (H₂O), muối ăn (NaCl), đá vôi (CaCO₃), khí carbon dioxide (CO₂), đường (C₁₂H₂₂O₁₁).

📌 4. CÁCH NHẬN BIẾT NHANH QUA CÔNG THỨC
- Công thức chỉ có MỘT kí hiệu hóa học ⇒ đơn chất (O₂, Fe, N₂).
- Công thức có từ HAI kí hiệu hóa học trở lên ⇒ hợp chất (H₂O, NaCl).""",

    "vi_du": """💡 VÍ DỤ 1: Tính khối lượng phân tử
Tính khối lượng phân tử của sulfuric acid H₂SO₄ (H = 1, S = 32, O = 16).
- Phân tử có 2 nguyên tử H, 1 nguyên tử S, 4 nguyên tử O.
- Khối lượng phân tử = 2 × 1 + 32 + 4 × 16 = 98 amu.

💡 VÍ DỤ 2: Phân loại chất
Cho các chất: O₂, NaCl, Cl₂, H₂O, Fe, CaCO₃.
- Đơn chất (một kí hiệu): O₂, Cl₂, Fe.
- Hợp chất (từ hai kí hiệu trở lên): NaCl, H₂O, CaCO₃.""",

    "cau_hoi": [
        TN("Chất nào sau đây là đơn chất?",
           ["Nước (H₂O)", "Khí oxygen (O₂)", "Muối ăn (NaCl)", "Đá vôi (CaCO₃)"], 1,
           "O₂ chỉ được tạo nên từ một nguyên tố là oxygen.", "biet"),
        TN("Chất nào sau đây là hợp chất?",
           ["Khí hydrogen (H₂)", "Đồng (Cu)", "Khí carbon dioxide (CO₂)", "Ozone (O₃)"], 2,
           "CO₂ được tạo nên từ hai nguyên tố C và O.", "biet"),
        TN("Kim loại nào ở thể lỏng ở nhiệt độ thường?",
           ["Sắt (Fe)", "Thủy ngân (Hg)", "Đồng (Cu)", "Nhôm (Al)"], 1,
           "Thủy ngân là kim loại duy nhất ở thể lỏng ở nhiệt độ thường.", "biet"),
        TN("Khí hiếm Neon (Ne) tồn tại trong tự nhiên ở dạng nào?",
           ["Phân tử Ne₂", "Phân tử Ne₃", "Các nguyên tử Ne riêng rẽ", "Hợp chất với oxygen"], 2,
           "Khí hiếm đã bền nên tồn tại ở dạng nguyên tử riêng rẽ.", "biet"),
        TN("Kí hiệu O₂ cho biết điều gì?",
           ["1 nguyên tử oxygen", "1 phân tử oxygen gồm 2 nguyên tử O", "2 phân tử oxygen", "2 hợp chất của oxygen"], 1,
           "Chỉ số 2 cho biết một phân tử gồm 2 nguyên tử O.", "hieu"),
        TN("Cách viết '5 Cu' có ý nghĩa là gì?",
           ["5 phân tử đồng", "5 nguyên tử đồng", "5 hợp chất của đồng", "Đồng có hóa trị V"], 1,
           "Hạt hợp thành đơn chất kim loại là nguyên tử ⇒ 5 Cu là 5 nguyên tử đồng.", "hieu"),
        TN("Dãy nào sau đây chỉ gồm các đơn chất?",
           ["O₂, Fe, N₂", "H₂O, O₂, Cu", "NaCl, CO₂, H₂", "CH₄, Al, S"], 0,
           "O₂, Fe, N₂ đều chỉ có một kí hiệu hóa học.", "hieu"),
        TN("Oxygen (O₂) và ozone (O₃) là:",
           ["Hai hợp chất khác nhau", "Hai đơn chất khác nhau của cùng nguyên tố oxygen",
            "Cùng một chất", "Hai nguyên tố khác nhau"], 1,
           "Cùng được tạo nên từ nguyên tố O nhưng số nguyên tử trong phân tử khác nhau.", "hieu"),
        TN("Khối lượng phân tử của nước (H₂O) là bao nhiêu? (H = 1, O = 16)",
           ["17 amu", "18 amu", "33 amu", "32 amu"], 1,
           "2 × 1 + 16 = 18 amu.", "van_dung"),
        TN("Khối lượng phân tử của khí carbon dioxide (CO₂) là bao nhiêu? (C = 12, O = 16)",
           ["28 amu", "44 amu", "12 amu", "32 amu"], 1,
           "12 + 2 × 16 = 44 amu.", "van_dung"),
        TN("Khối lượng phân tử của sulfuric acid (H₂SO₄) là bao nhiêu? (H = 1, S = 32, O = 16)",
           ["98 amu", "49 amu", "96 amu", "100 amu"], 0,
           "2 × 1 + 32 + 4 × 16 = 98 amu.", "van_dung"),
        TN("Khối lượng phân tử của đá vôi (CaCO₃) là bao nhiêu? (Ca = 40, C = 12, O = 16)",
           ["68 amu", "100 amu", "112 amu", "84 amu"], 1,
           "40 + 12 + 3 × 16 = 100 amu.", "van_dung"),
        TN("Khối lượng phân tử của muối ăn NaCl là bao nhiêu? (Na = 23, Cl = 35,5)",
           ["58,5 amu", "35,5 amu", "23 amu", "117 amu"], 0,
           "23 + 35,5 = 58,5 amu.", "van_dung"),
        TN("Methane có công thức CH₄. Trong 3 phân tử methane có bao nhiêu nguyên tử H?",
           ["3", "4", "7", "12"], 3,
           "Mỗi phân tử có 4 nguyên tử H ⇒ 3 × 4 = 12.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Phân loại các chất sau thành đơn chất và hợp chất: O₂, NaCl, Cl₂, H₂O, Fe, CaCO₃.",
           "Đơn chất: O₂, Cl₂, Fe. Hợp chất: NaCl, H₂O, CaCO₃.",
           giai_thich="Đơn chất chỉ có một kí hiệu hóa học; hợp chất có từ hai kí hiệu trở lên.", tu_luan=True),
        BT("Tính khối lượng phân tử của khí oxygen O₂ (O = 16), đơn vị amu.",
           ["32"], giai_thich="2 × 16 = 32 amu."),
        BT("Tính khối lượng phân tử của khí ammonia NH₃ (N = 14, H = 1), đơn vị amu.",
           ["17"], giai_thich="14 + 3 × 1 = 17 amu."),
        BT("Tính khối lượng phân tử của CaCO₃ (Ca = 40, C = 12, O = 16), đơn vị amu.",
           ["100"], giai_thich="40 + 12 + 3 × 16 = 100 amu."),
        BT("Tính tổng khối lượng của 5 phân tử nước H₂O (H = 1, O = 16), đơn vị amu.",
           ["90"], giai_thich="1 phân tử = 18 amu ⇒ 5 phân tử = 90 amu."),
    ],

    "bt_nang_cao": [
        BT("Phân tử hợp chất gồm 2 nguyên tử X liên kết với 1 nguyên tử O, có khối lượng phân tử 62 amu. X là nguyên tố nào? Ghi kí hiệu hoặc tên.",
           ["Na", "Sodium", "Natri"],
           goi_y="Công thức dạng X₂O ⇒ 2·X + 16 = 62.",
           loi_giai="2·X = 46 ⇒ X = 23 amu ⇒ X là Sodium (Na)."),
        BT("Hợp chất có công thức R(OH)₂ và khối lượng phân tử 74 amu. R là nguyên tố nào? (O = 16, H = 1)",
           ["Ca", "Calcium", "Canxi"],
           goi_y="R + 2 × (16 + 1) = 74.",
           loi_giai="R + 34 = 74 ⇒ R = 40 amu ⇒ R là Calcium (Ca)."),
        BT("Phân tử hợp chất gồm 1 nguyên tử X và 2 nguyên tử O; khối lượng phân tử nặng gấp 2,75 lần phân tử methane CH₄. X là nguyên tố nào? (C = 12, H = 1, O = 16)",
           ["C", "Carbon", "Cacbon"],
           goi_y="Tính khối lượng phân tử CH₄ trước.",
           loi_giai="CH₄ = 16 amu ⇒ hợp chất = 16 × 2,75 = 44 amu. X + 32 = 44 ⇒ X = 12 ⇒ Carbon (hợp chất là CO₂)."),
        BT("Khí A nặng gấp 2 lần khí B; khí B nhẹ bằng 1/2 khí oxygen (O₂ = 32 amu). Tính khối lượng phân tử của khí A (amu).",
           ["32"],
           goi_y="Tính khí B trước rồi suy ra khí A.",
           loi_giai="M_B = 32 : 2 = 16 amu; M_A = 2 × 16 = 32 amu (A có thể là khí O₂)."),
        BT("Bột nở chứa chất X; phân tử X gồm 1 nguyên tử Na, 1 nguyên tử H, 1 nguyên tử C và 3 nguyên tử O. Tính khối lượng phân tử của X (amu).",
           ["84"],
           goi_y="Công thức X là NaHCO₃.",
           loi_giai="23 + 1 + 12 + 3 × 16 = 84 amu."),
    ],
}

# ---------------------------- BÀI 6 ----------------------------------
C2["Bài 6: Giới thiệu về liên kết hóa học"] = {
    "ly_thuyet": """📌 1. VÌ SAO CÁC NGUYÊN TỬ LIÊN KẾT VỚI NHAU?
- Nguyên tử khí hiếm có lớp electron ngoài cùng bền vững (8 electron; riêng helium có 2 electron) nên hầu như không liên kết với nguyên tử khác.
- Nguyên tử của các nguyên tố khác có xu hướng nhường, nhận hoặc dùng chung electron để có lớp electron ngoài cùng giống khí hiếm.

📌 2. ION
- Nguyên tử nhường electron ⇒ ion dương. Ví dụ: Na nhường 1e ⇒ Na⁺; Mg nhường 2e ⇒ Mg²⁺.
- Nguyên tử nhận electron ⇒ ion âm. Ví dụ: Cl nhận 1e ⇒ Cl⁻; O nhận 2e ⇒ O²⁻.
- Kim loại thường nhường electron; phi kim thường nhận electron.

📌 3. LIÊN KẾT ION
- Được tạo thành do lực hút giữa các ion mang điện tích trái dấu.
- Thường gặp giữa kim loại điển hình và phi kim điển hình. Ví dụ: NaCl, MgO, MgCl₂.

📌 4. LIÊN KẾT CỘNG HÓA TRỊ
- Được tạo thành do các nguyên tử dùng chung một hay nhiều cặp electron.
- Thường gặp giữa các nguyên tử phi kim. Ví dụ: H₂ (1 cặp electron dùng chung), O₂ (2 cặp), H₂O, CO₂.

📌 5. TÍNH CHẤT CỦA HỢP CHẤT ION VÀ HỢP CHẤT CỘNG HÓA TRỊ
- Hợp chất ion: ở thể rắn ở nhiệt độ thường, khó bay hơi, nhiệt độ nóng chảy và nhiệt độ sôi cao; khi tan trong nước tạo dung dịch dẫn được điện.
- Hợp chất cộng hóa trị: có thể ở thể rắn, lỏng hoặc khí; nhiệt độ nóng chảy và nhiệt độ sôi thường thấp hơn; thường không dẫn điện.""",

    "vi_du": """💡 VÍ DỤ 1: Sự hình thành liên kết ion trong MgO (Mg: Z = 12, O: Z = 8)
- Mg (2, 8, 2) nhường 2 electron ⇒ ion Mg²⁺ (lớp ngoài cùng 8e giống Neon).
- O (2, 6) nhận 2 electron ⇒ ion O²⁻ (lớp ngoài cùng 8e giống Neon).
- Hai ion trái dấu Mg²⁺ và O²⁻ hút nhau tạo thành MgO.

💡 VÍ DỤ 2: Sự hình thành liên kết cộng hóa trị trong H₂O
- O có 6 electron lớp ngoài cùng, cần thêm 2 electron; mỗi H có 1 electron, cần thêm 1 electron.
- Nguyên tử O góp chung 1 electron với mỗi nguyên tử H ⇒ có 2 cặp electron dùng chung.
- Khi đó O có 8 electron lớp ngoài cùng (giống Neon), mỗi H có 2 electron (giống Helium).""",

    "cau_hoi": [
        TN("Vì sao các khí hiếm hầu như không liên kết với nguyên tử khác?",
           ["Vì lớp electron ngoài cùng đã bền vững", "Vì chúng không có electron",
            "Vì hạt nhân không mang điện", "Vì chúng là kim loại"], 0,
           "Khí hiếm có 8 electron lớp ngoài cùng (He có 2) – cấu trúc bền.", "biet"),
        TN("Liên kết ion được tạo thành do:",
           ["Lực hút giữa các ion mang điện tích trái dấu", "Sự dùng chung các cặp electron",
            "Lực hút giữa các phân tử", "Sự đẩy nhau giữa các ion cùng dấu"], 0,
           "Ion dương và ion âm hút nhau tạo liên kết ion.", "biet"),
        TN("Liên kết cộng hóa trị được tạo thành nhờ:",
           ["Lực hút giữa các ion", "Sự dùng chung các cặp electron",
            "Sự nhường hoàn toàn electron", "Lực hút của hạt nhân với neutron"], 1,
           "Các nguyên tử góp chung electron để tạo cặp electron dùng chung.", "biet"),
        TN("Liên kết hóa học trong phân tử muối ăn (NaCl) là:",
           ["Liên kết cộng hóa trị", "Liên kết ion", "Không có liên kết", "Liên kết hydrogen"], 1,
           "Na (kim loại) nhường e cho Cl (phi kim) tạo ion trái dấu hút nhau.", "biet"),
        TN("Nguyên tử Sodium nhường 1 electron sẽ tạo thành ion nào?",
           ["Na⁻", "Na⁺", "Na²⁺", "Na²⁻"], 1,
           "Mất 1 electron (–1) ⇒ dư 1 điện tích dương ⇒ Na⁺.", "hieu"),
        TN("Nguyên tử Oxygen nhận thêm 2 electron sẽ tạo thành ion nào?",
           ["O²⁻", "O²⁺", "O⁻", "O⁺"], 0,
           "Nhận 2 electron ⇒ dư 2 điện tích âm ⇒ O²⁻.", "hieu"),
        TN("Nguyên tử phi kim thường có xu hướng gì để đạt lớp electron ngoài cùng bền vững?",
           ["Nhường electron", "Nhận thêm electron hoặc dùng chung electron", "Mất hết lớp vỏ", "Không thay đổi"], 1,
           "Phi kim có 5, 6, 7 electron lớp ngoài cùng nên dễ nhận hoặc dùng chung electron.", "hieu"),
        TN("Phân tử nào sau đây được tạo thành bằng liên kết cộng hóa trị?",
           ["KCl", "MgCl₂", "H₂O", "Na₂O"], 2,
           "H₂O được tạo bởi hai phi kim H và O dùng chung electron.", "hieu"),
        TN("Hợp chất nào sau đây là hợp chất ion?",
           ["CH₄", "CO₂", "MgCl₂", "H₂O"], 2,
           "MgCl₂ tạo bởi kim loại Mg và phi kim Cl.", "hieu"),
        TN("Liên kết ion thường được hình thành giữa:",
           ["Phi kim với phi kim", "Kim loại điển hình với phi kim điển hình",
            "Kim loại với kim loại", "Khí hiếm với kim loại"], 1,
           "Kim loại dễ nhường e, phi kim dễ nhận e ⇒ tạo ion trái dấu.", "hieu"),
        TN("Ở nhiệt độ thường, hợp chất ion (như muối ăn) thường ở thể nào?",
           ["Thể khí", "Thể lỏng", "Thể rắn", "Dễ bay hơi"], 2,
           "Lực hút giữa các ion rất mạnh nên hợp chất ion thường ở thể rắn.", "hieu"),
        TN("Chất nào sau đây khi tan trong nước tạo dung dịch dẫn được điện?",
           ["Dầu ăn", "Đường (C₁₂H₂₂O₁₁)", "Muối ăn (NaCl)", "Bột mì"], 2,
           "NaCl là hợp chất ion; khi tan trong nước tạo các ion chuyển động được nên dẫn điện.", "van_dung"),
        TN("Trong phân tử H₂, hai nguyên tử H dùng chung bao nhiêu cặp electron?",
           ["1 cặp", "2 cặp", "3 cặp", "Không có"], 0,
           "Mỗi H góp 1 electron ⇒ 1 cặp electron dùng chung.", "van_dung"),
        TN("Trong phân tử N₂, hai nguyên tử N dùng chung bao nhiêu cặp electron? (N có 5 electron lớp ngoài cùng)",
           ["1 cặp", "2 cặp", "3 cặp", "4 cặp"], 2,
           "Mỗi N cần thêm 3 electron ⇒ hai nguyên tử dùng chung 3 cặp electron.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Ion được tạo thành khi nguyên tử Magnesium nhường 2 electron mang điện tích bao nhiêu? (Ghi dạng 2+)",
           ["2+", "+2"], giai_thich="Mất 2 electron ⇒ ion Mg²⁺ mang điện tích 2+."),
        BT("Trong phân tử O₂, hai nguyên tử oxygen dùng chung bao nhiêu cặp electron?",
           ["2"], giai_thich="Mỗi O cần thêm 2 electron ⇒ hai nguyên tử dùng chung 2 cặp electron."),
        BT("Chỉ ra loại liên kết trong phân tử muối ăn NaCl và giải thích ngắn gọn.",
           "Liên kết ion: Na nhường 1e thành Na⁺, Cl nhận 1e thành Cl⁻, hai ion trái dấu hút nhau.",
           giai_thich="Liên kết giữa kim loại điển hình và phi kim điển hình.", tu_luan=True),
        BT("Nêu hai điểm khác nhau về tính chất giữa hợp chất ion (như NaCl) và hợp chất cộng hóa trị (như H₂O, CO₂).",
           "Hợp chất ion: thể rắn, nhiệt độ nóng chảy/sôi cao. Hợp chất cộng hóa trị: có thể ở thể lỏng/khí, nhiệt độ nóng chảy/sôi thấp hơn.",
           giai_thich="Lực hút giữa các ion trong hợp chất ion rất mạnh nên cần nhiều nhiệt để phá vỡ.", tu_luan=True),
    ],

    "bt_nang_cao": [
        BT("Nguyên tử A nhường 2 electron để tạo ion, nguyên tử B nhận 1 electron để tạo ion. Hợp chất tạo bởi A và B có công thức chung là gì? Thuộc loại liên kết nào?",
           "AB₂ – liên kết ion.",
           goi_y="A tạo ion A²⁺, B tạo ion B⁻. Cần bao nhiêu ion B⁻ để trung hòa một ion A²⁺?",
           loi_giai="Một ion A²⁺ cần hai ion B⁻ để tổng điện tích bằng 0 ⇒ công thức AB₂. Do có sự nhường – nhận electron tạo ion trái dấu nên đây là liên kết ion.",
           tu_luan=True),
        BT("Vì sao ở điều kiện thường, khí nitrogen (N₂) rất khó tham gia phản ứng hóa học?",
           "Vì giữa hai nguyên tử N có liên kết rất bền.",
           goi_y="Hai nguyên tử N dùng chung mấy cặp electron?",
           loi_giai="Hai nguyên tử N dùng chung 3 cặp electron (liên kết ba N≡N). Liên kết này rất bền, cần nhiều năng lượng mới phá vỡ được.",
           tu_luan=True),
        BT("Cho các chất: nước (H₂O), muối ăn (NaCl), đường (C₁₂H₂₂O₁₁), khí ammonia (NH₃). Chất nào khi tan trong nước tạo dung dịch dẫn điện tốt? Vì sao?",
           "Muối ăn NaCl.",
           goi_y="Xét loại liên kết trong từng chất.",
           loi_giai="NaCl là hợp chất ion; khi tan trong nước tạo các ion Na⁺ và Cl⁻ chuyển động tự do nên dẫn điện. Các chất còn lại là hợp chất cộng hóa trị.",
           tu_luan=True),
        BT("Phân tử CO₂ có nguyên tử C ở giữa liên kết với 2 nguyên tử O. Hãy mô tả sự dùng chung electron trong phân tử (C có 4e, O có 6e lớp ngoài cùng).",
           "Giữa C và mỗi nguyên tử O có 2 cặp electron dùng chung: O=C=O.",
           goi_y="C cần thêm 4 electron, mỗi O cần thêm 2 electron.",
           loi_giai="Mỗi O góp 2 electron dùng chung với C, C góp 2 electron với mỗi O ⇒ giữa C và mỗi O có 2 cặp electron dùng chung (O=C=O). Cả ba nguyên tử đều có 8 electron lớp ngoài cùng.",
           tu_luan=True),
        BT("(Mở rộng) Vì sao kim loại dẫn điện tốt?",
           "Vì trong kim loại có các electron chuyển động tự do.",
           goi_y="Electron lớp ngoài cùng của kim loại liên kết với hạt nhân yếu hay mạnh?",
           loi_giai="Electron lớp ngoài cùng của kim loại dễ tách khỏi nguyên tử, chuyển động tự do trong khối kim loại; khi có hiệu điện thế, các electron này chuyển động có hướng tạo thành dòng điện.",
           tu_luan=True),
    ],
}

# ---------------------------- BÀI 7 ----------------------------------
C2["Bài 7: Hóa trị và công thức hóa học"] = {
    "ly_thuyet": """📌 1. HÓA TRỊ
- Hóa trị là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác; được ghi bằng chữ số La Mã.
- Quy ước: hydrogen có hóa trị I; oxygen có hóa trị II.
- Một nguyên tố có thể có nhiều hóa trị. Ví dụ: Fe (II, III); S (II, IV, VI); C (II, IV).
- Hóa trị một số nguyên tố và nhóm nguyên tử thường gặp:
  I: H, Na, K, Ag, Cl (khi liên kết với H hoặc kim loại); nhóm OH, NO₃
  II: O, Mg, Ca, Ba, Zn, Cu (thường gặp); nhóm SO₄, CO₃
  III: Al; nhóm PO₄
  Fe: II hoặc III; C: II hoặc IV; N: III (trong NH₃)

📌 2. QUY TẮC HÓA TRỊ
- Trong hợp chất AₓBᵧ (A hóa trị a, B hóa trị b): x · a = y · b.

📌 3. CÔNG THỨC HÓA HỌC (CTHH)
- Đơn chất kim loại và một số phi kim rắn: viết kí hiệu (Fe, Cu, C, S).
- Đơn chất phi kim dạng khí: kí hiệu + chỉ số (O₂, H₂, N₂, Cl₂).
- Hợp chất: kí hiệu các nguyên tố + chỉ số (H₂O, NaCl, CaCO₃).
- Ý nghĩa CTHH: cho biết các nguyên tố tạo nên chất, số nguyên tử mỗi nguyên tố trong một phân tử và khối lượng phân tử.

📌 4. LẬP CTHH THEO HÓA TRỊ
- Viết dạng chung AₓBᵧ ⇒ áp dụng x · a = y · b ⇒ x : y = b : a (rút gọn tối giản) ⇒ viết CTHH.

📌 5. TÍNH PHẦN TRĂM NGUYÊN TỐ TRONG HỢP CHẤT
- %A = (x × khối lượng nguyên tử A) : khối lượng phân tử × 100%.

📌 6. XÁC ĐỊNH CTHH KHI BIẾT % NGUYÊN TỐ VÀ KHỐI LƯỢNG PHÂN TỬ
- Khối lượng của A trong phân tử = %A × khối lượng phân tử ⇒ số nguyên tử A = khối lượng đó : khối lượng nguyên tử A.""",

    "vi_du": """💡 VÍ DỤ 1: Lập CTHH theo hóa trị
Lập CTHH của hợp chất tạo bởi Aluminium (III) và Oxygen (II).
- Dạng chung AlₓOᵧ: x · III = y · II ⇒ x : y = 2 : 3 ⇒ Al₂O₃.

💡 VÍ DỤ 2: Tính phần trăm nguyên tố
Tính phần trăm khối lượng của C trong CO₂ (C = 12, O = 16).
- Khối lượng phân tử CO₂ = 44 amu ⇒ %C = 12 : 44 × 100% ≈ 27,27%; %O ≈ 72,73%.

💡 VÍ DỤ 3: Xác định CTHH
Hợp chất của sulfur và oxygen có khối lượng phân tử 64 amu, trong đó S chiếm 50%. Tìm CTHH.
- Khối lượng S = 50% × 64 = 32 ⇒ 1 nguyên tử S; khối lượng O = 64 – 32 = 32 ⇒ 2 nguyên tử O ⇒ SO₂.""",

    "cau_hoi": [
        TN("Theo quy ước, hóa trị của hydrogen (H) và oxygen (O) trong hợp chất là:",
           ["H hóa trị I, O hóa trị I", "H hóa trị II, O hóa trị I", "H hóa trị I, O hóa trị II", "H hóa trị II, O hóa trị II"], 2,
           "Đây là quy ước dùng làm cơ sở để xác định hóa trị của các nguyên tố khác.", "biet"),
        TN("Trong hợp chất AₓBᵧ (a, b lần lượt là hóa trị của A, B), quy tắc hóa trị được viết là:",
           ["x + a = y + b", "x · b = y · a", "x · a = y · b", "a : x = b : y"], 2,
           "Tích chỉ số và hóa trị của nguyên tố này bằng tích chỉ số và hóa trị của nguyên tố kia.", "biet"),
        TN("Các kim loại kiềm (nhóm IA) có hóa trị bao nhiêu trong hợp chất?",
           ["I", "II", "III", "IV"], 0,
           "Nhóm IA có 1 electron lớp ngoài cùng nên có hóa trị I.", "hieu"),
        TN("Hóa trị của carbon (C) trong CO₂ là bao nhiêu?",
           ["I", "II", "III", "IV"], 3,
           "a × 1 = II × 2 ⇒ a = IV.", "van_dung"),
        TN("Hóa trị của sulfur (S) trong SO₃ là bao nhiêu?",
           ["II", "III", "IV", "VI"], 3,
           "a × 1 = II × 3 ⇒ a = VI.", "van_dung"),
        TN("Hóa trị của sulfur (S) trong H₂S là bao nhiêu?",
           ["I", "II", "III", "IV"], 1,
           "I × 2 = a × 1 ⇒ a = II.", "van_dung"),
        TN("Hóa trị của nitrogen (N) trong NH₃ là bao nhiêu?",
           ["I", "II", "III", "IV"], 2,
           "a × 1 = I × 3 ⇒ a = III.", "van_dung"),
        TN("Nhóm SO₄ có hóa trị II. Hóa trị của Al trong Al₂(SO₄)₃ là:",
           ["I", "II", "III", "IV"], 2,
           "a × 2 = II × 3 ⇒ a = III.", "van_dung"),
        TN("CTHH của hợp chất tạo bởi Fe (hóa trị III) và Cl (hóa trị I) là:",
           ["FeCl", "FeCl₂", "FeCl₃", "Fe₃Cl"], 2,
           "x : y = I : III = 1 : 3 ⇒ FeCl₃.", "van_dung"),
        TN("CTHH của hợp chất tạo bởi Ca (hóa trị II) và O (hóa trị II) là:",
           ["Ca₂O", "CaO₂", "CaO", "Ca₂O₂"], 2,
           "x : y = II : II = 1 : 1 ⇒ CaO.", "van_dung"),
        TN("Nhóm OH có hóa trị I. CTHH đúng của magnesium hydroxide (Mg hóa trị II) là:",
           ["MgOH", "Mg₂OH", "Mg(OH)₂", "Mg(OH)₃"], 2,
           "x : y = I : II = 1 : 2 ⇒ Mg(OH)₂.", "van_dung"),
        TN("Biết K có hóa trị I, Cl có hóa trị I, O có hóa trị II, nhóm OH có hóa trị I. CTHH nào viết SAI?",
           ["K₂O", "KCl₂", "KCl", "KOH"], 1,
           "K (I) và Cl (I) kết hợp theo tỉ lệ 1 : 1 ⇒ KCl, không phải KCl₂.", "van_dung"),
        TN("Phần trăm khối lượng của O trong H₂O là bao nhiêu? (H = 1, O = 16)",
           ["11,11%", "88,89%", "50%", "66,67%"], 1,
           "%O = 16 : 18 × 100% ≈ 88,89%.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Xác định hóa trị của N trong NH₃ (H hóa trị I). Ghi bằng chữ số La Mã hoặc số.",
           ["III", "3"], giai_thich="a × 1 = I × 3 ⇒ a = III."),
        BT("Xác định hóa trị của Fe trong Fe₂O₃. Ghi bằng chữ số La Mã hoặc số.",
           ["III", "3"], giai_thich="a × 2 = II × 3 ⇒ a = III."),
        BT("Lập CTHH của hợp chất tạo bởi C (hóa trị IV) và O (hóa trị II).",
           ["CO2", "CO₂"], giai_thich="x : y = II : IV = 1 : 2 ⇒ CO₂."),
        BT("Lập CTHH của hợp chất tạo bởi K (hóa trị I) và nhóm SO₄ (hóa trị II).",
           ["K2SO4", "K₂SO₄"], giai_thich="x : y = II : I = 2 : 1 ⇒ K₂SO₄."),
        BT("Tính phần trăm khối lượng của Ca trong CaCO₃ (Ca = 40, C = 12, O = 16). Chỉ ghi con số.",
           ["40", "40%"], giai_thich="%Ca = 40 : 100 × 100% = 40%."),
        BT("Nêu ý nghĩa của công thức hóa học H₂O.",
           "H₂O là hợp chất tạo bởi 2 nguyên tố H và O; một phân tử có 2 nguyên tử H và 1 nguyên tử O; khối lượng phân tử 18 amu.",
           giai_thich="CTHH cho biết: nguyên tố tạo nên chất, số nguyên tử mỗi nguyên tố, khối lượng phân tử.", tu_luan=True),
    ],

    "bt_nang_cao": [
        BT("Hợp chất A tạo bởi nguyên tố M (hóa trị III) và nhóm SO₄ (hóa trị II), có khối lượng phân tử 342 amu. M là nguyên tố nào? (S = 32, O = 16)",
           ["Al", "Aluminium", "Nhôm"],
           goi_y="Lập công thức chung M₂(SO₄)₃.",
           loi_giai="2·M + 3 × (32 + 4 × 16) = 342 ⇒ 2·M + 288 = 342 ⇒ M = 27 ⇒ Aluminium (Al)."),
        BT("Một hợp chất gồm N và H, có khối lượng phân tử 17 amu, trong đó N chiếm 82,35% khối lượng. Tìm CTHH của hợp chất.",
           ["NH3", "NH₃"],
           goi_y="Khối lượng N trong phân tử = 82,35% × 17.",
           loi_giai="Khối lượng N ≈ 14 ⇒ 1 nguyên tử N; khối lượng H = 17 – 14 = 3 ⇒ 3 nguyên tử H ⇒ NH₃."),
        BT("Lập CTHH của một oxide của sắt, biết tỉ lệ khối lượng Fe : O = 7 : 3. (Fe = 56, O = 16)",
           ["Fe2O3", "Fe₂O₃"],
           goi_y="Tỉ lệ số nguyên tử = tỉ lệ (khối lượng : khối lượng nguyên tử).",
           loi_giai="x : y = (7 : 56) : (3 : 16) = 0,125 : 0,1875 = 2 : 3 ⇒ Fe₂O₃."),
        BT("Hợp chất X gồm Cu, S, O có khối lượng phân tử 160 amu; Cu chiếm 40%, S chiếm 20%, còn lại là O. Tìm CTHH của X. (Cu = 64, S = 32, O = 16)",
           ["CuSO4", "CuSO₄"],
           goi_y="Tính khối lượng từng nguyên tố trong một phân tử rồi chia cho khối lượng nguyên tử.",
           loi_giai="Cu: 40% × 160 = 64 ⇒ 1 nguyên tử; S: 20% × 160 = 32 ⇒ 1 nguyên tử; O: 160 – 96 = 64 ⇒ 4 nguyên tử ⇒ CuSO₄."),
        BT("Tính hóa trị của Fe trong FeO và trong Fe₂O₃. Em có nhận xét gì về hóa trị của một nguyên tố?",
           "FeO: Fe hóa trị II; Fe₂O₃: Fe hóa trị III.",
           goi_y="Áp dụng quy tắc hóa trị với O hóa trị II.",
           loi_giai="FeO: a × 1 = II × 1 ⇒ a = II. Fe₂O₃: a × 2 = II × 3 ⇒ a = III. Nhận xét: một nguyên tố có thể có nhiều hóa trị khác nhau tùy hợp chất.",
           tu_luan=True),
        BT("Chỉ dùng quy tắc hóa trị, hãy giải thích vì sao CTHH của nước là H₂O chứ không phải HO₂.",
           "Vì x : y = II : I = 2 : 1.",
           goi_y="Viết dạng chung HₓOᵧ rồi áp dụng quy tắc hóa trị.",
           loi_giai="x · I = y · II ⇒ x : y = 2 : 1 ⇒ H₂O. Với HO₂: 1 × I ≠ 2 × II nên không thỏa mãn quy tắc hóa trị.",
           tu_luan=True),
    ],
}

# ---------------------- ÔN TẬP CHƯƠNG 2 --------------------------------
C2["Ôn tập Chương 2 – Nâng cao"] = {
    "ly_thuyet": """📌 TÓM TẮT KIẾN THỨC CHƯƠNG 2
- Phân tử: hạt đại diện cho chất. Khối lượng phân tử = tổng khối lượng các nguyên tử.
- Đơn chất: một nguyên tố. Hợp chất: từ hai nguyên tố trở lên.
- Liên kết ion: kim loại – phi kim (nhường, nhận electron). Liên kết cộng hóa trị: phi kim – phi kim (dùng chung electron).
- Quy tắc hóa trị: x · a = y · b ⇒ lập CTHH, tính hóa trị.
- %A = (x × A) : khối lượng phân tử × 100%.

📌 MẸO LÀM BÀI
- Khi lập CTHH có nhóm nguyên tử (OH, SO₄, NO₃, CO₃, PO₄) với chỉ số lớn hơn 1, nhớ đặt nhóm trong ngoặc: Mg(OH)₂, Al₂(SO₄)₃.
- Luôn rút gọn tỉ lệ x : y về tối giản (C₂O₄ ⇒ CO₂).""",

    "vi_du": """💡 VÍ DỤ: Hợp chất của X với O là X₂O₃; hợp chất của Y với H là H₂Y. Lập CTHH của hợp chất tạo bởi X và Y.
- X₂O₃: x × 2 = II × 3 ⇒ X hóa trị III.
- H₂Y: I × 2 = y × 1 ⇒ Y hóa trị II.
- Hợp chất X và Y: x : y = II : III = 2 : 3 ⇒ X₂Y₃.""",

    "cau_hoi": [
        TN("Khối lượng phân tử của Fe₂O₃ là bao nhiêu? (Fe = 56, O = 16)",
           ["160 amu", "72 amu", "88 amu", "232 amu"], 0,
           "2 × 56 + 3 × 16 = 160 amu.", "van_dung"),
        TN("Chất nào sau đây vừa là hợp chất, vừa có liên kết ion?",
           ["Cl₂", "KCl", "H₂", "CO₂"], 1,
           "KCl tạo bởi kim loại K và phi kim Cl.", "hieu"),
        TN("CTHH của hợp chất tạo bởi Al (hóa trị III) và nhóm NO₃ (hóa trị I) là:",
           ["AlNO₃", "Al₃NO₃", "Al(NO₃)₃", "Al(NO₃)₂"], 2,
           "x : y = I : III = 1 : 3 ⇒ Al(NO₃)₃.", "van_dung"),
        TN("Phần trăm khối lượng của N trong NH₄NO₃ là bao nhiêu? (N = 14, H = 1, O = 16)",
           ["17,5%", "35%", "28%", "46,7%"], 1,
           "Khối lượng phân tử = 80 amu; %N = 2 × 14 : 80 × 100% = 35%.", "van_dung"),
        TN("Trong các khí H₂, O₂, N₂, CO₂, khí nào có khối lượng phân tử lớn nhất?",
           ["H₂", "O₂", "N₂", "CO₂"], 3,
           "H₂ = 2, N₂ = 28, O₂ = 32, CO₂ = 44 amu.", "van_dung"),
        TN("X tạo với O hợp chất X₂O₃; Y tạo với H hợp chất H₂Y. CTHH của hợp chất giữa X và Y là:",
           ["XY", "X₂Y₃", "X₃Y₂", "XY₂"], 1,
           "X hóa trị III, Y hóa trị II ⇒ X₂Y₃.", "van_dung"),
    ],

    "bt_co_ban": [
        BT("Tính khối lượng phân tử của Al(NO₃)₃ (Al = 27, N = 14, O = 16), đơn vị amu.",
           ["213"], giai_thich="27 + 3 × (14 + 3 × 16) = 27 + 186 = 213 amu."),
        BT("Tính khối lượng phân tử của Ca₃(PO₄)₂ (Ca = 40, P = 31, O = 16), đơn vị amu.",
           ["310"], giai_thich="3 × 40 + 2 × (31 + 4 × 16) = 120 + 190 = 310 amu."),
    ],

    "bt_nang_cao": [
        BT("Hợp chất M₂O₃ có khối lượng phân tử 102 amu. M giữ nguyên hóa trị khi tạo hợp chất với Cl (hóa trị I). Lập CTHH hợp chất của M với Cl và tính khối lượng phân tử của nó. (O = 16, Cl = 35,5)",
           "AlCl₃ – 133,5 amu.",
           goi_y="Tìm M từ M₂O₃ trước; M có hóa trị III.",
           loi_giai="2·M + 48 = 102 ⇒ M = 27 (Al), hóa trị III ⇒ AlCl₃. Khối lượng phân tử = 27 + 3 × 35,5 = 133,5 amu.",
           tu_luan=True),
        BT("Một oxide của nitrogen có khối lượng phân tử 46 amu, trong đó N chiếm khoảng 30,43%. Tìm CTHH của oxide. (N = 14, O = 16)",
           ["NO2", "NO₂"],
           goi_y="Khối lượng N trong phân tử ≈ 30,43% × 46.",
           loi_giai="Khối lượng N ≈ 14 ⇒ 1 nguyên tử N; khối lượng O = 46 – 14 = 32 ⇒ 2 nguyên tử O ⇒ NO₂."),
        BT("Nguyên tố R có hóa trị II tạo với oxygen một oxide, trong đó O chiếm 20% khối lượng. R là nguyên tố nào? (O = 16)",
           ["Cu", "Copper", "Đồng"],
           goi_y="R hóa trị II ⇒ công thức RO. Lập: 16 : (R + 16) = 20%.",
           loi_giai="R + 16 = 16 : 0,2 = 80 ⇒ R = 64 ⇒ Copper (Cu); oxide là CuO."),
        BT("Xác định hóa trị của nhóm PO₄ trong Ca₃(PO₄)₂, biết Ca có hóa trị II.",
           ["III", "3"],
           goi_y="Gọi hóa trị nhóm PO₄ là a; áp dụng quy tắc hóa trị.",
           loi_giai="3 × II = 2 × a ⇒ a = III."),
        BT("(Bồi dưỡng HSG) Muối ăn NaCl có khối lượng phân tử 58,5 amu. Một hạt muối nặng 1 gam chứa khoảng bao nhiêu phân tử NaCl? (1 amu ≈ 1,66 × 10⁻²⁴ gam)",
           "Khoảng 1,03 × 10²² phân tử.",
           goi_y="Đổi khối lượng một phân tử ra gam, rồi lấy 1 gam chia cho số đó.",
           loi_giai="Một phân tử nặng 58,5 × 1,66 × 10⁻²⁴ ≈ 9,71 × 10⁻²³ gam. Số phân tử ≈ 1 : (9,71 × 10⁻²³) ≈ 1,03 × 10²² phân tử.",
           tu_luan=True),
    ],
}

H7["Chương 2: Phân tử. Liên kết hóa học"] = C2

HOA["Lớp 7"] = H7
