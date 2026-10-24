# -*- coding: utf-8 -*-
"""
NGÂN HÀNG DỮ LIỆU MÔN VẬT LÝ LỚP 7 — Bộ Kết Nối Tri Thức (KHTN)

Cấu trúc (app.py đọc đúng cấu trúc này):
  VATLY["Lớp 7"][Chương][Bài] = {
      ly_thuyet, vi_du, cau_hoi, bt_co_ban, bt_nang_cao
  }
  - cau_hoi:      q(nd, da, d, gt)           d = chỉ số đáp án đúng
  - bt_co_ban:    bt(de, dd, gt)             dd = danh sách đáp án chấp nhận
  - bt_nang_cao:  nc(de, hd, dd, lg)         hd = gợi ý, lg = lời giải

Hàm kiem_tra_vatly() kiểm tra lỗi dữ liệu; chạy trực tiếp file để xem kết quả.
"""


# ============================================================
# HÀM TẠO DỮ LIỆU
# ============================================================
def q(nd, da, d, gt=""):
    return {"nd": nd, "da": da, "d": d, "gt": gt}


def bt(de, dd, gt=""):
    return {"de": de, "dd": dd, "gt": gt}


def nc(de, hd, dd, lg=""):
    return {"de": de, "hd": hd, "dd": dd, "lg": lg}


def bai(ly_thuyet, vi_du, cau_hoi, bt_co_ban, bt_nang_cao):
    return {
        "ly_thuyet": ly_thuyet,
        "vi_du": vi_du,
        "cau_hoi": cau_hoi,
        "bt_co_ban": bt_co_ban,
        "bt_nang_cao": bt_nang_cao,
    }


# ============================================================
# CHƯƠNG 1: TỐC ĐỘ CHUYỂN ĐỘNG
# ============================================================
C1_B1 = bai(
    ly_thuyet="""📌 1. TỐC ĐỘ
- Tốc độ cho biết mức độ nhanh hay chậm của chuyển động.
- Công thức: v = s / t (s: quãng đường, t: thời gian, v: tốc độ).
- Đơn vị hợp pháp (hệ SI): mét trên giây (m/s). Trong thực tế hay dùng km/h.
- Quy đổi: 1 m/s = 3,6 km/h; 1 km/h = 1/3,6 m/s.
  Ví dụ: 36 km/h = 10 m/s; 20 m/s = 72 km/h.

📌 2. TỐC ĐỘ TRUNG BÌNH
- Tốc độ trung bình = tổng quãng đường / tổng thời gian.
- KHÔNG lấy trung bình cộng các tốc độ khi thời gian đi các đoạn khác nhau.
- Với hai đoạn đường s như nhau đi với v1 và v2: v_tb = 2·v1·v2 / (v1 + v2).

📌 3. ĐO TỐC ĐỘ
- Đo tốc độ trung bình: thước đo quãng đường + đồng hồ bấm giây.
- Cổng quang điện + đồng hồ hiện số: tự động đo thời gian khi vật đi qua.
- Tốc kế (xe máy, ô tô): cho biết tốc độ tức thời tại thời điểm quan sát.
- Súng bắn tốc độ (cảnh sát giao thông): dùng sóng radar hoặc laser.

📌 4. TỐC ĐỘ MỘT SỐ CHUYỂN ĐỘNG QUEN THUỘC
- Người đi bộ: khoảng 1,2 m/s (4 km/h).
- Xe đạp: khoảng 4 – 6 m/s.
- Âm thanh trong không khí: khoảng 340 m/s.
- Ánh sáng trong chân không: khoảng 300 000 km/s.""",

    vi_du="""💡 VÍ DỤ 1: Đổi đơn vị và tính tốc độ
Một xe máy đi quãng đường 60 km trong 1 giờ 30 phút.
- Đổi 1 giờ 30 phút = 1,5 h. v = 60 / 1,5 = 40 km/h.
- Đổi sang m/s: 40 / 3,6 ≈ 11,1 m/s.

💡 VÍ DỤ 2: Tốc độ trung bình không phải trung bình cộng
Một người đi 60 km trong 1 giờ, rồi đi tiếp 60 km trong 2 giờ.
- Tổng quãng đường 120 km; tổng thời gian 3 giờ.
- v_tb = 120 / 3 = 40 km/h (không phải (60 + 30) / 2 = 45 km/h).

💡 VÍ DỤ 3: Quy đổi để so sánh
Xe A chạy 25 m/s, xe B chạy 90 km/h. Ai nhanh hơn?
- 90 km/h = 25 m/s. Hai xe bằng nhau.""",

    cau_hoi=[
        q("Tốc độ là đại lượng cho biết điều gì?", ["Mức độ nhanh hay chậm của chuyển động", "Quãng đường vật đi được", "Thời gian vật chuyển động", "Quỹ đạo của vật"], 0, "Định nghĩa tốc độ."),
        q("Công thức tính tốc độ là:", ["v = s.t", "v = s/t", "v = t/s", "v = s + t"], 1),
        q("Đơn vị tốc độ trong hệ SI là:", ["km/h", "m/s", "cm/s", "m/phút"], 1),
        q("Đổi 36 km/h sang m/s:", ["10 m/s", "3,6 m/s", "100 m/s", "360 m/s"], 0, "36 : 3,6 = 10"),
        q("Đổi 20 m/s sang km/h:", ["20 km/h", "72 km/h", "60 km/h", "80 km/h"], 1, "20 × 3,6 = 72"),
        q("Đổi 72 km/h sang m/s:", ["20 m/s", "7,2 m/s", "72 m/s", "259,2 m/s"], 0, "72 : 3,6 = 20"),
        q("Đổi 5 m/s sang km/h:", ["18 km/h", "5 km/h", "1,39 km/h", "50 km/h"], 0, "5 × 3,6 = 18"),
        q("Ô tô đi 120 km trong 2 giờ, tốc độ là:", ["60 km/h", "240 km/h", "120 km/h", "30 km/h"], 0),
        q("Vật đi 300 m trong 1 phút, tốc độ là:", ["5 m/s", "300 m/s", "18 m/s", "0,2 m/s"], 0, "60 s, 300 : 60 = 5 m/s"),
        q("Một vật đi 1 km trong 10 phút. Tốc độ theo km/h là:", ["6 km/h", "10 km/h", "0,1 km/h", "60 km/h"], 0, "10 phút = 1/6 h; 1 : 1/6 = 6 km/h"),
        q("Đi với tốc độ 12 m/s trong 30 phút, quãng đường là:", ["21,6 km", "21 600 km", "0,36 km", "720 m"], 0, "1800 s × 12 m/s = 21 600 m"),
        q("Xe đi 60 km trong 1 giờ, sau đó đi 60 km trong 2 giờ. Tốc độ trung bình cả hành trình là:", ["40 km/h", "45 km/h", "50 km/h", "30 km/h"], 0, "Tổng 120 km ÷ tổng 3 h = 40 km/h"),
        q("Dụng cụ đo tốc độ tức thời gắn trên xe máy, ô tô là:", ["Tốc kế", "Lực kế", "Nhiệt kế", "Vôn kế"], 0),
        q("Người chạy 100 m trong 10 s, tốc độ là:", ["1 m/s", "10 m/s", "100 m/s", "0,1 m/s"], 1),
        q("Con rùa bò 1,2 m trong 1 phút. Tốc độ rùa là:", ["0,02 m/s", "0,2 m/s", "2 m/s", "1,2 m/s"], 0, "1,2 : 60 = 0,02 m/s"),
        q("Tốc độ âm thanh trong không khí khoảng 340 m/s, tương đương:", ["340 km/h", "1224 km/h", "3400 km/h", "12,24 km/h"], 1, "340 × 3,6 = 1224"),
        q("Tốc độ ánh sáng (300 000 km/s) lớn hơn tốc độ âm trong không khí khoảng:", ["882 lần", "88 lần", "8820 lần", "340 lần"], 0, "300 000 : 340 ≈ 882"),
        q("Cổng quang điện trong phòng thực hành dùng để:", ["Đo nhiệt độ", "Tự động bật/tắt đồng hồ khi vật đi qua", "Đo khoảng cách", "Chiếu sáng"], 1),
        q("Muốn đo tốc độ chạy 60 m của học sinh, cần dùng:", ["Thước đo độ dài và đồng hồ bấm giây", "Lực kế và cân", "Nhiệt kế và thước", "Vôn kế và ampe kế"], 0),
    ],

    bt_co_ban=[
        bt("Đổi: a) 18 km/h = ? m/s;  b) 5 m/s = ? km/h", ["a) 5 m/s; b) 18 km/h", "5 m/s; 18 km/h"], "18 : 3,6 = 5;  5 × 3,6 = 18."),
        bt("Học sinh đi từ nhà đến trường dài 1,5 km mất 20 phút. Tính tốc độ theo km/h và m/s.", ["4,5 km/h và 1,25 m/s", "4,5 km/h; 1,25 m/s"], "20 phút = 1/3 h; v = 1,5 : 1/3 = 4,5 km/h; 4,5 : 3,6 = 1,25 m/s."),
        bt("Chim đại bàng bay với tốc độ 25 m/s. Bay hết quãng đường 18 km mất bao nhiêu phút?", ["12", "12 phút"], "18 000 : 25 = 720 s = 12 phút."),
        bt("Xe đi từ A đến B với tốc độ 40 km/h trong 1 giờ 15 phút. Tính quãng đường AB.", ["50 km", "50"], "1,25 h × 40 km/h = 50 km."),
        bt("Một đoàn tàu dài 150 m lướt qua cột điện trong 10 s. Tính tốc độ của tàu (m/s).", ["15 m/s", "15"], "Quãng đường tàu đi = chiều dài tàu: 150 : 10 = 15 m/s."),
        bt("Xe chạy 25 m/s. Trong 0,4 s (thời gian phản ứng), xe đi thêm quãng đường bao nhiêu mét?", ["10 m", "10"], "25 × 0,4 = 10 m."),
    ],

    bt_nang_cao=[
        nc("Hai thành phố A và B cách nhau 120 km. Ô tô đi từ A đến B với 50 km/h. Nửa giờ sau, xe máy đi từ B về A với 45 km/h. Sau bao lâu kể từ lúc xe máy khởi hành thì hai xe gặp nhau?",
           "Tính quãng đường ô tô đi trước, rồi dùng tổng vận tốc.",
           ["1 giờ", "1"],
           "Ô tô đi trước 0,5 h được 25 km; còn lại 95 km; 95 : (50 + 45) = 1 h."),
        nc("Người đi xe đạp đi 1/3 quãng đường đầu với 15 km/h và 2/3 quãng đường còn lại với 10 km/h. Tính tốc độ trung bình cả quãng đường.",
           "v_tb = tổng quãng đường : tổng thời gian.",
           ["11,25 km/h", "11,25"],
           "Gọi quãng đường là S. t1 = (S/3)/15 = S/45; t2 = (2S/3)/10 = S/15 = 3S/45; t = 4S/45; v_tb = 45/4 = 11,25 km/h."),
        nc("Canô xuôi dòng từ A đến B mất 2 giờ, ngược dòng từ B về A mất 3 giờ. Vận tốc dòng nước 5 km/h. Tính vận tốc thực của canô và quãng đường AB.",
           "v_xuôi = v + 5; v_ngược = v − 5; quãng đường AB như nhau.",
           ["25 km/h và 60 km", "25 km/h; 60 km"],
           "2(v + 5) = 3(v − 5) ⇒ v = 25 km/h; AB = 2(25 + 5) = 60 km."),
        nc("Xe A khởi hành từ A lúc 7 h với 40 km/h. Xe B khởi hành từ B (cách A 100 km) lúc 8 h, chạy về A với 60 km/h. Hai xe gặp nhau lúc mấy giờ và cách A bao nhiêu km?",
           "Chọn gốc tại A, tính vị trí mỗi xe theo thời gian t (giờ, tính từ 7 h).",
           ["8 giờ 36 phút; cách A 64 km", "8h36; 64 km"],
           "Xe A: x = 40t. Xe B: x = 100 − 60(t − 1). Giải 40t = 160 − 60t ⇒ t = 1,6 h = 1 h 36 phút; x = 64 km."),
        nc("Một người đi bộ quãng đường 3 km: 2 km đầu với 4 km/h, 1 km sau với 6 km/h. Tính tốc độ trung bình.",
           "Tính thời gian từng đoạn rồi chia tổng quãng đường cho tổng thời gian.",
           ["4,5 km/h", "4,5"],
           "t1 = 2/4 = 0,5 h; t2 = 1/6 h; t = 2/3 h; v_tb = 3 : 2/3 = 4,5 km/h (không phải 5 km/h)."),
        nc("Tàu dài 200 m chạy với 72 km/h qua cầu dài 800 m. Tính thời gian từ lúc đầu tàu lên cầu đến khi đuôi tàu rời khỏi cầu.",
           "Quãng đường tàu phải đi = chiều dài cầu + chiều dài tàu.",
           ["50 giây", "50"],
           "72 km/h = 20 m/s; 1000 m : 20 m/s = 50 s."),
        nc("Xe ô tô chạy 72 km/h. Thời gian phản ứng của tài xế là 0,5 s. Sau khi đạp phanh, xe đi thêm 40 m mới dừng. Chướng ngại vật cách xe 60 m lúc tài xế phát hiện. Xe có đâm vào chướng ngại vật không?",
           "Quãng đường tổng = quãng đường phản ứng + quãng đường phanh.",
           ["Không đâm: tổng quãng đường 50 m < 60 m"],
           "Quãng đường phản ứng = 20 m/s × 0,5 s = 10 m; tổng = 10 + 40 = 50 m < 60 m."),
    ],
)

