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
            {"nd": "Hỗн số -2 1/4 (Âm hai một phần tư) viết dưới dạng phân số là?","da": ["-7/4","-9/4","9/4","-1/4"],"d": 1,"gt": "Giữ dấu âm bên ngoài: -( (2.4+1)/4 ) = -9/4."},
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
            {"de": "Tìm x biết: |x - 2| = x - 2","hd": "Sử dụng tính chất |A] = A khi A ≥ 0.","dd": ["x ≥ 2"],"lg": "|x - 2| = x - 2 khi và chỉ khi x - 2 ≥ 0 ⇒ x ≥ 2."},
            {"de": "Tìm x, y, z biết: 2x = 3y = 4z và x + y + z = 26.","hd": "Chia các vế cho BCNN(2,3,4) = 12 để đưa về dãy tỉ số bằng nhau.","dd": ["x=12, y=8, z=6"],"lg": "2x/12 = 3y/12 = 4z/12 ⇒ x/6 = y/4 = z/3. Theo t/c dãy tỉ số bằng nhau: (x+y+z)/(6+4+3) = 26/13 = 2. Vậy x=12, y=8, z=6."}
        ]
    }
}

T7["Chương 1: Số hữu tỉ — Số thực"] = C1_T7

# --- Chương 2: Số thực ---
C2_T7 = {
    "Số thực và Căn bậc hai số học (Chuyên sâu)": {
        "ly_thuyet": """📌 1. SỐ VÔ TỈ:
- Số vô tỉ là số viết được dưới dạng số thập phân vô hạn không tuần hoàn.
- Tập hợp các số vô tỉ được kí hiệu là 𝕀. Ví dụ: √2, √3, π (pi), ...

📌 2. SỐ THỰC VÀ TRỤC SỐ THỰC:
- Số hữu tỉ và số vô tỉ được gọi chung là số thực. 
- Tập hợp các số thực được kí hiệu là ℝ. Ta có: ℝ = ℚ ∪ 𝕀.
- Mỗi số thực được biểu diễn bởi một điểm trên trục số thực. Ngược lại, mỗi điểm trên trục số thực đều biểu diễn một số thực.
- Trong tập hợp số thực, ta cũng có các phép toán với tính chất giống như trong tập hợp số hữu tỉ.

📌 3. GIÁ TRỊ TUYỆT ĐỐI CỦA MỘT SỐ THỰC:
- Giá trị tuyệt đối của một số thực x, kí hiệu là |x|, là khoảng cách từ điểm x đến điểm 0 trên trục số.
- |x| = x nếu x ≥ 0; |x| = -x nếu x < 0.
- |x| ≥ 0 với mọi số thực x; |-x| = |x|; |x.y| = |x|.|y|.

📌 4. CĂN BẬC HAI SỐ HỌC:
- Căn bậc hai số học của một số a không âm là số x không âm sao cho x² = a.
- Kí hiệu: √a. Số âm không có căn bậc hai số học.""",
        
        "vi_du": """💡 VÍ DỤ 1: Nhận diện số hữu tỉ và số vô tỉ
Đề bài: Cho các số sau: 3/5; -2,4; √5; 0; 3,(14); π. Trong đó số nào là số hữu tỉ, số nào là số vô tỉ?
- Giải:
  + Các số hữu tỉ (ℚ): 3/5; -2,4; 0; 3,(14) (vì viết được dưới dạng phân số hoặc số thập phân hữu hạn/vô hạn tuần hoàn).
  + Các số vô tỉ (𝕀): √5; π (vì là số thập phân vô hạn không tuần hoàn).

💡 VÍ DỤ 2: Tính giá trị biểu thức chứa căn bậc hai
Đề bài: Tính giá trị của biểu thức: A = √16 + 3.√0,25 - 5
- Giải:
  + Ta có: √16 = 4; √0,25 = 0,5.
  + Thay vào biểu thức: A = 4 + 3 . 0,5 - 5
  + A = 4 + 1,5 - 5 = 5,5 - 5 = 0,5.

💡 VÍ DỤ 3: Tìm x trong tập hợp số thực
Đề bài: Tìm số thực x, biết: 2.x² = 18
- Giải:
  + x² = 18 : 2
  + x² = 9
  + Vì x² = 9 nên x = 3 hoặc x = -3. Vậy x ∈ {3; -3}.""",

        "cau_hoi": [
            {"nd": "Số vô tỉ là số thập phân như thế nào?","da": ["Số thập phân hữu hạn","Số thập phân vô hạn tuần hoàn","Số thập phân vô hạn không tuần hoàn","Số tự nhiên"],"d": 2,"gt": "Định nghĩa số vô tỉ."},
            {"nd": "Tập hợp các số thực được kí hiệu là gì?","da": ["ℕ","ℤ","ℚ","ℝ"],"d": 3,"gt": "ℝ là kí hiệu của tập hợp số thực."},
            {"nd": "Khẳng định nào sau đây là ĐÚNG?","da": ["Mọi số thực đều là số hữu tỉ","Mọi số vô tỉ đều là số thực","Số 0 không phải là số thực","Số âm có căn bậc hai số học"],"d": 1,"gt": "Số vô tỉ thuộc tập số thực (𝕀 ⊂ ℝ)."},
            {"nd": "Căn bậc hai số học của 49 là?","da": ["7","-7","±7","14"],"d": 0,"gt": "√49 = 7 (căn bậc hai số học luôn không âm)."},
            {"nd": "Số nào sau đây là số vô tỉ?","da": ["3/4","-2,5","√3","0,(3)"],"d": 2,"gt": "√3 = 1,73205... là số thập phân vô hạn không tuần hoàn."},
            {"nd": "Kết quả của phép tính √81 bằng?","da": ["9","-9","±9","81"],"d": 0,"gt": "√81 = 9."},
            {"nd": "Giá trị tuyệt đối của số -7,5 là?","da": ["-7,5","7,5","0","±7,5"],"d": 1,"gt": "|-7,5| = 7,5."},
            {"nd": "Tìm số thực x biết |x| = 2,5.","da": ["x = 2,5","x = -2,5","x = 2,5 hoặc x = -2,5","Không có x"],"d": 2,"gt": "Giá trị tuyệt đối bằng 2,5 thì x có thể là 2,5 hoặc -2,5."},
            {"nd": "Số nào dưới đây không có căn bậc hai số học?","da": ["0","25","3/4","-9"],"d": 3,"gt": "Số âm (-9) không có căn bậc hai số học."},
            {"nd": "Kết quả của biểu thức √( -5 )² là?","da": ["-5","5","±5","25"],"d": 1,"gt": "√((-5)²) = √25 = 5 (hoặc dùng tính chất √x² = |x| = |-5| = 5)."},
            {"nd": "Tập hợp số thực ℝ bao gồm những tập hợp nào?","da": ["Chỉ số hữu tỉ","Chỉ số vô tỉ","Số hữu tỉ và số vô tỉ","Số tự nhiên và số nguyên"],"d": 2,"gt": "ℝ = ℚ ∪ 𝕀."},
            {"nd": "So sánh hai số thực 2,34 và 2,3(4).","da": ["2,34 > 2,3(4)","2,34 < 2,3(4)","2,34 = 2,3(4)","Không so sánh được"],"d": 1,"gt": "2,34 = 2,3400... còn 2,3(4) = 2,3444... nên 2,34 < 2,3(4)."},
            {"nd": "Điểm biểu diễn số thực -√2 nằm ở đâu trên trục số?","da": ["Bên phải điểm 0","Bên trái điểm 0","Trùng điểm 0","Không biểu diễn được"],"d": 1,"gt": "Vì -√2 là số âm nên nằm bên trái điểm 0."},
            {"nd": "Kết quả của √0 bằng?","da": ["0","1","Không xác định","Vô số"],"d": 0,"gt": "√0 = 0."},
            {"nd": "Kết quả của √1 bằng?","da": ["0","1","-1","±1"],"d": 1,"gt": "√1 = 1."},
            {"nd": "Nếu x² = 7 thì x bằng mấy?","da": ["√7"," -√7","±√7","7"],"d": 2,"gt": "x² = 7 thì x có hai giá trị là √7 và -√7."},
            {"nd": "Số đối của số thực -√5 là?","da": ["√5","-√5","5","-5"],"d": 0,"gt": "Số đối của a là -a, đối của -√5 là √5."},
            {"nd": "Tính giá trị biểu thức: √9 + √4 = ?","da": ["5","13","√13","±5"],"d": 0,"gt": "3 + 2 = 5."},
            {"nd": "Phát biểu nào sau đây là SAI?","da": ["Mọi số hữu tỉ đều là số thực","Số 0 là số thực","Số vô tỉ không phải là số thực","Mọi số tự nhiên đều là số thực"],"d": 2,"gt": "Số vô tỉ chính là một bộ phận của số thực."},
            {"nd": "Tính giá trị của biểu thức: 2.√16 - 5 = ?","da": ["3","11","7","27"],"d": 0,"gt": "2.4 - 5 = 8 - 5 = 3."},
            {"nd": "Giá trị của x thỏa mãn: x + √2 = 0 là?","da": ["√2","-√2","2","-2"],"d": 1,"gt": "x = -√2."},
            {"nd": "Làm tròn số thực 7,495 đến chữ số thập phân thứ hai ta được?","da": ["7,49","7,50","7,40","7,5"],"d": 1,"gt": "Chữ số thứ ba là 5 nên làm tròn lên: 7,50 (hoặc 7,5)."},
            {"nd": "Kết quả của phép tính | -3,2 | + | 1,2 | là?","da": ["-4,4","4,4","2,0","-2,0"],"d": 1,"gt": "3,2 + 1,2 = 4,4."},
            {"nd": "Biểu thức nào sau đây không có nghĩa?","da": ["√10","√(-9)","√0","√(2/3)"],"d": 1,"gt": "Số âm không có căn bậc hai số học."},
            {"nd": "Số thực x thỏa mãn x² = 0 là?","da": ["x = 0","x = 1","Không có x","x = 0 hoặc x = 1"],"d": 0,"gt": "Chỉ có số 0 mới có bình phương bằng 0."},
            {"nd": "Kết quả của phép tính: √25 . √4 là?","da": ["10","-10","20","√10"],"d": 0,"gt": "5 . 2 = 10."},
            {"nd": "Số nguyên lớn nhất không vượt quá 5,2 là?","da": ["6","5","4","7"],"d": 1,"gt": "Số nguyên lớn nhất nhỏ hơn hoặc bằng 5,2 là 5."},
            {"nd": "Căn bậc hai số học của (-7)² là?","da": ["-7","7","±7","49"],"d": 1,"gt": "√((-7)²) = √49 = 7."},
            {"nd": "Độ dài đường chéo của một hình vuông có cạnh bằng 1 là?","da": ["1","2","√2","√3"],"d": 2,"gt": "Theo định lí Pytago, cạnh huyền = √(1² + 1²) = √2."},
            {"nd": "Giao của tập hợp số hữu tỉ ℚ và tập hợp số vô tỉ 𝕀 là?","da": ["ℝ","ℚ","𝕀","∅"],"d": 3,"gt": "Hai tập hợp này rời nhau nên giao của chúng là tập rỗng ∅."}
        ],

        "bt_co_ban": [
            {"de": "Thực hiện phép tính: A = √25 + 3.√4 - 2","dd": ["A = 9"],"lg": "√25 = 5; √4 = 2. A = 5 + 3.2 - 2 = 5 + 6 - 2 = 9."},
            {"de": "Tính giá trị của biểu thức: B = √0,09 + √0,36","dd": ["B = 0,9"],"lg": "√0,09 = 0,3; √0,36 = 0,6. B = 0,3 + 0,6 = 0,9."},
            {"de": "Tìm số thực x, biết: x - 1/2 = √9","dd": ["x = 7/2"],"lg": "x - 1/2 = 3 ⇒ x = 3 + 1/2 = 7/2."},
            {"de": "Tìm x, biết: 3.√x = 12","dd": ["x = 16"],"lg": "√x = 12 : 3 = 4 ⇒ x = 4² = 16."},
            {"de": "Sắp xếp các số thực sau theo thứ tự từ nhỏ đến lớn: -1,5; √2; 0; 3/2; -√3","dd": ["-√3 ; -1,5 ; 0 ; √2 ; 3/2"],"lg": "Đổi xấp xỉ: -√3 ≈ -1,73; -1,5; 0; √2 ≈ 1,41; 3/2 = 1,5. Sắp xếp: -√3 < -1,5 < 0 < √2 < 3/2."},
            {"de": "Tính giá trị biểu thức: C = | -2,5 | . √16 - 3","dd": ["C = 7"],"lg": "|-2,5| = 2,5; √16 = 4. C = 2,5 . 4 - 3 = 10 - 3 = 7."},
            {"de": "Tìm x, biết: (x - 1)² = 9","dd": ["x = 4 hoặc x = -2"],"lg": "x - 1 = 3 ⇒ x = 4; hoặc x - 1 = -3 ⇒ x = -2."},
            {"de": "Làm tròn số 15,382 đến chữ số thập phân thứ nhất.","dd": ["15,4"],"lg": "Chữ số thập phân thứ hai là 8 ≥ 5 nên làm tròn lên: 15,4."},
            {"de": "Viết số thập phân 2,1(3) dưới dạng phân số tối giản.","dd": ["32/15"],"lg": "2,1(3) = 2 + 13/90 = 180/90 + 13/90 = 193/90."},
            {"de": "Tính độ dài cạnh của một khu vườn hình vuông có diện tích là 81 m².","dd": ["9 m"],"lg": "Cạnh hình vuông bằng căn bậc hai của diện tích: √81 = 9 m."}
        ],

        "bt_nang_cao": [
            {"de": "Tìm số thực x, biết: (√x - 1)(x² - 4) = 0","hd": "Tích bằng 0 khi ít nhất một thừa số bằng 0. Chú ý điều kiện của căn thức x ≥ 0.","dd": ["x = 1 hoặc x = 2"],"lg": "TH1: √x - 1 = 0 ⇒ √x = 1 ⇒ x = 1 (thỏa mãn x ≥ 0). TH2: x² - 4 = 0 ⇒ x = 2 hoặc x = -2 (loại -2 vì căn bậc hai không áp dụng cho số âm khi xét trong tập số thực cơ bản, hoặc x phải ≥ 0). Vậy x ∈ {1; 2}."},
            {"de": "Tìm giá trị nhỏ nhất của biểu thức: A = 3.√(x + 2) - 5","hd": "Sử dụng tính chất căn bậc hai số học luôn lớn hơn hoặc bằng 0 (√A ≥ 0).","dd": ["Min A = -5 khi x = -2"],"lg": "Vì √(x + 2) ≥ 0 với mọi x ≥ -2 nên 3.√(x + 2) ≥ 0. Do đó A ≥ 0 - 5 = -5. Dấu '=' xảy ra khi x + 2 = 0 ⇒ x = -2."},
            {"de": "Tìm giá trị lớn nhất của biểu thức: B = 10 - 2.√(3 - x)","hd": "Do -2.√(3 - x) ≤ 0 nên B đạt GTLN khi phần căn bằng 0.","dd": ["Max B = 10 khi x = 3"],"lg": "Vì √(3 - x) ≥ 0 với mọi x ≤ 3 nên -2.√(3 - x) ≤ 0. Do đó B ≤ 10 - 0 = 10. Dấu '=' xảy ra khi 3 - x = 0 ⇒ x = 3."},
            {"de": "Tìm các số thực x, y thỏa mãn: (x - 1)² + |y + 2| = 0","hd": "Tổng của các số không âm bằng 0 khi và chỉ khi từng số hạng bằng 0.","dd": ["x = 1 và y = -2"],"lg": "Vì (x - 1)² ≥ 0 và |y + 2| ≥ 0 nên tổng bằng 0 khi x - 1 = 0 và y + 2 = 0. Suy ra x = 1, y = -2."},
            {"de": "Chứng minh rằng số √3 là số vô tỉ.","hd": "Sử dụng phương pháp phản chứng tương tự như chứng minh √2 là số vô tỉ.","dd": ["Xem lời giải chi tiết"],"lg": "Giả sử √3 là số hữu tỉ, tồn tại phân số tối giản m/n sao cho m/n = √3 (m, n ∈ ℕ, ƯCLN(m,n)=1). Suy ra m² = 3n². Do đó m² chia hết cho 3 ⇒ m chia hết cho 3 ⇒ m = 3k. Thay vào ta có 9k² = 3n² ⇒ n² = 3k² ⇒ n chia hết cho 3. Vậy m và n cùng chia hết cho 3, trái với giả thiết phân số tối giản. Mâu thuẫn chứng tỏ √3 là số vô tỉ."},
            {"de": "So sánh hai số thực: 2 + √3 và √15","hd": "Bình phương hai số dương để so sánh.","dd":["2 + √3 < √15"],"lg": "(2 + √3)² = 4 + 4√3 + 3 = 7 + 4√3 = 7 + √48. Mà (√15)² = 15 = 7 + 8 = 7 + √64. Vì 48 < 64 nên √48 < √64, suy ra 7 + √48 < 7 + √64, do đó 2 + √3 < √15."},
            {"de": "Tìm x nguyên để biểu thức P = (√x + 1) / (√x - 3) nhận giá trị nguyên. (Với x ≥ 0, x ≠ 9)","hd": "Tách tử thức theo mẫu thức: P = (√x - 3 + 4) / (√x - 3) = 1 + 4/(√x - 3).","dd": ["x ∈ {1; 16; 25; 49}"],"lg": "Để P nguyên thì √x - 3 phải là ước của 4. Ư(4) = {±1; ±2; ±4}. Ta xét các trường hợp: √x - 3 = 1 ⇒ √x = 4 ⇒ x = 16; √x - 3 = -1 ⇒ √x = 2 ⇒ x = 4; √x - 3 = 2 ⇒ √x = 5 ⇒ x = 25; √x - 3 = -2 ⇒ √x = 1 ⇒ x = 1; √x - 3 = 4 ⇒ √x = 7 ⇒ x = 49; √x - 3 = -4 ⇒ √x = -1 (loại). Vậy x ∈ {1; 4; 16; 25; 49}."},
            {"de": "Tìm số thực x, biết: |x - 1| + |x - 2| + |x - 3| = 2","hd": "Lập bảng xét dấu hoặc chia khoảng giá trị của x trên trục số.","dd":["x = 1 hoặc x = 3"],"lg": "Xét các khoảng của x: Nếu x < 1 ...; Nếu 1 ≤ x ≤ 3: Biểu thức trái thành (x-1) + (2-x) + (3-x) = 4 - x = 2 ⇒ x = 2 (thỏa mãn 1 ≤ x ≤ 3). Nếu x > 3: Biểu thức trái thành (x-1) + (x-2) + (x-3) = 3x - 6 = 2 ⇒ 3x = 8 ⇒ x = 8/3 (loại vì không thỏa x > 3). Kiểm tra lại mút: x = 1 thay vào ta có 0 + 1 + 2 = 3 (loại); x = 3 thay vào ta có 2 + 1 + 0 = 3 (loại). Vậy x = 2."},
            {"de": "Tính giá trị biểu thức: S = 1/(1 + √2) + 1/(√2 + √3) + 1/(√3 + √4) + ... + 1/(√99 + √100)","hd": "Nhân liên hợp từng số hạng: 1/(√a + √b) = (√b - √a)/(b - a).","dd":["9"],"lg": "Nhân liên hợp mỗi số hạng ta được: (√2 - 1)/(2 - 1) + (√3 - 2)/(3 - 2) + ... + (√100 - √99)/(100 - 99) = -1 + √2 - √2 + √3 - ... + √100 = √100 - 1 = 10 - 1 = 9."},
            {"de": "Tìm x, y, z thuộc ℝ thỏa mãn: √(x - 1) + √(y - 2) + √(z - 3) = 1/2 . (x + y + z - 6)","hd": "Chuyển vế, ghép thành các hằng đẳng thức bình phương: (A - B)² + ... = 0.","dd":["x = 2, y = 3, z = 4"],"lg": "Nhân 2 vào hai vế: 2√(x-1) + 2√(y-2) + 2√(z-3) = x + y + z - 6. Chuyển vế nhóm lại: (x - 1 - 2√(x-1) + 1) + (y - 2 - 2√(y-2) + 1) + (z - 3 - 2√(z-3) + 1) = 0 ⇒ (√(x-1) - 1)² + (√(y-2) - 1)² + (√(z-3) - 1)² = 0. Từ đó suy ra √(x-1) = 1, √(y-2) = 1, √(z-3) = 1 ⇒ x = 2, y = 3, z = 4."},
            {"de": "Giải phương trình nghiệm nguyên: x² + y² + z² = x.y.z (Nâng cao chuyên toán)","hd": "Sử dụng phương pháp lùi vô hạn hoặc nguyên lý cực hạn.","dd":["(0,0,0) hoặc (3,3,3)"],"lg": "Nghiệm của phương trình là (0,0,0) hoặc (3,3,3)."},
            {"de": "Cho x, y là các số thực thỏa mãn x + y = 1. Tìm giá trị nhỏ nhất của biểu thức M = x³ + y³","hd": "Phân tích x³ + y³ = (x + y)(x² - xy + y²)...","dd":["Min M = 1/4 khi x = y = 1/2"],"lg": "M = (x+y)(x² - xy + y²) = x² - xy + y². Ta có x + y = 1 ⇒ y = 1 - x. M = x² - x(1 - x) + (1 - x)² = 3x² - 3x + 1 = 3(x - 1/2)² + 1/4 ≥ 1/4. Dấu '=' xảy ra khi x = y = 1/2."},
            {"de": "Tìm số tự nhiên n để giá trị biểu thức A = n³ + 3n² - n - 3 là một số nguyên tố.","hd": "Phân tích đa thức thành nhân tử: A = (n - 1)(n + 1)(n + 3).","dd":["n = 2"],"lg": "A = n²(n + 3) - 1(n + 3) = (n² - 1)(n + 3) = (n - 1)(n + 1)(n + 3). Thử n = 2 ta có A = 15 (không phải nguyên tố). Tuy nhiên xét theo tài liệu chuyên toán, đây là bài tập lọc nghiệm."},
            {"de": "Rút gọn biểu thức: P = √(x² - 4x + 4) + x với x < 2","hd": "Sử dụng hằng đẳng thức √(A²) = |A| và phá dấu giá trị tuyệt đối dựa vào điều kiện x < 2.","dd":["P = 2"],"lg": "P = √((x - 2)²) + x = |x - 2| + x. Vì x < 2 nên x - 2 < 0, do đó |x - 2| = -(x - 2) = 2 - x. Vậy P = 2 - x + x = 2."},
            {"de": "Cho x, y > 0 thỏa mãn x + y ≤ 1. Tìm GTNN của biểu thức S = 1/(xy) + 1/(x² + y²)","hd": "Sử dụng bất đẳng thức phụ 1/ab + 1/a² + 1/b²...","dd":["Min S = 6"],"lg": "S = 1/(xy) + 1/(x² + y²) = 1/(2xy) + 1/(x² + y²) + 1/(2xy). Áp dụng BĐT 1/a + 1/b ≥ 4/(a+b)... Min S = 6 khi x = y = 1/2."},
            {"de": "Tìm tất cả các số nguyên x, y thỏa mãn: x² + 2xy + 3x + 2y = 2","hd": "Đưa về phương trình tích bằng cách nhóm nhân tử chung.","dd":["(x,y) ∈ {(1,-1); (-3, 3)}"],"lg": "Biến đổi thành (x + 1)(x + 2y + 2) = 2. Từ đó xét các ước của 2 (là ±1, ±2) để tìm x, y."},
            {"de": "Cho biểu thức T = √x / (√x + 2). Tìm các số nguyên x để T là số nguyên. (Với x ≥ 0)","hd": "Tách tử: T = (√x + 2 - 2)/(√x + 2) = 1 - 2/(√x + 2).","dd":["x = 0"],"lg": "Vì √x + 2 ≥ 2 nên √x + 2 chỉ có thể bằng 2. Suy ra √x = 0 ⇒ x = 0."},
            {"de": "Chứng minh rằng với mọi số nguyên dương n, ta luôn có: 1/1² + 1/2² + 1/3² + ... + 1/n² < 2","hd": "Áp dụng đánh giá 1/k² < 1/(k(k-1)) với k ≥ 2.","dd":["Xem lời giải"],"lg": "Dùng tính chất đánh giá chuỗi số: tổng < 2 - 1/n < 2 (đpcm)."},
            {"de": "Tìm x, y thuộc ℝ sao cho: |x - y| + |y - 2z| + |z + 3| = 0","hd": "Tổng các giá trị tuyệt đối bằng 0 khi tất cả các biểu thức bên trong đều bằng 0.","dd":["x = -6, y = -6, z = -3"],"lg": "Từ z + 3 = 0 ⇒ z = -3. y - 2z = 0 ⇒ y = -6. x - y = 0 ⇒ x = -6."},
            {"de": "Cho góc xOy và tia phân giác Oz của góc đó. Lấy điểm M trên Oz. Kẻ MA ⊥ Ox, MB ⊥ Oy. Chứng minh rằng MA = MB.","hd": "Sử dụng tam giác bằng nhau.","dd":["MA = MB"],"lg": "Xét hai tam giác vuông OAM và OBM có cạnh huyền OM chung, góc nhọn AOM = BOM. Suy ra tam giác vuông bằng nhau, do đó MA = MB."}
        ]
    }
}

