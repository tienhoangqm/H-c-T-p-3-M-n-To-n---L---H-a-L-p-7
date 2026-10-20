# -*- coding: utf-8 -*-
""" NGÂN HÀNG DỮ LIỆU MÔN HÓA HỌC (KHTN 7) — Bộ sách Kết Nối Tri Thức
Tập trung: HÓA HỌC LỚP 7 (Chuyên sâu)
"""

HOA = {}

# ==========================================
#                  LỚP 7
# ==========================================
H7 = {}

# --- Chương 1: Nguyên tử. Sơ lược bảng tuần hoàn ---
C1_H7 = {
    "Nguyên tử và Bảng tuần hoàn các nguyên tố hóa học (Chuyên sâu)": {
        "ly_thuyet": """📌 1. NGUYÊN TỬ:
- Nguyên tử là hạt vô cùng nhỏ, trung hòa về điện.
- Cấu tạo gồm 2 phần:
  + Hạt nhân (ở tâm): Chứa hạt Proton (kí hiệu p, mang điện dương +1) và Neutron (kí hiệu n, không mang điện).
  + Lớp vỏ: Chứa các hạt Electron (kí hiệu e, mang điện âm -1) chuyển động rất nhanh quanh hạt nhân.
- Trong nguyên tử trung hòa: Số p = Số e. Khối lượng nguyên tử chủ yếu tập trung ở hạt nhân (vì khối lượng e rất nhỏ).

📌 2. NGUYÊN TỐ HÓA HỌC:
- Là tập hợp những nguyên tử cùng loại, có cùng số proton trong hạt nhân.
- Kí hiệu hóa học (IUPAC): Hydrogen (H), Oxygen (O), Carbon (C), Nitrogen (N), Sodium (Na), Calcium (Ca), Iron (Fe), Copper (Cu),...

📌 3. SƠ LƯỢC BẢNG TUẦN HOÀN:
- Cấu tạo Bảng tuần hoàn (BTH): Ô nguyên tố, Chu kì (hàng ngang), Nhóm (cột dọc).
  + Số thứ tự Ô = Số hiệu nguyên tử (Z) = Số proton = Số electron.
  + Chu kì: Tập hợp các nguyên tố mà nguyên tử của chúng có cùng số lớp electron. Số thứ tự chu kì = Số lớp electron.
  + Nhóm: Tập hợp các nguyên tố có tính chất hóa học tương tự nhau và có cùng số electron lớp ngoài cùng. Số thứ tự Nhóm A = Số electron lớp ngoài cùng.
- Phân loại nguyên tố: Kim loại (thường ở nhóm IA, IIA, IIIA), Phi kim (thường ở nhóm VA, VIA, VIIA), Khí hiếm (Nhóm VIIIA).""",
        
        "vi_du": """💡 VÍ DỤ 1: Xác định cấu tạo nguyên tử
Đề bài: Nguyên tử Sodium (Na) có số hiệu nguyên tử (Z) là 11 và khối lượng nguyên tử (amu) xấp xỉ bằng 23. Tính số hạt p, e, n trong nguyên tử Na.
- Giải:
  + Số hiệu Z = 11 ⇒ Số proton p = 11.
  + Vì nguyên tử trung hòa về điện nên số electron e = p = 11.
  + Khối lượng nguyên tử ≈ số p + số n ⇒ 23 = 11 + n ⇒ Số neutron n = 23 - 11 = 12.

💡 VÍ DỤ 2: Xác định vị trí nguyên tố trong Bảng tuần hoàn
Đề bài: Nguyên tố Phosphorus (P) có 15 electron. Hãy xác định vị trí của P trong Bảng tuần hoàn (Ô, Chu kì, Nhóm).
- Giải:
  + Vì có 15 electron nên số hiệu nguyên tử Z = 15 ⇒ P nằm ở Ô số 15.
  + Sự phân bố 15 electron vào các lớp: Lớp thứ nhất (2e), Lớp thứ hai (8e), Lớp thứ ba (5e). 
  + Nguyên tử P có 3 lớp electron ⇒ P nằm ở Chu kì 3.
  + Lớp ngoài cùng có 5 electron ⇒ P nằm ở Nhóm VA.

💡 VÍ DỤ 3: Bài toán tổng số hạt cơ bản
Đề bài: Tổng số hạt cơ bản (p, n, e) trong một nguyên tử X là 40. Biết số hạt mang điện nhiều hơn số hạt không mang điện là 12. Xác định X.
- Giải:
  + Ta có hệ phương trình: Tổng số hạt: p + e + n = 40. Mặt khác p = e ⇒ 2p + n = 40 (1).
  + Hạt mang điện (p, e) nhiều hơn không mang điện (n): (p + e) - n = 12 ⇒ 2p - n = 12 (2).
  + Cộng (1) và (2): 4p = 52 ⇒ p = 13.
  + X có 13 proton, đối chiếu BTH, X là Aluminum (Nhôm - Al).""",

        "cau_hoi": [
            {"nd": "Nguyên tử mang điện tích gì?","da": ["Điện tích dương","Điện tích âm","Trung hòa về điện","Phụ thuộc vào nhiệt độ"],"d": 2,"gt": "Nguyên tử luôn có số p = số e nên trung hòa về điện."},
            {"nd": "Hạt nhân nguyên tử được cấu tạo bởi những loại hạt nào?","da": ["Chỉ có hạt proton","Hạt proton và hạt electron","Hạt proton và hạt neutron","Hạt electron và hạt neutron"],"d": 2,"gt": "Hạt nhân nằm ở trung tâm chứa p và n."},
            {"nd": "Hạt nào sau đây mang điện tích âm?","da": ["Proton","Neutron","Electron","Hạt nhân"],"d": 2,"gt": "Electron (e) mang điện tích -1."},
            {"nd": "Nguyên tố hóa học là tập hợp các nguyên tử có cùng:","da": ["Số neutron","Số proton","Khối lượng nguyên tử","Số lớp electron"],"d": 1,"gt": "Định nghĩa nguyên tố hóa học dựa trên số proton."},
            {"nd": "Khối lượng của nguyên tử tập trung chủ yếu ở phần nào?","da": ["Lớp vỏ electron","Hạt nhân","Khoảng không gian rỗng","Chia đều cho vỏ và hạt nhân"],"d": 1,"gt": "Khối lượng e rất nhỏ (chỉ bằng 1/1836 khối lượng p) nên xem như khối lượng nguyên tử bằng khối lượng hạt nhân."},
            {"nd": "Số thứ tự của ô nguyên tố trong Bảng tuần hoàn bằng với đại lượng nào sau đây?","da": ["Số hiệu nguyên tử (Số proton)","Số lớp electron","Số nơtron","Khối lượng nguyên tử"],"d": 0,"gt": "Số TT ô = Z = p = e."},
            {"nd": "Chu kì là tập hợp các nguyên tố hóa học mà nguyên tử của chúng có cùng:","da": ["Số electron lớp ngoài cùng","Số proton","Số neutron","Số lớp electron"],"d": 3,"gt": "Các nguyên tố có cùng số lớp e được xếp thành một hàng ngang gọi là chu kì."},
            {"nd": "Kí hiệu hóa học của nguyên tố Iron (Sắt) theo danh pháp IUPAC là gì?","da": ["I","Ir","Fe","S"],"d": 2,"gt": "Iron có kí hiệu là Fe (từ tiếng Latin Ferrum)."},
            {"nd": "Nguyên tố Calcium có kí hiệu hóa học là gì?","da": ["C","Ca","Cu","Cl"],"d": 1,"gt": "Calcium (Canxi) có kí hiệu là Ca."},
            {"nd": "Đơn vị khối lượng nguyên tử được kí hiệu là gì?","da": ["kg","gam","amu","ml"],"d": 2,"gt": "Đơn vị là amu (atomic mass unit)."},
            {"nd": "Trong Bảng tuần hoàn, các nguyên tố khí hiếm nằm ở nhóm nào?","da": ["Nhóm IA","Nhóm VIIA","Nhóm VIIIA","Nhóm IIA"],"d": 2,"gt": "Khí hiếm nằm ở cột cuối cùng bên phải, Nhóm VIIIA."},
            {"nd": "Một nguyên tử có 8 proton, 8 electron và 8 neutron. Khối lượng nguyên tử này xấp xỉ bằng bao nhiêu amu?","da": ["8 amu","16 amu","24 amu","0 amu"],"d": 1,"gt": "Khối lượng ≈ p + n = 8 + 8 = 16 amu."},
            {"nd": "Nguyên tử X có 12 electron. X nằm ở chu kì mấy trong Bảng tuần hoàn?","da": ["Chu kì 1","Chu kì 2","Chu kì 3","Chu kì 4"],"d": 2,"gt": "12e được xếp vào 3 lớp (2, 8, 2) ⇒ Chu kì 3."},
            {"nd": "Nhóm VIIA trong Bảng tuần hoàn gồm các nguyên tố được gọi là:","da": ["Kim loại kiềm","Khí hiếm","Halogen","Kim loại kiềm thổ"],"d": 2,"gt": "Nhóm VIIA là nhóm Halogen (Phi kim hoạt động mạnh)."},
            {"nd": "Hạt neutron mang điện tích gì?","da": ["Điện tích dương","Điện tích âm","Không mang điện","Điện tích thay đổi"],"d": 2,"gt": "Neutron là hạt không mang điện (neutral)."},
            {"nd": "Lớp electron thứ nhất (lớp trong cùng gần hạt nhân nhất) chứa tối đa bao nhiêu electron?","da": ["2","8","18","32"],"d": 0,"gt": "Lớp thứ nhất chỉ chứa tối đa 2 electron."},
            {"nd": "Nhóm A trong Bảng tuần hoàn là tập hợp các nguyên tố có cùng:","da": ["Số lớp electron","Số electron lớp ngoài cùng","Số proton","Số neutron"],"d": 1,"gt": "Các nguyên tố trong cùng một nhóm A có cùng số electron ở lớp vỏ ngoài cùng."},
            {"nd": "Nguyên tố C (Carbon) ở ô số 6. Hỏi nguyên tử Carbon có bao nhiêu electron?","da": ["12","6","3","4"],"d": 1,"gt": "Số TT ô = Số electron = 6."},
            {"nd": "Đa số các nguyên tố phi kim nằm ở khu vực nào của Bảng tuần hoàn?","da": ["Bên trái","Ở giữa","Bên phải","Dưới cùng"],"d": 2,"gt": "Phi kim chủ yếu nằm ở phía trên, bên phải của Bảng tuần hoàn."},
            {"nd": "Nguyên tố Hydrogen (H) nằm ở vị trí nào trong Bảng tuần hoàn?","da": ["Ô số 1, chu kì 1, nhóm IA","Ô số 2, chu kì 1, nhóm VIIIA","Ô số 1, chu kì 2, nhóm IA","Ô số 1, chu kì 1, nhóm VIIA"],"d": 0,"gt": "H có Z=1, 1 lớp e, 1 e lớp ngoài cùng."},
            {"nd": "Nhà bác học nào được coi là 'cha đẻ' của Bảng tuần hoàn các nguyên tố hóa học?","da": ["Isaac Newton","Albert Einstein","Dmitri Mendeleev","Marie Curie"],"d": 2,"gt": "Mendeleev (người Nga) đã công bố bảng tuần hoàn đầu tiên năm 1869."},
            {"nd": "Các nguyên tố Kim loại kiềm (như Li, Na, K) có bao nhiêu electron ở lớp ngoài cùng?","da": ["1","2","3","7"],"d": 0,"gt": "Kim loại kiềm nằm ở Nhóm IA nên có 1 electron lớp ngoài cùng."},
            {"nd": "Kí hiệu O biểu diễn cho nguyên tố nào?","da": ["Osmium","Oxygen","Oganesson","Vàng"],"d": 1,"gt": "O là kí hiệu của Oxygen (Oxi)."},
            {"nd": "Kí hiệu Na biểu diễn cho nguyên tố nào?","da": ["Nitrogen","Neon","Sodium","Niken"],"d": 2,"gt": "Na là kí hiệu của Sodium (Natri)."},
            {"nd": "Trong Bảng tuần hoàn có bao nhiêu chu kì?","da": ["7","8","18","10"],"d": 0,"gt": "Bảng tuần hoàn hiện tại có 7 chu kì."},
            {"nd": "Hạt nhân nguyên tử Helium có 2 proton. Vậy lớp vỏ nguyên tử Helium có bao nhiêu electron?","da": ["1","2","3","4"],"d": 1,"gt": "Nguyên tử trung hòa về điện nên số e = số p = 2."},
            {"nd": "Một nguyên tử có 3 lớp electron. Lớp ngoài cùng có 7 electron. Nguyên tố đó là kim loại hay phi kim?","da": ["Kim loại","Phi kim","Khí hiếm","Á kim"],"d": 1,"gt": "Các nguyên tố có 5, 6, 7 electron lớp ngoài cùng thường là Phi kim."},
            {"nd": "Lớp electron thứ hai chứa tối đa bao nhiêu electron?","da": ["2","8","18","32"],"d": 1,"gt": "Lớp thứ 2 chứa tối đa 8 electron."},
            {"nd": "Kí hiệu hóa học của nguyên tố Bạc (Silver) là?","da": ["Au","Ag","Cu","Al"],"d": 1,"gt": "Kí hiệu của Bạc là Ag (Argentum)."},
            {"nd": "Khẳng định nào sai khi nói về nguyên tố hóa học?","da": ["Nguyên tố là tập hợp các nguyên tử cùng loại","Các nguyên tử của cùng 1 nguyên tố có cùng số p","Các nguyên tử của cùng 1 nguyên tố bắt buộc phải có cùng số n","Hiện nay đã biết hơn 118 nguyên tố"],"d": 2,"gt": "Các nguyên tử cùng nguyên tố có thể có số nơtron khác nhau (gọi là đồng vị)."}
        ],

        "bt_co_ban": [
            {"de": "Hãy cho biết hạt nào mang điện tích dương, hạt nào mang điện tích âm và hạt nào không mang điện trong nguyên tử?","dd": ["Proton mang điện dương, Electron mang điện âm, Neutron không mang điện."],"gt": "Lý thuyết cấu tạo nguyên tử."},
            {"de": "Nguyên tử Magnesium (Mg) có 12 proton. Cho biết số electron và số hiệu nguyên tử của Mg.","dd": ["Số electron = 12; Số hiệu nguyên tử (Z) = 12."],"gt": "Số Z = Số p = Số e."},
            {"de": "Một nguyên tử X có 8 proton và 8 neutron. Tính khối lượng nguyên tử X (theo amu).","dd": ["16 amu"],"gt": "Khối lượng ≈ p + n = 8 + 8 = 16 amu."},
            {"de": "Xác định chu kì và nhóm của nguyên tố có 3 lớp electron, trong đó lớp ngoài cùng có 1 electron.","dd": ["Chu kì 3, Nhóm IA"],"gt": "3 lớp e ⇒ Chu kì 3; 1 e lớp ngoài cùng ⇒ Nhóm IA."},
            {"de": "Viết kí hiệu hóa học của các nguyên tố: Carbon, Nitrogen, Oxygen, Sodium.","dd": ["C, N, O, Na"],"gt": "Theo danh pháp IUPAC."},
            {"de": "Đọc tên các nguyên tố có kí hiệu hóa học sau: K, Ca, Fe, Cu.","dd": ["Potassium, Calcium, Iron, Copper"],"gt": "K là Kali (Potassium), Ca là Canxi (Calcium), Fe là Sắt (Iron), Cu là Đồng (Copper)."},
            {"de": "Cho biết nguyên tố Chlorine (Cl) ở ô số 17. Cho biết nguyên tử Cl có bao nhiêu lớp electron và bao nhiêu electron lớp ngoài cùng?","dd": ["Có 3 lớp electron, 7 electron lớp ngoài cùng"],"gt": "17e xếp thành 3 lớp: 2, 8, 7."},
            {"de": "Nguyên tố nào trong Bảng tuần hoàn có nguyên tử nhẹ nhất (chỉ có 1 proton)?","dd": ["Hydrogen (H)"],"gt": "H nằm ở ô số 1, là nguyên tố nhẹ nhất vũ trụ."},
            {"de": "Dựa vào số electron lớp ngoài cùng, hãy phân loại: Nguyên tử X (1e), Nguyên tử Y (7e), Nguyên tử Z (8e).","dd": ["X là Kim loại; Y là Phi kim; Z là Khí hiếm"],"gt": "1,2,3e là Kim loại; 5,6,7e là Phi kim; 8e là Khí hiếm."},
            {"de": "Nguyên tử X nặng gấp 2 lần nguyên tử Carbon (C=12amu). Xác định khối lượng nguyên tử X và cho biết X là nguyên tố nào?","dd": ["24 amu; Magnesium (Mg)"],"gt": "12 × 2 = 24 amu. Nguyên tố khối lượng 24 là Mg."}
        ],

        "bt_nang_cao": [
            {"de": "Tổng số hạt trong nguyên tử của nguyên tố A là 28. Trong đó số hạt không mang điện chiếm xấp xỉ 35,7%. Xác định số p, e, n của A.","hd": "Lập phương trình: p + e + n = 28 và n = 35,7% . 28.","dd": ["p = e = 9; n = 10"],"lg": "Số n = 28 . 35,7% ≈ 10. Mà 2p + n = 28 ⇒ 2p + 10 = 28 ⇒ 2p = 18 ⇒ p = 9. Vậy p=9, e=9, n=10 (Fluorine - F)."},
            {"de": "Nguyên tử M có tổng số hạt là 58. Biết số hạt mang điện nhiều hơn số hạt không mang điện là 18. Tìm vị trí của M trong Bảng tuần hoàn.","hd": "Giải hệ phương trình tìm p. Sau đó phân bố e để tìm Chu kì, Nhóm.","dd": ["Ô 19, Chu kì 4, Nhóm IA"],"lg": "2p + n = 58 và 2p - n = 18. Cộng lại: 4p = 76 ⇒ p = 19. M có 19e, phân bố: 2, 8, 8, 1. Vậy M ở Ô 19, Chu kì 4, Nhóm IA (Potassium - K)."},
            {"de": "Tổng số hạt trong nguyên tử X là 34. Hạt nhân của X có số proton ít hơn số neutron là 1 hạt. Tìm X.","hd": "2p + n = 34 và n - p = 1.","dd": ["X là Sodium (Na)"],"lg": "2p + n = 34. Thay n = p + 1 vào: 2p + p + 1 = 34 ⇒ 3p = 33 ⇒ p = 11. Số Z=11 là Sodium (Na)."},
            {"de": "Hợp chất AB2 có tổng số hạt proton là 22. Biết A ở chu kì 2, nhóm IVA. Xác định nguyên tố B.","hd": "A ở chu kì 2 nhóm IVA ⇒ A là Carbon (Z=6). Tổng Z_A + 2.Z_B = 22.","dd": ["B là Oxygen (O)"],"lg": "A là Carbon có 6 proton. 6 + 2.p_B = 22 ⇒ 2.p_B = 16 ⇒ p_B = 8. Z=8 là nguyên tố Oxygen (O). Hợp chất là CO2."},
            {"de": "Hai nguyên tố A và B đứng kế tiếp nhau trong cùng một chu kì của Bảng tuần hoàn. Tổng số điện tích hạt nhân của chúng là 25. Xác định A và B.","hd": "Kế tiếp trong 1 chu kì nghĩa là Z_B - Z_A = 1.","dd": ["Magnesium (Mg) và Aluminum (Al)"],"lg": "Hệ PT: Z_A + Z_B = 25 và -Z_A + Z_B = 1. Cộng lại: 2.Z_B = 26 ⇒ Z_B = 13 (Al). Suy ra Z_A = 12 (Mg)."},
            {"de": "Nguyên tử X có 3 lớp electron và có tính phi kim mạnh. Biết lớp ngoài cùng của X có 7 electron. Tính tổng số hạt mang điện của X.","hd": "Xác định tổng số e rồi nhân 2 (vì có cả p và e).","dd": ["34 hạt"],"lg": "Phân bố e: 2, 8, 7 ⇒ Tổng số e = 17. Số p = 17. Tổng số hạt mang điện = 17 + 17 = 34."},
            {"de": "Một nguyên tử Y có tổng số hạt là 52. Số hạt không mang điện gấp 1,06 lần số hạt mang điện dương. Khối lượng nguyên tử của Y là bao nhiêu?","hd": "2p + n = 52 và n = 1,06p.","dd": ["35 amu"],"lg": "2p + 1,06p = 52 ⇒ 3,06p = 52 ⇒ p ≈ 17. n = 52 - 34 = 18. Khối lượng ≈ p + n = 17 + 18 = 35 amu (Chlorine)."},
            {"de": "Hai nguyên tố X, Y thuộc cùng một nhóm A ở hai chu kì liên tiếp nhau. Tổng số proton của X và Y là 32. Xác định X, Y.","hd": "Cùng nhóm A liên tiếp chu kì thường cách nhau 8 (hoặc 18) nguyên tố. Giả sử Z_Y - Z_X = 8.","dd": ["Magnesium (Mg) và Calcium (Ca)"],"lg": "Z_X + Z_Y = 32 và Z_Y - Z_X = 8. Cộng lại: 2.Z_Y = 40 ⇒ Z_Y = 20 (Ca). Suy ra Z_X = 12 (Mg). Ca và Mg cùng thuộc nhóm IIA."},
            {"de": "Trong nguyên tử của nguyên tố R, tổng số hạt cơ bản là 115. Trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 25. Xác định số e của R.","hd": "2p + n = 115 và 2p - n = 25.","dd": ["e = 35"],"lg": "Cộng hai PT: 4p = 140 ⇒ p = 35 ⇒ e = 35. (Nguyên tố Bromine)."},
            {"de": "Nguyên tố X có số hiệu nguyên tử là 20. Trình bày sự phân bố electron vào các lớp và cho biết X dễ nhường hay nhận electron?","hd": "Lớp 1: 2e, Lớp 2: 8e, Lớp 3: 8e, Lớp 4: 2e.","dd": ["2, 8, 8, 2. X dễ nhường 2 electron."],"lg": "Z=20 phân bố: 2, 8, 8, 2. Vì có 2 electron lớp ngoài cùng (Kim loại) nên X có xu hướng nhường 2e để đạt cấu hình bền 8e của khí hiếm."},
            {"de": "Vì sao các nguyên tố ở Nhóm VIIIA (Khí hiếm) lại rất trơ về mặt hóa học (hầu như không phản ứng với chất khác)?","hd": "Quan sát số electron lớp ngoài cùng.","dd": ["Vì chúng đã có lớp vỏ ngoài cùng bền vững (đủ 8 electron)."],"lg": "Ngoại trừ Helium có 2e, các khí hiếm khác đều có 8 electron ở lớp vỏ ngoài cùng, đây là cấu hình năng lượng rất bền vững nên chúng không có nhu cầu nhường hay nhận thêm electron."},
            {"de": "Nguyên tử nguyên tố A nặng gấp 2 lần nguyên tử Nitrogen (N=14). Tính số hạt proton của A biết A có số p bằng số n.","hd": "Khối lượng A = 28 amu.","dd": ["14 proton"],"lg": "M_A = 2 × 14 = 28. Ta có p + n = 28, mà p = n ⇒ 2p = 28 ⇒ p = 14. A là Silicon (Si)."},
            {"de": "Nguyên tử X có tổng số hạt là 21. Tìm số hiệu nguyên tử của X. (Sử dụng bất đẳng thức p ≤ n ≤ 1,5p).","hd": "Từ 2p + n = 21 ⇒ n = 21 - 2p. Thay vào BĐT p ≤ 21 - 2p ≤ 1,5p.","dd": ["Z = 6 hoặc Z = 7"],"lg": "Giải BĐT: 3p ≤ 21 ⇒ p ≤ 7. Và 3,5p ≥ 21 ⇒ p ≥ 6. Vậy p có thể là 6 (C) hoặc 7 (N)."},
            {"de": "Trong các hạt p, n, e, hạt nào quyết định tính chất hóa học của một nguyên tử? Giải thích.","hd": "Hạt nằm ở vỏ.","dd": ["Electron (Đặc biệt là electron lớp ngoài cùng)."],"lg": "Các phản ứng hóa học bản chất là sự nhường, nhận hoặc dùng chung electron ở lớp vỏ ngoài cùng. Do đó, số e lớp ngoài cùng quyết định tính chất hóa học (kim loại, phi kim hay khí hiếm)."},
            {"de": "Khối lượng nguyên tử của Oxygen là 16 amu. Biết 1 amu ≈ 1,66 × 10^-24 gam. Tính khối lượng thực của 1 nguyên tử Oxygen ra gam.","hd": "Phép nhân cơ bản.","dd": ["2,656 × 10^-23 gam"],"lg": "M = 16 × 1,66 × 10^-24 = 26,56 × 10^-24 = 2,656 × 10^-23 (gam)."},
            {"de": "Tại sao trong bảng tuần hoàn, chu kì 1 chỉ có 2 nguyên tố, chu kì 2 và 3 có 8 nguyên tố?","hd": "Liên quan đến sức chứa tối đa của các lớp vỏ electron.","dd": ["Do lớp thứ nhất chỉ chứa tối đa 2e, lớp thứ 2 chứa tối đa 8e..."],"lg": "Số lượng nguyên tố trong một chu kì đúng bằng số lượng electron tối đa có thể điền vào lớp vỏ tương ứng với chu kì đó."},
            {"de": "Đồng vị là gì? Cho ví dụ về đồng vị của Carbon.","hd": "Cùng p, khác n.","dd": ["Đồng vị là những nguyên tử có cùng số proton nhưng khác số neutron."],"lg": "Ví dụ Carbon có C-12 (6p, 6n) và C-14 (6p, 8n). Chúng đều nằm ở ô số 6 nhưng khối lượng khác nhau."},
            {"de": "Một hợp chất có công thức XY2. Tổng số proton trong phân tử là 22. Biết X nằm ở ô số 6. Y là nguyên tố nào?","hd": "Z_X + 2.Z_Y = 22.","dd": ["Oxygen (O)"],"lg": "X là Carbon (Z=6). Suy ra 6 + 2.Z_Y = 22 ⇒ 2.Z_Y = 16 ⇒ Z_Y = 8. Z=8 là O. Hợp chất là CO2."},
            {"de": "Trong một kì thi, học sinh ghi kí hiệu Canxi là cA, Sắt là fE. Em hãy sửa lại cho đúng và nhắc lại quy tắc viết kí hiệu hóa học IUPAC.","hd": "Chữ cái đầu viết hoa, chữ cái sau viết thường.","dd": ["Ca, Fe"],"lg": "Quy tắc: Kí hiệu hóa học gồm 1 hoặc 2 chữ cái. Chữ cái đầu tiên luôn in hoa, chữ cái thứ hai (nếu có) viết thường."}
        ]
    }
}
H7["Chương 1: Nguyên tử. Bảng tuần hoàn"] = C1_H7