C1_B2 = bai(
    ly_thuyet="""📌 1. ĐỒ THỊ QUÃNG ĐƯỜNG – THỜI GIAN (s – t)
- Trục nằm ngang (Ot): thời gian t. Trục thẳng đứng (Os): quãng đường s.
- Đường thẳng nghiêng đi qua gốc tọa độ: chuyển động đều. Độ dốc càng lớn, tốc độ càng lớn.
- Đường nằm ngang: vật đứng yên (quãng đường không đổi theo thời gian).
- Đoạn dốc xuống: s giảm theo t, vật chuyển động theo chiều ngược lại với chiều chọn làm mốc.
- Tốc độ trên đồ thị: v = Δs / Δt (lấy hai điểm bất kì trên đoạn thẳng).

📌 2. KHOẢNG CÁCH AN TOÀN
- Khoảng cách an toàn là khoảng cách tối thiểu giữa hai xe để tránh va chạm khi xe trước phanh gấp.
- Quãng đường đi trong thời gian phản ứng: s_pư = v × t_pư (t_pư thường khoảng 0,4 – 0,6 s).
- Quãng đường phanh: phụ thuộc tốc độ, tình trạng đường và tình trạng xe.
- Tốc độ càng cao, khoảng cách an toàn càng lớn.
- Đường trơn (mưa, dầu, lá ướt): ma sát giảm, quãng đường phanh tăng.

📌 3. AN TOÀN GIAO THÔNG
- Tuân thủ biển báo tốc độ tối đa (viền đỏ, nền trắng, có số ghi km/h).
- Điểm mù của xe tải: vùng mà người lái không quan sát được qua gương.
- Không điều khiển phương tiện khi buồn ngủ: quãng đường đi "mù" có thể rất lớn.""",

    vi_du="""💡 VÍ DỤ 1: Tính tốc độ từ đồ thị
Đồ thị s – t của một người đi bộ đi qua gốc (0; 0) và điểm (2 h; 10 km).
- v = Δs / Δt = 10 / 2 = 5 km/h.

💡 VÍ DỤ 2: Đọc đồ thị đoạn nằm ngang
Đồ thị gồm đoạn OA dốc lên (0 → 2 h, s từ 0 → 10 km) và đoạn AB nằm ngang (2 → 3 h).
- OA: chuyển động đều với 5 km/h.
- AB: quãng đường không đổi, người đó đang dừng lại nghỉ.

💡 VÍ DỤ 3: Khoảng cách an toàn
Xe chạy 90 km/h (25 m/s), thời gian phản ứng 0,5 s.
- Quãng đường phản ứng: 25 × 0,5 = 12,5 m.
- Nếu khoảng cách với xe trước chỉ 20 m thì không đủ để phản ứng và phanh an toàn.""",

    cau_hoi=[
        q("Trên đồ thị quãng đường – thời gian, trục nằm ngang biểu diễn:", ["Quãng đường", "Thời gian", "Tốc độ", "Vận tốc"], 1),
        q("Đường biểu diễn là đường thẳng nằm ngang nghĩa là vật:", ["Đứng yên", "Chuyển động đều", "Tăng tốc", "Chuyển động chậm dần"], 0),
        q("Đường thẳng nghiêng đi qua gốc tọa độ nghĩa là vật:", ["Chuyển động đều", "Đứng yên", "Chuyển động nhanh dần", "Dừng lại"], 0),
        q("Trên đồ thị, đường A dốc hơn đường B. Điều đó cho biết:", ["A chậm hơn B", "A nhanh hơn B", "Hai xe bằng nhau", "Không so sánh được"], 1, "Độ dốc càng lớn, tốc độ càng lớn."),
        q("Đồ thị đi qua gốc và điểm (2 h; 60 km). Tốc độ là:", ["30 km/h", "120 km/h", "60 km/h", "20 km/h"], 0),
        q("Đồ thị đi qua (1 h; 40 km) và (3 h; 120 km). Tốc độ trong khoảng 1–3 h là:", ["40 km/h", "80 km/h", "120 km/h", "20 km/h"], 0, "(120 − 40) : (3 − 1) = 40 km/h"),
        q("Đồ thị s – t của vật đứng yên có dạng:", ["Đường nằm ngang", "Đường thẳng dốc lên", "Đường cong", "Đường gấp khúc"], 0),
        q("Đoạn đồ thị dốc xuống (s giảm theo t) cho thấy:", ["Vật chuyển động ngược chiều với chiều chọn làm mốc", "Vật đứng yên", "Vật tăng tốc", "Không có ý nghĩa"], 0),
        q("Khoảng cách an toàn giữa hai xe phụ thuộc chủ yếu vào:", ["Tốc độ của xe", "Màu sơn xe", "Hãng sản xuất", "Số người trên xe"], 0),
        q("Thời gian phản ứng là:", ["Thời gian từ lúc thấy nguy hiểm đến lúc đạp phanh", "Thời gian xe dừng hẳn", "Thời gian đổ xăng", "Thời gian đi từ A đến B"], 0),
        q("Xe chạy 72 km/h (20 m/s), thời gian phản ứng 0,5 s. Quãng đường đi thêm trước khi đạp phanh:", ["10 m", "20 m", "5 m", "36 m"], 0),
        q("Xe chạy 90 km/h, thời gian phản ứng 0,4 s. Quãng đường phản ứng là:", ["10 m", "4 m", "36 m", "90 m"], 0, "25 m/s × 0,4 s = 10 m"),
        q("Khi trời mưa, đường trơn, quãng đường phanh của xe sẽ:", ["Dài hơn", "Ngắn hơn", "Không đổi", "Bằng 0"], 0, "Ma sát giảm nên phanh lâu dừng hơn."),
        q("Biển báo viền đỏ, nền trắng, ghi số 60 có nghĩa là:", ["Tốc độ tối đa cho phép 60 km/h", "Tốc độ tối thiểu 60 km/h", "Cách 60 km đến trạm", "Trọng tải 60 tấn"], 0),
        q("Biển báo 60 km/h. Xe chạy 18 m/s (64,8 km/h). Xe:", ["Không vi phạm", "Vi phạm tốc độ", "Bằng tốc độ cho phép", "Không đủ dữ kiện"], 1),
        q("Điểm mù của xe tải là:", ["Vùng gương chiếu hậu không phản chiếu tới mắt tài xế", "Vùng đèn không sáng", "Vùng cấm đỗ xe", "Vùng kính bị mờ"], 0),
        q("Đồ thị s – t của chuyển động đều là:", ["Đường thẳng nghiêng", "Đường cong parabol", "Đường gấp khúc", "Đường tròn"], 0),
        q("Ô tô đi 40 km/h trong 1 h rồi nghỉ 30 phút. Sau đó đi tiếp 40 km/h trong 1 h. Tốc độ trung bình cả hành trình (tính cả thời gian nghỉ) là:", ["32 km/h", "40 km/h", "80 km/h", "20 km/h"], 0, "Tổng quãng đường 80 km; tổng thời gian 1 + 0,5 + 1 = 2,5 h; 80 : 2,5 = 32 km/h."),
        q("Vì sao không nên lái xe khi buồn ngủ?", ["Vì trong vài giây mất tập trung xe đi được quãng đường rất lớn", "Vì xe sẽ nóng", "Vì đèn xe tắt", "Vì xăng nhanh hết"], 0),
    ],

    bt_co_ban=[
        bt("Đồ thị đi qua gốc (0; 0) và điểm (3 h; 90 km). Tính tốc độ của vật.", ["30 km/h", "30"], "90 : 3 = 30 km/h."),
        bt("Xe đi 0–1 h được 40 km; nghỉ 30 phút; từ 1,5 h đến 2,5 h đi thêm 60 km. Tốc độ trung bình cả hành trình là bao nhiêu?", ["40 km/h", "40"], "Tổng quãng đường 100 km; tổng thời gian 2,5 h; v_tb = 40 km/h."),
        bt("Xe chạy 54 km/h, thời gian phản ứng 0,6 s. Quãng đường đi trong thời gian phản ứng là bao nhiêu mét?", ["9 m", "9"], "54 km/h = 15 m/s; 15 × 0,6 = 9 m."),
        bt("Xe chạy 60 km/h, cách xe trước 20 m. Nếu xe trước phanh gấp, điều gì có thể xảy ra?", ["Có nguy cơ va chạm", "Dễ va chạm"], "Khoảng cách 20 m không đủ để phản ứng và phanh an toàn ở tốc độ này."),
        bt("Một người lái xe nhắm mắt 2 giây khi xe chạy 100 km/h. Xe đi thêm quãng đường bao nhiêu mét trong lúc đó?", ["Khoảng 55,6 m", "55,6", "55"], "100 km/h ≈ 27,8 m/s; 27,8 × 2 ≈ 55,6 m."),
        bt("Một đoàn tàu xuất phát lúc 7 h, đến ga lúc 9 h, quãng đường 150 km, nhưng có dừng 30 phút ở giữa. Tốc độ chuyển động (không tính thời gian dừng) là bao nhiêu?", ["100 km/h", "100"], "Thời gian chuyển động = 2 h − 0,5 h = 1,5 h; 150 : 1,5 = 100 km/h."),
    ],

    bt_nang_cao=[
        nc("Đồ thị s – t của xe buýt: từ 0 đến 1 h đi được 40 km; nghỉ tại trạm 30 phút; sau đó đi tiếp 1 h được thêm 60 km. Tính tốc độ trung bình của xe trong suốt hành trình.",
           "Tổng quãng đường và tổng thời gian (kể cả thời gian nghỉ).",
           ["40 km/h", "40"],
           "Tổng S = 100 km; tổng t = 1 + 0,5 + 1 = 2,5 h; v_tb = 40 km/h."),
        nc("Hai người chạy đua trên đường tròn 400 m, xuất phát cùng vạch, chạy cùng chiều. Người 1: 6 m/s; người 2: 4 m/s. Sau bao lâu người 1 vượt người 2 lần đầu tiên?",
           "Người 1 phải chạy hơn người 2 đúng một vòng.",
           ["200 giây (3 phút 20 giây)", "200"],
           "Hiệu vận tốc = 2 m/s; t = 400 : 2 = 200 s."),
        nc("Thang cuốn đi lên với tốc độ 0,5 m/s. Một người bước trên thang với tốc độ 1 m/s so với thang. Tính tốc độ của người so với mặt đất khi đi cùng chiều và ngược chiều thang.",
           "Cùng chiều: cộng vận tốc; ngược chiều: trừ vận tốc.",
           ["Cùng chiều 1,5 m/s; ngược chiều 0,5 m/s"],
           "v = 1 + 0,5 = 1,5 m/s; v = 1 − 0,5 = 0,5 m/s."),
        nc("Từ điểm A, một xe chạy 30 km/h; sau 1 giờ, xe thứ hai chạy cùng chiều từ A với 50 km/h. Sau bao lâu xe thứ hai đuổi kịp xe thứ nhất và cách A bao nhiêu km?",
           "Xe 1 có quãng đường đi trước 30 km; hiệu vận tốc là 20 km/h.",
           ["Sau 1,5 giờ kể từ khi xe 2 xuất phát; cách A 75 km", "1,5 giờ; 75 km"],
           "Xe 1 đi trước 30 km; t = 30 : (50 − 30) = 1,5 h; quãng đường = 50 × 1,5 = 75 km."),
        nc("Canô đi xuôi dòng từ A đến B hết 2 h, đi ngược từ B về A hết 3 h. Vận tốc dòng nước 4 km/h. Tìm vận tốc thực của canô.",
           "Lập phương trình với quãng đường AB không đổi.",
           ["20 km/h"],
           "AB = 2(v + 4) = 3(v − 4) ⇒ 2v + 8 = 3v − 12 ⇒ v = 20 km/h."),
        nc("Đi xe đạp quanh một vòng hồ chu vi 15 km. Vòng 1 đạp với 15 km/h. Vòng 2 phải đạp với tốc độ bao nhiêu để tốc độ trung bình cả hai vòng là 20 km/h?",
           "Tốc độ trung bình = tổng quãng đường : tổng thời gian (không phải trung bình cộng).",
           ["30 km/h"],
           "Tổng S = 30 km; t_tổng = 30 : 20 = 1,5 h; t_vòng1 = 1 h; t_vòng2 = 0,5 h; v = 15 : 0,5 = 30 km/h."),
        nc("Một tàu chạy 54 km/h đi qua một đường hầm dài 400 m. Đoàn tàu dài 100 m. Tính thời gian từ lúc đầu tàu vào hầm đến khi đuôi tàu ra khỏi hầm.",
           "Quãng đường = chiều dài hầm + chiều dài tàu.",
           ["33,3 giây", "33,3", "33"],
           "54 km/h = 15 m/s; (400 + 100) : 15 ≈ 33,3 s. (Đáp số ≈ 33 giây)"),
        nc("Biển báo giới hạn tốc độ 80 km/h. Một ô tô đang chạy với tốc độ 100 km/h. Xe có vượt quá tốc độ cho phép không?",
           "Đổi đơn vị trước khi so sánh.",
           ["Có, tốc độ 100 km/h lớn hơn 80 km/h"],
           "100 km/h > 80 km/h nên xe đã vượt tốc độ cho phép."),
    ],
)