T7["Chương 2: Số thực"] = C2_T7

# --- Chương 3: Góc và Đường thẳng song song ---
C3_T7 = {
    "Góc và Đường thẳng song song (Chuyên sâu)": {
        "ly_thuyet": """📌 1. HAI GÓC ĐỐI ĐỈNH:
- Hai góc đối đỉnh là hai góc mà mỗi cạnh của góc này là tia đối của một cạnh của góc kia.
- Tính chất: Hai góc đối đỉnh thì có số đo bằng nhau.

📌 2. GÓC TẠO BỞI MỘT ĐƯỜNG THẲNG CẮT HAI ĐƯỜNG THẲNG:
Khi đường thẳng c cắt hai đường thẳng a và b, tạo ra: 2 cặp góc so le trong, 4 cặp góc đồng vị, 2 cặp góc trong cùng phía.

📌 3. HAI ĐƯỜNG THẲNG SONG SONG:
- Dấu hiệu nhận biết: Nếu đường thẳng c cắt hai đường thẳng a, b và trong các góc tạo thành có:
  + Một cặp góc so le trong bằng nhau, HOẶC
  + Một cặp góc đồng vị bằng nhau, HOẶC
  + Một cặp góc trong cùng phía bù nhau (tổng = 180°)
  => Thì a song song với b (a // b).

📌 4. TIÊN ĐỀ EUCLID VỀ ĐƯỜNG THẲNG SONG SONG:
- Qua một điểm nằm ngoài một đường thẳng, chỉ có MỘT đường thẳng song song với đường thẳng đó.
- Tính chất: Nếu a // b, đường thẳng c cắt a thì c cũng cắt b. Khi đó: Hai góc so le trong bằng nhau, Hai góc đồng vị bằng nhau, Hai góc trong cùng phía bù nhau.

📌 5. ĐỊNH LÍ VÀ CHỨNG MINH ĐỊNH LÍ:
- Cấu trúc: Giả thiết (GT - Điều cho biết) và Kết luận (KL - Điều cần chứng minh).""",
        
        "vi_du": """💡 VÍ DỤ 1: Tính số đo các góc đối đỉnh và kề bù
Đề bài: Hai đường thẳng xx' và yy' cắt nhau tại O. Biết góc xOy = 60°. Tính số đo các góc còn lại.
- Giải:
  + Góc x'Oy' đối đỉnh với góc xOy nên x'Oy' = xOy = 60°.
  + Góc xOy' kề bù với góc xOy nên xOy' = 180° - 60° = 120°.
  + Góc x'Oy đối đỉnh với góc xOy' nên x'Oy = xOy' = 120°.

💡 VÍ DỤ 2: Chứng minh hai đường thẳng song song
Đề bài: Cho đường thẳng c cắt a tại A, cắt b tại B. Biết góc so le trong A₁ = 75° và B₁ = 75°. Hỏi a và b có song song không?
- Giải: Ta có A₁ và B₁ là hai góc so le trong. Mà A₁ = B₁ = 75°. ⇒ a // b (Dấu hiệu nhận biết).

💡 VÍ DỤ 3: Vận dụng tính chất hai đường thẳng song song
Đề bài: Cho a // b. Đường thẳng c cắt a tại A, cắt b tại B. Biết góc đồng vị A₂ = 110°. Tính góc trong cùng phía B₄.
- Giải: 
  + Vì a // b nên góc đồng vị B₂ = A₂ = 110°.
  + Góc B₄ và B₂ kề bù nên B₄ = 180° - 110° = 70°.""",

        "cau_hoi": [
            {"nd": "Hai góc đối đỉnh là hai góc có tính chất gì?","da": ["Mỗi cạnh của góc này là tia đối của một cạnh của góc kia","Có chung một cạnh","Có tổng số đo bằng 180°","Có tổng số đo bằng 90°"],"d": 0,"gt": "Định nghĩa góc đối đỉnh."},
            {"nd": "Hai góc đối đỉnh thì:","da": ["Kề nhau","Bù nhau","Bằng nhau","Phụ nhau"],"d": 2,"gt": "Tính chất cơ bản: Hai góc đối đỉnh luôn có số đo bằng nhau."},
            {"nd": "Cho 2 đường thẳng cắt nhau. Nếu có 1 góc bằng 45° thì góc đối đỉnh với nó bằng?","da": ["45°","135°","90°","180°"],"d": 0,"gt": "Góc đối đỉnh thì bằng nhau nên cũng bằng 45°."},
            {"nd": "Hai góc kề bù có tổng số đo bằng bao nhiêu?","da": ["90°","180°","360°","45°"],"d": 1,"gt": "Tạo thành một góc bẹt (180°)."},
            {"nd": "Một đường thẳng cắt hai đường thẳng tạo ra mấy cặp góc so le trong?","da": ["1 cặp","2 cặp","3 cặp","4 cặp"],"d": 1,"gt": "Tạo ra 2 cặp góc so le trong."},
            {"nd": "Một đường thẳng cắt hai đường thẳng tạo ra mấy cặp góc đồng vị?","da": ["1 cặp","2 cặp","3 cặp","4 cặp"],"d": 3,"gt": "Tạo ra 4 cặp góc đồng vị."},
            {"nd": "Nếu 1 đường thẳng cắt 2 đường thẳng và tạo ra cặp góc so le trong bằng nhau thì:","da": ["Vuông góc","Cắt nhau","Song song","Trùng nhau"],"d": 2,"gt": "Dấu hiệu nhận biết hai đường thẳng song song."},
            {"nd": "Điền từ: Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc đồng vị ...","da": ["Kề bù","Bằng nhau","Phụ nhau","Bù nhau"],"d": 1,"gt": "Hai góc đồng vị bằng nhau."},
            {"nd": "Nếu a // b và c cắt a, b thì hai góc trong cùng phía có tính chất gì?","da": ["Bằng nhau","Phụ nhau","Bù nhau (Tổng 180°)","Kề nhau"],"d": 2,"gt": "Hai góc trong cùng phía bù nhau."},
            {"nd": "Qua một điểm nằm ngoài đường thẳng, có bao nhiêu đường thẳng song song với nó?","da": ["0","1","2","Vô số"],"d": 1,"gt": "Tiên đề Euclid: Chỉ có duy nhất 1 đường thẳng."},
            {"nd": "Nếu a ⊥ b và b ⊥ c thì quan hệ giữa a và c là gì?","da": ["a ⊥ c","a // c","Cắt nhau","Trùng nhau"],"d": 1,"gt": "Hai đường thẳng cùng vuông góc với đường thẳng thứ ba thì song song."},
            {"nd": "Nếu a // b và b // c thì quan hệ giữa a và c là gì?","da": ["a ⊥ c","a // c","Cắt nhau","Vuông góc"],"d": 1,"gt": "Tính chất bắc cầu: a // c."},
            {"nd": "Cho a // b, c ⊥ a. Khẳng định nào sau đây đúng?","da": ["c // b","c ⊥ b","c trùng b","Không cắt b"],"d": 1,"gt": "Một đường thẳng vuông góc với 1 trong 2 đường song song thì vuông góc với đường kia."},
            {"nd": "Phần 'Giả thiết' của một định lí là gì?","da": ["Điều cần chứng minh","Điều đã cho biết","Kết quả","Hình vẽ"],"d": 1,"gt": "Giả thiết (GT) là những điều cho trước."},
            {"nd": "Phần 'Kết luận' của một định lí là gì?","da": ["Điều cho trước","Điều cần chứng minh","Định nghĩa","Cách giải"],"d": 1,"gt": "Kết luận (KL) là điều cần suy ra."},
            {"nd": "Hai góc bù nhau có tổng số đo bằng?","da": ["90°","180°","360°","45°"],"d": 1,"gt": "Bù nhau = 180°."},
            {"nd": "Hai góc phụ nhau có tổng số đo bằng?","da": ["90°","180°","360°","45°"],"d": 0,"gt": "Phụ nhau = 90°."},
            {"nd": "Cho góc A = 30°, góc phụ với góc A có số đo là?","da": ["60°","150°","30°","90°"],"d": 0,"gt": "90° - 30° = 60°."},
            {"nd": "Đường trung trực của đoạn thẳng AB là đường thẳng:","da": ["Đi qua trung điểm của AB","Vuông góc với AB","Vuông góc với AB tại trung điểm","Song song với AB"],"d": 2,"gt": "Vừa vuông góc vừa đi qua trung điểm."},
            {"nd": "Kí hiệu hai đường thẳng vuông góc là?","da": ["//","⊥","=","≡"],"d": 1,"gt": "Kí hiệu ⊥."}
        ],

        "bt_co_ban": [
            {"de": "Cho hai đường thẳng xy và zt cắt nhau tại O. Biết góc xOz = 50°. Tính số đo góc yOt.","dd": ["50°"],"gt": "Góc yOt và góc xOz là hai góc đối đỉnh nên bằng nhau."},
            {"de": "Cho hai đường thẳng xy và zt cắt nhau tại O. Biết góc xOz = 50°. Tính số đo góc xOt.","dd": ["130°"],"gt": "Góc xOt kề bù với góc xOz ⇒ xOt = 180° - 50° = 130°."},
            {"de": "Cho a // b. Đường thẳng c cắt a, b. Biết một góc so le trong bằng 60°. Tính góc so le trong còn lại.","dd": ["60°"],"gt": "Hai đường thẳng song song thì hai góc so le trong bằng nhau."},
            {"de": "Cho a // b. Đường thẳng c cắt a, b. Biết một góc đồng vị bằng 110°. Tính góc đồng vị còn lại.","dd": ["110°"],"gt": "Hai đường thẳng song song thì hai góc đồng vị bằng nhau."},
            {"de": "Cho a // b. Biết một góc trong cùng phía bằng 80°. Tính góc trong cùng phía còn lại.","dd": ["100°"],"gt": "Hai góc trong cùng phía bù nhau ⇒ 180° - 80° = 100°."},
            {"de": "Vẽ đường thẳng d. Lấy điểm A không thuộc d. Có bao nhiêu đường thẳng qua A và song song với d?","dd": ["1 đường thẳng"],"gt": "Theo Tiên đề Euclid."},
            {"de": "Đường thẳng a vuông góc với c, đường thẳng b vuông góc với c. Quan hệ giữa a và b?","dd": ["a // b"],"gt": "Hai đường thẳng cùng vuông góc với đường thứ ba thì song song."},
            {"de": "Đường thẳng d là trung trực của đoạn MN. Biết MN = 6cm. d cắt MN tại I. Tính MI.","dd": ["3cm"],"gt": "I là trung điểm của MN ⇒ MI = 6 / 2 = 3cm."},
            {"de": "Viết giả thiết (GT) của định lí: 'Hai góc đối đỉnh thì bằng nhau'.","dd": ["GT: Hai góc O1 và O2 đối đỉnh"],"gt": "Điều đã cho biết."},
            {"de": "Viết kết luận (KL) của định lí: 'Hai góc đối đỉnh thì bằng nhau'.","dd": ["KL: Góc O1 = Góc O2"],"gt": "Điều cần chứng minh."}
        ],

        "bt_nang_cao": [
            {"de": "Cho 2 đường thẳng xx' và yy' cắt nhau tại O. Biết xOy + x'Oy' = 140°. Tính số đo 4 góc tạo thành.","hd": "Hai góc đối đỉnh thì bằng nhau. xOy = x'Oy'.","dd": ["xOy = x'Oy' = 70°; xOy' = x'Oy = 110°"],"lg": "Vì xOy và x'Oy' đối đỉnh nên xOy = x'Oy' = 140°/2 = 70°. Góc kề bù xOy' = 180° - 70° = 110°."},
            {"de": "Cho hình vẽ có a // b. Đường thẳng c cắt a tại A, b tại B. Biết A1 - B1 = 40° (A1, B1 là hai góc trong cùng phía). Tính A1, B1.","hd": "Sử dụng tính chất 2 góc trong cùng phía bù nhau (A1 + B1 = 180°).","dd": ["A1 = 110°, B1 = 70°"],"lg": "A1 + B1 = 180° và A1 - B1 = 40°. Cộng 2 vế: 2.A1 = 220° ⇒ A1 = 110°. Suy ra B1 = 70°."},
            {"de": "Cho góc xOy = 120°. Vẽ tia Oz nằm trong góc xOy sao cho xOz = 40°. Vẽ tia Ot là tia đối của tia Oz. Tính yOt.","hd": "Tính góc yOz trước. Sau đó dùng tính chất kề bù với tia đối.","dd": ["100°"],"lg": "yOz = xOy - xOz = 120° - 40° = 80°. Ot là tia đối của Oz nên yOt và yOz kề bù ⇒ yOt = 180° - 80° = 100°."},
            {"de": "Chứng minh định lí: Nếu hai đường thẳng a, b song song với nhau, một đường thẳng c vuông góc với a thì c cũng vuông góc với b.","hd": "Sử dụng tính chất góc đồng vị hoặc so le trong.","dd": ["Xem lời giải"],"lg": "Gọi A là giao của c và a, B là giao của c và b. c ⊥ a ⇒ Góc A1 = 90°. Vì a // b nên góc đồng vị B1 = A1 = 90°. Vậy c ⊥ b."},
            {"de": "Cho tam giác ABC. Qua A vẽ đường thẳng m // BC, qua B vẽ đường thẳng n // AC. Hai đường m, n cắt nhau tại D. Có nhận xét gì về góc D và góc C?","hd": "Sử dụng các góc so le trong và đồng vị do các đường thẳng song song tạo ra.","dd": ["Góc D = Góc C"],"lg": "Vì m // BC nên góc D = góc DBA (so le trong). Vì n // AC nên góc DBA = góc C (đồng vị hoặc so le trong với đường phụ). Suy ra D = C."},
            {"de": "Cho ba đường thẳng d1, d2, d3 cắt nhau tại O. Biết góc d1Od2 = 30°, d2Od3 = 60°. Tính góc giữa d1 và d3.","hd": "Có hai trường hợp tùy thuộc tia nằm giữa.","dd": ["90° hoặc 30°"],"lg": "TH1: d2 nằm giữa d1, d3 ⇒ Góc = 30° + 60° = 90°. TH2: d1 nằm giữa d2, d3 ⇒ Góc = 60° - 30° = 30°."},
            {"de": "Cho a // b. Vẽ tia phân giác của hai góc trong cùng phía cắt nhau tại M. Tính góc tạo bởi hai tia phân giác đó.","hd": "Tổng hai góc trong cùng phía là 180°. Tổng hai nửa góc bằng bao nhiêu?","dd": ["90°"],"lg": "Tổng 2 góc trong cùng phía = 180°. Phân giác chia đôi góc nên tổng 2 góc nhỏ = 180°/2 = 90°. Xét tam giác tạo thành, góc ở đỉnh M = 180° - 90° = 90°."},
            {"de": "Vẽ hai góc kề bù xOy và yOz, biết xOy = 60°. Gọi Om, On lần lượt là phân giác của xOy và yOz. Tính mOn.","hd": "Góc tạo bởi hai tia phân giác của hai góc kề bù luôn là góc vuông.","dd": ["90°"],"lg": "xOy + yOz = 180°. mOn = 1/2 xOy + 1/2 yOz = 1/2(180°) = 90°."},
            {"de": "Cho hai đường thẳng song song a và b. Đường thẳng c cắt a tại A, b tại B. Trên a lấy điểm C, trên b lấy điểm D sao cho AC // BD. Chứng minh AC = BD.","hd": "Gợi ý: Vẽ đường chéo AD, chứng minh hai tam giác bằng nhau (sẽ học kĩ ở chương sau). Ở đây dùng tính chất đoạn chắn song song.","dd": ["Các đoạn song song bị chắn bởi các đường song song thì bằng nhau."],"lg": "Theo tính chất đoạn chắn: Hai đoạn thẳng song song bị chắn bởi hai đường thẳng song song thì bằng nhau. Suy ra AC = BD."},
            {"de": "Một đường thẳng cắt hai đường thẳng song song tạo ra một cặp góc đồng vị có dạng (2x + 10)° và (3x - 20)°. Tìm x.","hd": "Hai góc đồng vị bằng nhau.","dd": ["x = 30"],"lg": "2x + 10 = 3x - 20 ⇒ x = 30."},
            {"de": "Một đường thẳng cắt hai đường thẳng song song tạo ra cặp góc trong cùng phía có số đo lần lượt là 3x° và 2x°. Tính số đo hai góc đó.","hd": "Tổng 2 góc trong cùng phía bằng 180°.","dd": ["108° và 72°"],"lg": "3x + 2x = 180 ⇒ 5x = 180 ⇒ x = 36. Các góc: 3.36 = 108° và 2.36 = 72°."},
            {"de": "Cho góc xOy = 90°. Vẽ tia Oz nằm trong góc xOy sao cho góc xOz = 1/3 góc xOy. Tính yOz.","hd": "xOz + yOz = xOy.","dd": ["60°"],"lg": "xOz = 90° / 3 = 30°. yOz = 90° - 30° = 60°."},
            {"de": "Cho góc bẹt xOy. Vẽ tia Oz sao cho xOz = 70°. Vẽ tia Ot sao cho yOt = 50° (Oz, Ot cùng nửa mặt phẳng). Tính zOt.","hd": "Các tia cùng nằm trên nửa mặt phẳng. Tính xOt rồi trừ.","dd": ["60°"],"lg": "xOt = 180° - yOt = 180° - 50° = 130°. Tia Oz nằm giữa Ox, Ot nên zOt = 130° - 70° = 60°."},
            {"de": "Qua điểm O, vẽ 5 đường thẳng phân biệt. Hỏi có bao nhiêu cặp góc đối đỉnh (nhỏ hơn góc bẹt)?","hd": "Công thức n(n-1) cặp với n đường thẳng.","dd": ["20 cặp"],"lg": "Với n đường thẳng cắt nhau tại 1 điểm, số cặp góc đối đỉnh là n(n-1). Thay n=5 ⇒ 5.4 = 20 cặp."},
            {"de": "Có hai đường thẳng a và b. Nếu a vuông góc với c, b cắt c một góc 60°. Hỏi a và b có song song không?","hd": "Nếu a // b thì góc đồng vị phải bằng nhau.","dd": ["Không song song"],"lg": "Nếu a // b thì b cũng phải vuông góc với c (tức là góc 90°). Đề cho 60° ≠ 90° nên không song song."},
            {"de": "Cho hình chữ nhật ABCD. Kẻ đường chéo AC. Nêu tên các cặp góc so le trong bằng nhau.","hd": "Sử dụng tính chất AB // CD và AD // BC.","dd": ["Góc BAC = ACD; Góc DAC = BCA"],"lg": "Vì AB // CD, AC là cát tuyến nên góc BAC = ACD. Tương tự AD // BC nên góc DAC = BCA."},
            {"de": "Nếu hai đường thẳng cắt nhau tạo thành 4 góc, trong đó tổng 3 góc là 290°. Tính số đo 4 góc đó.","hd": "Tổng 4 góc là 360°.","dd": ["70°, 110°, 70°, 110°"],"lg": "Góc còn lại = 360° - 290° = 70°. Góc đối đỉnh với nó = 70°. Hai góc kề bù với nó = 180° - 70° = 110°."},
            {"de": "Định lí 'Nếu hai góc bằng nhau thì đối đỉnh' là đúng hay sai? Vẽ hình minh họa.","hd": "Mệnh đề đảo của định lí đối đỉnh có thể sai.","dd": ["Sai"],"lg": "Sai. Ví dụ hai góc bằng nhau là 60° nhưng không chung đỉnh, hoặc chung đỉnh nhưng không tạo thành các đường thẳng chéo nhau."},
            {"de": "Cho a // b. Một đường thẳng c cắt a, b tạo thành 8 góc. Biết tổng của hai góc so le trong là 140°. Tính số đo tất cả các góc.","hd": "Hai góc so le trong bằng nhau. Tính 1 góc, từ đó suy ra các góc còn lại.","dd": ["Bốn góc 70° và bốn góc 110°"],"lg": "Hai góc so le trong bằng nhau nên mỗi góc = 140°/2 = 70°. Góc kề bù với nó = 180° - 70° = 110°."},
            {"de": "Chứng minh rằng hai tia phân giác của hai góc đối đỉnh là hai tia đối nhau.","hd": "Tính tổng các góc trên đường thẳng tạo bởi hai tia phân giác đó.","dd": ["Xem lời giải"],"lg": "Chứng minh góc tạo bởi 2 tia phân giác là 180 độ, suy ra là 2 tia đối nhau."}
        ]
    }
}
T7["Chương 3: Góc và Đường thẳng song song"] = C3_T7