# --- Chương 2: Phân tử. Liên kết hóa học ---
C2_H7 = {
    "Phân tử, Liên kết hóa học và Công thức hóa học (Chuyên sâu)": {
        "ly_thuyet": """📌 1. ĐƠN CHẤT VÀ HỢP CHẤT - PHÂN TỬ:
- Đơn chất: Là những chất được tạo nên từ 1 nguyên tố hóa học. VD: O₂, Fe, H₂.
- Hợp chất: Là những chất được tạo nên từ 2 nguyên tố hóa học trở lên. VD: H₂O, NaCl, CaCO₃.
- Phân tử: Là hạt đại diện cho chất, gồm một số nguyên tử liên kết với nhau.
- Khối lượng phân tử (amu): Bằng tổng khối lượng của các nguyên tử có trong phân tử.

📌 2. LIÊN KẾT ION:
- Hình thành bởi lực hút tĩnh điện giữa các ion mang điện tích trái dấu.
- Cơ chế: Kim loại nhường electron (tạo ion dương), Phi kim nhận electron (tạo ion âm). Hai ion trái dấu hút nhau.
- Hợp chất ion thường ở thể rắn, tan trong nước, nóng chảy ở nhiệt độ rất cao. VD: Muối ăn NaCl.

📌 3. LIÊN KẾT CỘNG HÓA TRỊ:
- Hình thành bởi sự dùng chung một hay nhiều cặp electron giữa các nguyên tử.
- Thường xảy ra giữa các nguyên tử phi kim với nhau. VD: Phân tử nước (H₂O), khí Oxygen (O₂).

📌 4. HÓA TRỊ VÀ QUY TẮC HÓA TRỊ:
- Hóa trị là con số biểu thị khả năng liên kết của nguyên tử nguyên tố này với nguyên tử nguyên tố khác.
- Quy ước: Hóa trị của H luôn là I; hóa trị của O thường là II.
- Quy tắc hóa trị: Trong hợp chất A_x B_y (a là hóa trị của A, b là hóa trị của B), ta luôn có tích: x . a = y . b.
- Lập công thức hóa học: Áp dụng quy tắc chéo, chỉ số của nguyên tố này bằng hóa trị của nguyên tố kia (rút gọn nếu cần).""",
        
        "vi_du": """💡 VÍ DỤ 1: Tính Khối lượng phân tử
Đề bài: Tính khối lượng phân tử của Sulfuric acid có công thức là H₂SO₄. Biết khối lượng nguyên tử H=1, S=32, O=16 (amu).
- Giải:
  Phân tử H₂SO₄ gồm 2 nguyên tử H, 1 nguyên tử S và 4 nguyên tử O.
  Khối lượng phân tử = 2 . 1 + 1 . 32 + 4 . 16 = 2 + 32 + 64 = 98 (amu).

💡 VÍ DỤ 2: Lập công thức hóa học dựa vào hóa trị
Đề bài: Lập công thức hóa học của hợp chất tạo bởi Aluminum (Al hóa trị III) và Oxygen (O hóa trị II).
- Giải:
  + Công thức dạng chung: Al_x O_y
  + Theo quy tắc hóa trị: x . III = y . II.
  + Chuyển thành tỉ lệ: x / y = II / III = 2 / 3.
  + Chọn x = 2, y = 3. 
  + Công thức hóa học là Al₂O₃.

💡 VÍ DỤ 3: Cơ chế hình thành liên kết ion
Đề bài: Trình bày sự hình thành liên kết ion trong phân tử Magnesium oxide (MgO). Biết Mg (Z=12), O (Z=8).
- Giải:
  + Mg có 2 electron lớp ngoài cùng ⇒ Nhường 2e để trở thành ion Mg²⁺.
  + O có 6 electron lớp ngoài cùng ⇒ Nhận 2e để trở thành ion O²⁻.
  + Hai ion trái dấu Mg²⁺ và O²⁻ hút nhau bằng lực tĩnh điện tạo thành phân tử MgO.""",

        "cau_hoi": [
            {"nd": "Chất nào sau đây là đơn chất?","da": ["Nước (H₂O)","Khí Oxygen (O₂)","Muối ăn (NaCl)","Đá vôi (CaCO₃)"],"d": 1,"gt": "Đơn chất được tạo từ 1 nguyên tố hóa học. O₂ chỉ có nguyên tố O."},
            {"nd": "Chất nào sau đây là hợp chất?","da": ["Khí Hydrogen (H₂)","Đồng (Cu)","Khí Carbon dioxide (CO₂)","Ozone (O₃)"],"d": 2,"gt": "Hợp chất tạo từ 2 nguyên tố trở lên. CO₂ được tạo từ C và O."},
            {"nd": "Khối lượng phân tử của nước (H₂O) là bao nhiêu amu? Biết H=1, O=16.","da": ["17 amu","18 amu","33 amu","32 amu"],"d": 1,"gt": "2.1 + 16 = 18 amu."},
            {"nd": "Liên kết hóa học trong phân tử muối ăn (NaCl) là loại liên kết gì?","da": ["Liên kết cộng hóa trị","Liên kết kim loại","Liên kết ion","Liên kết Hydrogen"],"d": 2,"gt": "Na (kim loại) nhường e cho Cl (phi kim) tạo thành các ion hút nhau."},
            {"nd": "Liên kết cộng hóa trị được hình thành nhờ cơ chế nào?","da": ["Lực hút tĩnh điện giữa các ion","Sự dùng chung các cặp electron","Sự nhường hoàn toàn electron","Sự đứt gãy liên kết"],"d": 1,"gt": "Cộng hóa trị là góp chung electron để xài chung."},
            {"nd": "Theo quy ước, hóa trị của Hydrogen (H) và Oxygen (O) trong các hợp chất thường là bao nhiêu?","da": ["H hóa trị I, O hóa trị I","H hóa trị II, O hóa trị I","H hóa trị I, O hóa trị II","H hóa trị II, O hóa trị II"],"d": 2,"gt": "Quy ước làm cơ sở để tính hóa trị các chất khác."},
            {"nd": "Trong hợp chất A_x B_y (với a, b lần lượt là hóa trị của A, B), quy tắc hóa trị được viết là:","da": ["x + a = y + b","x . b = y . a","x . a = y . b","a / x = b / y"],"d": 2,"gt": "Tích của chỉ số và hóa trị của nguyên tố này bằng tích của chỉ số và hóa trị nguyên tố kia."},
            {"nd": "Hóa trị của Carbon (C) trong hợp chất CO₂ là bao nhiêu? (Biết O hóa trị II)","da": ["I","II","III","IV"],"d": 3,"gt": "Gọi hóa trị C là a. Ta có a.1 = II.2 ⇒ a = IV."},
            {"nd": "Công thức hóa học của hợp chất tạo bởi Fe (hóa trị III) và Cl (hóa trị I) là?","da": ["FeCl","FeCl₂","FeCl₃","Fe₃Cl"],"d": 2,"gt": "Quy tắc chéo: Fe mang chỉ số của Cl (là 1), Cl mang chỉ số của Fe (là 3) ⇒ FeCl₃."},
            {"nd": "Khối lượng phân tử của khí Carbon dioxide (CO₂) là bao nhiêu? Biết C=12, O=16.","da": ["28 amu","44 amu","12 amu","32 amu"],"d": 1,"gt": "12 + 16.2 = 44 amu."},
            {"nd": "Phân tử nào sau đây có chứa liên kết cộng hóa trị?","da": ["KCl","MgCl₂","H₂O","Na₂O"],"d": 2,"gt": "Nước (H₂O) tạo bởi 2 phi kim là H và O, dùng chung electron."},
            {"nd": "Hợp chất có công thức SO₃, hóa trị của S là bao nhiêu?","da": ["II","III","IV","VI"],"d": 3,"gt": "Gọi hóa trị S là a: a.1 = II.3 ⇒ a = VI."},
            {"nd": "Kí hiệu O₂ chỉ điều gì?","da": ["1 nguyên tử Oxygen","1 phân tử khí Oxygen gồm 2 nguyên tử O","2 phân tử Oxygen","2 hợp chất Oxygen"],"d": 1,"gt": "Chỉ số 2 ở chân chữ O có nghĩa là có 2 nguyên tử O liên kết tạo thành 1 phân tử."},
            {"nd": "Các hợp chất ion (như muối ăn NaCl) thường có đặc điểm gì ở nhiệt độ thường?","da": ["Thể khí","Thể lỏng","Thể rắn","Dễ bay hơi"],"d": 2,"gt": "Hợp chất ion có mạng lưới tinh thể rất bền vững nên thường ở thể rắn."},
            {"nd": "Một nguyên tử phi kim thường có xu hướng gì để đạt cấu hình electron bền vững?","da": ["Nhường electron","Nhận thêm electron","Mất hết lớp vỏ electron","Không thay đổi"],"d": 1,"gt": "Phi kim (có 5,6,7 e lớp ngoài) có xu hướng nhận e để đủ 8e."},
            {"nd": "Kim loại kiềm (nhóm IA) có hóa trị mấy trong hợp chất?","da": ["I","II","III","IV"],"d": 0,"gt": "Nhóm IA có 1 electron lớp ngoài cùng nên có hóa trị I."},
            {"nd": "Khối lượng phân tử của Sulfuric acid (H₂SO₄) là? (H=1, S=32, O=16)","da": ["98 amu","49 amu","96 amu","100 amu"],"d": 0,"gt": "1.2 + 32 + 16.4 = 98 amu."},
            {"nd": "Nhóm (SO₄) có hóa trị II. Hóa trị của Al trong hợp chất Al₂(SO₄)₃ là?","da": ["I","II","III","IV"],"d": 2,"gt": "a.2 = II.3 ⇒ 2a = 6 ⇒ a = III."},
            {"nd": "Liên kết trong phân tử khí Nitrogen (N₂) là liên kết dùng chung bao nhiêu cặp electron?","da": ["1 cặp","2 cặp","3 cặp","4 cặp"],"d": 2,"gt": "Mỗi nguyên tử N có 5e lớp ngoài cùng, cần thêm 3e nên chúng dùng chung 3 cặp electron (Liên kết ba)."},
            {"nd": "Trong phân tử HCl, cặp electron dùng chung sẽ bị lệch về phía nguyên tử nào?","da": ["Lệch về phía H","Lệch về phía Cl","Nằm chính giữa","Không có cặp electron dùng chung"],"d": 1,"gt": "Cl có độ âm điện lớn hơn (hút e mạnh hơn) nên cặp e bị lệch về phía Cl."},
            {"nd": "Chất nào sau đây hòa tan tốt trong nước tạo thành dung dịch dẫn điện?","da": ["Dầu ăn","Đường (C₁₂H₂₂O₁₁)","Muối ăn (NaCl)","Bột mì"],"d": 2,"gt": "Hợp chất ion NaCl khi tan trong nước sẽ phân li thành các ion tự do có khả năng dẫn điện."},
            {"nd": "Cách viết '5 Cu' có ý nghĩa là gì?","da": ["5 phân tử Đồng","5 nguyên tử Đồng","5 hợp chất Đồng","Nguyên tố Đồng có hóa trị V"],"d": 1,"gt": "Đồng là kim loại, hạt đại diện là nguyên tử. '5 Cu' nghĩa là 5 nguyên tử Đồng."},
            {"nd": "Công thức hóa học của Methane là CH₄. Hỏi có bao nhiêu nguyên tử H trong 3 phân tử Methane?","da": ["3","4","7","12"],"d": 3,"gt": "1 phân tử có 4 H. 3 phân tử sẽ có 3 x 4 = 12 nguyên tử H."},
            {"nd": "Công thức hóa học nào viết SAI? (Biết K hóa trị I, O hóa trị II)","da": ["K₂O","KO₂","KCl","KOH"],"d": 1,"gt": "K hóa trị I, O hóa trị II. Công thức đúng phải là K₂O. KO₂ là dạng siêu oxit không phổ biến ở mức cơ bản."},
            {"nd": "Khí hiếm Neon (Ne) tồn tại ở dạng nào trong tự nhiên?","da": ["Phân tử Ne₂","Phân tử Ne₃","Nguyên tử độc lập Ne","Hợp chất ion"],"d": 2,"gt": "Khí hiếm đã bền vững nên không tạo liên kết, tồn tại ở dạng nguyên tử độc lập."},
            {"nd": "Hóa trị của S trong hợp chất H₂S là?","da": ["I","II","III","IV"],"d": 1,"gt": "H hóa trị I. 1.2 = a.1 ⇒ a = II."},
            {"nd": "Dấu hiệu nhận biết liên kết ion là nó thường xảy ra giữa:","da": ["Phi kim với Phi kim","Kim loại điển hình với Phi kim điển hình","Kim loại với Kim loại","Khí hiếm với Kim loại"],"d": 1,"gt": "Sự chênh lệch lực hút electron giữa Kim loại và Phi kim tạo ra việc nhường và nhận e."},
            {"nd": "Phân tử khối của đá vôi (CaCO₃) là? (Ca=40, C=12, O=16)","da": ["68 amu","100 amu","112 amu","84 amu"],"d": 1,"gt": "40 + 12 + 16.3 = 100 amu."},
            {"nd": "Nhóm Hydroxide (OH) có hóa trị I. Công thức đúng của Magnesium hydroxide là? (Mg hóa trị II)","da": ["MgOH","Mg₂OH","Mg(OH)₂","Mg(OH)₃"],"d": 2,"gt": "Theo quy tắc chéo: Mg(OH)₂."},
            {"nd": "Số Avogadro biểu thị số lượng hạt trong 1 mol chất. Đơn vị amu có mối liên hệ thế nào với gam?","da": ["1 amu = 1 gam","1 amu = 1 kg","Giá trị số của phân tử khối tính bằng amu đúng bằng khối lượng mol tính bằng g/mol","Không có liên hệ"],"d": 2,"gt": "Phân tử khối (amu) có cùng giá trị số học với Khối lượng mol (g/mol). VD: H₂O = 18 amu ⇒ 1 mol H₂O nặng 18 gam."}
        ],

        "bt_co_ban": [
            {"de": "Phân loại các chất sau đây thành Đơn chất và Hợp chất: O₂, NaCl, Cl₂, H₂O, Fe, CaCO₃.","dd": ["Đơn chất: O₂, Cl₂, Fe. Hợp chất: NaCl, H₂O, CaCO₃."],"gt": "Đơn chất gồm 1 kí hiệu hóa học. Hợp chất từ 2 kí hiệu trở lên."},
            {"de": "Tính khối lượng phân tử của các chất sau: Khí Oxygen (O₂), Khí Nitrogen (N₂). Biết O=16, N=14.","dd": ["O₂ = 32 amu; N₂ = 28 amu"],"gt": "16 . 2 = 32. 14 . 2 = 28."},
            {"de": "Xác định hóa trị của N trong hợp chất NH₃. Biết H hóa trị I.","dd": ["N hóa trị III"],"gt": "Gọi hóa trị N là a. a.1 = I.3 ⇒ a = III."},
            {"de": "Lập công thức hóa học của hợp chất tạo bởi K (hóa trị I) và nhóm SO₄ (hóa trị II).","dd": ["K₂SO₄"],"gt": "Áp dụng quy tắc chéo: Chỉ số của K là 2, của SO₄ là 1."},
            {"de": "Tính khối lượng phân tử của hợp chất Calcium carbonate (CaCO₃). Biết Ca=40, C=12, O=16.","dd": ["100 amu"],"gt": "40 + 12 + 16.3 = 100."},
            {"de": "Chỉ ra loại liên kết hóa học có trong phân tử Muối ăn (NaCl). Giải thích ngắn gọn.","dd": ["Liên kết ion. Na nhường 1e, Cl nhận 1e tạo thành ion trái dấu hút nhau."],"gt": "Giữa kim loại và phi kim."},
            {"de": "Nêu ý nghĩa của công thức hóa học H₂O.","dd": ["Cho biết H₂O là hợp chất tạo bởi 2 nguyên tố H và O. Một phân tử có 2 nguyên tử H và 1 nguyên tử O. Khối lượng phân tử = 18 amu."],"gt": "Công thức hóa học cho biết 3 ý nghĩa cơ bản."},
            {"de": "Lập công thức hóa học của hợp chất tạo bởi Carbon (hóa trị IV) và Oxygen (hóa trị II).","dd": ["CO₂"],"gt": "C_2 O_4, rút gọn tỉ lệ 2:4 thành 1:2 ⇒ CO₂."},
            {"de": "Xác định hóa trị của Fe trong hợp chất Fe₂O₃.","dd": ["Fe hóa trị III"],"gt": "a.2 = II.3 ⇒ 2a = 6 ⇒ a = III."},
            {"de": "Tính khối lượng của 5 phân tử nước (H₂O).","dd": ["90 amu"],"gt": "1 phân tử H₂O = 18 amu. 5 phân tử = 5 . 18 = 90 amu."}
        ],

        "bt_nang_cao": [
            {"de": "Một hợp chất có phân tử gồm 2 nguyên tử của nguyên tố X liên kết với 1 nguyên tử O và có khối lượng phân tử là 62 amu. Xác định nguyên tố X. (Biết O=16, Na=23, K=39).","hd": "Công thức X₂O. Khối lượng: 2.X + 16 = 62.","dd": ["X là Sodium (Na)"],"lg": "2.X + 16 = 62 ⇒ 2.X = 46 ⇒ X = 23 (amu). So vào bảng nguyên tử khối, X là Sodium (Na)."},
            {"de": "Hợp chất A tạo bởi nguyên tố M hóa trị III và nhóm SO₄ (hóa trị II). Biết phân tử khối của A là 342 amu. Tìm M. (Biết S=32, O=16).","hd": "Lập công thức tổng quát M₂(SO₄)₃.","dd": ["M là Aluminum (Al)"],"lg": "Công thức là M₂(SO₄)₃. Khối lượng = 2.M + (32 + 16.4).3 = 342 ⇒ 2.M + 288 = 342 ⇒ 2.M = 54 ⇒ M = 27. M là Nhôm (Al)."},
            {"de": "Lập công thức hóa học của một hợp chất biết trong đó Nitrogen (N) chiếm 82,35% về khối lượng, còn lại là Hydrogen (H). (Biết N=14, H=1).","hd": "Gọi công thức là N_x H_y. Thiết lập tỉ lệ (x.14)/(y.1) = 82,35 / 17,65.","dd": ["NH₃"],"lg": "%H = 100% - 82,35% = 17,65%. x : y = (82,35 / 14) : (17,65 / 1) ≈ 5,88 : 17,65 ≈ 1 : 3. Vậy công thức đơn giản nhất là NH₃."},
            {"de": "Giải thích vì sao ở điều kiện thường, phân tử N₂ (khí Nitrogen) lại rất trơ (khó tham gia phản ứng hóa học)?","hd": "Dựa vào liên kết cộng hóa trị giữa 2 nguyên tử N.","dd": ["Do giữa 2 nguyên tử N có liên kết ba cực kì bền vững."],"lg": "Trong phân tử N₂, hai nguyên tử N dùng chung tới 3 cặp electron (N≡N). Cần năng lượng rất lớn (nhiệt độ hàng ngàn độ C hoặc tia lửa điện) mới bẻ gãy được liên kết này."},
            {"de": "Hợp chất X có công thức R(OH)₂. Khối lượng phân tử của X là 74 amu. Tìm R. (Biết O=16, H=1).","hd": "R + (16 + 1).2 = 74.","dd": ["R là Calcium (Ca)"],"lg": "R + 17.2 = 74 ⇒ R + 34 = 74 ⇒ R = 40 (amu). R là Calcium (Ca)."},
            {"de": "Nguyên tử A nhường 2 electron để tạo ion, nguyên tử B nhận 1 electron để tạo ion. Hợp chất tạo bởi A và B có công thức chung là gì? Loại liên kết là gì?","hd": "A tạo ion A²⁺, B tạo ion B⁻. Để trung hòa điện tích cần 1 A và 2 B.","dd": ["AB₂. Liên kết ion."],"lg": "A nhường 2e nên mang hóa trị II, B nhận 1e nên mang hóa trị I. Theo quy tắc chéo, công thức là AB₂. Vì có sự nhường và nhận e nên là liên kết ion."},
            {"de": "Xác định hóa trị của nhóm (PO₄) trong hợp chất Ca₃(PO₄)₂. Biết Ca hóa trị II.","hd": "Gọi hóa trị nhóm PO₄ là a.","dd": ["Hóa trị III"],"lg": "3 . II = 2 . a ⇒ a = III."},
            {"de": "Một hợp chất có phân tử gồm 1 nguyên tử X liên kết với 2 nguyên tử O. Phân tử khối của hợp chất nặng gấp 2,75 lần phân tử khối của khí Methane (CH₄). Xác định X. (C=12, H=1).","hd": "Phân tử khối CH₄ = 16. Phân tử khối hợp chất = 16 . 2,75.","dd": ["X là Carbon (C) - Hợp chất là CO₂"],"lg": "M(CH₄) = 12 + 4 = 16. M(hợp chất) = 16 . 2,75 = 44 amu. Công thức XO₂ ⇒ X + 16.2 = 44 ⇒ X = 12 (Carbon)."},
            {"de": "Cho các chất: Nước (H₂O), Muối ăn (NaCl), Đường ăn (C₁₂H₂₂O₁₁), Khí Ammonia (NH₃). Chất nào tan trong nước dẫn được điện? Vì sao?","hd": "Dựa vào loại liên kết ion hay cộng hóa trị.","dd": ["Muối ăn (NaCl)"],"lg": "NaCl là hợp chất ion. Khi tan trong nước, mạng tinh thể bị phá vỡ tạo thành các ion tự do Na⁺ và Cl⁻ di chuyển được, tạo nên dòng điện. Các chất còn lại là cộng hóa trị, không phân li ra ion."},
            {"de": "Lập công thức hóa học của hợp chất sắt oxit, biết khối lượng của Fe và O trong hợp chất tỉ lệ với nhau là 7 : 3. (Biết Fe=56, O=16).","hd": "Tỉ lệ số nguyên tử = Tỉ lệ khối lượng / khối lượng nguyên tử.","dd": ["Fe₂O₃"],"lg": "Gọi CTHH là Fe_x O_y. x : y = (7/56) : (3/16) = 0,125 : 0,1875 = 2 : 3. Công thức là Fe₂O₃."},
            {"de": "Tại sao kim loại có tính dẫn điện tốt? (Mở rộng kiến thức về liên kết kim loại).","hd": "Sự tồn tại của các electron tự do.","dd": ["Vì trong tinh thể kim loại có các electron tự do chuyển động dễ dàng."],"lg": "Các electron lớp ngoài cùng của kim loại bị hạt nhân giữ rất yếu, chúng dễ dàng tách ra tạo thành 'biển electron tự do' mang dòng điện đi khắp vật thể."},
            {"de": "Hợp chất X có công thức M₂O₃. Khối lượng phân tử của M₂O₃ là 102 amu. Trong một hợp chất khác Y gồm M và Cl, biết M giữ nguyên hóa trị. Lập công thức hóa học và tính phân tử khối của Y. (Cl=35,5).","hd": "Tìm M. M hóa trị III.","dd": ["AlCl₃; 133,5 amu"],"lg": "2.M + 16.3 = 102 ⇒ 2.M = 54 ⇒ M = 27 (Nhôm - Al). Trong M₂O₃, M hóa trị III. Công thức với Cl (hóa trị I) là MCl₃ hay AlCl₃. Khối lượng = 27 + 35,5 . 3 = 133,5 amu."},
            {"de": "Tính hóa trị của Fe trong 2 hợp chất sau: FeO và Fe₂O₃. Có nhận xét gì về hóa trị của một nguyên tố?","hd": "Sử dụng quy tắc hóa trị với O (II).","dd": ["FeO: Fe hóa trị II. Fe₂O₃: Fe hóa trị III."],"lg": "Nhận xét: Một nguyên tố hóa học (như Fe) có thể có nhiều hóa trị khác nhau tùy thuộc vào hợp chất mà nó tham gia."},
            {"de": "Nêu 2 điểm khác biệt cơ bản về tính chất vật lí giữa hợp chất ion (vd: NaCl) và hợp chất cộng hóa trị (vd: H₂O, CO₂).","hd": "Thể tồn tại và nhiệt độ nóng chảy.","dd": ["Hợp chất ion: Ở thể rắn, nhiệt độ nóng chảy/sôi rất cao. Hợp chất cộng hóa trị: Có thể ở thể lỏng/khí, nhiệt độ nóng chảy/sôi thấp."],"lg": "Lực hút tĩnh điện trong mạng tinh thể ion rất mạnh, cần nhiều nhiệt để phá vỡ. Liên kết giữa các phân tử cộng hóa trị yếu hơn nhiều."},
            {"de": "Khí A nặng gấp 2 lần khí B. Khí B nhẹ bằng 1/2 khí Oxygen. Tính phân tử khối của A và B. Cho biết A có thể là khí gì?","hd": "O₂ = 32. Tính B, rồi tính A.","dd": ["B = 16 amu; A = 32 amu (Khí O₂)"],"lg": "M_B = 1/2 . 32 = 16 amu. M_A = 2 . M_B = 2 . 16 = 32 amu. A có thể chính là khí Oxygen (O₂)."},
            {"de": "Bột nở (baking powder) có chứa chất X. Phân tử X gồm 1 nguyên tử Na, 1 nguyên tử H, 1 nguyên tử C và 3 nguyên tử O. Viết CTHH và tính phân tử khối của X.","hd": "Viết liền các kí hiệu và chỉ số.","dd": ["NaHCO₃; 84 amu"],"lg": "CTHH: NaHCO₃ (Sodium bicarbonate). Phân tử khối = 23 + 1 + 12 + 16.3 = 84 amu."},
            {"de": "Lập CTHH và tính phân tử khối của hợp chất tạo bởi Calcium (hóa trị II) và nhóm Phosphate (PO₄ - hóa trị III).","hd": "Quy tắc chéo.","dd": ["Ca₃(PO₄)₂; 310 amu"],"lg": "CTHH: Ca₃(PO₄)₂. Khối lượng = 40.3 + (31 + 16.4).2 = 120 + 95.2 = 120 + 190 = 310 amu."},
            {"de": "Phân tử muối ăn tinh khiết được tạo bởi 1 nguyên tử Na và 1 nguyên tử Cl. Khối lượng phân tử của muối ăn là 58,5 amu. Một hạt muối nhỏ nặng 1 gam chứa khoảng bao nhiêu phân tử NaCl? (Biết 1 amu = 1,66.10^-24 gam).","hd": "Tính khối lượng 1 phân tử ra gam, rồi lấy 1 chia cho số đó. (Bài toán tư duy nâng cao)","dd": ["Xấp xỉ 1,03 × 10^22 phân tử"],"lg": "Khối lượng 1 phân tử = 58,5 × 1,66×10^-24 = 97,11 × 10^-24 gam. Số phân tử trong 1 gam = 1 / (97,11 × 10^-24) ≈ 1,03 × 10^22 phân tử. (Một con số khổng lồ!)."},
            {"de": "Trong phân tử CO₂, nguyên tử C nằm ở giữa và liên kết với 2 nguyên tử O ở hai bên. Đây là liên kết cộng hóa trị kép. Hãy vẽ sơ đồ hoặc mô tả sự dùng chung electron giữa C và O. (Biết C có 4e lớp ngoài, O có 6e lớp ngoài).","hd": "C cần 4e, O cần 2e để đủ 8.","dd": ["Xem lời giải"],"lg": "Mỗi nguyên tử O góp 2e chung với C. Nguyên tử C góp 2e cho O thứ nhất và 2e cho O thứ hai. Vậy giữa C và mỗi O có 2 cặp e dùng chung (liên kết đôi: O=C=O). Cả 3 nguyên tử đều đạt cấu hình 8e bền vững."},
            {"de": "Chỉ dùng quy tắc hóa trị, hãy chứng minh CTHH của nước là H₂O chứ không phải HO₂. (Biết H hóa trị I, O hóa trị II).","hd": "Lập tỉ lệ x/y.","dd": ["Xem lời giải"],"lg": "Công thức H_x O_y. Theo quy tắc: x.I = y.II ⇒ x/y = II/I = 2/1. Vậy x=2, y=1 ⇒ H₂O. Không thể là HO₂ vì 1.I ≠ 2.II (1 ≠ 4)."}
        ]
    }
}
H7["Chương 2: Phân tử. Liên kết hóa học"] = C2_H7

HOA["Lớp 7"] = H7