VL7_CHUONG1 = {
    "Bài 1: Tốc độ và cách đo tốc độ": C1_B1,
    "Bài 2: Đồ thị quãng đường – thời gian và an toàn giao thông": C1_B2,
}


# ============================================================
# CHƯƠNG 2: ÂM THANH
# ============================================================
C2_B1 = bai(
    ly_thuyet="""📌 1. NGUỒN ÂM VÀ SỰ TRUYỀN ÂM
- Vật phát ra âm gọi là nguồn âm. Mọi nguồn âm đều dao động.
- Âm truyền được trong chất rắn, chất lỏng, chất khí. Âm KHÔNG truyền được trong chân không.
- Tốc độ truyền âm: rắn > lỏng > khí. Trong không khí khoảng 340 m/s; trong nước khoảng 1500 m/s; trong thép khoảng 5000 m/s.
- Khi âm đi từ môi trường này sang môi trường khác, tần số không đổi, tốc độ thay đổi.

📌 2. TẦN SỐ VÀ ĐỘ CAO CỦA ÂM
- Tần số: số dao động trong 1 giây. Công thức: f = n / t. Đơn vị: héc (Hz).
- Chu kì T: thời gian thực hiện một dao động. f = 1 / T.
- Tần số càng lớn → âm càng cao (bổng). Tần số càng nhỏ → âm càng thấp (trầm).
- Tai người nghe được âm có tần số từ 20 Hz đến 20 000 Hz.
  + Hạ âm: tần số dưới 20 Hz.
  + Siêu âm: tần số trên 20 000 Hz.

📌 3. BIÊN ĐỘ VÀ ĐỘ TO CỦA ÂM
- Biên độ: độ lệch lớn nhất của vật dao động so với vị trí cân bằng.
- Biên độ càng lớn → âm càng to. Đơn vị độ to: đêxiben (dB).
- Ngưỡng nghe của tai khoảng 0 dB; ngưỡng đau khoảng 130 dB.

📌 4. ÂM SẮC
- Âm sắc giúp phân biệt âm của các nguồn khác nhau dù cùng độ cao và độ to (ví dụ đàn piano và đàn ghita chơi cùng nốt Đô).

📌 5. VÍ DỤ THỰC TẾ
- Dây đàn càng căng, càng ngắn, càng mảnh thì dao động càng nhanh → âm càng cao.""",

    vi_du="""💡 VÍ DỤ 1: Tính tần số
Con ong đập cánh 18 000 lần trong 1 phút. Tính tần số và cho biết tai người có nghe được không.
- f = 18 000 / 60 = 300 Hz. Nằm trong khoảng 20 Hz – 20 000 Hz nên tai người nghe được.

💡 VÍ DỤ 2: So sánh độ cao
Vật A dao động 60 lần trong 1 giây. Vật B dao động 200 lần trong 5 giây.
- f_A = 60 Hz; f_B = 200 / 5 = 40 Hz.
- f_A > f_B nên vật A phát âm cao hơn.

💡 VÍ DỤ 3: Từ chu kì đến tần số
Một vật có chu kì T = 0,02 s. Tần số f = 1 / 0,02 = 50 Hz. Đây là âm nghe được.""",

    cau_hoi=[
        q("Nguồn âm là vật:", ["Phát ra ánh sáng", "Dao động và phát ra âm", "Phản xạ âm", "Hấp thụ âm"], 1),
        q("Khi gảy đàn, nguồn âm là:", ["Dây đàn đang dao động", "Không khí xung quanh", "Tai người nghe", "Ánh sáng đèn"], 0),
        q("Âm không truyền được trong:", ["Chất rắn", "Chất lỏng", "Chân không", "Chất khí"], 2),
        q("Sắp xếp tốc độ truyền âm từ nhanh đến chậm:", ["Rắn, lỏng, khí", "Khí, lỏng, rắn", "Lỏng, rắn, khí", "Khí, rắn, lỏng"], 0),
        q("Tốc độ âm trong không khí ở điều kiện thường khoảng:", ["340 m/s", "1500 m/s", "3 × 10⁸ m/s", "34 m/s"], 0),
        q("Âm truyền trong nước nhanh hơn trong không khí vì:", ["Các hạt trong nước gần nhau hơn, truyền dao động nhanh hơn", "Nước sáng hơn", "Nước nóng hơn", "Không có lí do"], 0),
        q("Tần số là:", ["Số dao động trong 1 giây", "Thời gian thực hiện một dao động", "Biên độ dao động", "Quãng đường đi được trong 1 giây"], 0),
        q("Đơn vị của tần số là:", ["m", "s", "Hz", "dB"], 2),
        q("Vật dao động 300 lần trong 10 giây. Tần số là:", ["30 Hz", "3000 Hz", "300 Hz", "3 Hz"], 0),
        q("Âm càng cao (bổng) khi:", ["Tần số càng lớn", "Tần số càng nhỏ", "Biên độ càng lớn", "Biên độ càng nhỏ"], 0),
        q("Âm càng to khi:", ["Biên độ dao động càng lớn", "Tần số càng lớn", "Tần số càng nhỏ", "Vật dao động chậm"], 0),
        q("Đơn vị đo độ to của âm là:", ["Hz", "dB (đêxiben)", "m/s", "N"], 1),
        q("Tai người nghe được âm có tần số trong khoảng:", ["Dưới 20 Hz", "Từ 20 Hz đến 20 000 Hz", "Trên 20 000 Hz", "Từ 0 đến 100 Hz"], 1),
        q("Âm có tần số trên 20 000 Hz gọi là:", ["Hạ âm", "Siêu âm", "Âm sắc", "Âm vang"], 1),
        q("Âm có tần số dưới 20 Hz gọi là:", ["Hạ âm", "Siêu âm", "Âm bổng", "Âm vang"], 0),
        q("Dây A dao động 200 Hz, dây B dao động 250 Hz. Dây nào phát âm cao hơn?", ["Dây A", "Dây B", "Như nhau", "Không so sánh được"], 1),
        q("Cùng nốt Đô nhưng đàn piano và đàn ghita nghe khác nhau. Đặc trưng âm nào khác biệt?", ["Độ cao", "Độ to", "Âm sắc", "Tần số"], 2),
        q("Ngưỡng đau của tai người khoảng:", ["50 dB", "70 dB", "130 dB", "300 dB"], 2),
        q("Dây đàn càng căng và càng ngắn thì âm:", ["Càng cao", "Càng trầm", "Càng to", "Không đổi"], 0),
        q("Khi biên độ dao động của con lắc tăng lên, âm phát ra:", ["To hơn", "Cao hơn", "Có tần số lớn hơn", "Không đổi"], 0),
        q("Vật dao động 1200 lần trong 2 phút. Âm do vật phát ra là:", ["Hạ âm (10 Hz)", "Âm nghe được", "Siêu âm", "Âm sắc"], 0, "1200 : 120 = 10 Hz < 20 Hz"),
    ],

    bt_co_ban=[
        bt("Con ong đập cánh 18 000 lần trong 1 phút. Tính tần số đập cánh và cho biết tai người có nghe được không.", ["300 Hz; nghe được", "300 Hz, có"], "18 000 : 60 = 300 Hz, nằm trong 20 Hz – 20 kHz."),
        bt("Vật A dao động 60 lần trong 1 giây; vật B dao động 200 lần trong 5 giây. Vật nào phát âm cao hơn?", ["Vật A", "A"], "f_B = 40 Hz < f_A = 60 Hz ⇒ A cao hơn."),
        bt("Một vật dao động 50 lần trong 1 giây. Tính chu kì dao động.", ["0,02 s", "0,02"], "T = 1/f = 1/50 = 0,02 s."),
        bt("Vật dao động với tần số 50 Hz. Trong 2 phút vật thực hiện bao nhiêu dao động?", ["6000", "6 000"], "50 × 120 = 6000."),
        bt("Một con dơi phát siêu âm với chu kì 0,00005 s. Tính tần số và cho biết đó có phải siêu âm không.", ["20 000 Hz; đúng (ranh giới siêu âm)", "20000 Hz"], "f = 1 / 0,00005 = 20 000 Hz."),
        bt("Sắp xếp theo tốc độ truyền âm giảm dần: không khí, thép, nước.", ["Thép > nước > không khí", "thép, nước, không khí"], "Rắn > lỏng > khí."),
    ],

    bt_nang_cao=[
        nc("Dây đàn 1 dao động 400 lần trong 2 s; dây đàn 2 dao động 1000 lần trong 4 s. Dây nào phát âm cao hơn? Vì sao?",
           "Tính tần số của từng dây.",
           ["Dây 2 (250 Hz > 200 Hz)"],
           "f1 = 400 : 2 = 200 Hz; f2 = 1000 : 4 = 250 Hz ⇒ dây 2 cao hơn."),
        nc("Hai người đứng ở hai đầu ống thép dài 1020 m. Một người gõ mạnh vào ống. Người kia áp tai vào ống và nghe hai tiếng cách nhau 2,8 s. Biết tốc độ âm trong không khí 340 m/s. Tính tốc độ âm trong thép.",
           "Thời gian âm truyền qua không khí = 1020 / 340; âm truyền qua thép đến trước nên có thời gian ngắn hơn.",
           ["5100 m/s", "5100"],
           "t_khí = 3 s; t_thép = 3 − 2,8 = 0,2 s; v_thép = 1020 : 0,2 = 5100 m/s."),
        nc("Một tàu thăm dò lần 1 nhận sóng siêu âm phản xạ sau 1,2 s, lần 2 sau 1,8 s (v nước = 1500 m/s). Vị trí nào sâu hơn và sâu hơn bao nhiêu?",
           "h = v·t / 2.",
           ["Vị trí lần 2 sâu hơn 450 m"],
           "h1 = 1500 × 1,2 / 2 = 900 m; h2 = 1500 × 1,8 / 2 = 1350 m; chênh 450 m."),
        nc("Một người hét về phía vách núi và nghe tiếng vang sau 2 s. Tính khoảng cách từ người đến vách núi (v = 340 m/s). Nếu người đứng cách vách 17 m và vỗ tay, có nghe được tiếng vang không? Biết tai nghe được tiếng vang khi âm dội lại chậm ít nhất 1/15 s.",
           "Âm đi và về: quãng đường = 2d.",
           ["340 m; có nghe được tiếng vang"],
           "d = 340 × 2 / 2 = 340 m. Với d = 17 m: t = 2 × 17 / 340 = 0,1 s > 1/15 s ≈ 0,067 s ⇒ nghe được."),
        nc("Vì sao khi chớp lóe lên ta thấy chớp trước, rồi sau vài giây mới nghe tiếng sấm? Nếu chậm 5 s, sét đánh cách bao xa?",
           "Ánh sáng truyền nhanh hơn âm thanh rất nhiều.",
           ["1700 m"],
           "Ánh sáng đến gần như tức thì; s = 340 × 5 = 1700 m."),
        nc("Vì sao khi áp tai vào thanh ray, người ta nghe tiếng tàu đang đến sớm hơn nhiều so với nghe qua không khí? Hãy giải thích bằng tốc độ truyền âm.",
           "So sánh tốc độ truyền âm trong rắn và trong khí.",
           ["Vì âm truyền trong thép (rắn) nhanh hơn trong không khí nhiều lần"],
           "v_thép ≈ 5100 m/s >> v_khí ≈ 340 m/s."),
    ],
)