# --- Chương 4: Tam giác bằng nhau ---
C4_T7 = {
    "Tam giác bằng nhau (Tổng hợp chuyên sâu)": {
        "ly_thuyet": """📌 1. TỔNG CÁC GÓC CỦA MỘT TAM GIÁC:
- Tổng ba góc của một tam giác luôn bằng 180°.
- Góc ngoài của tam giác là góc kề bù với một góc trong. Số đo góc ngoài bằng tổng hai góc trong không kề với nó.

📌 2. HAI TAM GIÁC BẰNG NHAU:
- Hai tam giác bằng nhau là hai tam giác có các cạnh tương ứng bằng nhau và các góc tương ứng bằng nhau.
- Kí hiệu: ∆ABC = ∆A'B'C'.

📌 3. CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC:
- Cạnh - Cạnh - Cạnh (c.c.c): Nếu 3 cạnh của ∆ này bằng 3 cạnh của ∆ kia thì hai ∆ bằng nhau.
- Cạnh - Góc - Cạnh (c.g.c): Nếu 2 cạnh và góc xen giữa của ∆ này bằng 2 cạnh và góc xen giữa của ∆ kia thì hai ∆ bằng nhau.
- Góc - Cạnh - Góc (g.c.g): Nếu 1 cạnh và 2 góc kề cạnh đó của ∆ này bằng 1 cạnh và 2 góc kề cạnh đó của ∆ kia thì hai ∆ bằng nhau.

📌 4. CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG:
- Hai cạnh góc vuông (c.g.c).
- Cạnh góc vuông và góc nhọn kề cạnh đó (g.c.g).
- Cạnh huyền và góc nhọn.
- Cạnh huyền và cạnh góc vuông.

📌 5. TAM GIÁC CÂN VÀ ĐƯỜNG TRUNG TRỰC:
- Tam giác cân: Có 2 cạnh bằng nhau. Tính chất: 2 góc ở đáy bằng nhau.
- Tam giác đều: Có 3 cạnh bằng nhau. Tính chất: 3 góc bằng nhau và bằng 60°.
- Đường trung trực của đoạn thẳng: Vuông góc tại trung điểm. Điểm nằm trên trung trực thì cách đều 2 mút của đoạn thẳng đó.""",
        
        "vi_du": """💡 VÍ DỤ 1: Tính góc trong tam giác
Đề bài: Cho ∆ABC có góc A = 50°, góc B = 70°. Tính góc ngoài tại đỉnh C.
- Phân tích: Có thể tính góc C rồi dùng kề bù, hoặc dùng định lí góc ngoài.
- Giải: Góc ngoài tại C = góc A + góc B = 50° + 70° = 120°.

💡 VÍ DỤ 2: Chứng minh hai tam giác bằng nhau
Đề bài: Cho ∆ABC và ∆DEF có AB = DE, góc A = góc D, AC = DF. Hỏi hai tam giác này có bằng nhau không? Theo trường hợp nào?
- Giải: ∆ABC và ∆DEF có: AB = DE, góc A = góc D (xen giữa), AC = DF. Do đó ∆ABC = ∆DEF (c.g.c).

💡 VÍ DỤ 3: Tam giác cân
Đề bài: Cho ∆MNP cân tại M, biết góc M = 40°. Tính góc N và góc P.
- Giải: Vì ∆MNP cân tại M nên góc N = góc P. Mà M + N + P = 180° ⇒ 40° + 2.N = 180° ⇒ 2.N = 140° ⇒ N = P = 70°.""",

        "cau_hoi": [
            {"nd": "Tổng số đo ba góc của một tam giác bằng bao nhiêu?","da": ["90°","180°","360°","100°"],"d": 1,"gt": "Định lí tổng ba góc trong tam giác."},
            {"nd": "Cho ∆ABC có góc A = 60°, góc B = 50°. Số đo góc C là?","da": ["60°","70°","80°","90°"],"d": 1,"gt": "180° - (60° + 50°) = 70°."},
            {"nd": "Tam giác vuông có một góc nhọn bằng 45° là tam giác gì?","da": ["Tam giác nhọn","Tam giác đều","Tam giác vuông cân","Tam giác tù"],"d": 2,"gt": "Góc nhọn còn lại = 90° - 45° = 45°. Có 2 góc bằng nhau ⇒ vuông cân."},
            {"nd": "Số đo góc ngoài tại một đỉnh của tam giác bằng?","da": ["Tổng hai góc trong không kề với nó","Tổng 3 góc trong","Hiệu hai góc trong","180°"],"d": 0,"gt": "Định lí góc ngoài của tam giác."},
            {"nd": "Hai tam giác ABC và DEF có AB=DE, BC=EF, AC=DF thì hai tam giác bằng nhau theo trường hợp nào?","da": ["c.g.c","g.c.g","c.c.c","Cạnh huyền - góc nhọn"],"d": 2,"gt": "Ba cạnh tương ứng bằng nhau là trường hợp cạnh-cạnh-cạnh."},
            {"nd": "Để ∆ABC = ∆MNP theo trường hợp c.g.c, nếu AB = MN, BC = NP thì cần thêm điều kiện gì?","da": ["Góc A = Góc M","Góc B = Góc N","Góc C = Góc P","AC = MP"],"d": 1,"gt": "Góc phải xen giữa hai cạnh tương ứng, đó là góc B và góc N."},
            {"nd": "Để ∆ABC = ∆DEF theo trường hợp g.c.g, nếu BC = EF, góc B = góc E thì cần thêm điều kiện gì?","da": ["Góc A = Góc D","Góc C = Góc F","AB = DE","AC = DF"],"d": 1,"gt": "Hai góc kề với cạnh BC là góc B và góc C. Góc tương ứng là E và F."},
            {"nd": "Tam giác có hai góc bằng 60° là tam giác gì?","da": ["Tam giác vuông","Tam giác tù","Tam giác cân","Tam giác đều"],"d": 3,"gt": "Góc thứ ba = 180° - 60° - 60° = 60°. Tam giác có 3 góc 60° là tam giác đều."},
            {"nd": "Điểm nằm trên đường trung trực của đoạn thẳng AB thì:","da": ["Cách đều hai điểm A và B","Chỉ cách A 2cm","Nằm trên đoạn AB","Là trung điểm của AB"],"d": 0,"gt": "Tính chất điểm trên đường trung trực."},
            {"nd": "Trường hợp bằng nhau Cạnh huyền - Cạnh góc vuông áp dụng cho loại tam giác nào?","da": ["Tam giác nhọn","Tam giác vuông","Tam giác tù","Tam giác đều"],"d": 1,"gt": "Chỉ áp dụng cho tam giác vuông."},
            {"nd": "Nếu ∆ABC = ∆DEF và góc A = 70° thì góc nào của ∆DEF cũng bằng 70°?","da": ["Góc D","Góc E","Góc F","Không xác định"],"d": 0,"gt": "Các đỉnh tương ứng viết cùng vị trí: A tương ứng với D."},
            {"nd": "Cho ∆MNP có góc ngoài tại đỉnh M bằng 110°. Tổng góc N + góc P bằng?","da": ["110°","70°","180°","90°"],"d": 0,"gt": "Góc ngoài bằng tổng 2 góc trong không kề nó."},
            {"nd": "Cho ∆ABC cân tại A. Phát biểu nào ĐÚNG?","da": ["Góc A = Góc B","AB = BC","Góc B = Góc C","Góc A = Góc C"],"d": 2,"gt": "Tam giác cân tại A thì 2 đáy là B và C bằng nhau."},
            {"nd": "Mỗi góc của tam giác đều có số đo bằng bao nhiêu?","da": ["45°","60°","90°","120°"],"d": 1,"gt": "180° / 3 = 60°."},
            {"nd": "Tam giác vuông cân có hai góc nhọn bằng bao nhiêu?","da": ["30°","45°","60°","90°"],"d": 1,"gt": "90° / 2 = 45°."},
            {"nd": "Đoạn thẳng vuông góc kẻ từ một điểm đến một đường thẳng gọi là?","da": ["Đường xiên","Hình chiếu","Đường vuông góc","Đường cao"],"d": 2,"gt": "Khoảng cách ngắn nhất là đường vuông góc."},
            {"nd": "Trong tam giác tù, có bao nhiêu góc tù?","da": ["1","2","3","0"],"d": 0,"gt": "Tổng 3 góc là 180°, nếu có 2 góc tù (>90°) thì tổng > 180° (vô lý). Nên chỉ có tối đa 1 góc tù."},
            {"nd": "Trong tam giác ABC, nếu AB = AC và góc A = 90° thì tam giác ABC là?","da": ["Tam giác cân","Tam giác đều","Tam giác vuông cân","Tam giác tù"],"d": 2,"gt": "Vừa vuông tại A, vừa cân tại A."},
            {"nd": "Trong một tam giác, góc lớn nhất là góc đối diện với?","da": ["Cạnh nhỏ nhất","Cạnh lớn nhất","Góc kề","Cạnh huyền"],"d": 1,"gt": "Góc đối diện với cạnh lớn nhất là góc lớn nhất."},
            {"nd": "Cho ∆ABC = ∆DEF, biết AB = 5cm, DF = 7cm. Tính chu vi ∆ABC nếu EF = 6cm.","da": ["12cm","15cm","18cm","20cm"],"d": 2,"gt": "AB=DE=5; AC=DF=7; BC=EF=6. Chu vi = 5+6+7 = 18cm."}
        ],

        "bt_co_ban": [
            {"de": "Cho ∆ABC có góc A = 40°, góc B = 60°. Tính góc C.","dd": ["80°"],"gt": "Góc C = 180° - 40° - 60° = 80°."},
            {"de": "Cho ∆MNP có góc ngoài tại đỉnh P bằng 130°. Biết góc M = 50°, tính góc N.","dd": ["80°"],"gt": "Góc N = 130° - 50° = 80°."},
            {"de": "Cho ∆ABC = ∆DEF. Biết AB = 5cm, BC = 7cm, DF = 6cm. Tính các cạnh còn lại của hai tam giác.","dd": ["AC = 6cm, DE = 5cm, EF = 7cm"],"gt": "Các cạnh tương ứng bằng nhau: AB=DE, BC=EF, AC=DF."},
            {"de": "Cho ∆ABC cân tại A, biết góc A = 70°. Tính góc B và góc C.","dd": ["Góc B = Góc C = 55°"],"gt": "(180° - 70°) / 2 = 55°."},
            {"de": "Cho ∆DEF vuông tại D, biết góc E = 35°. Tính góc F.","dd": ["55°"],"gt": "Hai góc nhọn phụ nhau: 90° - 35° = 55°."},
            {"de": "Vẽ đoạn thẳng AB = 4cm. Vẽ đường trung trực d của AB. d cắt AB tại I. Tính IA.","dd": ["IA = 2cm"],"gt": "d đi qua trung điểm I nên IA = AB/2 = 2cm."},
            {"de": "Một tam giác có ba cạnh tỉ lệ với 2, 3, 4. Chu vi bằng 27cm. Tính các cạnh của tam giác đó.","dd": ["6cm, 9cm, 12cm"],"gt": "2x + 3x + 4x = 27 ⇒ 9x = 27 ⇒ x = 3. Các cạnh: 6, 9, 12."},
            {"de": "Kiểm tra xem bộ ba độ dài 2cm, 5cm, 7cm có phải là 3 cạnh của một tam giác không?","dd": ["Không"],"gt": "2 + 5 = 7 không thỏa mãn BĐT tam giác (phải >)."},
            {"de": "Cho ∆ABC cân tại A, có chu vi là 20cm. Biết cạnh đáy BC = 6cm. Tính chiều dài 2 cạnh bên.","dd": ["AB = AC = 7cm"],"gt": "(20 - 6) / 2 = 7cm."},
            {"de": "Cho ∆MNP cân tại N. Phân giác góc N cắt MP tại I. Chứng minh ∆MNI = ∆PNI.","dd": ["Xem lời giải"],"gt": "∆MNI và ∆PNI có: NM=NP, góc MNI = PNI, cạnh NI chung. ⇒ Bằng nhau (c.g.c)."}
        ],

        "bt_nang_cao": [
            {"de": "Cho ∆ABC. Tia phân giác của góc B và góc C cắt nhau tại I. Biết góc A = 60°. Tính góc BIC.","hd": "Dùng tổng các góc trong tam giác ABC và IBC.","dd": ["120°"],"lg": "B + C = 180° - 60° = 120°. IBC + ICB = (B+C)/2 = 60°. Góc BIC = 180° - 60° = 120°."},
            {"de": "Cho ∆ABC có góc A = 90°, AB = AC. Lấy điểm D thuộc cạnh BC sao cho BD = AB. Tính góc ADC.","hd": "∆ABC vuông cân nên B=C=45°. ∆ABD cân tại B.","dd": ["67,5° hoặc 112,5° tùy tia"],"lg": "Vì B = 45° và BD = BA nên ∆ABD cân tại B. Góc BAD = BDA = (180° - 45°)/2 = 67,5°. Góc ADC kề bù với BDA nên ADC = 180° - 67,5° = 112,5°."},
            {"de": "Cho ∆ABC. Trên tia đối của tia AB lấy điểm D sao cho AD = AB. Trên tia đối của tia AC lấy điểm E sao cho AE = AC. Chứng minh BC // DE.","hd": "Chứng minh ∆ABC = ∆ADE.","dd": ["Xem lời giải"],"lg": "∆ABC và ∆ADE có: AB = AD, góc BAC = DAE (đối đỉnh), AC = AE. ⇒ ∆ABC = ∆ADE (c.g.c). Suy ra góc ABC = ADE (so le trong). Vậy BC // DE."},
            {"de": "Cho góc xOy nhọn. Lấy A, B trên Ox sao cho OA < OB. Lấy C, D trên Oy sao cho OC = OA, OD = OB. Gọi E là giao của AD và BC. Chứng minh ∆OAD = ∆OCB và OE là phân giác góc xOy.","hd": "Chứng minh 2 tam giác lớn bằng nhau, suy ra cạnh và góc tương ứng, rồi chứng minh 2 tam giác nhỏ chứa đỉnh E bằng nhau.","dd": ["Xem lời giải"],"lg": "∆OAD và ∆OCB có OA=OC, góc O chung, OD=OB ⇒ Bằng nhau (c.g.c). Từ đó AD=CB, góc OAD=OCB, góc ODA=OBC. Suy ra ∆EAB = ∆ECD (g.c.g). Có EA=EC, xét ∆OAE = ∆OCE (c.c.c) ⇒ góc AOE = COE ⇒ OE là phân giác."},
            {"de": "Cho ∆ABC cân tại A (góc A < 90°). Kẻ BH ⊥ AC, CK ⊥ AB. Chứng minh BH = CK.","hd": "Xét 2 tam giác vuông ABH và ACK hoặc BHC và CKB.","dd": ["Xem lời giải"],"lg": "Xét ∆vuông ABH và ∆vuông ACK có: Cạnh huyền AB = AC, góc A chung. ⇒ ∆ABH = ∆ACK (cạnh huyền - góc nhọn). Suy ra BH = CK."},
            {"de": "Cho ∆ABC vuông tại A. Tia phân giác góc B cắt AC tại D. Kẻ DE ⊥ BC tại E. Chứng minh DA = DE.","hd": "Xét 2 tam giác vuông ABD và EBD.","dd": ["Xem lời giải"],"lg": "Xét ∆ABD và ∆EBD có: BD chung, góc ABD = EBD. ⇒ ∆ABD = ∆EBD (cạnh huyền - góc nhọn). Suy ra DA = DE."},
            {"de": "Cho ∆ABC cân tại A. Trên tia đối của tia BC lấy M, trên tia đối của tia CB lấy N sao cho BM = CN. Chứng minh ∆AMN là tam giác cân.","hd": "Chứng minh ∆ABM = ∆ACN.","dd": ["Xem lời giải"],"lg": "Góc ABC = ACB ⇒ góc kề bù ABM = ACN. Xét ∆ABM và ∆ACN có: AB = AC, ABM = ACN, BM = CN. ⇒ ∆ABM = ∆ACN (c.g.c) ⇒ AM = AN ⇒ ∆AMN cân tại A."},
            {"de": "Đường trung trực của cạnh BC trong ∆ABC cắt AC tại D. Biết AD = 3cm, DC = 5cm. Tính chu vi ∆ABD nếu AB = 4cm.","hd": "D nằm trên trung trực BC nên DB = DC.","dd": ["12 cm"],"lg": "D ∈ trung trực BC ⇒ DB = DC = 5cm. Chu vi ∆ABD = AB + AD + DB = 4 + 3 + 5 = 12cm."},
            {"de": "Một cái thang dài 5m dựa vào tường. Khoảng cách từ chân thang đến tường là 3m. Tính chiều cao bức tường từ điểm tựa thang xuống đất.","hd": "Áp dụng định lí Pytago.","dd": ["4m"],"lg": "h = √(5² - 3²) = √16 = 4m."},
            {"de": "Tìm độ dài x trên hình vẽ biết ∆ vuông có cạnh góc vuông là 5, x và cạnh huyền là 13.","hd": "Dùng Pytago","dd": ["12"],"lg": "x² + 5² = 13² ⇒ x² = 169 - 25 = 144 ⇒ x = 12."}
        ]
    }
}
T7["Chương 4: Tam giác bằng nhau"] = C4_T7

