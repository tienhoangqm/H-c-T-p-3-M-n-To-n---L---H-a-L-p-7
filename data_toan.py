# -*- coding: utf-8 -*-
"""TOÁN 7 KNTT — TOÀN BỘ NỘI DUNG (Tập 1 và Tập 2): Chương I–X.
File được ghép từ toan_c1.py … toan_c10.py. Biến xuất: TOAN."""


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
# FILE toan_c1.py
# ============================================================
# ============================================================
# BÀI 1: TẬP HỢP CÁC SỐ HỮU TỈ
# ============================================================
B1 = bai(
    ly_thuyet="""📌 1. SỐ HỮU TỈ
- Số hữu tỉ là số viết được dưới dạng phân số a/b với a, b ∈ ℤ, b ≠ 0.
- Tập hợp các số hữu tỉ kí hiệu là ℚ.
- Mỗi số nguyên, số thập phân hữu hạn, số thập phân vô hạn tuần hoàn đều là số hữu tỉ.
- Ví dụ: -7 = -7/1; 0,6 = 6/10; 1 4/5 = 9/5.

📌 2. SỐ ĐỐI
- Số đối của số hữu tỉ m là -m. Số đối của 0 là 0.
- Hai số đối nhau có tổng bằng 0: m + (-m) = 0.

📌 3. BIỂU DIỄN SỐ HỮU TỈ TRÊN TRỤC SỐ
- Chia đoạn đơn vị thành các phần bằng nhau, lấy một phần làm đơn vị mới.
- Số a/b (b > 0) nằm ở bên phải O nếu a > 0, bên trái O nếu a < 0.
- Hai điểm biểu diễn hai số đối nhau nằm về hai phía của O, cách O một khoảng bằng nhau.

📌 4. SO SÁNH HAI SỐ HỮU TỈ
- Viết hai số dưới dạng phân số có mẫu dương rồi so sánh tử số (hoặc so sánh trực tiếp nếu là số thập phân).
- Số hữu tỉ dương luôn lớn hơn 0; số hữu tỉ âm luôn nhỏ hơn 0.
- Trên trục số, nếu a < b thì điểm a nằm bên trái điểm b.
- Tính chất bắc cầu: nếu a < b và b < c thì a < c.
""",
    vi_du="""Ví dụ 1: Các số -7; 0,6; -1,2; 1 4/5 đều là số hữu tỉ vì:
-7 = -7/1;  0,6 = 6/10;  -1,2 = -12/10;  1 4/5 = 9/5.

Ví dụ 2: So sánh 0,7 và 6/5.
Ta có 0,7 = 7/10 và 6/5 = 12/10. Vì 7/10 < 12/10 nên 0,7 < 6/5.
Điểm 0,7 nằm trước điểm 6/5 trên trục số.

Ví dụ thực tế (chỉ số WHtR): chỉ số 0,5 nằm trong khoảng (0,42; 0,52] nên thuộc nhóm "Tốt".""",
    cau_hoi=[
        q("Số hữu tỉ là số viết được dưới dạng phân số a/b với điều kiện nào?", ["a, b ∈ ℤ, b ≠ 0", "a, b ∈ ℤ, a ≠ 0", "a, b ∈ ℕ", "a ∈ ℤ, b = 0"], 0, "Mẫu b phải khác 0."),
        q("Số nào là số hữu tỉ?", ["√2", "π", "-0,75", "√3"], 2, "-0,75 = -3/4."),
        q("Số đối của -2/5 là:", ["2/5", "-5/2", "5/2", "-2/5"], 0, "Số đối của -2/5 là 2/5."),
        q("Số đối của 0,6 là:", ["0,6", "-0,6", "1/0,6", "-1/0,6"], 1, "Số đối của 0,6 là -0,6."),
        q("Số hữu tỉ -3/4 viết dưới dạng số thập phân là:", ["-0,34", "-0,75", "-0,4", "-1,33"], 1, "3 : 4 = 0,75."),
        q("Số nào nằm giữa -1 và 0?", ["-2", "-1/2", "1/2", "-3"], 1, "-1 < -1/2 < 0."),
        q("Trong các số -1/2; -1/3; -2/3; -1/4, số lớn nhất là:", ["-1/2", "-1/3", "-2/3", "-1/4"], 3, "-1/4 ≈ -0,25 là số gần 0 nhất nên lớn nhất."),
        q("So sánh 2/3 và 3/5:", ["2/3 < 3/5", "2/3 > 3/5", "2/3 = 3/5", "Không so sánh được"], 1, "2/3 ≈ 0,67 > 0,6 = 3/5."),
        q("Trong các số -5/2; -3/2; 0; 1/3, số nhỏ nhất là:", ["-3/2", "-5/2", "0", "1/3"], 1, "-5/2 = -2,5 là nhỏ nhất."),
        q("Điểm biểu diễn số -3/2 trên trục số nằm ở đâu so với gốc O?", ["Bên phải O", "Bên trái O", "Trùng với O", "Không xác định"], 1, "Số âm nằm bên trái gốc O."),
        q("Số 0,25 viết dưới dạng phân số tối giản là:", ["25/100", "1/4", "2/5", "5/20"], 1, "0,25 = 25/100 = 1/4."),
        q("Phân số nào KHÔNG biểu diễn số -2/3?", ["-4/6", "2/-3", "4/-6", "4/6"], 3, "4/6 = 2/3 > 0, khác -2/3."),
        q("Số nguyên -4 có phải là số hữu tỉ không?", ["Không, vì là số âm", "Có, vì -4 = -4/1", "Không, vì không viết được dạng phân số", "Có, nhưng chỉ khi là số dương"], 1, "Mọi số nguyên đều là số hữu tỉ."),
        q("Chỉ số WHtR = 0,5 thuộc nhóm nào theo bảng đánh giá?", ["Gầy", "Tốt", "Hơi béo", "Béo phì"], 1, "0,42 < 0,5 ≤ 0,52 là nhóm Tốt."),
        q("Số đối của số 0 là:", ["1", "-1", "0", "Không có"], 2, "0 là số đối của chính nó."),
        q("Trên trục số, điểm biểu diễn -a và a nằm đối xứng qua điểm nào?", ["Điểm O", "Điểm -a", "Điểm a", "Điểm 1"], 0, "Hai số đối nhau đối xứng qua gốc O."),
        q("Trong các số sau, số hữu tỉ dương là:", ["0", "-1/2", "3/7", "-5"], 2, "3/7 > 0."),
        q("Số 5/-7 bằng số nào?", ["-5/7", "5/7", "-7/5", "7/-5"], 0, "5/-7 = -5/7."),
        q("Tập hợp các số hữu tỉ được kí hiệu là:", ["ℕ", "ℤ", "ℚ", "ℝ"], 2, "ℚ là tập các số hữu tỉ."),
        q("Số thập phân 1,5 viết dưới dạng phân số là:", ["15/10", "1/5", "5/1", "15/1"], 0, "1,5 = 15/10 = 3/2."),
        q("Số -0,625 viết dưới dạng phân số tối giản là:", ["-5/8", "-625/10", "-6/25", "-8/5"], 0, "-0,625 = -625/1000 = -5/8."),
        q("Có bao nhiêu số hữu tỉ x thỏa mãn x = -x?", ["0", "1", "2", "Vô số"], 0, "Chỉ có x = 0."),
        q("Số nào lớn hơn -1/3?", ["-1/2", "-2/3", "-1/4", "-1"], 2, "-1/4 ≈ -0,25 > -0,33 ≈ -1/3."),
        q("Khoảng cách từ điểm 3/4 đến gốc O trên trục số là:", ["3/4", "-3/4", "4/3", "0"], 0, "Khoảng cách bằng giá trị tuyệt đối 3/4."),
        q("Mỗi số hữu tỉ x có bao nhiêu số đối?", ["0", "1", "2", "Vô số"], 1, "Mỗi số có đúng một số đối."),
        q("Số thập phân vô hạn tuần hoàn 0,(3) bằng số hữu tỉ nào?", ["1/3", "3/10", "3/100", "Không phải số hữu tỉ"], 0, "0,(3) = 1/3."),
        q("Số 8 có phải là số hữu tỉ không?", ["Không", "Có, 8 = 8/1", "Có, 8 = 8/2", "Không, vì 8 là số tự nhiên"], 1, "8 = 8/1 nên là số hữu tỉ."),
        q("Số nào có giá trị bằng -1 1/5?", ["-6/5", "-5/6", "-1/5", "-5/1"], 0, "-1 1/5 = -6/5."),
        q("Sắp xếp -2/3; -1/2; 0; 1/4 theo thứ tự từ bé đến lớn:", ["-1/2; -2/3; 0; 1/4", "-2/3; -1/2; 0; 1/4", "0; 1/4; -1/2; -2/3", "1/4; 0; -1/2; -2/3"], 1, "-2/3 ≈ -0,67 < -0,5 < 0 < 0,25."),
        q("So sánh -5/4 và -4/5:", ["-5/4 < -4/5", "-5/4 > -4/5", "-5/4 = -4/5", "Không so sánh được"], 0, "-5/4 = -1,25 < -0,8 = -4/5."),
        q("Số đối của -(-3/7) là:", ["3/7", "-3/7", "7/3", "-7/3"], 0, "-(-3/7) = 3/7 là số đối của -3/7."),
        q("Hai số đối nhau -1/2 và 1/2 cách O một khoảng bằng:", ["1/2 đơn vị", "1 đơn vị", "0", "2 đơn vị"], 0, "Hai số đối cách O cùng một khoảng."),
        q("Ba số 0,5; 1/2; 5/10 có quan hệ thế nào?", ["Chỉ 0,5 và 1/2 bằng nhau", "Cả ba số bằng nhau", "Chỉ 1/2 và 5/10 bằng nhau", "Không số nào bằng nhau"], 1, "0,5 = 1/2 = 5/10."),
        q("Phân số nào KHÔNG bằng -3/5?", ["3/-5", "-3/-5", "-6/10", "-9/15"], 1, "-3/-5 = 3/5 > 0, khác -3/5."),
    ],
    bt_co_ban=[
        bt("Hãy cho biết đúng hay sai: a) 0,25 ∈ ℚ;  b) -6/7 ∈ ℚ;  c) -235 ∉ ℚ.", ["a) đúng; b) đúng; c) sai"], "Mọi số nguyên, phân số đều thuộc ℚ nên c) sai."),
        bt("Tìm số đối của -0,75.", ["0,75"], "Số đối của -0,75 là 0,75."),
        bt("Tìm số đối của 6 1/5.", ["-31/5", "-6,2"], "6 1/5 = 31/5 nên số đối là -31/5."),
        bt("Viết -0,625 dưới dạng phân số tối giản.", ["-5/8"], "-0,625 = -5/8."),
        bt("Điền dấu < hoặc > vào chỗ trống: -2,5 ... -2,125.", ["<"], "-2,5 < -2,125 vì 2,5 > 2,125 nên -2,5 nhỏ hơn."),
        bt("So sánh: -1/10000 và -1/23456.", ["<"], "Phân số có tử bằng nhau, mẫu càng lớn thì giá trị âm càng gần 0, nên -1/10000 < -1/23456."),
        bt("Sắp xếp các số 83; 82,5; 83 1/5; 81 2/5; 78 1/2 theo thứ tự từ nhỏ đến lớn.", ["78 1/2; 81 2/5; 82,5; 83; 83 1/5"], "Đổi về số thập phân để so sánh."),
        bt("Số nào trong các phân số sau biểu diễn số -0,625: 5/-8; 10/16; 20/-32; -10/16; -25/40; 35/-48?", ["5/-8; 20/-32; -10/16; -25/40"], "Kiểm tra mỗi phân số bằng -0,625 = -5/8."),
        bt("Số nào trong ℚ là số đối của chính nó?", ["0"], "Số đối của 0 là 0."),
    ],
    bt_nang_cao=[
        nc("Trên trục số, điểm A biểu diễn -1/2 và điểm B biểu diễn 1/3. Điểm nào nằm bên phải gốc O?", "Số dương nằm bên phải O.", ["B"], "1/3 > 0 nên B nằm bên phải O; -1/2 < 0 nên A nằm bên trái O."),
        nc("Chứng minh rằng 0,(6) là số hữu tỉ bằng cách đưa về phân số.", "Đặt x = 0,(6), nhân 10 rồi trừ.", ["2/3"], "x = 0,666...; 10x = 6,666...; 9x = 6; x = 6/9 = 2/3."),
        nc("Lấy số đối của 3/4 rồi cộng với 1/4. Kết quả là bao nhiêu?", "Số đối của 3/4 là -3/4.", ["-1/2", "-0,5"], "-3/4 + 1/4 = -2/4 = -1/2."),
        nc("Có bao nhiêu số nguyên x thỏa mãn -3 < x/2 < 1?", "Nhân hai vế với 2.", ["7"], "Nhân hai vế với 2: -6 < x < 2, nên x ∈ {-5, -4, -3, -2, -1, 0, 1}: có 7 số."),
        nc("Viết số hữu tỉ dương nhỏ hơn 1/2 và lớn hơn 1/3 có mẫu là 12.", "Quy đồng về mẫu 12.", ["5/12"], "1/3 = 4/12 < x < 6/12 = 1/2 nên x = 5/12."),
        nc("Viết một số hữu tỉ nằm giữa -1/2 và -1/3 có mẫu là 12.", "Đưa hai số về mẫu 12.", ["-5/12"], "-1/2 = -6/12 < -5/12 < -4/12 = -1/3."),
    ],
)


# ============================================================
# BÀI 2: CỘNG, TRỪ, NHÂN, CHIA SỐ HỮU TỈ
# ============================================================
B2 = bai(
    ly_thuyet="""📌 1. CỘNG VÀ TRỪ HAI SỐ HỮU TỈ
- Viết các số hữu tỉ dưới dạng phân số có mẫu dương, rồi áp dụng quy tắc cộng, trừ phân số.
- a/m + b/m = (a+b)/m;  a/b - c/d = a/b + (-c/d).
- Tính chất giao hoán, kết hợp như với số nguyên: x + y = y + x; (x + y) + z = x + (y + z).
- Hai số đối nhau có tổng bằng 0: a + (-a) = 0.
- Quy tắc dấu ngoặc: "+(...)" giữ nguyên dấu; "-(...)" đổi dấu tất cả các số hạng bên trong.

📌 2. NHÂN VÀ CHIA HAI SỐ HỮU TỈ
- Nhân: (a/b)·(c/d) = (a·c)/(b·d).
- Chia: (a/b) : (c/d) = (a/b)·(d/c) với c/d ≠ 0.
- Quy tắc dấu: hai số cùng dấu cho tích dương; khác dấu cho tích âm.
- Tính chất giao hoán, kết hợp, phân phối của phép nhân đối với phép cộng: a·(b + c) = a·b + a·c.
- Số nghịch đảo của a/b (a ≠ 0) là b/a.

📌 3. LƯU Ý
- Nếu các số đều viết dưới dạng số thập phân, có thể áp dụng quy tắc cộng, trừ, nhân, chia số thập phân.
""",
    vi_du="""Ví dụ 1: Tính -2/3 + 1/4 + 2,5 ...
Đổi về phân số: -2/3 + 1/4 = (-8 + 3)/12 = -5/12.

Ví dụ 2: Tính 8/9 - [7/4 - (3/4 - 2/3)]
= 8/9 - 7/4 + (3/4 - 2/3) = (8/9 - 2/3) - (7/4 - 3/4) = (8/9 - 6/9) - 1 = 2/9 - 1 = -7/9.

Ví dụ 3: Tính (6/7)·0,25 = (6/7)·(1/4) = 6/28 = 3/14.
Ví dụ 4 (bài toán mở đầu): khinh khí cầu bay lên 0,8·50 = 40 m; giảm 5/9·27 = 15 m; cách mặt đất 40 - 15 = 25 m.""",
    cau_hoi=[
        q("Kết quả của -2/3 + 1/4 là:", ["-5/12", "-1/12", "5/12", "-11/12"], 0, "-8/12 + 3/12 = -5/12."),
        q("Kết quả của 3/5 - (-1/5) là:", ["2/5", "4/5", "-2/5", "-4/5"], 1, "3/5 + 1/5 = 4/5."),
        q("Kết quả của (-2/3)·(3/4) là:", ["-1/2", "1/2", "-2/3", "-6/7"], 0, "-6/12 = -1/2."),
        q("Kết quả của (-4/5) : (2/3) là:", ["-6/5", "-8/15", "6/5", "-5/6"], 0, "(-4/5)·(3/2) = -12/10 = -6/5."),
        q("Kết quả của -0,5 + 1/3 là:", ["-1/6", "1/6", "-5/6", "5/6"], 0, "-1/2 + 1/3 = -3/6 + 2/6 = -1/6."),
        q("Kết quả của -1,5 · 2/3 là:", ["-1", "1", "-3/2", "-2/3"], 0, "-3/2 · 2/3 = -1."),
        q("Kết quả của 0,25 · (-4) là:", ["-1", "1", "-0,1", "-16"], 0, "0,25·4 = 1 nên kết quả là -1."),
        q("Kết quả của (-7) - (-5/8) là:", ["-51/8", "-61/8", "-35/8", "51/8"], 0, "-56/8 + 5/8 = -51/8."),
        q("Kết quả của 2 : (-1/4) là:", ["-8", "8", "-1/8", "-1/2"], 0, "2 · (-4) = -8."),
        q("Tổng của hai số đối nhau bằng:", ["0", "2a", "a", "-2a"], 0, "a + (-a) = 0."),
        q("Kết quả của 5/6 - 1/4 + (-1/2) là:", ["1/12", "-1/12", "11/12", "-7/12"], 0, "10/12 - 3/12 - 6/12 = 1/12."),
        q("Kết quả của (-1/2)·(-1/2) là:", ["1/4", "-1/4", "1/2", "-1/2"], 0, "Tích hai số âm là số dương."),
        q("Kết quả của (-3/4) : (-3/4) là:", ["1", "-1", "0", "-9/16"], 0, "Số chia bằng số bị chia nên thương bằng 1."),
        q("Tích hai số hữu tỉ âm là:", ["Số âm", "Số dương", "Số 0", "Không xác định"], 1, "Dấu: (-)·(-) = (+)."),
        q("Số nghịch đảo của -5/3 là:", ["-3/5", "3/5", "-5/3", "5/3"], 0, "Nghịch đảo của -5/3 là -3/5."),
        q("Kết quả của -0,75 · (-4/3) là:", ["1", "-1", "-3/4", "3"], 0, "3/4 · 4/3 = 1."),
        q("Kết quả của (-5) : 1/2 là:", ["-10", "10", "-5/2", "-2,5"], 0, "-5 · 2 = -10."),
        q("Kết quả của 2/5 · (-5) + 1 là:", ["-1", "1", "-3", "3"], 0, "-2 + 1 = -1."),
        q("Công thức chia hai phân số a/b : c/d (c, d ≠ 0) là:", ["a/b · d/c", "a/b · c/d", "a/b + d/c", "(a·b)/(c·d)"], 0, "Chia cho phân số là nhân với nghịch đảo."),
        q("Kết quả của 1,2 · (-3,5) là:", ["-4,2", "4,2", "-42", "-0,42"], 0, "1,2·3,5 = 4,2."),
        q("Kết quả của (-6,3) : 0,9 là:", ["-7", "7", "-5,4", "-0,7"], 0, "6,3 : 0,9 = 7."),
        q("Kết quả của -12 : 3/4 là:", ["-16", "16", "-9", "-4/9"], 0, "-12 · 4/3 = -16."),
        q("Kết quả của -2 + 0,5 là:", ["-1,5", "1,5", "-2,5", "2,5"], 0, "-2 + 0,5 = -1,5."),
        q("Giá trị của (-3/4) + (2/3)·(-3/2) là:", ["-7/4", "-1/4", "1/4", "-5/4"], 0, "(2/3)·(-3/2) = -1 nên -3/4 - 1 = -7/4."),
        q("Tích của -1 và 0 bằng:", ["0", "-1", "1", "Không xác định"], 0, "Số nhân với 0 bằng 0."),
        q("Kết quả của 4,5 · (-2) · (-3,2) là:", ["28,8", "-28,8", "-14,4", "14,4"], 0, "4,5·(-2) = -9; -9·(-3,2) = 28,8."),
        q("Theo tính chất phân phối, a·(b + c) bằng:", ["ab + ac", "ab + bc", "a + bc", "ab + c"], 0, "a·(b+c) = ab + ac."),
        q("Số x thỏa mãn x - 3/5 = -1/10 là:", ["1/2", "-1/2", "7/10", "-7/10"], 0, "x = 3/5 - 1/10 = 6/10 - 1/10 = 1/2."),
        q("Kết quả của (-3)·(-2,5) : (-5) là:", ["-1,5", "1,5", "-7,5", "7,5"], 0, "7,5 : (-5) = -1,5."),
        q("Kết quả của (-2/5)·(1/2) là:", ["-1/5", "1/5", "-2/3", "-3/5"], 0, "-2/10 = -1/5."),
        q("Một bình có 3/4 lít nước, rót ra 1/3 lít. Còn lại bao nhiêu lít?", ["5/12", "1/12", "13/12", "5/7"], 0, "3/4 - 1/3 = 9/12 - 4/12 = 5/12."),
        q("Kết quả của (-1/3)·(3/2)·(-2) là:", ["1", "-1", "2", "-2/3"], 0, "(-1/3)·(3/2) = -1/2; -1/2·(-2) = 1."),
        q("Kết quả của 1/2 + (-1/3) - (-1/6) là:", ["1/3", "-1/3", "2/3", "0"], 0, "3/6 - 2/6 + 1/6 = 2/6 = 1/3."),
        q("Trong Q, phép chia cho số 0:", ["Không thực hiện được", "Cho kết quả 0", "Cho kết quả 1", "Cho kết quả là số đối"], 0, "Không chia cho 0."),
        q("Kết quả của (-2)·(-3)·(-4) là:", ["-24", "24", "-9", "9"], 0, "Tích ba số âm là số âm: 2·3·4 = 24."),
        q("Giá trị của 1,25 · (-4,6) là:", ["-5,75", "5,75", "-0,575", "-57,5"], 0, "1,25·4,6 = 5,75."),
        q("Giá trị của 7,8 : (-0,13) là:", ["-60", "60", "-6", "6"], 0, "7,8 : 0,13 = 60; dấu âm."),
        q("Kết quả của (-0,4)·(-0,4) là:", ["0,16", "-0,16", "0,8", "-0,8"], 0, "Tích hai số âm là số dương: 0,16."),
        q("Kết quả của 3/4 : (-3/2) là:", ["-1/2", "1/2", "-9/8", "9/8"], 0, "3/4 · (-2/3) = -1/2."),
    ],
    bt_co_ban=[
        bt("Tính: -6/18 + 18/27.", ["1/3"], "-1/3 + 2/3 = 1/3."),
        bt("Tính: 2,5 - (-6/9).", ["19/6"], "5/2 + 2/3 = 15/6 + 4/6 = 19/6."),
        bt("Tính: -0,32 · (-0,875).", ["0,28", "0.28"], "0,32·0,875 = 0,28."),
        bt("Tính: (-5) : 2 1/5.", ["-25/11"], "-5 : 11/5 = -25/11."),
        bt("Tính: (-7) - (-5/8).", ["-51/8"], "-7 + 5/8 = -51/8."),
        bt("Tính: -21,25 + 13,3.", ["-7,95"], "-21,25 + 13,30 = -7,95."),
        bt("Tính: 8/9 - [7/4 - (3/4 - 2/3)].", ["-7/9"], "Bỏ dấu ngoặc lần lượt."),
        bt("Tính: 9/10 - (6/5 - 7/4).", ["29/20"], "6/5 - 7/4 = -11/20; 9/10 + 11/20 = 29/20."),
    ],
    bt_nang_cao=[
        nc("Tính hợp lý: A = 37/5 + (-0,7) + 5/2 + (-4,3).", "Đổi 37/5 = 7,4; nhóm các số thập phân.", ["4,9"], "A = (7,4 + 2,5) + (-0,7 - 4,3) = 9,9 - 5 = 4,9."),
        nc("Tính hợp lý: B = 3/2 · (-37/10) + 17/2 · (-37/10).", "Đặt thừa số chung (-37/10).", ["-37"], "B = (3/2 + 17/2)·(-37/10) = 10·(-37/10) = -37."),
        nc("Tính hợp lý: A = 12,4 · 6 1/4 + (-12,4)·(-2,5)².", "(-2,5)² = 6,25 = 6 1/4.", ["0"], "A = 12,4·6,25 + (-12,4)·6,25 = 0."),
        nc("Tính: P = (1/2 - 1/3 + 1/4)·(-12).", "Tính trong ngoặc trước.", ["-5"], "1/2 - 1/3 + 1/4 = 5/12; 5/12·(-12) = -5."),
        nc("Tìm x biết: x - 2/3 = 1/3 - x.", "Chuyển các số hạng chứa x về một vế.", ["1/2", "0,5"], "2x = 1 nên x = 1/2."),
        nc("Tính hợp lý: C = 7/6 · 3 1/4 + 7/6 · (-0,25).", "Đưa 7/6 làm thừa số chung.", ["7/2", "3,5"], "C = 7/6·(3 1/4 - 0,25) = 7/6·3 = 7/2."),
    ],
)


# ============================================================
# BÀI 3: LUỸ THỪA VỚI SỐ MŨ TỰ NHIÊN CỦA MỘT SỐ HỮU TỈ
# ============================================================
B3 = bai(
    ly_thuyet="""📌 1. LUỸ THỪA VỚI SỐ MŨ TỰ NHIÊN
- Luỹ thừa bậc n của số hữu tỉ x: xⁿ = x·x·…·x (n thừa số), với x ∈ ℚ, n ∈ ℕ, n > 1.
- x gọi là cơ số, n gọi là số mũ.
- Quy ước: x⁰ = 1 (x ≠ 0); x¹ = x.

📌 2. NHÂN VÀ CHIA HAI LUỸ THỪA CÙNG CƠ SỐ
- Nhân: xᵐ · xⁿ = xᵐ⁺ⁿ (giữ nguyên cơ số, cộng số mũ).
- Chia: xᵐ : xⁿ = xᵐ⁻ⁿ (x ≠ 0, m ≥ n).

📌 3. LUỸ THỪA CỦA MỘT TÍCH, MỘT THƯƠNG
- (x·y)ⁿ = xⁿ·yⁿ.
- (x/y)ⁿ = xⁿ/yⁿ (y ≠ 0).

📌 4. LUỸ THỪA CỦA LUỸ THỪA
- (xᵐ)ⁿ = xᵐ·ⁿ (giữ nguyên cơ số, nhân hai số mũ).

📌 5. LƯU Ý DẤU
- Luỹ thừa bậc chẵn của số âm là số dương; bậc lẻ của số âm là số âm.
""",
    vi_du="""Ví dụ 1: (-3)³ = (-3)·(-3)·(-3) = -27;  (1/3)⁴ = 1/81.

Ví dụ 2: 2²·3² = 4·9 = 36 và (2·3)² = 6² = 36. Vậy 2²·3² = (2·3)².

Ví dụ 3: (2/3)⁵·(2/3)³ = (2/3)⁸ = 256/6561;  (-5)⁵ : (-5)⁵ = (-5)⁰ = 1.

Ví dụ 4: [(-5)³]⁷ = (-5)^(3·7) = (-5)²¹.""",
    cau_hoi=[
        q("Kết quả của (-2)³ là:", ["-8", "8", "-6", "6"], 0, "(-2)³ = -8."),
        q("Kết quả của (1/3)⁴ là:", ["1/81", "1/12", "4/3", "1/3"], 0, "(1/3)⁴ = 1/81."),
        q("Kết quả của (-0,5)² là:", ["0,25", "-0,25", "0,5", "-0,5"], 0, "Bình phương số âm là số dương."),
        q("Với x ≠ 0, x⁰ bằng:", ["0", "1", "x", "Không xác định"], 1, "Quy ước x⁰ = 1."),
        q("Với mọi x, x¹ bằng:", ["1", "x", "x²", "0"], 1, "x¹ = x."),
        q("Kết quả của (2/3)² là:", ["4/9", "2/9", "4/6", "6/4"], 0, "(2/3)² = 4/9."),
        q("Kết quả của 2²·3² là:", ["36", "13", "12", "6"], 0, "2²·3² = 4·9 = 36."),
        q("Kết quả của 2³ · 2⁴ là:", ["2⁷", "2¹²", "2¹", "4⁷"], 0, "2³·2⁴ = 2⁷."),
        q("Kết quả của 5⁶ : 5² là:", ["5⁴", "5³", "5⁸", "1"], 0, "5⁶⁻² = 5⁴."),
        q("Kết quả của (x²)³ là:", ["x⁵", "x⁶", "x⁸", "x⁹"], 1, "(x²)³ = x⁶."),
        q("Kết quả của (-3)²·(-3)³ là:", ["(-3)⁵", "(-3)⁶", "(-3)¹", "9⁵"], 0, "(-3)^(2+3) = (-3)⁵."),
        q("Kết quả của (-1)⁹ là:", ["-1", "1", "9", "-9"], 0, "Luỹ thừa bậc lẻ của -1 là -1."),
        q("Kết quả của (-1)¹⁰ là:", ["1", "-1", "10", "-10"], 0, "Luỹ thừa bậc chẵn của -1 là 1."),
        q("Số 1 000 000 viết dưới dạng luỹ thừa của 10 là:", ["10⁵", "10⁶", "10⁷", "6¹⁰"], 1, "Có 6 chữ số 0 nên là 10⁶."),
        q("Thể tích hình lập phương cạnh a được tính bằng:", ["3a", "a²", "a³", "a + 3"], 2, "V = a³."),
        q("Kết quả của (0,2)³ là:", ["0,008", "0,06", "0,6", "0,0008"], 0, "0,2³ = 0,008."),
        q("Kết quả của (-2/5)² là:", ["4/25", "-4/25", "4/10", "-2/10"], 0, "Bình phương số âm là dương."),
        q("Kết quả của (5/6)⁰ là:", ["0", "1", "5/6", "Không xác định"], 1, "Mọi cơ số khác 0 luỹ thừa 0 bằng 1."),
        q("Kết quả của (-7)² là:", ["49", "-49", "14", "-14"], 0, "(-7)² = 49."),
        q("Biểu thức nào có kết quả âm?", ["(-2)⁴", "(-2)³", "(-1)²", "2²"], 1, "(-2)³ = -8."),
        q("Kết quả của x³ · x² là:", ["x⁵", "x⁶", "x¹", "x⁹"], 0, "x^(3+2) = x⁵."),
        q("Kết quả của (xy)² là:", ["x²y²", "x² + y²", "2xy", "x²y"], 0, "(xy)² = x²y²."),
        q("Kết quả của (a/b)ⁿ là:", ["aⁿ/bⁿ", "aⁿ·bⁿ", "a/bⁿ", "a^(n+b)"], 0, "Luỹ thừa của thương bằng thương các luỹ thừa."),
        q("Kết quả của (-3)⁴ là:", ["81", "-81", "12", "-12"], 0, "Bậc chẵn nên dương: 81."),
        q("Kết quả của 2¹⁰ : 2⁸ là:", ["4", "2", "16", "1024"], 0, "2^(10-8) = 2² = 4."),
        q("Số 100 000 000 viết dưới dạng luỹ thừa của 10 là:", ["10⁶", "10⁸", "10⁹", "8¹⁰"], 1, "Có 8 chữ số 0 nên là 10⁸."),
        q("Kết quả của (1/2)³ · 8 là:", ["1", "8", "1/8", "4"], 0, "(1/8)·8 = 1."),
        q("Với x ≠ 0, điều kiện để xᵐ : xⁿ = xᵐ⁻ⁿ là:", ["m ≥ n", "m ≤ n", "m > 0", "x > 0"], 0, "Khi chia, số mũ bị chia phải lớn hơn hoặc bằng số mũ chia."),
        q("Kết quả của (-1/2)³ là:", ["-1/8", "1/8", "-1/6", "-3/2"], 0, "(-1/2)³ = -1/8."),
        q("So sánh 2⁵ và 5²:", ["2⁵ > 5²", "2⁵ < 5²", "2⁵ = 5²", "Không so sánh được"], 0, "32 > 25."),
        q("Kết quả của 3² + 4² là:", ["25", "49", "14", "7"], 0, "9 + 16 = 25."),
        q("Số 81 viết dưới dạng luỹ thừa của 3 là:", ["3³", "3⁴", "3⁵", "4³"], 1, "81 = 3⁴."),
        q("Kết quả của (-0,1)⁴ là:", ["0,0001", "-0,0001", "0,004", "-0,4"], 0, "Bậc chẵn nên dương."),
        q("Kết quả của (-2)³ · (-2)² là:", ["-32", "32", "-64", "-8"], 0, "(-2)⁵ = -32."),
    ],
    bt_co_ban=[
        bt("Viết các số 125 và 3 125 dưới dạng luỹ thừa của 5.", ["5³; 5⁵", "5^3; 5^5"], "125 = 5³; 3125 = 5⁵."),
        bt("Viết (1/9)⁵ và (1/27)⁷ dưới dạng luỹ thừa cơ số 1/3.", ["(1/3)^10; (1/3)^21"], "(1/9)⁵ = (1/3)¹⁰; (1/27)⁷ = (1/3)²¹."),
        bt("Không dùng máy tính, tính (-3)⁸ biết (-3)⁷ = -2187.", ["6561"], "(-3)⁸ = (-3)⁷·(-3) = 6561."),
        bt("Tính (1 + 1/2 - 1/4)²·(2 + 3/7).", ["425/112"], "(5/4)²·(17/7) = 25/16·17/7 = 425/112."),
        bt("Tính 4 : (1/2 - 1/3)³.", ["864"], "(1/6)³ = 1/216; 4 : 1/216 = 864."),
        bt("Tính (-2)⁴.", ["16"], "(-2)⁴ = 16."),
        bt("Tính (0,5)³.", ["0,125"], "0,5³ = 0,125."),
        bt("Tính 10² · 10³.", ["10^5", "100000"], "10²·10³ = 10⁵."),
    ],
    bt_nang_cao=[
        nc("Khoảng cách từ Mộc tinh đến Mặt Trời là 7,78·10⁸ km; từ Trái Đất đến Mặt Trời là 1,5·10⁸ km. Khoảng cách từ Mộc tinh gấp khoảng bao nhiêu lần khoảng cách từ Trái Đất đến Mặt Trời?", "Lấy tỉ số hai khoảng cách.", ["5,2", "khoảng 5,2"], "7,78·10⁸ : 1,5·10⁸ ≈ 5,19 ≈ 5,2 lần."),
        nc("Sắp xếp các quốc gia theo số lượt khách đến Việt Nam từ nhỏ đến lớn: Hàn Quốc 4,3·10⁶; Hoa Kỳ 7,4·10⁵; Pháp 2,9·10⁵; Ý 7·10⁴.", "So sánh các luỹ thừa của 10.", ["Ý, Pháp, Hoa Kỳ, Hàn Quốc"], "7·10⁴ < 2,9·10⁵ < 7,4·10⁵ < 4,3·10⁶."),
        nc("Tìm x biết 2ˣ = 32.", "32 = 2⁵.", ["5"], "2ˣ = 2⁵ nên x = 5."),
        nc("Tìm số tự nhiên x biết (x - 1)² = 9 và x > 1.", "x - 1 là căn bậc hai của 9.", ["4"], "x - 1 = 3 nên x = 4."),
        nc("Tính 2²⁰ · 5²⁰.", "Viết 2²⁰·5²⁰ = (2·5)²⁰.", ["10^20", "100000000000000000000"], "(2·5)²⁰ = 10²⁰."),
        nc("Tính (-2/3)¹² biết (-2/3)¹¹ = -2048/177147.", "Nhân thêm một thừa số -2/3.", ["4096/531441"], "(-2048/177147)·(-2/3) = 4096/531441."),
    ],
)


# ============================================================
# BÀI 4: THỨ TỰ THỰC HIỆN CÁC PHÉP TÍNH. QUY TẮC CHUYỂN VẾ
# ============================================================
B4 = bai(
    ly_thuyet="""📌 1. THỨ TỰ THỰC HIỆN CÁC PHÉP TÍNH
- Biểu thức không có dấu ngoặc: thực hiện theo thứ tự Luỹ thừa → Nhân và chia → Cộng và trừ.
- Biểu thức chỉ có cộng, trừ (hoặc chỉ có nhân, chia): thực hiện từ trái sang phải.
- Biểu thức có dấu ngoặc: thực hiện trong ngoặc tròn ( ) trước, rồi ngoặc vuông [ ], cuối cùng ngoặc nhọn { }.

📌 2. ĐẲNG THỨC
- Đẳng thức là hai biểu thức nối với nhau bởi dấu "=". Vế trái ở bên trái, vế phải ở bên phải.
- Nếu a = b thì b = a; và a + c = b + c.

📌 3. QUY TẮC CHUYỂN VẾ
- Khi chuyển một số hạng từ vế này sang vế kia của đẳng thức, ta đổi dấu số hạng đó: dấu "+" thành "-", dấu "-" thành "+".
- Nếu a + b = c thì a = c - b.
- Nếu a - b = c thì a = c + b.
""",
    vi_du="""Ví dụ 1: Tính 1,2 - 3² + 7,5 : 3
= 1,2 - 9 + 2,5 = -5,3.

Ví dụ 2: Tìm a biết a + 6 = -9 → a = -9 - 6 = -15. Tìm b biết b - 8 = -3 → b = -3 + 8 = 5.

Ví dụ 3: Tìm x biết x + 1/2 = -6/7 → x = -6/7 - 1/2 = -19/14.
Tìm x biết x - 3/4 = 9/8 → x = 9/8 + 3/4 = 15/8.""",
    cau_hoi=[
        q("Kết quả của 2 + 3·4 là:", ["20", "14", "24", "10"], 1, "Nhân trước, cộng sau: 2 + 12 = 14."),
        q("Kết quả của 1,2 - 3² + 7,5 : 3 là:", ["-5,3", "-3,3", "5,3", "-7,3"], 0, "1,2 - 9 + 2,5 = -5,3."),
        q("Kết quả của (-2)³ : 4 là:", ["-2", "2", "-32", "-1/2"], 0, "-8 : 4 = -2."),
        q("Kết quả của 5 - 2·(-3) là:", ["11", "-1", "-11", "1"], 0, "5 + 6 = 11."),
        q("Kết quả của (1/2 + 1/3)·6 là:", ["5", "1", "4", "6"], 0, "(5/6)·6 = 5."),
        q("Tìm x biết x + 3 = 7:", ["4", "10", "-4", "-10"], 0, "x = 7 - 3 = 4."),
        q("Tìm x biết x - 5 = -2:", ["3", "-3", "7", "-7"], 0, "x = -2 + 5 = 3."),
        q("Tìm x biết x + 1/2 = 3/4:", ["1/4", "-1/4", "5/4", "-5/4"], 0, "x = 3/4 - 1/2 = 1/4."),
        q("Từ a - b = c suy ra:", ["a = c + b", "a = c - b", "a = b - c", "a = -c - b"], 0, "Chuyển -b sang vế phải thành +b."),
        q("Tìm x biết x - 0,7 = 1,3:", ["2", "0,6", "-2", "-0,6"], 0, "x = 1,3 + 0,7 = 2."),
        q("Tìm x biết -x + 4 = 9:", ["-5", "5", "13", "-13"], 0, "-x = 5 nên x = -5."),
        q("Tìm x biết x - (-1/3) = 1/6:", ["-1/6", "1/6", "1/2", "-1/2"], 0, "x = 1/6 - 1/3 = -1/6."),
        q("Kết quả của 8 : 2 · 4 là:", ["16", "1", "2", "8"], 0, "Từ trái sang phải: 4·4 = 16."),
        q("Kết quả của (-1)²·(-3) + 6 : (-2) là:", ["-6", "0", "-12", "6"], 0, "1·(-3) + (-3) = -6."),
        q("Kết quả của 3² - 2³ là:", ["1", "-1", "5", "17"], 0, "9 - 8 = 1."),
        q("Kết quả của [5 + 2·(9 - 2³)] : 7 là:", ["1", "7", "5", "2"], 0, "[5 + 2·1] : 7 = 1."),
        q("Kết quả của 10 + 36 : 2 · 3 là:", ["64", "28", "16", "54"], 0, "10 + 18·3 = 64."),
        q("Tìm x biết x - 1/2 = 1/3:", ["5/6", "1/6", "-5/6", "-1/6"], 0, "x = 1/3 + 1/2 = 5/6."),
        q("Kết quả của -1/2 + (1/4 - 3/4) là:", ["-1", "0", "1/2", "-3/2"], 0, "-1/2 - 1/2 = -1."),
        q("Kết quả của (-3)·2 + 5 là:", ["-1", "1", "11", "-11"], 0, "-6 + 5 = -1."),
        q("Tìm x biết x - 3,5 = -1,2:", ["2,3", "-4,7", "4,7", "-2,3"], 0, "x = -1,2 + 3,5 = 2,3."),
        q("Kết quả của (-2/3 + 1/2)·12 là:", ["-2", "2", "-1/6", "-14"], 0, "(-1/6)·12 = -2."),
        q("Kết quả của 2·3 - 4·(-2) + 1 là:", ["15", "-3", "9", "1"], 0, "6 + 8 + 1 = 15."),
        q("Tìm x biết 3x + 2 = 11:", ["3", "-3", "13/3", "7/3"], 0, "3x = 9 nên x = 3."),
        q("Kết quả của (1/2)² + 1/4 là:", ["1/2", "1/4", "1", "0"], 0, "1/4 + 1/4 = 1/2."),
        q("Thứ tự đúng khi thực hiện phép tính không có ngoặc là:", ["Cộng trừ → nhân chia → luỹ thừa", "Luỹ thừa → nhân chia → cộng trừ", "Nhân chia → luỹ thừa → cộng trừ", "Cộng trừ → luỹ thừa → nhân chia"], 1, "Luỹ thừa trước, nhân chia sau, cộng trừ cuối cùng."),
        q("Thứ tự đúng khi có các loại ngoặc là:", ["( ) → [ ] → { }", "{ } → [ ] → ( )", "[ ] → ( ) → { }", "Tùy ý"], 0, "Ngoặc tròn trong cùng, ngoặc vuông, ngoặc nhọn ngoài cùng."),
        q("Tìm x biết x : (-4) = 2:", ["-8", "8", "-1/2", "-6"], 0, "x = 2·(-4) = -8."),
        q("Tìm x biết x·(-3/4) = 1/2:", ["-2/3", "2/3", "-3/8", "3/8"], 0, "x = (1/2) : (-3/4) = -2/3."),
        q("Kết quả của 5 - [3 - (2 - 4)] là:", ["0", "4", "-2", "10"], 0, "5 - [3 + 2] = 0."),
        q("Kết quả của -2·3² là:", ["-18", "36", "18", "-6"], 0, "Luỹ thừa trước: -2·9 = -18."),
        q("Kết quả của (-2)²·3 là:", ["12", "-12", "6", "-6"], 0, "4·3 = 12."),
        q("Tìm x biết x : 2 = 3 - 1:", ["4", "2", "1", "6"], 0, "3 - 1 = 2 nên x = 4."),
        q("Kết quả của 1 - 2·(1/2)² là:", ["1/2", "0", "-1/2", "3/4"], 0, "1 - 2·1/4 = 1/2."),
        q("Trong biểu thức 2 + 3·(4 - 1)², thực hiện đầu tiên là:", ["Phép cộng 2 + 3", "Phép trừ 4 - 1 trong ngoặc", "Phép nhân 3·4", "Phép chia"], 1, "Ngoặc được thực hiện trước."),
    ],
    bt_co_ban=[
        bt("Tìm x biết x + 0,25 = 1/2.", ["1/4", "0,25"], "x = 1/2 - 0,25 = 1/4."),
        bt("Tìm x biết x - (-5/7) = 9/14.", ["-1/14"], "x = 9/14 - 5/7 = -1/14."),
        bt("Tìm x biết x + 7,25 = 15,75.", ["8,5"], "x = 15,75 - 7,25 = 8,5."),
        bt("Tìm x biết (-1/3) - x = 17/6.", ["-19/6"], "-x = 17/6 + 1/3 = 19/6 nên x = -19/6."),
        bt("Lan cần 2 3/4 cốc bột, đã có 1 1/2 cốc. Hỏi cần thêm bao nhiêu cốc?", ["5/4", "1 1/4", "1,25"], "11/4 - 3/2 = 5/4."),
        bt("Tính (2/3 + 1/4)·(1/2 - 1/3).", ["11/72"], "11/12 · 1/6 = 11/72."),
        bt("Tính (3/4 - 1/2)² : 1/8.", ["1/2", "0,5"], "(1/4)²·8 = 1/16·8 = 1/2."),
        bt("Tìm x biết 2x - 3 = 5.", ["4"], "2x = 8 nên x = 4."),
    ],
    bt_nang_cao=[
        nc("Bánh chưng nặng 0,8 kg gồm 0,5 kg gạo, 0,125 kg đậu xanh, 0,04 kg lá dong, còn lại là thịt. Khối lượng thịt là bao nhiêu kg?", "Lấy tổng khối lượng trừ các thành phần khác.", ["0,135", "0.135"], "0,8 - 0,5 - 0,125 - 0,04 = 0,135 kg."),
        nc("Tính hợp lí: -0,1 + 16/9 + 11,1 + (-20)/9.", "Nhóm số thập phân với nhau và phân số với nhau.", ["95/9"], "(-0,1 + 11,1) + (16/9 - 20/9) = 11 - 4/9 = 95/9."),
        nc("Tính: 17/11 - (6/5 - 16/11) + 26/5.", "Bỏ dấu ngoặc rồi nhóm các số cùng mẫu.", ["7"], "33/11 + 20/5 = 3 + 4 = 7."),
        nc("Tìm x biết (x + 1)² = 16 và x > 0.", "x + 1 là căn bậc hai của 16 và dương.", ["3"], "x + 1 = 4 nên x = 3."),
        nc("Tìm x biết x : (1/2) - 1 = 3.", "Chuyển 1 sang vế phải trước.", ["8"], "x : 1/2 = 4, nên x = 2; kiểm tra: 2 : 1/2 = 4, 4 - 1 = 3 (đúng)."),
    ],
)


CHUONG_1 = {
    "Chương I: Số hữu tỉ": {
        "Bài 1: Tập hợp các số hữu tỉ": B1,
        "Bài 2: Cộng, trừ, nhân, chia số hữu tỉ": B2,
        "Bài 3: Luỹ thừa với số mũ tự nhiên của một số hữu tỉ": B3,
        "Bài 4: Thứ tự thực hiện các phép tính. Quy tắc chuyển vế": B4,
    }
}

# ============================================================
# FILE toan_c2.py
# ============================================================
# ============================================================
# BÀI 5: LÀM QUEN VỚI SỐ THẬP PHÂN VÔ HẠN TUẦN HOÀN
# ============================================================
B5 = bai(
    ly_thuyet="""📌 1. SỐ THẬP PHÂN VÔ HẠN TUẦN HOÀN
- Số thập phân hữu hạn: có hữu hạn chữ số sau dấu phẩy (ví dụ 0,8; 1,25).
- Số thập phân vô hạn tuần hoàn: có vô hạn chữ số sau dấu phẩy, trong đó một nhóm chữ số lặp lại mãi. Nhóm lặp gọi là chu kì.
- Kí hiệu: 0,2777... = 0,2(7) (chu kì 7); -1,545454... = -1,(54) (chu kì 54).
- Mọi số hữu tỉ đều viết được dưới dạng số thập phân hữu hạn hoặc vô hạn tuần hoàn.

📌 2. LÀM TRÒN SỐ THẬP PHÂN
- Khi làm tròn đến một hàng nào đó, kết quả có độ chính xác bằng một nửa đơn vị của hàng đó.
- Bảng độ chính xác: hàng trăm 50; hàng chục 5; hàng đơn vị 0,5; hàng phần mười 0,05; hàng phần trăm 0,005; hàng phần nghìn 0,0005.
- Quy tắc: chữ số sau hàng làm tròn nhỏ hơn 5 thì giữ nguyên; từ 5 trở lên thì cộng thêm 1 vào hàng làm tròn.

📌 3. MẸO CHUYỂN PHÂN SỐ THÀNH SỐ THẬP PHÂN
- Phân số tối giản với mẫu dương mà mẫu không có ước nguyên tố khác 2 và 5 thì viết được thành số thập phân hữu hạn.
- Các trường hợp khác (có ước nguyên tố khác 2 và 5) cho số thập phân vô hạn tuần hoàn.
- 0,(1) = 1/9; 0,(01) = 1/99; 0,(9) = 1.
""",
    vi_du="""Ví dụ 1: 7/22 = 0,31818... = 0,3(18) là số thập phân vô hạn tuần hoàn với chu kì 18.
Ta có -7/22 = -0,3(18).

Ví dụ 2: Làm tròn 12 591,27:
a) với độ chính xác 50: 12 591,27 ≈ 12 600 (làm tròn đến hàng trăm);
b) với độ chính xác 0,05: 12 591,27 ≈ 12 591,3 (làm tròn đến hàng phần mười).""",
    cau_hoi=[
        q("Số 4/5 viết dưới dạng số thập phân là:", ["0,8", "0,(8)", "0,4", "0,45"], 0, "4 : 5 = 0,8 (hữu hạn)."),
        q("Số 5/18 viết dưới dạng số thập phân là:", ["0,2(7)", "0,(27)", "0,27", "0,5(18)"], 0, "5 : 18 = 0,2777... = 0,2(7)."),
        q("Chu kì của số thập phân 0,3(18) là:", ["18", "3", "81", "8"], 0, "Nhóm lặp lại là 18."),
        q("Số 1/9 viết dưới dạng số thập phân là:", ["0,(1)", "0,1", "0,(9)", "0,11"], 0, "1/9 = 0,111... = 0,(1)."),
        q("Số 7/22 viết dưới dạng số thập phân là:", ["0,3(18)", "0,31(8)", "0,(318)", "0,318"], 0, "7 : 22 = 0,31818... = 0,3(18)."),
        q("Số -17/11 viết dưới dạng số thập phân là:", ["-1,(54)", "-1,(45)", "-1,5454", "-1,(5)"], 0, "17 : 11 = 1,545454... = 1,(54)."),
        q("Số 1/4 là số thập phân:", ["Hữu hạn", "Vô hạn tuần hoàn", "Vô hạn không tuần hoàn", "Không xác định"], 0, "1/4 = 0,25."),
        q("Số 2/11 là số thập phân:", ["Hữu hạn", "Vô hạn tuần hoàn", "Vô hạn không tuần hoàn", "Không xác định"], 1, "2/11 = 0,(18)."),
        q("Số 0,(9) bằng:", ["0,9", "1", "0", "9"], 1, "0,(9) = 1."),
        q("Số 1/3 viết dưới dạng số thập phân là:", ["0,(3)", "0,3", "0,(31)", "0,4"], 0, "1/3 = 0,333... = 0,(3)."),
        q("Số 0,(17) bằng phân số nào?", ["17/99", "17/100", "1/17", "17/9"], 0, "0,(17) = 17/99."),
        q("Số 0,(01) bằng phân số nào?", ["1/99", "1/100", "1/9", "0,01"], 0, "0,(01) = 1/99."),
        q("Làm tròn 3,14159 đến hàng phần trăm được:", ["3,1", "3,14", "3,15", "3,2"], 1, "Chữ số sau hàng phần trăm là 1 < 5 nên giữ 3,14."),
        q("Làm tròn 46,333... đến hàng đơn vị được:", ["46", "47", "46,3", "50"], 0, "Chữ số sau hàng đơn vị là 3 < 5."),
        q("Làm tròn -1,27(534) đến hàng phần trăm được:", ["-1,27", "-1,28", "-1,3", "-1,26"], 1, "Chữ số sau hàng phần trăm là 5 nên làm tròn lên: -1,28."),
        q("Làm tròn 12 591,27 với độ chính xác 50 được:", ["12 600", "12 500", "12 591", "13 000"], 0, "Làm tròn đến hàng trăm."),
        q("Làm tròn 12 591,27 với độ chính xác 0,05 được:", ["12 591,3", "12 591,2", "12 591", "12 591,27"], 0, "Làm tròn đến hàng phần mười."),
        q("Độ chính xác khi làm tròn đến hàng chục là:", ["5", "10", "0,5", "50"], 0, "Bằng nửa đơn vị hàng chục: 5."),
        q("Độ chính xác khi làm tròn đến hàng phần mười là:", ["0,05", "0,5", "0,005", "0,1"], 0, "Bằng nửa đơn vị hàng phần mười: 0,05."),
        q("Số nào là số thập phân hữu hạn?", ["0,(3)", "0,125", "2/3", "1/7"], 1, "0,125 = 1/8, có hữu hạn chữ số."),
        q("Số nào viết được dưới dạng số thập phân vô hạn tuần hoàn?", ["1/4", "1/6", "1/8", "3/5"], 1, "1/6 = 0,1(6)."),
        q("Viết 0,(2) dưới dạng phân số là:", ["2/9", "2/10", "2/99", "1/2"], 0, "0,(2) = 2/9."),
        q("Số 0,(45) bằng phân số nào?", ["5/11", "45/100", "45/99", "4/9"], 0, "0,(45) = 45/99 = 5/11."),
        q("Làm tròn 3,4567 đến hàng phần nghìn được:", ["3,456", "3,457", "3,46", "3,5"], 1, "Chữ số sau hàng phần nghìn là 7 ≥ 5 nên làm tròn lên: 3,457."),
        q("Làm tròn 47 đến hàng chục được:", ["40", "50", "47", "45"], 1, "47 gần 50 hơn."),
        q("Chu kì của số 0,2(7) là:", ["7", "2", "27", "72"], 0, "Nhóm lặp lại là 7."),
        q("Trong các đẳng thức sau, đẳng thức đúng là:", ["0,(5) = 5/9", "0,(5) = 1/2", "0,(5) = 5/10", "0,(5) = 1/5"], 0, "0,(5) = 5/9."),
        q("Làm tròn 1/7 đến hàng phần trăm được:", ["0,14", "0,15", "0,142", "0,1"], 0, "1/7 = 0,142857..., làm tròn đến 0,14."),
        q("Mọi số hữu tỉ viết được dưới dạng:", ["Số thập phân hữu hạn hoặc vô hạn tuần hoàn", "Chỉ số thập phân hữu hạn", "Chỉ số thập phân vô hạn", "Số vô hạn không tuần hoàn"], 0, "Đây là tính chất của số hữu tỉ."),
        q("Số nào là số thập phân vô hạn tuần hoàn?", ["0,15", "0,1(23)", "1,25", "2,75"], 1, "0,1(23) có chu kì 23 lặp vô hạn."),
        q("Số 2 viết dưới dạng số thập phân là:", ["2,0", "2,(1)", "2,(2)", "2,01"], 0, "2 = 2,0."),
        q("Số -1,(54) viết dưới dạng phân số là:", ["-17/11", "-54/99", "-11/17", "-6/11"], 0, "-1,(54) = -(1 + 54/99) = -17/11."),
        q("Làm tròn 0,(6) đến hàng phần mười được:", ["0,6", "0,7", "0,67", "0,66"], 1, "0,666... làm tròn đến hàng phần mười: 0,7."),
        q("Làm tròn 3,(3) đến hàng đơn vị được:", ["3", "4", "3,3", "0"], 0, "3,333... làm tròn đến đơn vị: 3."),
    ],
    bt_co_ban=[
        bt("Viết 5/18 dưới dạng số thập phân vô hạn tuần hoàn và chỉ rõ chu kì.", ["0,2(7)"], "Chu kì là 7."),
        bt("Viết 7/22 dưới dạng số thập phân.", ["0,3(18)"], "Chu kì là 18."),
        bt("Viết -17/11 dưới dạng số thập phân.", ["-1,(54)"], "Chu kì là 54."),
        bt("Viết 1/4 và 2/11 dưới dạng số thập phân.", ["0,25; 0,(18)"], "1/4 hữu hạn; 2/11 vô hạn tuần hoàn."),
        bt("Làm tròn 3,14159 đến chữ số thập phân thứ ba.", ["3,142"], "Chữ số thứ tư là 5 nên làm tròn lên."),
        bt("Tìm chữ số thập phân thứ năm của 3,2(31).", ["1"], "3,2(31) = 3,2313131...; chữ số thứ năm là 1."),
        bt("Làm tròn 12 591,27 với độ chính xác 50.", ["12 600"], "Làm tròn đến hàng trăm."),
        bt("Làm tròn số 3,14159 với độ chính xác 0,005.", ["3,14"], "Làm tròn đến hàng phần trăm."),
        bt("Tính √100.", ["10"], "10² = 100."),
        bt("Tính √16 và √81.", ["4; 9"], "4² = 16; 9² = 81."),
        bt("Tính √1024 bằng máy tính cầm tay.", ["32"], "32² = 1024."),
        bt("Tính √2 làm tròn đến chữ số thập phân thứ chín.", ["1,414213562"], "√2 = 1,4142135623..."),
        bt("Tính √91 làm tròn đến chữ số thập phân thứ tư.", ["9,5394"], "√91 ≈ 9,5393920..."),
    ],
    bt_nang_cao=[
        nc("Chứng minh 0,(9) = 1.", "Đặt x = 0,(9), tính 10x - x.", ["1"], "10x = 9,(9); 10x - x = 9; x = 1."),
        nc("Viết 0,1(6) dưới dạng phân số tối giản.", "Đặt x = 0,1(6); nhân 10 rồi nhân 10 tiếp.", ["1/6"], "100x - 10x = 16 - 1 = 15 nên x = 15/90 = 1/6."),
        nc("Viết 0,(37) dưới dạng phân số.", "Chu kì có 2 chữ số nên mẫu là 99.", ["37/99"], "0,(37) = 37/99."),
        nc("Ước lượng kết quả của phép tính 31,(81) · 4,9 bằng cách làm tròn 31,(81) đến hàng đơn vị và 4,9 đến hàng đơn vị.", "Làm tròn từng thừa số.", ["160"], "32 · 5 = 160."),
        nc("Chu kì của số thập phân vô hạn tuần hoàn viết được từ 2/7 có bao nhiêu chữ số?", "Thực hiện phép chia 2 : 7.", ["6"], "2/7 = 0,(285714): chu kì có 6 chữ số."),
        nc("Số 0,1010010001... (viết liên tiếp các số 10, 100, 1000,...) có phải số hữu tỉ không?", "Xem xét có chu kì không.", ["Không"], "Không có chu kì lặp lại nên không phải số hữu tỉ."),
    ],
)


# ============================================================
# BÀI 6: SỐ VÔ TỈ. CĂN BẬC HAI SỐ HỌC
# ============================================================
B6 = bai(
    ly_thuyet="""📌 1. SỐ VÔ TỈ
- Số vô tỉ là số viết được dưới dạng số thập phân vô hạn không tuần hoàn.
- Tập hợp các số vô tỉ kí hiệu là 𝕀.
- Ví dụ: π = 3,14159265358...; √2 = 1,4142135623...; số -0,10100100010000...

📌 2. CĂN BẬC HAI SỐ HỌC
- Căn bậc hai số học của số a không âm, kí hiệu √a, là số x không âm sao cho x² = a.
- √0 = 0; √1 = 1; √4 = 2; √9 = 3; √16 = 4; √81 = 9; √100 = 10.
- Với a ≥ 0: (√a)² = a và √(a²) = a.
- Căn bậc hai số học của số tự nhiên không chính phương là số vô tỉ (ví dụ √2, √3, √5).

📌 3. TÍNH CĂN BẬC HAI BẰNG MÁY TÍNH CẦM TAY
- Dùng phím √ để tính; kết quả trên máy chỉ hiển thị hữu hạn chữ số nên thường là giá trị gần đúng.

📌 4. TẬP HỢP SỐ VÔ TỈ VÀ SỐ HỮU TỈ
- Số hữu tỉ và số vô tỉ không có phần chung.
""",
    vi_du="""Ví dụ 2: Tính √100 = 10; √191² = 191; √21,5² = 21,5.

Ví dụ 3: Dùng máy tính cầm tay tính √91 ≈ 9,539392014.
a) Làm tròn đến chữ số thập phân thứ tư: √91 ≈ 9,5394.
b) Với độ chính xác 0,05: √91 ≈ 9,5.""",
    cau_hoi=[
        q("Số vô tỉ là số viết được dưới dạng:", ["Số thập phân hữu hạn", "Số thập phân vô hạn tuần hoàn", "Số thập phân vô hạn không tuần hoàn", "Phân số"], 2, "Đây là định nghĩa số vô tỉ."),
        q("Số √2 là:", ["Số hữu tỉ", "Số vô tỉ", "Số nguyên", "Số tự nhiên"], 1, "√2 là số vô tỉ."),
        q("Số nào là số vô tỉ?", ["0,(3)", "√4", "√5", "-0,75"], 2, "√5 không viết được dưới dạng phân số."),
        q("√4 bằng:", ["2", "-2", "4", "±2"], 0, "Căn bậc hai số học của 4 là 2."),
        q("√81 bằng:", ["9", "-9", "81", "±9"], 0, "Căn bậc hai số học của 81 là 9."),
        q("√0 bằng:", ["0", "1", "Không xác định", "-0"], 0, "√0 = 0."),
        q("√(21,5²) bằng:", ["21,5", "-21,5", "±21,5", "43"], 0, "Căn bậc hai số học của bình phương một số không âm là chính số đó."),
        q("Căn bậc hai số học của 49 là:", ["7", "-7", "±7", "49"], 0, "√49 = 7."),
        q("√16 + √9 bằng:", ["7", "5", "25", "1"], 0, "4 + 3 = 7."),
        q("Căn bậc hai số học của một số a không âm là số x sao cho:", ["x ≥ 0 và x² = a", "x² = a, x tùy ý", "x = a²", "x ≤ 0 và x² = a"], 0, "Định nghĩa căn bậc hai số học."),
        q("√(-4):", ["Không xác định trong tập số không âm", "Bằng 2", "Bằng -2", "Bằng 4"], 0, "Căn bậc hai số học chỉ xét với số không âm."),
        q("Trong các số sau, số vô tỉ là:", ["π", "0,25", "2/3", "-7"], 0, "π là số vô tỉ."),
        q("Số thập phân -0,10100100010000... (sau dấu phẩy viết liên tiếp 10; 100; 1000;...) là:", ["Số vô tỉ", "Số hữu tỉ", "Số thập phân vô hạn tuần hoàn", "Số thập phân hữu hạn"], 0, "Không có chu kì nên là số vô tỉ."),
        q("Số 0,(1) là:", ["Số vô tỉ", "Số hữu tỉ", "Số nguyên", "Số tự nhiên"], 1, "0,(1) = 1/9 là số hữu tỉ."),
        q("Số nào là số thực nhưng không phải số vô tỉ?", ["√2", "π", "√9", "√5"], 2, "√9 = 3 là số hữu tỉ."),
        q("√1024 bằng:", ["32", "64", "16", "1024"], 0, "32² = 1024."),
        q("√2025 bằng:", ["45", "35", "55", "405"], 0, "45² = 2025."),
        q("Căn bậc hai của 100 là:", ["10", "-10", "50", "1000"], 0, "Căn bậc hai số học của 100 là 10."),
        q("Trong các số √4; √7; √9; √25, số vô tỉ là:", ["√4", "√7", "√9", "√25"], 1, "√4 = 2; √9 = 3; √25 = 5 đều hữu tỉ; √7 là vô tỉ."),
        q("Căn bậc hai số học của 0,25 là:", ["0,5", "0,05", "0,125", "0,25"], 0, "0,5² = 0,25."),
        q("Căn bậc hai số học của 1 là:", ["1", "0", "-1", "2"], 0, "1² = 1."),
        q("Hình vuông có diện tích 2 dm² có cạnh là:", ["√2 dm", "2 dm", "1 dm", "4 dm"], 0, "Cạnh² = 2 nên cạnh = √2 dm."),
        q("Số π làm tròn đến hàng phần trăm là:", ["3,14", "3,1", "3,15", "3,141"], 0, "π ≈ 3,14159."),
        q("√3 làm tròn đến chữ số thập phân thứ ba là:", ["1,73", "1,732", "1,731", "1,7321"], 1, "√3 ≈ 1,7320508 → 1,732."),
        q("Tập hợp số vô tỉ được kí hiệu là:", ["ℚ", "ℤ", "𝕀", "ℕ"], 2, "𝕀 là kí hiệu tập số vô tỉ."),
        q("√(a²) với a > 0 bằng:", ["a", "-a", "a²", "√a"], 0, "Vì a > 0 nên √(a²) = a."),
        q("Khẳng định đúng là:", ["√16 = 4", "√16 = -4", "√16 = ±4", "√16 = 16"], 0, "Căn bậc hai số học của 16 là 4."),
        q("Số 0,123456789101112... (viết liên tiếp các số tự nhiên) là:", ["Số vô tỉ", "Số hữu tỉ", "Số nguyên", "Số tự nhiên"], 0, "Không có chu kì nên là số vô tỉ."),
        q("√12 làm tròn đến chữ số thập phân thứ hai là:", ["3,46", "3,47", "3,4", "3,5"], 0, "√12 ≈ 3,4641."),
        q("Tổng √4 + √9 + √25 bằng:", ["10", "8", "12", "38"], 0, "2 + 3 + 5 = 10."),
        q("Tích √9 · √16 bằng:", ["12", "25", "7", "144"], 0, "3 · 4 = 12."),
        q("Nếu √x = 3 thì x bằng:", ["3", "9", "6", "√3"], 1, "3² = 9."),
        q("Hình vuông có diện tích 144 m² có chu vi là:", ["48 m", "24 m", "72 m", "12 m"], 0, "Cạnh = 12 m; chu vi = 4·12 = 48 m."),
        q("Số vô tỉ nằm giữa 1 và 2 là:", ["√2", "√4", "2", "1,5"], 0, "1 < √2 < 2."),
        q("Số √5 nằm giữa hai số nguyên liên tiếp nào?", ["1 và 2", "2 và 3", "3 và 4", "0 và 1"], 1, "2 < √5 < 3."),
    ],
    bt_co_ban=[
        bt("Tính √16.", ["4"], "4² = 16."),
        bt("Tính √81.", ["9"], "9² = 81."),
        bt("Tính √2021².", ["2021"], "Căn bậc hai của bình phương số không âm là chính số đó."),
        bt("Sàn thi đấu hình vuông có diện tích 144 m². Tính cạnh của sàn.", ["12"], "√144 = 12 m."),
        bt("Tính √1024 bằng máy tính cầm tay.", ["32"], "Kết quả chính xác."),
        bt("Tính √91 làm tròn đến chữ số thập phân thứ tư.", ["9,5394"], "√91 ≈ 9,539392..."),
        bt("Tính √15 với độ chính xác 0,005.", ["3,87"], "√15 ≈ 3,87298... ; làm tròn đến hàng phần trăm."),
        bt("Tính √2,56.", ["1,6"], "1,6² = 2,56."),
        bt("Tính √17256 với độ chính xác 0,005.", ["131,36"], "√17256 ≈ 131,3646..."),
        bt("Tính √793 881.", ["891"], "891² = 793 881."),
        bt("Hình vuông có diện tích 81 dm². Tính cạnh.", ["9"], "√81 = 9 dm."),
    ],
    bt_nang_cao=[
        nc("Biết 153² = 23 409. Tính √23 409.", "Áp dụng định nghĩa căn bậc hai số học.", ["153"], "√23 409 = 153."),
        nc("Tính √129 600 bằng cách phân tích ra thừa số nguyên tố.", "129 600 = 360².", ["360"], "129 600 = 2⁶·3⁴·5² = (2³·3²·5)² = 360², nên √129 600 = 360."),
        nc("Diện tích một hình vuông là 1 ha = 10 000 m². Tính cạnh của hình vuông đó (đơn vị m).", "Cạnh = √diện tích.", ["100"], "√10 000 = 100 m."),
        nc("Chứng minh √2 là số vô tỉ.", "Giả sử √2 = a/b tối giản.", ["Số vô tỉ", "vô tỉ"], "Nếu √2 = a/b thì a² = 2b², suy ra a chẵn, b chẵn, mâu thuẫn tối giản."),
        nc("Số 0,1010010001... có phải số vô tỉ không?", "Số thập phân không tuần hoàn.", ["Có"], "Không có chu kì, nên là số vô tỉ."),
    ],
)


# ============================================================
# BÀI 7: TẬP HỢP CÁC SỐ THỰC
# ============================================================
B7 = bai(
    ly_thuyet="""📌 1. SỐ THỰC
- Số hữu tỉ và số vô tỉ gọi chung là số thực.
- Tập hợp các số thực kí hiệu là ℝ.
- Mỗi số thực a có một số đối, kí hiệu -a.

📌 2. TRỤC SỐ THỰC
- Mỗi số thực được biểu diễn bởi đúng một điểm trên trục số; ngược lại mỗi điểm trên trục số biểu diễn đúng một số thực. Trục số khi đó gọi là trục số thực.

📌 3. SO SÁNH SỐ THỰC
- Với hai số thực a, b bất kì: a = b, a < b hoặc a > b.
- Tính chất bắc cầu: nếu a < b và b < c thì a < c.
- Trên trục số, nếu a < b thì điểm a nằm trước điểm b.
- Với 0 < a < b thì √a < √b.

📌 4. GIÁ TRỊ TUYỆT ĐỐI
- |a| là khoảng cách từ điểm a đến gốc O.
- |a| = a nếu a > 0; |a| = -a nếu a < 0; |0| = 0.
- Giá trị tuyệt đối của mọi số thực đều không âm.
""",
    vi_du="""Ví dụ: |−2,3| = 2,3; |√8| = √8; |−11| = 11; |7/5| = 7/5.

So sánh: √2 ≈ 1,414 > 1,41 nên −√2 < −1,41.

Ví dụ: Nếu 1 < x < 3 thì điểm biểu diễn x nằm giữa hai điểm 1 và 3 trên trục số.""",
    cau_hoi=[
        q("Tập số thực gồm:", ["Chỉ số hữu tỉ", "Chỉ số vô tỉ", "Số hữu tỉ và số vô tỉ", "Số nguyên và số tự nhiên"], 2, "ℝ = ℚ ∪ 𝕀."),
        q("Tập hợp các số thực được kí hiệu là:", ["ℚ", "ℝ", "𝕀", "ℤ"], 1, "ℝ là kí hiệu tập số thực."),
        q("Số đối của √2 là:", ["-√2", "√2", "1/√2", "-2"], 0, "Số đối của √2 là -√2."),
        q("Số đối của -0,(3) là:", ["0,(3)", "-0,(3)", "0,3", "-3"], 0, "Số đối của -0,(3) là 0,(3)."),
        q("|−2,3| bằng:", ["2,3", "−2,3", "0", "4,6"], 0, "Giá trị tuyệt đối luôn không âm."),
        q("|−√8| bằng:", ["√8", "−√8", "8", "0"], 0, "|−√8| = √8."),
        q("|0| bằng:", ["0", "1", "-0", "Không xác định"], 0, "Giá trị tuyệt đối của 0 bằng 0."),
        q("|−5,1| bằng:", ["5,1", "-5,1", "0", "10"], 0, "|−5,1| = 5,1."),
        q("Với a > 0, |a| bằng:", ["a", "-a", "0", "a²"], 0, "Giá trị tuyệt đối của số dương là chính nó."),
        q("Với a < 0, |a| bằng:", ["-a", "a", "0", "a²"], 0, "Giá trị tuyệt đối của số âm là số đối của nó."),
        q("Giá trị tuyệt đối của số a là:", ["Khoảng cách từ a đến O", "Số đối của a", "Bình phương của a", "Căn bậc ba của a"], 0, "Đây là định nghĩa."),
        q("Số nào lớn hơn?", ["-1 < -√2", "-1 > -√2", "-1 = -√2", "Không so sánh được"], 1, "-1 ≈ -1,000 > -1,414 ≈ -√2."),
        q("So sánh √2 và 1,41:", ["√2 < 1,41", "√2 > 1,41", "√2 = 1,41", "Không so sánh được"], 1, "√2 = 1,4142... > 1,41."),
        q("Số thực x thỏa mãn |x| = 2,5 là:", ["x = 2,5", "x = −2,5", "x = ±2,5", "x = 0"], 2, "Hai số đối nhau có cùng giá trị tuyệt đối."),
        q("So sánh 0,(3) và 1/3:", ["Bằng nhau", "0,(3) lớn hơn", "1/3 lớn hơn", "Không so sánh được"], 0, "0,(3) = 1/3."),
        q("Trên trục số thực, điểm √2 nằm ở đâu so với gốc O?", ["Bên phải O", "Bên trái O", "Trùng O", "Không xác định"], 0, "√2 > 0."),
        q("Trong các số 2,5; √6; −√3; 0, số dương là:", ["√6", "−√3", "0", "−2,5"], 0, "√6 > 0."),
        q("Số thực nào lớn nhất trong 3,14; π; 3,15; √9?", ["3,14", "π", "3,15", "√9"], 2, "π ≈ 3,14159 < 3,15; √9 = 3."),
        q("Hai số đối nhau có giá trị tuyệt đối:", ["Bằng nhau", "Đối nhau", "Bằng 0", "Khác nhau"], 0, "|a| = |−a|."),
        q("Số nào là số thực âm?", ["−√2", "√2", "0", "π"], 0, "−√2 < 0."),
        q("Với 0 < a < b thì:", ["√a < √b", "√a > √b", "√a = √b", "Không so sánh được"], 0, "Căn bậc hai là hàm đồng biến với số không âm."),
        q("So sánh √5 và 2,3:", ["√5 < 2,3", "√5 > 2,3", "√5 = 2,3", "Không so sánh được"], 0, "√5 ≈ 2,236 < 2,3."),
        q("Sắp xếp −3; −√8; 2; √5 theo thứ tự tăng dần:", ["−√8; −3; 2; √5", "−3; −√8; 2; √5", "2; √5; −3; −√8", "−3; −√8; √5; 2"], 1, "−3 < −√8 ≈ −2,83 < 2 < √5 ≈ 2,24."),
        q("|−3| + |2| bằng:", ["5", "1", "−5", "−1"], 0, "3 + 2 = 5."),
        q("|−1,5| · 2 bằng:", ["3", "−3", "1,5", "2"], 0, "1,5 · 2 = 3."),
        q("Số thực x thỏa mãn |x| = 0 là:", ["0", "1", "−1", "Không có"], 0, "Chỉ có x = 0."),
        q("|x| = 4,1 khi và chỉ khi:", ["x = 4,1", "x = −4,1", "x = ±4,1", "x = 16,81"], 2, "Hai số đối có cùng giá trị tuyệt đối."),
        q("Trên trục số thực, điểm √5 nằm giữa hai điểm nào?", ["2 và 3", "1 và 2", "3 và 4", "0 và 1"], 0, "2 < √5 < 3."),
        q("Trong các số −1; −√2; −1,5; 0, số nhỏ nhất là:", ["−1", "−√2", "−1,5", "0"], 2, "−1,5 < −√2 ≈ −1,414 < −1 < 0."),
        q("Điểm biểu diễn a và −a đối xứng qua:", ["O", "a", "−a", "1"], 0, "Hai số đối cách đều gốc O."),
        q("Khẳng định |a| ≥ 0 với mọi số thực a là:", ["Đúng", "Sai", "Chỉ đúng khi a > 0", "Chỉ đúng khi a < 0"], 0, "Giá trị tuyệt đối không âm."),
        q("Giá trị tuyệt đối của 0 là:", ["0", "1", "Không tồn tại", "-0"], 0, "|0| = 0."),
        q("Số vô tỉ âm trong các số sau là:", ["−√2", "−0,5", "−1/2", "−√4"], 0, "−√2 là số vô tỉ âm; −√4 = −2 hữu tỉ."),
        q("|−√8| bằng:", ["√8", "−√8", "8", "−8"], 0, "Giá trị tuyệt đối không âm."),
        q("Số nào KHÔNG thuộc khoảng −1 < x < 2?", ["−1,5", "0", "1,5", "2,5"], 3, "2,5 > 2 nên không thuộc khoảng."),
        q("Số đối của |−3| là:", ["−3", "3", "0", "−1/3"], 0, "|−3| = 3, số đối là −3."),
    ],
    bt_co_ban=[
        bt("Cách viết nào đúng: √2 ∈ ℚ; π ∈ 𝕀; 15 ∈ ℝ? Trả lời đúng hoặc sai cho từng khẳng định.", ["sai; đúng; đúng"], "√2 là số vô tỉ nên không thuộc ℚ."),
        bt("Viết số đối của 5,08(299).", ["-5,08(299)"], "Số đối là −5,08(299)."),
        bt("Viết số đối của −√5.", ["√5"], "Số đối của −√5 là √5."),
        bt("Tính |−2,3|.", ["2,3"], "Giá trị tuyệt đối của −2,3."),
        bt("Tính |7/5|.", ["7/5", "1,4"], "7/5 > 0."),
        bt("Tính |−11|.", ["11"], "|−11| = 11."),
        bt("Tính |−√8|.", ["√8"], "Giá trị tuyệt đối không âm."),
        bt("Tìm các số thực x thỏa mãn |x| = 2,5.", ["2,5; -2,5", "±2,5"], "x = ±2,5."),
        bt("Trong tập A = {7,1; −2,(61); 0; 5,14; 4/7; √15; −√81}, liệt kê các số hữu tỉ.", ["7,1; -2,(61); 0; 5,14; 4/7; -√81"], "−√81 = −9 là số hữu tỉ; √15 là số vô tỉ."),
        bt("Liệt kê các phần tử của tập {x ∈ ℤ : |x| < 5}.", ["-4, -3, -2, -1, 0, 1, 2, 3, 4"], "Các số nguyên có |x| ≤ 4."),
    ],
    bt_nang_cao=[
        nc("Tìm số thực x > 0 thỏa mãn |x| = 2,5.", "Chọn nghiệm dương.", ["2,5"], "x = 2,5."),
        nc("Tính A = |−3,5| + |−5,1| − |−2|.", "Tính từng giá trị tuyệt đối.", ["6,6"], "3,5 + 5,1 − 2 = 6,6."),
        nc("Điền dấu thích hợp: −√10 ... −3.", "So sánh √10 với 3.", ["<"], "√10 ≈ 3,16 > 3 nên −√10 < −3."),
        nc("Chứng minh nếu |a| = |b| thì a = b hoặc a = −b.", "Xét hai trường hợp.", ["a = b hoặc a = -b"], "Hai số có cùng giá trị tuyệt đối thì bằng nhau hoặc đối nhau."),
        nc("Có bao nhiêu số thực x thỏa mãn |x| < 0?", "Giá trị tuyệt đối không âm.", ["0"], "Không có số thực nào."),
    ],
)


CHUONG_2 = {
    "Chương II: Số thực": {
        "Bài 5: Làm quen với số thập phân vô hạn tuần hoàn": B5,
        "Bài 6: Số vô tỉ. Căn bậc hai số học": B6,
        "Bài 7: Tập hợp các số thực": B7,
    }
}

# ============================================================
# FILE toan_c3.py
# ============================================================
# ============================================================
# BÀI 8: GÓC Ở VỊ TRÍ ĐẶC BIỆT. TIA PHÂN GIÁC CỦA MỘT GÓC
# ============================================================
B8 = bai(
    ly_thuyet="""📌 1. HAI GÓC KỀ BÙ
- Hai góc có một cạnh chung, hai cạnh còn lại là hai tia đối nhau gọi là hai góc kề bù.
- Tính chất: hai góc kề bù có tổng số đo bằng 180°.

📌 2. HAI GÓC ĐỐI ĐỈNH
- Hai góc đối đỉnh là hai góc mà mỗi cạnh của góc này là tia đối của một cạnh của góc kia.
- Tính chất: hai góc đối đỉnh thì bằng nhau.

📌 3. HAI ĐƯỜNG THẲNG VUÔNG GÓC
- Hai đường thẳng cắt nhau tạo thành một góc vuông thì gọi là hai đường thẳng vuông góc. Kí hiệu xx' ⊥ yy'.

📌 4. TIA PHÂN GIÁC CỦA MỘT GÓC
- Tia nằm giữa hai cạnh của một góc và tạo với hai cạnh ấy hai góc bằng nhau gọi là tia phân giác của góc đó.
- Nếu Oz là tia phân giác của góc xOy thì xOz = zOy = (1/2)·xOy.
""",
    vi_du="""Ví dụ 1: Hai đường thẳng xx' và yy' cắt nhau tại O, góc xOy = 60°.
Góc x'Oy' = xOy = 60° (đối đỉnh); góc x'Oy = 180° − 60° = 120° (kề bù).

Ví dụ 2: Góc mOn = 70°, tia Ot là tia phân giác. Khi đó mOt = tOn = 70° : 2 = 35°.""",
    cau_hoi=[
        q("Hai góc kề bù có tổng số đo bằng:", ["90°", "180°", "360°", "120°"], 1, "Đây là tính chất hai góc kề bù."),
        q("Góc kề bù với góc 60° có số đo:", ["30°", "120°", "60°", "300°"], 1, "180° − 60° = 120°."),
        q("Hai góc đối đỉnh thì:", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Khác nhau"], 0, "Tính chất hai góc đối đỉnh."),
        q("Góc đối đỉnh với góc 35° có số đo:", ["35°", "145°", "55°", "325°"], 0, "Hai góc đối đỉnh bằng nhau."),
        q("Trong hình 3.4, góc mOt bù với góc 60° nên có số đo:", ["60°", "120°", "30°", "180°"], 1, "180° − 60° = 120°."),
        q("Tia Oz là tia phân giác của góc xOy khi:", ["xOz = zOy", "xOz = 2·zOy", "xOz + zOy = 180°", "xOz = xOy"], 0, "Tia phân giác chia góc thành hai góc bằng nhau."),
        q("Góc 70° có tia phân giác tạo với mỗi cạnh một góc:", ["35°", "70°", "140°", "17°"], 0, "70° : 2 = 35°."),
        q("Am là tia phân giác của góc xAy, góc xAm = 65°. Góc xAy bằng:", ["65°", "130°", "32,5°", "115°"], 1, "xAy = 2 · 65° = 130°."),
        q("Góc xOy = 68°, tia Oz là tia phân giác. Góc xOz bằng:", ["34°", "68°", "136°", "22°"], 0, "68° : 2 = 34°."),
        q("Hai góc kề bù, một góc 110° thì góc còn lại bằng:", ["70°", "110°", "250°", "90°"], 0, "180° − 110° = 70°."),
        q("Hai đường thẳng xx' và yy' cắt nhau tại O, góc xOy = 60°. Góc x'Oy' bằng:", ["60°", "120°", "30°", "90°"], 0, "Hai góc đối đỉnh bằng nhau."),
        q("Hai đường thẳng xx' và yy' cắt nhau tại O, góc xOy = 60°. Góc x'Oy bằng:", ["60°", "120°", "90°", "30°"], 1, "Góc x'Oy kề bù với góc xOy."),
        q("Hai đường thẳng vuông góc tạo thành góc có số đo:", ["45°", "90°", "180°", "60°"], 1, "Góc vuông bằng 90°."),
        q("Hai góc kề bù, một góc vuông thì góc kia bằng:", ["90°", "45°", "180°", "0°"], 0, "180° − 90° = 90°."),
        q("Hai cạnh còn lại của hai góc kề bù là:", ["Hai tia đối nhau", "Hai tia trùng nhau", "Hai tia vuông góc", "Hai tia bất kì"], 0, "Đây là định nghĩa hai góc kề bù."),
        q("Điểm M nằm trong góc xOy thì:", ["xOM + MOy = xOy", "xOM = MOy", "xOM · MOy = xOy", "xOM − MOy = xOy"], 0, "Tia OM nằm giữa hai cạnh của góc."),
        q("Tia phân giác của góc 80° tạo với một cạnh góc bằng:", ["40°", "80°", "160°", "20°"], 0, "80° : 2 = 40°."),
        q("Góc kề bù với góc 40° có số đo:", ["140°", "40°", "50°", "220°"], 0, "180° − 40° = 140°."),
        q("Tia phân giác của góc bẹt (180°) tạo với mỗi cạnh một góc bằng:", ["45°", "90°", "180°", "60°"], 1, "180° : 2 = 90°."),
        q("Hai góc kề bù, một góc nhọn thì góc kia là:", ["Góc tù", "Góc nhọn", "Góc vuông", "Góc bẹt"], 0, "180° − góc nhọn > 90°."),
        q("Hai đường thẳng cắt nhau tạo thành số cặp góc đối đỉnh là:", ["2", "4", "1", "6"], 0, "Có hai cặp góc đối đỉnh."),
        q("Góc 45° và góc đối đỉnh của nó có số đo:", ["45° và 45°", "45° và 135°", "90° và 90°", "180° và 180°"], 0, "Hai góc đối đỉnh bằng nhau."),
        q("Oz là tia phân giác của góc xOy = 100°. Góc xOz bằng:", ["50°", "100°", "200°", "25°"], 0, "100° : 2 = 50°."),
        q("Hai góc có tổng số đo bằng 180° và có một cạnh chung thì là:", ["Kề bù", "Đối đỉnh", "Bằng nhau", "Phụ nhau"], 0, "Đây là hai góc kề bù."),
        q("Hai góc kề bù, một góc gấp 3 lần góc kia. Góc nhỏ bằng:", ["45°", "60°", "30°", "90°"], 0, "x + 3x = 180° nên x = 45°."),
        q("Hai góc đối đỉnh đều bằng 75°. Góc kề bù với mỗi góc đó có số đo:", ["105°", "75°", "15°", "180°"], 0, "180° − 75° = 105°."),
        q("Góc bẹt có số đo bằng:", ["180°", "90°", "360°", "0°"], 0, "Góc bẹt là góc có số đo 180°."),
        q("Tia phân giác của góc 130° tạo với mỗi cạnh góc một góc bằng:", ["65°", "130°", "50°", "260°"], 0, "130° : 2 = 65°."),
        q("Hai đường thẳng vuông góc thì các góc tạo thành đều bằng:", ["90°", "45°", "180°", "60°"], 0, "Mỗi góc tạo thành là góc vuông."),
        q("Tổng số đo hai góc đối đỉnh bằng 100° thì mỗi góc bằng:", ["50°", "100°", "200°", "25°"], 0, "Hai góc đối đỉnh bằng nhau nên mỗi góc 50°."),
        q("Hai góc kề bù có tổng số đo bằng 180°. Điều ngược lại:", ["Đúng với hai góc kề nhau có tổng bằng 180°", "Sai", "Đúng với mọi hai góc", "Không xác định"], 0, "Hai góc có tổng 180° và một cạnh chung là hai góc kề bù."),
        q("Góc tạo bởi tia phân giác với cạnh góc có đặc điểm:", ["Bằng nửa góc ban đầu", "Bằng góc ban đầu", "Gấp đôi góc ban đầu", "Bằng 90°"], 0, "Nửa góc ban đầu."),
    ],
    bt_co_ban=[
        bt("Tính góc kề bù với góc 75°.", ["105°", "105"], "180° − 75° = 105°."),
        bt("Hai góc đối đỉnh xOy và x'Oy' với xOy = 60°. Tính x'Oy'.", ["60°", "60"], "Hai góc đối đỉnh bằng nhau."),
        bt("Trong hình 3.4, tính số đo góc mOt biết góc tOn = 60° và mOt kề bù với góc đó.", ["120°", "120"], "180° − 60° = 120°."),
        bt("Cho góc xOy = 68°, Oz là tia phân giác. Tính góc xOz.", ["34°", "34"], "68° : 2 = 34°."),
        bt("Am là tia phân giác góc xAy, xAm = 65°. Tính góc xAy.", ["130°", "130"], "2 · 65° = 130°."),
        bt("Vẽ góc xOy = 60°, tia Om là tia đối của tia Ox. Tính góc yOm.", ["120°", "120"], "Góc yOm kề bù với góc xOy."),
        bt("Cho hình 3.15a, DMA = 45°. Tính góc DMB.", ["135°", "135"], "Hai góc kề bù: 180° − 45° = 135°."),
        bt("Cho hình 3.15b, xBm = 36°. Tính góc yBm.", ["144°", "144"], "Hai góc kề bù: 180° − 36° = 144°."),
    ],
    bt_nang_cao=[
        nc("Vẽ góc xOy = 60°, tia Ot là tia phân giác, tia Om là tia đối của tia Ox. Tính góc tOm.", "Tính xOt rồi dùng kề bù.", ["150°", "150"], "xOt = 30°; tOm = 180° − 30° = 150°."),
        nc("Hai góc kề bù có tỉ số số đo là 2 : 7. Tính số đo góc nhỏ.", "Tổng bằng 180°, chia theo tỉ lệ 2 : 7.", ["40°", "40"], "2 + 7 = 9 phần; mỗi phần 20°; góc nhỏ 2 · 20° = 40°."),
        nc("Hai góc đối đỉnh có tổng số đo bằng 100°. Tính số đo mỗi góc.", "Hai góc đối đỉnh bằng nhau.", ["50°", "50"], "Mỗi góc 100° : 2 = 50°."),
    ],
)


# ============================================================
# BÀI 9: HAI ĐƯỜNG THẲNG SONG SONG VÀ DẤU HIỆU NHẬN BIẾT
# ============================================================
B9 = bai(
    ly_thuyet="""📌 1. CÁC GÓC TẠO BỞI MỘT ĐƯỜNG THẲNG CẮT HAI ĐƯỜNG THẲNG
- Cho đường thẳng c cắt hai đường thẳng a và b tại A và B. Có 8 góc được tạo thành.
- Cặp góc so le trong: nằm khác phía so với c và nằm trong hai đường thẳng a, b (ví dụ A1 và B3).
- Cặp góc đồng vị: nằm cùng phía so với c và cùng vị trí ở hai đường thẳng (ví dụ A1 và B1).
- Cặp góc trong cùng phía: nằm cùng phía so với c và nằm trong hai đường thẳng.

📌 2. TÍNH CHẤT
- Nếu a // b thì hai góc so le trong bằng nhau; hai góc đồng vị bằng nhau; hai góc trong cùng phía bù nhau (có tổng 180°).

📌 3. DẤU HIỆU NHẬN BIẾT HAI ĐƯỜNG THẲNG SONG SONG
- Nếu đường thẳng c cắt hai đường thẳng a, b và có một cặp góc so le trong bằng nhau (hoặc một cặp góc đồng vị bằng nhau) thì a // b.
- Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì song song với nhau.
""",
    vi_du="""Ví dụ: Trên hình 3.21, xAB = ABy' = 70°. Hai góc này ở vị trí so le trong nên xy // x'y'.

Luyện tập: Trên hình 3.19, nếu A2 = 40° và B4 = 40° thì các góc còn lại cũng được tính dễ dàng nhờ tính chất kề bù và đối đỉnh.""",
    cau_hoi=[
        q("Hai góc so le trong là hai góc:", ["Nằm khác phía với cát tuyến và nằm trong hai đường thẳng", "Nằm cùng phía trong", "Đối đỉnh", "Kề bù"], 0, "Đây là định nghĩa góc so le trong."),
        q("Hai góc đồng vị là hai góc:", ["Cùng phía với cát tuyến và cùng vị trí ở hai đường thẳng", "Khác phía, đối đỉnh", "Kề bù", "Phụ nhau"], 0, "Đây là định nghĩa góc đồng vị."),
        q("Khi a // b và c cắt a, b thì hai góc so le trong:", ["Bằng nhau", "Bù nhau", "Đối nhau", "Không xác định"], 0, "Tính chất hai đường thẳng song song."),
        q("Khi a // b bị c cắt, hai góc trong cùng phía có tổng số đo:", ["180°", "90°", "360°", "0°"], 0, "Hai góc trong cùng phía bù nhau."),
        q("Khi a // b, một cặp góc so le trong bằng 60°. Cặp góc so le trong còn lại có số đo:", ["60°", "120°", "30°", "90°"], 0, "Hai cặp góc so le trong đều bằng nhau khi a // b."),
        q("Hai góc trong cùng phía bằng 110° và 70°. Hai đường thẳng có song song không?", ["Có, vì tổng bằng 180°", "Không, vì tổng khác 90°", "Có, vì hai góc bằng nhau", "Không xác định"], 0, "Tổng 110° + 70° = 180° là dấu hiệu song song."),
        q("Nếu một cặp góc so le trong bằng nhau thì:", ["Hai đường thẳng song song", "Hai đường thẳng vuông góc", "Hai đường thẳng trùng nhau", "Hai đường thẳng cắt nhau"], 0, "Dấu hiệu nhận biết song song."),
        q("Đường thẳng c cắt a, b tạo cặp góc đồng vị bằng nhau thì:", ["a // b", "a ⊥ b", "a trùng b", "a cắt b"], 0, "Dấu hiệu nhận biết song song."),
        q("Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì:", ["Song song với nhau", "Vuông góc với nhau", "Cắt nhau", "Trùng nhau"], 0, "Nhận xét trong bài."),
        q("Hai đường thẳng a và b song song, góc đồng vị với góc 40° có số đo:", ["40°", "140°", "50°", "180°"], 0, "Góc đồng vị bằng nhau."),
        q("Đường thẳng c cắt a, b; góc so le trong 50° và 130°. Kết luận:", ["a không song song với b", "a song song với b", "a vuông góc b", "a trùng b"], 0, "Hai góc so le trong không bằng nhau nên a không song song b."),
        q("Đường thẳng c cắt a, b; hai góc trong cùng phía 120° và 60°. Kết luận:", ["a // b", "a không song song b", "a ⊥ b", "a cắt b"], 0, "120° + 60° = 180°."),
        q("Hai đường thẳng a // b, một góc trong cùng phía bằng 75°. Góc trong cùng phía còn lại bằng:", ["105°", "75°", "15°", "180°"], 0, "75° + 105° = 180°."),
        q("Nếu a // b và b // c thì:", ["a // c", "a ⊥ c", "a cắt c", "a trùng c"], 0, "Tính chất bắc cầu của song song."),
        q("Qua điểm M nằm ngoài đường thẳng a, có bao nhiêu đường thẳng song song với a?", ["Một", "Hai", "Không có", "Vô số"], 0, "Theo tiên đề Euclid."),
        q("Khi thợ xây kiểm tra các thanh ngang có song song không, họ dựa vào:", ["Cùng vuông góc với một thanh dọc", "Bằng độ dài", "Cùng cắt một đường", "Cùng nằm ngang"], 0, "Hai đường cùng vuông góc với một đường thứ ba thì song song."),
        q("Hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì:", ["Song song với nhau", "Vuông góc", "Cắt nhau", "Trùng nhau"], 0, "Nhận xét về tính bắc cầu."),
        q("Đường thẳng cắt hai đường song song tạo ra:", ["Các cặp góc so le trong bằng nhau", "Bốn góc vuông", "Không có góc nào", "Các góc luôn trùng nhau"], 0, "Tính chất của hai đường thẳng song song."),
        q("Góc so le trong với góc 65° (khi a // b) có số đo:", ["65°", "115°", "25°", "180°"], 0, "Góc so le trong bằng nhau khi hai đường song song."),
        q("Hai góc đồng vị không bằng nhau thì hai đường thẳng:", ["Không song song", "Song song", "Vuông góc", "Trùng nhau"], 0, "Đảo của tính chất đồng vị."),
        q("Cho a // b, góc A1 = 130°. Góc trong cùng phía với A1 bằng:", ["50°", "130°", "180°", "230°"], 0, "180° − 130° = 50°."),
        q("Đường thẳng d vuông góc với a và d vuông góc với b thì:", ["a // b", "a ⊥ b", "a cắt b", "a trùng b"], 0, "Hai đường cùng vuông góc với một đường thứ ba thì song song."),
        q("Hai góc đồng vị nằm:", ["Cùng phía với cát tuyến", "Khác phía với cát tuyến", "Đối đỉnh", "Kề bù"], 0, "Đồng vị là cùng phía với cát tuyến."),
        q("Cặp góc so le trong nằm:", ["Khác phía với cát tuyến", "Cùng phía với cát tuyến", "Đối đỉnh", "Kề bù"], 0, "So le trong nằm khác phía."),
        q("Trong hình 3.20b, a và b song song nếu:", ["Có một cặp góc so le trong bằng nhau", "Có hai góc vuông", "Đường c vuông góc a", "Không có điều kiện"], 0, "Dấu hiệu nhận biết song song."),
        q("Hai thanh ray đường sắt song song theo nguyên lí:", ["Các góc so le trong hoặc đồng vị bằng nhau", "Các góc bất kì bằng nhau", "Hai đường luôn cắt nhau", "Hai đường trùng nhau"], 0, "Dấu hiệu song song."),
        q("Cho a // b, góc A4 = 40°. Góc B2 (so le trong với A4) bằng:", ["40°", "140°", "50°", "180°"], 0, "Hai góc so le trong bằng nhau."),
        q("Nếu hai góc đồng vị có tổng bằng 180°, hai đường thẳng:", ["Không đảm bảo song song", "Chắc chắn song song", "Chắc chắn vuông góc", "Chắc chắn trùng nhau"], 0, "Chỉ tổng 180° của đồng vị không là dấu hiệu."),
        q("Đường thẳng xx' ⊥ yy' và yy' ⊥ zz'. Khi đó:", ["xx' // zz'", "xx' ⊥ zz'", "xx' cắt zz' tại O", "xx' trùng zz'"], 0, "Hai đường cùng vuông góc với một đường thẳng thì song song."),
        q("Chọn khẳng định đúng về góc trong hình chữ nhật:", ["Các cặp cạnh đối song song", "Các cạnh đều vuông góc", "Các góc đều nhọn", "Không có cạnh song song"], 0, "Hình chữ nhật có các cặp cạnh đối song song."),
    ],
    bt_co_ban=[
        bt("Cho a // b, góc so le trong bằng 52°. Tính góc đồng vị với góc đó.", ["52°", "52"], "Góc đồng vị bằng góc so le trong khi a // b."),
        bt("Cho a // b, góc trong cùng phía bằng 115°. Tính góc trong cùng phía còn lại.", ["65°", "65"], "180° − 115° = 65°."),
        bt("Hình 3.21: xAB = ABy' = 70°. Hai đường thẳng xy và x'y' có song song không?", ["có", "Có", "song song"], "Hai góc so le trong bằng nhau."),
        bt("Hình 3.22: góc A = 60°, góc D = 60°. Có AB // DC không?", ["có", "Có"], "Hai góc so le trong bằng nhau."),
        bt("Qua điểm M nằm ngoài đường thẳng BC, vẽ được bao nhiêu đường thẳng song song với BC?", ["1", "một"], "Theo tiên đề Euclid."),
        bt("Hình 3.29: xAz = 50°, yBz = 50°. Có Ax // By không?", ["có", "Có"], "Hai góc đồng vị bằng nhau."),
        bt("Cho hai đường thẳng a, b cùng vuông góc với c. Hỏi a và b có song song không?", ["có", "Có"], "Dấu hiệu nhận biết song song."),
        bt("Hai góc kề bù, một góc 40°. Tổng số đo hai góc bằng bao nhiêu?", ["180°", "180"], "Tổng hai góc kề bù luôn bằng 180°."),
    ],
    bt_nang_cao=[
        nc("Hình 3.7: MEF = 40° và EMN = 40°. Giải thích tại sao EF // NM.", "Xét cặp góc ở vị trí nào.", ["so le trong"], "Hai góc so le trong bằng nhau nên EF // NM."),
        nc("Cho hình 3.30, MNQ = PQN = 35°. Chứng minh MN // QP.", "Xét cặp góc so le trong.", ["so le trong"], "Hai góc so le trong MNQ và PQN bằng nhau nên MN // QP."),
        nc("Hai góc so le trong tạo bởi Ax và By với AB đều bằng 60°. Ax và By có song song không?", "Kiểm tra cặp góc so le trong.", ["có"], "Hai góc so le trong bằng nhau nên Ax // By."),
        nc("Hình 3.43: góc A = 45° và góc B = 45° (so le trong). Giải thích Ax' // By.", "Dựa vào cặp góc so le trong.", ["so le trong"], "Hai góc so le trong bằng nhau nên Ax' // By."),
    ],
)


# ============================================================
# BÀI 10: TIÊN ĐỀ EUCLID. TÍNH CHẤT CỦA HAI ĐƯỜNG THẲNG SONG SONG
# ============================================================
B10 = bai(
    ly_thuyet="""📌 1. TIÊN ĐỀ EUCLID
- Qua một điểm ở ngoài một đường thẳng, chỉ có một đường thẳng song song với đường thẳng đó.

📌 2. HỆ QUẢ TỪ TIÊN ĐỀ EUCLID
- Nếu một đường thẳng cắt một trong hai đường thẳng song song thì nó cũng cắt đường thẳng còn lại.

📌 3. TÍNH CHẤT CỦA HAI ĐƯỜNG THẲNG SONG SONG
- Nếu một đường thẳng cắt hai đường thẳng song song thì:
  • Hai góc so le trong bằng nhau;
  • Hai góc đồng vị bằng nhau;
  • Hai góc trong cùng phía bù nhau.
- Nếu một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với đường thẳng còn lại.
""",
    vi_du="""Ví dụ 2: Cho xy // x'y' và góc BAy = 50°. Ta có ABx' = BAy = 50° (so le trong), và y'Bz' = BAy = 50° (đồng vị).

Luyện tập: Cho MN // BC, góc ABC = 60° thì góc AMN = 60° (đồng vị), suy ra góc BMN = 180° − 60° = 120°.""",
    cau_hoi=[
        q("Qua điểm M nằm ngoài đường thẳng a, có bao nhiêu đường thẳng song song với a?", ["Một", "Hai", "Không có", "Vô số"], 0, "Đây là tiên đề Euclid."),
        q("Nếu một đường thẳng cắt một trong hai đường thẳng song song thì:", ["Cũng cắt đường còn lại", "Song song với đường còn lại", "Trùng với đường còn lại", "Vuông góc với đường còn lại"], 0, "Hệ quả của tiên đề Euclid."),
        q("Nếu a // b và c ⊥ a thì:", ["c ⊥ b", "c // b", "c cắt b không vuông", "c trùng b"], 0, "Đường thẳng vuông góc với một trong hai đường song song thì vuông góc với đường còn lại."),
        q("Phát biểu nào đúng với tiên đề Euclid?", ["Qua M nằm ngoài a, đường thẳng qua M song song với a là duy nhất", "Có vô số đường qua M song song với a", "Không có đường nào qua M song song với a", "Mọi đường qua M đều song song với a"], 0, "Đây là nội dung tiên đề Euclid."),
        q("Trong hình, a // b, góc trong cùng phía là 110°. Góc còn lại bằng:", ["70°", "110°", "250°", "90°"], 0, "180° − 110° = 70°."),
        q("Ví dụ 2: xy // x'y', góc BAy = 50°. Góc ABx' bằng:", ["50°", "130°", "40°", "100°"], 0, "Hai góc so le trong bằng nhau."),
        q("Trong hình, MN // BC, góc ABC = 60°. Góc AMN bằng:", ["60°", "120°", "30°", "150°"], 0, "Hai góc đồng vị bằng nhau."),
        q("Cho MN // BC, góc ABC = 60°, góc BMN bằng:", ["120°", "60°", "30°", "150°"], 0, "180° − 60° = 120°."),
        q("Cho MN // BC, góc MNC = 150°. Góc ACB bằng:", ["30°", "150°", "60°", "120°"], 0, "Góc ANM = 30° và ACB đồng vị với ANM."),
        q("Hình 3.37: xx' // yy' và zz' ⊥ xx'. Góc ABy bằng:", ["90°", "180°", "45°", "0°"], 0, "zz' ⊥ xx' nên zz' ⊥ yy'."),
        q("Nhận xét đúng: đường thẳng vuông góc với một trong hai đường song song thì:", ["Vuông góc với đường còn lại", "Song song với đường còn lại", "Cắt đường còn lại không vuông góc", "Trùng với đường còn lại"], 0, "Nhận xét trong bài."),
        q("Hai đường thẳng cùng song song với đường thứ ba thì:", ["Song song với nhau", "Vuông góc", "Cắt nhau", "Trùng nhau"], 0, "Tính chất bắc cầu."),
        q("c cắt a tại A và cắt b tại B (a // b). Số điểm chung của c và a là:", ["0", "1", "2", "Vô số"], 1, "Đường c cắt a tại đúng một điểm A."),
        q("Hai góc bằng nhau thì có nhất thiết là hai góc đối đỉnh không?", ["Không nhất thiết", "Luôn đối đỉnh", "Chỉ khi là góc vuông", "Luôn không đối đỉnh"], 0, "Hai góc bằng nhau không nhất thiết đối đỉnh."),
        q("Định lí 'Hai góc kề bù bằng nhau thì mỗi góc là góc vuông'. Giả thiết là:", ["Hai góc kề bù bằng nhau", "Mỗi góc là góc vuông", "Hai góc phụ nhau", "Hai góc đối đỉnh"], 0, "Phần sau 'nếu' là giả thiết."),
        q("Trong tính chất 'Hai góc đối đỉnh thì bằng nhau', kết luận là:", ["Hai góc bằng nhau", "Hai góc đối đỉnh", "Hai góc kề bù", "Hai góc phụ nhau"], 0, "Phần sau 'thì' là kết luận."),
        q("Từ tiên đề Euclid, qua một điểm ngoài đường thẳng có:", ["Đúng một đường song song", "Không có đường nào", "Hai đường", "Vô số đường"], 0, "Đây là nội dung tiên đề."),
        q("Hai góc so le trong bằng nhau khi:", ["Hai đường thẳng song song", "Hai đường thẳng vuông góc", "Hai đường thẳng cắt nhau", "Không có điều kiện"], 0, "Tính chất của hai đường thẳng song song."),
        q("Hai đường thẳng a // b, góc đồng vị bằng 70°, góc trong cùng phía với góc đó bằng:", ["110°", "70°", "20°", "180°"], 0, "180° − 70° = 110°."),
        q("Trong hình 3.36, MN // BC. Góc AMN và góc ABC có quan hệ:", ["Đồng vị, bằng nhau", "Đối đỉnh", "Kề bù", "Phụ nhau"], 0, "Hai góc đồng vị tạo bởi cát tuyến AB với MN và BC."),
        q("Hai đường thẳng a và b cùng vuông góc với c. Khi đó:", ["a // b", "a ⊥ b", "a cắt b", "a trùng b"], 0, "Dấu hiệu song song."),
        q("Số đường thẳng qua điểm B và song song với a (B ngoài a):", ["1", "2", "0", "vô số"], 0, "Theo tiên đề Euclid."),
        q("Cho a // b. Đường c cắt a, b. Góc so le trong với góc A1 là:", ["Góc B3", "Góc B1", "Góc A3", "Góc B2"], 0, "Góc A1 và góc B3 là cặp so le trong."),
        q("Nếu xx' // yy' thì góc đồng vị bằng nhau. Đây là:", ["Tính chất", "Định nghĩa", "Tiên đề", "Quy ước"], 0, "Đây là tính chất của hai đường thẳng song song."),
        q("Đường thẳng vuông góc với một đường song song thì:", ["Vuông góc với đường còn lại", "Song song với đường còn lại", "Trùng đường còn lại", "Không liên quan"], 0, "Tính chất hai đường song song."),
        q("Hai đường thẳng song song có bao nhiêu điểm chung?", ["0", "1", "2", "Vô số"], 0, "Hai đường thẳng song song không có điểm chung."),
        q("Trong hình 3.34, a // b, góc so le trong bằng nhau. Đây là kết quả của:", ["Tiên đề Euclid", "Định nghĩa góc", "Tiên đề về số thực", "Quy tắc cộng"], 0, "Áp dụng tiên đề Euclid và tính chất hai đường song song."),
        q("Cho a // b, một góc A1 = 110°. Góc đồng vị với A1 bằng:", ["110°", "70°", "20°", "180°"], 0, "Hai góc đồng vị bằng nhau khi a // b."),
        q("Cho a // b và đường thẳng c cắt a. Đường thẳng c có cắt b không?", ["Có", "Không", "Chỉ khi c vuông góc a", "Không xác định"], 0, "Theo hệ quả của tiên đề Euclid."),
        q("Cho a // b, đường thẳng d cắt b tại một điểm. Số điểm chung của d và a là:", ["1", "0", "2", "Vô số"], 0, "Theo hệ quả tiên đề Euclid, d cũng cắt a tại đúng một điểm."),
    ],
    bt_co_ban=[
        bt("Cho xy // x'y', góc BAy = 50°. Tính góc ABx'.", ["50°", "50"], "Hai góc so le trong bằng nhau."),
        bt("Cho xy // x'y', góc BAy = 50°. Tính góc y'Bz'.", ["50°", "50"], "Hai góc đồng vị bằng nhau."),
        bt("Cho MN // BC, góc ABC = 60°. Tính góc BMN.", ["120°", "120"], "Góc AMN = 60°, góc BMN = 120°."),
        bt("Cho MN // BC, góc MNC = 150°. Tính góc ACB.", ["30°", "30"], "Góc ANM = 30° và góc ACB đồng vị với góc ANM."),
        bt("Cho xx' // yy', zz' ⊥ xx'. Tính góc ABy.", ["90°", "90"], "zz' ⊥ yy'."),
        bt("Hai đường song song, một góc trong cùng phía bằng 75°. Tính góc trong cùng phía còn lại.", ["105°", "105"], "180° − 75° = 105°."),
        bt("Cho a // b, một góc đồng vị bằng 70°. Tính góc trong cùng phía với góc đó.", ["110°", "110"], "180° − 70° = 110°."),
    ],
    bt_nang_cao=[
        nc("Tam giác ABC. Qua A kẻ đường thẳng a song song với BC. Qua B kẻ đường thẳng b song song với AC. Có thể vẽ được bao nhiêu đường thẳng b?", "Áp dụng tiên đề Euclid.", ["1", "một"], "Qua B có đúng một đường thẳng song song với AC."),
        nc("Chứng minh rằng nếu a // b và c ⊥ a thì c ⊥ b.", "Dùng góc đồng vị.", ["c ⊥ b", "vuông góc"], "Góc tạo bởi c và b bằng góc tạo bởi c và a, bằng 90°."),
        nc("Cho góc xOy không phải góc bẹt. (1) Nếu Ot là tia phân giác của xOy thì xOt = tOy. (2) Nếu xOt = tOy thì Ot là tia phân giác của xOy. Khẳng định nào đúng?", "Xét trường hợp Ot là tia đối của một tia phân giác.", ["(1) đúng; (2) sai"], "(1) đúng theo định nghĩa. (2) sai: tia đối của tia phân giác cũng tạo với hai cạnh hai góc bằng nhau nhưng không nằm trong góc xOy."),
    ],
)


# ============================================================
# BÀI 11: ĐỊNH LÍ VÀ CHỨNG MINH ĐỊNH LÍ
# ============================================================
B11 = bai(
    ly_thuyet="""📌 1. ĐỊNH LÍ
- Định lí là một khẳng định được suy ra từ những khẳng định đúng đã biết.
- Mỗi định lí thường được phát biểu dưới dạng: Nếu ... thì ...
- Phần giữa "nếu" và "thì" là giả thiết (GT); phần sau "thì" là kết luận (KL).

📌 2. CHỨNG MINH ĐỊNH LÍ
- Chứng minh một định lí là dùng lập luận để từ giả thiết và những khẳng định đúng đã biết suy ra kết luận.
- Đo đạc chỉ cho kết quả gần đúng và chỉ trong trường hợp cụ thể, nên không đủ để khẳng định định lí đúng với mọi trường hợp.

📌 3. VÍ DỤ
- Định lí "Một đường thẳng vuông góc với một trong hai đường thẳng song song thì nó cũng vuông góc với đường thẳng còn lại".
  GT: d // d', d ⊥ d'; KL: d ⊥ d''.
""",
    vi_du="""Ví dụ: Định lí "Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc đồng vị bằng nhau".
GT: a // b, c cắt a tại A, cắt b tại B; KL: góc A1 = góc B1.
Chứng minh: Vẽ b' qua B sao cho góc B2 = góc A1, suy ra b' // a; theo tiên đề Euclid thì b' trùng b, nên B1 = A1.""",
    cau_hoi=[
        q("Định lí thường được phát biểu dưới dạng:", ["Nếu ... thì ...", "Vì ... nên ...", "Khi ... thì ...", "Bởi vì ..."], 0, "Đây là cấu trúc thông dụng của định lí."),
        q("Trong định lí 'Nếu hai góc đối đỉnh thì bằng nhau', giả thiết là:", ["Hai góc đối đỉnh", "Hai góc bằng nhau", "Hai góc kề bù", "Hai góc vuông"], 0, "Phần sau 'nếu'."),
        q("Trong định lí 'Nếu hai góc đối đỉnh thì bằng nhau', kết luận là:", ["Hai góc bằng nhau", "Hai góc đối đỉnh", "Hai góc kề bù", "Hai góc phụ nhau"], 0, "Phần sau 'thì'."),
        q("Chứng minh định lí là:", ["Dùng lập luận từ giả thiết và khẳng định đúng đã biết để suy ra kết luận", "Đo đạc hình vẽ", "Vẽ nhiều hình để kiểm tra", "Chỉ dựa vào hình vẽ"], 0, "Đây là định nghĩa chứng minh."),
        q("Đo đạc chỉ cho ta kết quả:", ["Gần đúng và chỉ trong một trường hợp cụ thể", "Đúng tuyệt đối", "Luôn chính xác", "Không liên quan"], 0, "Nên cần chứng minh để khẳng định."),
        q("Một khẳng định được suy ra từ những khẳng định đúng đã biết gọi là:", ["Định lí", "Định nghĩa", "Tiên đề", "Giả thuyết"], 0, "Đây là định nghĩa định lí."),
        q("Giả thiết của định lí 'Hai góc kề bù có tổng số đo bằng 180°' là:", ["Hai góc kề bù", "Tổng bằng 180°", "Hai góc bằng nhau", "Hai góc vuông"], 0, "Phần sau 'nếu'."),
        q("Kết luận của định lí 'Hai góc kề bù có tổng số đo bằng 180°' là:", ["Hai góc kề bù", "Tổng số đo bằng 180°", "Hai góc đối đỉnh", "Hai góc phụ nhau"], 1, "Phần sau 'thì'."),
        q("Trong chứng minh định lí góc đồng vị, GT là:", ["a // b, c cắt a và b", "a cắt b", "a ⊥ b", "Góc bằng nhau"], 0, "Đây là giả thiết."),
        q("Giả thiết và kết luận viết tắt lần lượt là:", ["GT và KL", "GH và KQ", "GT và KT", "GS và KL"], 0, "Kí hiệu viết tắt."),
        q("Trong định lí 'Một đường thẳng vuông góc với một trong hai đường song song...', KL là:", ["Nó cũng vuông góc với đường thẳng còn lại", "Hai đường song song", "Hai góc bằng nhau", "Nó song song với đường còn lại"], 0, "Phần sau 'thì'."),
        q("Định lí 'Hai góc kề bù bằng nhau thì mỗi góc là góc vuông'. GT là:", ["Hai góc kề bù bằng nhau", "Mỗi góc là góc vuông", "Hai góc phụ nhau", "Hai góc đối đỉnh"], 0, "Phần sau 'nếu'."),
        q("Nhà toán học Euclid sống vào thời:", ["Cổ Hi Lạp, trước Công nguyên", "La Mã, sau Công nguyên", "Ai Cập cổ đại", "Trung Quốc cổ đại"], 0, "Thông tin trong sách."),
        q("Định lí 'Hai đường thẳng phân biệt cùng vuông góc với đường thứ ba thì song song' được suy ra từ:", ["Dấu hiệu nhận biết hai đường thẳng song song", "Tiên đề Euclid", "Định nghĩa góc", "Định lí tổng các góc tam giác"], 0, "Đây là dấu hiệu nhận biết song song."),
        q("Phát biểu dưới dạng 'Nếu ... thì ...' của định lí 'Hai góc đối đỉnh bằng nhau' là:", ["Nếu hai góc đối đỉnh thì bằng nhau", "Hai góc bằng nhau thì đối đỉnh", "Hai góc đối đỉnh khi và chỉ khi bằng nhau", "Nếu hai góc bằng nhau thì đối đỉnh"], 0, "Giả thiết là hai góc đối đỉnh."),
        q("Đảo của định lí 'Nếu hai góc đối đỉnh thì bằng nhau' là:", ["Nếu hai góc bằng nhau thì đối đỉnh", "Nếu hai góc kề bù thì bằng nhau", "Nếu hai góc đối đỉnh thì kề bù", "Nếu hai góc phụ thì bằng nhau"], 0, "Đổi chỗ giả thiết và kết luận."),
        q("Để chứng minh định lí, cần:", ["Suy luận từ giả thiết", "Đo đạc", "Vẽ nhiều hình", "Hỏi bạn"], 0, "Chứng minh dựa vào lập luận."),
        q("Trong chứng minh định lí góc đồng vị, sau khi vẽ b' qua B, ta dùng tiên đề Euclid để suy ra:", ["b' trùng b", "b' song song a", "b' vuông góc a", "b' cắt a"], 0, "Qua B chỉ có một đường song song với a."),
        q("Phần 'Giả thiết' trong một định lí được đặt sau từ:", ["Nếu", "Thì", "Chứng minh", "Hình vẽ"], 0, "Giả thiết nằm sau 'nếu'."),
        q("Phần 'Kết luận' trong một định lí được đặt sau từ:", ["Thì", "Nếu", "Giả sử", "Chứng minh"], 0, "Kết luận nằm sau 'thì'."),
        q("KL viết tắt của:", ["Kết luận", "Khẳng định", "Kiến thức", "Kiểm tra"], 0, "Viết tắt trong chứng minh định lí."),
        q("Mỗi định lí phải:", ["Được suy ra từ những khẳng định đúng đã biết", "Được đo đạc", "Được quan sát", "Được vẽ"], 0, "Đây là định nghĩa định lí."),
        q("Trong định lí 'Nếu a // b và c cắt a, b thì góc so le trong bằng nhau', giả thiết gồm:", ["a // b; c cắt a, b", "a, b, c vuông góc", "Góc so le trong bằng nhau", "a cắt b"], 0, "Phần sau 'nếu'."),
        q("Khi chứng minh 'Hai góc kề bù bằng nhau thì mỗi góc vuông', ta dựa vào:", ["Hai góc kề bù có tổng 180° và hai góc bằng nhau", "Đo góc", "Vẽ hình đẹp", "Đoán"], 0, "Lập luận logic."),
        q("Nhà toán học Euclid thuộc nền văn minh:", ["Hi Lạp", "Ai Cập", "Trung Quốc", "Ấn Độ"], 0, "Sách nêu Euclid là nhà toán học cổ Hi Lạp."),
        q("Vì sao cần chứng minh định lí thay vì chỉ đo đạc?", ["Đo đạc chỉ đúng gần đúng và trong trường hợp cụ thể", "Vì dễ hơn", "Vì thích thế", "Vì bài tập yêu cầu"], 0, "Chứng minh đảm bảo đúng mọi trường hợp."),
        q("Trong định lí 'Nếu hai góc kề bù thì tổng số đo bằng 180°', phần sau 'thì' là:", ["Tổng số đo bằng 180°", "Hai góc kề bù", "Hai góc vuông", "Hai góc phụ nhau"], 0, "Phần sau 'thì' là kết luận."),
        q("Trong chứng minh định lí, mỗi bước lập luận phải dựa vào:", ["Giả thiết hoặc khẳng định đúng đã biết", "Ý kiến cá nhân", "Hình vẽ chính xác", "Đo đạc"], 0, "Lập luận logic từ điều đã biết."),
        q("Định lí 'Hai đường thẳng phân biệt cùng song song với một đường thẳng thứ ba thì song song với nhau' có giả thiết là:", ["Hai đường thẳng cùng song song với đường thứ ba", "Hai đường thẳng song song với nhau", "Hai đường thẳng vuông góc", "Hai đường thẳng cắt nhau"], 0, "Phần sau 'nếu' là giả thiết."),
        q("Khẳng định nào là một định lí?", ["Hai góc đối đỉnh thì bằng nhau", "Góc là hình tạo bởi hai tia chung gốc", "Đường tròn là tập hợp điểm", "Hai điểm xác định một đường thẳng"], 0, "Định lí là khẳng định suy ra từ khẳng định đúng đã biết."),
    ],
    bt_co_ban=[
        bt("Viết giả thiết và kết luận: 'Nếu hai đường thẳng cùng song song với đường thứ ba thì chúng song song với nhau'.", ["GT: a // c, b // c; KL: a // b"], "Phần sau 'nếu' là GT, sau 'thì' là KL."),
        bt("Phát biểu định lí 'Hai góc đối đỉnh bằng nhau' dưới dạng Nếu ... thì ...", ["Nếu hai góc đối đỉnh thì bằng nhau"], "Đây là dạng chuẩn."),
        bt("Xác định GT và KL của 'Hai góc kề bù có tổng số đo bằng 180°'.", ["GT: hai góc kề bù; KL: tổng số đo bằng 180°"], "Đọc theo cấu trúc nếu – thì."),
        bt("Viết GT và KL của 'Hai góc đối đỉnh bằng nhau' (luyện tập 1).", ["GT: hai góc đối đỉnh; KL: hai góc bằng nhau"], "Vẽ hình tương ứng."),
    ],
    bt_nang_cao=[
        nc("Chứng minh định lí: 'Hai góc kề bù bằng nhau thì mỗi góc là góc vuông'.", "Dùng tổng hai góc kề bù bằng 180°.", ["Hai góc kề bù có tổng 180° nên mỗi góc là 90°."], "Vì hai góc bằng nhau và tổng bằng 180° nên mỗi góc bằng 90°, tức là góc vuông."),
        nc("Chứng minh: nếu hai góc đối đỉnh thì bằng nhau.", "Dùng hai góc kề bù cùng với một góc.", ["Vì O1 + O3 = 180° và O2 + O3 = 180° nên O1 = O2."], "Từ hai đẳng thức kề bù suy ra hai góc đối đỉnh bằng nhau."),
        nc("Cho d ⊥ d', d' // d''. Viết GT và KL của định lí suy ra d ⊥ d''.", "Dùng định lí về đường vuông góc với một trong hai đường song song.", ["GT: d ⊥ d', d' // d''; KL: d ⊥ d''"], "Đây là định lí trong ví dụ bài 11."),
    ],
)


CHUONG_3 = {
    "Chương III: Góc và đường thẳng song song": {
        "Bài 8: Góc ở vị trí đặc biệt. Tia phân giác của một góc": B8,
        "Bài 9: Hai đường thẳng song song và dấu hiệu nhận biết": B9,
        "Bài 10: Tiên đề Euclid. Tính chất của hai đường thẳng song song": B10,
        "Bài 11: Định lí và chứng minh định lí": B11,
    }
}

# ============================================================
# FILE toan_c4.py
# ============================================================
# ============================================================
# BÀI 12: TỔNG CÁC GÓC TRONG MỘT TAM GIÁC
# ============================================================
B12 = bai(
    ly_thuyet="""📌 1. ĐỊNH LÍ TỔNG BA GÓC TRONG MỘT TAM GIÁC
- Tổng ba góc trong một tam giác bằng 180°.
- Với tam giác ABC: Â + B̂ + Ĉ = 180°.

📌 2. PHÂN LOẠI TAM GIÁC THEO GÓC
- Tam giác nhọn: cả ba góc đều nhọn.
- Tam giác vuông: có một góc vuông.
- Tam giác tù: có một góc tù.
- Hai góc nhọn của tam giác vuông phụ nhau (tổng bằng 90°).

📌 3. GÓC NGOÀI CỦA TAM GIÁC
- Góc ngoài tại một đỉnh có số đo bằng tổng số đo hai góc trong không kề với nó.
""",
    vi_du="""Ví dụ: Tam giác ABC có B = 50°, C = 60° thì A = 180° − 50° − 60° = 70°.

Tam giác DEF có E = 30°, F = 50° thì D = 180° − 30° − 50° = 100°.

Tam giác MNP vuông tại M, N = 60° thì P = 180° − 90° − 60° = 30°.""",
    cau_hoi=[
        q("Tổng ba góc trong một tam giác bằng:", ["90°", "180°", "360°", "270°"], 1, "Định lí tổng ba góc trong tam giác."),
        q("Tam giác ABC có A = 50°, B = 60°. Góc C bằng:", ["70°", "60°", "80°", "90°"], 0, "180° − 50° − 60° = 70°."),
        q("Tam giác có hai góc 90° và 30°. Góc còn lại bằng:", ["60°", "30°", "90°", "0°"], 0, "180° − 90° − 30° = 60°."),
        q("Tam giác vuông có một góc 60°. Góc nhọn còn lại bằng:", ["30°", "60°", "90°", "120°"], 0, "90° − 60° = 30°."),
        q("Hai góc nhọn của tam giác vuông có tổng:", ["90°", "180°", "60°", "120°"], 0, "Hai góc nhọn phụ nhau."),
        q("Tam giác có ba góc đều nhọn gọi là:", ["Tam giác nhọn", "Tam giác vuông", "Tam giác tù", "Tam giác đều"], 0, "Đây là phân loại theo góc."),
        q("Tam giác có một góc tù gọi là:", ["Tam giác tù", "Tam giác nhọn", "Tam giác vuông", "Tam giác cân"], 0, "Có góc lớn hơn 90°."),
        q("Tam giác ABC vuông tại A thì B + C bằng:", ["90°", "180°", "60°", "270°"], 0, "Tổng ba góc là 180°, trừ góc vuông 90°."),
        q("Góc ngoài tại đỉnh C của tam giác ABC bằng:", ["Tổng hai góc trong không kề với C", "Tổng ba góc trong", "Góc A", "Góc B"], 0, "Đây là tính chất góc ngoài."),
        q("Tam giác có góc ngoài 120° và một góc trong không kề với nó là 35°. Góc trong còn lại bằng:", ["85°", "155°", "35°", "120°"], 0, "120° − 35° = 85°."),
        q("Tam giác có hai góc bằng 45° thì là tam giác:", ["Vuông", "Nhọn", "Tù", "Đều"], 0, "45° + 45° = 90° nên có góc vuông."),
        q("Tam giác có ba góc bằng nhau thì mỗi góc bằng:", ["60°", "90°", "45°", "120°"], 0, "180° : 3 = 60°."),
        q("Tam giác có hai góc là 70° và 60°. Góc còn lại bằng:", ["50°", "70°", "60°", "40°"], 0, "180° − 70° − 60° = 50°."),
        q("Tam giác vuông có một góc nhọn bằng 55°. Góc nhọn còn lại bằng:", ["35°", "55°", "45°", "90°"], 0, "90° − 55° = 35°."),
        q("Tam giác ABC có A + B = 130°. Góc C bằng:", ["50°", "130°", "180°", "230°"], 0, "180° − 130° = 50°."),
        q("Tam giác MNP vuông tại M có N = 60°. Góc P bằng:", ["30°", "60°", "90°", "120°"], 0, "180° − 90° − 60° = 30°."),
        q("Góc ngoài tại một đỉnh của tam giác luôn:", ["Lớn hơn mỗi góc trong không kề với nó", "Nhỏ hơn mỗi góc trong không kề với nó", "Bằng 90°", "Bằng 180°"], 0, "Góc ngoài bằng tổng hai góc trong không kề, nên lớn hơn mỗi góc."),
        q("Trong tam giác có góc tù, các góc còn lại:", ["Đều nhọn", "Có một góc vuông", "Có một góc tù", "Đều tù"], 0, "Hai góc còn lại phải nhọn."),
        q("Tam giác ABC có A = 2B và C = 90°. Góc B bằng:", ["30°", "60°", "45°", "90°"], 0, "A + B = 90°; 2B + B = 90° nên B = 30°."),
        q("Tam giác có ba góc tỉ lệ 1 : 2 : 3. Góc lớn nhất bằng:", ["90°", "60°", "45°", "120°"], 0, "Tổng 6 phần = 180°, 1 phần = 30°; góc lớn nhất 3·30° = 90°."),
        q("Hai góc của một tam giác bằng nhau và đều bằng 50°. Góc còn lại bằng:", ["80°", "50°", "100°", "130°"], 0, "180° − 50° − 50° = 80°."),
        q("Trong hình 4.1 (ba góc tại mỗi đỉnh chung), các điểm A, B, C:", ["Không thẳng hàng", "Thẳng hàng", "Trùng nhau", "Cách đều nhau"], 1, "Tổng ba góc tại B bằng 180° nên A, B, C thẳng hàng."),
        q("Tam giác có góc ngoài bằng 110° và góc trong không kề với nó bằng 70°. Góc trong còn lại bằng:", ["40°", "110°", "70°", "180°"], 0, "110° − 70° = 40°."),
        q("Tam giác ABC vuông tại A có góc B = 40°. Góc C bằng:", ["50°", "40°", "90°", "140°"], 0, "90° − 40° = 50°."),
        q("Số đo ba góc của tam giác vuông cân là:", ["90°, 45°, 45°", "90°, 60°, 30°", "60°, 60°, 60°", "90°, 90°, 0°"], 0, "Tam giác vuông cân có góc vuông và hai góc 45°."),
        q("Tam giác có hai góc bằng 90° là tam giác:", ["Không tồn tại", "Vuông", "Đều", "Nhọn"], 0, "Tổng hai góc đã là 180°, không có tam giác."),
        q("Tam giác có ba góc nhọn thì tổng số đo ba góc là:", ["180°", "270°", "120°", "360°"], 0, "Luôn là 180°."),
        q("Góc ngoài tại đỉnh của tam giác đều có số đo:", ["120°", "60°", "90°", "180°"], 0, "Góc trong 60°; góc ngoài kề bù: 180° − 60° = 120°."),
        q("Tam giác ABC có A = 36° và B = 72°. Góc C bằng:", ["72°", "36°", "108°", "90°"], 0, "180° − 36° − 72° = 72°."),
        q("Tam giác DEF có góc D = 100°. Hai góc còn lại có tổng bằng:", ["80°", "100°", "180°", "260°"], 0, "180° − 100° = 80°."),
        q("Tam giác vuông có cạnh huyền là cạnh đối diện với:", ["Góc vuông", "Góc nhọn", "Góc tù", "Không góc nào"], 0, "Cạnh huyền đối diện góc vuông."),
    ],
    bt_co_ban=[
        bt("Tam giác MNP có M = 90°, N = 60°. Tính góc P.", ["30°", "30"], "180° − 90° − 60° = 30°."),
        bt("Tam giác ABC có A = 50°, B = 60°. Tính góc C.", ["70°", "70"], "180° − 50° − 60° = 70°."),
        bt("Tam giác vuông có một góc 55°. Tính góc nhọn còn lại.", ["35°", "35"], "90° − 55° = 35°."),
        bt("Tam giác có góc ngoài 120° và góc trong không kề 35°. Tính góc trong còn lại.", ["85°", "85"], "120° − 35° = 85°."),
        bt("Tam giác có hai góc 70° và 60°. Tính góc còn lại.", ["50°", "50"], "180° − 70° − 60° = 50°."),
        bt("Hình 4.6: tam giác có hai góc 120° và 35°. Tính góc còn lại (x).", ["25°", "25"], "180° − 120° − 35° = 25°."),
        bt("Tam giác vuông ABC, B = 40°. Tính góc C.", ["50°", "50"], "90° − 40° = 50°."),
        bt("Tam giác có góc A = 36°, B = 72°. Tính góc C.", ["72°", "72"], "180° − 36° − 72° = 72°."),
    ],
    bt_nang_cao=[
        nc("Tam giác ABC có A = 2B và C = 90°. Tính góc B.", "Dùng A + B = 90°.", ["30°", "30"], "2B + B = 90° nên B = 30°."),
        nc("Tam giác có ba góc tỉ lệ 1 : 2 : 3. Tính góc lớn nhất.", "Tổng 6 phần = 180°.", ["90°", "90"], "1 phần = 30°, góc lớn nhất 90°."),
        nc("Tam giác ABC có góc ngoài tại C bằng 130°, góc A = 60°. Tính góc B.", "Góc ngoài bằng tổng hai góc trong không kề.", ["70°", "70"], "130° = A + B nên B = 130° − 60° = 70°."),
        nc("Tam giác ABC cân tại A, góc A = 40°. Tính góc B (góc đáy).", "Hai góc đáy bằng nhau.", ["70°", "70"], "B = C = (180° − 40°) : 2 = 70°."),
    ],
)


# ============================================================
# BÀI 13: HAI TAM GIÁC BẰNG NHAU. TRƯỜNG HỢP BẰNG NHAU CẠNH - CẠNH - CẠNH
# ============================================================
B13 = bai(
    ly_thuyet="""📌 1. HAI TAM GIÁC BẰNG NHAU
- Hai tam giác bằng nhau nếu chúng có các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau.
- Kí hiệu: ΔABC = ΔA'B'C' khi AB = A'B', BC = B'C', CA = C'A' và Â = Â', B̂ = B̂', Ĉ = Ĉ'.
- Đỉnh tương ứng: A với A', B với B', C với C'. Cạnh tương ứng: AB với A'B', ...

📌 2. TRƯỜNG HỢP BẰNG NHAU CẠNH - CẠNH - CẠNH (c.c.c)
- Nếu ba cạnh của tam giác này bằng ba cạnh của tam giác kia thì hai tam giác đó bằng nhau.
""",
    vi_du="""Ví dụ 2: Tam giác ACB và BDA có AC = BD, BC = AD, AB là cạnh chung. Theo c.c.c: ΔACB = ΔBDA.

Vận dụng: Dùng compa vẽ hai cung tròn tâm O và A, tâm O và B; khi đó tia OM là tia phân giác của góc xOy vì ΔOAM = ΔOBM (c.c.c).""",
    cau_hoi=[
        q("Hai tam giác bằng nhau nếu:", ["Các cạnh và góc tương ứng bằng nhau", "Có một cạnh bằng nhau", "Có hai góc bằng nhau", "Có diện tích bằng nhau"], 0, "Định nghĩa hai tam giác bằng nhau."),
        q("Trường hợp bằng nhau c.c.c là:", ["Ba cạnh bằng ba cạnh", "Hai góc và một cạnh", "Hai cạnh và góc xen giữa", "Hai cạnh góc vuông"], 0, "c.c.c: cạnh - cạnh - cạnh."),
        q("Nếu ΔABC = ΔDEF thì cạnh AB tương ứng với:", ["DE", "EF", "DF", "EF hoặc DF"], 0, "Đỉnh A ↔ D, B ↔ E nên AB ↔ DE."),
        q("Nếu ΔABC = ΔDEF thì góc B tương ứng với:", ["Góc E", "Góc D", "Góc F", "Góc A"], 0, "B ↔ E."),
        q("Hai tam giác có ba cạnh 3 cm, 4 cm, 5 cm và ba cạnh 3 cm, 4 cm, 5 cm. Kết luận:", ["Bằng nhau theo c.c.c", "Không bằng nhau", "Bằng nhau theo c.g.c", "Chưa đủ dữ kiện"], 0, "Ba cạnh tương ứng bằng nhau."),
        q("Hai tam giác ABC và DEF có AB = DE, BC = EF, CA = FD thì:", ["ΔABC = ΔDEF", "ΔABC và ΔDEF không bằng nhau", "ΔABC = ΔFED", "Chưa đủ điều kiện"], 0, "Theo c.c.c."),
        q("Ví dụ 2: AC = BD, BC = AD, AB chung. Hai tam giác ACB và BDA bằng nhau theo:", ["c.c.c", "c.g.c", "g.c.g", "c.h.c"], 0, "Ba cạnh tương ứng bằng nhau."),
        q("Hai tam giác có hai cạnh bằng nhau thì:", ["Chưa đủ để kết luận bằng nhau", "Chắc chắn bằng nhau", "Chắc chắn không bằng nhau", "Bằng nhau theo c.c.c"], 0, "Cần ba cạnh tương ứng bằng nhau."),
        q("Hai tam giác có ba góc tương ứng bằng nhau thì:", ["Chưa chắc bằng nhau", "Chắc chắn bằng nhau", "Có ba cạnh bằng nhau", "Có diện tích bằng nhau"], 0, "Ba góc bằng nhau chưa đủ để kết luận bằng nhau."),
        q("Nếu ΔABC = ΔA'B'C' thì:", ["Chu vi hai tam giác bằng nhau", "Chu vi khác nhau", "Hai tam giác có diện tích khác nhau", "Các cạnh không tương ứng"], 0, "Các cạnh tương ứng bằng nhau nên chu vi bằng nhau."),
        q("Hình 4.14 vẽ tam giác ABC có AB = 5 cm, AC = 4 cm, BC = 6 cm bằng cách:", ["Dùng compa vẽ hai cung tròn", "Dùng thước đo góc", "Đo diện tích", "Đoán"], 0, "Dùng compa để xác định đỉnh A."),
        q("Vẽ tam giác có ba cạnh 3 cm, 4 cm, 5 cm. Số tam giác duy nhất (sai khác vị trí) là:", ["1", "2", "3", "Vô số"], 0, "Theo c.c.c, các tam giác có ba cạnh cho trước bằng nhau."),
        q("Đoạn thẳng có độ dài 5 cm là cạnh tương ứng với:", ["Cạnh có độ dài 5 cm", "Góc 5°", "Cạnh 5 m", "Đường cao"], 0, "Cạnh bằng nhau phải có độ dài bằng nhau."),
        q("ΔABC = ΔDEF với AB = 5 cm. Khi đó DE bằng:", ["5 cm", "10 cm", "2,5 cm", "Không xác định"], 0, "Cạnh tương ứng bằng nhau."),
        q("Hai tam giác bằng nhau thì:", ["Các cặp góc tương ứng bằng nhau", "Các cặp góc tương ứng khác nhau", "Các cặp cạnh khác nhau", "Không có điều kiện"], 0, "Định nghĩa."),
        q("Tia OM là tia phân giác của góc xOy khi ΔOAM = ΔOBM theo:", ["c.c.c", "c.g.c", "g.c.g", "c.h.c"], 0, "OA = OB, AM = BM, OM chung."),
        q("Hai tam giác ABC và A'B'C' có AB = A'B', BC = B'C', CA = C'A'. Góc A tương ứng với:", ["Góc A'", "Góc B'", "Góc C'", "Không xác định"], 0, "A ↔ A'."),
        q("Trong ΔABC = ΔDEF, nếu A = 50° thì D bằng:", ["50°", "40°", "130°", "90°"], 0, "Góc tương ứng bằng nhau."),
        q("Hai tam giác bằng nhau có:", ["Cùng hình dạng và kích thước", "Chỉ cùng hình dạng", "Chỉ cùng kích thước", "Không liên quan"], 0, "Đây là ý nghĩa của sự bằng nhau."),
        q("Trong ΔABC = ΔMNP, đỉnh tương ứng với B là:", ["N", "M", "P", "A"], 0, "B ↔ N."),
        q("Hai tam giác có các góc bằng nhau từng đôi và một cạnh bằng nhau thì:", ["Chưa chắc bằng nhau nếu không có c.c.c", "Chắc chắn bằng nhau", "Chắc chắn không bằng nhau", "Có diện tích bằng nhau"], 0, "Cần kiểm tra thêm trường hợp."),
        q("Tam giác có ba cạnh 2 cm, 3 cm, 6 cm:", ["Không tồn tại", "Là tam giác đều", "Là tam giác vuông", "Là tam giác cân"], 0, "Vì 2 + 3 < 6 nên không tạo thành tam giác."),
        q("Nếu AB = DE, BC = EF, CA = FD thì góc C bằng góc:", ["F", "D", "E", "A"], 0, "C ↔ F."),
        q("Hình chữ nhật ABCD có hai đường chéo cắt nhau tại O. Tam giác AOB và COD có OA = OC, OB = OD và AB = CD. Hai tam giác bằng nhau theo:", ["c.c.c", "g.c.g", "c.g.c", "Không bằng nhau"], 0, "Ba cạnh tương ứng bằng nhau."),
        q("Hai tam giác có diện tích bằng nhau thì:", ["Chưa chắc bằng nhau", "Chắc chắn bằng nhau", "Chắc chắn không bằng nhau", "Có ba góc bằng nhau"], 0, "Diện tích bằng nhau chưa đủ để kết luận bằng nhau."),
        q("Đường tròn tâm B bán kính 5 cm và đường tròn tâm C bán kính 4 cm cắt nhau tại A. Khi đó AB = 5 cm, AC = 4 cm. Điều này dựa vào:", ["Tính chất bán kính", "Định lí Pythagoras", "Quy tắc cộng", "Tiên đề Euclid"], 0, "Bán kính đường tròn bằng khoảng cách từ tâm đến điểm trên đường tròn."),
        q("Tam giác ABC có AB = 3 cm, BC = 4 cm, CA = 5 cm. Tam giác A'B'C' có A'B' = 5 cm, B'C' = 4 cm, C'A' = 3 cm. Hai tam giác có bằng nhau không?", ["Có, theo c.c.c (A ↔ C', B ↔ B', C ↔ A')", "Không", "Chỉ bằng nếu có góc bằng nhau", "Chưa đủ dữ kiện"], 0, "Ba cạnh tương ứng bằng nhau nên theo c.c.c."),
        q("Nếu ΔABC = ΔDEF thì cạnh BC tương ứng với:", ["EF", "DE", "DF", "Không có"], 0, "B ↔ E, C ↔ F."),
        q("Hai tam giác bằng nhau có thể đặt chồng khít lên nhau. Khẳng định này:", ["Đúng", "Sai", "Chỉ đúng với tam giác đều", "Chỉ đúng với tam giác vuông"], 0, "Đây là ý nghĩa của sự bằng nhau."),
        q("Hai tam giác bằng nhau thì:", ["Các cạnh và góc tương ứng bằng nhau", "Chỉ các cạnh bằng nhau", "Chỉ các góc bằng nhau", "Diện tích khác nhau"], 0, "Định nghĩa hai tam giác bằng nhau."),
    ],
    bt_co_ban=[
        bt("Cho ΔABC = ΔDEF. Cho AB = 5 cm. Tính DE.", ["5 cm", "5"], "Cạnh tương ứng bằng nhau."),
        bt("Cho ΔABC = ΔDEF. Góc A = 50°. Tính góc D.", ["50°", "50"], "Góc tương ứng bằng nhau."),
        bt("Hai tam giác có AB = DE, BC = EF, CA = FD. Hai tam giác có bằng nhau không?", ["có", "Có"], "Theo c.c.c."),
        bt("Cho hình 4.18: AB = DE, AC = DF, BC = EF. Tam giác nào bằng nhau?", ["ΔABC = ΔDEF", "ABC và DEF"], "Theo c.c.c."),
        bt("Cho ΔABC có AB = 4, BC = 5, CA = 3 (cm). Tam giác A'B'C' có A'B' = 4, B'C' = 5, C'A' = 3. Hai tam giác có bằng nhau không?", ["có", "Có"], "Theo c.c.c."),
    ],
    bt_nang_cao=[
        nc("Cho ΔABC = ΔA'B'C'. Biết AB = 4 cm, BC = 6 cm, CA = 5 cm. Tính chu vi tam giác A'B'C'.", "Các cạnh tương ứng bằng nhau.", ["15 cm", "15"], "Chu vi = 4 + 6 + 5 = 15 cm."),
        nc("Cho ΔABC và ΔDEF có AB = DE, AC = DF, BC = EF. Chứng minh ΔABC = ΔDEF.", "Áp dụng c.c.c.", ["c.c.c"], "Ba cạnh tương ứng bằng nhau nên bằng nhau theo c.c.c."),
        nc("Cho ΔABC = ΔDEF với BC = 8 cm và AB = 5 cm. Tính EF và DE.", "Cạnh tương ứng bằng nhau.", ["8 cm; 5 cm", "8; 5"], "EF = BC = 8 cm; DE = AB = 5 cm."),
    ],
)


# ============================================================
# BÀI 14: TRƯỜNG HỢP BẰNG NHAU THỨ HAI VÀ THỨ BA CỦA TAM GIÁC
# ============================================================
B14 = bai(
    ly_thuyet="""📌 1. TRƯỜNG HỢP BẰNG NHAU CẠNH - GÓC - CẠNH (c.g.c)
- Nếu hai cạnh và góc xen giữa của tam giác này bằng hai cạnh và góc xen giữa của tam giác kia thì hai tam giác đó bằng nhau.
- Góc xen giữa hai cạnh là góc được tạo bởi hai cạnh đó.

📌 2. TRƯỜNG HỢP BẰNG NHAU GÓC - CẠNH - GÓC (g.c.g)
- Nếu một cạnh và hai góc kề cạnh đó của tam giác này bằng một cạnh và hai góc kề cạnh đó của tam giác kia thì hai tam giác đó bằng nhau.
- Góc kề cạnh là góc có một đỉnh là đầu mút của cạnh đó.
""",
    vi_du="""Ví dụ 1: Hai tam giác ABC và ADC có AB = AD, góc BAC = góc DAC, AC chung. Theo c.g.c: ΔABC = ΔADC.

Ví dụ 2 (g.c.g): Tam giác ABC và DEC có góc BAC = góc EDC, AC = DC, góc BCA = góc ECD (đối đỉnh). Suy ra ΔABC = ΔDEC.

Luyện tập 1: ΔABC = ΔDEF, BC = 4 cm, góc B = 40°, góc C = 60°. Khi đó EF = BC = 4 cm và góc A = 80°, nên góc D = 80°.""",
    cau_hoi=[
        q("Trường hợp bằng nhau c.g.c là:", ["Hai cạnh và góc xen giữa bằng nhau", "Ba cạnh bằng nhau", "Hai góc và cạnh kề", "Hai cạnh góc vuông"], 0, "c.g.c: cạnh - góc - cạnh."),
        q("Trường hợp bằng nhau g.c.g là:", ["Một cạnh và hai góc kề cạnh đó", "Ba góc bằng nhau", "Ba cạnh bằng nhau", "Hai cạnh và góc đối"], 0, "g.c.g: góc - cạnh - góc."),
        q("Góc xen giữa hai cạnh AB và AC của tam giác ABC là:", ["Góc A", "Góc B", "Góc C", "Không có"], 0, "Góc A là góc giữa hai cạnh AB và AC."),
        q("Góc kề cạnh BC của tam giác ABC gồm:", ["Góc B và góc C", "Góc A", "Góc A và B", "Không có"], 0, "Góc kề cạnh BC là B và C."),
        q("Ví dụ 1: AB = AD, góc BAC = góc DAC, AC chung. Hai tam giác ABC và ADC bằng nhau theo:", ["c.g.c", "c.c.c", "g.c.g", "Không bằng nhau"], 0, "Hai cạnh và góc xen giữa."),
        q("Hai tam giác có hai cạnh bằng nhau và góc xen giữa bằng nhau thì:", ["Bằng nhau theo c.g.c", "Bằng nhau theo c.c.c", "Không bằng nhau", "Chưa đủ dữ kiện"], 0, "Đúng theo c.g.c."),
        q("Hai tam giác có hai góc và cạnh kề hai góc đó bằng nhau thì:", ["Bằng nhau theo g.c.g", "Bằng nhau theo c.c.c", "Không bằng nhau", "Chưa đủ dữ kiện"], 0, "Đúng theo g.c.g."),
        q("Luyện tập 1: ΔABC = ΔDEF, BC = 4 cm. Khi đó EF bằng:", ["4 cm", "2 cm", "8 cm", "Không xác định"], 0, "B ↔ E, C ↔ F nên EF = BC = 4 cm."),
        q("Luyện tập 1: ΔABC = ΔDEF, góc B = 40°, góc C = 60°. Góc EDF bằng:", ["80°", "40°", "60°", "100°"], 0, "A = 180° − 40° − 60° = 80° và D = A."),
        q("Ví dụ 2: ΔABC = ΔDEC theo:", ["g.c.g", "c.c.c", "c.g.c", "Không bằng nhau"], 0, "Có góc - cạnh - góc."),
        q("Lan nói: Nếu một cạnh và một góc kề cạnh đó của tam giác này bằng với tam giác kia thì bằng nhau. Nhận xét:", ["Chưa đủ, cần thêm góc kề thứ hai", "Đúng", "Sai hoàn toàn", "Đúng theo c.c.c"], 0, "Cần hai góc kề cạnh đó."),
        q("Hai tam giác có ba góc bằng nhau từng đôi thì:", ["Có thể không bằng nhau", "Chắc chắn bằng nhau", "Chắc chắn có ba cạnh bằng nhau", "Có diện tích bằng nhau"], 0, "Ba góc bằng nhau chưa đủ."),
        q("Hai tam giác có hai cạnh bằng nhau nhưng góc không xen giữa bằng nhau thì:", ["Chưa chắc bằng nhau", "Chắc chắn bằng nhau theo c.g.c", "Chắc chắn không bằng nhau", "Bằng nhau theo g.c.g"], 0, "Không đúng hình thức c.g.c."),
        q("Trong ΔABC = ΔDEF theo c.g.c, góc A tương ứng với:", ["Góc D", "Góc E", "Góc F", "Góc B"], 0, "A ↔ D."),
        q("Ví dụ 1 bài 14: góc xen giữa cạnh AB và AC là:", ["Góc A", "Góc B", "Góc C", "Góc ngoài"], 0, "Góc giữa hai cạnh AB, AC."),
        q("Hình 4.36: BAC = EDC, AC = DC, BCA = ECD (đối đỉnh). Tam giác ABC = DEC theo:", ["g.c.g", "c.c.c", "c.g.c", "Chưa đủ"], 0, "Hai góc và cạnh kề."),
        q("Nếu ΔABC = ΔDEF theo g.c.g thì cạnh chung là:", ["Một cạnh kề góc đã biết", "Cạnh đối diện góc", "Một cạnh bất kì", "Không có cạnh"], 0, "Cạnh nằm giữa hai góc."),
        q("Hai tam giác có hai cạnh bằng nhau và góc xen giữa bằng nhau. Yếu tố này gọi là:", ["c.g.c", "c.c.c", "g.c.g", "c.h.c"], 0, "c.g.c."),
        q("Hai tam giác ABC và DEF có AB = DE, góc A = góc D, góc B = góc E. Trường hợp bằng nhau là:", ["g.c.g", "c.c.c", "c.g.c", "Không bằng nhau"], 0, "Một cạnh AB và hai góc kề cạnh đó."),
        q("Hai tam giác có góc A = 60°, AB = AC và góc B = 60° thì:", ["Là tam giác đều", "Là tam giác vuông", "Là tam giác tù", "Không xác định"], 0, "Ba góc bằng nhau, tam giác đều."),
        q("Hai tam giác ABC và DEF có AB = DE, góc A = góc D, AC = DF. Theo đó:", ["ΔABC = ΔDEF (c.g.c)", "ΔABC = ΔFED", "ΔABC = ΔEDF", "Không bằng nhau"], 0, "Hai cạnh và góc xen giữa."),
        q("Trong trường hợp c.g.c, góc phải là góc:", ["Xen giữa hai cạnh bằng nhau", "Đối diện một cạnh", "Bất kì", "Ngoài tam giác"], 0, "Góc xen giữa."),
        q("Trong trường hợp g.c.g, các góc phải là:", ["Hai góc kề cạnh bằng nhau", "Hai góc đối diện", "Hai góc ngoài", "Hai góc bất kì"], 0, "Hai góc kề cạnh."),
        q("Tam giác ABC và A'B'C' có AB = A'B', góc A = góc A', góc B = góc B'. Theo g.c.g thì:", ["ΔABC = ΔA'B'C'", "Không bằng nhau", "Chỉ bằng nhau nếu AC = A'C'", "Bằng nhau theo c.c.c"], 0, "Một cạnh và hai góc kề cạnh đó."),
        q("Bạn Lan nói: 'Nếu một cạnh, một góc kề cạnh đó và góc đối diện cạnh đó của tam giác này bằng với tam giác kia thì hai tam giác bằng nhau.' Nhận xét đúng là:", ["Đúng, vì góc còn lại suy ra được", "Sai hoàn toàn", "Không xác định", "Chỉ đúng khi là tam giác vuông"], 0, "Ba góc của tam giác được xác định khi biết hai góc, nên có thể suy ra các cạnh còn lại bằng nhau."),
        q("Tam giác có ba cạnh bằng nhau thì ba góc của nó:", ["Bằng nhau", "Khác nhau", "Có một góc vuông", "Có một góc tù"], 0, "Tam giác đều có ba góc bằng 60°."),
        q("Hai tam giác có cạnh chung và hai góc kề cạnh chung đó bằng nhau. Khẳng định:", ["Hai tam giác bằng nhau theo g.c.g", "Hai tam giác bằng nhau theo c.c.c", "Hai tam giác không bằng nhau", "Hai tam giác vuông"], 0, "Đây là g.c.g."),
        q("Hai tam giác có hai cạnh và góc xen giữa bằng nhau: các cạnh còn lại:", ["Bằng nhau", "Khác nhau", "Vuông góc", "Song song"], 0, "Theo định nghĩa hai tam giác bằng nhau."),
        q("Trong ΔABC = ΔDEF theo g.c.g, cạnh AB tương ứng với:", ["DE", "EF", "DF", "Không có"], 0, "A ↔ D, B ↔ E."),
        q("Hai tam giác có cạnh chung AC và hai góc kề AC bằng nhau từng đôi. Trường hợp bằng nhau là:", ["g.c.g", "c.c.c", "c.g.c", "Không bằng nhau"], 0, "Một cạnh và hai góc kề cạnh đó."),
    ],
    bt_co_ban=[
        bt("Cho ΔABC = ΔDEF theo c.g.c với AB = DE, góc A = góc D, AC = DF. Chứng minh hai tam giác bằng nhau theo trường hợp nào?", ["c.g.c"], "Hai cạnh và góc xen giữa."),
        bt("Cho ΔABC = ΔDEF. BC = 4 cm. Tính EF.", ["4 cm", "4"], "Cạnh tương ứng bằng nhau."),
        bt("Cho ΔABC = ΔDEF với góc B = 40°, C = 60°. Tính góc D.", ["80°", "80"], "A = 80°, D = A."),
        bt("Cho ΔABC = ΔDEC theo g.c.g với AC = DC. Tính độ dài cạnh tương ứng với AC.", ["AC = DC"], "Cạnh bằng nhau."),
        bt("Cho ΔABC và ΔDEF có AB = DE, góc B = góc E, BC = EF. Hai tam giác bằng nhau theo trường hợp nào?", ["c.g.c"], "Hai cạnh và góc xen giữa là góc B."),
    ],
    bt_nang_cao=[
        nc("Cho ΔABC và ΔDEF có AB = DE, AC = DF, góc BAC = 60° = góc EDF. Tính EF khi BC = 6 cm.", "Áp dụng c.g.c.", ["6 cm", "6"], "Hai tam giác bằng nhau nên EF = BC = 6 cm."),
        nc("Cho ΔABC và ΔDEF có AB = DE, góc B = góc E = 70°, góc A = góc D = 60°, AC = 6 cm. Tính DF.", "Áp dụng g.c.g.", ["6 cm", "6"], "Hai tam giác bằng nhau theo g.c.g nên DF = AC = 6 cm."),
        nc("Cho đoạn AB và điểm C. Chứng minh hai tam giác ADE và BCE bằng nhau khi AE = BE, góc A = góc B và góc AED = góc BEC.", "Áp dụng g.c.g.", ["g.c.g"], "Có một cạnh và hai góc kề cạnh đó bằng nhau."),
    ],
)


# ============================================================
# BÀI 15: CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG
# ============================================================
B15 = bai(
    ly_thuyet="""📌 1. CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG
- Hai cạnh góc vuông tương ứng bằng nhau: hai tam giác vuông bằng nhau (c.g.c).
- Một cạnh góc vuông và góc nhọn kề cạnh ấy bằng nhau: hai tam giác vuông bằng nhau (g.c.g).
- Cạnh huyền và một cạnh góc vuông bằng nhau: hai tam giác vuông bằng nhau (cạnh huyền - cạnh góc vuông).
- Cạnh huyền và một góc nhọn bằng nhau: hai tam giác vuông bằng nhau (cạnh huyền - góc nhọn).
""",
    vi_du="""Ví dụ 1: Hai tam giác vuông BAC (vuông tại B) và DAC (vuông tại D) có AC chung và góc BAC = góc DAC. Theo cạnh huyền - góc nhọn: ΔBAC = ΔDAC.

Ví dụ 2: Tam giác ABC vuông tại B và ADC vuông tại D, AB = AD. Theo cạnh huyền - cạnh góc vuông: ΔABC = ΔADC.

Luyện tập 2: MA vuông góc Ox, MB vuông góc Oy, Oz là tia phân giác góc xOy thì MA = MB.""",
    cau_hoi=[
        q("Hai tam giác vuông bằng nhau nếu:", ["Hai cạnh góc vuông tương ứng bằng nhau", "Có một góc bằng nhau", "Có diện tích bằng nhau", "Có chu vi bằng nhau"], 0, "Trường hợp c.g.c của tam giác vuông."),
        q("Hai tam giác vuông có một cạnh góc vuông và góc nhọn kề cạnh ấy bằng nhau thì:", ["Bằng nhau", "Không bằng nhau", "Chưa đủ dữ kiện", "Chỉ đồng dạng"], 0, "Trường hợp g.c.g."),
        q("Hai tam giác vuông có cạnh huyền và một cạnh góc vuông bằng nhau thì:", ["Bằng nhau", "Không bằng nhau", "Chỉ bằng khi có góc nhọn", "Chưa đủ"], 0, "Trường hợp cạnh huyền - cạnh góc vuông."),
        q("Hai tam giác vuông có cạnh huyền và góc nhọn bằng nhau thì:", ["Bằng nhau", "Không bằng nhau", "Chỉ đồng dạng", "Chưa đủ"], 0, "Trường hợp cạnh huyền - góc nhọn."),
        q("Ví dụ 1: ΔBAC và ΔDAC có AC chung, góc BAC = góc DAC. Trường hợp bằng nhau là:", ["Cạnh huyền - góc nhọn", "c.c.c", "c.g.c", "g.c.g"], 0, "Cạnh AC là cạnh huyền và góc A là góc nhọn."),
        q("Ví dụ 2: ΔABC vuông tại B, ΔADC vuông tại D, AB = AD và AC chung. Trường hợp là:", ["Cạnh huyền - cạnh góc vuông", "c.c.c", "c.g.c", "g.c.g"], 0, "AC là cạnh huyền chung."),
        q("Luyện tập 2: Oz là tia phân giác góc xOy, MA ⊥ Ox, MB ⊥ Oy thì:", ["MA = MB", "MA > MB", "MA < MB", "MA = 2MB"], 0, "Theo tính chất tia phân giác và trường hợp cạnh huyền - góc nhọn."),
        q("Hình 4.45: AB = A'B', AC = A'C'. Hai tam giác vuông ABC và A'B'C' bằng nhau theo:", ["c.g.c (hai cạnh góc vuông)", "c.c.c", "g.c.g", "Không bằng nhau"], 0, "Hai cạnh góc vuông tương ứng bằng nhau."),
        q("Hình 4.47: BC = B'C', góc B = góc B'. Hai tam giác vuông ABC và A'B'C' bằng nhau theo:", ["Cạnh huyền - góc nhọn", "c.c.c", "c.g.c", "Không bằng nhau"], 0, "BC là cạnh huyền."),
        q("Hai tam giác vuông có cạnh huyền 5 cm và cạnh góc vuông 3 cm bằng nhau khi hai tam giác kia có:", ["Cạnh huyền 5 cm và cạnh góc vuông 3 cm", "Cạnh huyền 4 cm", "Hai cạnh góc vuông 3 cm và 5 cm", "Không đủ"], 0, "Cạnh huyền và một cạnh góc vuông."),
        q("Hai con dốc có cạnh góc vuông tương ứng bằng nhau và hai góc nhọn kề cạnh đó bằng nhau thì:", ["Độ cao hai con dốc bằng nhau", "Độ cao khác nhau", "Không so sánh được", "Độ cao bằng 0"], 0, "Hai tam giác vuông bằng nhau."),
        q("Trong trường hợp cạnh huyền - góc nhọn, góc nhọn phải là:", ["Góc nhọn của tam giác vuông", "Góc vuông", "Góc tù", "Góc ngoài"], 0, "Góc nhọn trong tam giác vuông."),
        q("Trong trường hợp c.g.c của tam giác vuông, góc xen giữa hai cạnh là:", ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0, "Góc vuông nằm giữa hai cạnh góc vuông."),
        q("Hai tam giác vuông có hai góc nhọn bằng nhau từng đôi. Hai tam giác đó:", ["Chưa chắc bằng nhau", "Chắc chắn bằng nhau", "Chắc chắn không bằng nhau", "Có cạnh huyền bằng nhau"], 0, "Cần thêm một cạnh tương ứng bằng nhau."),
        q("Hình 4.48: tìm cặp tam giác vuông bằng nhau. Ta cần:", ["Kiểm tra theo ba trường hợp của tam giác vuông", "Đo diện tích", "Đếm đỉnh", "Đoán"], 0, "Áp dụng các trường hợp bằng nhau."),
        q("Hai tam giác vuông ABC và DEF có AB = DE, BC = EF thì:", ["ΔABC = ΔDEF (cạnh huyền - cạnh góc vuông)", "Không bằng nhau", "Chỉ đồng dạng", "Chưa đủ"], 0, "Nếu BC là cạnh huyền."),
        q("Hai tam giác vuông ABC (vuông tại A) và DEF (vuông tại D) có AB = DE, AC = DF. Khi đó:", ["ΔABC = ΔDEF (c.g.c)", "ΔABC = ΔDFE", "Không bằng nhau", "Chưa đủ"], 0, "Hai cạnh góc vuông."),
        q("Hình 4.49: AB ⊥ BC, AD ⊥ CD, góc BAC = góc DAC. Suy ra:", ["ΔBAC = ΔDAC (cạnh huyền - góc nhọn)", "ΔBAC = ΔDCA", "Không bằng nhau", "Chưa đủ"], 0, "AC là cạnh huyền chung."),
        q("Trong Ví dụ 1 (hình 4.49), AC vuông góc với BD tại E vì:", ["BEA = DEA = 90°", "AB = AD", "BC = CD", "Không đủ"], 0, "Hai tam giác BAE và DAE bằng nhau nên góc BEA = DEA và cộng lại bằng 180°."),
        q("Hai tam giác vuông bằng nhau theo cạnh huyền - góc nhọn thì:", ["Các cạnh góc vuông tương ứng bằng nhau", "Các góc khác nhau", "Diện tích khác nhau", "Không có điều kiện"], 0, "Các phần tử tương ứng bằng nhau."),
        q("Hai tam giác vuông có một góc nhọn bằng nhau và cạnh huyền bằng nhau thì:", ["Bằng nhau", "Có diện tích khác nhau", "Không bằng nhau", "Chưa đủ"], 0, "Cạnh huyền - góc nhọn."),
        q("Hai tam giác vuông có hai cạnh góc vuông tương ứng bằng nhau thì:", ["Cạnh huyền bằng nhau", "Cạnh huyền khác nhau", "Góc nhọn khác nhau", "Không có điều kiện"], 0, "Theo định lí Pythagoras hoặc c.g.c."),
        q("Hai tam giác vuông bằng nhau theo trường hợp nào nếu cạnh góc vuông và góc nhọn kề bằng nhau:", ["g.c.g", "c.c.c", "c.g.c", "c.h.c"], 0, "Có một cạnh và hai góc kề, một góc là góc vuông."),
        q("Hai tam giác vuông có cạnh huyền bằng nhau và một góc nhọn bằng nhau. Chúng bằng nhau theo:", ["Cạnh huyền - góc nhọn", "c.c.c", "c.g.c với góc vuông", "Không bằng nhau"], 0, "Đây là trường hợp cạnh huyền - góc nhọn."),
        q("Hai tam giác vuông có hai cạnh góc vuông tương ứng bằng nhau. Trường hợp là:", ["c.g.c (góc vuông xen giữa)", "c.c.c", "g.c.g", "Không bằng nhau"], 0, "Góc vuông là góc xen giữa hai cạnh góc vuông."),
        q("Tam giác vuông ABC có góc vuông tại A. Cạnh huyền là:", ["BC", "AB", "AC", "Không có"], 0, "Cạnh huyền đối diện góc vuông."),
        q("Hai tam giác vuông bằng nhau khi có một cạnh góc vuông và cạnh huyền bằng nhau, tức là:", ["Cạnh huyền - cạnh góc vuông", "Hai góc nhọn", "Ba góc bằng nhau", "Chu vi bằng nhau"], 0, "Đây là trường hợp cạnh huyền - cạnh góc vuông."),
        q("Hai tam giác vuông có cạnh huyền và cạnh góc vuông bằng nhau (cạnh huyền - cạnh góc vuông) thì:", ["Bằng nhau", "Có góc khác", "Không bằng", "Có đường cao khác"], 0, "Theo trường hợp cạnh huyền - cạnh góc vuông."),
        q("Trong Hình 4.54 (đường tròn tâm O), ba tam giác vuông bằng nhau được chỉ ra nhờ:", ["Cạnh huyền là bán kính và cạnh góc vuông", "Diện tích", "Chu vi", "Không có"], 0, "Bán kính là cạnh huyền chung."),
        q("Nếu ΔABC vuông tại A và ΔA'B'C' vuông tại A' có AB = A'B', góc B = góc B' thì:", ["ΔABC = ΔA'B'C' (g.c.g)", "Không bằng nhau", "Chỉ đồng dạng", "Chưa đủ"], 0, "Một cạnh góc vuông và góc nhọn kề."),
    ],
    bt_co_ban=[
        bt("Hai tam giác vuông ABC và DEF có AB = DE, AC = DF. Hai tam giác bằng nhau theo trường hợp nào?", ["c.g.c"], "Hai cạnh góc vuông tương ứng."),
        bt("Hai tam giác vuông có cạnh huyền BC = EF và góc B = góc E. Hai tam giác bằng nhau theo trường hợp nào?", ["cạnh huyền - góc nhọn"], "Cạnh huyền và góc nhọn."),
        bt("Hai tam giác vuông đều có cạnh huyền 5 cm và một cạnh góc vuông 3 cm (tương ứng từng đôi). Chúng có bằng nhau không?", ["có", "Có"], "Cạnh huyền - cạnh góc vuông."),
        bt("Cho tam giác ABC vuông tại A, DEF vuông tại D. AB = DE, góc B = góc E. Tam giác có bằng nhau không?", ["có", "Có"], "Cạnh góc vuông và góc nhọn kề."),
    ],
    bt_nang_cao=[
        nc("Hình 4.49: AB ⊥ BC, AD ⊥ CD, góc BAC = góc DAC. Chứng minh AC ⊥ BD tại E.", "Chứng minh ΔBAE = ΔDAE rồi dùng kề bù.", ["AC vuông góc BD"], "ΔBAE = ΔDAE (c.g.c) nên góc BEA = DEA = 90°."),
        nc("Hai chiếc thang dài như nhau dựa vào tường, cùng độ cao BH = B'H'. Góc BAH và góc B'A'H' có bằng nhau không?", "Xét hai tam giác vuông ABH và A'B'H'.", ["có"], "Hai tam giác vuông bằng nhau theo cạnh huyền - cạnh góc vuông nên góc tương ứng bằng nhau."),
        nc("Cho đường tròn tâm O, dây cung BC, điểm A trên đường tròn; kẻ OM ⊥ BC. Chứng minh hai tam giác vuông OMB và OMC bằng nhau.", "Dùng cạnh huyền OB = OC và cạnh OM chung.", ["cạnh huyền - cạnh góc vuông"], "OB = OC (bán kính), OM chung nên bằng nhau."),
    ],
)


# ============================================================
# BÀI 16: TAM GIÁC CÂN. ĐƯỜNG TRUNG TRỰC CỦA ĐOẠN THẲNG
# ============================================================
B16 = bai(
    ly_thuyet="""📌 1. TAM GIÁC CÂN
- Tam giác cân là tam giác có hai cạnh bằng nhau.
- Trong tam giác cân ABC (AB = AC): A là đỉnh, AB và AC là hai cạnh bên, BC là cạnh đáy, B và C là hai góc ở đáy.
- Tính chất: trong tam giác cân, hai góc ở đáy bằng nhau. Ngược lại, tam giác có hai góc bằng nhau là tam giác cân.
- Tam giác đều là tam giác có ba cạnh bằng nhau; mỗi góc bằng 60°.

📌 2. ĐƯỜNG TRUNG TRỰC CỦA ĐOẠN THẲNG
- Đường thẳng vuông góc với một đoạn thẳng tại trung điểm của nó gọi là đường trung trực của đoạn thẳng đó.
- Điểm nằm trên đường trung trực của một đoạn thẳng thì cách đều hai mút của đoạn thẳng đó.
- Đường trung trực của đoạn thẳng là tập hợp các điểm cách đều hai mút của đoạn thẳng.
""",
    vi_du="""Ví dụ: Cho đoạn AB và điểm M không thuộc AB sao cho MA = MB. Gọi O là trung điểm AB. Ta có ΔOMA = ΔOMB (c.c.c), suy ra góc AOM = góc BOM = 90°, do đó MO là đường trung trực của AB.

Tính chất tam giác cân: Tam giác ABC cân tại A có góc A = 40° thì góc B = góc C = (180° − 40°) : 2 = 70°.""",
    cau_hoi=[
        q("Tam giác cân là tam giác có:", ["Hai cạnh bằng nhau", "Ba cạnh bằng nhau", "Hai góc vuông", "Một góc tù"], 0, "Định nghĩa tam giác cân."),
        q("Tam giác ABC cân tại A (AB = AC). Hai góc ở đáy là:", ["B và C", "A và B", "A và C", "B và A"], 0, "Đáy là BC nên góc đáy là B và C."),
        q("Trong tam giác cân ABC (AB = AC), góc B và góc C:", ["Bằng nhau", "Bù nhau", "Phụ nhau", "Khác nhau"], 0, "Hai góc ở đáy bằng nhau."),
        q("Tam giác cân có góc đỉnh 40°. Góc đáy bằng:", ["70°", "40°", "140°", "50°"], 0, "(180° − 40°) : 2 = 70°."),
        q("Tam giác cân có góc đáy 50°. Góc đỉnh bằng:", ["80°", "50°", "100°", "130°"], 0, "180° − 2·50° = 80°."),
        q("Tam giác đều có các góc bằng:", ["60°", "90°", "45°", "120°"], 0, "180° : 3 = 60°."),
        q("Tam giác cân có một góc 60° thì là tam giác:", ["Đều", "Vuông", "Tù", "Nhọn không đều"], 0, "Hai góc đáy bằng nhau và tổng 180° nên đều."),
        q("Đường trung trực của đoạn thẳng AB là đường thẳng:", ["Vuông góc với AB tại trung điểm của AB", "Song song với AB", "Đi qua A", "Cắt AB tại A"], 0, "Định nghĩa đường trung trực."),
        q("Điểm nằm trên đường trung trực của đoạn AB thì:", ["Cách đều A và B", "Trùng A", "Trùng B", "Bằng nhau về góc"], 0, "Tính chất đường trung trực."),
        q("Nếu MA = MB thì điểm M thuộc:", ["Đường trung trực của AB", "Đường thẳng AB", "Đường tròn tâm A", "Tia AB"], 0, "Điểm cách đều hai mút."),
        q("Trong tam giác cân ABC (AB = AC), đường trung tuyến kẻ từ A cũng là:", ["Đường cao và đường phân giác", "Đường tròn", "Đường thẳng song song", "Không liên quan"], 0, "Tính chất tam giác cân."),
        q("Tam giác có hai góc bằng nhau là tam giác:", ["Cân", "Vuông", "Đều", "Tù"], 0, "Dấu hiệu nhận biết tam giác cân."),
        q("Tam giác DEF có DE = DF = 4 cm, EF = 4 cm. Tam giác DEF là:", ["Tam giác đều", "Tam giác vuông", "Tam giác tù", "Tam giác thường"], 0, "Ba cạnh bằng nhau."),
        q("Tam giác cân có cạnh bên 4 cm và cạnh đáy 4 cm thì:", ["Là tam giác đều", "Là tam giác vuông", "Là tam giác tù", "Không xác định"], 0, "Ba cạnh bằng nhau."),
        q("Đường trung trực của một đoạn thẳng là:", ["Trục đối xứng của đoạn thẳng", "Đoạn thẳng khác", "Tia", "Điểm"], 0, "Nhận xét trong bài."),
        q("Ví dụ: MA = MB, M không thuộc AB. Kết luận:", ["M thuộc đường trung trực của AB", "M thuộc AB", "M cách A một khoảng khác B", "Không có kết luận"], 0, "Chứng minh trong ví dụ."),
        q("Luyện tập 2: M nằm trên đường trung trực của AB, AM = 3 cm. Khi đó BM bằng:", ["3 cm", "6 cm", "1,5 cm", "Không xác định"], 0, "Điểm trên đường trung trực cách đều hai mút."),
        q("Luyện tập 2: góc MAB = 60°, M nằm trên đường trung trực, tam giác MAB là:", ["Tam giác đều", "Tam giác vuông", "Tam giác tù", "Tam giác nhọn không cân"], 0, "Tam giác cân có góc 60° là tam giác đều."),
        q("Trong hình 4.64, Lan vẽ đường trung trực đúng là hình:", ["a", "b", "c", "Không hình nào"], 0, "Đường vuông góc tại trung điểm AB."),
        q("Tam giác cân có góc đỉnh là góc tù thì góc đáy:", ["Là góc nhọn", "Là góc tù", "Là góc vuông", "Là góc bẹt"], 0, "Hai góc đáy nhọn vì tổng 180°."),
        q("Tam giác đều cạnh 5 cm có chu vi:", ["15 cm", "10 cm", "20 cm", "25 cm"], 0, "3 · 5 = 15 cm."),
        q("Tam giác ABC cân tại A, D là trung điểm BC. Khi đó:", ["AD ⊥ BC", "AD song song BC", "AD trùng AB", "AD bằng BC"], 0, "Đường trung tuyến của tam giác cân ứng với đáy là đường cao."),
        q("Tam giác có ba góc bằng nhau là tam giác:", ["Đều", "Vuông", "Tù", "Cân không đều"], 0, "Ba góc 60° nên đều."),
        q("Tam giác cân có góc đỉnh 90° là tam giác:", ["Vuông cân", "Đều", "Tù", "Nhọn"], 0, "Tam giác vuông cân."),
        q("Tam giác cân ABC có góc A = 100°. Góc B bằng:", ["40°", "100°", "80°", "50°"], 0, "(180° − 100°) : 2 = 40°."),
        q("Trong một tam giác cân, đường cao kẻ từ đỉnh cũng là:", ["Đường trung tuyến", "Đường tròn", "Cạnh bên", "Đường thẳng song song"], 0, "Tính chất tam giác cân."),
        q("Khẳng định đúng: mỗi tam giác đều là tam giác cân vì:", ["Có hai cạnh bằng nhau", "Có góc vuông", "Có góc tù", "Không đúng"], 0, "Tam giác đều có ba cạnh bằng nhau nên có hai cạnh bằng nhau."),
        q("Trong Luyện tập 1: tam giác DEF có DE = DF = 4 cm và EF = 4 cm, góc E = 60°. Số đo các góc còn lại là:", ["60° và 60°", "40° và 80°", "90° và 30°", "45° và 45°"], 0, "Tam giác đều."),
        q("Điểm O là trung điểm của AB. Đường trung trực của AB đi qua:", ["Điểm O", "Điểm A", "Điểm B", "Không điểm nào"], 0, "Đường trung trực đi qua trung điểm."),
        q("Đường trung trực của đoạn AB là tập hợp các điểm:", ["Cách đều hai mút A và B", "Thuộc đường thẳng AB", "Cách A một khoảng 1 cm", "Trùng với B"], 0, "Đây là tính chất của đường trung trực."),
    ],
    bt_co_ban=[
        bt("Tam giác cân ABC có A = 40°. Tính góc B.", ["70°", "70"], "(180° − 40°) : 2 = 70°."),
        bt("Tam giác cân có góc đáy 50°. Tính góc đỉnh.", ["80°", "80"], "180° − 2·50° = 80°."),
        bt("Tam giác đều có cạnh 5 cm. Tính chu vi.", ["15 cm", "15"], "3 · 5 = 15 cm."),
        bt("Luyện tập 2: M nằm trên đường trung trực của AB, AM = 3 cm. Tính BM.", ["3 cm", "3"], "M cách đều A và B."),
        bt("Tam giác DEF có DE = DF = EF = 4 cm. Số đo mỗi góc là bao nhiêu?", ["60°", "60"], "Tam giác đều."),
    ],
    bt_nang_cao=[
        nc("Tam giác ABC có góc B = góc C. Chứng minh tam giác ABC cân.", "Dùng dấu hiệu tam giác cân.", ["ΔABC cân tại A"], "Tam giác có hai góc bằng nhau nên là tam giác cân."),
        nc("Tam giác cân ABC có AB = AC = 5 cm, BC = 6 cm. Tính chu vi tam giác.", "Cộng ba cạnh.", ["16 cm", "16"], "5 + 5 + 6 = 16 cm."),
        nc("Tam giác ABC cân tại A, D là trung điểm BC. Chứng minh AD ⊥ BC.", "Dùng hai tam giác ABD và ACD bằng nhau (c.c.c).", ["AD ⊥ BC"], "ΔABD = ΔACD (c.c.c) nên góc ADB = góc ADC = 90°."),
    ],
)


CHUONG_4 = {
    "Chương IV: Tam giác bằng nhau": {
        "Bài 12: Tổng các góc trong một tam giác": B12,
        "Bài 13: Hai tam giác bằng nhau. Trường hợp bằng nhau cạnh - cạnh - cạnh": B13,
        "Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác": B14,
        "Bài 15: Các trường hợp bằng nhau của tam giác vuông": B15,
        "Bài 16: Tam giác cân. Đường trung trực của đoạn thẳng": B16,
    }
}

# ============================================================
# FILE toan_c5.py
# ============================================================
# ============================================================
# BÀI 17: THU THẬP VÀ PHÂN LOẠI DỮ LIỆU
# ============================================================
B17 = bai(
    ly_thuyet="""📌 1. DỮ LIỆU LÀ SỐ VÀ DỮ LIỆU KHÔNG LÀ SỐ
- Dữ liệu là số (dữ liệu định lượng): các giá trị là số, ví dụ: cân nặng, chiều cao, số con trong gia đình, điểm kiểm tra.
- Dữ liệu không là số (dữ liệu định tính): các giá trị là tên gọi, loại, mức độ, ví dụ: tên tỉnh thành, môn thể thao yêu thích, nhóm máu.
  + Dữ liệu không là số có thể sắp thứ tự (ví dụ: Trung bình < Khá < Tốt < Xuất sắc; Rất thích > Thích > Không thích).
  + Dữ liệu không là số không thể sắp thứ tự (ví dụ: tên các tỉnh: Nam Định, Thái Bình, Hưng Yên, Bắc Ninh).

📌 2. THU THẬP DỮ LIỆU
- Có thể thu thập dữ liệu bằng: quan sát, phỏng vấn, điều tra bằng phiếu hỏi, đo đạc, đọc tài liệu/báo cáo.
- Để đưa ra kết luận hợp lí, dữ liệu thu được phải đảm bảo tính đại diện cho toàn bộ đối tượng đang được quan tâm.
- Muốn có tính đại diện: không chỉ lấy ý kiến của một nhóm (chỉ nam, chỉ một câu lạc bộ, chỉ người quen), mà phải lấy mẫu ngẫu nhiên từ toàn bộ đối tượng.
- Kết luận dựa trên mẫu không đại diện thường không hợp lí.""",
    vi_du="""Ví dụ 1: Cân nặng (43; 41; 48; 45; 52) là dữ liệu số. Tên các tỉnh Nam Định, Thái Bình, Hưng Yên, Bắc Ninh là dữ liệu không là số, không sắp thứ tự. Đánh giá Tốt, Xuất sắc, Khá, Trung bình là dữ liệu không là số, có thể sắp thứ tự.

Ví dụ 2: Để đánh giá mức độ hài lòng của hành khách trên một chuyến bay, cách hợp lí là đánh số ngẫu nhiên 100 hành khách rồi hỏi những người được chọn (số 5; 10; 15; …), vì nó đại diện cho cả hạng thương gia và hạng phổ thông. Lấy 20 hành khách hạng thương gia là không đại diện.

Ví dụ 3: Khảo sát 100 người bệnh ở độ tuổi 20–30 cho thấy 95% khỏi bệnh, nhưng không thể kết luận cho mọi người dùng vì đối tượng khảo sát không đại diện cho các độ tuổi khác nhau.""",
    cau_hoi=[
        q("Dữ liệu 'chiều cao của học sinh lớp 7A' thuộc loại nào?",
          ["Dữ liệu số (định lượng)", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Không phải dữ liệu"], 0,
          "Chiều cao là một số đo."),
        q("Dữ liệu 'màu sắc yêu thích' (đỏ, xanh, vàng) thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Dữ liệu số có thứ tự"], 1,
          "Các màu không là số và không thể sắp theo thứ tự tự nhiên."),
        q("Dữ liệu 'xếp loại học lực: Giỏi, Khá, Trung bình' thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Không phải dữ liệu"], 2,
          "Các xếp loại không là số nhưng có thể sắp theo mức độ: Giỏi > Khá > Trung bình."),
        q("Dữ liệu 'số con trong mỗi gia đình' thuộc loại nào?",
          ["Dữ liệu số (định lượng)", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Không phải dữ liệu"], 0,
          "Số con là một số đếm được."),
        q("Dữ liệu 'tên các tỉnh: Nam Định, Thái Bình, Hưng Yên, Bắc Ninh' thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Dữ liệu số có thứ tự"], 1,
          "Đây là tên gọi, không là số và không sắp thứ tự được."),
        q("Dữ liệu 'mức độ hài lòng: Rất hài lòng, Hài lòng, Không hài lòng' thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Không phải dữ liệu"], 2,
          "Mức độ hài lòng có thể sắp theo thứ tự từ cao xuống thấp."),
        q("Dữ liệu 'nhóm máu (A, B, AB, O)' thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Dữ liệu số có thứ tự"], 1,
          "Các nhóm máu là tên gọi, không sắp thứ tự."),
        q("Dữ liệu 'cỡ áo (S, M, L, XL)' thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Không phải dữ liệu"], 2,
          "Cỡ áo không là số nhưng có thứ tự từ nhỏ đến lớn."),
        q("Dữ liệu 'số học sinh đạt điểm 9 trở lên' thuộc loại nào?",
          ["Dữ liệu số (định lượng)", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Không phải dữ liệu"], 0,
          "Đây là một số đếm được."),
        q("Dữ liệu 'môn thể thao yêu thích' (bóng đá, bơi, cầu lông) thuộc loại nào?",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Dữ liệu số có thứ tự"], 1,
          "Tên các môn thể thao không là số và không sắp thứ tự."),
        q("Trong các loại dữ liệu sau, dữ liệu 'số lượt xem video' là:",
          ["Dữ liệu định tính", "Dữ liệu định lượng (là số)", "Dữ liệu không có giá trị", "Dữ liệu hình ảnh"], 1,
          "Số lượt xem là một số đếm được."),
        q("Dữ liệu định tính là dữ liệu:",
          ["Luôn là số", "Không phải là số", "Chỉ có thứ tự", "Là số lớn hơn 100"], 1,
          "Dữ liệu định tính là dữ liệu có giá trị là tên gọi, loại hoặc mức độ, không phải số."),
        q("Dữ liệu định lượng là:",
          ["Dữ liệu là số", "Dữ liệu là chữ", "Dữ liệu là hình ảnh", "Dữ liệu là âm thanh"], 0,
          "Dữ liệu định lượng là dữ liệu có giá trị là số."),
        q("Dữ liệu 'số ngày mưa trong tháng 7' là:",
          ["Dữ liệu không là số", "Dữ liệu số (định lượng)", "Dữ liệu không có thứ tự", "Không phải dữ liệu"], 1,
          "Số ngày mưa là một số đếm được."),
        q("Dữ liệu 'quốc tịch của du khách' là:",
          ["Dữ liệu số", "Dữ liệu không là số", "Dữ liệu số có thứ tự", "Dữ liệu đo được"], 1,
          "Quốc tịch là tên gọi, không phải số."),
        q("Phương pháp thu thập dữ liệu nào là điều tra bằng phiếu hỏi?",
          ["Ghi lại số lần một xe buýt đến bến trong một giờ", "Gửi phiếu hỏi cho các học sinh trong lớp và thu lại", "Đo chiều cao của một cây", "Quan sát học sinh chơi bóng"], 1,
          "Điều tra bằng phiếu hỏi là gửi phiếu cho đối tượng và thu lại câu trả lời."),
        q("Phương pháp thu thập dữ liệu nào là quan sát?",
          ["Đếm số xe qua một ngã tư trong 1 giờ", "Gửi phiếu hỏi về thói quen đọc sách", "Gọi điện phỏng vấn từng người", "Đọc báo cáo của cơ quan thống kê"], 0,
          "Quan sát là ghi nhận trực tiếp hiện tượng, ở đây là đếm xe."),
        q("Để có kết quả khách quan khi khảo sát, nên:",
          ["Hỏi những người thân quen nhất", "Chọn mẫu ngẫu nhiên, đại diện cho toàn bộ đối tượng", "Chỉ hỏi người lớn", "Chỉ hỏi những người giàu"], 1,
          "Mẫu ngẫu nhiên đại diện giúp kết luận chung hợp lí."),
        q("Một trường có 1 000 học sinh. Khảo sát chỉ những bạn nam trong trường về sở thích bóng đá, kết luận 'Đa phần học sinh thích bóng đá' có hợp lí không?",
          ["Hợp lí vì số người khảo sát đủ nhiều", "Không hợp lí vì chỉ khảo sát bạn nam, không đại diện cho cả trường", "Hợp lí vì bóng đá là môn phổ biến", "Hợp lí vì có 50 bạn được hỏi"], 1,
          "Mẫu chỉ gồm bạn nam nên không đại diện cho toàn bộ học sinh."),
        q("Trong khảo sát về tính đại diện, cách nào sau đây là hợp lí nhất để biết ý kiến học sinh khối 7?",
          ["Chỉ lấy ý kiến học sinh lớp 7A", "Chọn ngẫu nhiên học sinh ở các lớp của khối 7", "Chỉ lấy ý kiến học sinh đến sớm", "Chỉ lấy ý kiến học sinh trong câu lạc bộ Toán"], 1,
          "Chọn ngẫu nhiên ở nhiều lớp giúp mẫu đại diện cho cả khối."),
        q("Để kiểm tra 'Đa phần học sinh trong trường thuận tay phải', phương án phù hợp là:",
          ["Hỏi các bạn trong lớp mình", "Lập phiếu hỏi và gửi ngẫu nhiên đến học sinh các khối trong trường", "Chỉ hỏi các bạn thuận tay phải", "Quan sát 10 bạn ở sân trường"], 1,
          "Cần mẫu ngẫu nhiên trên toàn trường thì mới kết luận được cho cả trường."),
        q("Để kiểm tra 'Học sinh nam yêu thích các chương trình thể thao hơn các bạn nữ', nên:",
          ["Chỉ hỏi bạn nam", "Lập bảng hỏi và khảo sát ngẫu nhiên cả học sinh nam và nữ", "Chỉ hỏi bạn nữ", "Lấy ý kiến của một bạn duy nhất"], 1,
          "Cần khảo sát cả hai nhóm để so sánh."),
        q("Trong khảo sát 'Đánh giá mức độ phù hợp của đề thi thử môn Toán', phương án nào đảm bảo tính đại diện?",
          ["Chỉ hỏi các bạn trong câu lạc bộ Toán học", "Hỏi ngẫu nhiên học sinh trong toàn trường", "Chỉ hỏi giáo viên Toán", "Chỉ hỏi người đầu tiên đến lớp"], 1,
          "Đề thi dành cho toàn trường nên cần lấy ý kiến ngẫu nhiên từ toàn trường."),
        q("Bảng 'Mức độ yêu thích: Rất thích, Thích, Bình thường, Không thích' là dữ liệu:",
          ["Dữ liệu số", "Dữ liệu không là số, có thứ tự", "Dữ liệu không là số, không thứ tự", "Không phải dữ liệu"], 1,
          "Các mức độ không là số nhưng sắp được theo mức độ yêu thích."),
        q("Trong dữ liệu 'số anh chị em ruột của mỗi bạn: 0; 1; 2; 1; 3', dữ liệu thuộc loại:",
          ["Dữ liệu số (định lượng)", "Dữ liệu không là số", "Dữ liệu không thể sắp thứ tự", "Không phải dữ liệu"], 0,
          "Các giá trị là số đếm."),
        q("Dữ liệu 'loại phương tiện đến trường: xe đạp, xe máy, đi bộ' là:",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Dữ liệu đo lường"], 1,
          "Các phương tiện là tên gọi, không sắp thứ tự."),
        q("Có thể sắp thứ tự 'Trung bình, Khá, Tốt, Xuất sắc' không?",
          ["Có, sắp theo mức độ tăng dần", "Không, vì không là số", "Không, vì không có thứ tự", "Chỉ khi là số"], 0,
          "Các xếp loại không là số nhưng có thứ tự về mức độ."),
        q("Dữ liệu 'số học sinh tham gia câu lạc bộ, ví dụ 35' là:",
          ["Dữ liệu số (định lượng)", "Dữ liệu không là số", "Dữ liệu có thứ tự", "Không phải dữ liệu"], 0,
          "Đây là số lượng học sinh."),
        q("Dữ liệu 'tên bộ phim yêu thích' là:",
          ["Dữ liệu số", "Dữ liệu không là số", "Dữ liệu số có thứ tự", "Dữ liệu đo được"], 1,
          "Tên phim là tên gọi, không phải số."),
        q("Dữ liệu 'điểm kiểm tra Toán của học sinh' là:",
          ["Dữ liệu không là số", "Dữ liệu số (định lượng)", "Dữ liệu định tính không có thứ tự", "Không phải dữ liệu"], 1,
          "Điểm kiểm tra là số."),
        q("Dữ liệu 'mức độ đánh giá chất lượng bữa ăn: Tốt, Bình thường, Kém' là:",
          ["Dữ liệu số", "Dữ liệu không là số, không có thứ tự", "Dữ liệu không là số, có thứ tự", "Dữ liệu số có thứ tự"], 2,
          "Các mức Tốt > Bình thường > Kém có thứ tự."),
        q("Trong khảo sát 'số lượng sách mỗi học sinh đọc trong tháng', câu nào đúng?",
          ["Dữ liệu là định tính", "Dữ liệu là định lượng", "Dữ liệu không có thứ tự", "Không thu thập được"], 1,
          "Số lượng sách là số."),
        q("Hãng hàng không khảo sát 100 hành khách trên nhiều chuyến bay với cách chọn ngẫu nhiên. Đây là cách:",
          ["Không đại diện", "Đại diện cho toàn bộ hành khách", "Chỉ đại diện cho hạng thương gia", "Không đáng tin"], 1,
          "Chọn ngẫu nhiên trên nhiều chuyến bay giúp mẫu đại diện cho toàn bộ hành khách."),
        q("Quảng cáo thuốc dựa trên khảo sát 100 người 20–30 tuổi (95% khỏi bệnh) nên kết luận gì?",
          ["Kết luận đúng cho mọi người", "Kết luận không hợp lí vì mẫu không đại diện cho mọi độ tuổi", "Thuốc chắc chắn không hiệu quả", "Cần khảo sát 1 000 người trẻ tuổi"], 1,
          "Đối tượng khảo sát chỉ thuộc một độ tuổi nên không đại diện cho người dùng nói chung."),
    ],
    bt_co_ban=[
        bt("Dữ liệu 'Ca sĩ Việt Nam mà bạn thích nhất' có là số không? (trả lời 'có' hoặc 'không')",
           ["không", "Không"], "Tên ca sĩ không là số."),
        bt("Dữ liệu về mức độ đồng ý (Rất đồng ý, Đồng ý, Không đồng ý, Rất không đồng ý) có thể sắp thứ tự không? (trả lời 'có' hoặc 'không')",
           ["có", "Có"], "Có thể sắp từ 'Rất đồng ý' đến 'Rất không đồng ý'."),
        bt("Trong Ví dụ 1, tên các tỉnh Nam Định, Thái Bình, Hưng Yên, Bắc Ninh có sắp thứ tự được không? (trả lời 'có' hoặc 'không')",
           ["không", "Không"], "Đây là tên gọi nên không sắp thứ tự được."),
    ],
    bt_nang_cao=[
        nc("Ví dụ 3: Công ty đưa ra kết luận như trong quảng cáo có hợp lí không? (trả lời 'có' hoặc 'không')",
           "Xét đối tượng khảo sát có đại diện cho mọi người dùng không.",
           ["không", "Không"],
           "Đối tượng khảo sát chỉ gồm người từ 20 đến 30 tuổi, không đại diện cho toàn bộ người dùng."),
        nc("Tranh luận: Bạn muốn khảo sát thời gian sử dụng Internet vào hai ngày cuối tuần của học sinh. Cách 'chọn ngẫu nhiên một số bạn và gửi bảng hỏi đến bố mẹ' hay cách 'gửi phiếu hỏi đến các bạn trong câu lạc bộ Tin học' hợp lí hơn? (trả lời: cách 1 hoặc cách 2)",
           "Cách nào lấy được mẫu ngẫu nhiên, đại diện cho toàn trường?",
           ["cách 1", "Cách 1"],
           "Cách 1 chọn ngẫu nhiên học sinh trên toàn trường nên đại diện hơn; cách 2 chỉ lấy từ một câu lạc bộ nên không đại diện."),
    ],
)


# ============================================================
# BÀI 18: BIỂU ĐỒ HÌNH QUẠT TRÒN
# ============================================================
B18 = bai(
    ly_thuyet="""📌 1. BIỂU ĐỒ HÌNH QUẠT TRÒN LÀ GÌ
- Biểu đồ hình quạt tròn dùng để so sánh các phần trong toàn bộ dữ liệu.
- Phần chính là hình tròn, được chia thành nhiều hình quạt (thường được tô màu khác nhau).
- Mỗi hình quạt biểu diễn tỉ lệ của một phần so với toàn bộ dữ liệu.
- Cả hình tròn biểu diễn toàn bộ dữ liệu, tức là ứng với 100%.
- Các thành phần của biểu đồ: tiêu đề, hình tròn biểu diễn dữ liệu, chú giải (cho biết mỗi màu ứng với loại nào).

📌 2. ĐỌC BIỂU ĐỒ HÌNH QUẠT TRÒN
- Đọc tỉ lệ phần trăm ghi trên mỗi hình quạt.
- Tổng tỉ lệ của tất cả các hình quạt bằng 100%.
- Hình quạt càng lớn thì tỉ lệ càng lớn.
- Một hình quạt có góc bằng 1/4 hình tròn ứng với 25%; bằng nửa hình tròn ứng với 50%.

📌 3. VẼ BIỂU ĐỒ HÌNH QUẠT TRÒN
- Chuyển các số liệu thành tỉ lệ phần trăm trên tổng số liệu.
- Chia hình tròn thành các hình quạt tương ứng với tỉ lệ (có thể dùng hình tròn đã chia sẵn, mỗi hình quạt ứng với 10%, 5%,…).
- Tô màu và ghi chú giải, đặt tiêu đề cho biểu đồ.""",
    vi_du="""Ví dụ 1: Bảng tỉ lệ sách trong thư viện: sách giáo khoa 40%, sách tham khảo 20%, sách truyện 30%, sách khác 10%. Có thể biểu diễn bằng hình tròn với các hình quạt tương ứng 40%, 20%, 30%, 10%.

Ví dụ 2: Tổng số học sinh khảo sát là 250 + 175 + 75 = 500. Tỉ lệ bơi thành thạo: 250/500 = 50%; biết bơi nhưng chưa thành thạo: 175/500 = 35%; chưa biết bơi: 75/500 = 15%.

Ví dụ 3: Từ biểu đồ Hình 5.14 có thể lập bảng mức độ ảnh hưởng của các yếu tố đến chiều cao: vận động 20%, di truyền 23%, dinh dưỡng 32%, giấc ngủ và môi trường 16%, yếu tố khác 9%. Ngoài di truyền, ba yếu tố ảnh hưởng nhiều nhất là dinh dưỡng (32%), vận động (20%), giấc ngủ và môi trường (16%), tổng cộng 68%.

Ví dụ 4 (dự đoán): Trong Hình 5.16, 30% học sinh thích chơi thể thao. Với 200 học sinh khối 7, số bạn thích chơi thể thao là 200 · 30% = 60 học sinh.""",
    cau_hoi=[
        q("Biểu đồ hình quạt tròn dùng để:",
          ["So sánh các phần trong toàn bộ dữ liệu", "Biểu diễn sự thay đổi theo thời gian", "Biểu diễn từng điểm trên mặt phẳng toạ độ", "Biểu diễn đường thẳng song song"], 0,
          "Biểu đồ hình quạt tròn so sánh các phần trong toàn bộ."),
        q("Trong biểu đồ hình quạt tròn, cả hình tròn ứng với:",
          ["50%", "100%", "10%", "75%"], 1,
          "Cả hình tròn biểu diễn toàn bộ dữ liệu, tức 100%."),
        q("Trong Hình 5.4 (nguyên nhân gây tai nạn thương tích ở trẻ em), nguyên nhân chiếm tỉ lệ cao nhất là:",
          ["Tai nạn giao thông", "Đuối nước", "Ngã", "Ngộ độc"], 1,
          "Đuối nước chiếm 48%, cao nhất."),
        q("Trong Hình 5.4, tai nạn giao thông chiếm bao nhiêu phần trăm?",
          ["20%", "28%", "48%", "2%"], 1,
          "Tai nạn giao thông chiếm 28%."),
        q("Trong Hình 5.4, thương tích khác (không phân loại) chiếm bao nhiêu phần trăm?",
          ["2%", "20%", "28%", "48%"], 1,
          "Thương tích khác chiếm 20%."),
        q("Tổng tỉ lệ các nguyên nhân trong Hình 5.4 bằng:",
          ["90%", "100%", "110%", "80%"], 1,
          "48% + 28% + 2% + 2% + 20% = 100%."),
        q("Trong Hình 5.6 (huy chương cuộc thi), hai loại nào có cùng tỉ lệ thí sinh được trao?",
          ["Vàng và bạc", "Bạc và đồng", "Vàng và đồng", "Đồng và không có huy chương"], 1,
          "Huy chương bạc và đồng đều chiếm 20%."),
        q("Trong Hình 5.6, số thí sinh không có huy chương chiếm bao nhiêu phần trăm?",
          ["20%", "50%", "10%", "40%"], 1,
          "Phần hình quạt không có huy chương chiếm 50%, tức là một nửa hình tròn."),
        q("Hình 5.7 (tỉ lệ các loại kem bán được) được chia thành mấy hình quạt?",
          ["3", "4", "5", "6"], 1,
          "Có 4 hình quạt ứng với 4 loại kem."),
        q("Một hình quạt bằng 1/4 hình tròn biểu diễn tỉ lệ:",
          ["25%", "50%", "12,5%", "75%"], 0,
          "1/4 hình tròn ứng với 25%."),
        q("Trong thư viện (Ví dụ 1), tỉ lệ sách tham khảo là:",
          ["10%", "20%", "30%", "40%"], 1,
          "Sách tham khảo chiếm 20%."),
        q("Trong Hình 5.9, hình tròn được chia thành các hình quạt nhỏ, mỗi hình quạt ứng với 10%. Sách giáo khoa (40%) được biểu diễn bởi bao nhiêu hình quạt?",
          ["3", "4", "5", "6"], 1,
          "40% = 4 hình quạt 10%."),
        q("Sách truyện (30%) được biểu diễn bởi bao nhiêu hình quạt nhỏ 10%?",
          ["2", "3", "4", "5"], 1,
          "30% = 3 hình quạt 10%."),
        q("Trong Ví dụ 2, tỉ lệ học sinh bơi thành thạo là:",
          ["35%", "50%", "15%", "85%"], 1,
          "250/500 = 50%."),
        q("Trong Ví dụ 2, tỉ lệ học sinh chưa biết bơi là:",
          ["15%", "25%", "35%", "50%"], 0,
          "75/500 = 15%."),
        q("Trong Ví dụ 2, tổng số học sinh được khảo sát là:",
          ["250", "425", "500", "600"], 2,
          "250 + 175 + 75 = 500."),
        q("Luyện tập 2: tỉ lệ bạn lớp 7D dự đoán đội vô địch là bao nhiêu?",
          ["15%", "30%", "35%", "20%"], 2,
          "Bảng cho 7D là 35%."),
        q("Luyện tập 2: lớp nào có tỉ lệ dự đoán cao nhất?",
          ["7A", "7B", "7C", "7D"], 3,
          "7D có 35%, cao nhất trong các lớp."),
        q("Trong Hình 5.10 (kết quả dự đoán), mỗi hình quạt nhỏ ứng với:",
          ["5%", "10%", "20%", "1%"], 0,
          "Hình tròn được chia sẵn, mỗi hình quạt ứng với 5%."),
        q("Trong Ví dụ 4 (Hình 5.16), với 200 học sinh khối 7, số bạn thích chơi thể thao là:",
          ["30", "60", "90", "120"], 1,
          "200 · 30% = 60 học sinh."),
        q("Trong Hình 5.16, tỉ lệ bạn thích đọc sách là:",
          ["10%", "15%", "20%", "25%"], 3,
          "Phần đọc sách chiếm 25%."),
        q("Luyện tập 5: trong 200 học sinh khối 7, số bạn thích đọc sách hoặc nghe nhạc là:",
          ["45", "90", "70", "120"], 1,
          "Đọc sách 25% + nghe nhạc 20% = 45%; 45% của 200 là 90 học sinh."),
        q("Trong Hình 5.17 (thực trạng các tật khúc xạ về mắt), tỉ lệ học sinh cận thị là:",
          ["0,8%", "32,8%", "66,4%", "33%"], 1,
          "Phần 'Cận thị' ghi 32,8%."),
        q("Tranh luận Hình 5.17: nếu trường có 1 000 học sinh, số học sinh cận thị ước lượng là:",
          ["328", "32,8", "3 280", "0,328"], 0,
          "32,8% của 1 000 là 328 học sinh (đây là con số ước lượng)."),
        q("Trong Luyện tập 3 (tỉ lệ cỡ áo của lớp 7A), cỡ áo M chiếm:",
          ["15%", "50%", "30%", "5%"], 1,
          "Bảng cho cỡ M là 50%."),
        q("Trong Luyện tập 3, cỡ áo nào chiếm tỉ lệ ít nhất?",
          ["S", "M", "L", "XL"], 3,
          "XL chiếm 5%, ít nhất."),
        q("Bài 5.6 (Hình 5.18): châu lục có số dân đông nhất là:",
          ["Châu Phi", "Châu Á", "Châu Âu", "Châu Mỹ"], 1,
          "Châu Á chiếm 59,52%, cao nhất."),
        q("Bài 5.6: biết năm 2020 tổng số dân của 5 châu lục là 7 773 triệu người, số dân châu Á khoảng:",
          ["4 626 triệu người", "1 338 triệu người", "747 triệu người", "1 019 triệu người"], 0,
          "59,52% · 7 773 ≈ 4 626 triệu người."),
        q("Bài 5.8 (Hình 5.20): một đội hiến máu gồm 200 tình nguyện viên, số người mang nhóm máu O là:",
          ["40", "60", "80", "120"], 2,
          "Nhóm máu O chiếm 40%: 200 · 40% = 80 người."),
        q("Bài 5.8: số người mang nhóm máu A hoặc O là:",
          ["60", "100", "120", "140"], 2,
          "A (20%) + O (40%) = 60%; 60% của 200 là 120 người."),
        q("Bài 5.9: ước lượng trong 800 học sinh tiểu học, số học sinh bơi thành thạo là:",
          ["200", "400", "500", "350"], 1,
          "50% của 800 là 400 học sinh."),
        q("Bài 5.9: số học sinh chưa biết bơi trong 800 học sinh là:",
          ["80", "100", "120", "150"], 2,
          "15% của 800 là 120 học sinh."),
        q("Trong Ví dụ 3 (Hình 5.14), yếu tố ảnh hưởng nhiều nhất đến chiều cao (ngoài di truyền) là:",
          ["Vận động", "Dinh dưỡng", "Giấc ngủ và môi trường", "Yếu tố khác"], 1,
          "Dinh dưỡng chiếm 32%, cao nhất ngoài di truyền."),
        q("Trong Ví dụ 3, tổng mức độ ảnh hưởng của dinh dưỡng, vận động và giấc ngủ và môi trường là:",
          ["60%", "68%", "75%", "80%"], 1,
          "32% + 20% + 16% = 68%."),
        q("Luyện tập 4 (Hình 5.15): nguồn điện chiếm tỉ lệ cao nhất của Việt Nam năm 2019 là:",
          ["Thuỷ điện", "Điện than", "Điện khí", "Điện nhập khẩu"], 1,
          "Điện than chiếm 41,6%, cao nhất."),
    ],
    bt_co_ban=[
        bt("Bài 5.6 (Hình 5.18): châu lục có số dân ít nhất là châu lục nào?",
           ["Châu Úc"], "Châu Úc chiếm 0,55%, nhỏ nhất."),
        bt("Bài 5.7: trong bảng 5.7, tổng số bạn được khảo sát về thú nuôi yêu thích là bao nhiêu?",
           ["40"], "10 + 20 + 7 + 3 = 40."),
        bt("Bài 5.7: trong bảng 5.7, số bạn yêu thích mèo chiếm bao nhiêu phần trăm? (ghi số, không ghi %)",
           ["50"], "20 / 40 = 50%."),
        bt("Bài 5.8: trong 200 tình nguyện viên, số người mang nhóm máu A là bao nhiêu?",
           ["40"], "20% của 200 là 40 người."),
        bt("Bài 5.8: trong 200 tình nguyện viên, số người mang nhóm máu B là bao nhiêu?",
           ["60"], "30% của 200 là 60 người."),
        bt("Bài 5.9: trong 800 học sinh tiểu học, số học sinh bơi thành thạo là bao nhiêu?",
           ["400"], "50% của 800 là 400."),
        bt("Luyện tập 3: bảng tỉ lệ áo đồng phục lớp 7A, cỡ áo S chiếm bao nhiêu phần trăm? (ghi số)",
           ["15"], "Bảng ghi cỡ S là 15%."),
    ],
    bt_nang_cao=[
        nc("Bài 5.9: trong 800 học sinh tiểu học, số học sinh chưa biết bơi là bao nhiêu?",
           "Tính 15% của 800.",
           ["120"],
           "Chưa biết bơi chiếm 15% (từ kết quả ở Hình 5.12), nên 15% · 800 = 120 học sinh."),
        nc("Tranh luận Hình 5.17: Có chắc chắn trường có 1 000 học sinh thì đúng 328 em bị cận thị không? (trả lời 'có' hoặc 'không')",
           "328 là số ước lượng từ tỉ lệ 32,8%.",
           ["không", "Không"],
           "Con số 328 chỉ là ước lượng, không phải số chính xác."),
    ],
)


# ============================================================
# BÀI 19: BIỂU ĐỒ ĐOẠN THẲNG
# ============================================================
B19 = bai(
    ly_thuyet="""📌 1. BIỂU ĐỒ ĐOẠN THẲNG LÀ GÌ
- Biểu đồ đoạn thẳng thường được dùng để biểu diễn sự thay đổi của một đại lượng theo thời gian.
- Các thành phần: trục ngang biểu diễn thời gian; trục đứng biểu diễn đại lượng ta đang quan tâm; mỗi điểm biểu diễn giá trị của đại lượng tại một thời điểm; hai điểm liên tiếp được nối với nhau bằng một đoạn thẳng; tiêu đề của biểu đồ thường ở dòng trên cùng.

📌 2. ĐỌC VÀ PHÂN TÍCH BIỂU ĐỒ ĐOẠN THẲNG
- Đọc giá trị tại mỗi điểm theo trục đứng ứng với thời điểm trên trục ngang.
- Xu thế: đại lượng tăng (đường đi lên), giảm (đường đi xuống) hay không đổi (đường nằm ngang).
- Độ dốc của đoạn thẳng cho biết tốc độ tăng hoặc giảm của đại lượng: đoạn càng dốc thì đại lượng thay đổi càng nhanh.
- Độ dốc phụ thuộc vào việc chọn đơn vị trên trục đứng.

📌 3. VẼ BIỂU ĐỒ ĐOẠN THẲNG
- Bước 1: Vẽ trục ngang biểu diễn thời gian và trục đứng biểu diễn đại lượng; chọn đơn vị phù hợp với giá trị lớn nhất và nhỏ nhất.
- Bước 2: Với mỗi thời điểm trên trục ngang, đánh dấu một điểm biểu diễn giá trị tương ứng.
- Bước 3: Nối các điểm liên tiếp bằng các đoạn thẳng.
- Bước 4: Ghi chú thích cho các trục, điền giá trị tại các điểm (nếu cần), đặt tên cho biểu đồ.
- Khi số liệu lớn, không nên vẽ trục đứng bắt đầu từ 0 nếu đơn vị trục quá nhỏ (để biểu đồ rõ ràng hơn).""",
    vi_du="""Ví dụ 1: Chiều cao của cây đậu trong 5 ngày: 0,5; 0,75; 1; 1,4; 2,5 (cm). Ngày 5 cây tăng nhiều nhất so với các ngày còn lại, tăng 2,5 − 1,4 = 1,1 cm.

Ví dụ 2: Biểu đồ đoạn thẳng cho biết số lượng máy tính để bàn và máy tính xách tay được bán trong 6 tháng đầu năm. Tháng Sáu, cửa hàng bán được nhiều máy tính xách tay hơn. Trong hai tháng đầu, máy tính để bàn bán được nhiều hơn; các tháng sau số lượng máy tính để bàn giảm dần, còn máy tính xách tay có xu hướng tăng. Vì vậy thời gian tới cửa hàng nên nhập nhiều máy tính xách tay hơn.

Chú ý: Có thể biểu diễn nhiều bộ số liệu trên cùng một biểu đồ, mỗi đường có chú giải ứng với một bộ số liệu.""",
    cau_hoi=[
        q("Biểu đồ đoạn thẳng thường được dùng để biểu diễn:",
          ["Tỉ lệ các phần trong toàn bộ", "Sự thay đổi của một đại lượng theo thời gian", "So sánh các phần của một tổng", "Vị trí các điểm trên mặt phẳng"], 1,
          "Biểu đồ đoạn thẳng cho thấy xu thế thay đổi theo thời gian."),
        q("Trong biểu đồ đoạn thẳng, trục ngang thường biểu diễn:",
          ["Đại lượng ta đang quan tâm", "Thời gian", "Tỉ lệ phần trăm", "Tên các đối tượng"], 1,
          "Trục ngang là thời gian; trục đứng là đại lượng quan tâm."),
        q("Trong biểu đồ đoạn thẳng, trục đứng biểu diễn:",
          ["Thời gian", "Đại lượng ta đang quan tâm", "Tiêu đề", "Chú giải"], 1,
          "Trục đứng biểu diễn giá trị của đại lượng."),
        q("Tiêu đề của biểu đồ đoạn thẳng thường nằm ở:",
          ["Dòng dưới cùng", "Dòng trên cùng", "Bên trái", "Bên phải"], 1,
          "Tiêu đề ở dòng trên cùng."),
        q("Hình 5.21 (dân số Việt Nam qua 5 lần tổng điều tra): dân số năm 2019 là bao nhiêu triệu người?",
          ["64,4", "76,3", "85,8", "96,2"], 3,
          "Điểm cuối ứng với năm 2019 là 96,2 triệu người."),
        q("Hình 5.21: dân số Việt Nam năm 1989 là bao nhiêu triệu người?",
          ["54,7", "64,4", "76,3", "85,8"], 1,
          "Năm 1989 là 64,4 triệu người."),
        q("Từ năm 1979 đến năm 2019, số dân Việt Nam có xu hướng:",
          ["Tăng", "Giảm", "Không đổi", "Tăng rồi giảm"], 0,
          "Đường biểu diễn luôn đi lên, dân số tăng."),
        q("Từ năm 1979 đến năm 2019, dân số Việt Nam tăng bao nhiêu triệu người?",
          ["40,5", "41,5", "42,5", "31,5"], 1,
          "96,2 − 54,7 = 41,5 triệu người."),
        q("Luyện tập 1 (Hình 5.23): thứ hạng bóng đá nam Việt Nam năm 2016 là:",
          ["112", "134", "100", "94"], 1,
          "Điểm năm 2016 ứng với thứ hạng 134."),
        q("Luyện tập 1: thứ hạng của bóng đá nam Việt Nam năm 2020 là:",
          ["93", "94", "100", "112"], 0,
          "Điểm năm 2020 ghi 93."),
        q("Luyện tập 1: từ 2016 đến 2020, số thứ hạng của bóng đá nam Việt Nam có xu hướng:",
          ["Tăng liên tục", "Giảm liên tục", "Không đổi", "Tăng rồi giảm"], 1,
          "Số thứ hạng giảm từ 134 xuống 93, nghĩa là thứ hạng được cải thiện."),
        q("Ví dụ 1 (Hình 5.24): chiều cao của cây đậu ngày 4 là:",
          ["1,0 cm", "1,4 cm", "2,5 cm", "0,75 cm"], 1,
          "Ngày 4 chiều cao là 1,4 cm."),
        q("Ví dụ 1: vào ngày nào chiều cao của cây đậu tăng nhiều nhất so với ngày trước?",
          ["Ngày 2", "Ngày 3", "Ngày 4", "Ngày 5"], 3,
          "Ngày 5 tăng 1,1 cm, nhiều nhất."),
        q("Ví dụ 1: chiều cao cây đậu tăng bao nhiêu cm từ ngày 4 đến ngày 5?",
          ["1,1 cm", "0,9 cm", "1,4 cm", "2,5 cm"], 0,
          "2,5 − 1,4 = 1,1 cm."),
        q("Luyện tập 2 (Hình 5.25): năm 2018 có bao nhiêu triệu lượt khách quốc tế đến Việt Nam?",
          ["12,9", "15,5", "18", "10"], 1,
          "Điểm năm 2018 ghi 15,5 triệu lượt."),
        q("Luyện tập 2: năm 2020 có bao nhiêu triệu lượt khách quốc tế đến Việt Nam?",
          ["4", "18", "15,5", "12,9"], 0,
          "Điểm năm 2020 ghi 4 triệu lượt."),
        q("Luyện tập 2: từ năm 2015 đến năm 2019, số lượt khách quốc tế có xu hướng:",
          ["Giảm", "Tăng", "Không đổi", "Dao động không rõ"], 1,
          "Từ 8 triệu (2015) lên 18 triệu (2019) đường biểu diễn đi lên."),
        q("Ví dụ 2 (Hình 5.26): trong tháng Sáu, cửa hàng bán được loại máy tính nào nhiều hơn?",
          ["Máy tính để bàn", "Máy tính xách tay", "Bằng nhau", "Không xác định được"], 1,
          "Đường máy tính xách tay ở tháng Sáu cao hơn."),
        q("Ví dụ 2: thời gian tiếp theo, cửa hàng nên nhập loại máy tính nào nhiều hơn?",
          ["Máy tính để bàn", "Máy tính xách tay", "Cả hai như nhau", "Không nên nhập"], 1,
          "Máy tính xách tay có xu hướng tăng, máy tính để bàn giảm."),
        q("Luyện tập 3 (Hình 5.27): năm 2016, tỉ lệ học sinh biết bơi của tỉnh A là bao nhiêu?",
          ["25%", "37%", "46%", "60%"], 1,
          "Đường tỉnh A bắt đầu ở 37% năm 2016."),
        q("Luyện tập 3: năm 2020, tỉ lệ học sinh biết bơi của tỉnh B là bao nhiêu?",
          ["45%", "40%", "35%", "75%"], 0,
          "Tỉnh B đạt 45% năm 2020."),
        q("Thực hành (Bảng 5.1): khi vẽ biểu đồ chiều cao cây đậu, trục đứng nên chọn đơn vị là bao nhiêu và giá trị lớn nhất là bao nhiêu?",
          ["Đơn vị 0,5 cm và giá trị lớn nhất 3", "Đơn vị 1 cm và giá trị lớn nhất 10", "Đơn vị 0,1 và giá trị lớn nhất 5", "Đơn vị 2 và giá trị lớn nhất 2,5"], 0,
          "Chiều cao nhỏ nhất 0,5 cm, lớn nhất 2,5 cm, chọn đơn vị 0,5 và giá trị lớn nhất 3."),
        q("Độ dốc của đoạn thẳng trong biểu đồ đoạn thẳng cho biết:",
          ["Tốc độ tăng hoặc giảm của đại lượng", "Giá trị lớn nhất của đại lượng", "Tiêu đề của biểu đồ", "Số điểm trên biểu đồ"], 0,
          "Đoạn càng dốc thì đại lượng thay đổi càng nhanh."),
        q("Độ dốc của biểu đồ đoạn thẳng phụ thuộc vào yếu tố nào?",
          ["Màu sắc của đường", "Việc chọn đơn vị trên trục đứng", "Số điểm trên biểu đồ", "Tên biểu đồ"], 1,
          "Nếu đơn vị trục đứng thay đổi, độ dốc trông khác đi."),
        q("Khi số liệu lớn mà đơn vị trục đứng nhỏ, nên:",
          ["Vẽ trục đứng bắt đầu từ 0", "Không vẽ trục đứng bắt đầu từ 0", "Bỏ trục ngang", "Dùng biểu đồ hình quạt"], 1,
          "Không bắt đầu từ 0 để biểu đồ rõ ràng, dễ quan sát sự thay đổi."),
        q("Luyện tập 4 (Bảng thành tích chạy 1 500 m): thành tích tuần 5 là bao nhiêu phút?",
          ["6,5", "7", "8", "6"], 0,
          "Tuần 5 có thành tích 6,5 phút."),
        q("Ví dụ 2: Hình 5.25 cho biết năm 2017 có bao nhiêu triệu lượt khách quốc tế?",
          ["12,9", "12", "13", "15,5"], 0,
          "Điểm năm 2017 ghi 12,9 triệu lượt."),
        q("Trong biểu đồ đoạn thẳng, hai điểm liên tiếp được nối với nhau bằng:",
          ["Đường cong", "Đoạn thẳng", "Hình tròn", "Cột"], 1,
          "Các điểm liên tiếp được nối bằng đoạn thẳng."),
        q("Mỗi điểm trên biểu đồ đoạn thẳng biểu diễn:",
          ["Tổng của các đại lượng", "Giá trị của đại lượng tại một thời điểm", "Tỉ lệ phần trăm", "Tên đối tượng"], 1,
          "Điểm cho biết giá trị tại thời điểm tương ứng."),
        q("Khi biểu diễn nhiều bộ số liệu trên cùng một biểu đồ đoạn thẳng, mỗi đường cần có:",
          ["Một chú giải riêng", "Một trục riêng", "Một tiêu đề riêng", "Không cần ghi gì"], 0,
          "Chú giải giúp phân biệt các bộ số liệu."),
        q("Thử thách nhỏ (Hình 5.31): để thấy rõ hơn tuổi thọ trung bình của người Việt Nam ngày càng tăng, nên dùng biểu đồ:",
          ["Biểu đồ C (trục đứng từ 0 đến 80)", "Biểu đồ D (trục đứng từ 65 đến 77)", "Cả hai như nhau", "Biểu đồ hình quạt tròn"], 1,
          "Biểu đồ D có trục đứng không bắt đầu từ 0 nên sự thay đổi rõ hơn."),
        q("Trong Hình 5.27 (tỉ lệ học sinh biết bơi), tỉnh nào có tỉ lệ tăng nhanh hơn từ 2016 đến 2020?",
          ["Tỉnh A", "Tỉnh B", "Bằng nhau", "Không xác định"], 0,
          "Tỉnh A tăng từ 37% lên 90%, nhanh hơn tỉnh B (25% lên 45%)."),
    ],
    bt_co_ban=[
        bt("Bài 5.10 (Hình 5.32): kỉ lục thế giới về chạy cự li 100 m đạt được năm 1991 là bao nhiêu giây?",
           ["9,86"], "Đọc trên biểu đồ điểm năm 1991."),
        bt("Bài 5.10: từ năm 1912 đến năm 2009, kỉ lục thế giới đã giảm được bao nhiêu giây? (ghi số, ví dụ 1,02)",
           ["1,02"], "10,6 − 9,58 = 1,02 giây."),
        bt("Bài 5.11 (Hình 5.33): trong các năm 1950–1980, châu lục nào có số dân cao nhất? (ghi tên châu lục)",
           ["Châu Âu"], "Đường châu Âu luôn ở trên cùng."),
        bt("Bài 5.11: từ năm 1950 đến năm 1980, châu lục nào tăng số dân chậm nhất? (ghi tên châu lục)",
           ["Châu Âu"], "Đường châu Âu tăng ít nhất (từ khoảng 550 lên 700 triệu)."),
        bt("Bài 5.12: nhiệt độ cao nhất trong bảng ở Hà Nội là bao nhiêu °C? (ghi số)",
           ["34"], "Nhiệt độ 34°C lúc 12 giờ."),
        bt("Bài 5.13 (số trận thắng 2013–2020: 36; 42; 15; 23; 25; 35; 32; 20): năm 2015 đội thắng bao nhiêu trận?",
           ["15"], "Năm thứ ba (2015) là 15 trận."),
        bt("Hình 5.21: dân số Việt Nam năm 1989 là bao nhiêu triệu người? (ghi số)",
           ["64,4"], "Điểm năm 1989 ghi 64,4."),
    ],
    bt_nang_cao=[
        nc("Hình 5.21 (HĐ1): hoàn thành bảng dân số Việt Nam năm 2009 (triệu người).",
           "Đọc giá trị điểm năm 2009 trên biểu đồ.",
           ["85,8"],
           "Năm 2009 dân số là 85,8 triệu người."),
        nc("Ví dụ 2 (Hình 5.26): cửa hàng nên nhập loại máy tính nào nhiều hơn trong thời gian tới? (ghi tên loại)",
           "Xét xu hướng của hai đường biểu diễn.",
           ["máy tính xách tay", "Máy tính xách tay"],
           "Máy tính xách tay có xu hướng tăng, máy tính để bàn giảm dần."),
    ],
)


CHUONG_5 = {
    "Chương V: Thu thập và biểu diễn dữ liệu": {
        "Bài 17: Thu thập và phân loại dữ liệu": B17,
        "Bài 18: Biểu đồ hình quạt tròn": B18,
        "Bài 19: Biểu đồ đoạn thẳng": B19,
    }
}

# ============================================================
# FILE toan_c6.py
# ============================================================
# ============================================================
# BÀI 20: TỈ LỆ THỨC
# ============================================================
B20 = bai(
    ly_thuyet="""📌 1. TỈ LỆ THỨC
- Tỉ lệ thức là đẳng thức của hai tỉ số: a/b = c/d (b, d ≠ 0).
- Còn viết là a : b = c : d.
- Hai tỉ số a/b và c/d lập được thành tỉ lệ thức khi và chỉ khi chúng bằng nhau.

📌 2. TÍNH CHẤT CỦA TỈ LỆ THỨC
- Nếu a/b = c/d thì ad = bc.
- Ngược lại, nếu ad = bc (a, b, c, d ≠ 0) thì ta có các tỉ lệ thức:
  a/b = c/d; a/c = b/d; d/b = c/a; d/c = b/a.
- Từ tỉ lệ thức a/b = c/d ta suy ra:
  a = bc/d; b = ad/c; c = ad/b; d = bc/a.
- Đổi chỗ hai số hạng trong một tỉ lệ thức (a với d, b với c, hoặc cả a với d và b với c) ta được tỉ lệ thức mới.

📌 3. CÁCH LẬP TỈ LỆ THỨC TỪ BỐN SỐ
- Từ đẳng thức ad = bc (hoặc tích hai số này bằng tích hai số kia) ta có thể lập được nhiều tỉ lệ thức.
- Ví dụ: từ 2·6 = 3·4 ta có 2/3 = 4/6; 2/4 = 3/6; 6/3 = 4/2; 6/4 = 3/2.""",
    vi_du="""Ví dụ 1: 10 : 15 = 10/15 = 2/3 và (2/7) : (3/7) = 2/3. Vì hai tỉ số bằng nhau nên 10 : 15 = (2/7) : (3/7) là một tỉ lệ thức.

Vận dụng 1: Mặt sân 105 m × 68 m có tỉ số chiều rộng/chiều dài là 68/105. Mô phỏng 21 cm × 13,6 cm có tỉ số 13,6/21. Ta có 68 · 21 = 1 428 và 105 · 13,6 = 1 428 nên hai tỉ số bằng nhau: Nam vẽ đúng tỉ lệ thực tế.

Ví dụ 2: Lá cờ có chiều rộng 14 cm, tỉ số chiều rộng : chiều dài = 2 : 3. Gọi chiều dài là x (cm): 14/x = 2/3, suy ra x = 14 · 3 / 2 = 21 cm.

Vận dụng 2: 10 chiếc bánh cần 5 kg gạo nếp. 45 chiếc bánh cần 5 · 45 / 10 = 22,5 kg gạo nếp.""",
    cau_hoi=[
        q("Tỉ lệ thức là:",
          ["Đẳng thức của hai tỉ số a/b = c/d", "Tổng của hai tỉ số", "Hiệu của hai tỉ số", "Một tỉ số duy nhất"], 0,
          "Tỉ lệ thức là đẳng thức của hai tỉ số."),
        q("Với a/b = c/d (b, d ≠ 0), ta có tính chất:",
          ["ad = bc", "a + d = b + c", "ab = cd", "a·c = b·d"], 0,
          "Tích hai ngoại tỉ bằng tích hai trung tỉ: ad = bc."),
        q("Hai tỉ số 10 : 15 và (2/7) : (3/7) có lập thành tỉ lệ thức không?",
          ["Có", "Không", "Chỉ khi a = b", "Không xác định được"], 0,
          "10/15 = 2/3 và (2/7)/(3/7) = 2/3 nên bằng nhau."),
        q("Trong các cặp sau, cặp nào lập được tỉ lệ thức với 4 : 20?",
          ["2 : 5", "1 : 5", "1 : 4", "5 : 20"], 1,
          "4/20 = 1/5 nên cặp 1 : 5 lập được tỉ lệ thức."),
        q("Số 0,5 : 1,25 bằng tỉ số nào sau đây?",
          ["3/5 : 3/2", "4 : 20", "1 : 3", "2 : 3"], 0,
          "0,5/1,25 = 2/5 và (3/5)/(3/2) = 2/5."),
        q("Trong các tỉ số 4 : 20; 0,5 : 1,25; (3/5) : (3/2), những tỉ số nào bằng nhau?",
          ["4 : 20 và 0,5 : 1,25", "0,5 : 1,25 và (3/5) : (3/2)", "4 : 20 và (3/5) : (3/2)", "Không có tỉ số nào bằng nhau"], 1,
          "4/20 = 1/5 ≠ 2/5, còn 0,5 : 1,25 = (3/5) : (3/2) = 2/5."),
        q("Từ đẳng thức 2 · 6 = 3 · 4, tỉ lệ thức nào đúng?",
          ["2/3 = 6/4", "2/6 = 3/4", "2/3 = 4/6", "6/2 = 4/9"], 2,
          "2/3 = 4/6 vì 2 · 6 = 3 · 4."),
        q("Từ ad = bc (a, b, c, d ≠ 0), tỉ lệ thức nào KHÔNG suy ra được?",
          ["a/b = c/d", "a/c = b/d", "d/b = c/a", "a/d = b/c"], 3,
          "a/d = b/c tương đương với ac = bd, không suy ra từ ad = bc."),
        q("Từ 0,2 · 4,5 = 0,6 · 1,5, tỉ lệ thức nào đúng?",
          ["0,2 / 0,6 = 1,5 / 4,5", "0,2 / 4,5 = 0,6 / 1,5", "0,2 / 1,5 = 4,5 / 0,6", "0,2 / 0,6 = 4,5 / 1,5"], 0,
          "0,2 · 4,5 = 0,6 · 1,5 nên 0,2/0,6 = 1,5/4,5."),
        q("Đổi chỗ b với c trong tỉ lệ thức a/b = c/d được tỉ lệ thức nào?",
          ["a/c = b/d", "a/b = d/c", "b/a = c/d", "a/d = c/b"], 0,
          "Từ ad = bc, đổi chỗ b và c ta được ad = cb, tức a/c = b/d."),
        q("Đổi chỗ a với d trong tỉ lệ thức a/b = c/d được tỉ lệ thức nào?",
          ["d/b = c/a", "a/b = d/c", "c/b = a/d", "b/a = d/c"], 0,
          "Từ ad = bc, đổi chỗ a và d ta có d/b = c/a."),
        q("Từ 3x = 4y (x, y ≠ 0), tỉ lệ thức nào đúng?",
          ["x/4 = y/3", "x/3 = y/4", "3/x = 4/y", "x/y = 3/4"], 0,
          "x/4 = y/3 tương đương với 3x = 4y."),
        q("Từ bốn số 5; 10; 25; 50, tỉ lệ thức nào đúng?",
          ["5/10 = 25/50", "5/25 = 50/10", "5/50 = 10/25", "5/10 = 50/25"], 0,
          "5 · 50 = 10 · 25 = 250 nên 5/10 = 25/50."),
        q("Tỉ số 2/3 bằng tỉ số nào sau đây?",
          ["4 : 6", "4 : 5", "3 : 2", "2 : 4"], 0,
          "2/3 = 4/6 = 4 : 6."),
        q("Từ a/b = c/d suy ra a bằng:",
          ["bc/d", "ad/c", "ad/b", "bd/c"], 0,
          "Từ ad = bc suy ra a = bc/d."),
        q("Từ a/b = c/d suy ra b bằng:",
          ["ad/c", "bc/d", "cd/a", "ac/d"], 0,
          "Từ ad = bc suy ra b = ad/c."),
        q("Từ a/b = c/d suy ra d bằng:",
          ["bc/a", "ad/c", "ab/c", "cd/b"], 0,
          "Từ ad = bc suy ra d = bc/a."),
        q("Từ a/b = c/d suy ra c bằng:",
          ["ad/b", "bc/a", "ad/c", "ab/d"], 0,
          "Từ ad = bc suy ra c = ad/b."),
        q("Phân số 10/16 : 4/21 có thể viết thành tỉ số giữa hai số nguyên là:",
          ["105 : 32", "32 : 105", "10 : 21", "4 : 16"], 0,
          "(10/16) : (4/21) = (10 · 21)/(16 · 4) = 210/64 = 105/32."),
        q("Tỉ số 12 : 30 bằng tỉ số nào sau đây?",
          ["2,5 : 6,25", "(3/7) : (18/24)", "2 : 3", "12 : 20"], 0,
          "12/30 = 2/5 và 2,5/6,25 = 2/5."),
        q("Ví dụ 6/9 = 0,8/1,2 (Hình HĐ2 trang 6): hai tỉ số này có lập thành tỉ lệ thức không?",
          ["Đúng, vì cả hai tỉ số đều bằng 2/3", "Sai, vì 0,8 khác 6", "Sai, vì 1,2 khác 9", "Không xác định"], 0,
          "6/9 = 2/3 và 0,8/1,2 = 2/3 nên là tỉ lệ thức."),
        q("Tỉ lệ thức nào đúng?",
          ["1/2 = 3/6", "1/2 = 6/3", "1/6 = 2/3", "2/6 = 1/4"], 0,
          "1 · 6 = 2 · 3 nên 1/2 = 3/6."),
        q("Nếu a/b = c/d thì b/a bằng:",
          ["d/c", "c/d", "a/c", "ad/bc"], 0,
          "Đổi vai trò tử và mẫu của cả hai tỉ số: b/a = d/c."),
        q("Từ 2/3 = 4/6, suy ra 3/2 bằng:",
          ["6/4", "4/6", "2/4", "6/2"], 0,
          "Lật hai tỉ số: 3/2 = 6/4."),
        q("Vận dụng 1: mặt sân 105 m, mô phỏng 21 cm (cùng tỉ lệ). Tỉ số 21 : 105 bằng:",
          ["1 : 5", "1 : 4", "1 : 6", "21 : 68"], 0,
          "21/105 = 1/5."),
        q("Ví dụ 2: chiều rộng lá cờ là 14 cm, tỉ số chiều rộng : chiều dài = 2 : 3. Chiều dài là:",
          ["21 cm", "28 cm", "7 cm", "42 cm"], 0,
          "14/x = 2/3 suy ra x = 21 cm."),
        q("Tỉ số chiều rộng : chiều dài của các lá cờ Tổ quốc là:",
          ["2 : 3", "3 : 2", "3 : 5", "2 : 5"], 0,
          "Kết luận của Ví dụ 2: tỉ số chiều rộng và chiều dài luôn là 2 : 3."),
        q("Luyện tập 1: tỉ số nào bằng 3/5 : 3/2?",
          ["0,5 : 1,25", "4 : 20", "1 : 3", "2 : 3"], 0,
          "(3/5)/(3/2) = 2/5 = 0,5/1,25."),
        q("Luyện tập 2: từ đẳng thức 0,2 · 4,5 = 0,6 · 1,5, tỉ lệ thức nào sau đây đúng?",
          ["0,2 : 0,6 = 1,5 : 4,5", "0,2 : 4,5 = 0,6 : 1,5", "0,2 : 1,5 = 4,5 : 0,6", "0,2 : 0,6 = 4,5 : 1,5"], 0,
          "Đã kiểm tra: 0,2 · 4,5 = 0,6 · 1,5 nên 0,2/0,6 = 1,5/4,5."),
        q("Bài 6.5: cứ 3 lít nước tinh khiết pha với 27 g muối. Muốn có 45 g muối cần bao nhiêu lít nước?",
          ["5 lít", "4 lít", "6 lít", "7,5 lít"], 0,
          "3/27 = x/45 suy ra x = 5 lít."),
        q("Bài 6.6: 14 ngày cày hết cánh đồng cần 18 máy. Để cày trong 12 ngày cần bao nhiêu máy? (năng suất như nhau)",
          ["21 máy", "24 máy", "16 máy", "15 máy"], 0,
          "Số máy · số ngày không đổi: 18 · 14 = x · 12 suy ra x = 21 máy."),
    ],
    bt_co_ban=[
        bt("Bài 6.1b: viết tỉ số 1,3 : 2,75 dưới dạng tỉ số giữa hai số nguyên (ghi dạng a : b, ví dụ 3:4).",
           ["26:55", "26 : 55"], "1,3 : 2,75 = 130 : 275 = 26 : 55."),
        bt("Bài 6.3a: tìm x trong x/6 = −3/4 (ghi số thập phân, ví dụ −1,5).",
           ["−4,5", "-4,5", "−4.5", "-4.5"], "x = 6 · (−3)/4 = −4,5."),
        bt("Bài 6.3b: tìm x trong 5/x = 15/(−20). Ghi dạng phân số (ví dụ −20/3).",
           ["-20/3", "−20/3"], "x = 5 · (−20)/15 = −20/3."),
        bt("Bài 6.5: cần pha bao nhiêu lít nước tinh khiết khi có 45 g muối? (ghi số)",
           ["5"], "Tỉ lệ 3 lít : 27 g nên 45 g cần 5 lít."),
        bt("Bài 6.6: để cày hết cánh đồng trong 12 ngày cần bao nhiêu máy cày? (ghi số)",
           ["21"], "18 · 14 / 12 = 21 máy."),
        bt("Vận dụng 2: 10 chiếc bánh chưng cần 5 kg gạo nếp. 45 chiếc cần bao nhiêu kg gạo nếp? (ghi số)",
           ["22,5", "22.5"], "5 · 45 / 10 = 22,5 kg."),
    ],
    bt_nang_cao=[
        nc("Bài 6.2: trong các tỉ số 12 : 30; (3/7) : (18/24); 2,5 : 6,25, những tỉ số nào bằng nhau? (trả lời: hai tỉ số nào)",
           "Rút gọn từng tỉ số về dạng phân số tối giản.",
           ["12 : 30 và 2,5 : 6,25", "12:30 và 2,5:6,25", "12 : 30 và 2,5 : 6,25 bằng nhau"],
           "12/30 = 2/5 và 2,5/6,25 = 2/5 bằng nhau; (3/7)/(18/24) = 4/7 khác."),
        nc("Bài 6.4: lập tất cả các tỉ lệ thức có thể được từ đẳng thức 14 · (−15) = (−10) · 21. Hãy nêu một tỉ lệ thức đúng (ghi dạng a/b = c/d).",
           "Sử dụng tính chất: ad = bc.",
           ["14/(−10) = 21/(−15)", "14/(-10)=21/(-15)", "14/21 = (−10)/(−15)", "14/21=-10/-15"],
           "Từ 14 · (−15) = (−10) · 21, ta có 14/(−10) = 21/(−15), 14/21 = (−10)/(−15), v.v."),
    ],
)


# ============================================================
# BÀI 21: TÍNH CHẤT CỦA DÃY TỈ SỐ BẰNG NHAU
# ============================================================
B21 = bai(
    ly_thuyet="""📌 1. TÍNH CHẤT CỦA DÃY TỈ SỐ BẰNG NHAU
- Từ tỉ lệ thức a/b = c/d (các tỉ số có nghĩa) suy ra:
  a/b = c/d = (a + c)/(b + d) = (a − c)/(b − d).
- Mở rộng: từ dãy tỉ số bằng nhau a/b = c/d = e/f suy ra
  a/b = c/d = e/f = (a + c + e)/(b + d + f) = (a − c + e)/(b − d + f).
- Nếu a/b = c/d = e/f ta còn nói các số a, c, e tỉ lệ với các số b, d, f và viết a : c : e = b : d : f.

📌 2. CÁCH GIẢI BÀI TOÁN CHIA TỈ LỆ
- Đặt tỉ số chung bằng k (x/a = y/b = z/c = k), rồi dùng điều kiện đề bài (tổng hoặc hiệu) để tìm k.
- Sau đó suy ra x = a·k, y = b·k, z = c·k.""",
    vi_du="""Ví dụ 1: Tìm hai số x, y biết x/5 = y/11 và x + y = 32.
Áp dụng tính chất: x/5 = y/11 = (x + y)/(5 + 11) = 32/16 = 2. Suy ra x = 2 · 5 = 10 và y = 2 · 11 = 22.

Ví dụ 2: Ba nhà từ thiện đóng góp 450 triệu đồng theo tỉ lệ 3 : 5 : 7. Gọi số tiền là x, y, z: x/3 = y/5 = z/7 = (x + y + z)/15 = 450/15 = 30. Vậy x = 90, y = 150, z = 210 (triệu đồng).

Ví dụ luyện tập (Luyện tập trang 8): x/11 = y/17 và x − y = 12, k = 12/(11 − 17) = −2, suy ra x = −22, y = −34.""",
    cau_hoi=[
        q("Từ a/b = c/d, suy ra (a + c)/(b + d) bằng:",
          ["a/b", "a/d", "b/c", "ab/cd"], 0,
          "Tính chất dãy tỉ số bằng nhau."),
        q("Từ a/b = c/d, suy ra (a − c)/(b − d) bằng:",
          ["a/b", "c/d", "ab/cd", "a/c"], 0,
          "Tính chất dãy tỉ số bằng nhau cho hiệu."),
        q("Từ a/b = c/d = e/f, suy ra (a + c + e)/(b + d + f) bằng:",
          ["a/b", "a/c", "ab/cd", "b/d"], 0,
          "Mở rộng tính chất dãy tỉ số bằng nhau."),
        q("Ví dụ 1: tìm x biết x/5 = y/11 và x + y = 32.",
          ["10", "8", "12", "22"], 0,
          "x = 2 · 5 = 10."),
        q("Ví dụ 1: tìm y biết x/5 = y/11 và x + y = 32.",
          ["22", "11", "16", "32"], 0,
          "y = 2 · 11 = 22."),
        q("Luyện tập: tìm x biết x/11 = y/17 và x − y = 12.",
          ["−22", "22", "−34", "12"], 0,
          "k = 12/(11 − 17) = −2 nên x = −22."),
        q("Luyện tập: tìm y biết x/11 = y/17 và x − y = 12.",
          ["−34", "34", "−22", "−12"], 0,
          "y = −2 · 17 = −34."),
        q("Ví dụ 2: ba nhà từ thiện đóng góp 450 triệu đồng theo tỉ lệ 3 : 5 : 7. Nhà thứ nhất đóng góp:",
          ["90 triệu đồng", "150 triệu đồng", "210 triệu đồng", "30 triệu đồng"], 0,
          "x = 30 · 3 = 90."),
        q("Ví dụ 2: nhà từ thiện thứ hai đóng góp bao nhiêu triệu đồng?",
          ["90", "150", "210", "450"], 1,
          "y = 30 · 5 = 150."),
        q("Ví dụ 2: nhà từ thiện thứ ba đóng góp bao nhiêu triệu đồng?",
          ["90", "150", "210", "450"], 2,
          "z = 30 · 7 = 210."),
        q("Vận dụng: ba nhà đầu tư góp vốn theo tỉ lệ 2 : 3 : 4, tiền lãi 72 triệu đồng chia theo tỉ lệ vốn. Nhà đầu tư thứ nhất nhận được:",
          ["16 triệu đồng", "24 triệu đồng", "32 triệu đồng", "18 triệu đồng"], 0,
          "Tổng 2 + 3 + 4 = 9, k = 72/9 = 8, nhà thứ nhất 2 · 8 = 16 triệu."),
        q("Bài 6.7: x/9 = y/11 và x + y = 40. Giá trị của x là:",
          ["18", "22", "20", "9"], 0,
          "k = 40/20 = 2, x = 18."),
        q("Bài 6.7: giá trị của y là:",
          ["18", "22", "20", "11"], 1,
          "y = 2 · 11 = 22."),
        q("Bài 6.8: x/17 = y/21 và x − y = 8. Giá trị của x là:",
          ["−34", "34", "−42", "−8"], 0,
          "k = 8/(17 − 21) = −2, x = −34."),
        q("Bài 6.10: ba lớp 7A, 7B, 7C trồng 120 cây tỉ lệ với 7; 8; 9. Lớp 7B trồng:",
          ["35 cây", "40 cây", "45 cây", "24 cây"], 1,
          "Tổng 24, k = 5, 7B = 8 · 5 = 40 cây."),
        q("Bài 6.10: lớp 7C trồng bao nhiêu cây?",
          ["35", "40", "45", "120"], 2,
          "7C = 9 · 5 = 45 cây."),
        q("Từ bốn số 15; 18; 20; 24, tỉ lệ thức nào đúng?",
          ["15/18 = 20/24", "15/20 = 24/18", "18/15 = 20/24", "15/24 = 18/20"], 0,
          "15 · 24 = 18 · 20 = 360 nên 15/18 = 20/24."),
        q("Luyện tập chung Ví dụ 2: x/y = 3/2 và x + y = 15. Giá trị x là:",
          ["9", "6", "15", "3"], 0,
          "x/3 = y/2 = 15/5 = 3 nên x = 9."),
        q("Luyện tập chung Ví dụ 2: giá trị y là:",
          ["6", "9", "3", "15"], 0,
          "y = 3 · 2 = 6."),
        q("Luyện tập chung Ví dụ 3: ba cạnh tam giác tỉ lệ với 2; 3; 4 và cạnh lớn nhất hơn cạnh nhỏ nhất 6 cm. Cạnh lớn nhất là:",
          ["6 cm", "9 cm", "12 cm", "8 cm"], 2,
          "k = 3, cạnh nhỏ nhất 6, cạnh lớn nhất 3 · 4 = 12 cm."),
        q("Bài 6.11 (hoặc Bài 21): từ 3x = 4y, tỉ lệ thức nào đúng?",
          ["x/4 = y/3", "x/3 = y/4", "x/y = 3/4", "3/x = 4/y"], 0,
          "x/4 = y/3 tương đương 3x = 4y."),
        q("Bài 6.13a: x/y = 5/3 và x + y = 16. Giá trị x là:",
          ["10", "6", "8", "16"], 0,
          "k = 16/8 = 2, x = 10."),
        q("Bài 6.13b: x/y = 9/4 và x − y = −15. Giá trị x là:",
          ["−27", "27", "−12", "−15"], 0,
          "k = −15/5 = −3, x = −27."),
        q("Bài 6.14: số học sinh lớp 7A và 7B có tỉ số 0,95 = 19/20, lớp 7B nhiều hơn 7A 2 em. Lớp 7A có:",
          ["38 học sinh", "40 học sinh", "42 học sinh", "36 học sinh"], 0,
          "k = 2, 7A = 19 · 2 = 38."),
        q("Bài 6.14: lớp 7B có bao nhiêu học sinh?",
          ["38", "40", "42", "2"], 1,
          "7B = 20 · 2 = 40."),
        q("Bài 6.16: x/2 = y/3 = z/4 và x + 2y − 3z = −12. Giá trị x là:",
          ["6", "9", "12", "3"], 0,
          "x = 2k, y = 3k, z = 4k, k = 3 nên x = 6."),
        q("Bài 6.16: giá trị z là:",
          ["6", "9", "12", "3"], 2,
          "z = 4 · 3 = 12."),
        q("Bài 6.15: đường được làm trong 15 ngày, 45 người làm trong 10 ngày được nửa công việc. Cần bổ sung thêm bao nhiêu người để hoàn thành đúng hạn?",
          ["10 người", "15 người", "20 người", "5 người"], 1,
          "Cần 900 người-ngày, trong 15 ngày cần 60 người; thêm 15 người."),
        q("Chia 60 thành hai phần tỉ lệ với 2 và 3, phần lớn là:",
          ["36", "24", "30", "40"], 0,
          "k = 60/5 = 12, phần lớn 3 · 12 = 36."),
        q("Nếu x/3 = y/5 và x + y = 16, thì y bằng:",
          ["10", "6", "8", "16"], 0,
          "k = 2, y = 5 · 2 = 10."),
        q("Nếu x/2 = y/3 và y − x = 5, thì x bằng:",
          ["10", "15", "5", "2"], 0,
          "k = 5/(3 − 2) = 5, x = 2 · 5 = 10."),
    ],
    bt_co_ban=[
        bt("Bài 6.7: x/9 = y/11 và x + y = 40. Tìm x (ghi số).",
           ["18"], "k = 40/20 = 2, x = 18."),
        bt("Bài 6.8: x/17 = y/21 và x − y = 8. Tìm x (ghi số, có dấu).",
           ["−34", "-34"], "k = −2, x = −34."),
        bt("Bài 6.10: ba lớp trồng 120 cây tỉ lệ với 7; 8; 9. Lớp 7A trồng bao nhiêu cây? (ghi số)",
           ["35"], "7 · 5 = 35."),
        bt("Bài 6.14: tỉ số học sinh lớp 7A và 7B là 0,95; lớp 7B nhiều hơn 2 em. Lớp 7A có bao nhiêu học sinh? (ghi số)",
           ["38"], "19 · 2 = 38."),
        bt("Bài 6.16: x/2 = y/3 = z/4 và x + 2y − 3z = −12. Tìm x (ghi số).",
           ["6"], "k = 3, x = 6."),
        bt("Ví dụ 2: nhà từ thiện thứ nhất đóng góp bao nhiêu triệu đồng? (ghi số)",
           ["90"], "Tỉ lệ 3 : 5 : 7, tổng 450."),
    ],
    bt_nang_cao=[
        nc("Bài 6.9: tỉ số sản phẩm làm được của hai công nhân là 0,95 (tức 19 : 20 với người thứ nhất : người thứ hai), người thứ hai làm nhiều hơn người thứ nhất 10 sản phẩm. Người làm nhiều hơn làm được bao nhiêu sản phẩm?",
           "Đặt số sản phẩm của hai người là 19k và 20k, dùng hiệu bằng 10.",
           ["200"],
           "Hiệu 20k − 19k = k = 10. Người làm nhiều hơn làm 200 sản phẩm; người kia làm 190 sản phẩm."),
        nc("Bài 6.15: đường làm trong 15 ngày; 45 người làm 10 ngày được nửa công việc. Cần bổ sung thêm bao nhiêu người? (ghi số)",
           "Tổng công việc = 2 · 45 · 10 = 900 người-ngày.",
           ["15"],
           "900/15 = 60 người cần; 60 − 45 = 15 người."),
    ],
)


# ============================================================
# BÀI 22: ĐẠI LƯỢNG TỈ LỆ THUẬN
# ============================================================
B22 = bai(
    ly_thuyet="""📌 1. ĐẠI LƯỢNG TỈ LỆ THUẬN
- Nếu đại lượng y liên hệ với đại lượng x theo công thức y = ax (a là hằng số khác 0) thì ta nói y tỉ lệ thuận với x theo hệ số tỉ lệ a.
- Khi đó x cũng tỉ lệ thuận với y theo hệ số 1/a (vì x = (1/a)·y).

📌 2. TÍNH CHẤT
- Nếu y tỉ lệ thuận với x theo hệ số a thì: với mỗi cặp giá trị tương ứng, tỉ số y/x luôn bằng a.
- Tỉ số hai giá trị bất kì của đại lượng này bằng tỉ số hai giá trị tương ứng của đại lượng kia: y1/y2 = x1/x2.
- Nếu y tỉ lệ thuận với x và z tỉ lệ thuận với y thì z tỉ lệ thuận với x.

📌 3. GIẢI BÀI TOÁN VỀ ĐẠI LƯỢNG TỈ LỆ THUẬN
- Xác định hai đại lượng tỉ lệ thuận, lập tỉ lệ thức/dãy tỉ số bằng nhau, rồi tính các giá trị chưa biết.""",
    vi_du="""Nhận biết (HĐ1, HĐ2): Ô tô chuyển động với vận tốc 60 km/h có quãng đường s = 60t. Khi t = 1, 1,5, 2, 3 giờ thì s = 60, 90, 120, 180 km. Ta có s tỉ lệ thuận với t theo hệ số 60.

Ví dụ 1: x và y tỉ lệ thuận, x = 2 khi y = −4. Hệ số a = y/x = −4/2 = −2, nên y = −2x. Khi x = 3 thì y = −6. Khi y = 0,8 thì x = −0,4.

Ví dụ 2: y tỉ lệ thuận với x theo hệ số 5, tức y = 5x. Bảng: x = 2, 3, 4 thì y = 10, 15, 20, và y/x = 5 với mọi cặp.

Ví dụ 3: Hai xưởng may, xưởng 1 có 25 công nhân, xưởng 2 có 30 công nhân, xưởng 2 may nhiều hơn xưởng 1 là 20 bộ. Gọi số bộ của mỗi xưởng là x, y: x/25 = y/30 = (y − x)/5 = 20/5 = 4. Suy ra x = 100, y = 120.

Ví dụ 4: 635 quyển vở chia cho ba lớp 7A, 7B, 7C tỉ lệ với sĩ số 40; 42; 45. Ta có x/40 = y/42 = z/45 = 635/127 = 5, suy ra x = 200, y = 210, z = 225.""",
    cau_hoi=[
        q("Nếu y = ax (a ≠ 0), ta nói y tỉ lệ thuận với x theo hệ số:",
          ["a", "x", "y", "1/a"], 0,
          "Hệ số tỉ lệ là a."),
        q("Trong HĐ2, quãng đường s = 60t (t giờ). Khi t = 2 giờ, s bằng:",
          ["60 km", "120 km", "30 km", "180 km"], 1,
          "s = 60 · 2 = 120 km."),
        q("Trong HĐ1, khi t = 1,5 giờ thì quãng đường là:",
          ["60 km", "90 km", "120 km", "75 km"], 1,
          "s = 60 · 1,5 = 90 km."),
        q("Trong chuyển động với vận tốc 60 km/h, công thức tính quãng đường s theo thời gian t là:",
          ["s = t/60", "s = 60t", "s = 60 + t", "s = t²"], 1,
          "s tỉ lệ thuận với t, hệ số 60."),
        q("Nếu y = 5x thì x tỉ lệ thuận với y theo hệ số:",
          ["5", "1/5", "−5", "0"], 1,
          "x = (1/5)·y nên hệ số là 1/5."),
        q("Nếu y tỉ lệ thuận với x theo hệ số a thì x tỉ lệ thuận với y theo hệ số:",
          ["a", "1/a", "−a", "a²"], 1,
          "x = (1/a)·y."),
        q("Ví dụ 1: x và y tỉ lệ thuận, x = 2 khi y = −4. Hệ số tỉ lệ a là:",
          ["−2", "2", "−4", "1/2"], 0,
          "a = y/x = −4/2 = −2."),
        q("Ví dụ 1: với y = −2x, khi x = 3 thì y bằng:",
          ["−6", "6", "−1,5", "−8"], 0,
          "y = −2 · 3 = −6."),
        q("Ví dụ 1: với y = −2x, khi y = 0,8 thì x bằng:",
          ["−0,4", "0,4", "−1,6", "1,6"], 0,
          "x = −(1/2) · 0,8 = −0,4."),
        q("Ví dụ 2: y = 5x. Khi x1 = 2 thì y1 bằng:",
          ["5", "10", "15", "20"], 1,
          "y1 = 5 · 2 = 10."),
        q("Ví dụ 2 Nhận xét: nếu y tỉ lệ thuận với x thì tỉ số y1/x1 = y2/x2 = ... bằng:",
          ["Tổng hai giá trị", "Hệ số tỉ lệ a", "Tích hai giá trị", "Hiệu hai giá trị"], 1,
          "Mọi tỉ số y/x bằng hệ số tỉ lệ a."),
        q("Luyện tập 1: trong 100 g đậu tương có 34 g protein. Hệ số tỉ lệ thuận của khối lượng protein theo khối lượng đậu tương là:",
          ["34", "0,34", "3,4", "100"], 1,
          "34 g/100 g = 0,34."),
        q("Nếu y tỉ lệ thuận với x theo hệ số a thì x và y là:",
          ["Hai đại lượng tỉ lệ thuận", "Hai đại lượng tỉ lệ nghịch", "Hai đại lượng không liên quan", "Hai đại lượng bằng nhau"], 0,
          "Đó là định nghĩa hai đại lượng tỉ lệ thuận."),
        q("Ví dụ 3: xưởng 1 có 25 công nhân, xưởng 2 có 30 công nhân. Xưởng 1 may được bao nhiêu bộ quần áo một ngày?",
          ["100", "120", "90", "150"], 0,
          "x = 4 · 25 = 100 bộ."),
        q("Ví dụ 3: xưởng 2 may được bao nhiêu bộ quần áo một ngày?",
          ["100", "120", "90", "150"], 1,
          "y = 4 · 30 = 120 bộ."),
        q("Luyện tập 2: hai thanh kim loại có thể tích 10 cm³ và 15 cm³, thanh nặng hơn thanh kia 40 g. Thanh nhẹ hơn nặng:",
          ["80 g", "120 g", "40 g", "200 g"], 0,
          "Hệ số k = 40/(15 − 10) = 8; thanh nhẹ 8 · 10 = 80 g."),
        q("Ví dụ 4: 635 quyển vở chia cho lớp 7A (sĩ số 40) lớp 7B (42), lớp 7C (45). Lớp 7A nhận được:",
          ["200 quyển", "210 quyển", "225 quyển", "190 quyển"], 0,
          "x = 5 · 40 = 200 quyển."),
        q("Ví dụ 4: lớp 7C nhận được bao nhiêu quyển vở?",
          ["200", "210", "225", "215"], 2,
          "z = 5 · 45 = 225 quyển."),
        q("Luyện tập 3: chia 1 tấn gạo thành ba phần tỉ lệ với 2; 3; 5. Phần thứ nhất là:",
          ["200 kg", "300 kg", "500 kg", "100 kg"], 0,
          "1000 : 10 = 100 kg mỗi đơn vị, phần thứ nhất 2 · 100 = 200 kg."),
        q("Luyện tập 3: phần thứ ba là:",
          ["200 kg", "300 kg", "500 kg", "100 kg"], 2,
          "5 · 100 = 500 kg."),
        q("Đối với hai đại lượng tỉ lệ thuận, tỉ số giữa hai giá trị tương ứng:",
          ["Không đổi", "Tăng dần", "Giảm dần", "Bằng 0"], 0,
          "Tỉ số y/x luôn bằng hệ số a."),
        q("Bài 6.17: x và y tỉ lệ thuận, x = 2 thì y = −6. Hệ số a là:",
          ["−3", "3", "−6", "−12"], 0,
          "a = −6/2 = −3."),
        q("Bài 6.17: với y = −3x, khi y = 9 thì x bằng:",
          ["−3", "3", "−9", "9"], 0,
          "x = 9/(−3) = −3."),
        q("Bài 6.18a: bảng x = 5, 9, 15, 24 và y = 15, 27, 45, 72 cho thấy hệ số tỉ lệ là:",
          ["1/3", "3", "2", "5"], 1,
          "15/5 = 27/9 = 45/15 = 72/24 = 3."),
        q("Bài 6.18b: bảng x = 4, 8, 16, 25 và y = 8, 16, 30, 50 có phải tỉ lệ thuận không?",
          ["Có", "Không", "Chỉ một phần", "Không xác định"], 1,
          "8/4 = 2, 16/8 = 2 nhưng 30/16 khác 2, nên không tỉ lệ thuận."),
        q("Bài 6.19: y tỉ lệ thuận với x theo hệ số a, x tỉ lệ thuận với z theo hệ số b. Khi đó y tỉ lệ thuận với z theo hệ số:",
          ["a·b", "a + b", "a/b", "b − a"], 0,
          "y = ax = a·bz."),
        q("Bài 6.20: hai bể có cùng chiều dài và chiều rộng, chiều cao bể thứ nhất bằng 3/4 bể thứ hai. Bơm đầy bể thứ nhất mất 4,5 giờ. Bơm đầy bể thứ hai mất:",
          ["6 giờ", "4,5 giờ", "3 giờ", "5 giờ"], 0,
          "Thể tích bể 2 = 4/3 bể 1, thời gian 4,5 · 4/3 = 6 giờ."),
        q("Bài 6.21: chia 1,5 lít hoá chất thành ba phần tỉ lệ với 4; 5; 6. Lọ thứ nhất đựng:",
          ["0,4 lít", "0,5 lít", "0,6 lít", "1 lít"], 0,
          "k = 1,5/15 = 0,1; lọ 1 là 4 · 0,1 = 0,4 lít."),
        q("Bài 6.21: lọ thứ ba đựng:",
          ["0,4 lít", "0,5 lít", "0,6 lít", "0,3 lít"], 2,
          "6 · 0,1 = 0,6 lít."),
        q("Nếu x tỉ lệ thuận với y theo hệ số 2 và y tỉ lệ thuận với z theo hệ số 3 thì x tỉ lệ thuận với z theo hệ số:",
          ["5", "6", "1,5", "2/3"], 1,
          "x = 2y = 2 · 3z = 6z."),
    ],
    bt_co_ban=[
        bt("HĐ1: quãng đường ô tô đi trong 1,5 giờ với vận tốc 60 km/h là bao nhiêu km? (ghi số)",
           ["90"], "s = 60 · 1,5."),
        bt("Mở đầu: 4,5 kg củ sắn dây tươi cho 1 kg bột. Với 300 kg củ tươi (3 tạ) thu được bao nhiêu kg bột? (làm tròn 1 chữ số thập phân)",
           ["66,7", "66.7"], "300 : 4,5 ≈ 66,7 kg."),
        bt("Ví dụ 3: xưởng thứ nhất may được bao nhiêu bộ quần áo một ngày? (ghi số)",
           ["100"], "x = 4 · 25."),
        bt("Ví dụ 4: lớp 7A nhận được bao nhiêu quyển vở? (ghi số)",
           ["200"], "5 · 40 = 200."),
        bt("Bài 6.17: x và y tỉ lệ thuận, x = 2 thì y = −6. Hệ số a là bao nhiêu? (ghi số, có dấu)",
           ["−3", "-3"], "a = −6/2 = −3."),
        bt("Bài 6.20: nếu bể thứ nhất đầy trong 4,5 giờ, bể thứ hai (cao hơn 4/3 lần) đầy trong bao nhiêu giờ? (ghi số)",
           ["6"], "4,5 · 4/3 = 6."),
    ],
    bt_nang_cao=[
        nc("Bài 6.18: bảng x = 5; 9; 15; 24 và y = 15; 27; 45; 72 có phải hai đại lượng tỉ lệ thuận không? (trả lời 'có' hoặc 'không')",
           "Kiểm tra y/x có luôn bằng nhau không.",
           ["có", "Có"],
           "y/x = 3 với mọi cặp giá trị nên là hai đại lượng tỉ lệ thuận."),
        nc("Bài 6.19: y tỉ lệ thuận với x theo hệ số a, x tỉ lệ thuận với z theo hệ số b. y có tỉ lệ thuận với z không? Nếu có, hệ số là bao nhiêu? (ghi biểu thức theo a, b)",
           "y = ax, x = bz.",
           ["ab", "a·b", "a.b"],
           "y = a · b · z nên y tỉ lệ thuận với z, hệ số ab."),
    ],
)


# ============================================================
# BÀI 23: ĐẠI LƯỢNG TỈ LỆ NGHỊCH
# ============================================================
B23 = bai(
    ly_thuyet="""📌 1. ĐẠI LƯỢNG TỈ LỆ NGHỊCH
- Nếu đại lượng y liên hệ với đại lượng x theo công thức y = a/x (a là hằng số khác 0) thì ta nói y tỉ lệ nghịch với x theo hệ số tỉ lệ a.
- Khi đó x cũng tỉ lệ nghịch với y theo hệ số a.

📌 2. TÍNH CHẤT
- Tích hai giá trị tương ứng của hai đại lượng tỉ lệ nghịch luôn không đổi và bằng hệ số tỉ lệ: x1·y1 = x2·y2 = ... = a.
- Tỉ số hai giá trị bất kì của đại lượng này bằng nghịch đảo của tỉ số hai giá trị tương ứng của đại lượng kia: y1/y2 = x2/x1.

📌 3. GIẢI BÀI TOÁN VỀ ĐẠI LƯỢNG TỈ LỆ NGHỊCH
- Xác định hai đại lượng tỉ lệ nghịch, lập đẳng thức x1·y1 = x2·y2 hoặc dãy tỉ số bằng nhau với nghịch đảo, rồi tính.
- Mẹo: khi chia số theo tỉ lệ nghịch với a, b, c, ta chia theo tỉ lệ thuận với 1/a, 1/b, 1/c.""",
    vi_du="""Nhận biết (HĐ1, HĐ2): Ô tô đi quãng đường 180 km với vận tốc v, thời gian t = 180/v. Với v = 40, 50, 60, 80 km/h thì t = 4,5; 3,6; 3; 2,25 giờ. Thời gian t tỉ lệ nghịch với vận tốc v.

Ví dụ 1: x và y tỉ lệ nghịch, x = 2 khi y = −4. Hệ số a = xy = 2·(−4) = −8, y = −8/x. Khi x = 4 thì y = −2. Khi y = 0,5 thì x = −16.

Ví dụ 2: y tỉ lệ nghịch với x, a = 12, y = 12/x. Bảng: x = 2, 3, 4 thì y = 6, 4, 3, và x·y = 12 với mọi cặp.

Ví dụ 3: 4 thợ cùng xây một bức tường trong 9 ngày. Với 6 thợ: x/9 = 4/6, suy ra x = 4·9/6 = 6 ngày.

Ví dụ 4: 65 quả trứng gồm 3 loại, giá tiền mỗi loại như nhau: 4x = 3y = 2z. Chia theo tỉ lệ nghịch với 4; 3; 2 ta được x : y : z = 15 : 20 : 30 quả, tức 15, 20 và 30 quả.

Luyện tập 3: An mua 34 quyển vở, ba loại có giá 12 nghìn, 18 nghìn, 20 nghìn đồng và số tiền mỗi loại bằng nhau: số quyển là 15, 10, 9 (vì 15·12 = 10·18 = 9·20 = 180).""",
    cau_hoi=[
        q("Nếu y = a/x (a ≠ 0), ta nói y tỉ lệ nghịch với x theo hệ số:",
          ["a", "1/a", "x", "−a"], 0,
          "Hệ số tỉ lệ nghịch là a."),
        q("HĐ1: ô tô đi 180 km với vận tốc 40 km/h thì thời gian là:",
          ["4,5 giờ", "3,6 giờ", "7,2 giờ", "4 giờ"], 0,
          "t = 180/40 = 4,5 giờ."),
        q("HĐ1: với vận tốc 60 km/h thì thời gian đi 180 km là:",
          ["2 giờ", "3 giờ", "4 giờ", "5 giờ"], 1,
          "t = 180/60 = 3 giờ."),
        q("HĐ2: công thức tính thời gian t theo vận tốc v là:",
          ["t = 180v", "t = 180/v", "t = v/180", "t = 180 − v"], 1,
          "t tỉ lệ nghịch với v, hệ số 180."),
        q("Vận tốc và thời gian đi cùng một quãng đường có tỉ lệ nghịch không?",
          ["Có", "Không", "Không xác định", "Chỉ khi v = 180"], 0,
          "t = 180/v nên tỉ lệ nghịch."),
        q("Nếu y tỉ lệ nghịch với x theo hệ số a thì x tỉ lệ nghịch với y theo hệ số:",
          ["a", "1/a", "−a", "a²"], 0,
          "x = a/y, cùng hệ số a."),
        q("Ví dụ 1: x và y tỉ lệ nghịch, x = 2 khi y = −4. Hệ số a là:",
          ["−8", "8", "−2", "2"], 0,
          "a = 2 · (−4) = −8."),
        q("Ví dụ 1: với y = −8/x, khi x = 4 thì y bằng:",
          ["−2", "2", "−8", "8"], 0,
          "y = −8/4 = −2."),
        q("Ví dụ 1: với y = −8/x, khi y = 0,5 thì x bằng:",
          ["−16", "16", "−4", "4"], 0,
          "x = −8/0,5 = −16."),
        q("Ví dụ 2: y tỉ lệ nghịch với x, a = 12. Khi x = 2 thì y bằng:",
          ["6", "12", "24", "3"], 0,
          "y = 12/2 = 6."),
        q("Ví dụ 2: khi x = 4 thì y bằng:",
          ["3", "4", "12", "6"], 0,
          "y = 12/4 = 3."),
        q("Ví dụ 2 Nhận xét: với hai đại lượng tỉ lệ nghịch, tích x·y luôn:",
          ["Bằng tổng x + y", "Bằng hệ số tỉ lệ a", "Bằng hiệu x − y", "Bằng thương x/y"], 1,
          "Tích x·y = a không đổi."),
        q("Luyện tập 1: hai hình chữ nhật có cùng diện tích 12 cm² thì chiều dài và chiều rộng tỉ lệ nghịch với hệ số:",
          ["12", "6", "24", "1/12"], 0,
          "Chiều dài · chiều rộng = 12."),
        q("Vận dụng 1: 300 kg gạo đóng thành túi mỗi túi 5 kg, cần bao nhiêu túi?",
          ["60", "30", "15", "20"], 0,
          "300/5 = 60 túi."),
        q("Vận dụng 1: 15 túi thì mỗi túi có bao nhiêu kg?",
          ["20 kg", "15 kg", "12 kg", "25 kg"], 0,
          "300/15 = 20 kg."),
        q("Vận dụng 1: 12 túi thì mỗi túi có bao nhiêu kg?",
          ["20", "25", "30", "15"], 1,
          "300/12 = 25 kg."),
        q("Ví dụ 3: 4 thợ cùng xây xong bức tường trong 9 ngày. Với 6 thợ cùng làm thì mất bao nhiêu ngày?",
          ["4 ngày", "6 ngày", "9 ngày", "12 ngày"], 1,
          "4 · 9 = 6 · x suy ra x = 6 ngày."),
        q("Luyện tập 2: 280 công nhân hoàn thành hợp đồng trong 12 tháng. Để hoàn thành trong 10 tháng cần bao nhiêu công nhân?",
          ["336", "300", "240", "350"], 0,
          "280 · 12 / 10 = 336 công nhân."),
        q("Ví dụ 4: số quả trứng loại I là bao nhiêu?",
          ["15", "20", "30", "10"], 0,
          "x = (1/4)·60 = 15."),
        q("Ví dụ 4: số quả trứng loại III là bao nhiêu?",
          ["15", "20", "30", "25"], 2,
          "z = (1/2)·60 = 30."),
        q("Luyện tập 3: số quyển vở loại 120 trang (giá 12 nghìn) là bao nhiêu?",
          ["15", "10", "9", "20"], 0,
          "15 · 12 = 180 nghìn đồng."),
        q("Luyện tập 3: số quyển vở loại 240 trang (giá 20 nghìn) là bao nhiêu?",
          ["15", "10", "9", "8"], 2,
          "9 · 20 = 180 nghìn đồng."),
        q("Bài 6.22: x và y tỉ lệ nghịch, x = 2 thì y = −6. Hệ số a là:",
          ["−12", "12", "−3", "3"], 0,
          "a = 2 · (−6) = −12."),
        q("Bài 6.22: với y = −12/x, khi y = 3 thì x bằng:",
          ["−4", "4", "−12", "12"], 0,
          "x = −12/3 = −4."),
        q("Bài 6.23a: bảng x = 3, 6, 16, 24 và y = 160, 80, 30, 20 có tỉ lệ nghịch không?",
          ["Có, hệ số 480", "Không", "Có, hệ số 160", "Có, hệ số 20"], 0,
          "3·160 = 6·80 = 16·30 = 24·20 = 480."),
        q("Bài 6.23b: bảng x = 4, 8, 25, 32 và y = 160, 80, 26, 20 có tỉ lệ nghịch không?",
          ["Có", "Không", "Có, hệ số 640", "Không xác định"], 1,
          "4·160 = 640, 8·80 = 640 nhưng 25·26 = 650 khác."),
        q("Bài 6.24: y tỉ lệ nghịch với x theo hệ số a, x tỉ lệ nghịch với z theo hệ số b. Khi đó y tỉ lệ thuận với z theo hệ số:",
          ["a/b", "a·b", "a + b", "b/a"], 0,
          "y = a/x và x = b/z suy ra y = (a/b)·z."),
        q("Bài 6.25: với cùng số tiền, mua 17 tập giấy loại I (giá P) thì mua được bao nhiêu tập loại II (giá 0,85P)?",
          ["20 tập", "17 tập", "14 tập", "15 tập"], 0,
          "17P/(0,85P) = 20 tập."),
        q("Bài 6.26: ba đội máy cày làm trên ba cánh đồng cùng diện tích. Đội 1 xong trong 4 ngày, đội 2 trong 6 ngày, đội 3 trong 8 ngày. Đội 1 có bao nhiêu máy, biết đội 1 nhiều hơn đội 2 là 2 máy?",
          ["6", "4", "3", "8"], 0,
          "4m1 = 6m2 = 8m3 = 24 nên m1 = 6, m2 = 4, m3 = 3."),
        q("Bài 6.26: đội 3 có bao nhiêu máy?",
          ["6", "4", "3", "8"], 2,
          "m3 = 24/8 = 3 máy."),
        q("LTC Ví dụ 1: x tỉ lệ thuận với y theo hệ số 2, y tỉ lệ nghịch với z theo hệ số 3. Khi đó x tỉ lệ nghịch với z theo hệ số:",
          ["6", "5", "3", "2/3"], 0,
          "x = 2y = 2·3/z = 6/z."),
        q("LTC Ví dụ 2: giá một quyển vở 120 trang bằng 80% giá một quyển 200 trang. Với số tiền mua 16 quyển 200 trang, mua được bao nhiêu quyển 120 trang?",
          ["20", "16", "12", "24"], 0,
          "16 = 0,8 · x suy ra x = 20."),
        q("LTC Ví dụ 3: chu vi tam giác 48 cm, các cạnh tỉ lệ với 3; 4; 5. Cạnh lớn nhất là:",
          ["12 cm", "16 cm", "20 cm", "24 cm"], 2,
          "k = 48/12 = 4, cạnh lớn nhất 4 · 5 = 20 cm."),
    ],
    bt_co_ban=[
        bt("HĐ1: ô tô đi 180 km với vận tốc 40 km/h mất bao nhiêu giờ? (ghi số thập phân)",
           ["4,5", "4.5"], "t = 180/40 = 4,5."),
        bt("Bài 6.22: x và y tỉ lệ nghịch, x = 2 thì y = −6. Hệ số a là bao nhiêu? (ghi số, có dấu)",
           ["−12", "-12"], "a = 2 · (−6) = −12."),
        bt("Bài 6.25: với cùng số tiền, mua 17 tập loại I thì mua được bao nhiêu tập loại II (giá bằng 85% loại I)? (ghi số)",
           ["20"], "17 : 0,85 = 20."),
        bt("Bài 6.26: đội 1 có bao nhiêu máy cày? (ghi số)",
           ["6"], "m1 = 24/4 = 6."),
        bt("LTC Ví dụ 2: với số tiền để mua 16 quyển 200 trang, mua được bao nhiêu quyển 120 trang? (ghi số)",
           ["20"], "16/0,8 = 20."),
        bt("Luyện tập 2: 280 công nhân hoàn thành hợp đồng trong 12 tháng. Để hoàn thành trong 10 tháng cần bao nhiêu công nhân? (ghi số)",
           ["336"], "280 · 12/10 = 336."),
    ],
    bt_nang_cao=[
        nc("Bài 6.23: bảng x = 3, 6, 16, 24 và y = 160, 80, 30, 20 có tỉ lệ nghịch không? (trả lời 'có' hoặc 'không')",
           "Kiểm tra tích x·y có luôn bằng nhau không.",
           ["có", "Có"],
           "3·160 = 6·80 = 16·30 = 24·20 = 480 nên tỉ lệ nghịch với hệ số 480."),
        nc("Bài 6.26: đội 2 có bao nhiêu máy cày? (ghi số)",
           "m1 − m2 = 2 và m1 = 6, nên m2 = 4.",
           ["4"],
           "Đội 2 có 4 máy, đội 3 có 3 máy."),
        nc("Bài 6.24: y tỉ lệ nghịch với x theo hệ số a, x tỉ lệ nghịch với z theo hệ số b. Hệ số tỉ lệ thuận của y theo z là bao nhiêu? (ghi biểu thức theo a, b)",
           "y = a/x, x = b/z.",
           ["a/b", "a : b"],
           "y = a/(b/z) = (a/b)·z, hệ số a/b."),
        nc("Luyện tập 3 (Bài 23): An mua 34 quyển vở, số tiền mỗi loại bằng nhau. Số quyển loại 200 trang (giá 18 nghìn) là bao nhiêu? (ghi số)",
           "Số quyển tỉ lệ nghịch với giá: 12, 18, 20 cho 15, 10, 9.",
           ["10"],
           "10 · 18 = 180 nghìn đồng mỗi loại."),
        # ---- Luyện tập chung Chương VI (trang 19) ----
        nc("Luyện tập chung Ví dụ 1: cho x tỉ lệ thuận với y theo hệ số 2 và y tỉ lệ nghịch với z theo hệ số 3. Hệ số tỉ lệ nghịch của x với z là bao nhiêu? (ghi số)",
           "x = 2y, y = 3/z.",
           ["6"],
           "x = 2·3/z = 6/z nên x tỉ lệ nghịch với z theo hệ số 6."),
        # ---- Bài tập cuối chương VI (trang 21) ----
        nc("Bài 6.34: tìm x trong tỉ lệ thức x/2,5 = 10/15 (ghi số, ví dụ 5/3).",
           "x = 2,5 · 10/15.",
           ["5/3", "5 / 3"],
           "x = 2,5 · 10 / 15 = 5/3."),
        nc("Bài 6.36a: người cao 170 cm có chiều cao bằng bao nhiêu inch? Làm tròn đến hàng đơn vị. (1 in = 2,54 cm, ghi số)",
           "170 : 2,54 ≈ 66,9.",
           ["67"],
           "170/2,54 ≈ 66,9, làm tròn thành 67 inch."),
        nc("Bài 6.36b: chiều cao tính theo cm có tỉ lệ thuận với chiều cao tính theo inch không? Hệ số là bao nhiêu? (ghi số)",
           "1 in = 2,54 cm nên cm = 2,54 · in.",
           ["2,54", "2.54"],
           "Có, hai đại lượng tỉ lệ thuận với hệ số 2,54."),
        nc("Bài 6.37: số đo ba góc A, B, C của tam giác ABC tỉ lệ với 5; 6; 7. Số đo góc lớn nhất là bao nhiêu độ? (ghi số)",
           "Tổng 180°; k = 180/18 = 10.",
           ["70"],
           "A = 50°, B = 60°, C = 70°."),
        nc("Bài 6.38: ba đội công nhân làm cùng khối lượng, đội 1 làm trong 4 ngày, đội 2 trong 5 ngày, đội 3 trong 6 ngày. Đội 1 nhiều hơn đội 2 là 3 người. Đội 1 có bao nhiêu công nhân? (ghi số)",
           "Số công nhân tỉ lệ nghịch với số ngày; đặt n1·4 = n2·5 = n3·6 = K.",
           ["15"],
           "K = 60; n1 = 15, n2 = 12, n3 = 10."),
        nc("Bài 6.33: từ bốn số 0,2; 0,3; 0,8; 1,2 có thể lập được bao nhiêu tỉ lệ thức? (ghi số)",
           "Tích hai số ngoài bằng tích hai số trong: 0,2 · 1,2 = 0,3 · 0,8 = 0,24.",
           ["4"],
           "Có 4 tỉ lệ thức: 0,2:0,3=0,8:1,2; 0,2:0,8=0,3:1,2; 1,2:0,3=0,8:0,2; 1,2:0,8=0,3:0,2."),
    ],
)


CHUONG_6 = {
    "Chương VI: Tỉ lệ thức và đại lượng tỉ lệ": {
        "Bài 20: Tỉ lệ thức": B20,
        "Bài 21: Tính chất của dãy tỉ số bằng nhau": B21,
        "Bài 22: Đại lượng tỉ lệ thuận": B22,
        "Bài 23: Đại lượng tỉ lệ nghịch": B23,
    }
}

# ============================================================
# FILE toan_c7.py
# ============================================================
# ============================================================
# BÀI 24: BIỂU THỨC ĐẠI SỐ
# ============================================================
B24 = bai(
    ly_thuyet="""📌 1. BIỂU THỨC SỐ VÀ BIỂU THỨC ĐẠI SỐ
- Biểu thức không chứa chữ gọi là biểu thức số. Ví dụ: 23 + 8·9.
- Biểu thức chỉ chứa số hoặc chỉ chứa chữ, hoặc chứa cả số và chữ gọi là biểu thức đại số. Ví dụ: 3a + 7.
- Trong biểu thức đại số, các chữ (nếu có) dùng để thay thế hay đại diện cho những số nào đó gọi là các biến số (gọi tắt là biến).
- Một biểu thức đại số có thể chứa nhiều biến khác nhau.

📌 2. QUY ƯỚC VIẾT GỌN
- Không viết dấu nhân giữa các biến, giữa biến và số: a·b viết là ab; 2·a viết là 2a.
- Thường không viết thừa số 1 trong một tích: 1xy viết là xy; (−1)ab viết là −ab.
- x + x = 2x; x·x·x = x³; x + y = y + x; x(y + z) = xy + xz.

📌 3. GIÁ TRỊ CỦA BIỂU THỨC ĐẠI SỐ
- Để tính giá trị của một biểu thức đại số tại những giá trị cho trước của các biến, ta thay giá trị đã cho vào biểu thức rồi thực hiện các phép tính.""",
    vi_du="""Ví dụ: Bác Hoà mua cam giá 40 nghìn đồng/kg và một túi rau giá 15 nghìn đồng. Nếu mua x kg cam thì tổng số tiền là 40x + 15 (nghìn đồng). Với x = 2,5 kg: 40 · 2,5 + 15 = 115 nghìn đồng.

Vận dụng: Đi ô tô 40 km/h trong x giờ rồi đi bộ 5 km/h trong y giờ thì tổng quãng đường là 40x + 5y (km). Với x = 2,5 và y = 0,5: 40 · 2,5 + 5 · 0,5 = 102,5 km.

Ví dụ giá trị: A = 3p − q với p = 5, q = 7 thì A = 3 · 5 − 7 = 8.""",
    cau_hoi=[
        q("Biểu thức không chứa chữ gọi là:",
          ["Biểu thức số", "Biểu thức đại số", "Đa thức", "Đơn thức"], 0,
          "Biểu thức không chứa chữ là biểu thức số."),
        q("Biểu thức chứa chữ gọi là:",
          ["Biểu thức số", "Biểu thức đại số", "Số hữu tỉ", "Hằng số"], 1,
          "Biểu thức chứa chữ là biểu thức đại số."),
        q("Biểu thức 23 + 8 · 9 là:",
          ["Biểu thức số", "Biểu thức chứa chữ", "Biểu thức đại số có biến", "Đa thức"], 0,
          "Biểu thức chỉ có số nên là biểu thức số."),
        q("Biểu thức 3a + 7 là:",
          ["Biểu thức số", "Biểu thức chứa chữ", "Biểu thức không có phép tính", "Một số"], 1,
          "Biểu thức có chữ a nên là biểu thức đại số."),
        q("Các biến của biểu thức 3a + b là:",
          ["a và b", "3", "1 và 3", "chỉ b"], 0,
          "Các chữ a, b là biến."),
        q("Các biến trong biểu thức 3x² − 1 là:",
          ["x", "3", "1", "−1"], 0,
          "Biến duy nhất là x."),
        q("Trong biểu thức đại số, các chữ đại diện cho:",
          ["Các số nào đó", "Các hàm số", "Các phép tính", "Các đa thức"], 0,
          "Các chữ thay thế cho các số."),
        q("Viết gọn a · b ta được:",
          ["ab", "a + b", "a − b", "a : b"], 0,
          "Không viết dấu nhân giữa các biến."),
        q("Viết gọn 2 · a ta được:",
          ["2a", "a2", "a + 2", "2 + a"], 0,
          "Viết số đứng trước biến: 2a."),
        q("Cách viết gọn của 1 · xy là:",
          ["xy", "1xy", "x1y", "xy1"], 0,
          "Thường không viết thừa số 1."),
        q("Cách viết gọn của (−1) · ab là:",
          ["−ab", "ab", "−a + b", "(−1)ab"], 0,
          "(−1)ab viết là −ab."),
        q("x + x bằng:",
          ["2x", "x²", "x + 1", "2"], 0,
          "Cộng hai số hạng giống nhau: x + x = 2x."),
        q("x · x · x bằng:",
          ["x³", "3x", "x + 3", "x²"], 0,
          "Ba thừa số x nên bằng x³."),
        q("x(y + z) bằng:",
          ["xy + xz", "xy + z", "x + yz", "xyz"], 0,
          "Tính chất phân phối của phép nhân với phép cộng."),
        q("Chu vi hình chữ nhật có chiều rộng x (cm), chiều dài hơn chiều rộng 3 cm là:",
          ["4x + 6", "2x + 3", "4x + 3", "2x + 6"], 0,
          "Chiều dài x + 3, chu vi 2(x + x + 3) = 4x + 6."),
        q("Giá trị của biểu thức 40x + 15 tại x = 2,5 là:",
          ["115", "100", "105", "120"], 0,
          "40 · 2,5 + 15 = 100 + 15 = 115."),
        q("Biểu thức 40x + 15 có bao nhiêu biến?",
          ["1", "2", "0", "3"], 0,
          "Chỉ có biến x."),
        q("Giá trị của biểu thức A = 3p − q tại p = 5 và q = 7 là:",
          ["8", "22", "−2", "1"], 0,
          "A = 3 · 5 − 7 = 8."),
        q("Biểu thức đại số biểu thị 'hai lần số a cộng 3' là:",
          ["2a + 3", "2 + a³", "2(a + 3)", "a + 3 + 2a"], 0,
          "Hai lần số a là 2a, cộng 3 được 2a + 3."),
        q("Vận dụng: đi ô tô 40 km/h trong x giờ rồi đi bộ 5 km/h trong y giờ. Biểu thức tổng quãng đường là:",
          ["40x + 5y", "40 + 5", "45(x + y)", "40x · 5y"], 0,
          "Quãng đường ô tô 40x, đi bộ 5y."),
        q("Vận dụng: với x = 2,5 và y = 0,5, tổng quãng đường bằng:",
          ["102,5 km", "105 km", "100 km", "97,5 km"], 0,
          "40 · 2,5 + 5 · 0,5 = 100 + 2,5 = 102,5."),
        q("Bài 7.1a: nửa tổng của x và y được biểu thị bởi biểu thức:",
          ["(x + y)/2", "x + y/2", "x/2 + y", "2(x + y)"], 0,
          "Nửa tổng là (x + y) : 2."),
        q("Bài 7.2: diện tích hình thang có hai đáy a, b và chiều cao h là:",
          ["(a + b)h/2", "ab · h/2", "(a + b) · h", "a + b + h"], 0,
          "Công thức diện tích hình thang."),
        q("Bài 7.3a: giá trị của 4x + 3 tại x = 5,8 là:",
          ["26,2", "26", "23,2", "29"], 0,
          "4 · 5,8 + 3 = 23,2 + 3 = 26,2."),
        q("Bài 7.3b: giá trị của y² − 2y + 1 tại y = 2 là:",
          ["1", "0", "4", "−1"], 0,
          "4 − 4 + 1 = 1."),
        q("Bài 7.3c: giá trị của (2m + n)(m − n) tại m = 5,4 và n = 3,2 là:",
          ["30,8", "28", "15,4", "31"], 0,
          "(10,8 + 3,2)(5,4 − 3,2) = 14 · 2,2 = 30,8."),
        q("Biểu thức (a + b)² có chứa mấy biến?",
          ["2", "1", "0", "3"], 0,
          "Có hai biến a và b."),
        q("Cách viết gọn của x · x · y là:",
          ["x²y", "2xy", "xy²", "x + x + y"], 0,
          "x · x = x², nhân với y."),
        q("Cách viết gọn của 5 · a · b là:",
          ["5ab", "ab5", "5 + ab", "a5b"], 0,
          "Viết số đứng trước các biến."),
        q("Giá trị của x + y + z khi x = 1, y = 2, z = 3 là:",
          ["6", "5", "7", "8"], 0,
          "1 + 2 + 3 = 6."),
        q("Bài 7.4b: máy bơm thứ nhất 5 m³/h chạy x = 2 giờ, máy thứ hai 3,5 m³/h chạy y = 3 giờ. Tổng lượng nước bơm được là:",
          ["20,5 m³", "18 m³", "21 m³", "13 m³"], 0,
          "5 · 2 + 3,5 · 3 = 10 + 10,5 = 20,5 m³."),
    ],
    bt_co_ban=[
        bt("Ví dụ: tiền bác Hoà phải trả khi mua 2,5 kg cam (nghìn đồng), dùng biểu thức 40x + 15. Ghi số tiền.",
           ["115", "115000", "115 000"], "40 · 2,5 + 15 = 115."),
        bt("Bài 7.3a: giá trị của 4x + 3 tại x = 5,8 là bao nhiêu? (ghi số thập phân)",
           ["26,2", "26.2"], "4 · 5,8 + 3 = 26,2."),
        bt("Bài 7.3b: giá trị của y² − 2y + 1 tại y = 2 là bao nhiêu? (ghi số)",
           ["1"], "4 − 4 + 1 = 1."),
        bt("Bài 7.1a: viết biểu thức nửa tổng của x và y bằng cách dùng dấu chia (ví dụ: (x + y)/2). Ghi đáp số ở dạng này.",
           ["(x+y)/2", "(x + y)/2", "(x+y):2", "(x + y) : 2"], "Nửa tổng là (x + y) : 2."),
        bt("Bài 7.4b: tổng lượng nước hai máy bơm được khi x = 2 và y = 3 là bao nhiêu m³? (ghi số thập phân)",
           ["20,5", "20.5"], "5 · 2 + 3,5 · 3 = 20,5."),
    ],
    bt_nang_cao=[
        nc("Bài 7.1b: viết biểu thức biểu thị 'tổng của x và y nhân với tích của x và y'.",
           "Tổng là x + y, tích là xy.",
           ["(x+y)xy", "(x + y)xy", "xy(x + y)", "xy(x+y)"],
           "Biểu thức là (x + y) · xy."),
        nc("Bài 7.4a: máy bơm thứ nhất bơm 5 m³/h chạy x giờ, máy thứ hai bơm 3,5 m³/h chạy y giờ. Viết biểu thức đại số biểu thị lượng nước bơm được của hai máy.",
           "Lượng nước = (công suất) × (thời gian) cho từng máy.",
           ["5x + 3,5y", "5x+3,5y", "3,5y + 5x"],
           "Lượng nước của hai máy: 5x + 3,5y (m³)."),
        nc("Bài 7.3 (tổng quát): Thử thách nhỏ — Cho x = 1, tính giá trị của x³(x + 2) − x(x³ + 2³) − 2x(x² − 2²). Ghi kết quả.",
           "Rút gọn biểu thức trước khi thay số.",
           ["0"],
           "x⁴ + 2x³ − x⁴ − 8x − 2x³ + 8x = 0 với mọi x."),
    ],
)


# ============================================================
# BÀI 25: ĐA THỨC MỘT BIẾN
# ============================================================
B25 = bai(
    ly_thuyet="""📌 1. ĐƠN THỨC MỘT BIẾN
- Đơn thức một biến (gọi tắt là đơn thức) là biểu thức đại số có dạng tích của một số thực với một lũy thừa của biến.
- Số thực đó gọi là hệ số; số mũ của lũy thừa của biến gọi là bậc của đơn thức.
- Ví dụ: 4x³ có hệ số 4, bậc 3. −0,5x có hệ số −0,5, bậc 1. Một số khác 0 là đơn thức bậc 0.
- Số 0 cũng được coi là một đơn thức (không có bậc).

📌 2. ĐA THỨC MỘT BIẾN
- Đa thức một biến (gọi tắt là đa thức) là tổng của những đơn thức của cùng một biến. Mỗi đơn thức trong tổng là một hạng tử của đa thức.
- Số 0 cũng được coi là một đa thức, gọi là đa thức không.
- Ví dụ: 2x³ − 5x² + 7 có ba hạng tử là 2x³; −5x² và 7.

📌 3. ĐA THỨC THU GỌN, SẮP XẾP, BẬC, HỆ SỐ
- Đa thức thu gọn là đa thức không chứa hai đơn thức nào cùng bậc.
- Muốn thu gọn đa thức, ta cộng các đơn thức cùng bậc.
- Khi sắp xếp: viết các hạng tử theo lũy thừa giảm (hoặc tăng) của biến.
- Bậc của đa thức khác đa thức không là bậc cao nhất của các hạng tử; hệ số của hạng tử bậc cao nhất gọi là hệ số cao nhất; hệ số của hạng tử bậc 0 gọi là hệ số tự do.

📌 4. NGHIỆM CỦA ĐA THỨC
- Giá trị của đa thức F(x) tại x = a là F(a).
- Nếu F(a) = 0 thì a (hoặc x = a) là một nghiệm của đa thức F(x).
- Nếu hệ số tự do của đa thức bằng 0 thì x = 0 là một nghiệm của đa thức.""",
    vi_du="""Ví dụ 3: Thu gọn P = −x³ − 2x² + x³ + 4x + 5 = −2x² + 4x + 5. Bậc của P là 2, hệ số cao nhất là −2, hệ số tự do là 5.

Ví dụ 4: A(x) = 2x² + 6x có nghiệm x = −3 và x = 0 (vì A(−3) = 0 và A(0) = 0). B(x) = x² + 1 không có nghiệm vì x² + 1 ≥ 1 > 0 với mọi x.

Luyện tập 6 / Vận dụng: H(x) = −5x² + 15x có hệ số tự do bằng 0 nên x = 0 là nghiệm; H(3) = −45 + 45 = 0 nên x = 3 là nghiệm khác 0.""",
    cau_hoi=[
        q("Đơn thức một biến là biểu thức có dạng:",
          ["Tích của một số thực với một lũy thừa của biến", "Tổng các số", "Thương hai số", "Biểu thức có căn thức"], 0,
          "Đơn thức có dạng a·x^n."),
        q("Bậc của đơn thức 4x³ là:",
          ["3", "4", "1", "0"], 0,
          "Số mũ của x là 3."),
        q("Hệ số của đơn thức 4x³ là:",
          ["4", "3", "x³", "12"], 0,
          "Hệ số là số đứng trước lũy thừa."),
        q("Hệ số của đơn thức −0,5x là:",
          ["−0,5", "0,5", "−1", "1"], 0,
          "Hệ số là −0,5."),
        q("Bậc của đơn thức −0,5x là:",
          ["1", "0", "2", "−0,5"], 0,
          "x = x¹ nên bậc là 1."),
        q("Một số khác 0 là đơn thức có bậc:",
          ["0", "1", "2", "không có bậc"], 0,
          "Ví dụ: 2 = 2x⁰, bậc 0."),
        q("Số 0 là đơn thức như thế nào?",
          ["Là đơn thức không có bậc", "Là đơn thức bậc 0", "Không phải đơn thức", "Là đơn thức bậc 1"], 0,
          "Số 0 được coi là đơn thức nhưng không có bậc."),
        q("Hệ số của đơn thức 2x⁶ là:",
          ["2", "6", "x⁶", "12"], 0,
          "Hệ số là 2."),
        q("Bậc của đơn thức 2x⁶ là:",
          ["6", "2", "1", "0"], 0,
          "Bậc là số mũ 6."),
        q("Hệ số của đơn thức −(1/5)x² là:",
          ["−1/5", "1/5", "−5", "2"], 0,
          "Hệ số là −1/5."),
        q("Hệ số của đơn thức 3²x là:",
          ["9", "3", "2", "6"], 0,
          "3² = 9 nên hệ số là 9."),
        q("Đa thức một biến là:",
          ["Tổng của những đơn thức cùng một biến", "Tích các đơn thức", "Thương hai đơn thức", "Một số thực"], 0,
          "Định nghĩa đa thức một biến."),
        q("Các hạng tử của đa thức 2x³ − 5x² + 7 là:",
          ["2x³; −5x²; 7", "2x³; 5x²; 7", "2x³; −5x; 7", "2; −5; 7"], 0,
          "Các đơn thức trong tổng là các hạng tử."),
        q("Các hạng tử của đa thức B = 2x⁴ − 3x² + x + 1 là:",
          ["2x⁴; −3x²; x; 1", "2x⁴; 3x²; x; 1", "2x⁴; −3x²; x", "2x⁴; −3x²; 1"], 0,
          "Có bốn hạng tử."),
        q("Đa thức P = −3x⁴ + 5x² − 2x + 1 có bậc là:",
          ["4", "2", "1", "3"], 0,
          "Hạng tử bậc cao nhất là −3x⁴."),
        q("Hệ số cao nhất của P = −3x⁴ + 5x² − 2x + 1 là:",
          ["−3", "5", "−2", "1"], 0,
          "Hệ số của hạng tử bậc 4."),
        q("Hệ số tự do của P = −3x⁴ + 5x² − 2x + 1 là:",
          ["1", "−3", "5", "−2"], 0,
          "Hạng tử bậc 0 là 1."),
        q("Đa thức P = −x³ − 2x² + x³ + 4x + 5 khi thu gọn có bậc là:",
          ["2", "3", "1", "5"], 0,
          "Thu gọn được −2x² + 4x + 5 nên bậc là 2."),
        q("Hệ số cao nhất của đa thức P thu gọn (−2x² + 4x + 5) là:",
          ["−2", "4", "5", "−1"], 0,
          "Hạng tử bậc 2 là −2x²."),
        q("Hệ số tự do của đa thức −2x² + 4x + 5 là:",
          ["5", "4", "−2", "0"], 0,
          "Hạng tử không chứa biến là 5."),
        q("Đa thức 7 (là số khác 0) có bậc là:",
          ["0", "1", "7", "không có bậc"], 0,
          "Đa thức hằng khác 0 có bậc 0."),
        q("Đa thức không (số 0) có bậc là:",
          ["Không có bậc", "0", "1", "−1"], 0,
          "Đa thức không không có bậc."),
        q("Bậc của đa thức 5x² − 2x + 1 − 3x⁴ là:",
          ["4", "2", "1", "5"], 0,
          "Hạng tử cao nhất là −3x⁴."),
        q("Hệ số cao nhất của đa thức 1,5x² − 3,4x⁴ + 0,5x² − 1 khi thu gọn là:",
          ["−3,4", "1,5", "2", "−1"], 0,
          "Thu gọn: −3,4x⁴ + 2x² − 1 nên hệ số cao nhất là −3,4."),
        q("Bài 7.5b: hệ số của đơn thức −2x³ (là kết quả (1/2)x³ − (5/2)x³) là:",
          ["−2", "2", "−3", "3"], 0,
          "(1/2 − 5/2)x³ = −2x³."),
        q("Bài 7.9: đa thức F(x) bậc 3, hệ số cao nhất −6, hệ số tự do 3, hệ số của x² bằng hệ số của x và bằng 2. Hệ số của x là:",
          ["2", "−6", "3", "−2"], 0,
          "F(x) = −6x³ + 2x² + 2x + 3."),
        q("Bài 7.10a: x = −1/8 có phải nghiệm của P(x) = 4x + 1/2 không?",
          ["Có", "Không", "Chỉ khi x = 1/8", "Không xác định"], 0,
          "4 · (−1/8) + 1/2 = −1/2 + 1/2 = 0."),
        q("Bài 7.10b: trong ba số 1; −1; 2, số nào là nghiệm của Q(x) = x² + x − 2?",
          ["1", "−1", "2", "Không có số nào"], 0,
          "Q(1) = 0; Q(−1) = −2; Q(2) = 4."),
        q("Ví dụ 4: số nào là nghiệm của A(x) = 2x² + 6x?",
          ["−3", "3", "2", "1"], 0,
          "A(−3) = 18 − 18 = 0."),
        q("Ví dụ 4: đa thức B(x) = x² + 1 có nghiệm không?",
          ["Không có nghiệm", "Có nghiệm x = 1", "Có nghiệm x = 0", "Có nghiệm x = −1"], 0,
          "x² + 1 ≥ 1 > 0 với mọi x."),
        q("Nếu một đa thức có hệ số tự do bằng 0 thì:",
          ["x = 0 là một nghiệm của đa thức", "x = 1 là một nghiệm", "đa thức không có nghiệm", "nghiệm là −1"], 0,
          "Khi x = 0, mọi hạng tử đều bằng 0 nếu hệ số tự do bằng 0."),
        q("Luyện tập 6: giá trị của F(x) = 2x² − 3x − 2 tại x = −1 là:",
          ["3", "−3", "1", "0"], 0,
          "2 + 3 − 2 = 3."),
        q("Luyện tập 6: giá trị của F(x) = 2x² − 3x − 2 tại x = 2 là:",
          ["0", "2", "−2", "4"], 0,
          "8 − 6 − 2 = 0, nên x = 2 là một nghiệm."),
        q("Vận dụng: nghiệm khác 0 của H(x) = −5x² + 15x là:",
          ["3", "−3", "5", "2"], 0,
          "H(3) = −45 + 45 = 0."),
        q("Bài 7.22 (Vận dụng): đa thức f(x) = K(x) − D(x) có nghiệm x = 1. Ý nghĩa của nghiệm này là:",
          ["Sau 1 giờ, hai xe cùng đi được quãng đường bằng nhau", "Xe khách đứng yên", "Xe du lịch về đích", "Hai xe chưa xuất phát"], 0,
          "f(1) = 0 nghĩa là quãng đường hai xe bằng nhau sau 1 giờ."),
    ],
    bt_co_ban=[
        bt("Bài 7.5a: hệ số của đơn thức nhận được khi tính (1/2 x³)(−4x²) là bao nhiêu? (ghi số)",
           ["−2", "-2"], "(1/2)(−4) = −2."),
        bt("Bài 7.5a: bậc của đơn thức (1/2 x³)(−4x²) là bao nhiêu? (ghi số)",
           ["5"], "x³ · x² = x⁵, bậc 5."),
        bt("Bài 7.18: hệ số của x² trong tổng A là bao nhiêu? (ghi dạng thập phân)",
           ["0,1", "0.1"], "3/5 − 1/2 = 1/10 = 0,1."),
        bt("Bài 7.18: hệ số cao nhất của đa thức A là bao nhiêu?",
           ["2"], "A = 2x⁶ − 3x⁵ − 4x³ + 0,1x² − 3x + 8."),
        bt("Bài 7.10a: x = −1/8 có phải nghiệm của P(x) = 4x + 1/2 không? (trả lời 'có' hoặc 'không')",
           ["có", "Có"], "4(−1/8) + 1/2 = 0."),
        bt("Ví dụ 4: nghiệm x = −3 của A(x) = 2x² + 6x có làm A(−3) = 0 không? (trả lời 'có' hoặc 'không')",
           ["có", "Có"], "A(−3) = 0."),
    ],
    bt_nang_cao=[
        nc("Bài 7.9: viết đa thức F(x) biết bậc của F là 3, hệ số của x² bằng hệ số của x và bằng 2, hệ số cao nhất bằng −6, hệ số tự do bằng 3. Hệ số của x là bao nhiêu?",
           "F(x) = −6x³ + 2x² + 2x + 3.",
           ["2"],
           "Hệ số của x cũng bằng 2."),
        nc("Bài 7.18: thu gọn tổng A của các đơn thức 2x⁶; −5x³; −3x⁵; x³; (3/5)x²; −(1/2)x²; 8; −3x. Hệ số của x³ trong A là bao nhiêu?",
           "Cộng các đơn thức cùng bậc: −5x³ + x³ = −4x³.",
           ["−4", "-4"],
           "A = 2x⁶ − 3x⁵ − 4x³ + 0,1x² − 3x + 8."),
        nc("Bài 7.20 (Đa thức nhiệt độ): T(x) = 1,8x + 32. Nhiệt độ 0°C tương ứng với bao nhiêu °F?",
           "Thay x = 0 vào T(x).",
           ["32"],
           "T(0) = 32 °F."),
    ],
)


# ============================================================
# BÀI 26: PHÉP CỘNG VÀ PHÉP TRỪ ĐA THỨC MỘT BIẾN
# ============================================================
B26 = bai(
    ly_thuyet="""📌 1. CỘNG HAI ĐA THỨC
- Cách 1: Bỏ dấu ngoặc rồi nhóm các hạng tử cùng bậc, cộng các hệ số.
- Cách 2: Đặt tính cộng sao cho các hạng tử cùng bậc đặt thẳng cột, rồi cộng theo từng cột. Nếu đa thức thiếu hạng tử nào thì để trống ô tương ứng.
- Tính chất: giao hoán A + B = B + A; kết hợp (A + B) + C = A + (B + C); cộng với đa thức không A + 0 = A.

📌 2. TRỪ HAI ĐA THỨC
- Hiệu P − Q = P + (−Q), tức là đổi dấu tất cả các hạng tử của Q rồi cộng với P.
- Cách 1: Bỏ ngoặc (đổi dấu các hạng tử của Q), nhóm các hạng tử cùng bậc.
- Cách 2: Đặt tính trừ: đặt Q dưới P, các hạng tử cùng bậc thẳng cột, rồi trừ theo từng cột.
- Nếu Q + R = P thì R = P − Q; nếu R = P − Q thì Q + R = P.""",
    vi_du="""Ví dụ: P = x⁴ + 3x³ − 5x² + 7x và Q = −x³ + 4x² − 2x + 1.
P + Q = x⁴ + 2x³ − x² + 5x + 1.
P − Q = x⁴ + 4x³ − 9x² + 9x − 1.

Luyện tập 1 / 2: M = 0,5x⁴ − 4x³ + 2x − 2,5 và N = 2x³ + x² + 1,5. Ta có M + N = 0,5x⁴ − 2x³ + x² + 2x − 1 và M − N = 0,5x⁴ − 6x³ − x² + 2x − 4.

Vận dụng 1: Tổng ba đa thức A = 2x³ − 5x² + x − 7; B = x² − 2x + 6; C = −x³ + 4x² − 1 là x³ − x − 2.""",
    cau_hoi=[
        q("Với P = x⁴ + 3x³ − 5x² + 7x và Q = −x³ + 4x² − 2x + 1, tổng P + Q bằng:",
          ["x⁴ + 2x³ − x² + 5x + 1", "x⁴ + 2x³ − 9x² + 5x + 1", "x⁴ + 4x³ − x² + 5x + 1", "x⁴ + 2x³ − x² + 9x + 1"], 0,
          "Cộng các hạng tử cùng bậc: x³: 3 − 1 = 2; x²: −5 + 4 = −1; x: 7 − 2 = 5; hằng số: 1."),
        q("Với P và Q như trên, hiệu P − Q bằng:",
          ["x⁴ + 4x³ − 9x² + 9x − 1", "x⁴ + 4x³ − x² + 9x − 1", "x⁴ + 2x³ − 9x² + 9x − 1", "x⁴ + 4x³ − 9x² + 5x − 1"], 0,
          "P − Q = P + (−Q)."),
        q("Tổng của x³ − 5x + 2 và x³ − x² + 6x − 4 là:",
          ["2x³ − x² + x − 2", "2x³ − x² + 11x − 2", "2x³ − 6x² + x − 2", "2x³ − x² − x − 2"], 0,
          "2x³ − x² + (−5 + 6)x + (2 − 4) = 2x³ − x² + x − 2."),
        q("Trong P + Q, hạng tử bậc 3 là:",
          ["2x³", "x³", "3x³", "−x³"], 0,
          "Hệ số bậc 3 là 3 − 1 = 2."),
        q("Bậc của P + Q (= x⁴ + 2x³ − x² + 5x + 1) là:",
          ["4", "3", "2", "5"], 0,
          "Hạng tử cao nhất là x⁴."),
        q("Hệ số của x⁴ trong P + Q là:",
          ["1", "2", "3", "4"], 0,
          "Chỉ có x⁴ trong P (hệ số 1)."),
        q("Phép cộng đa thức có tính chất giao hoán: A + B bằng:",
          ["B + A", "A − B", "A · B", "0"], 0,
          "Tính chất giao hoán."),
        q("Đa thức A cộng đa thức không bằng:",
          ["A", "0", "−A", "2A"], 0,
          "A + 0 = 0 + A = A."),
        q("Nếu Q + R = P thì R bằng:",
          ["P − Q", "Q − P", "P + Q", "P · Q"], 0,
          "Chuyển vế đổi dấu."),
        q("Nếu R = P − Q thì Q + R bằng:",
          ["P", "Q", "P + Q", "0"], 0,
          "Q + (P − Q) = P."),
        q("Luyện tập 1: M = 0,5x⁴ − 4x³ + 2x − 2,5 và N = 2x³ + x² + 1,5. Tổng M + N là:",
          ["0,5x⁴ − 2x³ + x² + 2x − 1", "0,5x⁴ − 2x³ + x² + 2x + 1", "0,5x⁴ − 6x³ + x² + 2x − 1", "0,5x⁴ − 2x³ − x² + 2x − 1"], 0,
          "−4x³ + 2x³ = −2x³; −2,5 + 1,5 = −1."),
        q("Luyện tập 2: hiệu M − N (M và N như trên) bằng:",
          ["0,5x⁴ − 6x³ − x² + 2x − 4", "0,5x⁴ − 2x³ − x² + 2x − 4", "0,5x⁴ − 6x³ + x² + 2x − 4", "0,5x⁴ − 6x³ − x² + 2x + 1"], 0,
          "−4x³ − 2x³ = −6x³; −x²; −2,5 − 1,5 = −4."),
        q("Hệ số của x² trong M − N là:",
          ["−1", "1", "−4", "2"], 0,
          "0 − 1 = −1."),
        q("Hệ số tự do của M + N là:",
          ["−1", "1", "−2,5", "1,5"], 0,
          "−2,5 + 1,5 = −1."),
        q("Vận dụng 1: tổng A + B + C với A = 2x³ − 5x² + x − 7; B = x² − 2x + 6; C = −x³ + 4x² − 1 bằng:",
          ["x³ − x − 2", "x³ − 2x − 2", "x³ + x − 2", "3x³ − x − 2"], 0,
          "x³: 2 − 1 = 1; x²: −5 + 1 + 4 = 0; x: 1 − 2 = −1; hằng: −7 + 6 − 1 = −2."),
        q("Bài 7.12: tổng của x² − 3x + 2 và 4x³ − x² + x − 1 bằng:",
          ["4x³ − 2x + 1", "4x³ − 2x² + 1", "4x³ − 4x + 3", "4x³ − 2x − 1"], 0,
          "x²: 1 − 1 = 0; x: −3 + 1 = −2; hằng: 2 − 1 = 1."),
        q("Bài 7.13: hiệu (−x³ − 5x + 2) − (3x + 8) bằng:",
          ["−x³ − 8x − 6", "−x³ − 2x − 6", "−x³ − 8x + 10", "x³ − 8x − 6"], 0,
          "−5x − 3x = −8x; 2 − 8 = −6."),
        q("Bài 7.14: A + B với A = 6x⁴ − 4x³ + x − 1/3 và B = −3x⁴ − 2x³ − 5x² + x + 2/3 bằng:",
          ["3x⁴ − 6x³ − 5x² + 2x + 1/3", "3x⁴ − 6x³ − 5x² + 2x − 1/3", "3x⁴ − 2x³ − 5x² + 2x + 1/3", "3x⁴ − 6x³ + 5x² + 2x + 1/3"], 0,
          "x⁴: 6 − 3 = 3; x³: −4 − 2 = −6; x²: −5; x: 1 + 1 = 2; hằng: −1/3 + 2/3 = 1/3."),
        q("Bài 7.14: A − B bằng:",
          ["9x⁴ − 2x³ + 5x² − 1", "9x⁴ − 6x³ + 5x² − 1", "3x⁴ − 2x³ + 5x² − 1", "9x⁴ − 2x³ − 5x² − 1"], 0,
          "x⁴: 6 + 3 = 9; x³: −4 + 2 = −2; x²: +5; x: 1 − 1 = 0; hằng: −1/3 − 2/3 = −1."),
        q("Bài 7.16: giá tiền ba loại sách: truyện tranh 15 000 đồng (x + 5 cuốn), sách tham khảo 12 500 đồng (x + 8 cuốn), sách khoa học 21 500 đồng (x cuốn). Tổng số tiền là:",
          ["49 000x + 175 000", "49 000x + 75 000", "49 000x + 100 000", "51 500x + 175 000"], 0,
          "15 000(x + 5) + 12 500(x + 8) + 21 500x = 49 000x + 175 000."),
        q("Cộng hai đa thức cùng bậc: x³ + x³ bằng:",
          ["2x³", "x⁶", "2x⁶", "x³"], 0,
          "Cộng các hệ số, giữ nguyên lũy thừa."),
        q("Trừ hai đơn thức cùng bậc: 3x² − x² bằng:",
          ["2x²", "2x⁴", "2x", "3x⁴"], 0,
          "Trừ các hệ số: 3 − 1 = 2."),
        q("A − A bằng:",
          ["0", "2A", "A", "−2A"], 0,
          "A + (−A) = 0."),
        q("Khi đặt tính cộng, nếu đa thức thiếu một hạng tử bậc nào đó thì:",
          ["Để trống ô tương ứng", "Bỏ qua", "Thêm 0 vào ô đó", "Tính sai"], 0,
          "Chỉ đặt các hạng tử hiện có thẳng cột."),
        q("Tổng của x³ + x² và −x² + 1 là:",
          ["x³ + 1", "x³ + 2x² + 1", "x³ − 2x² + 1", "x³ + 1 + x²"], 0,
          "x² − x² = 0."),
        q("Với P(x) = 2x² + 3x và Q(x) = −2x² + x, P + Q bằng:",
          ["4x", "4x²", "0", "x"], 0,
          "2x² − 2x² = 0; 3x + x = 4x."),
        q("Với P và Q như câu trên, P − Q bằng:",
          ["4x² + 2x", "4x² + 4x", "2x² + 2x", "0"], 0,
          "2x² + 3x + 2x² − x = 4x² + 2x."),
        q("Bậc của P + Q (đã nói ở trên, bằng 4x) là:",
          ["1", "2", "0", "không có bậc"], 0,
          "Đa thức 4x có bậc 1."),
        q("Hiệu của hai đa thức 5x − 2 và 5x − 2 bằng:",
          ["0", "10x − 4", "2", "5x"], 0,
          "Hai đa thức giống nhau nên hiệu bằng 0."),
        q("Tổng của 3x³ − 1 và −3x³ + 1 bằng:",
          ["0", "6x³", "−2", "2"], 0,
          "Các hạng tử đối nhau triệt tiêu."),
        q("Hệ số của x² trong M − N (Luyện tập 2) là:",
          ["−1", "1", "−4", "2"], 0,
          "Đã tính ở trên: −1."),
    ],
    bt_co_ban=[
        bt("Tính bậc của đa thức P + Q (với P = x⁴ + 3x³ − 5x² + 7x; Q = −x³ + 4x² − 2x + 1). (ghi số)",
           ["4"], "x⁴ là hạng tử bậc cao nhất."),
        bt("Hệ số của x³ trong P + Q (P và Q như trên) là bao nhiêu? (ghi số)",
           ["2"], "3 + (−1) = 2."),
        bt("Vận dụng 1: hệ số của x trong tổng A + B + C là bao nhiêu? (ghi số, có dấu)",
           ["−1", "-1"], "1 − 2 = −1."),
        bt("Bài 7.12: hệ số của x³ trong tổng x² − 3x + 2 và 4x³ − x² + x − 1 là bao nhiêu? (ghi số)",
           ["4"], "Chỉ có 4x³ có bậc 3."),
        bt("Bài 7.16: dùng đa thức 49 000x + 175 000 (x là số cuốn sách khoa học). Khi x = 10, tổng số tiền là bao nhiêu đồng? (ghi số)",
           ["665000", "665 000"], "49 000 · 10 + 175 000 = 665 000."),
    ],
    bt_nang_cao=[
        nc("Bài 7.14: tính A − B với A = 6x⁴ − 4x³ + x − 1/3 và B = −3x⁴ − 2x³ − 5x² + x + 2/3. Hệ số tự do của A − B là bao nhiêu? (ghi số)",
           "Hệ số tự do = −1/3 − 2/3.",
           ["−1", "-1"],
           "A − B = 9x⁴ − 2x³ + 5x² − 1."),
        nc("Bài 7.15: cho A = 3x⁴ − 2x³ − x + 1, B = −2x³ + 4x² + 5x và C = −3x⁴ + 2x² + 5. Tính A + B + C; hệ số của x² là bao nhiêu? (ghi số)",
           "Cộng các hạng tử cùng bậc: x²: 4 + 2 = 6.",
           ["6"],
           "A + B + C = −4x³ + 6x² + 4x + 6."),
    ],
)


# ============================================================
# BÀI 27: PHÉP NHÂN ĐA THỨC MỘT BIẾN
# ============================================================
B27 = bai(
    ly_thuyet="""📌 1. NHÂN ĐƠN THỨC VỚI ĐA THỨC
- Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích với nhau.
- Ví dụ: (−2x³)(½x² + 3x − 5) = −x⁵ − 6x⁴ + 10x³.

📌 2. NHÂN ĐA THỨC VỚI ĐA THỨC
- Muốn nhân một đa thức với một đa thức, ta nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích với nhau.
- Có thể trình bày bằng cách đặt tính nhân: nhân lần lượt từng hạng tử của dòng dưới với đa thức ở dòng trên, rồi cộng theo cột.
- Phép nhân đa thức có các tính chất: giao hoán, kết hợp, phân phối đối với phép cộng.""",
    vi_du="""Ví dụ 1: (−2x³)(½x² + 3x − 5) = −x⁵ − 6x⁴ + 10x³.

Ví dụ 2: (x + 3)(2x² − 3x − 5) = 2x³ + 3x² − 14x − 15.

Vận dụng 1: P(x) = 7x²(x² − 5x + 2) − 5x(x³ − 7x² + 3x) = 2x⁴ − x²; với x = −1/2 thì P = −1/8.

Vận dụng 2: (x − 2)(2x³ − x² + 1) + (x − 2)x²(1 − 2x) = (x − 2)·1 = x − 2.""",
    cau_hoi=[
        q("(−2x³)(½x² + 3x − 5) bằng:",
          ["−x⁵ − 6x⁴ + 10x³", "x⁵ − 6x⁴ + 10x³", "−x⁵ + 6x⁴ + 10x³", "−x⁵ − 6x⁴ − 10x³"], 0,
          "−2x³ · ½x² = −x⁵; −2x³ · 3x = −6x⁴; −2x³ · (−5) = 10x³."),
        q("(x + 3)(2x² − 3x − 5) bằng:",
          ["2x³ + 3x² − 14x − 15", "2x³ − 3x² − 14x − 15", "2x³ + 3x² + 14x − 15", "2x³ + 3x² − 14x + 15"], 0,
          "Tích các hạng tử rồi cộng: 2x³ + 3x² − 14x − 15."),
        q("Luyện tập 1: (−2x²)(3x − 4x³ + 7 − x²) bằng:",
          ["8x⁵ + 2x⁴ − 6x³ − 14x²", "8x⁵ − 2x⁴ − 6x³ − 14x²", "8x⁵ + 2x⁴ + 6x³ − 14x²", "8x⁵ + 2x⁴ − 6x³ + 14x²"], 0,
          "−2x²·3x = −6x³; −2x²·(−4x³) = 8x⁵; −2x²·7 = −14x²; −2x²·(−x²) = 2x⁴."),
        q("Vận dụng 1: rút gọn P(x) = 7x²(x² − 5x + 2) − 5x(x³ − 7x² + 3x) được:",
          ["2x⁴ − x²", "2x⁴ − 35x³ − x²", "12x⁴ − x²", "2x⁴ + x²"], 0,
          "7x⁴ − 35x³ + 14x² − 5x⁴ + 35x³ − 15x² = 2x⁴ − x²."),
        q("Vận dụng 1: giá trị của P(x) tại x = −1/2 là:",
          ["−1/8", "1/8", "−1/4", "1/4"], 0,
          "2 · (1/16) − 1/4 = −1/8."),
        q("Vận dụng 2: rút gọn (x − 2)(2x³ − x² + 1) + (x − 2)x²(1 − 2x) được:",
          ["x − 2", "x³ − 2", "2x − 4", "x − 1"], 0,
          "(x − 2)[2x³ − x² + 1 + x² − 2x³] = (x − 2)·1."),
        q("(x + 1)(x + 2) bằng:",
          ["x² + 3x + 2", "x² + 2x + 2", "x² + 3x + 1", "x + 3x + 2"], 0,
          "x² + 2x + x + 2 = x² + 3x + 2."),
        q("(2x − 1)(x + 3) bằng:",
          ["2x² + 5x − 3", "2x² + 7x − 3", "2x² + 5x + 3", "2x² − 5x − 3"], 0,
          "2x² + 6x − x − 3 = 2x² + 5x − 3."),
        q("(x − 2)(x + 2) bằng:",
          ["x² − 4", "x² + 4", "x² − 2x − 4", "x² − 2"], 0,
          "Hiệu hai bình phương."),
        q("x · (x² − x + 1) bằng:",
          ["x³ − x² + x", "x³ + x² + x", "x² − x + 1", "x³ − x + 1"], 0,
          "Nhân đơn thức với từng hạng tử."),
        q("Ví dụ LTC 1: T(x) = 14x, giá trị T(30 000) là:",
          ["420 000 đồng", "14 000 đồng", "300 000 đồng", "4 200 000 đồng"], 0,
          "14 · 30 000 = 420 000."),
        q("Bài 7.23a: 6x²(2x³ − 3x² + 5x − 4) bằng:",
          ["12x⁵ − 18x⁴ + 30x³ − 24x²", "12x⁵ − 18x⁴ + 30x² − 24x", "12x⁶ − 18x⁴ + 30x³ − 24x²", "12x⁵ − 18x⁴ + 5x³ − 4x²"], 0,
          "6x²·2x³ = 12x⁵; 6x²·(−3x²) = −18x⁴; 6x²·5x = 30x³; 6x²·(−4) = −24x²."),
        q("Bài 7.25a: (x² − x)(2x² − x − 10) bằng:",
          ["2x⁴ − 3x³ − 9x² + 10x", "2x⁴ − 3x³ + 9x² + 10x", "2x⁴ + 3x³ − 9x² − 10x", "2x⁴ − 3x³ − 9x² − 10x"], 0,
          "2x⁴ − x³ − 10x² − 2x³ + x² + 10x = 2x⁴ − 3x³ − 9x² + 10x."),
        q("Bài 7.25b: 5(0,2x² − 3x)(x² − 7x + 3) bằng:",
          ["x⁴ − 22x³ + 108x² − 45x", "x⁴ − 22x³ + 108x² + 45x", "x⁴ + 22x³ + 108x² − 45x", "x⁴ − 22x³ − 108x² − 45x"], 0,
          "(0,2x² − 3x)(x² − 7x + 3) = 0,2x⁴ − 4,4x³ + 21,6x² − 9x; nhân 5."),
        q("Bài 7.26a: (x² − 2x + 5)(x − 2) bằng:",
          ["x³ − 4x² + 9x − 10", "x³ − 4x² + 9x + 10", "x³ + 4x² + 9x − 10", "x³ − 4x² − x − 10"], 0,
          "x³ − 2x² − 2x² + 4x + 5x − 10."),
        q("Bài 7.26b: (x² − 2x + 5)(2 − x) bằng:",
          ["−x³ + 4x² − 9x + 10", "x³ − 4x² + 9x − 10", "−x³ − 4x² − 9x + 10", "−x³ + 4x² + 9x + 10"], 0,
          "Đổi dấu kết quả câu a."),
        q("Bài 7.27: thể tích hình hộp chữ nhật có các kích thước x; x + 1; x − 1 là:",
          ["x³ − x", "x³ + x", "x² − 1", "x³ − x²"], 0,
          "x(x + 1)(x − 1) = x(x² − 1) = x³ − x."),
        q("Bài 7.28b: bậc của tích (−2,5x⁴ + 0,5x² + 1)(4x³ − 2x + 6) là:",
          ["7", "6", "5", "8"], 0,
          "Hạng tử bậc cao nhất là −2,5x⁴ · 4x³ = −10x⁷."),
        q("Bài 7.28a: bậc của tích (5x³ − 2x² + 4x − 4)(x³ + 3x² − 5) là:",
          ["6", "5", "7", "4"], 0,
          "5x³ · x³ = 5x⁶."),
        q("Hệ số của x² trong (2x − 3)(x² − 5x + 1) là:",
          ["−13", "−10", "−3", "3"], 0,
          "2x·(−5x) = −10x²; −3·x² = −3x²; tổng −13x²."),
        q("Hệ số của x trong (2x − 3)(x² − 5x + 1) là:",
          ["17", "15", "−17", "2"], 0,
          "2x·1 = 2x; −3·(−5x) = 15x; tổng 17x."),
        q("Muốn nhân một đa thức với một đa thức, ta làm thế nào?",
          ["Nhân mỗi hạng tử của đa thức này với từng hạng tử của đa thức kia rồi cộng các tích", "Cộng các hạng tử", "Nhân hệ số, cộng số mũ", "Chia đa thức kia"], 0,
          "Đó là quy tắc nhân đa thức với đa thức."),
        q("Muốn nhân đơn thức với đa thức, ta làm thế nào?",
          ["Nhân đơn thức với từng hạng tử của đa thức rồi cộng các tích", "Chỉ nhân với hạng tử đầu", "Chỉ nhân hệ số", "Nhân với bậc"], 0,
          "Quy tắc nhân đơn thức với đa thức."),
        q("2x · (3x² − 8x + 1) bằng:",
          ["6x³ − 16x² + 2x", "6x³ − 8x² + 2x", "6x² − 16x + 2", "6x³ − 16x² + 2"], 0,
          "2x·3x² = 6x³; 2x·(−8x) = −16x²; 2x·1 = 2x."),
        q("Phép nhân đa thức có những tính chất nào?",
          ["Giao hoán, kết hợp, phân phối với phép cộng", "Chỉ giao hoán", "Không có tính chất nào", "Chỉ kết hợp"], 0,
          "Các tính chất giống phép nhân số."),
        q("x² · x³ bằng:",
          ["x⁵", "x⁶", "2x⁵", "x⁹"], 0,
          "Cộng số mũ: 2 + 3 = 5."),
        q("Bài 7.24a: rút gọn 4x²(5x² + 3) − 6x(3x³ − 2x + 1) − 5x³(2x − 1), hệ số của x⁴ là:",
          ["−8", "8", "−18", "20"], 0,
          "20 − 18 − 10 = −8."),
        q("Bài 7.24a: sau khi rút gọn, hệ số của x³ là:",
          ["5", "−5", "24", "−6"], 0,
          "Chỉ có −5x³·(−1) = 5x³ từ phần cuối."),
        q("Hệ số của x³ trong (x + 3)(2x² − 3x − 5) là:",
          ["2", "3", "−3", "−5"], 0,
          "x · 2x² = 2x³."),
        q("Bài 7.23b: hệ số của x⁶ trong (−1,2x²)(2,5x⁴ − 2x³ + x² − 1,5) là:",
          ["−3", "3", "−1,2", "2,5"], 0,
          "−1,2 · 2,5 = −3."),
    ],
    bt_co_ban=[
        bt("Vận dụng 2: rút gọn (x − 2)(2x³ − x² + 1) + (x − 2)x²(1 − 2x). Ghi kết quả dạng đa thức.",
           ["x−2", "x - 2"], "(x − 2)·1 = x − 2."),
        bt("Ví dụ LTC: T(x) = 14x. Tổng số tiền khi mỗi cuốn 30 000 đồng là bao nhiêu? (ghi số, đồng)",
           ["420000", "420 000"], "14 · 30 000 = 420 000."),
        bt("Bài 7.23b: hệ số của x⁶ trong (−1,2x²)(2,5x⁴ − 2x³ + x² − 1,5) là bao nhiêu? (ghi số)",
           ["−3", "-3"], "−1,2 · 2,5 = −3."),
        bt("Vận dụng 1: giá trị của P(x) = 2x⁴ − x² tại x = −1/2 là bao nhiêu? (ghi dạng phân số, ví dụ −1/8)",
           ["−1/8", "-1/8", "−0,125", "-0,125"], "2/16 − 1/4 = −1/8."),
        bt("Bài 7.23a: hệ số của x⁵ trong 6x²(2x³ − 3x² + 5x − 4) là bao nhiêu? (ghi số)",
           ["12"], "6 · 2 = 12."),
    ],
    bt_nang_cao=[
        nc("Bài 7.24a: rút gọn 4x²(5x² + 3) − 6x(3x³ − 2x + 1) − 5x³(2x − 1). Ghi kết quả.",
           "Nhân từng đơn thức với đa thức rồi thu gọn.",
           ["−8x⁴ + 5x³ + 24x² − 6x", "-8x^4 + 5x^3 + 24x^2 - 6x"],
           "20x⁴ + 12x² − 18x⁴ + 12x² − 6x − 10x⁴ + 5x³ = −8x⁴ + 5x³ + 24x² − 6x."),
        nc("Bài 7.27: thể tích hình hộp chữ nhật có ba kích thước x; x + 1; x − 1 (cm³). Ghi đa thức.",
           "V = x(x + 1)(x − 1).",
           ["x³ − x", "x^3 - x"],
           "V = x³ − x."),
        nc("Thử thách nhỏ: rút gọn x³(x + 2) − x(x³ + 2³) − 2x(x² − 2²). Ghi kết quả.",
           "Nhân ra rồi thu gọn.",
           ["0"],
           "x⁴ + 2x³ − x⁴ − 8x − 2x³ + 8x = 0."),
    ],
)


# ============================================================
# BÀI 28: PHÉP CHIA ĐA THỨC MỘT BIẾN
# ============================================================
B28 = bai(
    ly_thuyet="""📌 1. CHIA ĐƠN THỨC CHO ĐƠN THỨC
- Cho hai đơn thức axᵐ và bxⁿ (b ≠ 0). Nếu m ≥ n thì phép chia axᵐ : bxⁿ là phép chia hết, và axᵐ : bxⁿ = (a/b)·x^(m−n).
- Quy ước: x⁰ = 1.

📌 2. CHIA ĐA THỨC CHO ĐA THỨC
- Phép chia hết: A : B = Q nghĩa là A = B·Q (B ≠ 0). A là đa thức bị chia, B là đa thức chia, Q là đa thức thương.
- Cách đặt tính chia: lấy hạng tử bậc cao nhất của A chia cho hạng tử bậc cao nhất của B được hạng tử thứ nhất của thương; nhân B với hạng tử đó rồi lấy A trừ đi; lặp lại với dư.
- Phép chia có dư: A = B·Q + R, với R = 0 hoặc bậc của R nhỏ hơn bậc của B.""",
    vi_du="""Ví dụ: Chia A = 2x⁴ − 13x³ + 15x² + 11x − 3 cho B = x² − 4x − 3 được thương Q = 2x² − 5x + 1 và dư 0 (A = B·Q).

Ví dụ phép chia có dư: D = 5x³ − 3x² − x + 7 chia cho E = x² + 1 được thương 5x − 3 và dư −6x + 10.

Luyện tập 3: A = 3x⁴ − 6x − 5 chia cho B = x² + 3x − 1 được thương Q = 3x² − 9x + 30 và dư R = −105x + 25.

Ví dụ 2: (−6x⁵ + 7x⁴ − 6x³) : 3x³ = −2x² + (7/3)x − 2.""",
    cau_hoi=[
        q("(6x⁴) : (−2x³) bằng:",
          ["−3x", "3x", "−3x⁷", "−3x²"], 0,
          "6 : (−2) = −3 và x⁴ : x³ = x."),
        q("12x³ : 4x bằng:",
          ["3x²", "3x", "8x²", "3x⁴"], 0,
          "12 : 4 = 3 và x³ : x = x²."),
        q("(−2x⁴) : x⁴ bằng:",
          ["−2", "2", "−2x", "0"], 0,
          "x⁴ : x⁴ = 1."),
        q("2x⁵ : 5x² bằng:",
          ["(2/5)x³", "(2/5)x⁷", "2x³", "(2/5)x²"], 0,
          "2 : 5 = 2/5 và x⁵ : x² = x³."),
        q("Với x ≠ 0 và m ≥ n, xᵐ : xⁿ bằng:",
          ["x^(m−n)", "x^(m+n)", "x^(mn)", "x^(m/n)"], 0,
          "Chia hai lũy thừa cùng cơ số: trừ số mũ."),
        q("Quy ước x⁰ bằng:",
          ["1", "0", "x", "không xác định"], 0,
          "Quy ước x⁰ = 1 với x ≠ 0."),
        q("Phép chia hết A : B = Q nghĩa là:",
          ["A = B · Q", "B = A · Q", "A + B = Q", "A − B = Q"], 0,
          "Đa thức bị chia bằng đa thức chia nhân đa thức thương."),
        q("Thương của A = 2x⁴ − 13x³ + 15x² + 11x − 3 chia cho B = x² − 4x − 3 là:",
          ["2x² − 5x + 1", "2x² − 5x − 1", "2x² + 5x + 1", "x² − 5x + 1"], 0,
          "Đã kiểm tra: (x² − 4x − 3)(2x² − 5x + 1) = A."),
        q("Bước đầu tiên khi chia A cho B: 2x⁴ : x² bằng:",
          ["2x²", "2x", "2x³", "x²"], 0,
          "Hạng tử đầu của thương."),
        q("Trong phép chia A : B, bước thứ hai là lấy A trừ đi:",
          ["B · (2x²)", "B · (2x)", "B · 2", "B · x²"], 0,
          "Nhân B với hạng tử 2x² rồi trừ khỏi A."),
        q("Dư thứ nhất trong phép chia A : B là:",
          ["−5x³ + 21x² + 11x − 3", "−5x³ + 21x² + 11x + 3", "−5x³ − 21x² + 11x − 3", "5x³ + 21x² + 11x − 3"], 0,
          "2x⁴ − 13x³ + 15x² + 11x − 3 − (2x⁴ − 8x³ − 6x²) = −5x³ + 21x² + 11x − 3."),
        q("Hạng tử tiếp theo của thương là (−5x³) : x² bằng:",
          ["−5x", "5x", "−5x²", "−5"], 0,
          "−5x³ : x² = −5x."),
        q("Khi chia D = 5x³ − 3x² − x + 7 cho E = x² + 1, thương là:",
          ["5x − 3", "5x + 3", "5x − 1", "x − 3"], 0,
          "5x³ : x² = 5x; dư tiếp theo chia cho x² được −3."),
        q("Khi chia D cho E, dư là:",
          ["−6x + 10", "6x − 10", "−6x − 10", "−6x + 7"], 0,
          "Đã kiểm tra: D = E(5x − 3) + (−6x + 10)."),
        q("Đa thức dư R trong phép chia A = B·Q + R phải thỏa mãn điều kiện:",
          ["R = 0 hoặc bậc của R nhỏ hơn bậc của B", "R có bậc bằng bậc B", "R có bậc lớn hơn bậc B", "R bằng thương Q"], 0,
          "Điều kiện của đa thức dư."),
        q("Luyện tập 3: thương Q khi chia A = 3x⁴ − 6x − 5 cho B = x² + 3x − 1 là:",
          ["3x² − 9x + 30", "3x² + 9x − 30", "3x² − 9x − 30", "3x² − 9x + 3"], 0,
          "3x² · B = 3x⁴ + 9x³ − 3x²; rồi −9x; rồi 30."),
        q("Luyện tập 3: dư R khi chia A cho B là:",
          ["−105x + 25", "105x − 25", "−105x − 25", "−15x + 25"], 0,
          "Đã thực hiện các bước chia."),
        q("Luyện tập 2a: (−x⁶ + 5x⁴ − 2x³) : 0,5x² bằng:",
          ["−2x⁴ + 10x² − 4x", "−2x⁴ + 10x² − 4", "−x⁴ + 10x² − 4x", "−2x⁴ + 5x² − 4x"], 0,
          "−x⁶ : 0,5x² = −2x⁴; 5x⁴ : 0,5x² = 10x²; −2x³ : 0,5x² = −4x."),
        q("Luyện tập 2b: (9x² − 4) : (3x + 2) bằng:",
          ["3x − 2", "3x + 2", "x − 2", "9x − 2"], 0,
          "(3x − 2)(3x + 2) = 9x² − 4."),
        q("Ví dụ 2: (−6x⁵ + 7x⁴ − 6x³) : 3x³ bằng:",
          ["−2x² + (7/3)x − 2", "−2x² + 7x − 2", "−2x² + (7/3)x + 2", "−2x + (7/3)x − 2"], 0,
          "Chia từng hạng tử cho 3x³."),
        q("Chia x³ − 3x² + x − 1 cho x² − 3x, dư là:",
          ["x − 1", "x + 1", "−x − 1", "2x − 1"], 0,
          "Thương x; dư = x³ − 3x² + x − 1 − x(x² − 3x) = x − 1."),
        q("Bài 7.30a: 8x⁵ : 4x³ bằng:",
          ["2x²", "2x⁸", "4x²", "2x"], 0,
          "8 : 4 = 2; x⁵ : x³ = x²."),
        q("Bài 7.30b: 120x⁷ : (−24x⁵) bằng:",
          ["−5x²", "5x²", "−5x¹²", "−5x"], 0,
          "120 : (−24) = −5; x⁷ : x⁵ = x²."),
        q("Bài 7.31a: (−5x³ + 15x² + 18x) : (−5x) bằng:",
          ["x² − 3x − 3,6", "x² + 3x + 3,6", "x² − 3x + 3,6", "x³ − 3x − 3,6"], 0,
          "−5x³ : −5x = x²; 15x² : −5x = −3x; 18x : −5x = −3,6."),
        q("Bài 7.32a: (6x³ − 2x² − 9x + 3) : (3x − 1) bằng:",
          ["2x² − 3", "2x² + 3", "2x² − 3x", "2x − 3"], 0,
          "Phép chia hết, thương 2x² − 3."),
        q("Bài 7.32b: (4x⁴ + 14x³ − 21x − 9) : (2x² − 3) bằng:",
          ["2x² + 7x + 3", "2x² − 7x + 3", "2x² + 7x − 3", "x² + 7x + 3"], 0,
          "Đặt tính chia: 2x², 7x, 3; dư 0."),
        q("Bài 7.33: chia 0,5x⁵ + 3,2x³ − 2x² cho 0,25xⁿ với n = 3 có chia hết không?",
          ["Không", "Có", "Có, thương 2x²", "Chỉ khi x = 0"], 0,
          "−2x² : 0,25x³ = −8/x không là đa thức."),
        q("Bài 7.34a: thương Q(x) khi chia F(x) = 6x⁴ − 3x³ + 15x² + 2x − 1 cho G(x) = 3x² là:",
          ["2x² − x + 5", "2x² − x − 5", "2x² + x + 5", "2x² − x + 5x"], 0,
          "6x⁴ : 3x² = 2x²; −3x³ : 3x² = −x; 15x² : 3x² = 5."),
        q("Bài 7.34a: dư R(x) khi chia F(x) cho G(x) = 3x² là:",
          ["2x − 1", "2x + 1", "−2x − 1", "2x"], 0,
          "Dư có bậc 1 < 2 nên R = 2x − 1."),
        q("Bài 7.35: khi chia đa thức 21x − 4 cho 3x², thương và dư là:",
          ["Thương 0, dư 21x − 4", "Thương 7x, dư −4", "Thương x, dư 21x", "Thương 21/3, dư 0"], 0,
          "Bậc của đa thức bị chia nhỏ hơn bậc đa thức chia nên thương 0."),
        q("Bài 7.36: rút gọn (5x³ − 4x²) : 2x² + (3x⁴ + 6x) : 3x − x(x² − 1) được:",
          ["3,5x", "3,5x³", "x", "−3,5x"], 0,
          "(2,5x − 2) + (x³ + 2) − x³ + x = 3,5x."),
        q("Bài 7.37b: rút gọn 3x(2x² − x) − 2x²(3x + 1) + 5(x² − 1) được:",
          ["−5", "5", "0", "−1"], 0,
          "6x³ − 3x² − 6x³ − 2x² + 5x² − 5 = −5."),
        q("Bài 7.37a: rút gọn 2x(x + 3) − 3x²(x + 2) + x(3x² + 4x − 6) bằng:",
          ["0", "2x", "x", "−6x"], 0,
          "Các hạng tử triệt tiêu."),
        q("Bài 7.38a: giá trị của x biết 3x² − 3x(x − 2) = 36 là:",
          ["6", "−6", "3", "−3"], 0,
          "6x = 36 nên x = 6."),
        q("Bài 7.39b: (x − 1)(x + 1)(x² + 1) bằng:",
          ["x⁴ − 1", "x⁴ + 1", "x² − 1", "x⁴ − 2x² + 1"], 0,
          "(x² − 1)(x² + 1) = x⁴ − 1."),
        q("Bài 7.40: P(x) = x²(7x − 5) − (28x⁵ − 20x⁴ − 12x³) : 4x² rút gọn bằng:",
          ["3x", "x", "7x³", "x³ + 3x"], 0,
          "7x³ − 5x² − (7x³ − 5x² − 3x) = 3x; P(5) = 15."),
        q("Bài 7.41: để x³ − 3x² + 2x − b chia hết cho x − 3 thì b bằng:",
          ["6", "−6", "3", "−3"], 0,
          "P(3) = 27 − 27 + 6 − b = 0 nên b = 6."),
    ],
    bt_co_ban=[
        bt("Bài 7.30a: 8x⁵ : 4x³ bằng bao nhiêu? (ghi dạng ax^k, ví dụ 2x²)",
           ["2x²", "2x^2"], "8 : 4 = 2; x⁵ : x³ = x²."),
        bt("Bài 7.37a: rút gọn 2x(x + 3) − 3x²(x + 2) + x(3x² + 4x − 6). Ghi kết quả (số 0 nếu rút gọn về 0).",
           ["0"], "Các hạng tử triệt tiêu."),
        bt("Bài 7.41: tìm b để x³ − 3x² + 2x − b chia hết cho x − 3. (ghi số)",
           ["6"], "P(3) = 6 − b = 0."),
        bt("Bài 7.40: với a = 5, P(a) bằng bao nhiêu? (ghi số)",
           ["15"], "P(x) = 3x nên P(5) = 15."),
        bt("Luyện tập 2a: bậc của thương (−x⁶ + 5x⁴ − 2x³) : 0,5x² là bao nhiêu? (ghi số)",
           ["4"], "Hạng tử cao nhất −2x⁴, bậc 4."),
    ],
    bt_nang_cao=[
        nc("Bài 7.34b: thương Q(x) của F(x) = 12x⁴ + 10x³ − x − 3 cho G(x) = 3x² + x + 1. Hệ số của x² trong Q là bao nhiêu? (ghi số)",
           "Chia từng bước: 4x², rồi 2x, rồi −2.",
           ["4"],
           "Q(x) = 4x² + 2x − 2, R(x) = −x − 1."),
        nc("Bài 7.36 (LTC): rút gọn (5x³ − 4x²) : 2x² + (3x⁴ + 6x) : 3x − x(x² − 1). Hệ số của x là bao nhiêu? (ghi số)",
           "Chia từng hạng tử rồi thu gọn.",
           ["3,5", "3.5", "7/2"],
           "Kết quả là 3,5x."),
        nc("Bài 7.32b (LTC): thực hiện (4x⁴ + 14x³ − 21x − 9) : (2x² − 3) bằng đặt tính chia. Hệ số của x trong thương là bao nhiêu? (ghi số)",
           "Thương là 2x² + 7x + 3.",
           ["7"],
           "Phép chia hết với thương 2x² + 7x + 3."),
        nc("Bài 7.42 (BTCC VII): taxi tính 8 000 đồng cho 0,5 km đầu, sau đó 11 000 đồng/km. Đa thức biểu thị số tiền có hệ số cao nhất là bao nhiêu? (ghi số)",
           "Số tiền = 8 000 + 11 000(x − 0,5) = 11 000x + 2 500.",
           ["11000", "11 000"],
           "Đa thức bậc 1 với hệ số cao nhất 11 000 và hệ số tự do 2 500."),
        nc("Bài 7.42b: giá trị của đa thức tại x = 9 (số tiền phải trả khi đi 9 km) là bao nhiêu đồng? (ghi số)",
           "Thay x = 9 vào 11 000x + 2 500.",
           ["101500", "101 500"],
           "11 000 · 9 + 2 500 = 101 500 đồng."),
        nc("Bài 7.44d (BTCC VII): tìm đa thức P sao cho A = (x + 1)·P với A = x⁴ + x³ − 2x − 2. Ghi P(x).",
           "Chia A cho x + 1.",
           ["x³ − 2", "x^3 - 2", "x³-2"],
           "P = x³ − 2 vì (x + 1)(x³ − 2) = x⁴ + x³ − 2x − 2."),
        nc("Bài 7.44a (BTCC VII): tìm đa thức B sao cho A + B = x³ + 3x + 1 với A = x⁴ + x³ − 2x − 2. Ghi B(x).",
           "B = (x³ + 3x + 1) − A.",
           ["−x⁴ + 5x + 3", "-x^4 + 5x + 3", "-x⁴+5x+3"],
           "B = −x⁴ + 5x + 3."),
    ],
)


CHUONG_7 = {
    "Chương VII: Biểu thức đại số và đa thức một biến": {
        "Bài 24: Biểu thức đại số": B24,
        "Bài 25: Đa thức một biến": B25,
        "Bài 26: Phép cộng và phép trừ đa thức một biến": B26,
        "Bài 27: Phép nhân đa thức một biến": B27,
        "Bài 28: Phép chia đa thức một biến": B28,
    }
}

# ============================================================
# FILE toan_c8.py
# ============================================================
# ============================================================
# BÀI 29: LÀM QUEN VỚI BIẾN CỐ
# ============================================================
B29 = bai(
    ly_thuyet="""📌 1. BIẾN CỐ
- Các hiện tượng, sự kiện trong tự nhiên, cuộc sống được gọi chung là biến cố.

📌 2. CÁC LOẠI BIẾN CỐ
- Biến cố chắc chắn: là biến cố biết trước được chắc chắn luôn xảy ra.
- Biến cố không thể: là biến cố biết trước được chắc chắn không bao giờ xảy ra.
- Biến cố ngẫu nhiên: là biến cố không thể biết trước được có xảy ra hay không.

📌 3. BIẾN CỐ ĐỒNG KHẢ NĂNG
- Nếu hai biến cố có khả năng xảy ra như nhau thì ta nói hai biến cố đó đồng khả năng.
- Ví dụ: gieo một đồng xu cân đối, mặt sấp và mặt ngửa là đồng khả năng.""",
    vi_du="""Ví dụ 1: A: "Trong điều kiện thường, nước đun đến 100°C sẽ sôi" là biến cố chắc chắn. B: "Tháng Hai năm sau có 31 ngày" là biến cố không thể. C: "Khi gieo hai con xúc xắc thì tổng số chấm bằng 8" là biến cố ngẫu nhiên.

Ví dụ 2: Có bốn tấm thẻ ghi số 1; 2; 3; 6. Rút ngẫu nhiên một tấm thẻ:
- B: "Rút được thẻ ghi số nhỏ hơn 7" là biến cố chắc chắn (luôn đúng).
- C: "Rút được thẻ ghi số lớn hơn 10" là biến cố không thể.
- A: "Rút được thẻ ghi số nguyên tố" là biến cố ngẫu nhiên (rút được 2 hoặc 3 thì xảy ra, rút được 1 hoặc 6 thì không).

Thử thách nhỏ: Nếu túi I toàn bi đen và túi II toàn bi đỏ thì người chơi chắc chắn thắng; nếu túi II không có bi đỏ thì người chơi không thể thắng; nếu túi II có cả bi đỏ và bi khác màu thì biến cố "người chơi thắng" là ngẫu nhiên.""",
    cau_hoi=[
        q("Các hiện tượng, sự kiện trong tự nhiên và cuộc sống được gọi chung là:",
          ["Biến cố", "Số liệu", "Xác suất", "Đa thức"], 0,
          "Đó là khái niệm biến cố."),
        q("Biến cố chắc chắn là biến cố:",
          ["Luôn xảy ra", "Không bao giờ xảy ra", "Có thể xảy ra", "Không xác định"], 0,
          "Biến cố chắc chắn luôn xảy ra."),
        q("Biến cố không thể là biến cố:",
          ["Không bao giờ xảy ra", "Luôn xảy ra", "Có thể xảy ra", "Xảy ra một nửa số lần"], 0,
          "Biến cố không thể không bao giờ xảy ra."),
        q("Biến cố ngẫu nhiên là biến cố:",
          ["Không thể biết trước được có xảy ra hay không", "Luôn xảy ra", "Không xảy ra", "Chắc chắn"], 0,
          "Ta không biết trước biến cố có xảy ra hay không."),
        q("'Trong điều kiện thường, nước đun đến 100°C sẽ sôi' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Không xác định"], 0,
          "Luôn đúng trong điều kiện thường."),
        q("'Tháng Hai năm sau có 31 ngày' là biến cố:",
          ["Không thể", "Chắc chắn", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Tháng Hai không bao giờ có 31 ngày."),
        q("'Khi gieo hai con xúc xắc, tổng số chấm bằng 8' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Không xác định"], 0,
          "Có thể xảy ra nhưng không chắc chắn."),
        q("Ví dụ 2: 'Rút được thẻ ghi số nhỏ hơn 7' (thẻ 1; 2; 3; 6) là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Tất cả các số 1; 2; 3; 6 đều nhỏ hơn 7."),
        q("Ví dụ 2: 'Rút được thẻ ghi số lớn hơn 10' là biến cố:",
          ["Không thể", "Chắc chắn", "Ngẫu nhiên", "Không xác định"], 0,
          "Không có thẻ nào ghi số lớn hơn 10."),
        q("Ví dụ 2: 'Rút được thẻ ghi số nguyên tố' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Không xác định"], 0,
          "Có thể rút được 2 hoặc 3, cũng có thể rút được 1 hoặc 6."),
        q("'Ngày mai, Mặt Trời mọc ở phía tây' là biến cố:",
          ["Không thể", "Chắc chắn", "Ngẫu nhiên", "Không xác định"], 0,
          "Mặt Trời không bao giờ mọc ở phía tây."),
        q("'Mặt Trời mọc ở phía đông' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Không xác định"], 0,
          "Đây là hiện tượng luôn xảy ra."),
        q("'Khi gieo hai con xúc xắc, số chấm xuất hiện trên cả hai con đều là 6' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Không xác định"], 0,
          "Có thể xảy ra, nhưng không chắc chắn."),
        q("'Gieo một con xúc xắc, số chấm bé hơn 7' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Không xác định"], 0,
          "Số chấm luôn từ 1 đến 6."),
        q("'Gieo một con xúc xắc, số chấm bằng 7' là biến cố:",
          ["Ngẫu nhiên", "Không thể", "Chắc chắn", "Không xác định"], 1,
          "Xúc xắc không có mặt 7 chấm."),
        q("Luyện tập 1: 'Tổng số chấm trên hai con xúc xắc lớn hơn 1' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Tổng ít nhất là 2 nên luôn lớn hơn 1."),
        q("Luyện tập 1: 'Tổng số chấm trên hai con xúc xắc bằng 7' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Không xác định"], 0,
          "Tổng 7 có thể xảy ra nhưng không chắc chắn."),
        q("Luyện tập 1 (2): các quả cầu ghi số 3; 6; 9; 12; 15; 18; 24. 'Lấy được quả cầu có ghi số chia hết cho 7' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Không xác định"], 2,
          "Không có số nào trong túi chia hết cho 7."),
        q("Luyện tập 1 (2): 'Lấy được quả cầu có ghi số chia hết cho 3' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Không xác định"], 0,
          "Tất cả các số trong túi đều chia hết cho 3."),
        q("Thử thách nhỏ: để người chơi chắc chắn thắng, túi II phải có:",
          ["Toàn bi đỏ", "Không có bi đỏ", "Có cả bi đỏ và bi khác màu", "Toàn bi xanh"], 0,
          "Khi đó lấy một viên từ túi II luôn là bi đỏ."),
        q("Thử thách nhỏ: để người chơi không thể thắng, túi II phải:",
          ["Không có bi đỏ", "Chỉ có bi đỏ", "Có nhiều bi đỏ", "Có bi đen"], 0,
          "Không có bi đỏ thì không bao giờ thắng."),
        q("8.1: Minh lấy ngẫu nhiên một viên bi trong túi có 5 viên trắng và 5 viên đen. 'Minh lấy được viên bi màu trắng hoặc màu đen' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Mọi viên bi đều là trắng hoặc đen."),
        q("8.1: 'Minh lấy được viên bi màu đỏ' là biến cố:",
          ["Không thể", "Chắc chắn", "Ngẫu nhiên", "Không xác định"], 0,
          "Túi không có bi đỏ."),
        q("8.1: 'Minh lấy được viên bi màu trắng' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Không xác định"], 0,
          "Có thể lấy được bi trắng nhưng không chắc chắn."),
        q("8.3: chọn ngẫu nhiên một số trong tập {2; 3; 5; 6; 7; 8; 10}. 'Số được chọn là số chính phương' là biến cố:",
          ["Không thể", "Chắc chắn", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Không có số chính phương trong tập hợp."),
        q("8.3: 'Số được chọn bé hơn 11' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Không xác định"], 0,
          "Mọi số trong tập đều bé hơn 11."),
        q("8.8: túi có các thẻ 9; 12; 15; 18; 21; 24. 'Rút được thẻ ghi số chia hết cho 10' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Đồng khả năng"], 1,
          "Không có số nào chia hết cho 10."),
        q("8.8: 'Rút được thẻ ghi số chia hết cho 3' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Không xác định"], 0,
          "Tất cả các số 9; 12; 15; 18; 21; 24 đều chia hết cho 3."),
        q("8.8: 'Rút được thẻ ghi số chẵn' là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Đồng khả năng"], 2,
          "Có số chẵn (12; 18; 24) nhưng cũng có số lẻ."),
        q("8.6: một tổ có 5 bạn nam và 5 bạn nữ. Biến cố 'Bạn được gọi là bạn nam' và 'Bạn được gọi là bạn nữ' có đồng khả năng không?",
          ["Có", "Không", "Chỉ khi có 6 bạn", "Không xác định"], 0,
          "Số nam và số nữ bằng nhau nên khả năng như nhau."),
        q("Biến cố 'Ngày mai trời mưa' là biến cố:",
          ["Ngẫu nhiên", "Chắc chắn", "Không thể", "Đồng khả năng"], 0,
          "Có thể mưa hoặc không mưa."),
        q("Biến cố ngẫu nhiên là biến cố:",
          ["Có thể xảy ra hoặc không xảy ra", "Luôn xảy ra", "Không bao giờ xảy ra", "Chắc chắn xảy ra"], 0,
          "Biến cố ngẫu nhiên có thể xảy ra hoặc không."),
        q("Trong Ví dụ 1, biến cố 'nước đun đến 100°C sẽ sôi' (A) là biến cố:",
          ["Chắc chắn", "Không thể", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Đã giải ở Ví dụ 1."),
        q("Biến cố 'Trong điều kiện thường, nước đóng băng ở 50°C' là biến cố:",
          ["Không thể", "Chắc chắn", "Ngẫu nhiên", "Đồng khả năng"], 0,
          "Nước không đóng băng ở 50°C trong điều kiện thường."),
    ],
    bt_co_ban=[
        bt("Ví dụ 1: biến cố 'Nước đun đến 100°C sẽ sôi' là biến cố gì? (chắc chắn, không thể hoặc ngẫu nhiên)",
           ["chắc chắn", "Chắc chắn"], "Luôn xảy ra trong điều kiện thường."),
        bt("8.1: biến cố 'Minh lấy được viên bi màu trắng' là biến cố gì? (chắc chắn, không thể hoặc ngẫu nhiên)",
           ["ngẫu nhiên", "Ngẫu nhiên"], "Có thể xảy ra nhưng không chắc chắn."),
        bt("8.3: biến cố 'Số được chọn bé hơn 11' là biến cố gì? (chắc chắn, không thể hoặc ngẫu nhiên)",
           ["chắc chắn", "Chắc chắn"], "Mọi số trong tập đều bé hơn 11."),
        bt("8.8: biến cố 'Rút được thẻ ghi số chia hết cho 10' là biến cố gì? (chắc chắn, không thể hoặc ngẫu nhiên)",
           ["không thể", "Không thể"], "Không có số nào chia hết cho 10."),
        bt("8.6: hai biến cố 'Bạn được gọi là bạn nam' và 'Bạn được gọi là bạn nữ' có đồng khả năng không? (trả lời 'có' hoặc 'không')",
           ["có", "Có"], "Số nam và số nữ bằng nhau (5 và 5)."),
    ],
    bt_nang_cao=[
        nc("8.2: hai hộp mỗi hộp có thẻ 1 đến 6, rút mỗi hộp một thẻ. Biến cố 'Chênh lệch giữa hai số ghi trên hai tấm thẻ bé hơn 3' là biến cố gì? (chắc chắn, không thể hoặc ngẫu nhiên)",
           "Thử các cặp số có chênh lệch từ 0 đến 5.",
           ["ngẫu nhiên", "Ngẫu nhiên"],
           "Có cặp có chênh lệch bé hơn 3 và cặp có chênh lệch lớn hơn hoặc bằng 3."),
        nc("8.2: biến cố 'Chênh lệch giữa hai số ghi trên hai tấm thẻ bằng 6' là biến cố gì? (chắc chắn, không thể hoặc ngẫu nhiên)",
           "Chênh lệch lớn nhất giữa hai số từ 1 đến 6 là bao nhiêu?",
           ["không thể", "Không thể"],
           "Chênh lệch lớn nhất là 5 nên không thể bằng 6."),
        nc("Thử thách nhỏ: để biến cố 'Người chơi thắng' là biến cố chắc chắn, túi II cần có viên bi màu gì? (ghi màu)",
           "Người chơi thắng khi lấy được viên bi đỏ.",
           ["đỏ", "màu đỏ", "toàn bi đỏ", "toàn màu đỏ"],
           "Túi II toàn bi đỏ thì người chơi chắc chắn thắng."),
    ],
)


# ============================================================
# BÀI 30: LÀM QUEN VỚI XÁC SUẤT CỦA BIẾN CỐ
# ============================================================
B30 = bai(
    ly_thuyet="""📌 1. XÁC SUẤT CỦA BIẾN CỐ
- Khả năng xảy ra của một biến cố được đo bằng một số nhận giá trị từ 0 đến 1, gọi là xác suất của biến cố đó.
- Xác suất của biến cố càng gần 1 thì biến cố càng có nhiều khả năng xảy ra.
- Xác suất của biến cố càng gần 0 thì biến cố càng ít khả năng xảy ra.
- Biến cố chắc chắn có xác suất bằng 1; biến cố không thể có xác suất bằng 0.

📌 2. XÁC SUẤT CỦA BIẾN CỐ ĐỒNG KHẢ NĂNG
- Nếu k biến cố đồng khả năng và luôn xảy ra duy nhất một biến cố trong k biến cố này thì xác suất của mỗi biến cố đó đều bằng 1/k.
- Ví dụ: gieo đồng xu cân đối, xác suất xuất hiện mặt sấp là 1/2 (50%).
- Ví dụ: gieo xúc xắc cân đối, xác suất xuất hiện mỗi mặt là 1/6.

📌 3. THANG ĐO XÁC SUẤT
- 0 (không thể) — 1/2 (đồng khả năng) — 1 (chắc chắn).""",
    vi_du="""Ví dụ 1: Xác suất để trúng giải độc đắc xổ số Vietlott 6/45 là 0,0000001228 (tức 0,00001228%). Bản tin dự báo mưa 43% nghĩa là xác suất có mưa là 0,43. Xác suất để xuất hiện mặt sấp khi gieo đồng xu cân đối là 1/2 (50%).

Ví dụ 2: Đội A thắng 60%, thua 35%, hoà 5%. Xác suất thua của đội A là 35% nghĩa là xác suất thắng của đội B là 35%. Vì 60% > 35% nên đội A có khả năng thắng cao hơn.

Ví dụ 3: Biến cố "Ngày mai, Mặt Trời mọc ở phía tây" có xác suất 0; biến cố "Tháng Ba có ít hơn 32 ngày" có xác suất 1.

Ví dụ 4: Lớp 7A có 10 lá phiếu ghi số từ 1 đến 10 (đồng khả năng). Xác suất để Mai rút được lá phiếu ghi số 5 là 1/10.

Luyện tập 1 (dự báo thời tiết): Hôm nay khả năng mưa là 40%, cao nhất trong 5 ngày; thứ Ba 11 khả năng mưa 13%, thấp nhất.""",
    cau_hoi=[
        q("Xác suất của một biến cố được đo bằng số nhận giá trị:",
          ["Từ 0 đến 1", "Từ −1 đến 1", "Bất kì", "Chỉ là số nguyên"], 0,
          "Xác suất luôn nằm trong đoạn [0; 1]."),
        q("Xác suất của biến cố chắc chắn bằng:",
          ["1", "0", "1/2", "100"], 0,
          "Biến cố chắc chắn có xác suất bằng 1."),
        q("Xác suất của biến cố không thể bằng:",
          ["0", "1", "1/2", "−1"], 0,
          "Biến cố không thể có xác suất bằng 0."),
        q("Xác suất của biến cố càng gần 1 thì:",
          ["Biến cố càng có nhiều khả năng xảy ra", "Biến cố càng ít khả năng xảy ra", "Biến cố không xảy ra", "Biến cố không thể"], 0,
          "Gần 1 nghĩa là khả năng xảy ra lớn."),
        q("Xác suất của biến cố càng gần 0 thì:",
          ["Biến cố càng ít khả năng xảy ra", "Biến cố càng có nhiều khả năng xảy ra", "Biến cố chắc chắn", "Biến cố đồng khả năng"], 0,
          "Gần 0 nghĩa là khả năng xảy ra nhỏ."),
        q("Xác suất xuất hiện mặt sấp khi gieo đồng xu cân đối là:",
          ["1/2", "1/4", "1", "0"], 0,
          "Hai mặt đồng khả năng nên mỗi mặt 1/2."),
        q("Ví dụ 1: xác suất trúng giải độc đắc Vietlott 6/45 là 0,0000001228. Viết dưới dạng phần trăm là:",
          ["0,00001228%", "0,1228%", "1,228%", "12,28%"], 0,
          "0,0000001228 = 0,00001228%."),
        q("Ví dụ 1: bản tin dự báo khả năng có mưa là 43%. Xác suất của biến cố này là:",
          ["0,43", "4,3", "43", "0,043"], 0,
          "43% = 0,43."),
        q("Ví dụ 2: đội A thắng 60%, thua 35%, hoà 5%. Xác suất thắng của đội B là:",
          ["35%", "60%", "5%", "40%"], 0,
          "Xác suất thắng của B bằng xác suất thua của A."),
        q("Ví dụ 2: đội nào có khả năng thắng cao hơn?",
          ["Đội A", "Đội B", "Bằng nhau", "Không xác định được"], 0,
          "60% > 35%."),
        q("Luyện tập 1: ngày nào có khả năng mưa nhiều nhất?",
          ["Hôm nay", "Chủ nhật 09", "Thứ Hai 10", "Thứ Ba 11"], 0,
          "Hôm nay 40%, cao nhất."),
        q("Luyện tập 1: ngày nào có khả năng mưa ít nhất?",
          ["Hôm nay", "Chủ nhật 09", "Thứ Hai 10", "Thứ Ba 11"], 3,
          "Thứ Ba 11 là 13%, thấp nhất."),
        q("Ví dụ 3: xác suất của biến cố 'Ngày mai, Mặt Trời mọc ở phía tây' là:",
          ["0", "1", "1/2", "2"], 0,
          "Biến cố không thể nên xác suất bằng 0."),
        q("Ví dụ 3: xác suất của biến cố 'Tháng Ba có ít hơn 32 ngày' là:",
          ["1", "0", "1/2", "0,3"], 0,
          "Biến cố chắc chắn có xác suất bằng 1."),
        q("Luyện tập 2: gieo đồng thời hai con xúc xắc, xác suất để tổng số chấm nhỏ hơn 13 là:",
          ["1", "0", "1/2", "1/36"], 0,
          "Tổng luôn nhỏ hơn 13 nên xác suất bằng 1."),
        q("Luyện tập 2: gieo đồng thời hai con xúc xắc, xác suất để tổng số chấm bằng 1 là:",
          ["0", "1", "1/12", "1/36"], 0,
          "Tổng nhỏ nhất là 2 nên không thể bằng 1."),
        q("Hai biến cố đồng khả năng và luôn xảy ra một trong hai: xác suất của mỗi biến cố là:",
          ["Bằng nhau và bằng 0,5", "Khác nhau", "Bằng 1", "Bằng 0"], 0,
          "Hai biến cố đồng khả năng nên mỗi cái 1/2."),
        q("Trên thang đo xác suất, vị trí đồng khả năng nằm ở:",
          ["1/2", "0", "1", "1/4"], 0,
          "Đồng khả năng ứng với 1/2."),
        q("Ví dụ 4: có 10 lá phiếu ghi số 1 đến 10 đồng khả năng. Xác suất để rút được lá ghi số 5 là:",
          ["1/10", "1/5", "1/9", "1/2"], 0,
          "Có 10 biến cố đồng khả năng nên mỗi cái 1/10."),
        q("Trong một trò chơi có k biến cố đồng khả năng và luôn xảy ra duy nhất một biến cố, xác suất của mỗi biến cố là:",
          ["1/k", "k", "1/2", "k/2"], 0,
          "Tổng xác suất bằng 1 nên mỗi cái 1/k."),
        q("Luyện tập 3: trò chơi Ô cửa bí mật có ba ô cửa, phần thưởng đặt sau một ô. Xác suất để người chơi chọn được ô có phần thưởng là:",
          ["1/3", "1/2", "2/3", "1"], 0,
          "Ba ô đồng khả năng nên mỗi ô 1/3."),
        q("Luyện tập 4: gieo một con xúc xắc cân đối, xác suất để số chấm xuất hiện là 2 là:",
          ["1/6", "1/3", "1/2", "1/4"], 0,
          "Có 6 mặt đồng khả năng."),
        q("8.4a: Mai và Việt mỗi người gieo một con xúc xắc. Xác suất để tổng số chấm lớn hơn 1 là:",
          ["1", "0", "1/2", "1/36"], 0,
          "Tổng luôn ít nhất là 2 nên luôn lớn hơn 1."),
        q("8.4b: xác suất để tích số chấm lớn hơn 36 là:",
          ["0", "1", "1/36", "1/6"], 0,
          "Tích lớn nhất là 36 nên không thể lớn hơn 36."),
        q("8.5: Paul chọn ngẫu nhiên một trong hai hộp (một hộp gắn cờ Hà Lan, một hộp gắn cờ Tây Ban Nha). Xác suất để Paul dự đoán đội Tây Ban Nha thắng là:",
          ["1/2", "1", "0", "1/3"], 0,
          "Có hai hộp đồng khả năng."),
        q("8.6: tổ có 5 bạn nam và 5 bạn nữ. Xác suất để bạn được gọi là bạn nam là:",
          ["1/2", "1/5", "1", "0"], 0,
          "5 trong 10 bạn là nam."),
        q("8.7: gieo một con xúc xắc cân đối. Xác suất số chấm xuất hiện nhỏ hơn 7 là:",
          ["1", "1/6", "0", "1/2"], 0,
          "Mọi mặt đều nhỏ hơn 7."),
        q("8.7: xác suất số chấm xuất hiện bằng 0 là:",
          ["0", "1/6", "1", "1/2"], 0,
          "Không có mặt 0 chấm."),
        q("8.7: xác suất số chấm xuất hiện bằng 6 là:",
          ["1/6", "1", "0", "1/3"], 0,
          "Có một mặt 6 trong 6 mặt."),
        q("8.9: gieo hai con xúc xắc, xác suất để hiệu số chấm bằng 6 là:",
          ["0", "1/6", "1/36", "1"], 0,
          "Hiệu lớn nhất là 5."),
        q("8.9: gieo hai con xúc xắc, xác suất để số chấm trên cả hai con đều bé hơn 7 là:",
          ["1", "0", "1/2", "1/6"], 0,
          "Mọi mặt đều bé hơn 7."),
        q("8.10: trong hộp có 15 quả cầu xanh và 15 quả cầu đỏ. Xác suất lấy được quả cầu đỏ là:",
          ["1/2", "1/15", "1", "0"], 0,
          "15 trong 30 quả là đỏ."),
        q("8.11: chọn ngẫu nhiên một số trong {11; 12; 13; 14}. Xác suất để chọn được số chia hết cho 5 là:",
          ["0", "1/4", "1/2", "1"], 0,
          "Không có số nào chia hết cho 5."),
        q("8.11: xác suất để chọn được số có hai chữ số là:",
          ["1", "0", "1/2", "1/4"], 0,
          "Cả bốn số đều có hai chữ số."),
        q("8.11: xác suất để chọn được số nguyên tố là:",
          ["1/2", "1/4", "1", "0"], 0,
          "11 và 13 là số nguyên tố: 2 trên 4."),
        q("8.11: xác suất để chọn được số chia hết cho 6 là:",
          ["1/4", "1/2", "1/3", "0"], 0,
          "Chỉ có số 12 chia hết cho 6."),
    ],
    bt_co_ban=[
        bt("Ví dụ 4: xác suất để Mai rút được lá phiếu ghi số 5 là bao nhiêu? (ghi phân số)",
           ["1/10", "0,1", "0.1"], "Có 10 lá phiếu đồng khả năng."),
        bt("8.4a: xác suất để tổng số chấm của hai con xúc xắc lớn hơn 1 là bao nhiêu? (ghi số)",
           ["1"], "Tổng luôn lớn hơn 1."),
        bt("8.4b: xác suất để tích số chấm lớn hơn 36 là bao nhiêu? (ghi số)",
           ["0"], "Tích tối đa là 36."),
        bt("8.7C: gieo xúc xắc cân đối, xác suất số chấm bằng 6 là bao nhiêu? (ghi phân số)",
           ["1/6", "1÷6"], "Có 6 mặt đồng khả năng."),
        bt("8.11b: xác suất chọn được số có hai chữ số từ {11; 12; 13; 14} là bao nhiêu? (ghi số)",
           ["1"], "Mọi số đều có hai chữ số."),
    ],
    bt_nang_cao=[
        nc("8.5: xác suất để Paul dự đoán đội Tây Ban Nha thắng là bao nhiêu? (ghi phân số)",
           "Có hai hộp đồng khả năng.",
           ["1/2", "0,5", "0.5"],
           "Xác suất là 1/2."),
        nc("8.9a: hai con xúc xắc, xác suất hiệu số chấm bằng 6 là bao nhiêu? (ghi số)",
           "Hiệu lớn nhất giữa hai mặt xúc xắc là 5.",
           ["0"],
           "Không có cặp nào có hiệu bằng 6."),
        nc("8.6b: xác suất của biến cố 'Bạn được gọi là bạn nữ' là bao nhiêu? (ghi phân số)",
           "5 nữ trong 10 bạn.",
           ["1/2", "0,5", "0.5"],
           "Xác suất 5/10 = 1/2."),
        nc("Luyện tập 1 (Hình 8.2): hôm nay khả năng có mưa là 40%. Viết xác suất này dưới dạng số thập phân. (ghi số)",
           "40% = 40/100.",
           ["0,4", "0.4"],
           "Xác suất là 0,4."),
    ],
)


CHUONG_8 = {
    "Chương VIII: Làm quen với biến cố và xác suất của biến cố": {
        "Bài 29: Làm quen với biến cố": B29,
        "Bài 30: Làm quen với xác suất của biến cố": B30,
    }
}

# ============================================================
# FILE toan_c9.py
# ============================================================
# ============================================================
# BÀI 31: QUAN HỆ GIỮA GÓC VÀ CẠNH ĐỐI DIỆN TRONG MỘT TAM GIÁC
# ============================================================
B31 = bai(
    ly_thuyet="""📌 1. GÓC ĐỐI DIỆN VỚI CẠNH LỚN HƠN
Định lí 1: Trong một tam giác, góc đối diện với cạnh lớn hơn là góc lớn hơn.
- Ví dụ: tam giác ABC có AB > AC thì Ĉ > B̂.

📌 2. CẠNH ĐỐI DIỆN VỚI GÓC LỚN HƠN
Định lí 2: Trong một tam giác, cạnh đối diện với góc lớn hơn là cạnh lớn hơn.
- Ví dụ: tam giác ABC có B̂ > Ĉ thì AC > AB.

📌 3. NHẬN XÉT
- Trong tam giác vuông, góc vuông là góc lớn nhất nên cạnh huyền (cạnh đối diện góc vuông) là cạnh lớn nhất.
- Trong tam giác tù, góc tù là góc lớn nhất nên cạnh đối diện góc tù là cạnh lớn nhất.
- Trong tam giác cân có góc ở đỉnh tù thì cạnh đáy là cạnh lớn nhất.""",
    vi_du="""Ví dụ 1: Tam giác ABC có AB = 2, BC = 4, AC = 5. Sắp xếp các góc theo thứ tự tăng dần.
Giải: Cạnh lớn nhất là AC = 5 đối diện góc B̂; cạnh nhỏ nhất là AB = 2 đối diện góc Ĉ. Vậy B̂ > Â > Ĉ.

Ví dụ 2: Tam giác ABC có B̂ = 80°, Ĉ = 45°. Sắp xếp ba cạnh AB, BC, CA theo thứ tự độ dài từ lớn đến bé.
Giải: Â = 180° − (80° + 45°) = 55°. Ta có B̂ > Â > Ĉ nên AC > BC > AB.

Luyện tập 1: Tam giác MNP có MN = 3 cm, NP = 5 cm, MP = 7 cm. Sắp xếp các góc theo thứ tự tăng dần.
Luyện tập 2: Tam giác MNP có M̂ = 47°, N̂ = 53°. Viết các cạnh theo thứ tự độ dài từ bé đến lớn.""",
    cau_hoi=[
        q("Trong một tam giác, góc đối diện với cạnh lớn hơn là góc:",
          ["Lớn hơn", "Nhỏ hơn", "Bằng nhau", "Vuông"], 0,
          "Định lí 1: cạnh lớn hơn đối diện góc lớn hơn."),
        q("Trong một tam giác, cạnh đối diện với góc lớn hơn là cạnh:",
          ["Lớn hơn", "Nhỏ hơn", "Bằng nhau", "Đáy"], 0,
          "Định lí 2 là điều ngược lại của Định lí 1."),
        q("Tam giác ABC có AB = 2 cm, BC = 4 cm, AC = 5 cm. Góc lớn nhất của tam giác là:",
          ["Góc B", "Góc A", "Góc C", "Không xác định"], 0,
          "Cạnh lớn nhất AC = 5 đối diện góc B."),
        q("Tam giác ABC có AB = 2 cm, BC = 4 cm, AC = 5 cm. Góc nhỏ nhất của tam giác là:",
          ["Góc A", "Góc B", "Góc C", "Bằng nhau"], 2,
          "Cạnh nhỏ nhất AB = 2 đối diện góc C."),
        q("Tam giác ABC có B̂ = 80°, Ĉ = 45°. Cạnh lớn nhất của tam giác là:",
          ["AB", "BC", "AC", "Bằng nhau"], 2,
          "Góc lớn nhất 80° đối diện cạnh AC."),
        q("Tam giác ABC có B̂ = 80°, Ĉ = 45°. Cạnh nhỏ nhất của tam giác là:",
          ["AB", "BC", "AC", "AB = BC"], 0,
          "Góc nhỏ nhất 45° đối diện cạnh AB."),
        q("Trong tam giác vuông, cạnh lớn nhất là:",
          ["Cạnh huyền", "Cạnh góc vuông", "Cạnh đáy", "Đường cao"], 0,
          "Góc vuông là góc lớn nhất nên cạnh huyền là cạnh lớn nhất."),
        q("Trong tam giác tù, cạnh lớn nhất là cạnh:",
          ["Đối diện góc tù", "Kề góc tù", "Đáy", "Cạnh bên"], 0,
          "Góc tù là góc lớn nhất nên cạnh đối diện nó lớn nhất."),
        q("Tam giác MNP có MN = 3, NP = 5, MP = 7. Góc lớn nhất là:",
          ["Góc M", "Góc N", "Góc P", "Bằng nhau"], 1,
          "Cạnh lớn nhất MP = 7 đối diện góc N."),
        q("Tam giác MNP có MN = 3, NP = 5, MP = 7. Góc nhỏ nhất là:",
          ["Góc M", "Góc N", "Góc P", "Không có"], 2,
          "Cạnh nhỏ nhất MN = 3 đối diện góc P."),
        q("Tam giác MNP có M̂ = 47°, N̂ = 53° (nên P̂ = 80°). Cạnh lớn nhất là:",
          ["MP", "NP", "MN", "Bằng nhau"], 2,
          "Góc lớn nhất 80° đối diện cạnh MN."),
        q("Tam giác ABC có Â = 105°, B̂ = 35°. Cạnh lớn nhất là:",
          ["AB", "AC", "BC", "Bằng nhau"], 2,
          "Góc 105° là góc lớn nhất, đối diện cạnh BC."),
        q("Tam giác ABC có Â = 105°, B̂ = 35°. Tam giác ABC là tam giác:",
          ["Tù", "Vuông", "Nhọn", "Đều"], 0,
          "Ĉ = 40°, tam giác có một góc tù 105°."),
        q("Tam giác cân có một góc 96°. Cạnh lớn nhất của tam giác là:",
          ["Cạnh bên", "Cạnh đáy", "Hai cạnh bằng nhau", "Không xác định"], 1,
          "Góc 96° là góc ở đỉnh, nên cạnh đáy đối diện là lớn nhất."),
        q("Tam giác ABC vuông tại A. So sánh BC và AB:",
          ["BC > AB", "BC < AB", "BC = AB", "Không so sánh được"], 0,
          "BC là cạnh huyền nên lớn hơn cạnh góc vuông AB."),
        q("Tam giác ABC có Â > B̂. Khi đó:",
          ["BC > AC", "BC < AC", "BC = AC", "AB > AC"], 0,
          "Â đối diện BC, B̂ đối diện AC; Â > B̂ nên BC > AC."),
        q("Tam giác ABC có AB < AC. So sánh các góc:",
          ["B̂ < Ĉ", "B̂ > Ĉ", "B̂ = Ĉ", "Không so sánh được"], 1,
          "AB đối diện Ĉ, AC đối diện B̂; AB < AC nên Ĉ < B̂."),
        q("Tam giác ABC có Â = B̂. Khi đó:",
          ["BC = AC", "BC > AC", "BC < AC", "AB = BC"], 0,
          "Â đối diện BC, B̂ đối diện AC; hai góc bằng nhau thì hai cạnh bằng nhau."),
        q("Trong một tam giác có một góc tù thì:",
          ["Góc tù là góc lớn nhất", "Góc tù là góc nhỏ nhất", "Góc tù bằng góc vuông", "Hai góc còn lại bằng nhau"], 0,
          "Góc tù lớn hơn 90° và lớn hơn hai góc nhọn còn lại."),
        q("Trong tam giác vuông, góc lớn nhất là:",
          ["Góc vuông", "Góc nhọn", "Góc tù", "Góc bẹt"], 0,
          "Tổng hai góc nhọn bằng 90° nên mỗi góc nhọn nhỏ hơn góc vuông."),
        q("Cạnh đối diện với góc nhỏ nhất của tam giác là cạnh:",
          ["Nhỏ nhất", "Lớn nhất", "Bằng cạnh bên", "Là cạnh huyền"], 0,
          "Góc nhỏ hơn đối diện cạnh nhỏ hơn."),
        q("Tam giác DEF có DE = 5, EF = 8, DF = 6. Góc lớn nhất là:",
          ["Góc D", "Góc E", "Góc F", "Bằng nhau"], 0,
          "Cạnh lớn nhất EF = 8 đối diện góc D."),
        q("Tam giác DEF có DE = 5, EF = 8, DF = 6. Góc nhỏ nhất là:",
          ["Góc D", "Góc E", "Góc F", "Không xác định"], 2,
          "Cạnh nhỏ nhất DE = 5 đối diện góc F."),
        q("Tam giác ABC vuông tại A. Cạnh lớn nhất là:",
          ["BC", "AB", "AC", "Bằng nhau"], 0,
          "BC là cạnh huyền."),
        q("Trong tam giác ABC có BC < AB. So sánh các góc:",
          ["Â < Ĉ", "Â > Ĉ", "Â = Ĉ", "Không so sánh được"], 0,
          "BC đối diện Â, AB đối diện Ĉ; BC < AB nên Â < Ĉ."),
        q("Trong một tam giác, nếu hai cạnh bằng nhau thì hai góc đối diện:",
          ["Bằng nhau", "Lớn hơn", "Nhỏ hơn", "Bù nhau"], 0,
          "Hai cạnh bằng nhau thì hai góc đối diện bằng nhau."),
        q("Tam giác ABC có Â = 100°. Cạnh lớn nhất là:",
          ["AB", "AC", "BC", "Bằng nhau"], 2,
          "Góc tù 100° đối diện cạnh BC."),
        q("Tam giác ABC có B̂ = 60°, Ĉ = 70°. Cạnh lớn nhất là:",
          ["AB", "AC", "BC", "Không xác định"], 1,
          "Â = 50° là nhỏ nhất; góc lớn nhất Ĉ = 70° đối diện AB, nên cạnh lớn nhất là AB."),
        q("Trong tam giác ABC, ta có AB > AC. Khi đó:",
          ["Ĉ > B̂", "Ĉ < B̂", "Ĉ = B̂", "Â > B̂"], 0,
          "AB đối diện Ĉ, AC đối diện B̂; AB > AC nên Ĉ > B̂."),
        q("Tam giác có ba góc 50°, 60°, 70°. Cạnh lớn nhất đối diện góc:",
          ["50°", "60°", "70°", "Không xác định"], 2,
          "Góc lớn nhất 70° đối diện cạnh lớn nhất."),
    ],
    bt_co_ban=[
        bt("Tam giác ABC có Â = 105°, B̂ = 35°. Cạnh lớn nhất của tam giác là cạnh nào? (gõ tên cạnh, ví dụ AB)",
           ["BC"], "Bài 9.1b."),
        bt("Tam giác cân có một góc 96°. Cạnh lớn nhất là cạnh bên hay cạnh đáy? (gõ: đáy hoặc bên)",
           ["đáy", "cạnh đáy"], "Bài 9.3."),
        bt("Tam giác ABC có Â = 60°, B̂ = 70°. Cạnh lớn nhất là cạnh nào? (gõ tên cạnh)",
           ["AC", "CA"], "Góc lớn nhất 70° đối diện cạnh AC."),
        bt("Tam giác MNP có M̂ = 47°, N̂ = 53°. Cạnh nhỏ nhất là cạnh nào? (gõ tên cạnh)",
           ["NP", "PN"], "Góc nhỏ nhất 47° đối diện cạnh NP."),
        bt("Trong tam giác ABC có AB = 2 cm, BC = 4 cm, AC = 5 cm. Góc lớn nhất là góc nào? (gõ tên góc, ví dụ A)",
           ["B"], "Cạnh lớn nhất AC đối diện góc B."),
        bt("Bài 9.2: Trong hình 9.6, DC = BC, D nằm giữa A và C. Kết luận đúng là a, b hay c? "
           "(a: Â = B̂; b: Â > B̂; c: Â < B̂). Gõ chữ cái.",
           ["c"], "Góc BDC là góc ngoài của tam giác ABD nên BDC > Â; B̂ > DBC = BDC nên B̂ > Â."),
    ],
    bt_nang_cao=[
        nc("Bài 9.3: Trong tam giác cân có một góc 96°, cạnh lớn nhất là cạnh bên hay cạnh đáy? Vì sao?",
           "Góc 96° lớn hơn 90° nên là góc ở đỉnh; góc đối diện cạnh đáy là lớn nhất.",
           ["cạnh đáy"],
           "Góc ở đỉnh là góc tù 96° nên cạnh đáy đối diện là cạnh lớn nhất."),
        nc("Bài 9.4: Ba bạn Mai, Việt, Hà đi đến trường D theo ba con đường AD, BD, CD (A, B, C thẳng hàng, B nằm giữa A và C; ACD là góc tù). Bạn nào đi xa nhất, bạn nào đi gần nhất?",
           "Dùng quan hệ góc – cạnh đối diện trong các tam giác ABD, BCD với góc ACD tù.",
           ["Mai đi xa nhất, Hà đi gần nhất"],
           "∠BCD = ∠ACD là góc tù nên BD > CD; trong tam giác ABD có AD > BD. Vậy AD > BD > CD."),
        nc("Bài 9.5: Ba địa điểm A, B, C là ba đỉnh tam giác ABC với Â tù, AC = 500 m. Đặt loa tại một điểm giữa A và B. Tại C có nghe được tiếng loa nếu bán kính nghe rõ là 500 m không?",
           "Trong tam giác có góc A tù thì cạnh BC lớn nhất; xét khoảng cách từ C tới điểm M trên AB.",
           ["Không"],
           "Vì Â tù nên với M nằm giữa A và B, góc CAM tù, do đó CM > CA = 500 m. Vậy C không nghe được."),
        nc("Bài 9.6 (ôn tập): Chiều cao của tam giác ứng với một cạnh có phải là khoảng cách từ đỉnh đối diện đến đường thẳng chứa cạnh đó không?",
           "Khoảng cách từ một điểm đến đường thẳng là đoạn vuông góc.",
           ["Có"],
           "Chiều cao kẻ từ đỉnh vuông góc với cạnh đối diện, đúng là khoảng cách."),
    ],
)

# ============================================================
# BÀI 32: QUAN HỆ GIỮA ĐƯỜNG VUÔNG GÓC VÀ ĐƯỜNG XIÊN
# ============================================================
B32 = bai(
    ly_thuyet="""📌 1. ĐƯỜNG VUÔNG GÓC VÀ ĐƯỜNG XIÊN
- Từ một điểm A không nằm trên đường thẳng d, kẻ đường thẳng vuông góc với d tại H. Đoạn AH gọi là đoạn vuông góc (đường vuông góc) kẻ từ A đến d; H gọi là chân đường vuông góc hạ từ A xuống d.
- Lấy điểm M trên d (M khác H), đoạn AM gọi là đường xiên kẻ từ A đến d.

📌 2. SO SÁNH ĐƯỜNG VUÔNG GÓC VÀ ĐƯỜNG XIÊN
Định lí: Trong các đường xiên và đường vuông góc kẻ từ một điểm nằm ngoài một đường thẳng đến đường thẳng đó thì đường vuông góc là đường ngắn nhất.
- Vì AH là đoạn ngắn nhất trong các đoạn thẳng kẻ từ A đến d, độ dài AH được gọi là khoảng cách từ điểm A đến đường thẳng d.
- Khi A nằm trên đường thẳng d, khoảng cách từ A đến d bằng 0.

📌 3. LUYỆN TẬP
- Vì AH ⊥ d nên tam giác AHM vuông tại H, AM là cạnh huyền nên AH < AM.""",
    vi_du="""Luyện tập: Cho hình vuông ABCD cạnh 2 cm, M là một điểm trên cạnh BC.
a) Chỉ ra các đường vuông góc và đường xiên kẻ từ A đến đường thẳng BC.
b) So sánh AB và AM.
c) Tìm khoảng cách từ C đến đường thẳng AB.

Thử thách nhỏ: Quan sát Hình 9.11, khi M thay đổi trên d và xa H thì AM càng lớn: nếu HM < HN thì AM < AN (dùng quan hệ góc – cạnh đối diện trong tam giác AMN).""",
    cau_hoi=[
        q("Điểm H trong đường vuông góc kẻ từ A đến đường thẳng d gọi là:",
          ["Chân đường vuông góc", "Đỉnh", "Trung điểm", "Tâm"], 0,
          "H là chân đường vuông góc hạ từ A xuống d."),
        q("Đoạn thẳng AM (M nằm trên d, M khác H) gọi là:",
          ["Đường xiên", "Đường vuông góc", "Đường trung tuyến", "Đường cao"], 0,
          "AM là đường xiên kẻ từ A đến d."),
        q("Trong các đoạn thẳng nối điểm A với các điểm trên đường thẳng d, đoạn ngắn nhất là:",
          ["Đường vuông góc", "Đường xiên", "Đường trung tuyến", "Đường kính"], 0,
          "Đường vuông góc là đường ngắn nhất."),
        q("Khoảng cách từ điểm A đến đường thẳng d là:",
          ["Độ dài AH", "Độ dài AM", "Độ dài HM", "AH + AM"], 0,
          "Khoảng cách là độ dài đoạn vuông góc AH."),
        q("Khi điểm A nằm trên đường thẳng d, khoảng cách từ A đến d bằng:",
          ["0", "1", "Không xác định", "Độ dài AH"], 0,
          "Theo chú ý trong sách, khoảng cách bằng 0."),
        q("Trong Hình 9.9, AH < AM vì:",
          ["AH là cạnh góc vuông, AM là cạnh huyền", "AM là cạnh góc vuông", "AH = AM", "Không so sánh được"], 0,
          "Tam giác AHM vuông tại H nên cạnh huyền AM lớn hơn cạnh góc vuông AH."),
        q("Cho A ngoài d, AH ⊥ d, M thuộc d. Khẳng định đúng là:",
          ["AH ≤ AM", "AH ≥ AM", "AH = 2AM", "AM luôn ngắn nhất"], 0,
          "Đường vuông góc luôn ngắn hơn hoặc bằng đường xiên."),
        q("Trong tam giác vuông ABC (Â = 90°), cạnh lớn nhất là:",
          ["BC", "AB", "AC", "Bằng nhau"], 0,
          "BC là cạnh huyền nên lớn nhất."),
        q("Hình vuông ABCD cạnh 2 cm, M thuộc BC. Đường vuông góc kẻ từ A đến đường thẳng BC là đoạn nào?",
          ["AB", "AC", "AD", "AM"], 0,
          "AB ⊥ BC nên AB là đường vuông góc từ A đến BC."),
        q("Hình vuông ABCD cạnh 2 cm, M thuộc BC (M khác B). Đường xiên kẻ từ A đến BC là đoạn nào?",
          ["AM", "AD", "AB", "BD"], 0,
          "AM không vuông góc với BC nên là đường xiên."),
        q("Hình vuông ABCD cạnh 2 cm, M thuộc BC. So sánh AB và AM:",
          ["AB < AM", "AB > AM", "AB = AM", "Không so sánh được"], 0,
          "AB là đường vuông góc nên ngắn hơn đường xiên AM."),
        q("Hình vuông ABCD cạnh 2 cm. Khoảng cách từ C đến đường thẳng AB là:",
          ["2 cm", "2√2 cm", "4 cm", "1 cm"], 0,
          "CB ⊥ AB nên khoảng cách từ C đến AB là BC = 2 cm."),
        q("Hình vuông ABCD cạnh 2 cm. Khoảng cách từ D đến đường thẳng AB là:",
          ["2 cm", "1 cm", "0 cm", "2√2 cm"], 0,
          "AD ⊥ AB nên khoảng cách là AD = 2 cm."),
        q("Trong Hình 9.8, bạn Nam xuất phát từ O, muốn bơi sang bờ bên kia nhanh nhất thì chọn đường:",
          ["OA", "OB", "OC", "Đều như nhau"], 0,
          "OA vuông góc với cạnh bể nên là đường ngắn nhất."),
        q("Trong Hình 9.11, nếu HM < HN thì:",
          ["AM < AN", "AM > AN", "AM = AN", "Không xác định"], 0,
          "Khi M càng xa H thì AM càng lớn."),
        q("Trong tam giác AHM vuông tại H (AH ⊥ d), cạnh AM là:",
          ["Cạnh huyền", "Cạnh góc vuông", "Cạnh đáy", "Cạnh bên"], 0,
          "AM đối diện góc vuông H nên là cạnh huyền."),
        q("Trong tam giác AHM vuông tại H, góc lớn nhất là:",
          ["Góc H", "Góc A", "Góc M", "Bằng nhau"], 0,
          "Góc vuông là góc lớn nhất trong tam giác vuông."),
        q("Hình vuông ABCD cạnh 2 cm, M thuộc BC. Với mọi M, AM luôn lớn hơn hoặc bằng:",
          ["AB", "AD", "BC", "CD"], 0,
          "AB là đường vuông góc từ A đến BC nên AM ≥ AB."),
        q("Điểm A cách đường thẳng d một khoảng 5 cm, M thuộc d. Khi đó:",
          ["AM ≥ 5 cm", "AM ≤ 5 cm", "AM = 0", "AM = 10 cm"], 0,
          "Khoảng cách 5 cm là đường ngắn nhất nên AM ≥ 5 cm."),
        q("Cho AH ⊥ d, AH = 3 cm, AM = 5 cm, M thuộc d. Độ dài HM là:",
          ["4 cm", "2 cm", "8 cm", "√34 cm"], 0,
          "Theo định lí Pythagoras: HM = √(25 − 9) = 4 cm."),
        q("Điểm A cách đường thẳng d là 4 cm. Với mọi M thuộc d, ta có:",
          ["AM ≥ 4 cm", "AM ≤ 4 cm", "AM = 4 cm", "AM = 0"], 0,
          "Khoảng cách là đường ngắn nhất."),
        q("Trong tam giác ABC có AH ⊥ BC (H thuộc BC), ta có AH ≤ AB vì:",
          ["AH là cạnh góc vuông, AB là cạnh huyền", "AB là cạnh góc vuông", "AH = AB", "Không đủ điều kiện"], 0,
          "Trong tam giác vuông AHB, AB là cạnh huyền."),
        q("Cho AB ⊥ AC, AB = 3 cm. Khoảng cách từ B đến đường thẳng AC là:",
          ["3 cm", "4 cm", "0 cm", "Không xác định"], 0,
          "BA ⊥ AC nên khoảng cách là AB = 3 cm."),
        q("Khoảng cách từ một điểm đến một đường thẳng là:",
          ["Độ dài đoạn vuông góc hạ từ điểm đó", "Độ dài đường xiên lớn nhất", "Tổng hai đường xiên", "Độ dài đường trung tuyến"], 0,
          "Định nghĩa khoảng cách từ điểm đến đường thẳng."),
        q("Trong Hình 9.9, M khác H thì tam giác AHM là:",
          ["Tam giác vuông tại H", "Tam giác đều", "Tam giác cân tại A", "Tam giác tù"], 0,
          "AH ⊥ d nên góc AHM = 90°."),
        q("Đường vuông góc kẻ từ A đến d, nếu AH = 2 cm thì mọi đường xiên AM (M thuộc d) đều có độ dài:",
          ["Lớn hơn hoặc bằng 2 cm", "Nhỏ hơn 2 cm", "Bằng 2 cm", "Bằng 0"], 0,
          "Đường vuông góc là đường ngắn nhất."),
        q("Khi M thay đổi trên d và xa H dần, đường xiên AM:",
          ["Càng lớn", "Càng nhỏ", "Không đổi", "Bằng 0"], 0,
          "Theo quan hệ góc – cạnh đối diện, xa H thì AM lớn hơn."),
        q("Trong tam giác vuông AHM (H là chân đường vuông góc), AM² bằng:",
          ["AH² + HM²", "AH² − HM²", "AH + HM", "AH·HM"], 0,
          "Định lí Pythagoras cho tam giác vuông AHM."),
        q("Cho A ngoài đường thẳng d, AH = 6 cm, AM = 10 cm (M thuộc d). Độ dài HM là:",
          ["8 cm", "4 cm", "16 cm", "√34 cm"], 0,
          "HM = √(100 − 36) = 8 cm."),
        q("Đường vuông góc kẻ từ A đến d có độ dài nhỏ hơn đường xiên AM. Điều này đúng vì:",
          ["Tam giác AHM vuông tại H nên AM là cạnh huyền", "AM là cạnh góc vuông", "AH bằng AM", "H trùng M"], 0,
          "Cạnh huyền lớn hơn cạnh góc vuông."),
    ],
    bt_co_ban=[
        bt("Bài 9.6: Chiều cao của tam giác ứng với một cạnh có phải là khoảng cách từ đỉnh đối diện đến đường thẳng chứa cạnh đó không? (gõ: có hoặc không)",
           ["có"], "Đó đúng là khoảng cách từ đỉnh đến đường thẳng."),
        bt("Bài 9.7a: Trong hình vuông ABCD, đỉnh nào cách đều hai điểm A và C? (gõ 2 đỉnh, ví dụ BD)",
           ["BD", "DB"], "B và D nằm trên đường trung trực của AC."),
        bt("Bài 9.7b: Trong hình vuông ABCD, đỉnh nào cách đều hai đường thẳng AB và AD? (gõ 2 đỉnh, ví dụ AC)",
           ["AC", "CA"], "A và C nằm trên hai đường phân giác của góc tạo bởi AB, AD."),
        bt("Bài 9.8a: Tam giác cân ABC (AB = AC), M thay đổi trên BC. AM nhỏ nhất khi M ở đâu? (gõ: trung điểm BC)",
           ["trung điểm", "trung điểm BC", "trung điểm của BC"], "AM nhỏ nhất khi AM ⊥ BC, lúc đó M là trung điểm BC."),
        bt("Bài 9.15: Có tam giác nào với độ dài ba cạnh 2,5 cm; 3,4 cm và 6 cm không? (gõ: có hoặc không)",
           ["không"], "2,5 + 3,4 = 5,9 < 6 nên không tạo được tam giác."),
        bt("Bài 9.16: Tính chu vi tam giác cân biết hai cạnh là 2 cm và 5 cm (đơn vị cm).",
           ["12", "12 cm"], "Tam giác cân có các cạnh 5, 5, 2 (vì 2 + 2 < 5 không thỏa mãn nên cạnh đáy là 2). Chu vi = 12 cm."),
        bt("Bài 9.17: Hai cạnh của tam giác bằng 7 cm và 2 cm. Cạnh còn lại có số đo là số tự nhiên lẻ. Tính độ dài cạnh đó (cm).",
           ["7", "7 cm"], "Cạnh x thỏa 5 < x < 9, x lẻ nên x = 7."),
    ],
    bt_nang_cao=[
        nc("Bài 9.8b: Tam giác cân ABC (AB = AC), M là điểm tuỳ ý nằm giữa B và C. Chứng minh rằng AM < AB.",
           "Xét góc AMB hoặc AMC; trong tam giác AMB, góc đối diện AB so với AM.",
           ["AM < AB"],
           "Vì M nằm giữa B và C nên ∠ABM hoặc ∠ACM là góc không tù; so sánh cạnh với góc đối diện chứng minh AM < AB."),
        nc("Bài 9.9: Cho tam giác ABC vuông tại A. Hai điểm M, N theo thứ tự nằm trên các cạnh AB, AC (M, N không là đỉnh). Chứng minh MN < BC.",
           "So sánh MN với NB và NB với BC; dùng quan hệ góc – cạnh trong tam giác vuông.",
           ["MN < BC"],
           "Trong tam giác vuông MAN ta có MN < NB; trong tam giác vuông NAB ta có NB < BC. Suy ra MN < BC."),
        nc("Bài 9.18: Biết hai cạnh của tam giác có độ dài a và b. Dựa vào bất đẳng thức tam giác, giải thích vì sao chu vi tam giác đó lớn hơn 2a và nhỏ hơn 2(a + b).",
           "Dùng bất đẳng thức tam giác: |a − b| < c < a + b.",
           ["2a < chu vi < 2(a+b)"],
           "Cạnh thứ ba c thỏa b − a < c < a + b nên chu vi = a + b + c > 2a và < 2(a + b)."),
        nc("Bài 9.19: Hai khu vườn A, B nằm cùng phía với con kênh d. Xác định trên bờ kênh một điểm C để tổng độ dài đường ống nước từ máy bơm đến hai khu vườn là ngắn nhất.",
           "Lấy B' đối xứng với B qua d; khi đó CB = CB' và tổng AC + CB = AC + CB'.",
           ["Giao điểm của AB' với d"],
           "Tổng AC + CB = AC + CB' ≥ AB' với đẳng thức khi C nằm trên đoạn AB', tức C là giao điểm của AB' và d."),
    ],
)

# ============================================================
# BÀI 33: QUAN HỆ GIỮA BA CẠNH CỦA MỘT TAM GIÁC
# ============================================================
B33 = bai(
    ly_thuyet="""📌 1. BẤT ĐẲNG THỨC TAM GIÁC
Định lí: Trong một tam giác, độ dài của một cạnh bất kì luôn nhỏ hơn tổng độ dài hai cạnh còn lại.
- Với tam giác ABC: AB < AC + BC; AC < AB + BC; BC < AB + AC.
- Các hệ thức trên gọi là các bất đẳng thức tam giác.

📌 2. HỆ QUẢ
Trong một tam giác, độ dài của một cạnh bất kì luôn lớn hơn hiệu độ dài hai cạnh còn lại.
- Nếu a, b, c là độ dài ba cạnh của một tam giác thì: b − c < a < b + c.

📌 3. CÁCH KIỂM TRA BA ĐỘ DÀI CÓ LÀ BA CẠNH CỦA MỘT TAM GIÁC
- Chỉ cần so sánh: độ dài lớn nhất có nhỏ hơn tổng hai độ dài còn lại (hoặc độ dài nhỏ nhất có lớn hơn hiệu hai độ dài còn lại) hay không.
- Nếu ba độ dài không thoả mãn bất đẳng thức tam giác thì không phải là ba cạnh của một tam giác.""",
    vi_du="""Ví dụ: Kiểm tra bộ ba độ dài nào không thể là độ dài ba cạnh của một tam giác.
a) 2 cm, 4 cm, 7 cm: vì 2 + 4 = 6 < 7 nên không thể là ba cạnh của tam giác.
b) 2 cm, 3 cm, 4 cm: vì 4 < 2 + 3 = 5 (và 2 > 4 − 3 = 1) nên có thể là ba cạnh của tam giác (vẽ được tam giác ABC).

Luyện tập: Bộ ba nào không thể là độ dài ba cạnh của một tam giác?
a) 5 cm, 4 cm, 6 cm.
b) 3 cm, 6 cm, 10 cm.

Vận dụng: Giải thích vì sao nếu dựng cột điện ở vị trí C trên đoạn thẳng AB thì tổng độ dài dây dẫn điện là ngắn nhất.""",
    cau_hoi=[
        q("Trong một tam giác, độ dài một cạnh luôn nhỏ hơn:",
          ["Tổng độ dài hai cạnh còn lại", "Hiệu độ dài hai cạnh còn lại", "Tích hai cạnh còn lại", "Cạnh lớn nhất"], 0,
          "Đó là bất đẳng thức tam giác."),
        q("Trong một tam giác, độ dài một cạnh luôn lớn hơn:",
          ["Hiệu độ dài hai cạnh còn lại", "Tổng độ dài hai cạnh còn lại", "Tích hai cạnh còn lại", "Cạnh nhỏ nhất"], 0,
          "Đó là hệ quả của bất đẳng thức tam giác."),
        q("Ba độ dài 10 cm, 20 cm, 25 cm có thể là ba cạnh của một tam giác không?",
          ["Có", "Không", "Chưa đủ dữ liệu", "Chỉ là tam giác vuông"], 0,
          "10 + 20 = 30 > 25 nên thỏa mãn."),
        q("Ba độ dài 5 cm, 15 cm, 25 cm có thể là ba cạnh của một tam giác không?",
          ["Không", "Có", "Chưa đủ dữ liệu", "Chỉ là tam giác đều"], 0,
          "5 + 15 = 20 < 25 nên không thỏa mãn."),
        q("Ba độ dài 2 cm, 4 cm, 7 cm không tạo thành tam giác vì:",
          ["2 + 4 < 7", "2 + 4 > 7", "2 + 7 < 4", "4 + 7 < 2"], 0,
          "Tổng hai cạnh nhỏ hơn cạnh còn lại."),
        q("Ba độ dài 2 cm, 3 cm, 4 cm có là ba cạnh của một tam giác không?",
          ["Có", "Không", "Chỉ khi có góc vuông", "Không xác định"], 0,
          "2 + 3 = 5 > 4 nên thỏa mãn."),
        q("Ba đoạn thẳng 1 cm, 2 cm, 4 cm có ghép thành tam giác không?",
          ["Không", "Có", "Chỉ khi là tam giác cân", "Chỉ khi là tam giác vuông"], 0,
          "1 + 2 = 3 < 4 nên không thể."),
        q("Ba đoạn thẳng 5 cm, 5 cm, 10 cm có ghép thành tam giác không?",
          ["Không", "Có", "Có, là tam giác cân", "Có, là tam giác đều"], 0,
          "5 + 5 = 10 không lớn hơn 10 nên không tạo được tam giác."),
        q("Ba độ dài 3 cm, 4 cm, 5 cm có là ba cạnh của một tam giác không?",
          ["Có", "Không", "Chỉ khi là tam giác đều", "Không xác định"], 0,
          "3 + 4 = 7 > 5 nên thỏa mãn."),
        q("Để kiểm tra ba độ dài có là ba cạnh của tam giác, ta chỉ cần:",
          ["So sánh cạnh lớn nhất với tổng hai cạnh còn lại", "So sánh tổng ba cạnh với 10", "So sánh hai cạnh bằng nhau", "Tính diện tích"], 0,
          "Theo chú ý trong sách."),
        q("Tam giác ABC có AB = 4 cm, BC = 6 cm. Độ dài lớn nhất có thể của AC (số nguyên cm) là:",
          ["9", "10", "11", "12"], 0,
          "2 < AC < 10 nên AC lớn nhất có thể là 9."),
        q("Tam giác ABC có AB = 4 cm, BC = 6 cm. Độ dài nhỏ nhất có thể của AC (số nguyên cm) là:",
          ["1", "2", "3", "4"], 2,
          "2 < AC < 10 nên AC nhỏ nhất nguyên là 3."),
        q("Tam giác ABC có AB = 1 cm, BC = 7 cm, AC là số nguyên cm. Khi đó AC bằng:",
          ["6", "7", "8", "9"], 1,
          "6 < AC < 8 nên AC = 7."),
        q("Tam giác ABC có AB = 2 cm, BC = 6 cm (BC lớn nhất), AC là số nguyên cm. Khi đó AC bằng:",
          ["3", "4", "5", "6"], 2,
          "4 < AC ≤ 6 và AC < BC = 6 nên AC = 5."),
        q("Tam giác có hai cạnh 7 cm và 2 cm. Cạnh thứ ba là số tự nhiên lẻ có thể là:",
          ["5", "7", "9", "3"], 1,
          "Cạnh x thỏa 5 < x < 9; số lẻ đó là 7."),
        q("Tam giác cân có hai cạnh 2 cm và 5 cm. Chu vi của tam giác là:",
          ["9 cm", "12 cm", "16 cm", "14 cm"], 1,
          "Các cạnh là 5, 5, 2 nên chu vi = 12 cm."),
        q("Hệ thức tổng hai cạnh lớn hơn cạnh còn lại được gọi là:",
          ["Bất đẳng thức tam giác", "Định lí Pythagoras", "Định lí Thales", "Tính chất đường trung tuyến"], 0,
          "Gọi là bất đẳng thức tam giác."),
        q("Ba đoạn AB = 3, AC = 4, BC = 1 có tạo thành tam giác không?",
          ["Không", "Có", "Có, là tam giác vuông", "Có, là tam giác cân"], 0,
          "1 + 3 = 4 không lớn hơn 4 nên không tạo thành tam giác."),
        q("Trong tam giác ABC có AC = 5 và BC = 3, cạnh AB nằm trong khoảng:",
          ["(2; 8)", "(3; 5)", "(5; 8)", "(0; 3)"], 0,
          "5 − 3 < AB < 5 + 3 nên 2 < AB < 8."),
        q("Trong tam giác có ba cạnh 2, 3, 4, góc lớn nhất đối diện cạnh:",
          ["2", "3", "4", "Không xác định"], 2,
          "Cạnh lớn nhất 4 đối diện góc lớn nhất."),
        q("Vận dụng: vì sao tổng dây dẫn AC + CB ngắn nhất khi C nằm trên AB?",
          ["Bất đẳng thức tam giác", "Tính chất đường trung tuyến", "Định lí Pythagoras", "Định lí Thales"], 0,
          "Với C' ngoài đoạn AB, AC' + C'B > AB = AC + CB."),
        q("Tam giác ABC có a = 5, b = 8. Với c là cạnh thứ ba, ta có:",
          ["3 < c < 13", "c > 13", "c < 3", "c = 5"], 0,
          "b − a < c < a + b nên 3 < c < 13."),
        q("Bộ ba 4 cm, 6 cm, 10 cm có tạo thành tam giác không?",
          ["Không", "Có", "Có, là tam giác cân", "Có, là tam giác đều"], 0,
          "4 + 6 = 10 không lớn hơn 10."),
        q("Bộ ba 3 cm, 4 cm, 6 cm có là ba cạnh của một tam giác không?",
          ["Có", "Không", "Chỉ khi là tam giác vuông", "Không xác định"], 0,
          "3 + 4 = 7 > 6 nên thỏa mãn (Luyện tập 9.10b)."),
        q("Bộ ba 2 cm, 4 cm, 5 cm có là ba cạnh của một tam giác không?",
          ["Có", "Không", "Chỉ khi là tam giác đều", "Không xác định"], 0,
          "2 + 4 = 6 > 5 nên thỏa mãn (Luyện tập 9.10c)."),
        q("Bộ ba 3 cm, 6 cm, 10 cm có là ba cạnh của một tam giác không?",
          ["Không", "Có", "Có, là tam giác cân", "Có, là tam giác vuông"], 0,
          "3 + 6 = 9 < 10 nên không thỏa mãn."),
        q("Với a = 4, b = 6, c = 9, có tồn tại tam giác có ba cạnh này không?",
          ["Có", "Không", "Chỉ khi là tam giác đều", "Không xác định"], 0,
          "4 + 6 = 10 > 9 nên thỏa mãn."),
        q("Ba đoạn thẳng 3 cm, 7 cm, 9 cm có tạo thành tam giác không?",
          ["Có", "Không", "Chỉ khi là tam giác vuông", "Không xác định"], 0,
          "3 + 7 = 10 > 9 nên thỏa mãn."),
        q("Ba đoạn thẳng 1 cm, 1 cm, 2 cm có tạo thành tam giác không?",
          ["Không", "Có", "Có, là tam giác đều", "Có, là tam giác vuông"], 0,
          "1 + 1 = 2 không lớn hơn 2 nên không tạo thành tam giác."),
        q("Ba độ dài 6 cm, 8 cm, 13 cm có tạo thành tam giác không?",
          ["Không", "Có", "Có, là tam giác vuông", "Có, là tam giác cân"], 0,
          "6 + 8 = 14 > 13 nên thỏa mãn bất đẳng thức tam giác."),
    ],
    bt_co_ban=[
        bt("Luyện tập a: Bộ ba 5 cm, 4 cm, 6 cm có là ba cạnh của một tam giác không? (gõ: có hoặc không)",
           ["có"], "5 + 4 > 6."),
        bt("Luyện tập b: Bộ ba 3 cm, 6 cm, 10 cm có là ba cạnh của một tam giác không? (gõ: có hoặc không)",
           ["không"], "3 + 6 = 9 < 10."),
        bt("Bài 9.10: Trong các bộ ba 2 cm–3 cm–5 cm; 3 cm–4 cm–6 cm; 2 cm–4 cm–5 cm, bộ nào không thể là ba cạnh của một tam giác? (gõ bộ, ví dụ 2-3-5)",
           ["2-3-5", "2, 3, 5", "2 3 5"], "2 + 3 = 5 không lớn hơn 5."),
        bt("Bài 9.11a: Tam giác ABC có AB = 1 cm, BC = 7 cm và CA là số nguyên (cm). Tính CA (cm).",
           ["7", "7 cm"], "6 < CA < 8 nên CA = 7."),
        bt("Bài 9.11b: Tam giác ABC có AB = 2 cm, BC = 6 cm và BC là cạnh lớn nhất; CA là số nguyên (cm). Tính CA (cm).",
           ["5", "5 cm"], "4 < CA < 6 nên CA = 5."),
    ],
    bt_nang_cao=[
        nc("Bài 9.12: Cho điểm M nằm bên trong tam giác ABC. Gọi N là giao điểm của đường thẳng AM và cạnh BC. (a) So sánh MB với MN + NB, từ đó suy ra MA + MB < NA + NB. (b) So sánh NA với CA + CN, từ đó suy ra NA + NB < CA + CB. (c) Chứng minh MA + MB < CA + CB.",
           "Áp dụng bất đẳng thức tam giác cho các tam giác MNB, ANC.",
           ["MA + MB < CA + CB"],
           "(a) MB < MN + NB nên MA + MB < MA + MN + NB = NA + NB. (b) NA < CA + CN nên NA + NB < CA + CN + NB = CA + CB. Từ (a),(b): MA + MB < CA + CB."),
        nc("Bài 9.13: Cho tam giác ABC, điểm D nằm giữa B và C. Chứng minh rằng AD nhỏ hơn nửa chu vi tam giác ABC.",
           "Áp dụng bất đẳng thức tam giác cho AD với hai đường AB, AC và BD + DC = BC.",
           ["AD < (AB + BC + CA)/2"],
           "AD < AB + BD và AD < AC + DC. Cộng hai bất đẳng thức: 2AD < AB + AC + BC, suy ra AD < nửa chu vi."),
        nc("Bài 9.14 (LTC): Nếu M là điểm tuỳ ý nằm trên cạnh BC hoặc CD của hình vuông ABCD, giải thích vì sao AM luôn lớn hơn hoặc bằng độ dài cạnh hình vuông.",
           "Với M trên BC, AB ⊥ BC; với M trên CD, AD ⊥ CD.",
           ["AM ≥ cạnh hình vuông"],
           "AB là đường vuông góc từ A đến BC nên AM ≥ AB; tương tự AM ≥ AD khi M thuộc CD."),
        nc("Bài 9.17 (LTC): Vẽ tam giác có hai cạnh 7 cm và 2 cm. Tính độ dài cạnh còn lại biết rằng số đo của nó (theo cm) là một số tự nhiên lẻ.",
           "Dùng bất đẳng thức tam giác: 5 < x < 9.",
           ["7"],
           "x ∈ {6, 7, 8}; số lẻ là 7."),
    ],
)

# ============================================================
# BÀI 34: SỰ ĐỒNG QUY CỦA BA ĐƯỜNG TRUNG TUYẾN, BA ĐƯỜNG PHÂN GIÁC TRONG MỘT TAM GIÁC
# ============================================================
B34 = bai(
    ly_thuyet="""📌 1. ĐƯỜNG TRUNG TUYẾN
- Đoạn thẳng AM nối đỉnh A của tam giác ABC với trung điểm M của cạnh BC gọi là đường trung tuyến (xuất phát từ đỉnh A hoặc ứng với cạnh BC) của tam giác ABC.
- Mỗi tam giác có ba đường trung tuyến.

📌 2. SỰ ĐỒNG QUY CỦA BA ĐƯỜNG TRUNG TUYẾN
Định lí 1: Ba đường trung tuyến của một tam giác cùng đi qua một điểm. Điểm đó cách mỗi đỉnh một khoảng bằng 2/3 độ dài đường trung tuyến đi qua đỉnh ấy.
- Điểm đồng quy của ba đường trung tuyến gọi là trọng tâm của tam giác.
- Ví dụ: GA/MA = GB/NB = GC/PC = 2/3.

📌 3. ĐƯỜNG PHÂN GIÁC
- Trong tam giác ABC, tia phân giác của góc A cắt cạnh BC tại D thì đoạn thẳng AD gọi là đường phân giác (xuất phát từ đỉnh A) của tam giác ABC.
- Mỗi tam giác có ba đường phân giác.

📌 4. SỰ ĐỒNG QUY CỦA BA ĐƯỜNG PHÂN GIÁC
Định lí 2: Ba đường phân giác của một tam giác đồng quy tại một điểm. Điểm này cách đều ba cạnh của tam giác đó.
- Điểm đồng quy của ba đường phân giác là tâm của đường tròn nội tiếp tam giác.""",
    vi_du="""Ví dụ 1: Cho tam giác ABC với AM là trung tuyến và G là trọng tâm.
a) Chứng minh GA = 2GM.
b) Biết GM = 2 cm, tính GA.
Giải: GA = (2/3)MA và GM = (1/3)MA nên GA = 2GM. Khi GM = 2 cm thì GA = 4 cm.

Luyện tập 1: Trong tam giác ABC ở Ví dụ 1, cho trung tuyến BN và GN = 1 cm. Tính GB và NB.
Giải: GB = 2GN = 2 cm; NB = GB + GN = 3 cm.

Ví dụ 2: Tam giác ABC cân tại A, I là giao điểm ba đường phân giác. Chứng minh AI là đường trung tuyến của tam giác ABC.

Luyện tập 2: Cho tam giác ABC có hai đường phân giác AM, BN cắt nhau tại I. Hỏi CI có là đường phân giác của góc C không? (Có, vì ba đường phân giác đồng quy tại I.)

Vận dụng 2: Chứng minh rằng trong tam giác đều, điểm cách đều ba cạnh của tam giác là trọng tâm của tam giác đó.""",
    cau_hoi=[
        q("Đoạn thẳng nối đỉnh của tam giác với trung điểm cạnh đối diện được gọi là:",
          ["Đường trung tuyến", "Đường cao", "Đường trung trực", "Đường trung bình"], 0,
          "Đó là định nghĩa đường trung tuyến."),
        q("Mỗi tam giác có mấy đường trung tuyến?",
          ["1", "2", "3", "4"], 2,
          "Mỗi đỉnh có một đường trung tuyến."),
        q("Ba đường trung tuyến của tam giác đồng quy tại điểm gọi là:",
          ["Trọng tâm", "Trực tâm", "Tâm đường tròn ngoại tiếp", "Tâm đường tròn nội tiếp"], 0,
          "Điểm đồng quy trung tuyến là trọng tâm."),
        q("Trọng tâm cách mỗi đỉnh một khoảng bằng:",
          ["2/3 độ dài đường trung tuyến đi qua đỉnh đó", "1/2 độ dài cạnh", "1/3 độ dài trung tuyến", "Độ dài cạnh đối diện"], 0,
          "Đó là nội dung Định lí 1."),
        q("Trong tam giác ABC, G là trọng tâm, AM là trung tuyến. Ta có:",
          ["GA = 2GM", "GA = GM", "GA = 3GM", "GM = 3GA"], 0,
          "Từ Định lí 1: GA = 2GM."),
        q("Trọng tâm G, GM = 2 cm (M là trung điểm của BC, A là đỉnh). Khi đó GA bằng:",
          ["2 cm", "4 cm", "6 cm", "8 cm"], 1,
          "GA = 2GM = 4 cm."),
        q("Trọng tâm G của tam giác chia đường trung tuyến AM theo tỉ số GA : AM bằng:",
          ["2 : 3", "1 : 2", "1 : 3", "3 : 2"], 0,
          "GA = (2/3) AM."),
        q("Trọng tâm G, trung tuyến AM. Tỉ số GM : AM bằng:",
          ["1 : 3", "1 : 2", "2 : 3", "1 : 4"], 0,
          "GM = (1/3) AM."),
        q("Trong Luyện tập 1, biết GN = 1 cm. Khi đó GB bằng:",
          ["1 cm", "2 cm", "3 cm", "4 cm"], 1,
          "GB = 2GN = 2 cm."),
        q("Trong Luyện tập 1, biết GN = 1 cm. Khi đó NB bằng:",
          ["2 cm", "3 cm", "4 cm", "6 cm"], 1,
          "NB = GB + GN = 2 + 1 = 3 cm."),
        q("Tia phân giác của góc A cắt cạnh BC tại D, đoạn AD gọi là:",
          ["Đường phân giác", "Đường cao", "Đường trung trực", "Đường trung tuyến"], 0,
          "Đó là định nghĩa đường phân giác."),
        q("Mỗi tam giác có mấy đường phân giác?",
          ["1", "2", "3", "4"], 2,
          "Mỗi đỉnh có một đường phân giác."),
        q("Ba đường phân giác của một tam giác đồng quy tại một điểm, điểm này cách đều:",
          ["Ba cạnh của tam giác", "Ba đỉnh của tam giác", "Hai đỉnh", "Các trung điểm"], 0,
          "Đó là nội dung Định lí 2."),
        q("Điểm đồng quy của ba đường phân giác là tâm của:",
          ["Đường tròn nội tiếp tam giác", "Đường tròn ngoại tiếp tam giác", "Trọng tâm", "Trực tâm"], 0,
          "Đường tròn tiếp xúc với ba cạnh bên trong tam giác."),
        q("Trong Ví dụ 2, tam giác ABC cân tại A thì giao điểm ba đường phân giác nằm trên:",
          ["Đường trung tuyến xuất phát từ A", "Đường cao từ B", "Cạnh BC", "Đường trung trực AB"], 0,
          "Vì AI là đường trung tuyến của tam giác ABC."),
        q("Trong Ví dụ 2, khi chứng minh BM = CM, ta dùng trường hợp bằng nhau:",
          ["c.g.c", "c.c.c", "g.c.g", "Cạnh huyền – góc nhọn"], 0,
          "Tam giác ABM = ACM theo c.g.c."),
        q("Luyện tập 2: tam giác ABC có hai đường phân giác AM, BN cắt nhau tại I. Thì CI là đường phân giác của góc C:",
          ["Có", "Không", "Chỉ khi tam giác cân", "Chỉ khi tam giác đều"], 0,
          "Ba đường phân giác đồng quy nên CI là phân giác của góc C."),
        q("Trọng tâm của tam giác luôn nằm ở đâu?",
          ["Bên trong tam giác", "Bên ngoài tam giác", "Trên một cạnh", "Trùng một đỉnh"], 0,
          "Trọng tâm luôn nằm bên trong tam giác."),
        q("Trong tam giác đều, điểm cách đều ba cạnh của tam giác là:",
          ["Trọng tâm", "Trực tâm", "Điểm bất kì", "Trung điểm một cạnh"], 0,
          "Vận dụng 2: đó là trọng tâm."),
        q("Vận dụng 1: để tấm bìa hình tam giác cân bằng trên giá nhọn, cần đặt tại:",
          ["Trọng tâm", "Trực tâm", "Tâm đường tròn ngoại tiếp", "Trung điểm một cạnh"], 0,
          "Trọng tâm là điểm cân bằng của tấm bìa."),
        q("Tam giác ABC có M là trung điểm BC và AM là trung tuyến. Khi đó:",
          ["M là trung điểm BC", "M là chân đường cao", "M là chân phân giác", "M là đỉnh"], 0,
          "Trung tuyến nối đỉnh với trung điểm cạnh đối diện."),
        q("Với G là trọng tâm tam giác ABC, BG bằng bao nhiêu lần GN (N là trung điểm AC)?",
          ["1", "2", "3", "1/2"], 1,
          "BG = 2GN."),
        q("Trọng tâm G, trung tuyến AM, GM = 3 cm. Khi đó AG bằng:",
          ["6 cm", "3 cm", "9 cm", "4 cm"], 0,
          "AG = 2GM = 6 cm."),
        q("Đường phân giác của góc A là tia:",
          ["Chia góc A thành hai góc bằng nhau", "Vuông góc với BC", "Đi qua trung điểm BC", "Đi qua trọng tâm"], 0,
          "Định nghĩa tia phân giác của góc."),
        q("Trọng tâm G của tam giác ABC, với trung tuyến AM: GM bằng:",
          ["1/3 AM", "1/2 AM", "2/3 AM", "AM"], 0,
          "GM = (1/3) AM."),
        q("Điểm đồng quy ba đường phân giác và điểm đồng quy ba đường trung tuyến của một tam giác:",
          ["Có thể khác nhau", "Luôn trùng nhau", "Luôn nằm trên cạnh", "Luôn là trung điểm"], 0,
          "Trong tam giác thường, hai điểm này khác nhau (trừ tam giác đều)."),
        q("Trong tam giác đều, ba đường phân giác và ba đường trung tuyến:",
          ["Trùng nhau", "Phân biệt", "Song song", "Vuông góc"], 0,
          "Trong tam giác đều, các đường này đều trùng nhau."),
        q("Một tam giác có ba đường phân giác đồng quy tại I. Điểm I cách đều:",
          ["Ba cạnh của tam giác", "Ba đỉnh", "Hai đỉnh", "Ba trung điểm"], 0,
          "Đó là Định lí 2."),
        q("Trong tam giác cân tại A, đường trung tuyến AI cũng là:",
          ["Đường phân giác và đường cao", "Đường trung tuyến duy nhất", "Đường cao từ B", "Không phải đường nào"], 0,
          "Trong tam giác cân, đường trung tuyến ứng với đáy cũng là phân giác và đường cao."),
        q("Trong tam giác ABC, G là trọng tâm. Điều nào sau đây đúng?",
          ["GA = 2GM với M là trung điểm BC", "GA = GM", "GA = 3GM", "GM = 2GA"], 0,
          "Trọng tâm chia trung tuyến theo tỉ số 2 : 1 tính từ đỉnh."),
    ],
    bt_co_ban=[
        bt("Ví dụ 1 (b): G là trọng tâm tam giác ABC, AM là trung tuyến, GM = 2 cm. Tính GA (cm).",
           ["4", "4 cm"], "GA = 2GM = 4 cm."),
        bt("Luyện tập 1: Tam giác ABC có trung tuyến BN, G là trọng tâm, GN = 1 cm. Tính GB (cm).",
           ["2", "2 cm"], "GB = 2GN = 2 cm."),
        bt("Luyện tập 1: Tiếp theo, tính NB (cm).",
           ["3", "3 cm"], "NB = GB + GN = 3 cm."),
        bt("Bài 9.20: Tam giác ABC có trung tuyến BN, CP và trọng tâm G. Điền số thích hợp vào dấu '?': BG = ? · BN. (gõ phân số, ví dụ 2/3)",
           ["2/3", "2 / 3"], "BG = (2/3)BN."),
        bt("Bài 9.20: Tiếp theo, BG = ? · GN (gõ số nguyên).",
           ["2"], "BG = 2GN."),
        bt("Luyện tập 2: Tam giác ABC có hai đường phân giác AM, BN cắt nhau tại I. CI có là đường phân giác của góc C không? (gõ: có hoặc không)",
           ["có"], "Ba đường phân giác đồng quy."),
        bt("Bài 9.23: Kí hiệu I là giao điểm ba đường phân giác của tam giác ABC. Tính góc BIC (độ) biết góc BAC = 120°.",
           ["150", "150°"], "∠BIC = 90° + Â/2 = 90° + 60° = 150°."),
    ],
    bt_nang_cao=[
        nc("Bài 9.21: (a) Trong tam giác cân, hai đường trung tuyến ứng với hai cạnh bên bằng nhau. (b) Ngược lại, nếu tam giác có hai đường trung tuyến bằng nhau thì tam giác đó cân.",
           "Dùng trọng tâm và các tam giác bằng nhau (c.g.c, c.c.c).",
           ["Chứng minh"],
           "(a) Hai tam giác chứa trung tuyến bằng nhau theo c.g.c nên hai trung tuyến bằng nhau. (b) Dùng tính chất trọng tâm và định lí tổng ba góc để suy ra tam giác cân."),
        nc("Bài 9.22: Cho tam giác ABC có các trung tuyến BM và CN cắt nhau tại G. Biết góc GBC lớn hơn góc GCB. So sánh BM và CN.",
           "Trong tam giác GBC, góc lớn hơn đối diện cạnh lớn hơn; dùng GB = 2/3 BM, GC = 2/3 CN.",
           ["BM < CN"],
           "∠GBC > ∠GCB nên GC > GB, suy ra (2/3)CN > (2/3)BM, tức CN > BM."),
        nc("Bài 9.24: Gọi BE và CF là hai đường phân giác của tam giác ABC cân tại A. Chứng minh BE = CF.",
           "Dùng tam giác bằng nhau (g.c.g) với cạnh BC chung và các góc tương ứng.",
           ["BE = CF"],
           "Vì ABC cân tại A nên B̂ = Ĉ; ∠EBC = ∠FCB; BC chung, suy ra ΔBEC = ΔCFB (g.c.g), do đó BE = CF."),
        nc("Bài 9.25: Trong tam giác ABC, hai đường phân giác của góc B và góc C cắt nhau tại D. Kẻ DP ⊥ BC, DQ ⊥ CA, DR ⊥ AB. (a) Giải thích vì sao DP = DR. (b) Giải thích vì sao DP = DQ. (c) Từ đó suy ra DR = DQ. Tại sao D nằm trên tia phân giác của góc A?",
           "Dùng tính chất điểm trên tia phân giác cách đều hai cạnh của góc.",
           ["D nằm trên tia phân giác của góc A"],
           "D thuộc phân giác góc B nên DP = DR; D thuộc phân giác góc C nên DP = DQ. Do đó DR = DQ, mà D nằm bên trong góc A nên D thuộc tia phân giác góc A."),
    ],
)

# ============================================================
# BÀI 35: SỰ ĐỒNG QUY CỦA BA ĐƯỜNG TRUNG TRỰC, BA ĐƯỜNG CAO TRONG MỘT TAM GIÁC
# ============================================================
B35 = bai(
    ly_thuyet="""📌 1. ĐƯỜNG TRUNG TRỰC CỦA TAM GIÁC
- Trong một tam giác, đường trung trực của mỗi cạnh gọi là đường trung trực của tam giác. Mỗi tam giác có ba đường trung trực.

📌 2. SỰ ĐỒNG QUY CỦA BA ĐƯỜNG TRUNG TRỰC
Định lí 1: Ba đường trung trực của một tam giác đồng quy tại một điểm. Điểm này cách đều ba đỉnh của tam giác.
- Điểm đồng quy là tâm của đường tròn ngoại tiếp tam giác (đường tròn đi qua ba đỉnh).

📌 3. ĐƯỜNG CAO CỦA TAM GIÁC
- Đoạn thẳng kẻ từ một đỉnh, vuông góc với cạnh đối diện là một đường cao của tam giác. Mỗi tam giác có ba đường cao.

📌 4. SỰ ĐỒNG QUY CỦA BA ĐƯỜNG CAO
Định lí 2: Ba đường cao của một tam giác đồng quy tại một điểm.
- Điểm đồng quy của ba đường cao gọi là trực tâm của tam giác.
- Tam giác nhọn: trực tâm nằm bên trong tam giác. Tam giác vuông tại A: trực tâm trùng với A. Tam giác tù: trực tâm nằm bên ngoài tam giác.""",
    vi_du="""Ví dụ 1: Cho tam giác ABC cân tại A, vẽ đường trung tuyến AI.
a) Chứng minh AI là đường trung trực của cạnh BC.
b) Điểm cách đều ba đỉnh của tam giác ABC có nằm trên AI không?
Giải: a) ΔAIB = ΔAIC (c.c.c) nên ∠AIB = ∠AIC, mà hai góc kề bù nên đều bằng 90°. Vậy AI là đường trung trực của BC. b) Điểm cách đều ba đỉnh nằm trên đường trung trực BC nên nằm trên AI.

Ví dụ 2: Cho tam giác ABC, AB = AC, ... Tam giác đều: trực tâm H cách đều ba đỉnh (vì đường cao đồng thời là trung trực).

Luyện tập 1: Chứng minh rằng trong tam giác đều ABC, trọng tâm G cách đều ba đỉnh của tam giác đó.

Vận dụng 1: Để khoan giếng chung cách đều ba ngôi nhà (ba đỉnh tam giác không tù), chọn điểm là giao điểm ba đường trung trực của tam giác đó.

Thử thách nhỏ: Dùng tính chất đường trung trực của đoạn thẳng để giải thích: nếu Q cách đều ba đỉnh của tam giác ABC thì Q là giao điểm ba đường trung trực của tam giác ABC.

Luyện tập 2: a) Trong tam giác ABC cân tại A, đường trung trực của cạnh BC là đường cao và cũng là đường phân giác xuất phát từ A. b) Trong tam giác đều, điểm cách đều ba đỉnh cũng cách đều ba cạnh.""",
    cau_hoi=[
        q("Đường trung trực của đoạn thẳng BC là:",
          ["Đường thẳng vuông góc với BC tại trung điểm của BC", "Đường thẳng đi qua B", "Đường thẳng song song với BC", "Đường thẳng đi qua trọng tâm"], 0,
          "Đó là định nghĩa đường trung trực của đoạn thẳng."),
        q("Mỗi tam giác có mấy đường trung trực?",
          ["1", "2", "3", "4"], 2,
          "Mỗi cạnh có một đường trung trực."),
        q("Ba đường trung trực của tam giác đồng quy tại điểm, điểm này cách đều:",
          ["Ba đỉnh của tam giác", "Ba cạnh của tam giác", "Hai đỉnh", "Ba trung điểm"], 0,
          "Đó là Định lí 1."),
        q("Điểm đồng quy của ba đường trung trực là tâm của:",
          ["Đường tròn ngoại tiếp tam giác", "Đường tròn nội tiếp tam giác", "Đường tròn bàng tiếp", "Trọng tâm"], 0,
          "Đường tròn đi qua ba đỉnh là đường tròn ngoại tiếp."),
        q("Trong tam giác cân tại A, đường trung trực của BC cũng đi qua:",
          ["Đỉnh A", "Đỉnh B", "Đỉnh C", "Trọng tâm"], 0,
          "Vì AB = AC nên A nằm trên trung trực BC."),
        q("Tâm đường tròn ngoại tiếp tam giác vuông nằm ở:",
          ["Trung điểm cạnh huyền", "Đỉnh góc vuông", "Trọng tâm", "Chân đường cao"], 0,
          "Trung điểm cạnh huyền cách đều ba đỉnh."),
        q("Tâm đường tròn ngoại tiếp tam giác nhọn nằm:",
          ["Bên trong tam giác", "Bên ngoài tam giác", "Trên một cạnh", "Trùng một đỉnh"], 0,
          "Với tam giác nhọn, tâm nằm bên trong."),
        q("Tâm đường tròn ngoại tiếp tam giác tù nằm:",
          ["Bên ngoài tam giác", "Bên trong tam giác", "Trên cạnh đối diện góc tù", "Trùng đỉnh tù"], 0,
          "Với tam giác tù, tâm nằm bên ngoài."),
        q("Đường cao của tam giác là:",
          ["Đoạn thẳng kẻ từ một đỉnh vuông góc với cạnh đối diện", "Đoạn thẳng nối đỉnh với trung điểm cạnh đối diện", "Đường thẳng đi qua trung điểm hai cạnh", "Đoạn thẳng nối hai đỉnh"], 0,
          "Đó là định nghĩa đường cao."),
        q("Mỗi tam giác có mấy đường cao?",
          ["1", "2", "3", "4"], 2,
          "Mỗi đỉnh có một đường cao."),
        q("Ba đường cao của tam giác đồng quy tại một điểm gọi là:",
          ["Trực tâm", "Trọng tâm", "Tâm đường tròn nội tiếp", "Tâm đường tròn ngoại tiếp"], 0,
          "Điểm đồng quy của ba đường cao là trực tâm."),
        q("Trong tam giác nhọn, trực tâm nằm:",
          ["Bên trong tam giác", "Bên ngoài tam giác", "Trên một cạnh", "Trùng một đỉnh"], 0,
          "Với tam giác nhọn, trực tâm nằm bên trong."),
        q("Trong tam giác vuông tại A, trực tâm trùng với:",
          ["Đỉnh A", "Trung điểm BC", "Đỉnh B", "Không xác định"], 0,
          "Kí hiệu H ≡ A."),
        q("Trong tam giác tù, trực tâm nằm:",
          ["Bên ngoài tam giác", "Bên trong tam giác", "Trên cạnh", "Trùng đỉnh"], 0,
          "Với tam giác tù, trực tâm nằm bên ngoài."),
        q("Trong tam giác đều, trực tâm H cách đều:",
          ["Ba đỉnh của tam giác", "Hai đỉnh", "Một cạnh", "Không cách đều"], 0,
          "Ví dụ 2: trong tam giác đều trực tâm cách đều ba đỉnh."),
        q("Trong tam giác cân tại A, đường cao AI (I là trung điểm BC) là:",
          ["Đường trung trực của BC", "Đường phân giác góc B", "Đường cao từ B", "Cạnh bên"], 0,
          "AI vừa là trung tuyến, vừa là trung trực của BC."),
        q("Trong Ví dụ 1, để chứng minh ΔAIB = ΔAIC ta dùng trường hợp:",
          ["c.c.c", "c.g.c", "g.c.g", "Cạnh huyền – góc nhọn"], 0,
          "AB = AC, IB = IC, AI chung."),
        q("Điểm cách đều ba đỉnh của tam giác là giao điểm của:",
          ["Ba đường trung trực", "Ba đường cao", "Ba đường trung tuyến", "Ba đường phân giác"], 0,
          "Đó là Định lí 1."),
        q("Nếu OA = OB = OC thì O là tâm của:",
          ["Đường tròn ngoại tiếp tam giác ABC", "Đường tròn nội tiếp tam giác ABC", "Đường tròn bàng tiếp", "Đường tròn bất kì"], 0,
          "Điểm cách đều ba đỉnh là tâm đường tròn ngoại tiếp."),
        q("Trong tam giác đều, các điểm trọng tâm, trực tâm và tâm đường tròn ngoại tiếp:",
          ["Trùng nhau", "Phân biệt", "Nằm trên ba đỉnh", "Không xác định"], 0,
          "Trong tam giác đều, các điểm này trùng nhau."),
        q("Vận dụng 1: ba ngôi nhà là ba đỉnh tam giác nhọn, điểm khoan giếng cách đều ba nhà là:",
          ["Giao điểm ba đường trung trực", "Giao điểm ba đường cao", "Trọng tâm", "Trung điểm một cạnh"], 0,
          "Điểm cách đều ba đỉnh là giao điểm ba đường trung trực."),
        q("Đường trung trực của đoạn AB là tập hợp các điểm:",
          ["Cách đều A và B", "Thuộc đoạn AB", "Cách A một khoảng 0", "Nằm trên đường thẳng AB"], 0,
          "Điểm cách đều hai đầu đoạn thẳng nằm trên đường trung trực."),
        q("Trong tam giác cân tại A, đường cao kẻ từ A cũng là:",
          ["Đường trung tuyến, đường phân giác và đường trung trực", "Đường trung tuyến duy nhất", "Đường cao từ B", "Không phải đường nào"], 0,
          "Đó là nội dung nhận xét về tam giác cân."),
        q("Đường cao AH của tam giác ABC có H thuộc:",
          ["Đường thẳng BC", "Đường thẳng AB", "Đường thẳng AC", "Trung điểm AB"], 0,
          "H là chân đường cao nằm trên cạnh (đường thẳng) BC."),
        q("Trong tam giác đều ABC, đường cao AI cũng là:",
          ["Đường trung tuyến và đường phân giác", "Đường tròn", "Cạnh", "Đường thẳng song song BC"], 0,
          "Tam giác đều có các đường đặc biệt trùng nhau."),
        q("Trong tam giác ABC, ba đường cao đồng quy tại H. Nếu góc A tù thì H nằm:",
          ["Bên ngoài tam giác", "Bên trong tam giác", "Trên cạnh BC", "Trùng A"], 0,
          "Khi tam giác tù, trực tâm nằm ngoài tam giác."),
        q("Đường cao AI trong tam giác ABC có tính chất:",
          ["AI ⊥ BC", "AI ∥ BC", "AI là trung tuyến", "AI = BC"], 0,
          "Đường cao vuông góc với cạnh đối diện."),
        q("Trong tam giác ABC có ba đường trung trực đồng quy tại O. Khi đó:",
          ["OA = OB = OC", "OA = OB ≠ OC", "OA ≠ OB", "O là trọng tâm"], 0,
          "Điểm đồng quy ba đường trung trực cách đều ba đỉnh."),
        q("Tam giác ABC có ba đường cao đồng quy tại H. Nếu tam giác ABC vuông tại A thì:",
          ["H trùng A", "H trùng B", "H trùng C", "H nằm ngoài tam giác"], 0,
          "Với tam giác vuông tại A, trực tâm là đỉnh A."),
        q("Điểm cách đều ba đỉnh của tam giác nhọn nằm ở:",
          ["Bên trong tam giác", "Bên ngoài tam giác", "Trên một cạnh", "Trùng một đỉnh"], 0,
          "Tâm đường tròn ngoại tiếp tam giác nhọn nằm trong tam giác."),
    ],
    bt_co_ban=[
        bt("Bài 9.26: H là trực tâm của tam giác ABC không vuông. Tìm trực tâm của tam giác HBC. (gõ tên đỉnh, ví dụ A)",
           ["A"], "Trực tâm của tam giác HBC là A."),
        bt("Bài 9.27: Tam giác ABC có Â = 100° và trực tâm H. Tính góc BHC (độ).",
           ["80", "80°"], "∠BHC = 180° − Â = 80°."),
        bt("Ví dụ 2: Trong tam giác đều, trực tâm H cách đều ba đỉnh. (gõ: đúng hoặc sai)",
           ["đúng"], "Đường cao đồng thời là trung trực nên H là tâm đường tròn ngoại tiếp."),
    ],
    bt_nang_cao=[
        nc("Ví dụ 1 (LTC IX): Chứng minh rằng tam giác ABC có đường trung tuyến AM đồng thời là đường phân giác thì ABC là tam giác cân tại A.",
           "Lấy E đối xứng với A qua M; chứng minh ΔBAM = ΔCEM và ΔCAE cân.",
           ["ABC cân tại A"],
           "Từ ΔBAM = ΔCEM (c.g.c) có AB = EC và ∠BAM = ∠CEM = ∠CAM; suy ra ΔCAE cân tại C nên CE = CA, do đó AB = AC."),
        nc("Ví dụ 2 (LTC IX): Tam giác ABC có Â = 135°, các đường cao AI, BJ, CK, trực tâm H. Chứng minh (a) ΔAKC vuông cân, suy ra AK = CK; (b) ΔHAK = ΔBCK, suy ra AH = BC.",
           "Dùng tổng ba góc trong tam giác và góc kề bù của Â.",
           ["AK = CK; AH = BC"],
           "(a) ∠KAC = 45°, ∠ACK = 45°, do đó ΔAKC vuông cân tại K. (b) ΔHAK = ΔBCK (g.c.g) nên AH = BC."),
        nc("Bài 9.28: Xét điểm O cách đều ba đỉnh của tam giác ABC. Chứng minh rằng nếu O nằm trên một cạnh của tam giác ABC thì ABC là tam giác vuông.",
           "O là trung điểm cạnh huyền nếu nằm trên cạnh.",
           ["Tam giác vuông"],
           "O nằm trên cạnh BC và cách đều A, B, C nên O là trung điểm BC; khi đó BC là đường kính và góc A vuông."),
        nc("Bài 9.29: (a) Làm thế nào để xác định bán kính đường tròn của chi tiết máy bị gãy? (b) Trên bản đồ, ba khu dân cư A, B, C không thẳng hàng. Tìm điểm M cách đều A, B, C để quy hoạch trường học.",
           "Vẽ hai dây cung và các đường trung trực; giao điểm là tâm đường tròn.",
           ["Giao điểm ba đường trung trực"],
           "Chọn ba điểm trên đường tròn, dựng ba đường trung trực, giao điểm là tâm; bán kính là khoảng cách đến một điểm trên đường tròn. Tương tự M là giao điểm ba đường trung trực của tam giác ABC."),
        nc("Bài 9.30: Cho hai đường thẳng b, c không vuông góc, cắt nhau tại A và điểm H không thuộc b và c. Tìm điểm B thuộc b, C thuộc c sao cho tam giác ABC nhận H làm trực tâm.",
           "Kẻ qua H các đường vuông góc với c và b; B, C là giao với b, c.",
           ["Dựng đường thẳng qua H vuông góc với c và b"],
           "Dựng B ∈ b sao cho BH ⊥ AC, và C ∈ c sao cho CH ⊥ AB; khi đó H là trực tâm của tam giác ABC."),
        nc("Bài 9.31: Chứng minh rằng tam giác có đường trung tuyến và đường cao xuất phát từ cùng một đỉnh trùng nhau là tam giác cân.",
           "Dùng tam giác có đường trung tuyến đồng thời là đường cao.",
           ["Tam giác cân"],
           "Đường cao ⊥ cạnh đối và chia cạnh đó làm đôi nên đây là trung trực, do đó tam giác cân tại đỉnh đó."),
        nc("Bài 9.32: Cho ba điểm A, B, C thẳng hàng. Gọi d là đường thẳng vuông góc với AB tại A. Với M thuộc d, M khác A, vẽ CM; qua B kẻ đường thẳng vuông góc với CM cắt d tại N. Chứng minh BM ⊥ CN.",
           "Chứng minh B là trực tâm của tam giác CMN.",
           ["BM ⊥ CN"],
           "Trong tam giác MCN, NA ⊥ MC... (dùng hai đường cao) để suy ra B là trực tâm, nên MB ⊥ CN."),
        nc("Bài 9.33: Có một mảnh tôn hình tròn cần đục một lỗ ở tâm. Làm thế nào để xác định được tâm của mảnh tôn đó?",
           "Vẽ hai dây cung bất kì và dựng đường trung trực của chúng.",
           ["Giao điểm hai đường trung trực"],
           "Giao điểm của hai đường trung trực hai dây cung chính là tâm đường tròn."),
        nc("Bài 9.34: Cho tam giác ABC, kẻ tia phân giác At của góc tạo bởi tia AB và tia đối của tia AC. Chứng minh rằng nếu đường thẳng chứa tia At song song với BC thì tam giác ABC cân tại A.",
           "Dùng góc so le trong và tính chất phân giác.",
           ["ABC cân tại A"],
           "∠BAt = ∠ABC (so le trong), ∠tAC' = ∠ACB (đồng vị); do At là phân giác nên ∠B = ∠C."),
        nc("Bài 9.35: Kí hiệu S là diện tích tam giác. G là trọng tâm tam giác ABC, M là trung điểm BC. (a) Chứng minh S_GBC = (1/3)S_ABC. (b) Chứng minh S_GCA = S_GAB = (1/3)S_ABC.",
           "Gợi ý: GM = (1/3)AM; diện tích tam giác tỉ lệ với chiều cao.",
           ["S_GBC = (1/3) S_ABC"],
           "S_GBM = (1/3) S_ABM và S_GCM = (1/3) S_ACM; cộng lại suy ra S_GBC = (1/3)S_ABC; tương tự cho các tam giác còn lại."),
        nc("Bài 9.36 (BTCC IX): Tam giác ABC có góc BAC tù. Lấy D nằm giữa A và B, E nằm giữa A và C. Chứng minh DE < BC.",
           "Dùng quan hệ góc – cạnh trong tam giác ADE và tam giác ABC.",
           ["DE < BC"],
           "Dùng quan hệ góc – cạnh trong các tam giác ADE và ABC: do góc A tù nên cạnh đối diện góc tù BC là cạnh lớn nhất trong tam giác ABC, từ đó DE < BC."),
        nc("Bài 9.37 (BTCC IX): Tam giác ABC (AB > AC). Trên đường thẳng BC lấy D và E sao cho B nằm giữa D và C, C nằm giữa B và E, BD = BA, CE = CA. (a) So sánh góc ADE và góc AED. (b) So sánh AD và AE.",
           "Dùng tam giác cân ABD và ACE; so sánh góc đối diện cạnh.",
           ["ADE < AED; AD < AE"],
           "Tam giác ABD cân tại B và tam giác ACE cân tại C; so sánh các góc ở đáy và dùng quan hệ góc – cạnh đối diện để so sánh AD và AE. (Đối chiếu lời giải chi tiết trong sách trang 84.)"),
        nc("Bài 9.38 (BTCC IX): Gọi AI và AM lần lượt là đường cao và đường trung tuyến xuất phát từ A của tam giác ABC. Chứng minh (a) AI < (1/2)(AB + AC); (b) AM < (1/2)(AB + AC).",
           "Dùng khoảng cách ngắn nhất và bất đẳng thức tam giác; lấy D sao cho M là trung điểm AD.",
           ["AI < (AB+AC)/2; AM < (AB+AC)/2"],
           "AI ≤ AB và AI ≤ AC (đường vuông góc ngắn nhất) nên 2AI ≤ AB + AC, dấu bằng không xảy ra khi tam giác không vuông cân tại A. Với AM: lấy D đối xứng A qua M, ΔABM = ΔDCM (c.g.c) nên DC = AB; trong ΔADC có AD < AC + CD = AC + AB, mà AD = 2AM nên AM < (AB + AC)/2."),
        nc("Bài 9.39 (BTCC IX): Tam giác ABC có đường phân giác AD (D trên BC, BD = 2DC). Trên đường thẳng AC lấy E sao cho C là trung điểm AE. Chứng minh tam giác ABE cân tại A.",
           "Gợi ý: D là trọng tâm của tam giác ABE; tam giác này có đường phân giác AD đồng thời là đường trung tuyến.",
           ["ABE cân tại A"],
           "D là trọng tâm tam giác ABE, AD vừa là phân giác vừa là trung tuyến nên ABE cân tại A."),
        nc("Bài 9.40 (BTCC IX): Một sợi dây thép dài 1,2 m. Cần đánh dấu trên sợi dây hai điểm để khi uốn gập lại tại hai điểm đó sẽ tạo thành tam giác cân có một cạnh dài 30 cm. Hãy mô tả các cách đánh dấu hai điểm.",
           "Xét các trường hợp: cạnh đáy 30 cm, hoặc cạnh bên 30 cm; dùng bất đẳng thức tam giác.",
           ["Hai trường hợp"],
           "Nếu một cạnh bên dài 30 cm thì đáy 60 cm, nhưng 30 + 30 = 60 không lớn hơn 60 nên không tạo thành tam giác. Vậy cách duy nhất: đáy 30 cm, hai cạnh bên mỗi cạnh 45 cm (45 + 45 + 30 = 120 cm). Đánh dấu hai điểm cách đầu dây 45 cm và 90 cm."),
    ],
)

CHUONG_9 = {
    "Chương IX: Quan hệ giữa các yếu tố trong một tam giác": {
        "Bài 31: Quan hệ giữa góc và cạnh đối diện trong một tam giác": B31,
        "Bài 32: Quan hệ giữa đường vuông góc và đường xiên": B32,
        "Bài 33: Quan hệ giữa ba cạnh của một tam giác": B33,
        "Bài 34: Sự đồng quy của ba đường trung tuyến, ba đường phân giác trong một tam giác": B34,
        "Bài 35: Sự đồng quy của ba đường trung trực, ba đường cao trong một tam giác": B35,
    }
}

# ============================================================
# FILE toan_c10.py
# ============================================================
# ============================================================
# BÀI 36: HÌNH HỘP CHỮ NHẬT VÀ HÌNH LẬP PHƯƠNG
# ============================================================
B36 = bai(
    ly_thuyet="""📌 1. MỘT SỐ YẾU TỐ CƠ BẢN
- Hình hộp chữ nhật ABCD.A'B'C'D' có 6 mặt là các hình chữ nhật, 8 đỉnh, 12 cạnh và 4 đường chéo.
- Các cạnh bên song song và bằng nhau.
- Hình lập phương là hình hộp chữ nhật có 6 mặt là các hình vuông.

📌 2. DIỆN TÍCH XUNG QUANH VÀ THỂ TÍCH
- Hình hộp chữ nhật (a, b, c): diện tích xung quanh S_xq = 2(a + b)c; diện tích toàn phần S_tp = 2(ab + bc + ca); thể tích V = abc.
- Hình lập phương cạnh a: S_xq = 4a²; S_tp = 6a²; V = a³.
- Chú ý: khi tính diện tích và thể tích, các kích thước phải cùng đơn vị độ dài.""",
    vi_du="""Ví dụ 1: Chiếc khay nhựa dạng hình hộp chữ nhật có kích thước 27 cm × 20 cm × 10 cm.
a) Diện tích xung quanh: 2 · (27 + 20) · 10 = 940 (cm²).
b) Diện tích đáy: 27 · 20 = 540 (cm²). Diện tích nhựa: 940 + 540 = 1 480 (cm²).

Luyện tập 1: Bác Tú sơn xung quanh bốn mặt ngoài của thành bể nước dài 3 m, rộng 2 m, cao 1,5 m, giá 20 000 đồng/m². Chi phí: S_xq = 2(3 + 2) · 1,5 = 15 (m²); 15 · 20 000 = 300 000 đồng.

Ví dụ 2: Thể tích hộp sữa 10 · 10 · 15 = 1 500 (cm³).

Luyện tập 2: Hình lập phương cạnh a cm có diện tích xung quanh 100 cm²: 4a² = 100 nên a = 5, V = 125 cm³.

Vận dụng 2: Thùng giữ nhiệt có lòng trong 50 cm × 30 cm × 30 cm, dung tích = 45 000 cm³ = 45 lít.""",
    cau_hoi=[
        q("Hình hộp chữ nhật có bao nhiêu đỉnh?", ["6", "8", "10", "12"], 1,
          "Hình hộp chữ nhật có 8 đỉnh."),
        q("Hình hộp chữ nhật có bao nhiêu cạnh?", ["8", "10", "12", "16"], 2,
          "Có 12 cạnh."),
        q("Hình hộp chữ nhật có bao nhiêu mặt?", ["4", "6", "8", "12"], 1,
          "Có 6 mặt là hình chữ nhật."),
        q("Hình hộp chữ nhật có bao nhiêu đường chéo?", ["2", "4", "6", "8"], 1,
          "Có 4 đường chéo."),
        q("Hình lập phương có 6 mặt là các hình gì?", ["Hình vuông", "Hình chữ nhật", "Hình tròn", "Tam giác"], 0,
          "Hình lập phương là hình hộp có 6 mặt vuông."),
        q("Các cạnh bên của hình hộp chữ nhật có tính chất gì?",
          ["Song song và bằng nhau", "Vuông góc với nhau", "Bằng nhau nhưng không song song", "Chéo nhau"], 0,
          "Đó là nhận xét trong sách."),
        q("Diện tích xung quanh của hình hộp chữ nhật kích thước a, b, c là:",
          ["2(a + b)c", "2(ab + bc + ca)", "abc", "4a²"], 0,
          "S_xq = 2(a + b)c."),
        q("Diện tích toàn phần của hình hộp chữ nhật kích thước a, b, c là:",
          ["2(a + b)c", "2(ab + bc + ca)", "abc", "6a²"], 1,
          "S_tp = S_xq + 2·S_đáy = 2(ab + bc + ca)."),
        q("Diện tích xung quanh của hình lập phương cạnh a là:",
          ["4a²", "6a²", "a³", "2a²"], 0,
          "Có 4 mặt bên, mỗi mặt có diện tích a²."),
        q("Thể tích hình hộp chữ nhật kích thước a, b, c là:",
          ["abc", "2(a + b)c", "a³ + b³", "ab + bc"], 0,
          "V = abc."),
        q("Thể tích hình lập phương cạnh a là:",
          ["a³", "4a²", "a²", "3a"], 0,
          "V = a³."),
        q("Khay nhựa dài 27 cm, rộng 20 cm, cao 10 cm (Ví dụ 1). Diện tích xung quanh là:",
          ["940 cm²", "540 cm²", "1 480 cm²", "1 080 cm²"], 0,
          "2 · (27 + 20) · 10 = 940 cm²."),
    ] + [
        q("Khay nhựa Ví dụ 1 cần bao nhiêu diện tích nhựa (kể cả đáy)?",
          ["940 cm²", "540 cm²", "1 480 cm²", "2 000 cm²"], 2,
          "940 + 540 = 1 480 cm²."),
        q("Hộp sữa dài 10 cm, rộng 10 cm, cao 15 cm có thể tích là:",
          ["1 500 cm³", "1 000 cm³", "2 000 cm³", "150 cm³"], 0,
          "V = 10 · 10 · 15 = 1 500 cm³."),
        q("Hình lập phương có diện tích xung quanh 100 cm² thì cạnh bằng:",
          ["5 cm", "10 cm", "25 cm", "2,5 cm"], 0,
          "4a² = 100 nên a = 5 cm."),
        q("Hình lập phương có diện tích xung quanh 100 cm² thì thể tích là:",
          ["125 cm³", "100 cm³", "25 cm³", "500 cm³"], 0,
          "a = 5, V = 125 cm³."),
        q("Thùng giữ nhiệt có lòng trong 50 cm × 30 cm × 30 cm. Dung tích là:",
          ["45 lít", "30 lít", "50 lít", "15 lít"], 0,
          "V = 45 000 cm³ = 45 dm³ = 45 lít."),
        q("Xe đông lạnh có lòng thùng 5,6 m × 2 m × 2 m. Thể tích là:",
          ["22,4 m³", "11,2 m³", "5,6 m³", "44,8 m³"], 0,
          "V = 5,6 · 2 · 2 = 22,4 m³."),
        q("Hình lập phương cạnh 4 cm có thể tích:",
          ["64 cm³", "16 cm³", "48 cm³", "12 cm³"], 0,
          "V = 4³ = 64 cm³."),
        q("Hình hộp chữ nhật 2 cm × 3 cm × 4 cm có thể tích:",
          ["24 cm³", "9 cm³", "12 cm³", "36 cm³"], 0,
          "V = 2 · 3 · 4 = 24 cm³."),
        q("Hình hộp chữ nhật 3 cm × 4 cm × 5 cm có diện tích toàn phần:",
          ["94 cm²", "60 cm²", "47 cm²", "120 cm²"], 0,
          "S_tp = 2(12 + 20 + 15) = 94 cm²."),
        q("Hình lập phương cạnh 3 cm có diện tích toàn phần:",
          ["54 cm²", "36 cm²", "27 cm²", "18 cm²"], 0,
          "S_tp = 6 · 9 = 54 cm²."),
        q("18 viên đá hình lập phương cạnh 2 cm, tổng thể tích là:",
          ["144 cm³", "36 cm³", "72 cm³", "288 cm³"], 0,
          "Mỗi viên 8 cm³, 18 · 8 = 144 cm³."),
        q("Hộp sữa tươi 1 lít, cao 20 cm, dài 10 cm thì rộng là:",
          ["5 cm", "4 cm", "6 cm", "10 cm"], 0,
          "1000 = 10 · rộng · 20 nên rộng = 5 cm."),
        q("Bể nước dài 2 m, sau khi đổ 120 thùng (mỗi thùng 20 lít) thì cao 0,8 m. Chiều rộng bể là:",
          ["1,5 m", "1 m", "2 m", "0,8 m"], 0,
          "2400 lít = 2,4 m³; rộng = 2,4 : (2 · 0,8) = 1,5 m."),
        q("Hộp khẩu trang 20 cm × 10 cm × 8 cm có thể tích:",
          ["1 600 cm³", "800 cm³", "2 000 cm³", "880 cm³"], 0,
          "V = 20 · 10 · 8 = 1 600 cm³."),
        q("Hộp 50 cm × 40 cm × 30 cm có thể tích:",
          ["60 dm³", "600 dm³", "6 dm³", "120 dm³"], 0,
          "V = 60 000 cm³ = 60 dm³."),
        q("Hộp hình hộp chữ nhật 20 cm × 14 cm × 15 cm có thể tích:",
          ["4 200 cm³", "2 100 cm³", "5 040 cm³", "4 000 cm³"], 0,
          "V = 20 · 14 · 15 = 4 200 cm³."),
        q("Đường chéo của hình hộp chữ nhật là đoạn nối:",
          ["Hai đỉnh không cùng nằm trên một mặt", "Hai đỉnh kề nhau", "Hai trung điểm", "Hai cạnh đối"], 0,
          "Đường chéo nối hai đỉnh không thuộc cùng một mặt."),
        q("Mỗi đỉnh của hình hộp chữ nhật là đầu mút của bao nhiêu cạnh?",
          ["3", "4", "2", "6"], 0,
          "Có 3 cạnh xuất phát từ mỗi đỉnh."),
        q("Khi tính diện tích và thể tích một hình, các kích thước phải:",
          ["Cùng đơn vị độ dài", "Khác đơn vị", "Đơn vị bất kì", "Là đơn vị diện tích"], 0,
          "Đó là chú ý trong sách."),
        q("Hình hộp chữ nhật có ba kích thước 2, 3, 6 (cm). Thể tích là:",
          ["36 cm³", "11 cm³", "18 cm³", "72 cm³"], 0,
          "V = 2 · 3 · 6 = 36 cm³."),
        q("Hình hộp chữ nhật có kích thước 2 cm, 3 cm, 6 cm. Diện tích toàn phần là:",
          ["72 cm²", "36 cm²", "22 cm²", "11 cm²"], 0,
          "S_tp = 2(6 + 12 + 18) = 72 cm²."),
        q("Hình lập phương có thể tích 27 cm³ thì cạnh bằng:",
          ["3 cm", "9 cm", "27 cm", "4 cm"], 0,
          "a³ = 27 nên a = 3 cm."),
        q("Hình lập phương cạnh 2 cm có diện tích xung quanh:",
          ["16 cm²", "8 cm²", "24 cm²", "4 cm²"], 0,
          "S_xq = 4 · 2² = 16 cm²."),
        q("Bể nước 3 m × 2 m × 1,5 m, sơn bốn mặt xung quanh có diện tích:",
          ["15 m²", "9 m²", "6 m²", "18 m²"], 0,
          "S_xq = 2(3 + 2) · 1,5 = 15 m²."),
    ],
    bt_co_ban=[
        bt("Luyện tập 1: Bể nước 3 m × 2 m × 1,5 m, sơn bốn mặt xung quanh giá 20 000 đồng/m². Số tiền phải trả là bao nhiêu đồng?",
           ["300000", "300 000"], "15 m² · 20 000 = 300 000 đồng."),
        bt("Bài 10.4: Lòng thùng xe đông lạnh dài 5,6 m, rộng 2 m, cao 2 m. Thể tích là bao nhiêu m³? (gõ số, ví dụ 22.4)",
           ["22.4", "22,4"], "V = 5,6 · 2 · 2 = 22,4 m³."),
        bt("Bài 10.5a: Hộp sữa tươi 1 lít, cao 20 cm, dài 10 cm. Chiều rộng là bao nhiêu cm?",
           ["5", "5 cm"], "1000 : (10 · 20) = 5 cm."),
        bt("Bài 10.5b: Diện tích vật liệu làm vỏ hộp sữa (cm²) bằng bao nhiêu? (bỏ qua mép hộp)",
           ["700"], "S_tp = 2(10·5 + 10·20 + 5·20) = 700 cm²."),
        bt("Bài 10.6a: Bể nước dài 2 m; đổ 120 thùng (20 lít/thùng) thì cao 0,8 m. Chiều rộng bể (m) là bao nhiêu? (gõ số thập phân, ví dụ 1.5)",
           ["1.5", "1,5"], "Thể tích nước 2,4 m³; rộng = 2,4 : (2 · 0,8) = 1,5 m."),
        bt("Bài 10.6b: Đổ thêm 60 thùng nữa thì đầy bể. Chiều cao bể (m) là bao nhiêu? (gõ số thập phân, ví dụ 1.2)",
           ["1.2", "1,2"], "Thêm 1,2 m³, chiều cao tăng 1,2 : (2 · 1,5) = 0,4 m; tổng 0,8 + 0,4 = 1,2 m."),
        bt("Bài 10.8a: Hộp đựng đồ có kích thước 50 cm × 40 cm × 30 cm. Thể tích là bao nhiêu dm³?",
           ["60", "60 dm³"], "V = 60 000 cm³ = 60 dm³."),
        bt("Bài 10.9: 18 viên đá hình lập phương cạnh 2 cm. Tổng thể tích là bao nhiêu cm³?",
           ["144", "144 cm³"], "18 · 8 = 144 cm³."),
        bt("Ví dụ 2: Hộp sữa 10 cm × 10 cm × 15 cm. Thể tích là bao nhiêu cm³?",
           ["1500", "1 500", "1500 cm³"], "V = 1 500 cm³."),
        bt("Luyện tập 2: Hình lập phương cạnh a cm có diện tích xung quanh 100 cm². Thể tích là bao nhiêu cm³?",
           ["125", "125 cm³"], "a = 5 cm, V = 125 cm³."),
    ],
    bt_nang_cao=[
        nc("Bài 10.2: Gọi tên các đỉnh, cạnh, đường chéo và mặt của hình hộp chữ nhật ABCD.EFGH (Hình 10.12).",
           "Hình hộp có 8 đỉnh, 12 cạnh, 4 đường chéo, 6 mặt.",
           ["8 đỉnh, 12 cạnh, 4 đường chéo, 6 mặt"],
           "Đối chiếu Hình 10.12 để gọi tên đầy đủ các đỉnh, cạnh, đường chéo và mặt."),
        nc("Bài 10.8b: Hộp đựng đồ đa năng có kích thước 50 cm × 40 cm × 30 cm, bên ngoài phủ vải (kể cả nắp). Diện tích vải phủ bề mặt ngoài là bao nhiêu cm²?",
           "Tính diện tích toàn phần của hình hộp chữ nhật.",
           ["9400"],
           "S_tp = 2(50·40 + 50·30 + 40·30) = 2(2000 + 1500 + 1200) = 9 400 cm²."),
        nc("Bài 10.10: Thùng hình lập phương cạnh 7 dm chứa nước sâu 4 dm. Thả 25 viên gạch hình hộp chữ nhật 2 dm × 1 dm × 0,5 dm (ngập trong nước). Hỏi nước dâng lên cách miệng thùng bao nhiêu dm?",
           "Thể tích một viên gạch = 2 · 1 · 0,5 = 1 dm³; mực nước dâng thêm = 25 : (7 · 7).",
           ["2,49", "2.49", "≈ 2,49 dm"],
           "Thể tích gạch = 25 dm³. Mực nước dâng thêm 25 : 49 dm. Mực nước mới 4 + 25/49 ≈ 4,51 dm; cách miệng thùng 7 − 4,51 ≈ 2,49 dm."),
        nc("Bài 10.16: Hộp khẩu trang bằng bìa cứng dạng hình hộp chữ nhật 20 cm × 10 cm × 8 cm. (a) Tính thể tích. (b) Tính diện tích bìa cứng (bỏ qua mép dán).",
           "V = abc; S_tp = 2(ab + bc + ca).",
           ["1600; 880"],
           "(a) V = 1 600 cm³. (b) S_tp = 2(200 + 160 + 80) = 880 cm²."),
        nc("Bài 10.20 (BTCC X): Hộp hình hộp chữ nhật bằng bìa, dài 20 cm, rộng 14 cm, cao 15 cm. (a) Tính thể tích. (b) Tính diện tích bìa dùng để làm hộp.",
           "V = abc; S_tp = 2(ab + bc + ca).",
           ["4200; 1580"],
           "(a) V = 4 200 cm³. (b) S_tp = 2(280 + 300 + 210) = 1 580 cm²."),
        nc("Bài 10.22 (BTCC X): Khối gạch hình lập phương cạnh 20 cm. Tính diện tích xung quanh và diện tích toàn phần của khối gạch.",
           "S_xq = 4a², S_tp = 6a².",
           ["1600; 2400"],
           "S_xq = 4 · 400 = 1 600 cm²; S_tp = 6 · 400 = 2 400 cm²."),
        nc("Bài 10.23 (BTCC X): Căn phòng dạng hình hộp chữ nhật dài 5 m, rộng 4 m, cao 3 m. Cần lăn sơn tường và trần; tổng diện tích các cửa là 5,8 m². Tính diện tích cần lăn sơn.",
           "Diện tích cần sơn = S_xq + S_trần − diện tích cửa.",
           ["68,2"],
           "S_xq = 2(5 + 4)·3 = 54 m²; trần 20 m²; cần sơn 54 + 20 − 5,8 = 68,2 m²."),
        nc("Bài 10.24 (BTCC X): Bể cá hình hộp chữ nhật bằng kính (không nắp) dài 80 cm, rộng 50 cm, cao 45 cm. Mực nước ban đầu 35 cm. (a) Tính diện tích kính. (b) Thả hòn đá chìm hoàn toàn, mực nước dâng lên 37,5 cm. Tính thể tích hòn đá.",
           "Diện tích kính = 2(80·45 + 50·45) + 80·50; thể tích hòn đá = đáy · độ dâng nước.",
           ["15700; 10000"],
           "(a) S = 2(3600 + 2250) + 4000 = 15 700 cm². (b) V = 80 · 50 · 2,5 = 10 000 cm³."),
    ],
)

# ============================================================
# BÀI 37: HÌNH LĂNG TRỤ ĐỨNG TAM GIÁC VÀ HÌNH LĂNG TRỤ ĐỨNG TỨ GIÁC
# ============================================================
B37 = bai(
    ly_thuyet="""📌 1. HÌNH LĂNG TRỤ ĐỨNG
- Hình lăng trụ đứng tam giác có hai mặt đáy là hai tam giác song song và bằng nhau; các mặt bên là hình chữ nhật; các cạnh bên song song và bằng nhau.
- Hình lăng trụ đứng tứ giác có hai đáy là hai tứ giác song song và bằng nhau; các mặt bên là hình chữ nhật.
- Độ dài một cạnh bên gọi là chiều cao của lăng trụ đứng.
- Ví dụ: hình lăng trụ đứng tam giác ABC.A'B'C' có các đỉnh A, B, C, A', B', C'; các cạnh đáy AB, BC, CA, A'B', B'C', C'A'; các cạnh bên AA', BB', CC'; các mặt đáy ABC và A'B'C'; các mặt bên ABB'A', ACC'A', BCC'B'.

📌 2. DIỆN TÍCH XUNG QUANH VÀ THỂ TÍCH
- Diện tích xung quanh: S_xq = C · h, với C là chu vi một đáy và h là chiều cao.
- Thể tích: V = S_đáy · h, với S_đáy là diện tích một đáy và h là chiều cao.""",
    vi_du="""Ví dụ 1: Hình lăng trụ đứng tam giác ABC.A'B'C' có các đỉnh A, B, C, A', B', C'; mặt đáy ABC và A'B'C'; mặt bên ABB'A', ACC'A', BCC'B' là các hình chữ nhật.

Ví dụ 2: Quyển lịch để bàn có giá đỡ là hình lăng trụ đứng tam giác với các cạnh đáy 20 cm, 20 cm, 7 cm và chiều cao 25 cm. S_xq = C · h = (20 + 20 + 7) · 25 = 1 175 (cm²).

Luyện tập 1 và Vận dụng: Tính diện tích vải làm lều và khúc gỗ theo kích thước trong hình (tham khảo sách trang 97).

Ví dụ 3: Lăng kính thủy tinh là hình lăng trụ đứng tam giác với đáy tam giác có đáy 10 cm, chiều cao 8,7 cm, chiều cao lăng trụ 20 cm. S_đáy = ½ · 10 · 8,7 = 43,5 cm²; V = 43,5 · 20 = 870 cm³.

Luyện tập 2: Khay đựng linh kiện có đáy là hình thang vuông (hai cạnh đáy 30 cm và 40 cm) — tham khảo Hình 10.29.

Thử thách nhỏ: Tính thể tích bể bơi ghép bởi một hình hộp chữ nhật và một hình lăng trụ đứng tam giác (Hình 10.30).""",
    cau_hoi=[
        q("Hình lăng trụ đứng tam giác có bao nhiêu đỉnh?", ["4", "5", "6", "8"], 2,
          "Hai đáy tam giác, mỗi đáy 3 đỉnh: tổng 6 đỉnh."),
        q("Hình lăng trụ đứng tam giác có bao nhiêu cạnh?", ["6", "8", "9", "12"], 2,
          "3 cạnh đáy trên, 3 cạnh đáy dưới và 3 cạnh bên: tổng 9."),
        q("Hình lăng trụ đứng tam giác có bao nhiêu mặt bên?", ["2", "3", "4", "5"], 1,
          "Có 3 mặt bên là các hình chữ nhật."),
        q("Mặt đáy của hình lăng trụ đứng tam giác là:", ["Tam giác", "Hình vuông", "Hình chữ nhật", "Tứ giác"], 0,
          "Hai mặt đáy là hai tam giác bằng nhau."),
        q("Mặt bên của hình lăng trụ đứng là:", ["Hình chữ nhật", "Tam giác", "Hình thang", "Hình tròn"], 0,
          "Các mặt bên là hình chữ nhật."),
        q("Các cạnh bên của hình lăng trụ đứng có tính chất gì?",
          ["Song song và bằng nhau", "Vuông góc với nhau", "Chéo nhau", "Bằng cạnh đáy"], 0,
          "Đó là nhận xét trong sách."),
        q("Độ dài một cạnh bên của lăng trụ đứng gọi là:", ["Chiều cao lăng trụ", "Cạnh đáy", "Đường cao đáy", "Đường chéo"], 0,
          "Độ dài cạnh bên là chiều cao của lăng trụ đứng."),
        q("Hình lăng trụ đứng tứ giác có bao nhiêu đỉnh?", ["6", "8", "10", "12"], 1,
          "Hai đáy tứ giác, mỗi đáy 4 đỉnh: tổng 8."),
        q("Hình lăng trụ đứng tứ giác có bao nhiêu mặt bên?", ["3", "4", "5", "6"], 1,
          "Số mặt bên bằng số cạnh đáy = 4."),
        q("Hình hộp chữ nhật là lăng trụ đứng tứ giác có đáy là:", ["Hình chữ nhật", "Hình thang", "Tam giác", "Hình bình hành"], 0,
          "Hình hộp chữ nhật có đáy là hình chữ nhật."),
        q("Diện tích xung quanh của hình lăng trụ đứng được tính theo công thức:",
          ["S_xq = C · h", "S_xq = C · h / 2", "S_xq = S_đáy · h", "S_xq = 2 · S_đáy"], 0,
          "C là chu vi đáy, h là chiều cao."),
        q("Thể tích hình lăng trụ đứng được tính theo công thức:",
          ["V = S_đáy · h", "V = C · h", "V = 2 · S_đáy", "V = S_xq · h"], 0,
          "Thể tích bằng diện tích đáy nhân chiều cao."),
        q("Ví dụ 2: quyển lịch có đáy 20 cm, 20 cm, 7 cm và cao 25 cm. Diện tích xung quanh là:",
          ["1 175 cm²", "1 200 cm²", "1 100 cm²", "1 000 cm²"], 0,
          "(20 + 20 + 7) · 25 = 1 175 cm²."),
        q("Ví dụ 3: lăng kính có đáy tam giác đáy 10 cm, cao 8,7 cm. Diện tích đáy là:",
          ["43,5 cm²", "87 cm²", "17,4 cm²", "50 cm²"], 0,
          "S = ½ · 10 · 8,7 = 43,5 cm²."),
        q("Ví dụ 3: lăng kính cao 20 cm. Thể tích thủy tinh là:",
          ["870 cm³", "435 cm³", "1 740 cm³", "174 cm³"], 0,
          "V = 43,5 · 20 = 870 cm³."),
        q("Tam giác vuông có hai cạnh góc vuông 6 cm và 8 cm có diện tích:",
          ["24 cm²", "48 cm²", "14 cm²", "10 cm²"], 0,
          "S = ½ · 6 · 8 = 24 cm²."),
        q("Bài 10.13: lăng trụ đứng có đáy tam giác 6 cm, 8 cm, 10 cm, chiều cao 15 cm. Thể tích là:",
          ["360 cm³", "720 cm³", "180 cm³", "240 cm³"], 0,
          "S_đáy = 24 cm², V = 24 · 15 = 360 cm³."),
        q("Bài 10.13: lăng trụ đứng nói trên có diện tích xung quanh là:",
          ["360 cm²", "240 cm²", "480 cm²", "720 cm²"], 0,
          "S_xq = (6 + 8 + 10) · 15 = 360 cm²."),
        q("Bài 10.19: mương đào có mặt cắt hình thang (đáy trên 1,8 m, đáy dưới 1,2 m, sâu 1,5 m) dài 20 m. Thể tích đất đào là:",
          ["45 m³", "36 m³", "18 m³", "30 m³"], 0,
          "S = (1,8 + 1,2)/2 · 1,5 = 2,25 m²; V = 2,25 · 20 = 45 m³."),
        q("Bài 10.21: lăng trụ đứng có đáy tam giác vuông cạnh 5, 12 (huyền 13) và chiều dài 20. Thể tích là:",
          ["600", "300", "660", "120"], 0,
          "S_đáy = 30, V = 30 · 20 = 600."),
        q("Bài 10.21: hình hộp chữ nhật 9 × 4 × 9 có thể tích:",
          ["324", "234", "306", "81"], 0,
          "V = 9 · 4 · 9 = 324."),
        q("Ví dụ 2 (LTC): khối gỗ là lăng trụ đứng tam giác có đáy tam giác vuông với hai cạnh góc vuông 60 cm, 90 cm và chiều cao 70 cm. Thể tích 189 000 cm³ là kết quả của:",
          ["½ · 60 · 90 · 70", "60 · 90 · 70", "½ · 60 · 90", "60 · 70"], 0,
          "V = S_đáy · h = ½ · 60 · 90 · 70 = 189 000 cm³."),
        q("Đổi 189 000 cm³ sang m³ được:",
          ["0,189 m³", "1,89 m³", "18,9 m³", "0,0189 m³"], 0,
          "1 m³ = 1 000 000 cm³ nên 189 000 cm³ = 0,189 m³."),
        q("Ví dụ 3 (LTC): lều có diện tích đáy 1,92 m² và chiều dài 5 m. Thể tích khoảng không bên trong là:",
          ["9,6 m³", "1,92 m³", "5 m³", "19,2 m³"], 0,
          "V = 1,92 · 5 = 9,6 m³."),
        q("Ví dụ 3 (LTC): diện tích vải bạt cần dùng là:",
          ["23,84 m²", "39,84 m²", "16 m²", "36 m²"], 0,
          "S_tp = 36 + 2 · 1,92 = 39,84; trừ mặt bên 5 · 3,2 = 16 → 23,84 m²."),
        q("Ví dụ 3 (LTC): diện tích đáy lều (tam giác có đáy 3,2 m, cao 1,2 m) là:",
          ["1,92 m²", "3,84 m²", "2,4 m²", "1,2 m²"], 0,
          "S = (3,2 · 1,2) : 2 = 1,92 m²."),
        q("Trong hình lăng trụ đứng tam giác, hai mặt đáy:",
          ["Là hai tam giác bằng nhau và song song", "Là hai hình vuông", "Là hai đường thẳng", "Là hai đường tròn"], 0,
          "Hai đáy là hai tam giác bằng nhau, song song."),
        q("Lăng trụ đứng tam giác có đáy là tam giác đều cạnh 2 cm, chiều cao 3 cm. Thể tích là:",
          ["3√3 cm³", "6 cm³", "2√3 cm³", "9 cm³"], 0,
          "S_đáy = √3, V = 3√3 cm³."),
        q("Lăng trụ đứng có đáy tam giác 3 cm, 4 cm, 5 cm và chiều cao 10 cm. Diện tích xung quanh là:",
          ["120 cm²", "60 cm²", "12 cm²", "130 cm²"], 0,
          "C = 12, S_xq = 12 · 10 = 120 cm²."),
        q("Lăng trụ đứng có đáy tam giác vuông 3, 4, 5 cm và chiều cao 10 cm. Thể tích là:",
          ["60 cm³", "12 cm³", "120 cm³", "30 cm³"], 0,
          "S_đáy = 6, V = 6 · 10 = 60 cm³."),
        q("1 dm³ bằng:", ["1 lít", "10 lít", "100 lít", "0,1 lít"], 0,
          "1 dm³ = 1 lít."),
        q("Trong hình lăng trụ đứng, cạnh bên vuông góc với:",
          ["Hai mặt đáy", "Các cạnh đáy", "Mặt bên", "Không vuông góc với đâu"], 0,
          "Cạnh bên vuông góc với hai mặt đáy của lăng trụ đứng."),
    ],
    bt_co_ban=[
        bt("Bài 10.13: Thể tích hình lăng trụ đứng có đáy là tam giác 6 cm, 8 cm, 10 cm và chiều cao 15 cm là bao nhiêu cm³?",
           ["360", "360 cm³"], "V = 24 · 15 = 360 cm³."),
        bt("Bài 10.13: Diện tích xung quanh của hình lăng trụ đó là bao nhiêu cm²?",
           ["360", "360 cm²"], "S_xq = (6 + 8 + 10) · 15 = 360 cm²."),
        bt("Bài 10.19: Thể tích đất đào của mương (m³) là bao nhiêu?",
           ["45", "45 m³"], "2,25 · 20 = 45 m³."),
        bt("Ví dụ 3: Thể tích thủy tinh làm lăng kính (cm³) là bao nhiêu?",
           ["870", "870 cm³"], "43,5 · 20 = 870 cm³."),
        bt("Ví dụ 2: Diện tích bìa làm giá đỡ quyển lịch (cm²) là bao nhiêu?",
           ["1175", "1 175", "1175 cm²"], "S_xq = 47 · 25 = 1 175 cm²."),
        bt("Bài 10.21: Thể tích của hình lăng trụ đứng có đáy tam giác vuông 5 cm, 12 cm, cạnh huyền 13 cm và chiều dài 20 cm là bao nhiêu cm³?",
           ["600", "600 cm³"], "S_đáy = 30; V = 30 · 20 = 600 cm³."),
    ],
    bt_nang_cao=[
        nc("Bài 10.11: Quan sát Hình 10.31 và gọi tên các mặt đáy, mặt bên, cạnh đáy, cạnh bên của hình lăng trụ đứng tam giác MNP.A'B'C' (dựa vào hình vẽ trong sách).",
           "Mặt đáy là hai tam giác; mặt bên là các hình chữ nhật; cạnh bên song song và bằng nhau.",
           ["Theo hình vẽ"],
           "Đối chiếu với Hình 10.31 để gọi tên các yếu tố; các mặt bên là hình chữ nhật."),
        nc("Bài 10.7 (LTC IX/X tương tự): Kể tên các đỉnh, cạnh và đường chéo của hình lập phương MNPQ.EFGH (Hình 10.16).",
           "Hình lập phương có 8 đỉnh, 12 cạnh, 4 đường chéo.",
           ["8 đỉnh, 12 cạnh, 4 đường chéo"],
           "Đối chiếu Hình 10.16 để gọi tên đầy đủ."),
    ],
)

CHUONG_10 = {
    "Chương X: Một số hình khối trong thực tiễn": {
        "Bài 36: Hình hộp chữ nhật và hình lập phương": B36,
        "Bài 37: Hình lăng trụ đứng tam giác và hình lăng trụ đứng tứ giác": B37,
    }
}

# ============================================================
# TỔNG HỢP
# ============================================================
TOAN = {
    "Lớp 7": {
        **CHUONG_1,
        **CHUONG_2,
        **CHUONG_3,
        **CHUONG_4,
        **CHUONG_5,
        **CHUONG_6,
        **CHUONG_7,
        **CHUONG_8,
        **CHUONG_9,
        **CHUONG_10,
    }
}