C2_B2 = bai(
    ly_thuyet="""📌 1. PHẢN XẠ ÂM VÀ TIẾNG VANG
- Phản xạ âm: âm dội lại khi gặp mặt chắn.
- Tiếng vang: âm phản xạ đến tai chậm hơn âm trực tiếp ít nhất 1/15 s.
- Với tiếng vang, quãng đường âm đi và về ít nhất: 340 × 1/15 ≈ 22,7 m, nên người phải đứng cách vật phản xạ ít nhất khoảng 11,3 m.
- Vật phản xạ âm tốt: mặt nhẵn, cứng (gương, tường gạch, kim loại).
- Vật phản xạ âm kém (hấp thụ âm tốt): mềm, xốp, gồ ghề (rèm nhung, mút xốp, thảm, bông).

📌 2. CHỐNG Ô NHIỄM TIẾNG ỒN
- Tiếng ồn ô nhiễm: âm to, kéo dài, ảnh hưởng sức khỏe và tâm lí.
- Biện pháp:
  + Ở nguồn âm: dùng thiết bị êm hơn, bảo dưỡng máy móc.
  + Trên đường truyền: trồng cây xanh (phân tán và hấp thụ âm), xây tường chắn âm.
  + Ở tai người: dùng nút bịt tai, chụp tai chống ồn.
- Trong phòng hát, rạp chiếu phim: dùng vật liệu xốp, rèm nhung để giảm tiếng vang.

📌 3. ỨNG DỤNG SIÊU ÂM
- Siêu âm truyền đi thành chùm hướng và phản xạ khi gặp vật. Dựa vào thời gian phản xạ để tính khoảng cách: s = v·t / 2.
- Ứng dụng: đo độ sâu đáy biển (máy sonar); siêu âm y tế (kiểm tra thai nhi, các cơ quan); phát hiện vết nứt trong kim loại; dơi định vị con mồi.""",

    vi_du="""💡 VÍ DỤ 1: Tiếng vang
Người đứng trước vách núi, hét lớn và nghe tiếng vang sau 2 s. Tính khoảng cách đến vách.
- Âm đi và về: quãng đường 2d = v·t = 340 × 2 = 680 m.
- d = 340 m.

💡 VÍ DỤ 2: Đo độ sâu bằng siêu âm
Tàu phát siêu âm xuống đáy biển, nhận lại phản xạ sau 2 s. Biết v nước = 1500 m/s.
- h = v·t / 2 = 1500 × 2 / 2 = 1500 m.

💡 VÍ DỤ 3: Vì sao phòng hát cần vật liệu xốp?
Tường nhẵn phản xạ mạnh làm tiếng hát bị dội lại, gây vang và chói tai. Dùng mút xốp, rèm nhung giúp hấp thụ âm, tiếng hát rõ ràng hơn.""",

    cau_hoi=[
        q("Hiện tượng âm dội lại khi gặp mặt chắn gọi là:", ["Phản xạ âm", "Khúc xạ âm", "Nhiễu xạ âm", "Hấp thụ âm"], 0),
        q("Tiếng vang nghe được khi âm phản xạ đến tai chậm hơn âm trực tiếp ít nhất:", ["1/15 s", "1 s", "2 s", "1/100 s"], 0),
        q("Vật phản xạ âm tốt có đặc điểm:", ["Mặt nhẵn, cứng", "Mặt gồ ghề, mềm", "Xốp, nhẹ", "Chứa nhiều không khí"], 0),
        q("Vật hấp thụ âm tốt thường là:", ["Gương", "Tường bê tông nhẵn", "Rèm nhung, mút xốp", "Kim loại đánh bóng"], 2),
        q("Trong rạp chiếu phim, tường sần sùi và rèm nhung để:", ["Hấp thụ âm, giảm tiếng vang", "Tăng tiếng vang", "Trang trí", "Làm sáng phòng"], 0),
        q("Biện pháp chống ồn tại nguồn âm là:", ["Dùng thiết bị êm hơn, bảo dưỡng máy", "Trồng cây hai bên đường", "Xây tường cách âm", "Đeo bịt tai"], 0),
        q("Trồng nhiều cây xanh quanh nhà giúp chống ồn bằng cách:", ["Phân tán và hấp thụ âm trên đường truyền", "Tăng tần số âm", "Phản xạ âm mạnh hơn", "Làm âm truyền nhanh hơn"], 0),
        q("Để giảm tiếng ồn đường phố vào nhà, nên:", ["Lắp cửa kính cách âm, trồng cây xanh", "Mở cửa sổ thật to", "Bật nhạc thật lớn", "Đóng cửa ở nhà bếp"], 0),
        q("Siêu âm được ứng dụng trong:", ["Chụp ảnh thai nhi, đo độ sâu biển", "Phát nhạc", "Thắp sáng", "Làm nóng nước"], 0),
        q("Máy đo độ sâu đáy biển (sonar) dựa trên:", ["Phản xạ sóng siêu âm", "Khúc xạ ánh sáng", "Từ trường Trái Đất", "Lực hấp dẫn"], 0),
        q("Dơi định vị con mồi bằng:", ["Siêu âm", "Hạ âm", "Ánh sáng", "Âm nghe được"], 0),
        q("Tàu phát siêu âm xuống đáy biển, sau 2 s nhận phản xạ. v nước = 1500 m/s. Độ sâu là:", ["1500 m", "3000 m", "750 m", "150 m"], 0, "1500 × 2 / 2 = 1500 m"),
        q("Tường lớp học thường quét sơn hơi nhám để:", ["Giảm tiếng vang", "Tăng tiếng vang", "Giữ nhiệt", "Phản chiếu ánh sáng"], 0),
        q("Để nghe được tiếng vang, quãng đường âm đi và về tối thiểu khoảng:", ["22,7 m", "11,3 m", "340 m", "1 m"], 0, "340 × 1/15 ≈ 22,7 m"),
        q("Khi nghe âm, màng nhĩ đóng vai trò:", ["Vật nhận dao động âm", "Nguồn âm", "Vật phản xạ ánh sáng", "Vật cách điện"], 0),
        q("Áp tai vào đường ray nghe tiếng tàu sớm hơn vì:", ["Âm truyền trong rắn nhanh hơn trong không khí", "Ánh sáng đến nhanh hơn", "Tai nhạy hơn", "Không có lí do"], 0),
        q("Vật liệu cách âm tốt thường là:", ["Xốp, bông thủy tinh, cao su", "Thép", "Thủy tinh", "Gỗ đặc"], 0),
        q("Khi âm đi từ không khí vào nước, tần số của âm:", ["Không đổi", "Tăng", "Giảm", "Bằng 0"], 0),
        q("Vật nào phản xạ âm kém nhất?", ["Mút xốp dày", "Tấm kính", "Tường đá", "Tấm kim loại"], 0),
        q("Thiết bị nào sau đây KHÔNG dùng siêu âm?", ["Đèn pin", "Máy kiểm tra vết nứt kim loại", "Máy siêu âm y tế", "Máy đo độ sâu biển"], 0),
    ],

    bt_co_ban=[
        bt("Người đứng cách vách núi 680 m. Sau bao lâu thì nghe được tiếng vang? (v = 340 m/s)", ["4 s", "4"], "t = 2 × 680 / 340 = 4 s."),
        bt("Khoảng cách tối thiểu từ người đến tường để nghe được tiếng vang trong không khí (v = 340 m/s) là bao nhiêu?", ["11,3 m", "11,33 m"], "d = 340 × (1/15) / 2 ≈ 11,3 m."),
        bt("Tàu phát siêu âm xuống đáy biển, nhận phản xạ sau 2 s. v nước = 1500 m/s. Tính độ sâu đáy biển.", ["1500 m", "1500"], "h = 1500 × 2 / 2 = 1500 m."),
        bt("Một sonar phát xung và nhận phản xạ sau 0,4 s (v = 1500 m/s). Tính độ sâu.", ["300 m", "300"], "h = 1500 × 0,4 / 2 = 300 m."),
        bt("Người đứng cách vật cản 85 m, nghe tiếng vang sau bao lâu? (v = 340 m/s)", ["0,5 s", "0,5"], "t = 2 × 85 / 340 = 0,5 s."),
        bt("Kể tên 3 vật liệu cách âm tốt thường dùng trong xây dựng.", ["Xốp, bông thủy tinh, cao su", "xốp, bông, cao su"], "Các vật liệu mềm, xốp chứa nhiều không khí."),
    ],

    bt_nang_cao=[
        nc("Tại sao khi áp tai xuống đất, ta nghe được tiếng xe đang đến từ xa trước khi nghe bằng không khí?",
           "So sánh tốc độ truyền âm trong các môi trường.",
           ["Vì âm truyền trong đất (rắn) nhanh hơn và ít bị suy giảm hơn trong không khí"],
           "Âm truyền qua đất có tốc độ lớn hơn không khí nhiều lần."),
        nc("Một tàu sonar có tần số phát 40 000 Hz. Tai người có nghe được sóng này không? Vì sao vẫn nói đây là âm?",
           "So sánh với giới hạn nghe của tai người.",
           ["Không nghe được vì tần số > 20 000 Hz (đây là siêu âm)"],
           "Siêu âm vẫn là sóng âm, chỉ tai người không nghe được."),
        nc("Vì sao người ta thường cắm ống thép hoặc đặt tai vào đường ray để phát hiện tàu đến?",
           "Tốc độ âm trong thép và trong không khí.",
           ["Âm truyền trong thép nhanh hơn trong không khí nên đến tai sớm hơn"],
           "v_thép ≈ 5000 m/s, v_khí ≈ 340 m/s."),
        nc("Hai bạn đứng cách một tường đá 34 m và hát cùng lúc. Bạn A hát 1 câu; bạn B hát tiếp ngay. Bạn A có nghe được tiếng vang của chính mình không? Vì sao?",
           "Tính thời gian âm đi và về và so với 1/15 s.",
           ["Có, vì thời gian âm đi và về là 0,2 s > 1/15 s"],
           "t = 2 × 34 / 340 = 0,2 s > 1/15 s."),
        nc("Thiết kế căn phòng hát karaoke không làm ồn nhà bên cạnh. Em sẽ chọn vật liệu nào cho tường và cửa? Vì sao?",
           "Vật liệu cách âm, hấp thụ âm tốt.",
           ["Tường dùng bông/xốp cách âm, cửa kính nhiều lớp hoặc cửa gỗ có lớp đệm xốp"],
           "Vật liệu xốp, mềm chứa nhiều không khí giúp hấp thụ âm và ngăn truyền âm."),
        nc("Vì sao trong phòng hòa nhạc người ta thường đặt rèm nhung ở tường nhưng vẫn giữ một số bề mặt cứng?",
           "Cân bằng giữa hấp thụ và phản xạ âm.",
           ["Để âm thanh vừa đủ vang, không quá khô và không quá dội"],
           "Hấp thụ hết âm thì nhạc nghe khô; phản xạ quá nhiều thì bị dội, ồn."),
    ],
)