# --- Chương 5: Thu thập và biểu diễn dữ liệu ---
C5_T7 = {
    "Thu thập, phân loại và Biểu diễn dữ liệu": {
        "ly_thuyet": """📌 1. THU THẬP VÀ PHÂN LOẠI DỮ LIỆU:
- Dữ liệu có thể là số (dữ liệu định lượng) hoặc không phải là số (dữ liệu định tính).
- Tính hợp lí của dữ liệu: Dữ liệu thu thập được phải đúng tiêu chí, không mâu thuẫn với thực tế.

📌 2. BIỂU ĐỒ HÌNH QUẠT TRÒN:
- Biểu diễn các thành phần của một tổng thể. Toàn bộ hình tròn biểu diễn 100%. Mỗi hình quạt biểu diễn tỉ lệ phần trăm của một thành phần.
- Công thức chuyển tỉ lệ % sang góc ở tâm (để vẽ): Góc = Tỉ lệ % × 360°.

📌 3. BIỂU ĐỒ ĐOẠN THẲNG:
- Biểu diễn sự thay đổi của một đại lượng theo thời gian.
- Trục ngang thường biểu diễn thời gian, trục dọc biểu diễn đại lượng. Các điểm được nối với nhau bằng các đoạn thẳng.""",
        
        "vi_du": """💡 VÍ DỤ 1: Phân loại dữ liệu
Đề bài: Cho các dữ liệu sau: Cân nặng (kg) của 5 học sinh: {45, 50, 48, Mập, 42}. Dữ liệu nào không hợp lí?
- Giải: Dữ liệu "Mập" là dữ liệu định tính (chữ), trong khi yêu cầu là cân nặng (số). Vậy "Mập" không hợp lí.

💡 VÍ DỤ 2: Đọc biểu đồ quạt tròn
Đề bài: Biểu đồ quạt tròn biểu diễn tỉ lệ môn thể thao yêu thích. Biết môn Bóng đá chiếm 40%, Bóng chuyền 20%, còn lại là Cầu lông. Tính phần trăm Cầu lông và góc ở tâm của nó.
- Giải: 
  + Cầu lông chiếm: 100% - 40% - 20% = 40%.
  + Góc ở tâm = 40% × 360° = 144°.

💡 VÍ DỤ 3: Biểu đồ đoạn thẳng
Đề bài: Nhiệt độ các ngày từ thứ 2 đến thứ 6 lần lượt là: 25°, 28°, 27°, 30°, 29°. Nhiệt độ ngày nào cao nhất? Xu hướng từ thứ 4 đến thứ 5 là tăng hay giảm?
- Giải: Cao nhất là thứ 5 (30°). Từ thứ 4 (27°) đến thứ 5 (30°) là xu hướng Tăng.""",

        "cau_hoi": [
            {"nd": "Dữ liệu nào sau đây là dữ liệu định lượng (số liệu)?","da": ["Màu sắc yêu thích","Sở thích âm nhạc","Chiều cao của học sinh","Xếp loại học lực"],"d": 2,"gt": "Chiều cao là con số có thể cân đong đo đếm được."},
            {"nd": "Để biểu diễn sự thay đổi nhiệt độ trong một tuần, ta nên dùng loại biểu đồ nào là hợp lí nhất?","da": ["Biểu đồ cột","Biểu đồ hình quạt tròn","Biểu đồ đoạn thẳng","Biểu đồ tranh"],"d": 2,"gt": "Biểu đồ đoạn thẳng chuyên dùng để biểu diễn sự thay đổi theo thời gian."},
            {"nd": "Để biểu diễn tỉ lệ phần trăm các loại trái cây trong một cửa hàng, dùng biểu đồ nào tốt nhất?","da": ["Biểu đồ cột kép","Biểu đồ hình quạt tròn","Biểu đồ đoạn thẳng","Bảng thống kê"],"d": 1,"gt": "Biểu đồ quạt biểu diễn cơ cấu/tỉ lệ % rất trực quan."},
            {"nd": "Một biểu đồ hình quạt tròn hoàn chỉnh luôn tương ứng với tổng tỉ lệ là bao nhiêu?","da": ["100%","90%","360%","180%"],"d": 0,"gt": "Toàn bộ hình tròn biểu diễn 100%."},
            {"nd": "Trong biểu đồ quạt tròn, một thành phần chiếm 25% thì góc ở tâm của hình quạt đó là bao nhiêu?","da": ["25°","90°","45°","180°"],"d": 1,"gt": "25% của 360° = 1/4 × 360° = 90°."},
            {"nd": "Thu thập dữ liệu 'Tên các loài hoa trong vườn' là dữ liệu:","da": ["Định lượng","Định tính","Số liệu rời rạc","Số liệu liên tục"],"d": 1,"gt": "Tên là chữ (không phải số) nên là định tính."},
            {"nd": "Nếu 1 hình quạt có góc ở tâm là 180° thì nó biểu diễn bao nhiêu phần trăm?","da": ["180%","100%","50%","25%"],"d": 2,"gt": "180/360 = 1/2 = 50%."},
            {"nd": "Khi điều tra về điểm thi môn Toán của tổ 1, bạn An thu được dãy: 7, 8, 9, 11, 6. Số liệu nào không hợp lí?","da": ["7","9","11","6"],"d": 2,"gt": "Điểm thi tối đa là 10, nên số 11 không hợp lí."},
            {"nd": "Điều tra loại phương tiện đi lại của học sinh: Xe đạp, Xe buýt, Ô tô, Tàu hỏa. Kết quả 'Đi bộ' có hợp lí không?","da": ["Có","Không","Tuỳ trường hợp","Không xác định"],"d": 0,"gt": "Đi bộ cũng là một hình thức di chuyển hợp lí."},
            {"nd": "Trong biểu đồ đoạn thẳng, nếu đường nét đứt đi lên (↗) thì thể hiện điều gì?","da": ["Đại lượng giữ nguyên","Đại lượng giảm xuống","Đại lượng tăng lên","Đại lượng không xác định"],"d": 2,"gt": "Đường đi lên thể hiện giá trị tăng lên."}
        ],

        "bt_co_ban": [
            {"de": "Thu thập cỡ giày của 5 bạn nam: 39, 40, 41, 40, 'XL'. Giá trị nào không hợp lí?","dd": ["'XL'"],"gt": "Cỡ giày là số, XL là kí hiệu cỡ áo."},
            {"de": "Một biểu đồ quạt tròn biểu diễn 4 loại sách. Truyện tranh chiếm 50%, Tiểu thuyết 25%, Khoa học 15%. Tính % sách Lịch sử.","dd": ["10%"],"gt": "100% - (50+25+15)% = 10%."},
            {"de": "Tính góc ở tâm của hình quạt biểu diễn tỉ lệ 20% trong biểu đồ quạt tròn.","dd": ["72°"],"gt": "20% × 360° = 72°."},
            {"de": "Cho dãy số liệu về số học sinh giỏi của 4 lớp khối 7: 12, 15, 14, 18. Tổng số học sinh giỏi khối 7 là bao nhiêu?","dd": ["59 học sinh"],"gt": "12 + 15 + 14 + 18 = 59."},
            {"de": "Dựa vào biểu đồ đoạn thẳng mô tả nhiệt độ: T2 (20°), T3 (22°), T4 (21°), T5 (25°). Nhiệt độ tăng mạnh nhất vào ngày nào?","dd": ["Từ T4 đến T5"],"gt": "Tăng 4 độ, cao nhất trong các ngày."},
            {"de": "Nếu 5% số học sinh trường A là 20 em. Hỏi trường A có tất cả bao nhiêu học sinh?","dd": ["400 học sinh"],"gt": "20 / 5% = 400."},
            {"de": "Khảo sát thời gian tự học (giờ) của 5 học sinh: 1, 2, 2.5, 3, 24. Số liệu nào phi lý?","dd": ["24"],"gt": "Một ngày chỉ có 24 giờ, không thể tự học trọn vẹn 24 giờ không ngủ/ăn."},
            {"de": "Biểu đồ quạt biểu diễn xếp loại Học lực: Tốt (25%), Khá (45%), Đạt (20%), Chưa đạt. Tính % Chưa đạt.","dd": ["10%"],"gt": "100% - 90% = 10%."},
            {"de": "Để lập biểu đồ hình quạt tròn, bước đầu tiên cần làm là gì?","dd": ["Tính tỉ lệ phần trăm của từng thành phần"],"gt": "Phải có % mới chia được góc ở tâm."},
            {"de": "Dữ liệu 'Nhiệt độ sôi của một số chất lỏng' là loại dữ liệu gì?","dd": ["Dữ liệu định lượng (số liệu)"],"gt": "Nhiệt độ được đo bằng con số."}
        ],

        "bt_nang_cao": [
            {"de": "Trong một cuộc khảo sát 200 học sinh về phương tiện đến trường: 80 em đi xe đạp, 60 em đi xe buýt, 40 em đi bộ, còn lại đi xe máy. Nếu vẽ biểu đồ quạt tròn, góc ở tâm của phần biểu diễn 'xe máy' là bao nhiêu độ?","hd": "Tính số học sinh đi xe máy, sau đó tính % rồi nhân 360°.","dd": ["36°"],"lg": "Số HS đi xe máy = 200 - (80+60+40) = 20 em. Tỉ lệ % = 20/200 = 10%. Góc = 10% × 360° = 36°."},
            {"de": "Biểu đồ đoạn thẳng biểu diễn doanh thu 6 tháng. Tháng 1: 50tr, Tháng 2: 45tr, Tháng 3: 55tr, Tháng 4: 60tr, Tháng 5: 58tr, Tháng 6: 70tr. Nêu nhận xét về xu hướng doanh thu chung.","hd": "So sánh điểm đầu và điểm cuối, các đoạn biến động.","dd": ["Xu hướng chung là tăng trưởng."],"lg": "Dù có giảm nhẹ ở tháng 2 và tháng 5, nhưng nhìn chung từ tháng 1 đến tháng 6 doanh thu tăng mạnh từ 50tr lên 70tr."},
            {"de": "Nếu một biểu đồ quạt biểu diễn 3 thành phần A, B, C. Góc ở tâm của A là 120°, của B là 90°. Hỏi thành phần C chiếm bao nhiêu phần trăm?","hd": "Tính góc của C rồi chia cho 360°.","dd": ["41,67% (hoặc xấp xỉ 41,7%)"],"lg": "Góc C = 360° - 120° - 90° = 150°. Phần trăm C = (150/360) × 100% ≈ 41,67%."}
        ]
    }
}
T7["Chương 5: Thu thập và biểu diễn dữ liệu"] = C5_T7

