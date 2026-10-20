# -*- coding: utf-8 -*-
""" NGÂN HÀNG DỮ LIỆU MÔN TOÁN 
Tập trung: TOÁN LỚP 7 (Kết Nối Tri Thức)
"""

TOAN = {}

T7 = {}

C1_T7 = {
    "Bài 1: Tập hợp ℚ các số hữu tỉ và Các phép toán": {
        "ly_thuyet": """📌 1. TẬP HỢP SỐ HỮU TỈ (ℚ):
- Số hữu tỉ là số viết được dưới dạng phân số a/b, trong đó a, b là các số nguyên và b ≠ 0.
- Kí hiệu tập hợp số hữu tỉ là ℚ. Mọi số nguyên, số thập phân hữu hạn, số thập phân vô hạn tuần hoàn, hỗn số đều là số hữu tỉ.
- Mối quan hệ giữa các tập hợp số: ℕ ⊂ ℤ ⊂ ℚ.

📌 2. BIỂU DIỄN SỐ HỮU TỈ TRÊN TRỤC SỐ:
- Mỗi số hữu tỉ được biểu diễn bởi một điểm trên trục số. Số hữu tỉ dương nằm bên phải điểm 0, số hữu tỉ âm nằm bên trái điểm 0.
- Hai số đối nhau có điểm biểu diễn cách đều điểm 0 và nằm ở hai phía của điểm 0.

📌 3. CỘNG, TRỪ SỐ HỮU TỈ:
- Để cộng, trừ hai số hữu tỉ, ta viết chúng dưới dạng phân số có mẫu dương rồi áp dụng quy tắc cộng, trừ phân số.
- Tính chất: Giao hoán, Kết hợp, Cộng với số 0, Cộng với số đối.

📌 4. NHÂN, CHIA SỐ HỮU TỈ:
- Nhân: a/b . c/d = (a.c) / (b.d)
- Chia: a/b : c/d = a/b . d/c = (a.d) / (b.c) (với c/d ≠ 0).

📌 5. THỨ TỰ THỰC HIỆN PHÉP TÍNH:
- Nếu không có ngoặc: Lũy thừa → Nhân, chia → Cộng, trừ.
- Nếu có ngoặc: Trong ngoặc làm trước, ngoài ngoặc làm sau; ( ) → [ ] → { }.""",
        
        "vi_du": """💡 VÍ DỤ 1: So sánh hai số hữu tỉ
Đề bài: So sánh hai số hữu tỉ x = -2/3 và y = -4/5.
- Phân tích: Để so sánh, ta quy đồng mẫu số (chọn mẫu số chung dương).
- Giải:
  Mẫu chung của 3 và 5 là 15.
  x = -2/3 = -10/15
  y = -4/5 = -12/15
  Vì -10 > -12 nên -10/15 > -12/15. Suy ra: -2/3 > -4/5 (hay x > y).

💡 VÍ DỤ 2: Thực hiện phép tính (Hợp lý nếu có thể)
Đề bài: Tính A = 5/7 . (-3/11) + 5/7 . (-8/11) + 2/7
- Phân tích: Quan sát thấy 5/7 là thừa số chung, ta sử dụng tính chất phân phối của phép nhân đối với phép cộng để tính nhanh.
- Giải:
  A = 5/7 . [(-3/11) + (-8/11)] + 2/7
  A = 5/7 . (-11/11) + 2/7
  A = 5/7 . (-1) + 2/7
  A = -5/7 + 2/7 = -3/7.

💡 VÍ DỤ 3: Bài toán tìm x
Đề bài: Tìm x biết: 3/4 - x = 1/2 : (-2/5)
- Phân tích: Thực hiện phép tính ở vế phải trước, sau đó tìm x đóng vai trò là số trừ (Số trừ = Số bị trừ - Hiệu).
- Giải:
  Vế phải: 1/2 : (-2/5) = 1/2 . (-5/2) = -5/4
  Ta có: 3/4 - x = -5/4
  ⇒ x = 3/4 - (-5/4)
  ⇒ x = 3/4 + 5/4 = 8/4 = 2. Vậy x = 2.""",

        "cau_hoi": [
            {"nd": "Tập hợp các số hữu tỉ được kí hiệu là gì?","da": ["ℕ","ℤ","ℚ","ℝ"],"d": 2,"gt": "ℚ là kí hiệu của tập hợp số hữu tỉ."},
            {"nd": "Số nào sau đây là số hữu tỉ âm?","da": ["3/4","-0,25","0","(-2)/(-5)"],"d": 1,"gt": "-0,25 = -1/4 < 0. Chú ý (-2)/(-5) = 2/5 > 0."},
            {"nd": "Khẳng định nào sau đây ĐÚNG?","da": ["Mọi số nguyên đều là số hữu tỉ","Mọi số hữu tỉ đều là số nguyên","Số 0 không là số hữu tỉ","Tập ℚ ⊂ ℤ"],"d": 0,"gt": "Mọi số nguyên a đều viết được dưới dạng a/1 nên nó là số hữu tỉ."},
            {"nd": "Số đối của số hữu tỉ -7/9 là?","da": ["9/7","-9/7","7/9","-7/9"],"d": 2,"gt": "Số đối của a là -a, nên số đối của -7/9 là 7/9."},
            {"nd": "Nghịch đảo của số -3/5 là?","da": ["3/5","-5/3","5/3","-3/5"],"d": 1,"gt": "Nghịch đảo của a/b là b/a, do đó nghịch đảo của -3/5 là -5/3."},
            {"nd": "Điểm biểu diễn số hữu tỉ -1/2 nằm ở đâu trên trục số?","da": ["Bên phải điểm 0","Bên trái điểm 0","Trùng điểm 0","Giữa 1 và 2"],"d": 1,"gt": "-1/2 là số âm nên nằm bên trái điểm 0."},
            {"nd": "Phân số nào sau đây biểu diễn cùng một số hữu tỉ với phân số -3/4?","da": ["-6/8","3/4","6/8","-9/16"],"d": 0,"gt": "-3/4 = (-3.2)/(4.2) = -6/8."},
            {"nd": "So sánh hai số -0,5 và -1/3.","da": ["-0,5 > -1/3","-0,5 < -1/3","-0,5 = -1/3","Không so sánh được"],"d": 1,"gt": "-0,5 = -1/2 = -3/6; -1/3 = -2/6. Vì -3 < -2 nên -0,5 < -1/3."},
            {"nd": "Kết quả của phép tính (-2/5) + (4/5) là?","da": ["-6/5","-2/5","2/5","6/5"],"d": 2,"gt": "(-2 + 4)/5 = 2/5."},
            {"nd": "Kết quả của phép tính (1/3) - (-1/2) là?","da": ["-1/6","1/6","5/6","-5/6"],"d": 2,"gt": "1/3 + 1/2 = 2/6 + 3/6 = 5/6."},
            {"nd": "Kết quả của phép tính (-3/4) . (8/9) là?","da": ["-2/3","2/3","-3/2","3/2"],"d": 0,"gt": "Rút gọn chéo: -3 với 9 còn 3 ở mẫu, 8 với 4 còn 2 ở tử ⇒ -2/3."},
            {"nd": "Kết quả của phép tính (-5/6) : (10/3) là?","da": ["-1/4","1/4","-25/9","25/9"],"d": 0,"gt": "(-5/6) . (3/10) = -15/60 = -1/4."},
            {"nd": "Giá trị của biểu thức (-1/2) + 0,25 là?","da": ["-0,75","-0,25","0,25","0,75"],"d": 1,"gt": "-0,5 + 0,25 = -0,25."},
            {"nd": "Tính 2 - (-3/4) = ?","da": ["5/4","11/4","1/4","-11/4"],"d": 1,"gt": "2 + 3/4 = 8/4 + 3/4 = 11/4."},
            {"nd": "Cho x + 1/2 = -3/4. Giá trị của x là?","da": ["-1/4","1/4","-5/4","5/4"],"d": 2,"gt": "x = -3/4 - 1/2 = -3/4 - 2/4 = -5/4."},
            {"nd": "Cho x - (-1/3) = 1/6. Giá trị của x là?","da": ["-1/6","1/6","1/2","-1/2"],"d": 0,"gt": "x + 1/3 = 1/6 ⇒ x = 1/6 - 2/6 = -1/6."},
            {"nd": "Cho x . (2/5) = -4/15. Giá trị của x là?","da": ["-2/3","2/3","-8/75","8/75"],"d": 0,"gt": "x = (-4/15) : (2/5) = (-4/15) . (5/2) = -20/30 = -2/3."},
            {"nd": "Cho (-3/7) : x = 9/14. Giá trị của x là?","da": ["-27/98","-2/3","2/3","-3/2"],"d": 1,"gt": "x = (-3/7) : (9/14) = (-3/7) . (14/9) = -2/3."},
            {"nd": "Tính giá trị biểu thức (1/2)²?","da": ["1/4","1/2","1","1/8"],"d": 0,"gt": "(1/2) . (1/2) = 1/4."},
            {"nd": "Tính giá trị biểu thức (-2/3)³?","da": ["-8/9","8/9","-8/27","8/27"],"d": 2,"gt": "Số âm mũ lẻ ra số âm: (-2)³ / 3³ = -8/27."},
            {"nd": "Cho tỉ lệ thức x/4 = 3/2. Giá trị của x là?","da": ["3","6","8","12"],"d": 1,"gt": "Nhân chéo: 2x = 12 ⇒ x = 6."},
            {"nd": "Khẳng định nào sai?","da": ["ℚ ∪ 𝕀 = ℝ","ℕ ⊂ ℤ","ℤ ⊂ ℚ","ℚ ∩ 𝕀 = ℚ"],"d": 3,"gt": "Tập số hữu tỉ ℚ và vô tỉ 𝕀 là 2 tập rời nhau, giao của chúng là tập rỗng ∅."},
            {"nd": "Số 0 là:","da": ["Số hữu tỉ dương","Số hữu tỉ âm","Số hữu tỉ không dương cũng không âm","Không phải số hữu tỉ"],"d": 2,"gt": "0 = 0/1 nên là số hữu tỉ, nó phân định số âm và số dương."},
            {"nd": "Hỗn số -2 1/4 (Âm hai một phần tư) viết dưới dạng phân số là?","da": ["-7/4","-9/4","9/4","-1/4"],"d": 1,"gt": "Giữ dấu âm bên ngoài: -( (2.4+1)/4 ) = -9/4."},
            {"nd": "Giá trị biểu thức |-3,5| là?","da": ["3,5","-3,5","0","Không xác định"],"d": 0,"gt": "Giá trị tuyệt đối luôn ≥ 0."},
            {"nd": "Tìm x biết |x| = 1/3?","da": ["x = 1/3","x = -1/3","x = ±1/3","x = 0"],"d": 2,"gt": "Có hai số có giá trị tuyệt đối bằng 1/3 là 1/3 và -1/3."},
            {"nd": "Nếu x < 0 thì |x| bằng?","da": ["x","-x","0","1"],"d": 1,"gt": "Theo định nghĩa, nếu x < 0 thì |x| = -x (để ra số dương)."},
            {"nd": "Thứ tự thực hiện phép tính đối với biểu thức không có dấu ngoặc là?","da": ["Cộng, trừ → Nhân, chia → Lũy thừa","Nhân, chia → Cộng, trừ → Lũy thừa","Lũy thừa → Nhân, chia → Cộng, trừ","Lũy thừa → Cộng, trừ → Nhân, chia"],"d": 2,"gt": "Quy tắc thứ tự thực hiện phép tính chuẩn."},
            {"nd": "Tính 0,5 - 3/4 + 1/2 = ?","da": ["1/4","0,5","-1/4","0"],"d": 0,"gt": "1/2 - 3/4 + 1/2 = 2/4 - 3/4 + 2/4 = 1/4."},
            {"nd": "Tính -1,2 . (-5/6) = ?","da": ["1","-1","1,2","-1,2"],"d": 0,"gt": "(-12/10) . (-5/6) = (-6/5) . (-5/6) = 1."},
            {"nd": "Tính (-3)^2 . (-3)^3 = ?","da": ["(-3)^6","(-3)^5","(-3)^1","9^5"],"d": 1,"gt": "Cùng cơ số, cộng số mũ: 2+3=5."},
            {"nd": "Tính ((-2/3)^2)^3 = ?","da": ["(-2/3)^5","(-2/3)^6","(-2/3)^1","(-2/3)^8"],"d": 1,"gt": "Lũy thừa của lũy thừa, nhân số mũ: 2.3=6."},
            {"nd": "Tính 5^8 : 5^2 = ?","da": ["5^4","5^6","5^10","25^6"],"d": 1,"gt": "Chia cùng cơ số, trừ số mũ: 8-2=6."},
            {"nd": "Viết số thập phân 0,125 dưới dạng phân số tối giản:","da": ["1/8","1/4","125/1000","5/40"],"d": 0,"gt": "0,125 = 125/1000, chia cả tử và mẫu cho 125 ta được 1/8."},
            {"nd": "Cho biểu thức A = (1 - 1/2) . (1 - 1/3) . (1 - 1/4). Giá trị của A là?","da": ["1/2","1/3","1/4","1/24"],"d": 2,"gt": "A = 1/2 . 2/3 . 3/4. Triệt tiêu 2 và 3, còn 1/4."},
            {"nd": "Phân số nào sau đây không thể viết được dưới dạng số thập phân hữu hạn?","da": ["3/8","7/20","5/12","11/25"],"d": 2,"gt": "Mẫu 12 = 2² . 3 (có thừa số 3 khác 2 và 5) nên là số TPVHTH."},
            {"nd": "Làm tròn số -3,14159 đến chữ số thập phân thứ hai là?","da": ["-3,14","-3,15","-3,10","-3,1"],"d": 0,"gt": "Chữ số thứ ba là 1 < 5 nên giữ nguyên phần trước đó: -3,14."},
            {"nd": "Số hữu tỉ được kí hiệu bằng chữ cái nào sau đây?","da": ["N","Z","Q","R"],"d": 2,"gt": "Kí hiệu Q (Quotient)."},
            {"nd": "Tập hợp các số thực bao gồm:","da": ["Số hữu tỉ và số nguyên","Số hữu tỉ và số tự nhiên","Số vô tỉ và số nguyên","Số hữu tỉ và số vô tỉ"],"d": 3,"gt": "ℝ = ℚ ∪ 𝕀."},
            {"nd": "Số nào sau đây không có số nghịch đảo?","da": ["1","-1","0","100"],"d": 2,"gt": "Không thể chia cho 0, nên 0 không có số nghịch đảo."},
            {"nd": "Tích của một số hữu tỉ khác 0 với số nghịch đảo của nó bằng?","da": ["0","1","-1","Chính nó"],"d": 1,"gt": "a/b . b/a = 1."},
            {"nd": "Giá trị của x thỏa mãn x : (-0,5) = -1,2 là?","da": ["0,6","-0,6","2,4","-2,4"],"d": 0,"gt": "x = (-1,2) . (-0,5) = 0,6."},
            {"nd": "Giá trị của x thỏa mãn -4/5 . x = 1 là?","da": ["-4/5","4/5","-5/4","5/4"],"d": 2,"gt": "x là nghịch đảo của -4/5 nên x = -5/4."},
            {"nd": "Tổng của hai số đối nhau bằng?","da": ["1","-1","0","Tùy ý"],"d": 2,"gt": "a + (-a) = 0."},
            {"nd": "Kết quả của 2^3 . 2^0 là?","da": ["2^0","2^3","0","2^4"],"d": 1,"gt": "2^0 = 1, nên 2^3 . 1 = 2^3."},
            {"nd": "Kết quả của [(-1/2)^2]^3 là?","da": ["1/64","-1/64","1/32","-1/32"],"d": 0,"gt": "(-1/2)^6 = 1/64."},
            {"nd": "Tập hợp các số hữu tỉ dương được kí hiệu là?","da": ["ℚ*","ℚ+","ℚ-","ℕ*"],"d": 1,"gt": "ℚ+ là tập các số hữu tỉ dương."},
            {"nd": "Tập hợp các số nguyên Z là tập con của tập hợp nào?","da": ["Tập ℕ","Tập ℚ","Không có","Tập rỗng"],"d": 1,"gt": "Mọi số nguyên đều là số hữu tỉ nên ℤ ⊂ ℚ."},
            {"nd": "Cho a, b, c là các số hữu tỉ. Nếu a = b thì a + c ? b + c. Dấu điền vào ô trống là?","da": [">","<","=","≠"],"d": 2,"gt": "Tính chất của đẳng thức: cộng cùng 1 số thì vẫn bằng nhau."},
            {"nd": "Cho dãy số: -1; -1/2; 0; 1/2; 1;... Số hạng tiếp theo là?","da": ["1,5","2","1/4","0"],"d": 0,"gt": "Dãy số tăng dần cách đều 1/2 đơn vị. 1 + 1/2 = 1,5."}
        ],

        "bt_co_ban": [
            {"de": "Thực hiện phép tính: A = (-3/5) + (4/7) - (-1/5)","dd": ["A = 6/35"],"gt": "Nhóm: [(-3/5) + 1/5] + 4/7 = -2/5 + 4/7 = -14/35 + 20/35 = 6/35."},
            {"de": "Thực hiện phép tính: B = (-5/9) . (3/10)","dd": ["B = -1/6"],"gt": "Rút gọn chéo: -5 với 10 còn 2 ở mẫu, 3 với 9 còn 3 ở mẫu. Tử còn -1, mẫu là 3.2=6."},
            {"de": "Thực hiện phép tính: C = (2/3) : (-8/9)","dd": ["C = -3/4"],"gt": "C = 2/3 . (-9/8). Rút gọn chéo: 2 với 8 còn 4 (mẫu), -9 với 3 còn -3 (tử) ⇒ -3/4."},
            {"de": "Tìm x biết: x + 1/4 = -3/4","dd": ["x = -1"],"gt": "x = -3/4 - 1/4 = -4/4 = -1."},
            {"de": "Tìm x biết: (2/5) . x = 8/15","dd": ["x = 4/3"],"gt": "x = 8/15 : 2/5 = 8/15 . 5/2. Rút gọn: 8/2=4, 5/15=1/3 ⇒ 4/3."},
            {"de": "Tính giá trị biểu thức: D = ( -1/2 )² + |-3/4|","dd": ["D = 1"],"gt": "( -1/2 )² = 1/4; |-3/4| = 3/4. D = 1/4 + 3/4 = 4/4 = 1."},
            {"de": "Tìm x biết: |x| - 1/2 = 1","dd": ["x = 1,5 hoặc x = -1,5"],"gt": "|x| = 1 + 1/2 = 3/2. Vậy x = 3/2 hoặc x = -3/2."},
            {"de": "Sắp xếp các số sau theo thứ tự tăng dần: -1/3; 0,5; 0; -1; 2/3","dd": ["-1 ; -1/3 ; 0 ; 0,5 ; 2/3"],"gt": "Đổi ra số thập phân hoặc quy đồng để so sánh dễ dàng."},
            {"de": "Tính lũy thừa: E = ( -2/3 )³","dd": ["E = -8/27"],"gt": "Mũ lẻ của số âm ra số âm: (-2)³/3³ = -8/27."},
            {"de": "Đổi số thập phân 1,25 ra phân số tối giản.","dd": ["5/4"],"gt": "1,25 = 125/100 = 5/4."}
        ],

        "bt_nang_cao": [
            {"de": "Tính hợp lý: A = 5/13 . ( -3/10 ) + 5/13 . ( -7/10 ) + 8/13","hd": "Dùng tính chất phân phối của phép nhân đối với phép cộng: a.b + a.c = a.(b+c)","dd": ["1"],"lg": "A = 5/13 . (-3/10 - 7/10) + 8/13 = 5/13 . (-10/10) + 8/13 = 5/13 . (-1) + 8/13 = -5/13 + 8/13 = 3/13. (Sửa lại kết quả đúng là 3/13)"},
            {"de": "Tìm x biết: (x - 1/3)² = 4/9","hd": "Đưa 4/9 về dạng bình phương. Chú ý 4/9 = (2/3)² = (-2/3)². Có 2 trường hợp.","dd": ["x = 1 hoặc x = -1/3"],"lg": "TH1: x - 1/3 = 2/3 ⇒ x = 1. TH2: x - 1/3 = -2/3 ⇒ x = -1/3."},
            {"de": "Tìm x biết: 2^(x+1) + 2^(x+2) = 48","hd": "Tách 2^(x+1) = 2^x . 2 và 2^(x+2) = 2^x . 4, sau đó đặt nhân tử chung.","dd": ["x = 3"],"lg": "2^x . 2 + 2^x . 4 = 48 ⇒ 2^x . (2 + 4) = 48 ⇒ 2^x . 6 = 48 ⇒ 2^x = 8 ⇒ 2^x = 2³ ⇒ x = 3."},
            {"de": "Tính giá trị biểu thức M = |x - 1,5| + |x - 2,5| tại x = 2.","hd": "Thay x = 2 vào biểu thức rồi tính giá trị tuyệt đối.","dd": ["1"],"lg": "M = |2 - 1,5| + |2 - 2,5| = |0,5| + |-0,5| = 0,5 + 0,5 = 1."},
            {"de": "Tìm giá trị nhỏ nhất của biểu thức P = |x + 3/4| - 5","hd": "Dựa vào tính chất |A| ≥ 0 với mọi A.","dd": ["Min P = -5 khi x = -3/4"],"lg": "Ta có |x + 3/4| ≥ 0 ∀x. Suy ra |x + 3/4| - 5 ≥ -5. Dấu '=' xảy ra khi x + 3/4 = 0 ⇒ x = -3/4."},
            {"de": "Tìm giá trị lớn nhất của biểu thức Q = 10 - |2x - 1|","hd": "Dựa vào tính chất |A| ≥ 0 nên -|A| ≤ 0.","dd": ["Max Q = 10 khi x = 1/2"],"lg": "Ta có |2x - 1| ≥ 0 ⇒ -|2x - 1| ≤ 0 ⇒ 10 - |2x - 1| ≤ 10. Dấu '=' xảy ra khi 2x - 1 = 0 ⇒ x = 1/2."},
            {"de": "Tính nhanh: S = 1/(1.2) + 1/(2.3) + 1/(3.4) + ... + 1/(49.50)","hd": "Dùng công thức tách phân số: 1/(n.(n+1)) = 1/n - 1/(n+1). Triệt tiêu các số hạng ở giữa.","dd": ["49/50"],"lg": "S = (1 - 1/2) + (1/2 - 1/3) + ... + (1/49 - 1/50) = 1 - 1/50 = 49/50."},
            {"de": "Tìm x, y biết: |x - 1/2| + (y + 3/4)² = 0","hd": "Tổng của hai biểu thức không âm bằng 0 khi và chỉ khi từng biểu thức bằng 0.","dd": ["x = 1/2 và y = -3/4"],"lg": "Do |x - 1/2| ≥ 0 và (y + 3/4)² ≥ 0 nên tổng bằng 0 khi x - 1/2 = 0 và y + 3/4 = 0. Vậy x = 1/2, y = -3/4."},
            {"de": "Cho a/b = c/d (với b, d ≠ 0). Chứng minh rằng: (a+b)/b = (c+d)/d","hd": "Cộng 1 vào hai vế của đẳng thức a/b = c/d.","dd": ["Xem lời giải"],"lg": "Ta có a/b = c/d. Cộng 1 vào 2 vế: a/b + 1 = c/d + 1 ⇒ a/b + b/b = c/d + d/d ⇒ (a+b)/b = (c+d)/d (đpcm)."},
            {"de": "Tìm ba số x, y, z biết x/2 = y/3 = z/4 và x + y - z = 10.","hd": "Áp dụng tính chất dãy tỉ số bằng nhau.","dd": ["x=20, y=30, z=40"],"lg": "x/2 = y/3 = z/4 = (x + y - z)/(2 + 3 - 4) = 10/1 = 10. Suy ra x=20, y=30, z=40."},
            {"de": "Tính M = [ (-0,5)³ . (-2)⁴ ] / (-1/2)²","hd": "Chuyển hết về phân số cơ số 2 hoặc -2.","dd": ["-2"],"lg": "(-0,5)³ = -1/8; (-2)⁴ = 16; (-1/2)² = 1/4. M = (-1/8 . 16) / (1/4) = (-2) / (1/4) = -2 . 4 = -8. (Sửa lại kết quả đúng là -8)"},
            {"de": "Tìm x biết: 3/(x-1) = 4/(x+2)","hd": "Sử dụng tính chất tỉ lệ thức (nhân chéo).","dd": ["x = 10"],"lg": "3(x + 2) = 4(x - 1) ⇒ 3x + 6 = 4x - 4 ⇒ x = 10."},
            {"de": "So sánh 2^300 và 3^200","hd": "Đưa về cùng số mũ bằng tính chất lũy thừa: (x^m)^n = x^(m.n).","dd": ["2^300 < 3^200"],"lg": "2^300 = (2³)^100 = 8^100. 3^200 = (3²)^100 = 9^100. Vì 8 < 9 nên 8^100 < 9^100 ⇒ 2^300 < 3^200."},
            {"de": "Chứng minh rằng số thập phân vô hạn tuần hoàn 0,(9) bằng 1.","hd": "Đặt x = 0,9999... nhân 10x rồi trừ đi x.","dd": ["Xem lời giải"],"lg": "Đặt x = 0,999... ⇒ 10x = 9,999... Lấy 10x - x = 9,999... - 0,999... ⇒ 9x = 9 ⇒ x = 1."},
            {"de": "Tìm hai số nguyên x, y biết: x/y = -3/4 và x.y = -12.","hd": "Đặt x = -3k, y = 4k thay vào phương trình tích.","dd": ["x = -3, y = 4 hoặc x = 3, y = -4"],"lg": "x = -3k, y = 4k ⇒ (-3k)(4k) = -12 ⇒ -12k² = -12 ⇒ k² = 1 ⇒ k = 1 hoặc k = -1. Từ đó suy ra (x,y)."},
            {"de": "Tìm phần nguyên của số hữu tỉ x = -4,7.","hd": "Phần nguyên của x (kí hiệu [x]) là số nguyên lớn nhất không vượt quá x.","dd": ["-5"],"lg": "Số nguyên lớn nhất nhỏ hơn hoặc bằng -4,7 là -5. Chú ý không phải là -4."},
            {"de": "Tính nhanh: B = 1/3 + 1/3² + 1/3³ + ... + 1/3^10","hd": "Nhân 3B rồi lấy 3B - B.","dd": ["B = (3^10 - 1) / (2.3^10)"],"lg": "3B = 1 + 1/3 + 1/3² + ... + 1/3^9. Trừ B ta được: 2B = 1 - 1/3^10. Vậy B = (1 - 1/3^10) / 2."},
            {"de": "Một quyển sách giảm giá 20% thì có giá 40.000đ. Hỏi giá ban đầu là bao nhiêu?","hd": "Giá sau khi giảm tương ứng với bao nhiêu % giá ban đầu?","dd": ["50.000đ"],"lg": "Giá sau khi giảm = 100% - 20% = 80% giá ban đầu. Giá ban đầu = 40.000 : 80% = 40.000 : 0,8 = 50.000đ."},
            {"de": "Tìm x biết: |x - 2| = x - 2","hd": "Sử dụng tính chất |A| = A khi A ≥ 0.","dd": ["x ≥ 2"],"lg": "|x - 2| = x - 2 khi và chỉ khi x - 2 ≥ 0 ⇒ x ≥ 2."},
            {"de": "Tìm x, y, z biết: 2x = 3y = 4z và x + y + z = 26.","hd": "Chia các vế cho BCNN(2,3,4) = 12 để đưa về dãy tỉ số bằng nhau.","dd": ["x=12, y=8, z=6"],"lg": "2x/12 = 3y/12 = 4z/12 ⇒ x/6 = y/4 = z/3. Theo t/c dãy tỉ số bằng nhau: (x+y+z)/(6+4+3) = 26/13 = 2. Vậy x=12, y=8, z=6."}
        ]
    }
}

T7["Chương 1: Số hữu tỉ — Số thực"] = C1_T7
TOAN["Lớp 7"] = T7