VL7_CHUONG2 = {
    "Bài 1: Âm thanh, tần số và độ to của âm": C2_B1,
    "Bài 2: Phản xạ âm, chống ô nhiễm tiếng ồn và siêu âm": C2_B2,
}


# ============================================================
# CHƯƠNG 3: ÁNH SÁNG
# ============================================================
C3_B1 = bai(
    ly_thuyet="""📌 1. NGUỒN SÁNG VÀ VẬT SÁNG
- Nguồn sáng: vật tự phát ra ánh sáng (Mặt Trời, ngọn lửa, bóng đèn đang sáng, đom đóm).
- Vật sáng: vật hắt lại ánh sáng chiếu vào nó (Mặt Trăng, cuốn sách, cái bàn).
- Ta nhìn thấy một vật khi có ánh sáng từ vật truyền vào mắt.

📌 2. ĐỊNH LUẬT TRUYỀN THẲNG
- Trong môi trường trong suốt và đồng tính, ánh sáng truyền theo đường thẳng.
- Tia sáng: đường thẳng có mũi tên chỉ hướng truyền.
- Các loại chùm sáng: song song (các tia không giao nhau), hội tụ (các tia gặp nhau tại một điểm), phân kì (các tia loe rộng ra).
- Ứng dụng: ngắm đường thẳng, cắm cọc thẳng hàng, lỗ kim tạo ảnh ngược.

📌 3. BÓNG TỐI VÀ BÓNG NỬA TỐI
- Bóng tối: vùng phía sau vật cản, không nhận được ánh sáng từ nguồn.
- Bóng nửa tối: vùng chỉ nhận được một phần ánh sáng từ nguồn (xuất hiện khi nguồn có kích thước đáng kể).

📌 4. NHẬT THỰC VÀ NGUYỆT THỰC
- Nhật thực: Mặt Trăng nằm giữa Trái Đất và Mặt Trời, che khuất Mặt Trời. Người trong vùng bóng tối thấy nhật thực toàn phần.
- Nguyệt thực: Trái Đất nằm giữa Mặt Trời và Mặt Trăng, che khuất ánh sáng Mặt Trời chiếu lên Mặt Trăng.

📌 5. TỐC ĐỘ ÁNH SÁNG
- Trong chân không: khoảng 300 000 km/s.
- Ánh sáng từ Mặt Trời đến Trái Đất mất khoảng 8 phút 20 giây.
- Năm ánh sáng: quãng đường ánh sáng đi được trong 1 năm (khoảng 9,46 × 10¹² km).""",

    vi_du="""💡 VÍ DỤ 1: Thời gian ánh sáng truyền
Khoảng cách Trái Đất – Mặt Trời khoảng 150 triệu km; c = 300 000 km/s.
- t = 150 000 000 / 300 000 = 500 s = 8 phút 20 giây.

💡 VÍ DỤ 2: Giải thích nhật thực
Khi Mặt Trăng nằm đúng giữa Mặt Trời và Trái Đất, Mặt Trăng chắn ánh sáng Mặt Trời. Người ở vùng bóng tối trên Trái Đất thấy nhật thực toàn phần; người ở vùng bóng nửa tối thấy nhật thực một phần.

💡 VÍ DỤ 3: Vì sao ta thấy Mặt Trăng?
Mặt Trăng là vật sáng: nó không tự phát sáng mà hắt lại ánh sáng Mặt Trời chiếu vào. Ánh sáng này truyền đến mắt ta nên ta nhìn thấy Mặt Trăng.""",

    cau_hoi=[
        q("Nguồn sáng là vật:", ["Tự phát ra ánh sáng", "Phản chiếu ánh sáng", "Trong suốt", "Có màu trắng"], 0),
        q("Vật nào dưới đây là nguồn sáng?", ["Ngọn nến đang cháy", "Mặt Trăng", "Tờ giấy trắng", "Chiếc gương"], 0),
        q("Mặt Trăng là:", ["Vật sáng (không phải nguồn sáng)", "Nguồn sáng", "Gương phẳng", "Vật trong suốt"], 0),
        q("Ta nhìn thấy một vật khi:", ["Có ánh sáng từ vật truyền vào mắt", "Vật phát ra âm thanh", "Mắt ta phát ra ánh sáng", "Vật đang chuyển động"], 0),
        q("Định luật truyền thẳng của ánh sáng áp dụng trong môi trường:", ["Trong suốt và đồng tính", "Bất kì", "Đặc", "Có nhiều bụi"], 0),
        q("Chùm sáng song song là chùm sáng có các tia:", ["Không giao nhau, không loe rộng", "Giao nhau tại một điểm", "Loe rộng ra", "Hội tụ"], 0),
        q("Chùm sáng hội tụ là chùm các tia:", ["Gặp nhau tại một điểm", "Song song", "Loe ra", "Đi ngược chiều"], 0),
        q("Bóng tối là vùng:", ["Không nhận được ánh sáng từ nguồn truyền tới", "Nhận được một phần ánh sáng", "Chỉ có màu đen", "Gần nguồn sáng"], 0),
        q("Bóng nửa tối xuất hiện khi nguồn sáng:", ["Có kích thước đáng kể", "Là một điểm", "Trong suốt", "Không sáng"], 0),
        q("Nguyệt thực xảy ra khi:", ["Trái Đất nằm giữa Mặt Trời và Mặt Trăng", "Mặt Trăng nằm giữa Trái Đất và Mặt Trời", "Mặt Trời nằm giữa Trái Đất và Mặt Trăng", "Ba thiên thể thẳng hàng theo thứ tự tùy ý"], 0),
        q("Nhật thực xảy ra khi:", ["Mặt Trăng nằm giữa Trái Đất và Mặt Trời", "Trái Đất nằm giữa Mặt Trời và Mặt Trăng", "Mặt Trời nằm giữa Trái Đất và Mặt Trăng", "Mặt Trăng ở xa Trái Đất"], 0),
        q("Ánh sáng Mặt Trời đến Trái Đất mất khoảng:", ["8 phút 20 giây", "1 giờ", "1 giây", "24 giờ"], 0),
        q("Hình ảnh ngược của vật qua lỗ kim được giải thích bởi:", ["Ánh sáng truyền thẳng", "Phản xạ ánh sáng", "Khúc xạ ánh sáng", "Tán sắc ánh sáng"], 0),
        q("Năm ánh sáng là đơn vị đo:", ["Khoảng cách", "Thời gian", "Cường độ sáng", "Nhiệt độ"], 0),
        q("Tia sáng được biểu diễn bằng:", ["Đường thẳng có mũi tên", "Đường cong kín", "Đường tròn", "Chấm điểm"], 0),
        q("Vì sao ta nhìn thấy cuốn sách trên bàn?", ["Sách hắt ánh sáng vào mắt ta", "Sách phát sáng", "Mắt ta phát ra tia sáng", "Sách trong suốt"], 0),
        q("Đom đóm đang phát sáng là:", ["Nguồn sáng", "Vật sáng", "Gương", "Vật trong suốt"], 0),
        q("Thời gian ánh sáng từ Mặt Trăng đến Trái Đất (khoảng 384 000 km) là:", ["Khoảng 1,28 s", "Khoảng 1 phút", "Khoảng 8 phút", "Khoảng 1 giờ"], 0, "384 000 : 300 000 ≈ 1,28 s"),
        q("Năm ánh sáng là quãng đường ánh sáng đi được trong:", ["1 năm", "1 giờ", "1 giây", "1 ngày"], 0),
        q("Ánh sáng KHÔNG truyền qua được vật:", ["Vật đục, không trong suốt", "Thủy tinh trong", "Nước lặng", "Không khí"], 0),
    ],

    bt_co_ban=[
        bt("Khoảng cách Trái Đất – Mặt Trời 150 triệu km; c = 300 000 km/s. Tính thời gian ánh sáng đi tới Trái Đất.", ["500 s (8 phút 20 s)", "500"], "150 000 000 : 300 000 = 500 s."),
        bt("Vì sao trong phòng kín không có đèn, ta không nhìn thấy đồ vật?", ["Vì không có ánh sáng từ vật truyền vào mắt"], "Cần có ánh sáng từ vật đến mắt để nhìn thấy."),
        bt("Tính quãng đường ánh sáng đi được trong 1 năm (c = 3 × 10⁵ km/s, 1 năm ≈ 3,15 × 10⁷ s).", ["9,45 × 10¹² km", "9,45 × 10^12 km"], "3 × 10⁵ × 3,15 × 10⁷ = 9,45 × 10¹² km."),
        bt("Vì sao cọc tiêu thẳng hàng được cắm bằng cách ngắm? Dựa vào tính chất nào của ánh sáng?", ["Ánh sáng truyền thẳng"], "Các cọc nằm trên cùng một đường thẳng khi ánh sáng từ cọc xa bị cọc gần che khuất."),
        bt("Mặt Trăng nằm cách Trái Đất khoảng 384 000 km. Tính thời gian ánh sáng từ Trái Đất đến Mặt Trăng.", ["Khoảng 1,28 s", "1,28"], "384 000 : 300 000 ≈ 1,28 s."),
        bt("Nêu điều kiện để xảy ra nhật thực toàn phần.", ["Mặt Trăng nằm giữa Trái Đất và Mặt Trời thẳng hàng, người quan sát ở vùng bóng tối"], "Bóng tối của Mặt Trăng chạm tới bề mặt Trái Đất."),
    ],

    bt_nang_cao=[
        nc("Nhật thực toàn phần và nhật thực một phần khác nhau ở điều kiện nào?",
           "Bóng tối và bóng nửa tối.",
           ["Toàn phần: người nằm trong vùng bóng tối; một phần: người nằm trong vùng bóng nửa tối"],
           "Vùng bóng tối không nhận được ánh sáng Mặt Trời; vùng bóng nửa tối chỉ nhận được một phần."),
        nc("Ống thẳng dài 2 m, người nhìn thẳng qua ống thấy viên bi ở đầu kia. Nếu thay bằng ống cong chữ U, người có còn thấy viên bi không? Vì sao?",
           "Định luật truyền thẳng.",
           ["Ống thẳng: thấy; ống cong: không thấy"],
           "Ánh sáng truyền theo đường thẳng nên không đi qua được đoạn ống cong."),
        nc("Vì sao ban đêm ta nhìn thấy Mặt Trăng dù Mặt Trăng không tự phát sáng?",
           "Vật sáng hắt lại ánh sáng.",
           ["Mặt Trăng hắt lại ánh sáng Mặt Trời chiếu vào nó"],
           "Ánh sáng này truyền đến mắt ta nên ta nhìn thấy Mặt Trăng."),
        nc("Một nguồn sáng hình cầu chiếu lên một quả bóng. Vì sao có vùng bóng tối và vùng bóng nửa tối?",
           "Nguồn sáng có kích thước, không phải một điểm.",
           ["Vùng bóng tối: không nhận được ánh sáng từ bất kì điểm nào của nguồn; vùng bóng nửa tối: nhận được từ một phần nguồn"],
           "Ánh sáng từ các điểm khác nhau của nguồn tạo thành các vùng bóng khác nhau."),
        nc("Dùng một lỗ kim trên tấm bìa để chiếu hình ảnh một ngọn nến lên màn. Hình trên màn cùng chiều hay ngược chiều với ngọn nến? Giải thích.",
           "Ánh sáng truyền thẳng qua lỗ kim.",
           ["Ngược chiều, vì các tia sáng từ đỉnh và chân nến đi qua lỗ kim theo đường thẳng và đảo vị trí"],
           "Các tia sáng từ đầu trên của nến đi xuống, từ đầu dưới đi lên, qua lỗ kim và tạo ảnh ngược."),
        nc("Đèn đường cao 6 m đặt trên mặt đất. Một người cao 1,6 m đứng cách chân đèn 10 m. Bóng người trên mặt đất dài bao nhiêu? Nếu người đó đi lại gần đèn thêm 2 m thì bóng dài bao nhiêu?",
           "Dùng tam giác đồng dạng: chiều cao người / bóng = chiều cao đèn / (bóng + khoảng cách từ người đến chân đèn).",
           ["4 m; khoảng 2,9 m", "4; 2,9"],
           "Ban đầu: 1,6/x = 6/(x + 10) ⇒ 1,6x + 16 = 6x ⇒ x = 4 m. Sau khi đi lại gần 2 m (cách chân đèn 8 m): 1,6/y = 6/(y + 8) ⇒ 1,6y + 12,8 = 6y ⇒ y = 12,8 : 4,4 ≈ 2,9 m."),
    ],
)