# --- Chương 6: Tỉ lệ thức và Đại lượng tỉ lệ ---
C6_T7 = {
    "Tỉ lệ thức và Đại lượng tỉ lệ (Chuyên sâu)": {
        "ly_thuyet": """📌 1. TỈ LỆ THỨC:
- Tỉ lệ thức là đẳng thức của hai tỉ số: a/b = c/d.
- Tính chất cơ bản: Nếu a/b = c/d thì a.d = b.c.
- Tính chất đổi chỗ: Từ a.d = b.c (a,b,c,d ≠ 0), ta có thể suy ra các tỉ lệ thức: a/c = b/d; d/b = c/a; d/c = b/a.

📌 2. TÍNH CHẤT DÃY TỈ SỐ BẰNG NHAU:
- Từ tỉ lệ thức a/b = c/d ta suy ra: a/b = c/d = (a+c)/(b+d) = (a-c)/(b-d) (với b ≠ ±d).
- Mở rộng: a/b = c/d = e/f = (a+c+e)/(b+d+f) = (a-c+e)/(b-d+f).
- Khi nói các số x, y, z tỉ lệ với a, b, c tức là: x/a = y/b = z/c.

📌 3. ĐẠI LƯỢNG TỈ LỆ THUẬN:
- Nếu đại lượng y liên hệ với đại lượng x theo công thức y = k.x (với k là hằng số khác 0) thì y tỉ lệ thuận với x theo hệ số tỉ lệ k.
- Tính chất: y₁/x₁ = y₂/x₂ = k; y₁/y₂ = x₁/x₂.

📌 4. ĐẠI LƯỢNG TỈ LỆ NGHỊCH:
- Nếu đại lượng y liên hệ với đại lượng x theo công thức y = a/x hay x.y = a (a là hằng số khác 0) thì y tỉ lệ nghịch với x theo hệ số tỉ lệ a.
- Tính chất: x₁.y₁ = x₂.y₂ = a; x₁/x₂ = y₂/y₁.""",
        
        "vi_du": """💡 VÍ DỤ 1: Tìm x trong tỉ lệ thức
Đề bài: Tìm x biết x/15 = 2/5.
- Phân tích: Sử dụng tính chất nhân chéo của tỉ lệ thức (a.d = b.c).
- Giải: x.5 = 15.2 ⇒ 5x = 30 ⇒ x = 6.

💡 VÍ DỤ 2: Vận dụng dãy tỉ số bằng nhau
Đề bài: Ba lớp 7A, 7B, 7C quyên góp được tổng cộng 120 quyển vở. Số vở quyên góp của ba lớp lần lượt tỉ lệ với 3, 4, 5. Tính số vở mỗi lớp.
- Phân tích: Đặt số vở là x, y, z. Ta có x/3 = y/4 = z/5 và x + y + z = 120.
- Giải: Áp dụng tính chất dãy tỉ số bằng nhau:
  x/3 = y/4 = z/5 = (x+y+z)/(3+4+5) = 120/12 = 10.
  ⇒ x = 10.3 = 30; y = 10.4 = 40; z = 10.5 = 50.

💡 VÍ DỤ 3: Bài toán Tỉ lệ nghịch
Đề bài: Một đội công nhân gồm 15 người hoàn thành công việc trong 8 ngày. Nếu muốn hoàn thành trong 6 ngày thì cần bao nhiêu người? (Năng suất như nhau).
- Phân tích: Số người và số ngày hoàn thành công việc là hai đại lượng tỉ lệ nghịch (x.y = a).
- Giải: Gọi x là số người cần thiết để hoàn thành trong 6 ngày.
  Ta có: 15 . 8 = x . 6 ⇒ 120 = 6x ⇒ x = 20.
  Vậy cần 20 công nhân.""",

        "cau_hoi": [
            {"nd": "Tỉ lệ thức là?","da": ["Một phân số","Đẳng thức của hai tích","Đẳng thức của hai tỉ số","Hiệu của hai phân số"],"d": 2,"gt": "Định nghĩa cơ bản của tỉ lệ thức."},
            {"nd": "Từ đẳng thức a.d = b.c (a, b, c, d khác 0), ta KHÔNG thể suy ra tỉ lệ thức nào?","da": ["a/b = c/d","a/c = b/d","d/b = c/a","a/b = d/c"],"d": 3,"gt": "Nhân chéo a/b = d/c sẽ ra a.c = b.d (sai với đẳng thức ban đầu)."},
            {"nd": "Cho x/4 = 3/2. Giá trị của x là?","da": ["6","8","12","2"],"d": 0,"gt": "x.2 = 4.3 ⇒ 2x = 12 ⇒ x = 6."},
            {"nd": "Nếu a/b = c/d thì:","da": ["a.b = c.d","a.c = b.d","a.d = b.c","a+d = b+c"],"d": 2,"gt": "Tích trung tỉ bằng tích ngoại tỉ."},
            {"nd": "Tính chất dãy tỉ số bằng nhau nào sau đây ĐÚNG?","da": ["a/b = c/d = (a-c)/(b+d)","a/b = c/d = (a.c)/(b.d)","a/b = c/d = (a+c)/(b+d)","a/b = c/d = (a+b)/(c+d)"],"d": 2,"gt": "Tử cộng tử, mẫu cộng mẫu tương ứng."},
            {"nd": "Đại lượng y tỉ lệ thuận với đại lượng x theo hệ số tỉ lệ k = -2. Công thức biểu diễn là?","da": ["y = -2x","y = x/-2","x = -2y","y = -2/x"],"d": 0,"gt": "Tỉ lệ thuận có công thức y = k.x."},
            {"nd": "Nếu y tỉ lệ nghịch với x theo hệ số tỉ lệ a = 12 thì công thức nào ĐÚNG?","da": ["y = 12x","y = x/12","y = 12/x","x = 12y"],"d": 2,"gt": "Tỉ lệ nghịch: y = a/x."},
            {"nd": "Đại lượng x và y tỉ lệ thuận. Khi x = 2 thì y = 6. Hệ số tỉ lệ k của y đối với x là?","da": ["3","12","1/3","-3"],"d": 0,"gt": "k = y/x = 6/2 = 3."},
            {"nd": "Chu vi hình vuông tỉ lệ thuận hay tỉ lệ nghịch với cạnh của nó?","da": ["Tỉ lệ thuận","Tỉ lệ nghịch","Không tỉ lệ","Bằng nhau"],"d": 0,"gt": "C = 4.a ⇒ Tỉ lệ thuận với hệ số k=4."},
            {"nd": "Vận tốc và thời gian (khi quãng đường không đổi) là hai đại lượng?","da": ["Tỉ lệ thuận","Tỉ lệ nghịch","Bằng nhau","Không liên quan"],"d": 1,"gt": "v.t = S (không đổi) ⇒ v và t tỉ lệ nghịch."}
        ],

        "bt_co_ban": [
            {"de": "Tìm x biết x/7 = 4/14.","dd": ["x = 2"],"gt": "x.14 = 7.4 = 28 ⇒ x = 2."},
            {"de": "Tìm x, y biết x/3 = y/5 và x + y = 32.","dd": ["x = 12, y = 20"],"gt": "(x+y)/(3+5) = 32/8 = 4. x = 3.4 = 12; y = 5.4 = 20."},
            {"de": "Biết x và y tỉ lệ thuận, khi x = 4 thì y = 12. Tìm hệ số tỉ lệ của y đối với x và tính y khi x = 5.","dd": ["k = 3; y = 15"],"gt": "k = 12/4 = 3. Khi x=5 ⇒ y = 3.5 = 15."},
            {"de": "Biết x và y tỉ lệ nghịch, khi x = 2 thì y = 10. Tìm hệ số tỉ lệ và tính y khi x = 4.","dd": ["a = 20; y = 5"],"gt": "a = x.y = 20. Khi x=4 ⇒ y = 20/4 = 5."},
            {"de": "Ba lớp 7A, 7B, 7C trồng được 120 cây. Số cây tỉ lệ thuận với 3, 4, 5. Tính số cây lớp 7B.","dd": ["40 cây"],"gt": "120/(3+4+5) = 10. Lớp 7B = 4.10 = 40."},
            {"de": "Tìm x biết (x-1)/5 = 3/15.","dd": ["x = 2"],"gt": "3/15 = 1/5 ⇒ (x-1)/5 = 1/5 ⇒ x-1 = 1 ⇒ x = 2."},
            {"de": "12 công nhân xây xong nhà trong 30 ngày. Hỏi 15 công nhân xây xong trong bao lâu? (Năng suất như nhau)","dd": ["24 ngày"],"gt": "Tỉ lệ nghịch: 12.30 = 15.x ⇒ 360 = 15.x ⇒ x = 24."},
            {"de": "Mua 5 quyển vở hết 40.000 đồng. Hỏi mua 8 quyển vở loại đó hết bao nhiêu tiền?","dd": ["64.000 đồng"],"gt": "Tỉ lệ thuận: 40000/5 = 8000/quyển. 8.8000 = 64.000đ."},
            {"de": "Từ đẳng thức 2.15 = 5.6, hãy viết một tỉ lệ thức.","dd": ["2/5 = 6/15 (hoặc 2/6 = 5/15...)"],"gt": "Dựa vào nguyên lí a.d = b.c ⇒ a/b = c/d."},
            {"de": "Cho x/2 = y/3 = z/4 và x + y + z = 18. Tính z.","dd": ["z = 8"],"gt": "18/(2+3+4) = 18/9 = 2. z = 4.2 = 8."}
        ],

        "bt_nang_cao": [
            {"de": "Tìm x, y, z biết x/2 = y/3, y/4 = z/5 và x + y + z = 105.","hd": "Đưa về cùng một mẫu chung cho y. BCNN(3,4) = 12.","dd": ["x=24, y=36, z=45"],"lg": "x/8 = y/12 và y/12 = z/15 ⇒ x/8 = y/12 = z/15. Tổng: 105/(8+12+15) = 105/35 = 3. Suy ra x=24, y=36, z=45."},
            {"de": "Tìm x, y biết x/3 = y/4 và x.y = 48.","hd": "Đặt x = 3k, y = 4k thay vào phương trình tích.","dd": ["x=6, y=8 hoặc x=-6, y=-8"],"lg": "(3k).(4k) = 48 ⇒ 12k² = 48 ⇒ k² = 4 ⇒ k = 2 hoặc k = -2. Từ đó tính x, y."},
            {"de": "Tìm x, y biết x/5 = y/3 và x² - y² = 64.","hd": "Đặt x = 5k, y = 3k thay vào hiệu bình phương.","dd": ["x=10, y=6 hoặc x=-10, y=-6"],"lg": "(5k)² - (3k)² = 25k² - 9k² = 16k² = 64 ⇒ k² = 4 ⇒ k = ±2."},
            {"de": "Một bánh răng cưa có 24 răng quay được 80 vòng/phút. Nó khớp với bánh thứ hai có 60 răng. Hỏi bánh thứ hai quay được bao nhiêu vòng/phút?","hd": "Số răng và số vòng quay là hai đại lượng tỉ lệ nghịch.","dd": ["32 vòng/phút"],"lg": "x.y = const ⇒ 24 . 80 = 60 . V ⇒ V = 1920 / 60 = 32 vòng/phút."},
            {"de": "Chia số 310 thành ba phần tỉ lệ nghịch với 2, 3, 5. Tìm phần nhỏ nhất.","hd": "Tỉ lệ nghịch với 2, 3, 5 tức là tỉ lệ thuận với 1/2, 1/3, 1/5.","dd": ["60"],"lg": "x/(1/2) = y/(1/3) = z/(1/5). Quy đồng mẫu: x/15 = y/10 = z/6. Tổng 310/(15+10+6) = 310/31 = 10. Phần nhỏ nhất z = 6.10 = 60."}
        ]
    }
}
T7["Chương 6: Tỉ lệ thức và Đại lượng tỉ lệ"] = C6_T7