C3_B2 = bai(
    ly_thuyet="""📌 1. ĐỊNH LUẬT PHẢN XẠ ÁNH SÁNG
- Phản xạ ánh sáng: tia sáng dội ngược lại môi trường cũ khi gặp bề mặt nhẵn bóng.
- Các khái niệm:
  + Tia tới, tia phản xạ, điểm tới.
  + Pháp tuyến: đường thẳng vuông góc với gương tại điểm tới.
  + Góc tới i: góc giữa tia tới và pháp tuyến. Góc phản xạ i′: góc giữa tia phản xạ và pháp tuyến.
- Định luật: (1) Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến. (2) Góc phản xạ bằng góc tới: i′ = i.
- Chú ý: góc giữa tia tới và mặt gương = 90° − i.

📌 2. PHẢN XẠ KHUẾCH TÁN
- Chiếu chùm sáng song song vào bề mặt gồ ghề, các tia phản xạ theo nhiều hướng khác nhau.
- Nhờ phản xạ khuếch tán, ta nhìn thấy các vật không phát sáng từ nhiều hướng.

📌 3. ẢNH TẠO BỞI GƯƠNG PHẲNG
- Là ảnh ảo: không hứng được trên màn chắn, nhìn thấy nhờ tia phản xạ đi vào mắt.
- Kích thước ảnh bằng kích thước vật.
- Ảnh và vật đối xứng qua mặt gương: khoảng cách vật–gương = khoảng cách ảnh–gương.
- Ảnh bị đảo ngược trái – phải (ứng dụng: chữ viết ngược trên xe cứu thương).

📌 4. GƯƠNG QUAY VÀ NHIỀU GƯƠNG
- Khi gương quay một góc α, tia phản xạ quay một góc 2α.
- Hai gương phẳng hợp với nhau góc α: số ảnh n = 360°/α − 1 (nếu 360°/α là số nguyên).
- Kính tiềm vọng (tàu ngầm): dùng hai gương phẳng đặt song song/nghiêng 45° để bẻ đường đi tia sáng.""",

    vi_du="""💡 VÍ DỤ 1: Tính góc phản xạ
Tia sáng SI tới gương phẳng, tia tới hợp với mặt gương một góc 30°.
- Góc tới i = 90° − 30° = 60°.
- Góc phản xạ i′ = i = 60°.

💡 VÍ DỤ 2: Ảnh qua gương phẳng
Người cao 1,6 m đứng cách gương phẳng 2 m.
- Ảnh cao 1,6 m (bằng vật).
- Ảnh cách gương 2 m, nên khoảng cách người–ảnh = 4 m.

💡 VÍ DỤ 3: Người đi lại gần gương
Người đi về phía gương với 2 m/s. Ảnh cũng đi về phía gương với 2 m/s (đối xứng).
- Tốc độ tương đối giữa người và ảnh: 2 + 2 = 4 m/s.""",

    cau_hoi=[
        q("Góc tới là góc hợp bởi:", ["Tia tới và pháp tuyến tại điểm tới", "Tia tới và mặt gương", "Tia tới và tia phản xạ", "Pháp tuyến và mặt gương"], 0),
        q("Theo định luật phản xạ, góc phản xạ:", ["Bằng góc tới", "Lớn hơn góc tới", "Nhỏ hơn góc tới", "Bằng hai lần góc tới"], 0),
        q("Tia tới hợp với mặt gương góc 30°. Góc tới là:", ["60°", "30°", "90°", "120°"], 0, "i = 90° − 30° = 60°"),
        q("Tia tới trùng với pháp tuyến. Góc phản xạ bằng:", ["0°", "90°", "45°", "180°"], 0),
        q("Tia tới và tia phản xạ hợp với nhau góc 90°. Góc tới là:", ["45°", "90°", "30°", "60°"], 0, "i + i′ = 90° ⇒ i = 45°"),
        q("Chiếu tia sáng vuông góc vào gương phẳng, tia phản xạ:", ["Đi ngược lại đúng đường tia tới", "Đi theo phương ngang", "Không phản xạ", "Vuông góc với tia tới"], 0),
        q("Tia tới hợp với gương góc 60°. Tia phản xạ hợp với gương góc:", ["60°", "30°", "120°", "90°"], 0),
        q("Ảnh của vật qua gương phẳng là:", ["Ảnh ảo, bằng vật", "Ảnh thật, bằng vật", "Ảnh ảo, nhỏ hơn vật", "Ảnh ảo, lớn hơn vật"], 0),
        q("Điểm sáng S cách gương 5 cm. Khoảng cách từ S đến ảnh S′ là:", ["10 cm", "5 cm", "2,5 cm", "15 cm"], 0),
        q("Người cao 1,6 m đứng trước gương phẳng. Ảnh của người đó cao:", ["1,6 m", "3,2 m", "0,8 m", "Tùy khoảng cách"], 0),
        q("Người đi lại gần gương phẳng thêm 1 m, ảnh của họ:", ["Cũng tiến lại gần gương 1 m", "Đứng yên", "Lùi ra xa 1 m", "Biến mất"], 0),
        q("Ảnh tạo bởi gương phẳng không hứng được trên màn vì:", ["Là ảnh ảo", "Là ảnh thật", "Quá nhỏ", "Ánh sáng yếu"], 0),
        q("Khi gương quay một góc α quanh điểm tới, tia phản xạ quay một góc:", ["2α", "α", "α/2", "90°"], 0),
        q("Mặt nước lặng hoạt động như:", ["Gương phẳng", "Thấu kính", "Nguồn sáng", "Màn chắn"], 0),
        q("Phản xạ khuếch tán xảy ra khi:", ["Bề mặt gồ ghề", "Bề mặt phẳng nhẵn", "Chiếu vuông góc", "Môi trường trong suốt"], 0),
        q("Chữ AMBULANCE viết ngược trên xe cứu thương để:", ["Tài xế phía trước đọc được qua gương chiếu hậu", "Trang trí", "Chống nắng", "Thu hút chim"], 0),
        q("Hai gương phẳng hợp nhau 90°. Tia ló cuối cùng so với tia tới:", ["Song song và ngược chiều", "Vuông góc", "Trùng nhau", "Tạo góc 45°"], 0),
        q("Đặt điểm sáng S trước gương phẳng, S phát ra:", ["Vô số tia sáng", "Một tia sáng", "Hai tia sáng", "Không có tia nào"], 0),
        q("Hai gương phẳng song song đối diện nhau. Một vật đặt giữa hai gương sẽ cho:", ["Vô số ảnh", "Một ảnh", "Hai ảnh", "Không có ảnh"], 0),
        q("Ảnh qua gương phẳng bị đảo ngược theo chiều nào?", ["Trái – phải", "Trên – dưới", "Trước – sau", "Không đảo"], 0),
        q("Kính tiềm vọng trong tàu ngầm dựa trên nguyên lí nào?", ["Phản xạ ánh sáng qua gương phẳng", "Khúc xạ qua thấu kính", "Truyền thẳng ánh sáng", "Nhiễu xạ ánh sáng"], 0),
    ],

    bt_co_ban=[
        bt("Góc tạo bởi tia tới và mặt gương là 40°. Tính góc phản xạ.", ["50°", "50"], "Góc tới i = 90° − 40° = 50°; i′ = 50°."),
        bt("Tia tới hợp với pháp tuyến góc 30°. Góc hợp bởi tia tới và tia phản xạ là bao nhiêu?", ["60°", "60"], "i + i′ = 30° + 30° = 60°."),
        bt("Điểm sáng cách gương phẳng 4 cm. Ảnh của điểm sáng cách gương bao nhiêu?", ["4 cm", "4"], "Ảnh đối xứng qua gương."),
        bt("Người đứng cách gương 1,5 m rồi đi lại gần thêm 0,5 m. Khoảng cách từ người đến ảnh của mình lúc này là bao nhiêu?", ["2 m", "2"], "Người–gương = 1 m ⇒ người–ảnh = 2 m."),
        bt("Điểm sáng S cách gương 6 cm, dời S ra xa gương thêm 3 cm. Khoảng cách S đến ảnh S′ lúc này là bao nhiêu?", ["18 cm", "18"], "S cách gương 9 cm ⇒ SS′ = 18 cm."),
        bt("Tia sáng SI tới gương, góc tới 25°. Góc phản xạ là bao nhiêu?", ["25°", "25"], "Góc phản xạ bằng góc tới."),
    ],

    bt_nang_cao=[
        nc("Hai gương phẳng hợp với nhau một góc 60°. Điểm sáng S đặt giữa hai gương. Hệ hai gương tạo được bao nhiêu ảnh của S?",
           "n = 360° / α − 1.",
           ["5 ảnh", "5"],
           "360 : 60 − 1 = 5."),
        nc("Mép dưới của gương treo tường cách sàn bao nhiêu để người cao 1,6 m (mắt cách đỉnh đầu 10 cm) nhìn thấy đến tận mũi giày của mình?",
           "Mắt ở độ cao 1,5 m; mũi giày ở độ cao 0 m. Gương phải chứa tia phản xạ từ mũi giày lên mắt.",
           ["0,75 m (75 cm)", "0,75"],
           "Mép dưới gương bằng một nửa độ cao từ mắt đến mũi giày: 1,5 : 2 = 0,75 m."),
        nc("Một người đi về phía gương phẳng với tốc độ 2 m/s. Ảnh của người đó đi với tốc độ bao nhiêu so với mặt đất và so với người?",
           "Ảnh đối xứng với người qua gương.",
           ["So với đất: 2 m/s; so với người: 4 m/s"],
           "Người và ảnh cùng tiến về phía gương, nên tốc độ tương đối giữa chúng là 4 m/s."),
        nc("Hai gương phẳng hợp nhau góc 90°. Tia sáng SI chiếu tới gương thứ nhất, phản xạ tới gương thứ hai. Chứng minh tia phản xạ cuối cùng song song và ngược chiều với tia tới SI.",
           "Vẽ hình, dùng định luật phản xạ cho hai lần phản xạ.",
           ["Tia ló ngược chiều và song song với tia tới SI"],
           "Hai lần phản xạ với pháp tuyến vuông góc nhau làm tia ló quay đi 180°, nên ngược chiều và song song với tia tới."),
        nc("Cột điện cao 6 m có bóng dài 8 m trên mặt đất. Cùng lúc, cái cây có bóng dài 4 m. Tính chiều cao cái cây (các tia Mặt Trời coi là song song).",
           "Tỉ số chiều cao / bóng không đổi.",
           ["3 m"],
           "h / 4 = 6 / 8 ⇒ h = 3 m."),
        nc("Một điểm sáng S cách gương phẳng 20 cm. Dời S ra xa gương thêm 10 cm. Ảnh của S dời đi bao nhiêu so với vị trí ảnh ban đầu, và ảnh so với gương?",
           "Ảnh luôn đối xứng với vật qua gương.",
           ["Ảnh dời đi 10 cm, và cách gương 30 cm"],
           "S cách gương 30 cm ⇒ ảnh cũng cách gương 30 cm; ảnh ban đầu cách gương 20 cm; ảnh dời 10 cm."),
        nc("Góc tới tăng từ 30° lên 50°. Góc hợp bởi tia tới và tia phản xạ tăng thêm bao nhiêu độ?",
           "Góc giữa tia tới và tia phản xạ bằng 2i.",
           ["Tăng thêm 40°"],
           "Lúc đầu 2 × 30° = 60°; lúc sau 2 × 50° = 100°; tăng 40°."),
    ],
)

VL7_CHUONG3 = {
    "Bài 1: Ánh sáng, sự truyền thẳng và nhật, nguyệt thực": C3_B1,
    "Bài 2: Phản xạ ánh sáng và gương phẳng": C3_B2,
}


# ============================================================
# CHƯƠNG 4: TỪ TRƯỜNG
# ============================================================
C4_B1 = bai(
    ly_thuyet="""📌 1. NAM CHÂM VÀ TỪ TÍNH
- Nam châm: vật có từ tính, hút được sắt, thép, niken, coban.
- Mỗi nam châm có hai cực: cực Bắc (N) và cực Nam (S). Từ tính mạnh nhất ở hai cực.
- Tương tác: cùng tên đẩy nhau; khác tên hút nhau.
- Không thể tách rời hai cực: bẻ đôi nam châm, mỗi mảnh vẫn có đủ cực N và S.

📌 2. TỪ TRƯỜNG
- Từ trường là không gian xung quanh nam châm (hoặc dòng điện) mà trong đó có lực từ tác dụng lên vật từ.
- Không nhìn thấy từ trường bằng mắt, nhận biết bằng kim nam châm thử.

📌 3. TỪ PHỔ VÀ ĐƯỜNG SỨC TỪ
- Từ phổ: hình ảnh mạt sắt xếp quanh nam châm. Chỗ mạt sắt dày, từ trường mạnh.
- Đường sức từ: đường cong biểu diễn từ trường. Chiều đường sức từ ngoài nam châm đi từ cực N đến cực S ("Ra Bắc – Vào Nam").
- Đường sức từ không cắt nhau. Nơi đường sức dày, từ trường mạnh.
- Từ trường đều: các đường sức thẳng, song song, cách đều (ví dụ giữa hai nhánh nam châm chữ U).

📌 4. NHIỄM TỪ
- Vật bằng sắt, thép có thể bị nhiễm từ khi đặt trong từ trường hoặc vuốt nam châm theo một chiều.
- Nung nóng hoặc va đập mạnh có thể làm nam châm yếu đi hoặc mất từ tính.""",

    vi_du="""💡 VÍ DỤ 1: Xác định cực bằng cực đã biết
Cực N của kim nam châm được đưa lại gần đầu A của thanh nam châm và bị hút.
- Khác tên thì hút, nên đầu A là cực S.

💡 VÍ DỤ 2: Chiều đường sức từ
Đường sức từ đi từ X ra, vào Y. Theo quy ước "Ra Bắc – Vào Nam": X là cực Bắc (N), Y là cực Nam (S).

💡 VÍ DỤ 3: Từ trường mạnh ở đâu?
Nhìn vào từ phổ: mạt sắt dày đặc ở hai đầu thanh nam châm, thưa dần về giữa. Vậy từ trường mạnh nhất ở hai đầu (hai cực).""",

    cau_hoi=[
        q("Vật liệu nào KHÔNG bị nam châm hút?", ["Sắt", "Thép", "Đồng", "Niken"], 2),
        q("Nam châm luôn có:", ["2 cực từ", "1 cực từ", "3 cực từ", "Không có cực"], 0),
        q("Khi đưa hai cực cùng tên lại gần nhau thì:", ["Đẩy nhau", "Hút nhau", "Không tác dụng", "Dính vào nhau"], 0),
        q("Môi trường xung quanh nam châm có khả năng tác dụng lực từ gọi là:", ["Từ trường", "Điện trường", "Trọng trường", "Chân không"], 0),
        q("Dụng cụ dùng để nhận biết từ trường là:", ["Kim nam châm thử", "Nhiệt kế", "Thước", "Vôn kế"], 0),
        q("Hình ảnh mạt sắt xếp quanh nam châm gọi là:", ["Từ phổ", "Điện phổ", "Đường sức điện", "Ảnh gương"], 0),
        q("Theo quy ước, đường sức từ bên ngoài nam châm:", ["Đi ra từ cực Bắc, đi vào cực Nam", "Đi ra từ cực Nam, vào cực Bắc", "Đi ngang", "Không có chiều"], 0),
        q("Nơi từ trường mạnh, các đường sức từ được vẽ:", ["Dày đặc hơn", "Thưa hơn", "Không vẽ", "Song song với nhau"], 0),
        q("Hai đường sức từ của cùng một nam châm:", ["Không cắt nhau", "Cắt nhau tại cực", "Cắt nhau ở giữa", "Trùng nhau"], 0),
        q("Khi bẻ đôi một thanh nam châm, kết quả là:", ["Mỗi đoạn vẫn có đủ cực N và S", "Một đoạn chỉ có N", "Một đoạn chỉ có S", "Mất từ tính hoàn toàn"], 0),
        q("Nung nóng nam châm nhiều lần có thể:", ["Làm giảm hoặc mất từ tính", "Tăng từ tính", "Không ảnh hưởng", "Đổi cực"], 0),
        q("Ở giữa thanh nam châm thẳng, từ tính:", ["Yếu nhất", "Mạnh nhất", "Bằng hai đầu", "Tăng dần"], 0),
        q("Từ trường đều là từ trường có các đường sức:", ["Thẳng, song song, cách đều", "Cong khép kín", "Tròn đồng tâm", "Cắt nhau"], 0),
        q("Kim nam châm nhỏ đặt trên một đường sức từ, cực N của kim:", ["Hướng theo chiều đường sức từ", "Ngược chiều đường sức", "Vuông góc đường sức", "Không định hướng"], 0),
        q("Để nhiễm từ cho một chiếc đinh sắt, ta làm cách nào?", ["Vuốt đinh theo một chiều dọc theo nam châm", "Nung đinh", "Ngâm đinh trong nước", "Gõ búa vào đinh"], 0),
        q("Ở hai đầu thanh nam châm hình chữ U, từ trường:", ["Mạnh nhất", "Yếu nhất", "Bằng không", "Ở giữa mạnh nhất"], 0),
        q("Cực N của hai thanh nam châm đặt gần nhau: hiện tượng nào đúng?", ["Đẩy nhau", "Hút nhau", "Không tác dụng", "Đổi cực"], 0),
        q("Vật liệu nào sau đây có thể bị nam châm hút?", ["Niken", "Nhôm", "Đồng", "Nhựa"], 0),
        q("Từ trường tồn tại ở đâu?", ["Xung quanh nam châm và dòng điện", "Chỉ trong nước", "Chỉ trong chân không", "Chỉ ở xích đạo"], 0),
        q("Hai thanh giống hệt nhau, một là nam châm, một là sắt. Đưa một đầu thanh A chạm vào điểm giữa thanh B thì hầu như không hút. Kết luận đúng là:", ["B là nam châm, A là sắt", "A là nam châm", "Cả hai đều là sắt", "Không kết luận được"], 0, "Từ tính ở điểm giữa nam châm rất yếu nên không hút mạnh; B là nam châm, A là thanh sắt."),
    ],

    bt_co_ban=[
        bt("Đưa cực N của kim nam châm lại gần một đầu thanh A, kim bị hút. Đầu A là cực gì?", ["Cực S", "S"], "Khác cực thì hút."),
        bt("Làm thế nào để xác định cực của một thanh nam châm không ghi cực, khi có kim nam châm đã biết cực?", ["Đưa cực N của kim lại gần; hút thì đầu đó là S, đẩy thì là N"], "Áp dụng quy luật tương tác từ."),
        bt("Vì sao cửa tủ lạnh có thể dính chặt vào thân tủ?", ["Có dải nam châm (cao su từ) ở mép cửa"], "Nam châm ở mép cửa hút với lớp kim loại trên thân tủ."),
        bt("Vỏ la bàn không được làm bằng sắt vì:", ["Sắt bị nhiễm từ, làm lệch kim nam châm"], "Vật bị nhiễm từ sẽ tác dụng lực lên kim la bàn."),
        bt("Một thanh nam châm bị gãy làm đôi. Mỗi mảnh có bao nhiêu cực?", ["Mỗi mảnh có 2 cực (N và S)", "2"], "Không có đơn cực từ."),
        bt("Trong cần cẩu phế liệu, nam châm điện có ưu điểm gì so với nam châm vĩnh cửu?", ["Ngắt điện là thả được vật, bật điện là hút được"], "Có thể bật/tắt từ tính bằng dòng điện."),
    ],

    bt_nang_cao=[
        nc("Có hai thanh giống hệt nhau về hình dạng, kích thước và màu sắc: một là nam châm, một là thanh sắt. Chỉ dùng hai thanh này, làm thế nào để phân biệt?",
           "Từ tính mạnh ở hai đầu, yếu ở giữa.",
           ["Đặt một đầu thanh A chạm vào điểm giữa thanh B. Hút mạnh ⇒ A là nam châm; hầu như không hút ⇒ A là sắt, B là nam châm"],
           "Đầu nam châm hút mạnh sắt ở mọi vị trí; còn điểm giữa nam châm có từ tính yếu nên hút rất ít."),
        nc("Một cây kim thép để gần nam châm lâu ngày, sau đó có thể hút được mạt sắt. Vì sao?",
           "Hiện tượng nhiễm từ.",
           ["Kim bị nhiễm từ, trở thành nam châm tạm thời"],
           "Các miền từ bên trong kim sắp xếp theo một hướng nhất định."),
        nc("Hai cực N của hai thanh nam châm đặt đối diện, gần nhau. Mô tả hiện tượng và từ phổ giữa chúng.",
           "Cùng tên đẩy nhau.",
           ["Hai thanh đẩy nhau; các đường sức đẩy ra hai bên, không nối liền giữa hai cực"],
           "Từ phổ có dạng các đường cong uốn ra xa nhau."),
        nc("Một thanh nam châm bị đốt nóng trên ngọn lửa. Từ tính của nó thay đổi thế nào? Vì sao?",
           "Nhiệt làm các nguyên tử dao động mạnh.",
           ["Từ tính giảm, có thể mất hẳn"],
           "Nhiệt phá vỡ sự sắp xếp định hướng của các miền từ bên trong."),
        nc("Một học sinh nói: 'Dùng búa đập vỡ cực Bắc của thanh nam châm thì chỉ còn lại cực Nam.' Nhận xét đúng hay sai? Vì sao?",
           "Không có đơn cực từ trong tự nhiên.",
           ["Sai. Mỗi mảnh vỡ tự tạo lại đủ cực N và S"],
           "Hai cực luôn đi đôi; mặt đứt gãy trở thành cực mới."),
        nc("Vẽ đường sức từ giữa hai nam châm thẳng đặt cùng trục, khác tên hút nhau. Mô tả chiều đường sức.",
           "Đường sức đi từ N sang S.",
           ["Các đường sức nối từ cực N của nam châm này tới cực S của nam châm kia"],
           "Khác tên nên các đường sức nối liền giữa hai nam châm."),
    ],
)