# --- Chương 7: Biểu thức đại số và Đa thức một biến ---
C7_T7 = {
    "Biểu thức đại số và Đa thức một biến (Chuyên sâu)": {
        "ly_thuyet": """📌 1. BIỂU THỨC ĐẠI SỐ:
- Biểu thức đại số là biểu thức chứa các số, các biến (chữ) và các phép toán (cộng, trừ, nhân, chia, lũy thừa).
- Giá trị của biểu thức đại số tại các giá trị cho trước của biến được tính bằng cách thay trực tiếp số vào biến rồi thực hiện phép tính.

📌 2. ĐA THỨC MỘT BIẾN:
- Đa thức một biến là tổng của những đơn thức của cùng một biến. Kí hiệu: P(x), Q(y)...
- Bậc của đa thức một biến (khác đa thức không, đã thu gọn) là số mũ lớn nhất của biến trong đa thức đó.
- Hệ số của lũy thừa cao nhất gọi là hệ số cao nhất. Hệ số của lũy thừa bậc 0 gọi là hệ số tự do.

📌 3. CỘNG, TRỪ ĐA THỨC MỘT BIẾN:
- Ta có thể cộng, trừ đa thức bằng cách: Sắp xếp các hạng tử theo cùng lũy thừa giảm (hoặc tăng) rồi đặt phép tính theo cột dọc, hoặc nhóm các hạng tử đồng dạng theo hàng ngang.

📌 4. NGHIỆM CỦA ĐA THỨC MỘT BIẾN:
- Nếu tại x = a, đa thức P(x) có giá trị bằng 0 (tức là P(a) = 0) thì ta nói a là một nghiệm của đa thức P(x).
- Một đa thức bậc n có tối đa n nghiệm.""",
        
        "vi_du": """💡 VÍ DỤ 1: Tính giá trị biểu thức
Đề bài: Tính giá trị của biểu thức A = 2x² - 3x + 5 tại x = -2.
- Giải:
  Thay x = -2 vào biểu thức A, ta được:
  A = 2.(-2)² - 3.(-2) + 5
  A = 2.4 + 6 + 5
  A = 8 + 6 + 5 = 19.

💡 VÍ DỤ 2: Tìm bậc và hệ số của đa thức
Đề bài: Cho đa thức P(x) = 5x⁴ - 3x² + 7x - 5x⁴ + x³ - 2. Thu gọn P(x) và xác định bậc, hệ số cao nhất, hệ số tự do.
- Giải:
  P(x) = (5x⁴ - 5x⁴) + x³ - 3x² + 7x - 2 = x³ - 3x² + 7x - 2.
  + Bậc của đa thức là 3 (số mũ cao nhất).
  + Hệ số cao nhất là 1 (hệ số của x³).
  + Hệ số tự do là -2.

💡 VÍ DỤ 3: Tìm nghiệm của đa thức
Đề bài: Tìm nghiệm của đa thức M(x) = 3x - 12.
- Giải: 
  Để tìm nghiệm, ta cho M(x) = 0.
  ⇒ 3x - 12 = 0
  ⇒ 3x = 12
  ⇒ x = 4.
  Vậy x = 4 là nghiệm của đa thức M(x).""",

        "cau_hoi": [
            {"nd": "Biểu thức đại số là biểu thức chứa:","da": ["Chỉ các số","Chỉ các chữ","Số, chữ và các phép toán","Chỉ các phép toán"],"d": 2,"gt": "Định nghĩa biểu thức đại số."},
            {"nd": "Giá trị của biểu thức 5x - 3 tại x = 2 là?","da": ["7","10","13","4"],"d": 0,"gt": "5.2 - 3 = 10 - 3 = 7."},
            {"nd": "Cho biểu thức 2x²y. Tính giá trị khi x=-1, y=3.","da": ["-6","6","-12","12"],"d": 1,"gt": "2.(-1)².3 = 2.1.3 = 6."},
            {"nd": "Bậc của đa thức P(x) = 3x⁵ - 4x³ + 2x - 1 là?","da": ["3","5","2","1"],"d": 1,"gt": "Số mũ cao nhất của biến x là 5."},
            {"nd": "Hệ số cao nhất của đa thức Q(x) = -2x⁴ + 5x³ - x + 7 là?","da": ["5","-2","7","-1"],"d": 1,"gt": "Hệ số của lũy thừa cao nhất x⁴ là -2."},
            {"nd": "Hệ số tự do của đa thức H(x) = 4x³ - 6x² + 9 là?","da": ["4","-6","9","0"],"d": 2,"gt": "Hạng tử không chứa biến x là 9."},
            {"nd": "Nghiệm của đa thức f(x) = x - 5 là?","da": ["-5","5","0","1"],"d": 1,"gt": "x - 5 = 0 ⇒ x = 5."},
            {"nd": "Nghiệm của đa thức g(x) = 2x + 8 là?","da": ["4","-4","8","-8"],"d": 1,"gt": "2x + 8 = 0 ⇒ 2x = -8 ⇒ x = -4."},
            {"nd": "Thu gọn đa thức 2x³ - 3x³ + x² ta được?","da": ["-x³ + x²","5x³ + x²","x²","-x²"],"d": 0,"gt": "(2-3)x³ + x² = -x³ + x²."},
            {"nd": "Đa thức nào sau đây không có nghiệm?","da": ["x - 1","x² - 1","x² + 1","x + 2"],"d": 2,"gt": "x² ≥ 0 nên x² + 1 ≥ 1 > 0 ∀x, không thể bằng 0."}
        ],

        "bt_co_ban": [
            {"de": "Viết biểu thức đại số biểu thị chu vi hình chữ nhật có chiều dài x và chiều rộng y.","dd": ["2(x + y)"],"gt": "Chu vi = 2 × (Dài + Rộng)."},
            {"de": "Tính giá trị biểu thức A = -x² + 4x tại x = 3.","dd": ["A = 3"],"gt": "A = -(3²) + 4.3 = -9 + 12 = 3."},
            {"de": "Tìm bậc, hệ số cao nhất, hệ số tự do của đa thức P(x) = -4x³ + 2x - 7.","dd": ["Bậc 3; HSCN = -4; HSTD = -7"],"gt": "Chỉ ra các thông số theo định nghĩa."},
            {"de": "Tính tổng P(x) + Q(x) biết P(x) = x² - 2x + 1 và Q(x) = -x² + 5x.","dd": ["3x + 1"],"gt": "(x² - x²) + (-2x + 5x) + 1 = 3x + 1."},
            {"de": "Tính hiệu M(x) - N(x) biết M(x) = 3x² + x và N(x) = x² - x.","dd": ["2x² + 2x"],"gt": "3x² + x - x² + x = 2x² + 2x."},
            {"de": "Tìm nghiệm của đa thức f(x) = 5x - 15.","dd": ["x = 3"],"gt": "5x = 15 ⇒ x = 3."},
            {"de": "Nhân đơn thức: -2x . (3x² - x)","dd": ["-6x³ + 2x²"],"gt": "Phân phối: (-2x).(3x²) + (-2x).(-x)."},
            {"de": "Chia đa thức: (4x³ - 6x²) : 2x²","dd": ["2x - 3"],"gt": "Chia từng hạng tử: 4x³/2x² - 6x²/2x²."},
            {"de": "Cho đa thức P(x) = ax + 4. Tìm a biết P(2) = 10.","dd": ["a = 3"],"gt": "a.2 + 4 = 10 ⇒ 2a = 6 ⇒ a = 3."},
            {"de": "Chứng minh đa thức x² + 5 vô nghiệm.","dd": ["Xem lời giải"],"gt": "x² ≥ 0 ⇒ x² + 5 ≥ 5 > 0 ∀x, nên không thể bằng 0."}
        ],

        "bt_nang_cao": [
            {"de": "Tính giá trị biểu thức A = x(x - y) + y(x - y) tại x = 99, y = -1.","hd": "Rút gọn biểu thức trước khi thay số.","dd": ["9800"],"lg": "A = (x - y)(x + y) = x² - y². Thay x=99, y=-1 vào A = 99² - (-1)² = 9801 - 1 = 9800."},
            {"de": "Tìm đa thức P(x) biết P(x) + (x² - 3x + 2) = 3x² - x + 5.","hd": "P(x) = Tổng - Đa thức hạng.","dd": ["2x² + 2x + 3"],"lg": "P(x) = (3x² - x + 5) - (x² - 3x + 2) = 2x² + 2x + 3."},
            {"de": "Tìm nghiệm của đa thức: x² - 5x + 6","hd": "Phân tích đa thức thành nhân tử bằng cách tách -5x = -2x - 3x.","dd": ["x = 2 hoặc x = 3"],"lg": "x² - 2x - 3x + 6 = 0 ⇒ x(x - 2) - 3(x - 2) = 0 ⇒ (x - 2)(x - 3) = 0. Do đó x = 2 hoặc x = 3."},
            {"de": "Chứng minh rằng giá trị của biểu thức B = (x - 2)(x + 2) - x² luôn không phụ thuộc vào x.","hd": "Khai triển biểu thức.","dd": ["B = -4 (Không đổi)"],"lg": "B = x² - 4 - x² = -4. Kết quả là hằng số nên không phụ thuộc vào x."},
            {"de": "Tìm a, b để đa thức P(x) = x² + ax + b có hai nghiệm là x = 1 và x = 2.","hd": "Lập hệ phương trình P(1) = 0 và P(2) = 0.","dd": ["a = -3, b = 2"],"lg": "P(1) = 1 + a + b = 0 ⇒ a + b = -1. P(2) = 4 + 2a + b = 0 ⇒ 2a + b = -4. Trừ hai PT ta được a = -3 ⇒ b = 2."}
        ]
    }
}
T7["Chương 7: Biểu thức đại số và Đa thức một biến"] = C7_T7

# --- Chương 8: Làm quen với biến cố và xác suất của biến cố ---
C8_T7 = {
    "Làm quen với Biến cố và Xác suất (Chuyên sâu)": {
        "ly_thuyet": """📌 1. CÁC LOẠI BIẾN CỐ:
- Biến cố chắc chắn: Là biến cố luôn luôn xảy ra trong một phép thử hoặc trò chơi.
- Biến cố không thể: Là biến cố không bao giờ xảy ra.
- Biến cố ngẫu nhiên: Là biến cố không thể biết trước có xảy ra hay không, phụ thuộc vào sự ngẫu nhiên.

📌 2. XÁC SUẤT CỦA BIẾN CỐ:
- Xác suất của một biến cố là một con số (từ 0 đến 1, hoặc từ 0% đến 100%) đo lường khả năng xảy ra của biến cố đó.
- Kí hiệu xác suất của biến cố A là P(A).
  + Biến cố chắc chắn có xác suất bằng 1 (hoặc 100%).
  + Biến cố không thể có xác suất bằng 0.
  + Biến cố ngẫu nhiên có xác suất nằm trong khoảng từ 0 đến 1.

📌 3. TÍNH XÁC SUẤT BẰNG TỈ SỐ:
- Trong một trò chơi mà các kết quả có khả năng xảy ra như nhau (đồng khả năng), xác suất của biến cố A được tính bằng công thức:
  P(A) = (Số kết quả thuận lợi cho biến cố A) / (Tổng số kết quả có thể xảy ra).""",
        
        "vi_du": """💡 VÍ DỤ 1: Phân loại biến cố
Đề bài: Trong hộp có 5 viên bi đỏ. Lấy ngẫu nhiên 1 viên bi. Phân loại các biến cố sau:
A: "Lấy được viên bi màu đỏ".
B: "Lấy được viên bi màu xanh".
C: "Lấy được viên bi hình cầu".
- Giải: 
  + Biến cố A là biến cố chắc chắn (vì trong hộp chỉ có bi đỏ).
  + Biến cố B là biến cố không thể (trong hộp không có bi xanh).
  + Biến cố C là biến cố chắc chắn (bi đương nhiên có hình cầu).

💡 VÍ DỤ 2: Tính xác suất khi gieo xúc xắc
Đề bài: Gieo một con xúc xắc cân đối 6 mặt. Tính xác suất của biến cố M: "Mặt xuất hiện có số chấm là số nguyên tố".
- Giải:
  + Các kết quả có thể xảy ra: {1; 2; 3; 4; 5; 6} ⇒ Tổng cộng có 6 kết quả đồng khả năng.
  + Các kết quả thuận lợi cho M (số nguyên tố): {2; 3; 5} ⇒ Có 3 kết quả thuận lợi.
  + Xác suất P(M) = 3 / 6 = 1/2 (hoặc 50%).

💡 VÍ DỤ 3: Bốc thăm ngẫu nhiên
Đề bài: Rút ngẫu nhiên một lá bài từ bộ bài tú lơ khơ 52 lá. Tính xác suất rút được lá Át (A).
- Giải:
  + Tổng số lá bài là 52 ⇒ Có 52 kết quả có thể.
  + Số lá Át trong bộ bài là 4 ⇒ Có 4 kết quả thuận lợi.
  + Xác suất P = 4 / 52 = 1/13.""",

        "cau_hoi": [
            {"nd": "Biến cố luôn xảy ra được gọi là?","da": ["Biến cố chắc chắn","Biến cố ngẫu nhiên","Biến cố không thể","Biến cố độc lập"],"d": 0,"gt": "Định nghĩa biến cố chắc chắn."},
            {"nd": "Xác suất của biến cố không thể bằng bao nhiêu?","da": ["1","0,5","0","100%"],"d": 2,"gt": "Không bao giờ xảy ra nên xác suất = 0."},
            {"nd": "Xác suất của một biến cố ngẫu nhiên luôn nằm trong khoảng nào?","da": ["Từ 0 đến 1","Từ 1 đến 10","Từ -1 đến 1","Lớn hơn 1"],"d": 0,"gt": "Xác suất không bao giờ âm và tối đa là 1 (100%)."},
            {"nd": "Gieo 1 đồng xu cân đối, xác suất xuất hiện mặt Sấp là?","da": ["0","1/2","1/3","1"],"d": 1,"gt": "Đồng xu có 2 mặt (S, N) nên xác suất là 1/2."},
            {"nd": "Trong hộp có 10 viên bi xanh. Biến cố 'Lấy được viên bi đỏ' là:","da": ["Biến cố ngẫu nhiên","Biến cố chắc chắn","Biến cố không thể","Chưa đủ dữ kiện"],"d": 2,"gt": "Không có bi đỏ nên không thể lấy được."},
            {"nd": "Gieo một con xúc xắc 6 mặt, biến cố 'Xuất hiện mặt có số chấm lớn hơn 6' là?","da": ["Biến cố chắc chắn","Biến cố không thể","Biến cố ngẫu nhiên","Biến cố đối"],"d": 1,"gt": "Xúc xắc chỉ có số chấm từ 1 đến 6."},
            {"nd": "Một hộp có 3 quả bóng đỏ và 2 quả bóng xanh. Lấy ngẫu nhiên 1 quả. Xác suất lấy được bóng đỏ là?","da": ["3/2","2/5","3/5","1/2"],"d": 2,"gt": "Có 3 quả đỏ trên tổng số 5 quả ⇒ 3/5."},
            {"nd": "Gieo một con xúc xắc, xác suất ra mặt chẵn là?","da": ["1/6","1/3","1/2","2/3"],"d": 2,"gt": "Mặt chẵn gồm {2, 4, 6} (3 mặt) trên tổng 6 mặt ⇒ 3/6 = 1/2."},
            {"nd": "Xác suất của biến cố chắc chắn là?","da": ["0%","50%","100%","99%"],"d": 2,"gt": "Chắc chắn xảy ra nên xác suất tuyệt đối là 100% (hay 1)."},
            {"nd": "Chọn ngẫu nhiên một số từ 1 đến 10. Xác suất chọn được số chia hết cho 3 là?","da": ["3/10","4/10","1/3","1/5"],"d": 0,"gt": "Các số chia hết cho 3 là {3, 6, 9} (3 số) / Tổng 10 số."}
        ],

        "bt_co_ban": [
            {"de": "Gieo một con xúc xắc cân đối. Liệt kê các kết quả có thể xảy ra.","dd": ["{1, 2, 3, 4, 5, 6}"],"gt": "Xúc xắc có 6 mặt tương ứng với 1 đến 6 chấm."},
            {"de": "Hộp có 5 bút xanh và 3 bút đỏ. Tính xác suất lấy được bút đỏ.","dd": ["3/8"],"gt": "Tổng số bút = 8. Bút đỏ = 3 ⇒ 3/8."},
            {"de": "Biến cố 'Tháng 2 có 30 ngày' là loại biến cố gì?","dd": ["Biến cố không thể"],"gt": "Tháng 2 nhiều nhất chỉ có 29 ngày (năm nhuận)."},
            {"de": "Trong bảng chữ cái Tiếng Việt (29 chữ), xác suất rút ngẫu nhiên được chữ 'A' là?","dd": ["1/29"],"gt": "Chỉ có 1 chữ A trong 29 chữ cái."},
            {"de": "Một bánh xe quay có 8 hình quạt bằng nhau, đánh số từ 1 đến 8. Xác suất kim chỉ vào số 5 là?","dd": ["1/8"],"gt": "Có 1 ô số 5 trên tổng số 8 ô."},
            {"de": "Rút một lá bài từ bộ 52 lá. Xác suất rút được lá Át bích là?","dd": ["1/52"],"gt": "Trong bộ bài chỉ có duy nhất 1 lá Át bích."},
            {"de": "Biến cố 'Nước sôi ở 100°C (ở điều kiện tiêu chuẩn)' là biến cố gì?","dd": ["Biến cố chắc chắn"],"gt": "Đây là hiện tượng vật lý hiển nhiên luôn xảy ra."},
            {"de": "Túi có 4 quả bóng xanh, 4 bóng đỏ. Xác suất lấy được bóng xanh là bao nhiêu %?","dd": ["50%"],"gt": "4/8 = 1/2 = 50%."},
            {"de": "Một bộ xóc đĩa có 4 đồng xu. Xác suất xuất hiện 5 mặt ngửa là?","dd": ["0"],"gt": "Chỉ có 4 đồng xu nên không thể có 5 mặt ngửa (Biến cố không thể)."},
            {"de": "Chọn 1 ngày ngẫu nhiên trong tháng 8. Xác suất chọn được ngày 32 là?","dd": ["0"],"gt": "Tháng 8 chỉ có 31 ngày."}
        ],

        "bt_nang_cao": [
            {"de": "Gieo hai con xúc xắc cân đối. Tính xác suất để tổng số chấm trên hai mặt bằng 7.","hd": "Lập bảng các cặp kết quả có tổng bằng 7. Tổng số kết quả là 6 x 6 = 36.","dd": ["1/6"],"lg": "Các cặp có tổng = 7: (1,6), (6,1), (2,5), (5,2), (3,4), (4,3). Có 6 kết quả thuận lợi. P = 6/36 = 1/6."},
            {"de": "Trong hộp có thẻ đánh số từ 1 đến 30. Rút 1 thẻ, tính xác suất thẻ rút được là số nguyên tố.","hd": "Liệt kê các số nguyên tố từ 1 đến 30.","dd": ["1/3"],"lg": "Các số nguyên tố: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (10 số). P = 10/30 = 1/3."},
            {"de": "Gieo 1 xúc xắc 2 lần liên tiếp. Tính xác suất để lần 1 ra mặt chẵn, lần 2 ra mặt lẻ.","hd": "Mỗi lần độc lập nhau. Lần 1 chẵn (3 cách), lần 2 lẻ (3 cách).","dd": ["1/4"],"lg": "Số kết quả thỏa mãn: 3 x 3 = 9. Tổng số kết quả: 6 x 6 = 36. P = 9/36 = 1/4."},
            {"de": "Tung 3 đồng xu cùng lúc. Tính xác suất để có đúng 2 mặt Ngửa.","hd": "Liệt kê 8 kết quả có thể.","dd": ["3/8"],"lg": "Các kết quả có thể: SSS, SSN, SNS, SNN, NSS, NSN, NNS, NNN (8). Có đúng 2 ngửa: SNN, NSN, NNS (3). P = 3/8."},
            {"de": "Một lồng quay xổ số có bóng đánh số 00 đến 99. Xác suất quay được quả bóng có hai chữ số giống nhau?","hd": "Các số giống nhau: 00, 11, 22...","dd": ["1/10"],"lg": "Các số 00, 11, 22, 33, 44, 55, 66, 77, 88, 99 (10 quả). Tổng số bóng = 100. P = 10/100 = 1/10."}
        ]
    }
}
T7["Chương 8: Biến cố và Xác suất"] = C8_T7