C4_B2 = bai(
    ly_thuyet="""📌 1. TỪ TRƯỜNG TRÁI ĐẤT
- Trái Đất hoạt động như một nam châm khổng lồ, có từ trường bao quanh.
- Nguyên nhân: dòng chuyển động của kim loại lỏng (sắt, niken) ở lõi ngoài Trái Đất.
- Từ cực Nam của Trái Đất nằm gần cực Bắc địa lí, từ cực Bắc nằm gần cực Nam địa lí. Chúng không trùng khít với cực địa lí.
- Góc giữa hướng Bắc địa lí và hướng Bắc từ gọi là góc từ thiên.

📌 2. LA BÀN
- La bàn gồm một kim nam châm nhẹ, quay tự do trên trục nhọn.
- Kim định hướng theo từ trường Trái Đất: cực N của kim chỉ về phía Bắc.
- Không đặt vật bằng sắt, thép hoặc dòng điện mạnh gần la bàn vì sẽ làm lệch kim.

📌 3. NAM CHÂM ĐIỆN VÀ ỨNG DỤNG
- Nam châm điện: cuộn dây dẫn có dòng điện, thường có lõi sắt non. Từ tính bật/tắt bằng dòng điện.
- Ứng dụng: loa điện, động cơ điện, rơle, cần cẩu nâng sắt thép, máy MRI (y tế).
- Nam châm có lực rất mạnh nên cần tránh đặt gần thẻ ngân hàng, ổ cứng; người có vật kim loại không nên vào gần máy MRI.

📌 4. ĐỘNG VẬT VÀ TỪ TRƯỜNG
- Một số loài chim, rùa biển, cá... có khả năng cảm nhận từ trường Trái Đất để định hướng khi di cư.

📌 5. VAI TRÒ CỦA TỪ TRƯỜNG TRÁI ĐẤT
- Từ quyển che chắn một phần các hạt mang điện năng lượng cao từ Mặt Trời, bảo vệ sự sống trên Trái Đất.""",

    vi_du="""💡 VÍ DỤ 1: Vì sao la bàn chỉ hướng Bắc?
Gần cực Bắc địa lí của Trái Đất có từ cực Nam. Cực N của kim la bàn bị từ cực Nam này hút nên kim chỉ về phía Bắc.

💡 VÍ DỤ 2: Vì sao phải tháo kim loại khi vào phòng MRI?
Máy MRI tạo từ trường rất mạnh. Vật bằng sắt, thép có thể bị hút mạnh, gây nguy hiểm; các thiết bị y tế kim loại có thể bị hỏng.

💡 VÍ DỤ 3: Nam châm điện trong cần cẩu
Khi bật điện, cuộn dây có dòng điện tạo từ trường mạnh, nam châm hút được khối thép. Khi tắt điện, từ trường mất, thép rơi xuống.""",

    cau_hoi=[
        q("Trái Đất có từ trường vì:", ["Lõi kim loại lỏng chuyển động tạo dòng điện", "Có ánh sáng", "Có nhiều nước", "Nằm gần Mặt Trời"], 0),
        q("Kim la bàn chỉ hướng Bắc địa lí vì:", ["Từ cực Nam của Trái Đất gần Bắc địa lí và hút cực N của kim", "Từ cực Bắc hút cực N", "Trái Đất quay", "Kim nặng"], 0),
        q("Góc giữa hướng Bắc từ và Bắc địa lí gọi là:", ["Góc từ thiên", "Góc tới", "Góc khúc xạ", "Góc nghiêng"], 0),
        q("Một số loài chim di cư tìm đường nhờ:", ["Cảm nhận từ trường Trái Đất", "Thị lực kém", "Tiếng gió", "Mùi hương"], 0),
        q("Lõi của nam châm điện thường là:", ["Sắt non", "Nhôm", "Nhựa", "Gỗ"], 0),
        q("Ưu điểm của nam châm điện so với nam châm vĩnh cửu:", ["Bật/tắt được từ tính bằng dòng điện", "Không bao giờ hỏng", "Nhẹ hơn", "Không có cực"], 0),
        q("Thiết bị dùng nam châm trong đời sống là:", ["Loa điện, động cơ điện", "Bếp gas", "Bàn là", "Nồi cơm điện"], 0),
        q("Vì sao thẻ ATM và ổ cứng không nên để gần nam châm mạnh?", ["Từ trường có thể làm nhiễu hoặc xóa dữ liệu từ tính", "Nam châm làm thẻ nóng", "Nam châm làm thẻ nặng", "Không ảnh hưởng"], 0),
        q("Vì sao bệnh nhân vào phòng MRI phải tháo đồ kim loại?", ["Từ trường rất mạnh hút các vật bằng kim loại", "Để tránh lạnh", "Để chụp đẹp hơn", "Vì kim loại phát sáng"], 0),
        q("Từ quyển Trái Đất có vai trò:", ["Che chắn một phần hạt mang điện năng lượng cao từ Mặt Trời", "Chắn ánh sáng", "Chắn âm thanh", "Giữ nhiệt"], 0),
        q("Vì sao kim la bàn đặt trên mặt bàn gần dây dẫn có dòng điện mạnh lại chỉ sai hướng?", ["Dòng điện tạo từ trường làm nhiễu từ trường Trái Đất", "Dòng điện làm kim nặng", "Dòng điện làm kim nóng", "Không có lí do"], 0),
        q("Vỏ la bàn thường làm bằng:", ["Nhựa, nhôm hoặc đồng", "Sắt", "Thép", "Niken"], 0),
        q("Từ cực Nam của Trái Đất nằm gần:", ["Cực Bắc địa lí", "Xích đạo", "Cực Nam địa lí", "Kinh tuyến 0°"], 0),
        q("Nam châm có thể hút được:", ["Đinh sắt", "Cốc nhựa", "Thước gỗ", "Sợi len"], 0),
        q("Lực tương tác giữa hai nam châm là:", ["Lực hút hoặc đẩy", "Lực điện", "Lực ma sát", "Không có"], 0),
        q("Đường sức từ ngoài nam châm thẳng có dạng:", ["Các đường cong đi từ cực N đến cực S", "Các vòng tròn đồng tâm", "Đường thẳng vuông góc", "Đường gấp khúc"], 0),
        q("Thanh nam châm chữ U có từ trường mạnh nhất ở:", ["Hai đầu nhánh", "Đáy chữ U", "Trung điểm đáy", "Khoảng trống giữa hai nhánh"], 0),
        q("Muốn tăng lực hút của nam châm điện, ta có thể:", ["Tăng cường độ dòng điện hoặc tăng số vòng dây", "Giảm dòng điện", "Tháo lõi sắt", "Đặt nam châm vào nước"], 0),
        q("Thiết bị nào dưới đây KHÔNG dùng nam châm?", ["La bàn", "Loa điện", "Cửa tủ lạnh có dải từ", "Bàn là điện"], 3, "Bàn là đốt nóng bằng điện trở, không dùng nam châm."),
        q("Trong phòng thí nghiệm, muốn xác định từ trường tại một điểm, ta đặt:", ["Kim nam châm thử tại điểm đó", "Thước đo", "Nhiệt kế", "Cân"], 0),
    ],

    bt_co_ban=[
        bt("Vì sao cực Bắc của kim la bàn luôn chỉ về hướng Bắc địa lí?", ["Gần cực Bắc địa lí có từ cực Nam của Trái Đất hút cực N của kim"], "Khác tên thì hút."),
        bt("Cắt đôi thanh nam châm ở giữa, ta được gì?", ["Hai nam châm, mỗi cái có đủ cực N và S"], "Không có đơn cực từ."),
        bt("Nam châm điện dùng trong cần cẩu bãi phế liệu có ưu điểm gì?", ["Ngắt điện là thả được vật, không cần lực thả"], "Từ tính biến mất khi ngắt điện."),
        bt("Kim nam châm định hướng Đông – Tây một cách bất thường. Nguyên nhân có thể là gì?", ["Có nam châm hoặc dòng điện mạnh ở gần"], "Từ trường bên ngoài làm nhiễu từ trường Trái Đất."),
        bt("Vì sao không đặt la bàn gần điện thoại hoặc loa lớn?", ["Vì từ trường của thiết bị làm sai kim la bàn"], "Các thiết bị này có nam châm hoặc dòng điện."),
        bt("Trong y tế, máy MRI có điều gì đặc biệt cần lưu ý với người bệnh?", ["Phải tháo mọi vật kim loại, đồ trang sức trước khi vào"], "Từ trường rất mạnh hút các vật từ tính."),
    ],

    bt_nang_cao=[
        nc("Vì sao nam châm được bọc bằng một lớp sắt dày thì từ trường bên ngoài yếu đi?",
           "Sắt là vật dẫn từ tốt.",
           ["Các đường sức từ đi qua lớp sắt nhiều hơn, ít thoát ra ngoài"],
           "Lớp sắt là đường khép kín thuận lợi cho từ trường nên từ trường tập trung bên trong."),
        nc("Đốt nóng nam châm trên ngọn lửa. Từ tính thay đổi thế nào? Giải thích.",
           "Nhiệt làm nguyên tử dao động mạnh.",
           ["Từ tính giảm dần, có thể mất hẳn"],
           "Nhiệt phá vỡ trật tự định hướng của các miền từ."),
        nc("Nếu Trái Đất mất từ trường, điều gì có thể xảy ra với sự sống?",
           "Vai trò che chắn của từ quyển.",
           ["Bức xạ và hạt mang điện từ Mặt Trời tác động mạnh hơn lên sinh vật và khí quyển"],
           "Từ quyển giúp làm lệch hướng các hạt mang điện năng lượng cao."),
        nc("Có ý kiến: 'Đứng đúng tại cực Bắc địa lí, kim la bàn sẽ quay loạn xạ.' Nhận xét thế nào về mặt vật lí?",
           "Đường sức từ gần cực đâm gần thẳng đứng xuống đất.",
           ["Có phần đúng: kim không định hướng ngang ổn định vì đường sức từ gần như thẳng đứng"],
           "Ở gần cực từ, đường sức gần như thẳng đứng nên kim không nằm ngang được, định hướng ngang trở nên khó khăn."),
        nc("Ở giữa hai cực N của hai nam châm đặt đối diện có một điểm mà kim nam châm thử không bị quay. Giải thích vì sao.",
           "Hai từ trường ngược chiều triệt tiêu tại điểm giữa.",
           ["Tại điểm giữa, từ trường của hai nam châm có độ lớn bằng nhau, ngược chiều nên triệt tiêu"],
           "Hai vectơ cảm ứng từ ngược chiều, cùng độ lớn, cộng lại bằng không."),
        nc("Để bảo quản nam châm chữ U lâu dài, người ta ghép hai nhánh bằng một thanh sắt. Vì sao việc này giữ từ tính tốt hơn?",
           "Tạo mạch từ khép kín.",
           ["Đường sức từ đi qua thanh sắt, khép kín, giảm từ trường rò rỉ và làm từ tính ổn định"],
           "Thanh sắt là đường dẫn từ, giữ từ trường trong mạch kín."),
    ],
)

VL7_CHUONG4 = {
    "Bài 1: Nam châm, từ trường và đường sức từ": C4_B1,
    "Bài 2: Trái Đất, la bàn và ứng dụng của nam châm": C4_B2,
}


# ============================================================
# GỘP VÀO CẤU TRÚC APP
# ============================================================
VATLY = {
    "Lớp 7": {
        "Chương 1: Tốc độ chuyển động": VL7_CHUONG1,
        "Chương 2: Âm thanh": VL7_CHUONG2,
        "Chương 3: Ánh sáng": VL7_CHUONG3,
        "Chương 4: Từ trường": VL7_CHUONG4,
    }
}


# ============================================================
# KIỂM TRA DỮ LIỆU
# ============================================================
def kiem_tra_vatly():
    loi = []
    for chuong, bais in VATLY["Lớp 7"].items():
        for ten_bai, d in bais.items():
            for i, c in enumerate(d["cau_hoi"], 1):
                if not (0 <= c["d"] < len(c["da"])):
                    loi.append(f"{chuong} / {ten_bai} / câu {i}: chỉ số đáp án sai")
                if len(set(c["da"])) != len(c["da"]):
                    loi.append(f"{chuong} / {ten_bai} / câu {i}: đáp án trùng nhau")
            for i, b in enumerate(d["bt_co_ban"], 1):
                if not b["dd"]:
                    loi.append(f"{chuong} / {ten_bai} / bài cơ bản {i}: thiếu đáp án")
            for i, b in enumerate(d["bt_nang_cao"], 1):
                if not b["dd"]:
                    loi.append(f"{chuong} / {ten_bai} / bài nâng cao {i}: thiếu đáp án")
    return loi


if __name__ == "__main__":
    tong_cau = sum(len(b["cau_hoi"]) for c in VATLY["Lớp 7"].values() for b in c.values())
    tong_cb = sum(len(b["bt_co_ban"]) for c in VATLY["Lớp 7"].values() for b in c.values())
    tong_nc = sum(len(b["bt_nang_cao"]) for c in VATLY["Lớp 7"].values() for b in c.values())
    print("Số chương:", len(VATLY["Lớp 7"]))
    print("Số câu trắc nghiệm:", tong_cau)
    print("Số bài tập cơ bản:", tong_cb)
    print("Số bài tập nâng cao:", tong_nc)
    ds_loi = kiem_tra_vatly()
    print("Lỗi dữ liệu:", "không có" if not ds_loi else ds_loi)