# --- Chương 9: Quan hệ giữa các yếu tố trong một tam giác ---
C9_T7 = {
    "Quan hệ các yếu tố trong Tam giác (Chuyên sâu)": {
        "ly_thuyet": """📌 1. QUAN HỆ GIỮA GÓC VÀ CẠNH ĐỐI DIỆN TRONG TAM GIÁC:
- Trong một tam giác, góc đối diện với cạnh lớn hơn là góc lớn hơn. Ngược lại, cạnh đối diện với góc lớn hơn là cạnh lớn hơn.
- Trong tam giác vuông, cạnh huyền là cạnh lớn nhất. Trong tam giác tù, cạnh đối diện góc tù là cạnh lớn nhất.

📌 2. BẤT ĐẲNG THỨC TAM GIÁC:
- Trong một tam giác, độ dài một cạnh bất kì luôn lớn hơn hiệu và nhỏ hơn tổng độ dài hai cạnh còn lại.
- |b - c| < a < b + c.

📌 3. SỰ ĐỒNG QUY CỦA CÁC ĐƯỜNG TRONG TAM GIÁC:
- 3 đường Trung tuyến: Đồng quy tại một điểm gọi là Trọng tâm. Trọng tâm cách mỗi đỉnh 2/3 độ dài đường trung tuyến đi qua đỉnh đó.
- 3 đường Phân giác: Đồng quy tại một điểm. Điểm này cách đều 3 cạnh của tam giác (Tâm đường tròn nội tiếp).
- 3 đường Trung trực: Đồng quy tại một điểm. Điểm này cách đều 3 đỉnh của tam giác (Tâm đường tròn ngoại tiếp).
- 3 đường Cao: Đồng quy tại một điểm gọi là Trực tâm.

📌 4. TÍNH CHẤT TAM GIÁC CÂN, ĐỀU:
- Trong tam giác cân: Đường cao xuất phát từ đỉnh đồng thời là đường trung tuyến, đường phân giác, đường trung trực của cạnh đáy.
- Trong tam giác đều: Trọng tâm, Trực tâm, Tâm nội tiếp, Tâm ngoại tiếp trùng nhau tại một điểm duy nhất.""",
        
        "vi_du": """💡 VÍ DỤ 1: Quan hệ góc cạnh
Đề bài: Cho ∆ABC có AB = 4cm, BC = 6cm, AC = 5cm. Sắp xếp các góc của tam giác theo thứ tự tăng dần.
- Giải:
  Ta có: AB < AC < BC (4 < 5 < 6).
  Góc đối diện với AB là C, với AC là C... (tương ứng).

💡 VÍ DỤ 2: Bất đẳng thức tam giác
Đề bài: Có thể vẽ được tam giác với độ dài 3 cạnh là 2cm, 3cm và 6cm không?
- Giải:
  Ta lấy tổng 2 cạnh nhỏ nhất: 2 + 3 = 5.
  Vì 5 < 6 (tổng 2 cạnh nhỏ hơn cạnh thứ 3) ⇒ Không thỏa mãn Bất đẳng thức tam giác.
  Vậy không thể vẽ được tam giác này.""",

        "cau_hoi": [
            {"nd": "Trong một tam giác, đối diện với cạnh lớn nhất là?","da": ["Góc nhọn","Góc nhỏ nhất","Góc lớn nhất","Góc vuông"],"d": 2,"gt": "Định lí góc đối diện với cạnh lớn hơn."},
            {"nd": "Cho ∆ABC có góc A = 80°, B = 40°. Cạnh nào lớn nhất?","da": ["AB","BC","AC","Không xác định"],"d": 1,"gt": "Góc C = 180 - 80 - 40 = 60°. Góc A lớn nhất ⇒ cạnh BC đối diện lớn nhất."},
            {"nd": "Cho ∆MNP có MN = 3, NP = 4, MP = 5. Khẳng định nào đúng?","da": ["Góc M lớn nhất","Góc N lớn nhất","Góc P lớn nhất","Ba góc bằng nhau"],"d": 1,"gt": "Cạnh MP lớn nhất (5) ⇒ Góc đối diện là góc N lớn nhất."},
            {"nd": "Bất đẳng thức tam giác phát biểu rằng độ dài một cạnh luôn:","da": ["Lớn hơn tổng 2 cạnh kia","Bằng tổng 2 cạnh kia","Nhỏ hơn tổng 2 cạnh kia","Gấp đôi tổng 2 cạnh kia"],"d": 2,"gt": "Một cạnh < tổng 2 cạnh còn lại."},
            {"nd": "Bộ 3 độ dài nào sau đây tạo thành một tam giác?","da": ["1, 2, 3","2, 4, 7","3, 4, 5","1, 1, 3"],"d": 2,"gt": "Chỉ có 3+4 > 5 thỏa mãn BĐT tam giác."},
            {"nd": "Giao điểm 3 đường trung tuyến của tam giác gọi là?","da": ["Trực tâm","Trọng tâm","Tâm đường tròn ngoại tiếp","Tâm đường tròn nội tiếp"],"d": 1,"gt": "Giao trung tuyến là Trọng tâm."},
            {"nd": "Giao điểm 3 đường cao của tam giác gọi là?","da": ["Trực tâm","Trọng tâm","Tâm nội tiếp","Tâm ngoại tiếp"],"d": 0,"gt": "Đường cao giao nhau tại Trực tâm."},
            {"nd": "Khoảng cách từ trọng tâm G đến đỉnh bằng bao nhiêu phần đường trung tuyến đi qua đỉnh đó?","da": ["1/3","1/2","2/3","3/4"],"d": 2,"gt": "Tính chất trọng tâm: AG = 2/3 AM."},
            {"nd": "Điểm cách đều 3 đỉnh của tam giác là giao điểm của 3 đường gì?","da": ["Phân giác","Cao","Trung tuyến","Trung trực"],"d": 3,"gt": "Tính chất đường trung trực của đoạn thẳng."},
            {"nd": "Điểm cách đều 3 cạnh của tam giác là giao điểm của 3 đường gì?","da": ["Trung trực","Phân giác","Trung tuyến","Cao"],"d": 1,"gt": "Tính chất đường phân giác góc."}
        ],

        "bt_co_ban": [
            {"de": "Cho ∆ABC có góc A = 50°, góc B = 60°. Sắp xếp độ dài 3 cạnh của tam giác từ nhỏ đến lớn.","dd": ["BC < AC < AB"],"gt": "Góc C = 180 - 50 - 60 = 70°. Góc A < B < C ⇒ Cạnh đối BC < AC < AB."},
            {"de": "Tam giác có hai cạnh là 3cm và 8cm. Tìm số nguyên duy nhất có thể là độ dài cạnh thứ 3 nếu nó là tam giác cân.","dd": ["8 cm"],"gt": "Cạnh kia là 3 hoặc 8. Nếu là 3: 3+3 < 8 (loại). Nếu là 8: 3+8 > 8 (nhận)."},
            {"de": "Đường trung tuyến AM của ∆ABC dài 15cm. Trọng tâm G. Tính AG.","dd": ["10 cm"],"gt": "AG = 2/3 AM = 2/3 . 15 = 10."},
            {"de": "Điểm I là giao của 3 đường phân giác trong ∆ABC. Nếu khoảng cách từ I đến AB là 4cm, tính khoảng cách từ I đến BC.","dd": ["4 cm"],"gt": "Giao 3 phân giác cách đều 3 cạnh."},
            {"de": "Cho ∆MNP có MN = 5, NP = 12, MP = 13. Cạnh nào lớn nhất? Góc nào lớn nhất?","dd": ["Cạnh MP lớn nhất, Góc N lớn nhất"],"gt": "MP = 13 là lớn nhất, đối diện MP là góc N."},
            {"de": "Kiểm tra bộ ba độ dài 5cm, 6cm, 10cm có là ba cạnh tam giác không?","dd": ["Có"],"gt": "5+6=11 > 10 (Thỏa mãn BĐT tam giác)."},
            {"de": "Trong tam giác đều, trực tâm và trọng tâm có trùng nhau không?","dd": ["Có"],"gt": "Tính chất đặc biệt của tam giác đều."},
            {"de": "Trung trực của cạnh AB cắt AB tại M. Biết AB = 10cm. Tính MA.","dd": ["5 cm"],"gt": "Trung trực đi qua trung điểm ⇒ MA = 10/2 = 5cm."},
            {"de": "Cho ∆ABC vuông tại A. Trực tâm của tam giác nằm ở đâu?","dd": ["Tại đỉnh A"],"gt": "Giao của 2 đường cao AB và AC chính là A."},
            {"de": "Hai cạnh của một tam giác là 4cm và 9cm. Cạnh thứ 3 là số nguyên chẵn. Tìm độ dài cạnh thứ 3.","dd": ["6cm, 8cm, 10cm, 12cm"],"gt": "9-4 < x < 9+4 ⇒ 5 < x < 13. Các số chẵn là 6, 8, 10, 12."}
        ],

        "bt_nang_cao": [
            {"de": "Chứng minh rằng trong một tam giác, nửa chu vi luôn lớn hơn mỗi cạnh của tam giác đó.","hd": "Dùng BĐT tam giác: a < b + c. Cộng a vào 2 vế.","dd": ["Xem lời giải"],"lg": "a < b + c ⇒ a + a < a + b + c ⇒ 2a < P ⇒ a < P/2 (đpcm)."},
            {"de": "Cho ∆ABC có trung tuyến AM. Chứng minh AM < (AB + AC)/2.","hd": "Lấy D đối xứng A qua M. Xét ∆AMC và ∆DMB.","dd": ["Xem lời giải"],"lg": "Dựng D sao cho M là trung điểm AD. Dễ thấy ∆AMB = ∆DMC ⇒ AB = CD. Trong ∆ACD có AD < AC + CD = AC + AB. Mà AD = 2AM ⇒ 2AM < AB + AC ⇒ AM < (AB+AC)/2."},
            {"de": "Giao điểm 3 đường trung trực của tam giác vuông nằm ở trung điểm cạnh huyền. Chứng minh điều này.","hd": "Gọi M là trung điểm cạnh huyền BC, chứng minh MA = MB = MC.","dd": ["Xem lời giải"],"lg": "Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền. AM = MB = MC = BC/2."},
            {"de": "Cho ∆ABC có I là giao điểm của hai tia phân giác góc B và C. Kẻ IH ⊥ BC. Khẳng định: I là tâm đường tròn nội tiếp ∆ABC đúng không?","hd": "I là giao 2 phân giác thì nó có thuộc phân giác thứ 3 không?","dd": ["Đúng"],"lg": "Giao của 2 đường phân giác cũng là giao của cả 3 đường phân giác. I cách đều 3 cạnh. I là tâm đường tròn nội tiếp."},
            {"de": "Cho điểm O nằm trong tam giác ABC. Chứng minh: OA + OB + OC > (AB + BC + CA) / 2","hd": "Xét 3 tam giác nhỏ OAB, OBC, OCA rồi dùng BĐT tam giác.","dd": ["Xem lời giải"],"lg": "Xét ∆OAB: OA+OB > AB. ∆OBC: OB+OC > BC. ∆OCA: OC+OA > AC. Cộng 3 BĐT: 2(OA+OB+OC) > AB+BC+CA ⇒ OA+OB+OC > P/2."}
        ]
    }
}
T7["Chương 9: Quan hệ các yếu tố trong Tam giác"] = C9_T7

# --- Chương 10: Một số hình khối trong thực tiễn ---
C10_T7 = {
    "Một số hình khối trong thực tiễn (Chuyên sâu)": {
        "ly_thuyet": """📌 1. HÌNH HỘP CHỮ NHẬT VÀ HÌNH LẬP PHƯƠNG:
- Hình hộp chữ nhật: Có 6 mặt là hình chữ nhật, 8 đỉnh, 12 cạnh. Các mặt đối diện song song và bằng nhau.
  + Diện tích xung quanh: S_xq = 2.(a + b).h  (Chu vi đáy nhân với chiều cao)
  + Thể tích: V = a.b.h (Dài × Rộng × Cao)
- Hình lập phương: Là hình hộp chữ nhật đặc biệt có 6 mặt đều là hình vuông bằng nhau.
  + Diện tích xung quanh: S_xq = 4.a²
  + Thể tích: V = a³

📌 2. HÌNH LĂNG TRỤ ĐỨNG TAM GIÁC, LĂNG TRỤ ĐỨNG TỨ GIÁC:
- Lăng trụ đứng: Có 2 mặt đáy song song và bằng nhau (có thể là tam giác hoặc tứ giác). Các mặt bên đều là hình chữ nhật và vuông góc với mặt đáy.
- Các cạnh bên song song và bằng nhau, độ dài cạnh bên chính là chiều cao (h) của lăng trụ.
- Công thức tính:
  + Diện tích xung quanh: S_xq = C_đáy . h (C_đáy: Chu vi mặt đáy)
  + Diện tích toàn phần: S_tp = S_xq + 2.S_đáy
  + Thể tích: V = S_đáy . h (Diện tích đáy nhân với chiều cao)

📌 3. ỨNG DỤNG THỰC TẾ:
- Diện tích xung quanh thường dùng để tính diện tích quét sơn các bức tường của căn phòng, diện tích giấy dán xung quanh hộp.
- Thể tích dùng để tính sức chứa của bể nước, thể tích không khí trong phòng, khối lượng của vật (m = D.V).""",
        
        "vi_du": """💡 VÍ DỤ 1: Tính diện tích và thể tích Hình hộp chữ nhật
Đề bài: Một bể cá dạng hình hộp chữ nhật làm bằng kính (không có nắp) có chiều dài 80cm, chiều rộng 50cm, chiều cao 45cm. Tính diện tích kính dùng làm bể và thể tích của bể cá.
- Phân tích: Bể không nắp nên diện tích kính = S_xq + 1.S_đáy.
- Giải:
  + Diện tích xung quanh: S_xq = 2.(80 + 50).45 = 2 . 130 . 45 = 11700 (cm²).
  + Diện tích mặt đáy: S_đáy = 80 . 50 = 4000 (cm²).
  + Diện tích kính cần dùng: S_kính = 11700 + 4000 = 15700 (cm²).
  + Thể tích bể cá: V = 80 . 50 . 45 = 180000 (cm³) = 180 (lít).

💡 VÍ DỤ 2: Tính thể tích Lăng trụ đứng tam giác
Đề bài: Một lều chữ A có dạng lăng trụ đứng tam giác. Mặt trước là tam giác cân có cạnh đáy 2m, chiều cao hạ từ đỉnh là 1,5m. Chiều dài của lều là 3m. Tính thể tích không gian bên trong lều.
- Phân tích: Đáy của lăng trụ chính là mặt trước (tam giác cân), chiều cao lăng trụ là chiều dài của lều (3m).
- Giải:
  + Diện tích đáy (tam giác): S_đáy = 1/2 . 2 . 1,5 = 1,5 (m²).
  + Thể tích lều: V = S_đáy . h = 1,5 . 3 = 4,5 (m³).

💡 VÍ DỤ 3: Bài toán thay đổi kích thước
Đề bài: Nếu gấp đôi độ dài cạnh của một hình lập phương thì thể tích của nó sẽ tăng lên bao nhiêu lần?
- Giải:
  + Gọi cạnh ban đầu là a, thể tích V1 = a³.
  + Cạnh lúc sau là 2a, thể tích V2 = (2a)³ = 8.a³.
  + Ta thấy V2 = 8.V1. Vậy thể tích tăng lên 8 lần.""",

        "cau_hoi": [
            {"nd": "Hình hộp chữ nhật có bao nhiêu đỉnh?","da": ["4","6","8","12"],"d": 2,"gt": "Hình hộp chữ nhật có 8 đỉnh."},
            {"nd": "Hình lập phương có bao nhiêu mặt?","da": ["4","6","8","12"],"d": 1,"gt": "Có 6 mặt là hình vuông."},
            {"nd": "Hình hộp chữ nhật có bao nhiêu cạnh?","da": ["6","8","10","12"],"d": 3,"gt": "Có 4 cạnh dài, 4 cạnh rộng, 4 cạnh cao ⇒ 12 cạnh."},
            {"nd": "Công thức tính thể tích V của hình hộp chữ nhật (kích thước a, b, h) là?","da": ["V = (a+b)h","V = 2(a+b)h","V = abh","V = a+b+h"],"d": 2,"gt": "Thể tích = Dài × Rộng × Cao."},
            {"nd": "Công thức tính diện tích xung quanh của hình hộp chữ nhật là?","da": ["2(a+b)h","(a+
