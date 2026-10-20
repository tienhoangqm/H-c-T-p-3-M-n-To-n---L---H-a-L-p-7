# -*- coding: utf-8 -*-
""" NGÂN HÀNG DỮ LIỆU MÔN VẬT LÝ — Bộ sách Kết Nối Tri Thức
Tập trung: VẬT LÝ LỚP 7 (Chuyên sâu)
"""

VATLY = {}

# (Giả sử phía trên này là phần VL6 của lớp 6 anh đã có)

# ==========================================
#                  LỚP 7
# ==========================================
VL7 = {}

# --- Chương 1: Tốc độ chuyển động ---
C1_VL7 = {
    "Tốc độ chuyển động và Đồ thị quãng đường - thời gian (Chuyên sâu)": {
        "ly_thuyet": """📌 1. TỐC ĐỘ CHUYỂN ĐỘNG:
- Khái niệm: Tốc độ là đại lượng cho biết mức độ nhanh hay chậm của chuyển động.
- Công thức tính tốc độ: v = s / t 
  (Trong đó: v là tốc độ, s là quãng đường đi được, t là thời gian đi hết quãng đường đó).
- Đơn vị đo tốc độ: Đơn vị hợp pháp trong hệ SI là mét trên giây (m/s). Trong thực tế thường dùng kilômét trên giờ (km/h).
  + Quy đổi: 1 m/s = 3,6 km/h. Vận tốc âm thanh trong không khí ≈ 340 m/s. Vận tốc ánh sáng ≈ 300.000 km/s.

📌 2. ĐO TỐC ĐỘ:
- Để đo tốc độ trong phòng thực hành, ta có thể dùng: Đồng hồ bấm giây kết hợp thước cuộn, hoặc dùng Cổng quang điện và đồng hồ đo thời gian hiện số.
- Các thiết bị đo tốc độ thực tế: Tốc kế (trên ô tô, xe máy), Súng bắn tốc độ (cảnh sát giao thông sử dụng).

📌 3. ĐỒ THỊ QUÃNG ĐƯỜNG - THỜI GIAN:
- Trục nằm ngang (trục hoành Ot) biểu diễn Thời gian.
- Trục thẳng đứng (trục tung Os) biểu diễn Quãng đường.
- Ý nghĩa đồ thị:
  + Đường biểu diễn là một đường thẳng nằm nghiêng (dốc lên): Vật đang chuyển động với tốc độ không đổi. Đường càng dốc thì tốc độ càng lớn.
  + Đường biểu diễn là một đường thẳng nằm ngang (song song trục Ot): Vật đang đứng yên (quãng đường không thay đổi theo thời gian).

📌 4. AN TOÀN GIAO THÔNG:
- Khoảng cách an toàn: Là khoảng cách tối thiểu cần giữ với xe chạy liền trước để tránh va chạm khi xe trước phanh gấp. Tốc độ càng cao, khoảng cách an toàn phải càng lớn.
- Tuân thủ biển báo tốc độ tối đa cho phép để đảm bảo an toàn cho bản thân và người khác.""",
        
        "vi_du": """💡 VÍ DỤ 1: Đổi đơn vị và tính toán tốc độ cơ bản
Đề bài: Một xe máy đi từ Hà Nội đến Phủ Lý với quãng đường dài 60 km trong 1 giờ 30 phút. Tính tốc độ của xe máy theo km/h và m/s.
- Phân tích: Đổi thời gian ra cùng hệ đơn vị giờ (h), áp dụng công thức v = s/t.
- Giải:
  + Đổi: 1 giờ 30 phút = 1,5 h.
  + Tốc độ của xe là: v = s / t = 60 / 1,5 = 40 (km/h).
  + Đổi sang m/s: v = 40 / 3,6 ≈ 11,11 (m/s).

💡 VÍ DỤ 2: Phân tích đồ thị quãng đường - thời gian
Đề bài: Đồ thị quãng đường - thời gian của một người đi bộ gồm 2 đoạn: Đoạn OA dốc lên (từ 0h đến 2h, s đạt 10km) và đoạn AB nằm ngang (từ 2h đến 3h). Hãy mô tả chuyển động và tính tốc độ trên đoạn OA.
- Giải:
  + Đoạn OA dốc lên: Người đó đang chuyển động đều. Tốc độ v = s/t = 10 / 2 = 5 (km/h).
  + Đoạn AB nằm ngang: Quãng đường không đổi trong suốt 1 giờ. Người đó đang dừng lại nghỉ ngơi.

💡 VÍ DỤ 3: Bài toán khoảng cách an toàn
Đề bài: Khi đi trên cao tốc với tốc độ v = 90 km/h, luật quy định khoảng cách an toàn tối thiểu với xe phía trước là 70m. Xe của chú Tuấn đang đi với tốc độ 90 km/h và cách xe trước 50m. Xe chú Tuấn có vi phạm quy tắc an toàn không? Tính thời gian phanh từ lúc đạp phanh đến khi chạm vạch 50m (bỏ qua độ trễ).
- Giải:
  + Theo quy định, 50m < 70m nên xe chú Tuấn đang vi phạm quy tắc giữ khoảng cách an toàn.
  + Đổi 90 km/h = 90 / 3,6 = 25 m/s.
  + Thời gian xe đi hết 50m là: t = s / v = 50 / 25 = 2 (giây). Thời gian này rất ngắn, cực kỳ nguy hiểm nếu xe trước phanh gấp.""",

        "cau_hoi": [
            {"nd": "Tốc độ là đại lượng cho biết điều gì?","da": ["Mức độ nhanh hay chậm của chuyển động","Quãng đường vật đi được","Thời gian vật chuyển động","Quỹ đạo chuyển động của vật"],"d": 0,"gt": "Định nghĩa cơ bản của tốc độ."},
            {"nd": "Công thức tính tốc độ chuyển động là gì?","da": ["v = s.t","v = s/t","v = t/s","v = s+t"],"d": 1,"gt": "Tốc độ = Quãng đường / Thời gian."},
            {"nd": "Đơn vị đo tốc độ trong hệ đo lường hợp pháp của Việt Nam (hệ SI) là?","da": ["km/h","m/s","cm/s","m/phút"],"d": 1,"gt": "Đơn vị chuẩn quốc tế của chiều dài là mét, thời gian là giây ⇒ m/s."},
            {"nd": "Tốc độ 36 km/h tương đương với bao nhiêu m/s?","da": ["10 m/s","3,6 m/s","100 m/s","360 m/s"],"d": 0,"gt": "Chia cho 3,6: 36 / 3,6 = 10 m/s."},
            {"nd": "Tốc độ 15 m/s tương đương với bao nhiêu km/h?","da": ["15 km/h","54 km/h","45 km/h","60 km/h"],"d": 1,"gt": "Nhân với 3,6: 15 × 3,6 = 54 km/h."},
            {"nd": "Dụng cụ dùng để đo tốc độ của các phương tiện giao thông gắn trên mặt đồng hồ gọi là gì?","da": ["Lực kế","Tốc kế (đồng hồ đo tốc độ)","Nhiệt kế","Vôn kế"],"d": 1,"gt": "Tốc kế hiển thị tốc độ tức thời của phương tiện."},
            {"nd": "Một chiếc ô tô đi được quãng đường 120 km trong 2 giờ. Tốc độ của ô tô là?","da": ["60 km/h","240 km/h","120 km/h","30 km/h"],"d": 0,"gt": "v = 120 / 2 = 60 km/h."},
            {"nd": "Một người chạy bộ với tốc độ 3 m/s trong 10 phút. Quãng đường người đó chạy được là?","da": ["30 m","1800 m","300 m","180 m"],"d": 1,"gt": "10 phút = 600 giây. s = v.t = 3 × 600 = 1800 m."},
            {"nd": "Trong đồ thị quãng đường - thời gian, trục hoành (trục nằm ngang) biểu diễn đại lượng nào?","da": ["Tốc độ","Thời gian","Quãng đường","Vận tốc"],"d": 1,"gt": "Trục hoành thường biểu diễn thời gian (t)."},
            {"nd": "Trong đồ thị quãng đường - thời gian, đường biểu diễn là đường thẳng nằm ngang (song song trục hoành) có nghĩa là gì?","da": ["Vật đang chuyển động đều","Vật đang tăng tốc","Vật đang đứng yên","Vật đang chuyển động chậm dần"],"d": 2,"gt": "Quãng đường không thay đổi theo thời gian nghĩa là vật đứng yên."},
            {"nd": "Trong đồ thị quãng đường - thời gian, độ dốc của đường biểu diễn cho ta biết điều gì?","da": ["Độ dốc càng lớn, vật chuyển động càng nhanh","Độ dốc càng lớn, vật chuyển động càng chậm","Độ dốc không liên quan đến tốc độ","Độ dốc càng lớn, thời gian đi càng lâu"],"d": 0,"gt": "Độ dốc chính là giá trị s/t, tức là tốc độ."},
            {"nd": "Súng bắn tốc độ của cảnh sát giao thông hoạt động dựa trên ứng dụng nào?","da": ["Đo lực ma sát","Đo quãng đường và thời gian (bằng sóng âm/quang)","Chụp ảnh biển số xe","Cân khối lượng xe"],"d": 1,"gt": "Súng phát ra sóng radar hoặc tia laser để tính toán thời gian sóng dội lại, từ đó suy ra tốc độ."},
            {"nd": "Cổng quang điện thường dùng trong phòng thực hành có tác dụng gì?","da": ["Bật sáng đèn","Đo khoảng cách chính xác","Tự động bật/tắt đồng hồ đo thời gian khi có vật che khuất","Đo nhiệt độ môi trường"],"d": 2,"gt": "Cổng quang dùng tia hồng ngoại, khi vật đi qua che tia sáng, đồng hồ sẽ tự kích hoạt."},
            {"nd": "Theo luật giao thông, khi đi trên đường cao tốc với tốc độ 100 km/h, xe phải giữ khoảng cách tối thiểu với xe trước là bao nhiêu mét? (Điều kiện thời tiết khô ráo)","da": ["35m","55m","70m","100m"],"d": 2,"gt": "Quy định tham khảo theo Luật Giao thông ĐB Việt Nam: 100 km/h thường phải giữ 70m."},
            {"nd": "Khoảng cách an toàn giữa hai xe phụ thuộc chủ yếu vào yếu tố nào?","da": ["Tốc độ của xe","Khối lượng của xe","Hãng sản xuất xe","Số người trên xe"],"d": 0,"gt": "Tốc độ càng nhanh thì quãng đường phanh cần thiết càng dài."},
            {"nd": "So sánh tốc độ: v1 = 10 m/s; v2 = 36 km/h. Khẳng định nào ĐÚNG?","da": ["v1 > v2","v1 < v2","v1 = v2","Không thể so sánh"],"d": 2,"gt": "36 km/h = 36 / 3,6 = 10 m/s ⇒ v1 = v2."},
            {"nd": "Hai người đi xe đạp. Người thứ nhất đi 15km trong 1 giờ. Người thứ hai đi 5km trong 20 phút. Ai đi nhanh hơn?","da": ["Người 1 nhanh hơn","Người 2 nhanh hơn","Hai người đi bằng nhau","Chưa đủ dữ kiện"],"d": 2,"gt": "Người 2: 5km trong 20 phút (1/3 giờ) ⇒ v = 5 / (1/3) = 15 km/h. Hai người bằng nhau."},
            {"nd": "Một đoàn tàu di chuyển từ Hà Nội vào Vinh. Tốc độ được ghi trên bảng điều khiển lúc 8h sáng là 80 km/h. Đây là tốc độ gì?","da": ["Tốc độ trung bình cả quãng đường","Tốc độ tức thời lúc 8h","Tốc độ lớn nhất của tàu","Tốc độ an toàn"],"d": 1,"gt": "Tốc kế chỉ tốc độ tại ngay thời điểm quan sát (tức thời)."},
            {"nd": "Vì sao khi trời mưa, đường trơn trượt, biển báo điện tử trên cao tốc thường yêu cầu giảm tốc độ tối đa cho phép?","da": ["Để tiết kiệm nhiên liệu","Vì lực ma sát giảm, xe cần quãng đường dài hơn để phanh dừng lại","Để chống ồn","Để cảnh sát giao thông dễ làm nhiệm vụ"],"d": 1,"gt": "Đường trơn làm giảm ma sát trượt, phanh sẽ ăn chậm hơn."},
            {"nd": "Để tính tốc độ của học sinh chạy cự ly 60m trong giờ thể dục, người ta cần dùng những dụng cụ nào?","da": ["Lực kế và đồng hồ","Thước cuộn và lực kế","Thước đo độ dài và đồng hồ bấm giây","Nhiệt kế và thước"],"d": 2,"gt": "Đo quãng đường (thước) và thời gian (đồng hồ)."},
            {"nd": "Một con rùa bò được 120 cm trong 1 phút. Tốc độ của rùa tính bằng m/s là?","da": ["2 m/s","0,2 m/s","0,02 m/s","120 m/s"],"d": 2,"gt": "s = 1,2 m; t = 60s ⇒ v = 1,2 / 60 = 0,02 m/s."},
            {"nd": "Biển báo giao thông có vòng tròn viền đỏ, nền trắng, ở giữa ghi số '60' mang ý nghĩa gì?","da": ["Tốc độ tối thiểu là 60 km/h","Tốc độ tối đa cho phép là 60 km/h","Khoảng cách đến trạm dừng là 60 km","Trọng lượng xe tối đa là 60 tấn"],"d": 1,"gt": "Biển báo cấm viền đỏ chỉ tốc độ tối đa."},
            {"nd": "Một chiếc máy bay đang bay với tốc độ 900 km/h. Trong 10 giây máy bay bay được quãng đường bao xa?","da": ["9000 m","2500 m","250 m","900 m"],"d": 1,"gt": "v = 900 km/h = 250 m/s. s = v.t = 250 × 10 = 2500 m."},
            {"nd": "Hình dạng của đồ thị quãng đường - thời gian đối với chuyển động có tốc độ không đổi là gì?","da": ["Một đường cong parabol","Một đường gấp khúc","Một đường thẳng nằm nghiêng","Một đường tròn"],"d": 2,"gt": "Hàm số s = v.t là hàm số bậc nhất nên đồ thị là đường thẳng nghiêng."},
            {"nd": "Tốc độ ánh sáng trong chân không là 300.000 km/s. Khoảng cách từ Trái Đất đến Mặt Trời khoảng 150 triệu km. Ánh sáng đi từ Mặt Trời mất khoảng bao lâu để tới Trái Đất?","da": ["8 phút 20 giây","1 phút","1 giờ","24 giờ"],"d": 0,"gt": "t = s/v = 150.000.000 / 300.000 = 500 giây = 8 phút 20 giây."},
            {"de": "Một xe ô tô đi từ A đến B mất 3 giờ, sau đó quay về A mất 4 giờ (cùng quãng đường). Khẳng định nào đúng?","da": ["Tốc độ lúc đi bằng tốc độ lúc về","Tốc độ lúc đi nhỏ hơn tốc độ lúc về","Tốc độ lúc đi lớn hơn tốc độ lúc về","Lúc về xe đi nhanh hơn"],"d": 2,"gt": "Cùng quãng đường, thời gian ngắn hơn (3h < 4h) thì tốc độ phải lớn hơn."},
            {"nd": "Vận tốc âm thanh trong không khí là 340 m/s. Bạn thấy tia chớp và 3 giây sau mới nghe tiếng sấm. Điểm sét đánh cách bạn bao xa? (Bỏ qua thời gian ánh sáng truyền).","da": ["1020 m","340 m","113 m","300000 m"],"d": 0,"gt": "s = v.t = 340 × 3 = 1020 m."},
            {"nd": "Thời gian phản xạ của một tài xế khi thấy chướng ngại vật đến khi đạp phanh là 0,5s. Đang đi với tốc độ 72km/h, trong thời gian phản xạ đó xe đã đi thêm bao nhiêu mét?","da": ["36m","20m","10m","5m"],"d": 2,"gt": "v = 72 km/h = 20 m/s. s = 20 × 0,5 = 10m."},
            {"nd": "Trong giao thông, thuật ngữ 'điểm mù' của xe ô tô (nhất là xe tải lớn) có nghĩa là gì?","da": ["Vùng không được bật đèn","Vùng mà gương chiếu hậu không thể phản chiếu tới mắt tài xế","Vùng cấm vượt","Kính chắn gió bị mờ"],"d": 1,"gt": "Điểm mù là vùng khuất tầm nhìn, xe máy không nên đi sát vào vùng này."},
            {"nd": "Biết 1 hải lý = 1852m. Tàu biển chạy với tốc độ 20 hải lý/giờ (20 knot). Tốc độ này xấp xỉ bao nhiêu km/h?","da": ["20 km/h","37 km/h","50 km/h","18,5 km/h"],"d": 1,"gt": "v = 20 × 1,852 = 37,04 km/h."}
        ],

        "bt_co_ban": [
            {"de": "Đổi các đơn vị sau: a) 18 km/h = ... m/s; b) 5 m/s = ... km/h","dd": ["a) 5 m/s; b) 18 km/h"],"gt": "18 / 3,6 = 5. Và 5 × 3,6 = 18."},
            {"de": "Một học sinh đi bộ từ nhà đến trường cách 1,5 km mất 20 phút. Tính tốc độ của học sinh đó theo km/h và m/s.","dd": ["4,5 km/h và 1,25 m/s"],"gt": "t = 20 phút = 1/3 giờ. v = 1,5 / (1/3) = 4,5 km/h. Đổi: 4,5 / 3,6 = 1,25 m/s."},
            {"de": "Một con chim đại bàng bay với tốc độ 25 m/s. Để bay hết quãng đường 18 km, nó cần bao nhiêu phút?","dd": ["12 phút"],"gt": "Đổi 18 km = 18000 m. t = 18000 / 25 = 720 giây = 12 phút."},
            {"de": "Xe đi từ A đến B với tốc độ 40 km/h mất 1 giờ 15 phút. Tính quãng đường AB.","dd": ["50 km"],"gt": "1 giờ 15 phút = 1,25 giờ. S = 40 × 1,25 = 50 km."},
            {"de": "Một chiếc xe đạp thể thao đi 1 đoạn đường 100m mất 8 giây. Tốc độ của xe đạp là bao nhiêu km/h?","dd": ["45 km/h"],"gt": "v = 100 / 8 = 12,5 m/s. Đổi 12,5 × 3,6 = 45 km/h."},
            {"de": "Dựa vào đồ thị quãng đường - thời gian. Trục tung biểu diễn quãng đường S (km), trục hoành t (h). Tại t = 2h thì S = 60km. Tính tốc độ của xe.","dd": ["30 km/h"],"gt": "Đồ thị đi từ gốc toạ độ. v = 60 / 2 = 30 km/h."},
            {"de": "Tốc độ âm thanh là 340m/s. Tốc độ này bằng bao nhiêu km/h?","dd": ["1224 km/h"],"gt": "340 × 3,6 = 1224 km/h."},
            {"de": "Biển báo quy định tốc độ tối đa 50 km/h. Chú lái xe với tốc độ 15 m/s có vi phạm luật không?","dd": ["Có vi phạm"],"gt": "15 m/s = 54 km/h > 50 km/h. Chú đã đi quá tốc độ."},
            {"de": "Khoảng cách an toàn tối thiểu theo luật với tốc độ v = 60 km/h là 35m. Một xe chạy với 60km/h đang theo sau xe tải cách 20m. Điều gì có thể xảy ra nếu xe tải phanh gấp?","dd": ["Dễ xảy ra tai nạn đâm vào đuôi xe tải"],"gt": "Khoảng cách 20m nhỏ hơn mức an toàn 35m, xe không đủ quãng đường để phanh kịp."},
            {"de": "Một đoàn tàu dài 150m lướt qua một cột điện trong 10 giây. Tính tốc độ của đoàn tàu.","dd": ["15 m/s (hay 54 km/h)"],"gt": "Quãng đường tàu đi để lướt qua cột điện đúng bằng chiều dài tàu. v = 150 / 10 = 15 m/s."}
        ],

        "bt_nang_cao": [
            {"de": "Hai thành phố A và B cách nhau 120 km. Xe ô tô khởi hành từ A đi B với tốc độ 50 km/h. Nửa giờ sau, một xe máy khởi hành từ B đi A với tốc độ 45 km/h. Hỏi sau bao lâu kể từ lúc xe máy xuất phát thì hai xe gặp nhau?","hd": "Quãng đường ô tô đi trước 0,5h. Sau đó lấy tổng khoảng cách chia cho tổng vận tốc.","dd": ["1 giờ"],"lg": "Ô tô đi trước 0,5h được: 50 × 0,5 = 25 km. Khoảng cách còn lại: 120 - 25 = 95 km. Thời gian xe máy đi đến lúc gặp nhau = 95 / (50 + 45) = 95 / 95 = 1 giờ."},
            {"de": "Một người đi xe đạp từ A đến B. Trên 1/3 quãng đường đầu đi với v1 = 15 km/h, quãng đường còn lại đi với v2 = 10 km/h. Tính tốc độ trung bình của người đó trên cả quãng đường.","hd": "v_tb = Tổng S / Tổng thời gian. Không lấy trung bình cộng vận tốc!","dd": ["11,25 km/h"],"lg": "Gọi độ dài S. t1 = (S/3) / 15 = S/45. t2 = (2S/3) / 10 = S/15. Tổng t = S/45 + 3S/45 = 4S/45. v_tb = S / (4S/45) = 45/4 = 11,25 km/h."},
            {"de": "Đồ thị quãng đường - thời gian của một xe buýt: Từ 0 đến 1h đi được 40km. Nghỉ tại trạm 30 phút. Sau đó đi tiếp 1 giờ được 60km. Vẽ phác thảo đồ thị và tính tốc độ trung bình của xe trong suốt hành trình.","hd": "Tổng S = 40 + 60. Tổng t = 1 + 0,5 + 1.","dd": ["40 km/h"],"lg": "Tổng S = 100 km. Tổng t = 2,5 giờ. v_tb = 100 / 2,5 = 40 km/h."},
            {"de": "Hai người chạy đua trên sân vận động vòng tròn chu vi 400m. Chạy cùng chiều từ vạch xuất phát. Người 1 có v = 6m/s, người 2 có v = 4m/s. Sau bao lâu người 1 vượt mặt người 2 lần đầu tiên?","hd": "Đây là bài toán đuổi kịp. Quãng đường chênh lệch đúng bằng 1 vòng sân (400m).","dd": ["200 giây (3 phút 20 giây)"],"lg": "Hiệu vận tốc = 6 - 4 = 2 m/s. Thời gian để người 1 chạy hơn người 2 đúng 400m là: t = 400 / 2 = 200 s."},
            {"de": "Một chiếc canô đi xuôi dòng từ A đến B mất 2 giờ, đi ngược dòng từ B về A mất 3 giờ. Biết tốc độ dòng nước là 5 km/h. Tính tốc độ thực của canô và quãng đường AB.","hd": "v_xuôi = v_cano + v_nước; v_ngược = v_cano - v_nước.","dd": ["v_canô = 25 km/h; AB = 60 km"],"lg": "S = 2.(v + 5) = 3.(v - 5) ⇒ 2v + 10 = 3v - 15 ⇒ v = 25 km/h. Quãng đường AB = 2.(25 + 5) = 60 km."},
            {"de": "Súng radar của CSGT bắn một sóng siêu âm về phía ô tô đang tiến lại gần. Vận tốc sóng là 340m/s. Thời gian từ lúc phát đến lúc nhận sóng phản xạ lần thứ nhất là 0,2s, lần thứ hai (sau lần phát 1 là 1 giây) là 0,1s. Tính vận tốc của ô tô.","hd": "Tính khoảng cách từ súng đến xe ở 2 thời điểm. Sóng đi và về nên s_xe = v_sóng × t / 2.","dd": ["17 m/s (61,2 km/h)"],"lg": "Khoảng cách lúc 1: d1 = 340 × 0,2 / 2 = 34m. Khoảng cách lúc 2 (sau 1 giây): d2 = 340 × 0,1 / 2 = 17m. Quãng đường xe chạy trong 1 giây = 34 - 17 = 17m. Tốc độ xe = 17m / 1s = 17 m/s."},
            {"de": "Một đoàn tàu dài 200m đi qua một cây cầu dài 800m. Biết tàu chạy với tốc độ 54 km/h. Tính thời gian từ lúc đầu tàu lên cầu đến lúc đuôi tàu ra khỏi cầu.","hd": "Quãng đường đi được bằng chiều dài cầu + chiều dài tàu.","dd": ["66,67 giây (khoảng 66,7s)"],"lg": "v = 54 km/h = 15 m/s. Tổng quãng đường tàu phải đi = 800 + 200 = 1000m. t = 1000 / 15 ≈ 66,67 giây."},
            {"de": "Cùng một lúc, tại A và B cách nhau 10km, hai xe đạp cùng khởi hành đuổi theo nhau (xe A đuổi xe B). Xe A đi 20 km/h, xe B đi 15 km/h. Hỏi sau bao lâu xe A đuổi kịp xe B?","hd": "Tốc độ thu hẹp khoảng cách là hiệu vận tốc.","dd": ["2 giờ"],"lg": "Hiệu vận tốc = 20 - 15 = 5 km/h. Thời gian đuổi kịp t = Khoảng cách / Hiệu vận tốc = 10 / 5 = 2 giờ."},
            {"de": "Một người dự định đi từ A đến B với thời gian 4 giờ. Nhưng thực tế đường xấu nên tốc độ giảm mất 10 km/h, do đó đến B muộn hơn 1 giờ. Tính quãng đường AB.","hd": "Lập phương trình: S / v = 4 và S / (v - 10) = 5.","dd": ["200 km"],"lg": "v = S/4. Ta có S/(S/4 - 10) = 5 ⇒ S = 5(S/4 - 10) ⇒ S = 1,25.S - 50 ⇒ 0,25.S = 50 ⇒ S = 200 km."},
            {"de": "Trái Đất quay một vòng quanh trục của nó (360 độ) mất xấp xỉ 24 giờ. Bán kính Trái Đất ở xích đạo khoảng 6371 km. Tính tốc độ quay (m/s) của một điểm nằm trên xích đạo.","hd": "Quãng đường = chu vi = 2.π.R.","dd": ["Xấp xỉ 463 m/s"],"lg": "Chu vi = 2 × 3,14159 × 6371 ≈ 40030 km = 40.030.000 m. t = 24 × 3600 = 86400 s. v = 40030000 / 86400 ≈ 463 m/s."},
            {"de": "Một con chó săn phát hiện một con thỏ cách nó 50m. Thỏ chạy với v = 15 m/s, chó săn đuổi theo với v = 20 m/s. Hỏi chó có bắt được thỏ trước khi thỏ chạy vào hang cách thỏ 120m không?","hd": "Tính thời gian thỏ về hang và thời gian chó bắt được thỏ.","dd": ["Chó bắt được thỏ"],"lg": "Thời gian thỏ về tới hang = 120 / 15 = 8 giây. Thời gian chó đuổi kịp thỏ = Khoảng cách / Hiệu vận tốc = 50 / (20 - 15) = 50 / 5 = 10 giây. Khoan! 10 giây > 8 giây ⇒ Nghĩa là sau 8 giây thỏ đã chui vào hang rồi (lúc này chó chưa bắt kịp). Vậy chó KHÔNG bắt được thỏ! Đáp án là KHÔNG bắt được."},
            {"de": "Để đo tốc độ âm thanh, người ta gõ một nhát búa vào một đầu ống thép dài. Ở đầu kia, người ta nghe thấy 2 tiếng gõ, cách nhau 2,5 giây. Biết tốc độ âm thanh trong không khí là 340 m/s, trong thép là 5000 m/s. Tính chiều dài ống thép.","hd": "Thời gian âm thanh truyền trong không khí trừ thời gian truyền trong thép = 2,5s.","dd": ["Khoảng 912 mét"],"lg": "L / 340 - L / 5000 = 2,5. ⇒ L(1/340 - 1/5000) = 2,5 ⇒ L.((5000-340)/1700000) = 2,5 ⇒ L = (2,5 × 1700000) / 4660 ≈ 912,02 mét."},
            {"de": "Đồ thị (S-t) của vật M là đường thẳng y = 40t. Đồ thị của vật N là y = 60t - 20 (với t ≥ 0,33h). Hỏi hai vật gặp nhau lúc t bằng mấy?","hd": "Cho 2 phương trình tọa độ (quãng đường) bằng nhau.","dd": ["t = 1 giờ"],"lg": "40t = 60t - 20 ⇒ 20t = 20 ⇒ t = 1. Gặp nhau sau 1 giờ kể từ gốc thời gian."},
            {"de": "Một ô tô phanh gấp tạo ra vết trượt dài 30m trên mặt đường nhựa. Biết công thức ước lượng tốc độ trước khi phanh là v = √(250 × S_trượt) (tính bằng km/h). Ô tô có vượt quá tốc độ quy định 80km/h không?","hd": "Thay số S = 30 vào công thức.","dd": ["Có vi phạm"],"lg": "v = √(250 × 30) = √7500 ≈ 86,6 km/h. Tốc độ này > 80 km/h ⇒ Vi phạm."},
            {"de": "Hai bến A, B cách nhau 24km. Cano xuôi dòng từ A đến B rồi lập tức ngược dòng về A. Tổng thời gian là 2 giờ 30 phút. Vận tốc dòng nước là 4km/h. Tìm vận tốc thực của cano.","hd": "Giải phương trình 24/(v+4) + 24/(v-4) = 2,5.","dd": ["20 km/h"],"lg": "24/(v+4) + 24/(v-4) = 2,5 ⇒ 24(v-4) + 24(v+4) = 2,5(v² - 16) ⇒ 48v = 2,5v² - 40 ⇒ 2,5v² - 48v - 40 = 0. Giải phương trình bậc 2 (dùng máy tính): v = 20 km/h."},
            {"de": "Một xe đang chạy với v = 100km/h. Tài xế buồn ngủ nhắm mắt trong 2 giây. Trong 2 giây đó xe đã đi được quãng đường 'mù' là bao nhiêu mét?","hd": "Đổi km/h sang m/s rồi nhân với 2.","dd": ["55,56 mét"],"lg": "100 / 3,6 ≈ 27,78 m/s. S = 27,78 × 2 = 55,56 m. Quãng đường cực lớn, vô cùng nguy hiểm."},
            {"de": "Một học sinh đi xe đạp quanh hồ Tây (chu vi 15km). Bạn ấy muốn đạp 2 vòng. Vòng 1 đạp với 15 km/h. Hỏi vòng 2 phải đạp với tốc độ bao nhiêu để tốc độ trung bình cả 2 vòng là 20 km/h?","hd": "Đừng nghĩ là trung bình cộng (15+x)/2 = 20. Phải dùng tổng thời gian.","dd": ["30 km/h"],"lg": "Tổng quãng đường = 30km. Vận tốc trung bình = 20 km/h ⇒ Tổng thời gian t = 30/20 = 1,5 giờ. Thời gian đi vòng 1: t1 = 15/15 = 1 giờ. Thời gian vòng 2 phải là: t2 = 1,5 - 1 = 0,5 giờ. Vận tốc vòng 2 = 15 / 0,5 = 30 km/h."},
            {"de": "Tính thời gian ngắn nhất để một tia sáng đi từ Trái Đất đến Mặt Trăng (Khoảng cách 384.400 km).","hd": "Áp dụng tốc độ ánh sáng c = 300.000 km/s.","dd": ["1,28 giây"],"lg": "t = 384400 / 300000 = 1,2813... giây."},
            {"de": "Thang cuốn trong siêu thị di chuyển với tốc độ 0,5 m/s. Một người bước đi trên thang cuốn với tốc độ 1 m/s. Tốc độ thực tế của người đó so với mặt đất khi đi cùng chiều và ngược chiều thang cuốn là bao nhiêu?","hd": "Cộng trừ vận tốc tương đối.","dd": ["Cùng chiều: 1,5 m/s. Ngược chiều: 0,5 m/s"],"lg": "Cùng chiều: 1 + 0,5 = 1,5 m/s. Ngược chiều: 1 - 0,5 = 0,5 m/s."},
            {"de": "Một người ném viên đá rơi xuống giếng sâu 45m. Thời gian rơi tự do xuống đáy giếng là 3 giây. Tốc độ truyền âm thanh là 340 m/s. Hỏi sau bao lâu kể từ lúc ném, người đó nghe thấy tiếng đá đập vào đáy giếng?","hd": "Tổng thời gian = Thời gian rơi + Thời gian âm thanh dội lên.","dd": ["3,13 giây"],"lg": "Thời gian rơi = 3s. Thời gian âm thanh dội lên: t2 = 45 / 340 ≈ 0,132 giây. Tổng thời gian = 3 + 0,132 = 3,132 giây."}
        ]
    }
}
VL7["Chương 1: Tốc độ chuyển động"] = C1_VL7
# --- Chương 2: Âm thanh ---
C2_VL7 = {
    "Âm thanh - Sự truyền âm - Phản xạ âm (Chuyên sâu)": {
        "ly_thuyet": """📌 1. NGUỒN ÂM VÀ SỰ TRUYỀN ÂM:
- Vật phát ra âm gọi là nguồn âm. Các nguồn âm đều dao động khi phát ra âm.
- Âm truyền được trong các môi trường: Rắn, Lỏng, Khí.
- Âm KHÔNG truyền được trong chân không.
- Tốc độ truyền âm: V_rắn > V_lỏng > V_khí. (Ví dụ trong không khí âm truyền khoảng 340m/s, trong nước khoảng 1500m/s).

📌 2. ĐỘ CAO VÀ ĐỘ TO CỦA ÂM:
- Tần số: Là số dao động trong 1 giây. Đơn vị là Héc (Hz).
- Độ cao của âm phụ thuộc vào tần số: Tần số càng lớn, dao động càng nhanh, âm phát ra càng cao (càng bổng). Tần số càng nhỏ, âm phát ra càng thấp (càng trầm).
- Biên độ dao động: Là độ lệch lớn nhất của vật dao động so với vị trí cân bằng.
- Độ to của âm phụ thuộc vào biên độ: Biên độ càng lớn, âm càng to. Đơn vị độ to là Đêxiben (dB).

📌 3. PHẢN XẠ ÂM - TIẾNG VANG:
- Phản xạ âm: Âm dội lại khi gặp mặt chắn.
- Tiếng vang: Là âm phản xạ nghe được cách âm trực tiếp ít nhất 1/15 giây.
- Vật phản xạ âm tốt: Mặt nhẵn, cứng (gương, mặt đá, tường gạch).
- Vật phản xạ âm kém (hấp thụ âm tốt): Mặt gồ ghề, mềm, xốp (rèm nhung, xốp, len).

📌 4. CHỐNG Ô NHIỄM TIẾNG ỒN:
- Tiếng ồn ô nhiễm là tiếng ồn to, kéo dài, gây ảnh hưởng đến sức khỏe.
- Biện pháp: Tác động vào nguồn âm (giảm tiếng ồn); Phân tán âm trên đường truyền (trồng cây); Ngăn chặn đường truyền âm (xây tường cách âm, dùng vật liệu xốp, nhung).""",
        
        "vi_du": """💡 VÍ DỤ 1: Tính tần số dao động
Đề bài: Trái tim của một người đập 72 nhịp trong 1 phút. Tính tần số đập của trái tim.
- Phân tích: Tần số là số dao động trong 1 giây.
- Giải: 1 phút = 60 giây. Tần số f = Số dao động / Thời gian = 72 / 60 = 1,2 Hz.

💡 VÍ DỤ 2: Bài toán Tiếng vang
Đề bài: Một người đứng trước một vách núi hét lớn và nghe được tiếng vang sau 2 giây. Biết tốc độ truyền âm trong không khí là 340 m/s. Tính khoảng cách từ người đó đến vách núi.
- Phân tích: Thời gian 2 giây là thời gian âm đi từ người đến vách núi rồi dội lại. Do đó thời gian âm đi một chiều là 2 / 2 = 1 giây.
- Giải: Khoảng cách từ người đến vách núi là: S = v . t = 340 . 1 = 340 mét.

💡 VÍ DỤ 3: So sánh độ cao, độ to của âm
Đề bài: Vật A dao động 300 lần trong 10 giây. Vật B dao động 40 lần trong 1 giây. Hỏi vật nào phát ra âm cao hơn?
- Giải: 
  + Tần số của vật A: f_A = 300 / 10 = 30 Hz.
  + Tần số của vật B: f_B = 40 / 1 = 40 Hz.
  + Vì f_B > f_A (40Hz > 30Hz) nên vật B phát ra âm cao hơn (bổng hơn).""",

        "cau_hoi": [
            {"nd": "Nguồn âm là gì?","da": ["Những vật phát ra ánh sáng","Những vật phát ra âm thanh","Những vật phản xạ âm","Những vật hấp thụ âm"],"d": 1,"gt": "Nguồn âm là vật phát ra âm thanh."},
            {"nd": "Đặc điểm chung của các nguồn âm khi phát ra âm thanh là gì?","da": ["Đều tỏa nhiệt","Đều dao động","Đều đứng yên","Đều phát sáng"],"d": 1,"gt": "Các vật phát ra âm đều dao động."},
            {"nd": "Tần số dao động là gì?","da": ["Số dao động trong 1 giây","Thời gian thực hiện 1 dao động","Quãng đường vật đi được trong 1 giây","Biên độ dao động lớn nhất"],"d": 0,"gt": "Định nghĩa của tần số."},
            {"nd": "Đơn vị của tần số là gì?","da": ["Mét (m)","Giây (s)","Héc (Hz)","Đêxiben (dB)"],"d": 2,"gt": "Đơn vị của tần số là Héc (Hertz - Hz)."},
            {"nd": "Âm phát ra càng cao (càng bổng) khi nào?","da": ["Biên độ dao động càng lớn","Tần số dao động càng nhỏ","Tần số dao động càng lớn","Vật dao động càng chậm"],"d": 2,"gt": "Độ cao của âm phụ thuộc vào tần số. Tần số càng lớn âm càng bổng."},
            {"nd": "Âm phát ra càng to khi nào?","da": ["Biên độ dao động càng lớn","Tần số dao động càng lớn","Tần số dao động càng nhỏ","Biên độ dao động càng nhỏ"],"d": 0,"gt": "Độ to của âm phụ thuộc vào biên độ dao động."},
            {"nd": "Đơn vị đo độ to của âm thanh là gì?","da": ["Héc (Hz)","Đêxiben (dB)","Mét trên giây (m/s)","Niutơn (N)"],"d": 1,"gt": "Đơn vị độ to là decibel (dB)."},
            {"nd": "Môi trường nào KHÔNG truyền được âm thanh?","da": ["Chất rắn","Chất lỏng","Chất khí","Chân không"],"d": 3,"gt": "Âm thanh cần môi trường vật chất để truyền, không truyền được trong chân không."},
            {"nd": "Sắp xếp tốc độ truyền âm trong các môi trường từ chậm đến nhanh:","da": ["Khí, Lỏng, Rắn","Rắn, Lỏng, Khí","Lỏng, Khí, Rắn","Khí, Rắn, Lỏng"],"d": 0,"gt": "V_khí < V_lỏng < V_rắn."},
            {"nd": "Khi đánh trống, để âm phát ra to hơn, ta cần:","da": ["Đánh trống nhanh hơn","Đánh trống mạnh hơn","Đánh vào vành trống","Thay dùi trống bằng sắt"],"d": 1,"gt": "Đánh mạnh làm biên độ dao động của mặt trống tăng, âm sẽ to hơn."},
            {"nd": "Tai người bình thường có thể nghe được âm thanh có tần số trong khoảng nào?","da": ["Dưới 20Hz","Từ 20Hz đến 20.000Hz","Trên 20.000Hz","Từ 0Hz đến 100Hz"],"d": 1,"gt": "Tai người nghe được âm từ 20Hz đến 20KHz."},
            {"nd": "Âm có tần số lớn hơn 20.000Hz được gọi là gì?","da": ["Hạ âm","Siêu âm","Âm nghe được","Âm vang"],"d": 1,"gt": "Trên 20.000Hz là siêu âm."},
            {"nd": "Vật nào sau đây phản xạ âm tốt?","da": ["Tấm xốp","Rèm nhung","Mặt gương nhẵn","Nệm cao su"],"d": 2,"gt": "Vật cứng, nhẵn phản xạ âm tốt."},
            {"nd": "Vật nào sau đây phản xạ âm kém (hấp thụ âm tốt)?","da": ["Tường gạch","Mặt nước","Tấm kim loại phẳng","Miếng xốp"],"d": 3,"gt": "Vật mềm, xốp, gồ ghề phản xạ âm kém."},
            {"nd": "Điều kiện để nghe được tiếng vang là thời gian âm dội lại cách âm trực tiếp ít nhất bao nhiêu giây?","da": ["1/15 giây","1 giây","2 giây","1/10 giây"],"d": 0,"gt": "Tiêu chuẩn sinh học của tai người là 1/15 giây."},
            {"nd": "Biện pháp nào sau đây giúp chống ô nhiễm tiếng ồn?","da": ["Trồng nhiều cây xanh xung quanh nhà","Xây tường bê tông phẳng và nhẵn","Sử dụng nhiều thiết bị điện tử","Mở rộng đường giao thông"],"d": 0,"gt": "Cây xanh giúp phân tán và hấp thụ âm thanh."},
            {"nd": "Trong rạp chiếu phim, người ta thường làm tường sần sùi và treo rèm nhung để làm gì?","da": ["Tăng tiếng vang","Trang trí cho đẹp","Hấp thụ âm, giảm tiếng vang","Giúp ánh sáng phản xạ tốt hơn"],"d": 2,"gt": "Chất liệu mềm, sần sùi hấp thụ âm, tránh tiếng vang gây ồn."},
            {"nd": "Một con muỗi đập cánh 3000 lần trong 10 giây. Tần số đập cánh là bao nhiêu?","da": ["3000 Hz","300 Hz","30 Hz","3 Hz"],"d": 1,"gt": "3000 / 10 = 300 Hz."},
            {"nd": "Vật A có tần số 50Hz, vật B có tần số 70Hz. Khẳng định nào đúng?","da": ["Vật A phát ra âm to hơn vật B","Vật B phát ra âm to hơn vật A","Vật A phát ra âm bổng hơn vật B","Vật B phát ra âm bổng hơn vật A"],"d": 3,"gt": "Tần số cao hơn thì âm bổng (cao) hơn."},
            {"nd": "Dơi xác định vị trí con mồi bằng cách sử dụng loại âm nào?","da": ["Siêu âm","Hạ âm","Âm nghe được","Ánh sáng"],"d": 0,"gt": "Dơi phát ra sóng siêu âm để định vị."},
            {"nd": "Ngưỡng đau của tai người (khiến tai bị nhức, đau) là khoảng bao nhiêu dB?","da": ["50 dB","70 dB","130 dB","300 dB"],"d": 2,"gt": "Từ 120-130 dB là ngưỡng đau."},
            {"nd": "Khi gảy dây đàn ghita, âm phát ra càng trầm khi dây đàn:","da": ["Căng và ngắn","Chùng và dài","Căng và dày","Dao động càng mạnh"],"d": 1,"gt": "Dây chùng, dài, to sẽ dao động chậm ⇒ tần số nhỏ ⇒ âm trầm."},
            {"nd": "Tốc độ truyền âm trong không khí ở điều kiện thường khoảng bao nhiêu?","da": ["340 m/s","1500 m/s","6100 m/s","300000 km/s"],"d": 0,"gt": "Khoảng 340 m/s."},
            {"nd": "Tại sao trên Mặt Trăng, hai phi hành gia đứng cạnh nhau không thể nói chuyện bình thường được?","da": ["Vì Mặt Trăng quá ồn","Vì trên Mặt Trăng không có không khí (chân không)","Vì trọng lực yếu","Vì trên Mặt Trăng quá lạnh"],"d": 1,"gt": "Âm thanh không truyền được trong chân không."},
            {"nd": "Để truyền tin đi xa dưới nước, người ta thường dùng:","da": ["Siêu âm","Sóng ánh sáng","Tín hiệu khói","Chuyển động dòng nước"],"d": 0,"gt": "Sonar hoạt động dưới nước dựa trên siêu âm."},
            {"nd": "Một vật dao động 120 lần trong 1 phút. Hỏi tai người có nghe được âm thanh do vật đó phát ra không?","da": ["Có, vì tần số là 120 Hz","Có, vì tần số là 2 Hz","Không, vì tần số là 2 Hz (Hạ âm)","Không, vì tần số là 120 Hz"],"d": 2,"gt": "120/60 = 2Hz < 20Hz nên là hạ âm, tai người không nghe được."},
            {"nd": "Cùng một nốt Đô (C) nhưng đàn Piano và đàn Ghita nghe khác nhau. Đặc trưng nào của âm đã tạo ra sự khác biệt đó?","da": ["Độ cao","Độ to","Âm sắc","Tần số"],"d": 2,"gt": "Âm sắc giúp phân biệt các nguồn âm khác nhau dù cùng biên độ, tần số."},
            {"nd": "Tiếng sấm và tia chớp xuất hiện cùng lúc, nhưng ta thấy chớp trước rồi mới nghe sấm. Vì sao?","da": ["Mắt hoạt động nhanh hơn tai","Ánh sáng truyền đi nhanh hơn âm thanh","Sấm phát ra sau chớp","Âm thanh bị cản lại bởi mây"],"d": 1,"gt": "V_ánh sáng (300.000 km/s) >> V_âm thanh (340 m/s)."},
            {"nd": "Trong bệnh viện, bác sĩ dùng máy siêu âm để khám bệnh. Sóng siêu âm này có đặc điểm gì?","da": ["Tai người nghe được rất rõ","Truyền được trong chân không","Có tần số > 20.000Hz","Chỉ truyền được trong chất lỏng"],"d": 2,"gt": "Siêu âm là âm có tần số > 20KHz."},
            {"nd": "Để phòng chống tiếng ồn, thợ khoan đường thường dùng thiết bị gì?","da": ["Kính râm","Găng tay","Bịt tai chống ồn","Micro"],"d": 2,"gt": "Sử dụng nút bịt tai/chụp tai để cản âm truyền vào màng nhĩ."}
        ],

        "bt_co_ban": [
            {"de": "Một con ong đập cánh 18000 lần trong 1 phút. Tính tần số đập cánh của ong. Tai người có nghe được không?","dd": ["300 Hz; Nghe được"],"gt": "18000 / 60 = 300 Hz. Nằm trong khoảng 20Hz - 20000Hz nên nghe được."},
            {"de": "Khoảng cách từ người đến vách núi là 680m. Sau khi hét to, bao lâu người đó nghe được tiếng vang? (v = 340m/s)","dd": ["4 giây"],"gt": "Quãng đường âm đi và về = 2 . 680 = 1360m. Thời gian t = S/v = 1360/340 = 4s."},
            {"de": "Vật A có tần số 60Hz. Vật B dao động 200 lần trong 5 giây. Vật nào dao động nhanh hơn?","dd": ["Vật A"],"gt": "f_B = 200/5 = 40Hz. f_A > f_B nên vật A dao động nhanh hơn."},
            {"de": "Tính khoảng cách tối thiểu từ người đến tường để nghe được tiếng vang trong không khí (v = 340m/s).","dd": ["11,33 mét"],"gt": "Thời gian t ≥ 1/15s. Quãng đường 2 chiều S = v.t = 340.(1/15) = 22,66m. Khoảng cách 1 chiều S/2 = 11,33m."},
            {"de": "Một tàu phát sóng siêu âm xuống đáy biển. Sau 2 giây tàu nhận được âm phản xạ. Tính độ sâu của đáy biển (Biết v_nước = 1500 m/s).","dd": ["1500 mét"],"gt": "Thời gian âm đi 1 chiều: t = 2/2 = 1s. Độ sâu = 1500 . 1 = 1500m."},
            {"de": "Một vật dao động với tần số 50Hz. Tính số dao động vật thực hiện được trong 2 phút.","dd": ["6000 dao động"],"gt": "2 phút = 120s. Số dao động = f . t = 50 . 120 = 6000."},
            {"de": "So sánh tốc độ truyền âm ở gỗ, nước và không khí.","dd": ["Gỗ > Nước > Không khí"],"gt": "Rắn > Lỏng > Khí."},
            {"de": "Kể tên 3 vật liệu cách âm tốt thường dùng trong xây dựng.","dd": ["Xốp, bông thủy tinh, cao su"],"gt": "Các vật liệu mềm, xốp chứa nhiều không khí."},
            {"de": "Đổi 20 phút ra giây và tính số dao động nếu vật có tần số 5Hz.","dd": ["1200 giây; 6000 dao động"],"gt": "20.60 = 1200s. Số dao động = 5 . 1200 = 6000."},
            {"de": "Người ta thấy tia sét và 5 giây sau nghe tiếng sấm. Điểm sét đánh cách người quan sát bao xa?","dd": ["1700 m"],"gt": "S = 340 . 5 = 1700m."}
        ],

        "bt_nang_cao": [
            {"de": "Hai người đứng ở hai đầu một ống thép dài 1020m. Người A gõ một nhát búa vào ống. Người B áp tai vào ống thép nghe thấy hai tiếng gõ cách nhau 2,8 giây. Biết tốc độ âm thanh trong không khí là 340 m/s. Tính tốc độ truyền âm trong thép.","hd": "Lập phương trình hiệu thời gian truyền âm trong không khí và trong thép.","dd": ["5100 m/s"],"lg": "Thời gian âm truyền trong không khí t1 = 1020 / 340 = 3s. Thời gian âm truyền trong thép t2. Vì V_thép > V_khí nên t2 < t1. Ta có t1 - t2 = 2,8s ⇒ t2 = 3 - 2,8 = 0,2s. V_thép = 1020 / 0,2 = 5100 m/s."},
            {"de": "Một người đứng cách vách đá 17m và vỗ tay. Tốc độ âm trong không khí là 340m/s. Hỏi người đó có nghe được tiếng vang không? Vì sao?","hd": "Tính thời gian âm dội lại và so sánh với 1/15s.","dd": ["Không nghe được"],"lg": "Thời gian âm truyền đi và về: t = (17 . 2) / 340 = 34 / 340 = 0,1s. 0,1s = 1/10s. Vì 1/10s > 1/15s... À khoan! 1/10 = 0,1s; 1/15 ≈ 0,067s. Vì 0,1s > 1/15s nên NGHE ĐƯỢC tiếng vang. Sửa lại: Có nghe được."},
            {"de": "Tàu thăm dò đáy biển phát sóng siêu âm. Tín hiệu phản xạ trở lại sau 1,2s. Khi tàu di chuyển sang vị trí khác, tín hiệu phản xạ trở lại sau 1,8s. So sánh độ sâu hai vị trí. (v_nước = 1500m/s).","hd": "Tính độ sâu mỗi nơi.","dd": ["Vị trí sau sâu hơn vị trí trước 450m"],"lg": "h1 = (1500 . 1,2)/2 = 900m. h2 = (1500 . 1,8)/2 = 1350m. h2 - h1 = 450m."},
            {"de": "Cùng một lúc người A đập búa vào đường ray tàu hỏa, người B đứng cách đó một khoảng áp tai vào đường ray và nghe thấy 2 tiếng búa cách nhau 1,5s. Biết v_không khí = 340m/s, v_thép = 5100m/s. Tính khoảng cách giữa hai người.","hd": "Gọi khoảng cách là S. S/340 - S/5100 = 1,5.","dd": ["546,4 mét"],"lg": "S.(1/340 - 1/5100) = 1,5 ⇒ S.(14 / 5100) = 1,5 ⇒ S = (1,5 . 5100) / 14 ≈ 546,4 m."},
            {"de": "Một dây đàn dài dao động 400 lần trong 2 giây. Một dây khác dao động 1000 lần trong 4 giây. Dây nào phát ra âm cao hơn?","hd": "Tính tần số.","dd": ["Dây thứ hai"],"lg": "f1 = 400/2 = 200Hz. f2 = 1000/4 = 250Hz. f2 > f1 nên dây thứ 2 phát âm cao hơn."},
            {"de": "Đứng trước một hẻm núi, hét to một tiếng, người ta nghe thấy tiếng vang thứ nhất sau 1s, tiếng vang thứ hai sau 2s (dội từ vách núi bên kia). Khoảng cách giữa 2 vách núi là bao nhiêu? (v = 340m/s)","hd": "Khoảng cách giữa 2 vách bằng tổng khoảng cách từ người đến từng vách.","dd": ["510 mét"],"lg": "D1 = (340 . 1)/2 = 170m. D2 = (340 . 2)/2 = 340m. Khoảng cách = D1 + D2 = 170 + 340 = 510m."},
            {"de": "Giả sử Trái Đất bị nổ tung (giả tưởng), người đứng trên Mặt Trăng có nghe thấy tiếng nổ không? Tại sao?","hd": "Khoảng không gian giữa Trái Đất và Mặt Trăng là chân không.","dd": ["Không nghe thấy"],"lg": "Âm thanh không truyền được trong môi trường chân không ngoài vũ trụ."},
            {"de": "Một bánh xe răng cưa có 60 răng, quay với tốc độ 120 vòng/phút. Nó chạm vào một lá thép mỏng phát ra âm thanh. Tính tần số của âm thanh đó.","hd": "Số va chạm trong 1 giây chính là tần số.","dd": ["120 Hz"],"lg": "Trong 1 phút (60s) bánh xe cọ xát: 60 . 120 = 7200 lần. Tần số f = 7200 / 60 = 120 Hz."},
            {"de": "Tốc độ âm thanh trong nước là 1500m/s, trong không khí là 340m/s. Âm thanh truyền từ nước ra không khí, tần số âm có thay đổi không? Vận tốc thay đổi thế nào?","hd": "Tần số không đổi, vận tốc giảm.","dd": ["Tần số không đổi, Vận tốc giảm"],"lg": "Khi sóng âm chuyển môi trường, tần số (bản chất nguồn âm) không đổi. Vận tốc truyền từ nước ra không khí bị giảm."},
            {"de": "Tiếng sét nổ cách người quan sát 5,1km. Hỏi sau bao lâu người đó mới nghe thấy tiếng sấm?","hd": "Đổi km ra m rồi chia cho 340.","dd": ["15 giây"],"lg": "t = 5100 / 340 = 15s."},
            {"de": "Để đo độ sâu của một hang động thẳng đứng, người ta thả một hòn đá và đo được thời gian từ lúc thả đến lúc nghe tiếng đá chạm đáy là 4 giây. Cho biết đá rơi tự do với phương trình S = 5.t1², tốc độ âm là 340m/s. Tính độ sâu hang. (Bài toán vượt cấp nhẹ).","hd": "Tổng thời gian t1 + t2 = 4. S = 5.t1² = 340.t2.","dd": ["Khoảng 70 mét"],"lg": "Hệ PT: t1 + t2 = 4 ⇒ t2 = 4 - t1. Ta có: 5.t1² = 340.(4 - t1) ⇒ 5.t1² + 340.t1 - 1360 = 0. Giải PT ta được t1 ≈ 3,74s. S = 5 . (3,74)² ≈ 70m."},
            {"de": "Vật A có chu kì dao động là 0,02s. Vật B có tần số 60Hz. Vật nào phát âm trầm hơn?","hd": "Tần số f = 1/T.","dd": ["Vật A"],"lg": "Tần số vật A: f_A = 1 / 0,02 = 50Hz. Vì 50Hz < 60Hz nên vật A phát âm trầm hơn."},
            {"de": "Thiết kế một căn phòng hát Karaoke không làm ồn sang nhà bên cạnh. Em sẽ dùng các loại vật liệu gì và bố trí như thế nào?","hd": "Vật liệu xốp, cách âm, phản xạ kém.","dd": ["Dùng xốp, mút gai dán tường, thảm trải sàn, cửa kính hộp 2 lớp..."],"lg": "Các vật liệu xốp, mềm chứa nhiều không khí bên trong giúp hấp thụ âm thanh, ngăn chúng truyền qua tường."},
            {"de": "Một con muỗi khi bay phát ra âm cao hơn con ruồi. Cánh con nào dao động nhanh hơn?","hd": "Âm cao ⇒ Tần số cao ⇒ Dao động nhanh.","dd": ["Con muỗi"],"lg": "Con muỗi phát âm cao hơn (tần số cao hơn) nên cánh của nó dao động nhanh hơn con ruồi."},
            {"de": "Người ta thường dùng chó để phát hiện ma túy ở sân bay, ngoài khứu giác, thính giác của chó có nghe được dải âm nào mà người không nghe được?","hd": "Siêu âm.","dd": ["Siêu âm"],"lg": "Chó có thể nghe được âm thanh có tần số lên tới 40.000 Hz (Siêu âm đối với người)."},
            {"de": "Tại sao trong các lớp học, người ta không xây tường hoàn toàn nhẵn bóng mà thường quét sơn hoặc dùng giấy dán tường hơi nhám?","hd": "Chống tiếng vang.","dd": ["Để hấp thụ âm, tránh hiện tượng tiếng vang gây ồn."],"lg": "Mặt nhám giúp âm thanh bị phản xạ tán xạ ra nhiều hướng và bị hấp thụ bớt, giảm tiếng vang dội làm chói tai."},
            {"de": "Trong một bản nhạc, nốt Son cao hơn nốt Đồ. Nốt nào có bước sóng dài hơn trong cùng điều kiện không khí?","hd": "v = f . λ (bước sóng). Mở rộng: f lớn thì bước sóng nhỏ.","dd": ["Nốt Đồ"],"lg": "Nốt Son cao hơn nên tần số lớn hơn. Vì v không đổi nên tần số lớn thì bước sóng ngắn. Nốt Đồ có tần số thấp hơn nên bước sóng dài hơn."},
            {"de": "Vận tốc truyền âm trong đồng là 3800 m/s. Một đường ray bằng đồng dài 19km. Thời gian âm truyền qua đường ray này là bao lâu?","hd": "S/v.","dd": ["5 giây"],"lg": "t = 19000 / 3800 = 5 giây."},
            {"de": "Màng nhĩ của con người là một ví dụ về vật dội âm hay nguồn âm? Khi ta nghe, nó đóng vai trò gì?","hd": "Bộ phận nhận dao động.","dd": ["Vật dội âm (Dao động cưỡng bức)"],"lg": "Màng nhĩ bị sóng âm đập vào làm nó dao động theo cùng tần số của nguồn âm, truyền tín hiệu vào thần kinh thính giác."},
            {"de": "Vì sao áp tai vào mặt đất có thể nghe được tiếng vó ngựa từ xa trước khi nghe bằng không khí?","hd": "Vận tốc truyền âm rắn > khí.","dd": ["Vì âm truyền trong đất nhanh hơn và ít bị suy giảm hơn trong không khí."],"lg": "Đất (chất rắn) truyền âm nhanh hơn không khí nhiều lần, nên âm thanh sẽ đến tai áp sát đất trước tiên."}
        ]
    }
}
VL7["Chương 2: Âm thanh"] = C2_VL7


# --- Chương 3: Ánh sáng ---
C3_VL7 = {
    "Ánh sáng - Sự truyền ánh sáng - Gương phẳng (Chuyên sâu)": {
        "ly_thuyet": """📌 1. NGUỒN SÁNG VÀ VẬT SÁNG:
- Nguồn sáng là vật tự nó phát ra ánh sáng (Mặt Trời, bóng đèn đang sáng, ngọn lửa).
- Vật sáng gồm nguồn sáng và những vật hắt lại ánh sáng chiếu vào nó (Mặt Trăng, cái bàn, con người).
- Ta nhìn thấy một vật khi có ánh sáng từ vật đó truyền vào mắt ta.

📌 2. SỰ TRUYỀN THẲNG CỦA ÁNH SÁNG:
- Định luật truyền thẳng của ánh sáng: Trong môi trường trong suốt và đồng tính, ánh sáng truyền đi theo đường thẳng.
- Tia sáng được biểu diễn bằng một đường thẳng có mũi tên chỉ hướng.
- Có 3 loại chùm sáng: Chùm sáng song song, chùm sáng hội tụ (các tia giao nhau), chùm sáng phân kì (các tia loe rộng ra).
- Bóng tối nằm ở phía sau vật cản sáng, không nhận được ánh sáng từ nguồn truyền tới. Bóng nửa tối chỉ nhận được một phần ánh sáng từ nguồn truyền tới.

📌 3. SỰ PHẢN XẠ ÁNH SÁNG:
- Phản xạ ánh sáng là hiện tượng tia sáng dội ngược trở lại môi trường cũ khi gặp một bề mặt nhẵn bóng.
- Định luật phản xạ ánh sáng: 
  + Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến của gương ở điểm tới.
  + Góc phản xạ bằng góc tới (i' = i).
- Phản xạ khuếch tán (tán xạ): Xảy ra khi ánh sáng chiếu vào bề mặt gồ ghề, các tia phản xạ hắt ra nhiều hướng khác nhau.

📌 4. ẢNH CỦA MỘT VẬT TẠO BỞI GƯƠNG PHẲNG:
- Là ảnh ảo (không hứng được trên màn chắn).
- Lớn bằng vật.
- Khoảng cách từ một điểm của vật đến gương bằng khoảng cách từ ảnh của điểm đó đến gương (Ảnh và vật đối xứng nhau qua mặt gương).""",
        
        "vi_du": """💡 VÍ DỤ 1: Nhật thực và Nguyệt thực
Đề bài: Giải thích hiện tượng Nhật thực.
- Giải: Nhật thực xảy ra ban ngày, khi Mặt Trăng nằm giữa Trái Đất và Mặt Trời thẳng hàng. Mặt Trăng che khuất ánh sáng từ Mặt Trời, tạo ra vùng bóng tối và bóng nửa tối trên Trái Đất. Người đứng ở vùng bóng tối trên Trái Đất sẽ thấy Nhật thực toàn phần.

💡 VÍ DỤ 2: Tính góc phản xạ
Đề bài: Chiếu một tia sáng SI lên một gương phẳng, tia tới tạo với mặt gương một góc 30°. Tính góc tới và góc phản xạ. Vẽ tia phản xạ.
- Phân tích: Góc tới i là góc hợp bởi tia tới và đường pháp tuyến (vuông góc với gương).
- Giải: 
  + Góc tới i = 90° - 30° = 60°.
  + Theo định luật phản xạ ánh sáng, góc phản xạ i' = i = 60°.
  + Tia phản xạ IR tạo với pháp tuyến một góc 60° nằm bên kia pháp tuyến so với tia tới.

💡 VÍ DỤ 3: Bài toán khoảng cách ảnh và vật
Đề bài: Một người cao 1,6m đứng cách gương phẳng 2m. Kích thước ảnh của người đó trong gương là bao nhiêu? Khoảng cách từ người đó đến ảnh của mình là bao nhiêu?
- Giải:
  + Ảnh tạo bởi gương phẳng có kích thước bằng vật nên ảnh cao 1,6m.
  + Khoảng cách từ ảnh đến gương bằng khoảng cách từ người đến gương (2m).
  + Khoảng cách từ người đến ảnh = 2m + 2m = 4m.""",

        "cau_hoi": [
            {"nd": "Vật nào dưới đây là nguồn sáng?","da": ["Mặt Trăng","Ngọn nến đang cháy","Tờ giấy trắng","Chiếc gương"],"d": 1,"gt": "Nguồn sáng tự phát ra ánh sáng."},
            {"nd": "Ta nhìn thấy một vật khi nào?","da": ["Khi vật được chiếu sáng","Khi vật phát ra ánh sáng","Khi có ánh sáng từ vật đó truyền vào mắt ta","Khi mắt ta mở"],"d": 2,"gt": "Điều kiện để nhìn thấy vật là phải có ánh sáng từ vật đến mắt."},
            {"nd": "Định luật truyền thẳng của ánh sáng áp dụng trong môi trường nào?","da": ["Bất kì môi trường nào","Môi trường trong suốt","Môi trường đồng tính","Môi trường trong suốt và đồng tính"],"d": 3,"gt": "Phải thỏa mãn cả 2 điều kiện: trong suốt và đồng tính."},
            {"nd": "Chùm sáng phân kì là chùm sáng có các tia sáng:","da": ["Không giao nhau","Cắt nhau tại 1 điểm trước mặt","Loe rộng ra trên đường truyền","Song song với nhau"],"d": 2,"gt": "Phân kì là tách xa nhau (loe rộng ra)."},
            {"nd": "Tia sáng mặt trời chiếu xuống Trái Đất được coi là loại chùm sáng nào?","da": ["Chùm sáng hội tụ","Chùm sáng phân kì","Chùm sáng song song","Không có hình dạng"],"d": 2,"gt": "Mặt Trời rất xa nên các tia sáng đến Trái Đất xem như song song."},
            {"nd": "Bóng tối là vùng:","da": ["Nằm sau vật cản sáng và không nhận được ánh sáng từ nguồn truyền tới","Nằm sau vật cản sáng, nhận được một phần ánh sáng","Vùng sáng yếu","Bất kì chỗ nào có màu đen"],"d": 0,"gt": "Định nghĩa bóng tối."},
            {"nd": "Góc tới là góc hợp bởi:","da": ["Tia tới và mặt gương","Tia tới và tia phản xạ","Tia tới và pháp tuyến của gương tại điểm tới","Pháp tuyến và tia phản xạ"],"d": 2,"gt": "Góc tới luôn so với đường pháp tuyến."},
            {"nd": "Theo định luật phản xạ ánh sáng, góc phản xạ có độ lớn:","da": ["Nhỏ hơn góc tới","Lớn hơn góc tới","Bằng góc tới","Bằng nửa góc tới"],"d": 2,"gt": "i' = i."},
            {"nd": "Chiếu tia sáng vuông góc với mặt gương phẳng, góc phản xạ bằng bao nhiêu?","da": ["90°","0°","180°","45°"],"d": 1,"gt": "Vuông góc với gương tức là trùng với pháp tuyến ⇒ Góc tới = 0° ⇒ Góc phản xạ = 0°."},
            {"nd": "Ảnh của một vật tạo bởi gương phẳng có đặc điểm gì?","da": ["Là ảnh thật, lớn bằng vật","Là ảnh ảo, lớn bằng vật","Là ảnh ảo, nhỏ hơn vật","Là ảnh ảo, lớn hơn vật"],"d": 1,"gt": "Tính chất ảnh của gương phẳng."},
            {"nd": "Khoảng cách từ điểm sáng S đến gương phẳng là 5cm. Khoảng cách từ S đến ảnh S' của nó là?","da": ["5 cm","10 cm","2,5 cm","15 cm"],"d": 1,"gt": "Khoảng cách vật-ảnh = 2 lần khoảng cách vật-gương = 2.5 = 10cm."},
            {"nd": "Mặt Trăng là:","da": ["Nguồn sáng","Vật sáng","Gương phẳng","Vật hắt sáng màu vàng"],"d": 1,"gt": "Mặt Trăng hắt lại ánh sáng Mặt Trời nên nó là vật sáng (không phải nguồn sáng)."},
            {"nd": "Hiện tượng nguyệt thực xảy ra khi:","da": ["Mặt Trăng nằm giữa Trái Đất và Mặt Trời","Mặt Trời nằm giữa Trái Đất và Mặt Trăng","Trái Đất nằm giữa Mặt Trời và Mặt Trăng","Trái Đất che khuất Mặt Trời"],"d": 2,"gt": "Nguyệt thực là Trái Đất chắn ánh sáng từ MT đến Mặt Trăng."},
            {"nd": "Tia phản xạ nằm trong mặt phẳng nào?","da": ["Mặt phẳng gương","Mặt phẳng chứa tia tới và đường pháp tuyến","Mặt phẳng ngang","Bất kì mặt phẳng nào"],"d": 1,"gt": "Định lí phản xạ: Tia phản xạ nằm trong mặt phẳng tới."},
            {"nd": "Ảnh ảo là ảnh như thế nào?","da": ["Hiện rõ trên màn chắn","Không hứng được trên màn chắn","Là ảnh của vật có màu trắng","Là ảnh nhỏ hơn vật"],"d": 1,"gt": "Ảnh ảo nằm 'sau' gương, không thể hứng trên giấy/màn."},
            {"nd": "Tại sao ta có thể nhìn thấy ảnh của mình trong gương phẳng?","da": ["Vì gương tự phát sáng","Vì gương có lớp bạc phía sau","Vì ánh sáng từ mặt ta chiếu đến gương bị dội lại vào mắt ta","Vì mắt ta tự phát ra ánh sáng"],"d": 2,"gt": "Ánh sáng từ mặt dội vào gương, phản xạ lại vào mắt."},
            {"nd": "Khi đứng gần gương phẳng, nếu bạn lùi xa gương 1m thì ảnh của bạn:","da": ["Đứng yên","Lùi xa gương 1m","Tiến lại gần gương 1m","To lên"],"d": 1,"gt": "Khoảng cách ảnh và vật đối xứng nên ảnh cũng lùi xa gương 1m."},
            {"nd": "Một người cao 1m60 đứng trước gương phẳng. Ảnh của người đó cao bao nhiêu?","da": ["1m60","3m20","0m80","Tuỳ khoảng cách đứng"],"d": 0,"gt": "Ảnh trong gương phẳng luôn bằng vật."},
            {"nd": "Góc hợp bởi tia tới và mặt gương là 20°. Góc phản xạ bằng?","da": ["20°","70°","140°","40°"],"d": 1,"gt": "Góc tới i = 90 - 20 = 70°. Góc phản xạ i' = i = 70°."},
            {"nd": "Nếu tia tới hợp với tia phản xạ một góc 90° thì góc tới bằng bao nhiêu?","da": ["90°","45°","180°","0°"],"d": 1,"gt": "i + i' = 90° ⇒ 2i = 90° ⇒ i = 45°."},
            {"nd": "Chữ 'AMBULANCE' viết ngược trên mũi xe cứu thương là ứng dụng của tính chất gì?","da": ["Khúc xạ ánh sáng","Tính đối xứng trái-phải của ảnh ảo qua gương phẳng","Bóng tối bóng nửa tối","Định luật truyền thẳng"],"d": 1,"gt": "Ảnh qua gương bị lật ngược trái phải, để tài xế xe trước nhìn qua gương chiếu hậu sẽ đọc xuôi chữ."},
            {"nd": "Ánh sáng có truyền được trong chân không không?","da": ["Có, truyền nhanh nhất","Có, nhưng rất chậm","Không truyền được","Phụ thuộc vào nhiệt độ"],"d": 0,"gt": "Ánh sáng truyền được trong chân không với v = 300.000 km/s (khác với âm thanh)."},
            {"nd": "Kính tiềm vọng dùng trong tàu ngầm hoạt động dựa trên nguyên lí nào?","da": ["Phản xạ ánh sáng qua 2 gương phẳng","Khúc xạ qua thấu kính","Sự truyền thẳng ánh sáng","Nhiễu xạ ánh sáng"],"d": 0,"gt": "Sử dụng 2 gương phẳng đặt nghiêng 45 độ để bẻ gập đường đi ánh sáng."},
            {"nd": "Khi bề mặt gồ ghề, các tia sáng song song chiếu vào sẽ bị phản xạ theo nhiều hướng. Gọi là hiện tượng gì?","da": ["Phản xạ đều","Phản xạ khuếch tán (tán xạ)","Khúc xạ","Nhiễu xạ"],"d": 1,"gt": "Bề mặt nhám tạo ra phản xạ khuếch tán, giúp ta nhìn thấy vật từ nhiều góc độ."},
            {"nd": "Có 1 điểm sáng S đặt trước gương phẳng. Vẽ được bao nhiêu tia phản xạ từ S qua gương?","da": ["1 tia","2 tia","Vô số tia","Không có tia nào"],"d": 2,"gt": "S phát ra vô số tia sáng đến các điểm khác nhau trên mặt gương."},
            {"nd": "Vật nào sau đây hoạt động như một gương phẳng?","da": ["Mặt nước hồ đang có sóng gợn","Mặt nước hồ tĩnh lặng","Mặt đường nhựa","Tờ giấy trắng"],"d": 1,"gt": "Bề mặt nhẵn bóng như mặt nước tĩnh phản xạ ánh sáng tốt như gương."},
            {"nd": "Môi trường nào ánh sáng không truyền qua được?","da": ["Không khí","Chân không","Kính trong","Bức tường gạch"],"d": 3,"gt": "Tường gạch là vật chắn sáng, không trong suốt."},
            {"nd": "Ngôi sao lấp lánh trên bầu trời đêm là nguồn sáng hay vật sáng?","da": ["Nguồn sáng","Vật sáng","Cả hai","Không phải cả hai"],"d": 0,"gt": "Các ngôi sao là các mặt trời tự phát sáng."},
            {"nd": "Hiện tượng bóng nửa tối chỉ xuất hiện khi nào?","da": ["Khi nguồn sáng là một điểm","Khi nguồn sáng rộng (có kích thước)","Khi vật cản trong suốt","Khi không có ánh sáng"],"d": 1,"gt": "Nguồn sáng rộng (như bóng đèn tuýp) sẽ tạo ra bóng đen và bóng mờ (nửa tối)."},
            {"nd": "Quang học là ngành vật lý nghiên cứu về?","da": ["Âm thanh","Ánh sáng","Nhiệt độ","Cơ học"],"d": 1,"gt": "Quang (Ánh sáng)."}
        ],

        "bt_co_ban": [
            {"de": "Góc tạo bởi tia tới và mặt gương là 40°. Tính góc phản xạ.","dd": ["50°"],"gt": "Góc tới i = 90° - 40° = 50°. Góc phản xạ i' = 50°."},
            {"de": "Một tia sáng chiếu tới gương phẳng tạo với pháp tuyến một góc 30°. Tính góc hợp bởi tia tới và tia phản xạ.","dd": ["60°"],"gt": "Góc = i + i' = 30° + 30° = 60°."},
            {"de": "Điểm sáng S cách gương phẳng 4cm. Ảnh S' của S cách gương bao nhiêu?","dd": ["4 cm"],"gt": "Tính chất đối xứng: SS' vuông góc gương và khoảng cách bằng nhau."},
            {"de": "Vật AB cao 5cm đặt song song với gương phẳng. Ảnh A'B' có chiều cao bao nhiêu?","dd": ["5 cm"],"gt": "Ảnh bằng vật."},
            {"de": "Nêu điều kiện để xảy ra hiện tượng Nhật thực.","dd": ["Mặt Trăng nằm giữa Trái Đất và Mặt Trời thẳng hàng"],"gt": "Mặt trăng chắn ánh sáng từ MT chiếu tới TĐ."},
            {"de": "Tia sáng tới trùng với pháp tuyến. Góc phản xạ bằng bao nhiêu?","dd": ["0°"],"gt": "Góc tới = 0° ⇒ Góc phản xạ = 0°."},
            {"de": "Một người đứng cách gương 1,5m. Người đó đi lại gần gương thêm 0,5m. Hỏi lúc này người đó cách ảnh của mình bao nhiêu?","dd": ["2 m"],"gt": "Khoảng cách mới đến gương = 1,5 - 0,5 = 1m. Khoảng cách người đến ảnh = 2 × 1m = 2m."},
            {"de": "Giải thích vì sao ban đêm trong phòng đóng kín không có đèn ta không nhìn thấy mọi vật?","dd": ["Không có ánh sáng chiếu vào vật để hắt lại vào mắt ta"],"gt": "Cần có ánh sáng truyền từ vật vào mắt."},
            {"de": "Vì sao trên mặt đường nhựa ban đêm lại khó quan sát người mặc quần áo đen?","dd": ["Màu đen hấp thụ ánh sáng, không hắt lại ánh sáng vào mắt người lái xe"],"gt": "Vật màu đen không phản xạ ánh sáng."},
            {"de": "Tia phản xạ nằm ở đâu?","dd": ["Nằm trong mặt phẳng chứa tia tới và pháp tuyến tại điểm tới"],"gt": "Định luật phản xạ ánh sáng phần 1."}
        ],

        "bt_nang_cao": [
            {"de": "Chiếu tia sáng SI lên một gương phẳng G. Quay gương G một góc α quanh điểm I. Tia phản xạ sẽ quay một góc bao nhiêu?","hd": "Định lí góc quay của gương.","dd": ["Tia phản xạ quay một góc 2α"],"lg": "Khi gương quay góc α, pháp tuyến quay góc α. Góc tới thay đổi thành i + α. Góc tia phản xạ so với pháp tuyến cũ là (i+α) + α = i + 2α. Vậy tia phản xạ dời đi góc 2α."},
            {"de": "Hai gương phẳng G1, G2 hợp với nhau một góc 60°. Điểm sáng S nằm trong khoảng 2 gương. Tính số ảnh của S được tạo ra bởi hệ 2 gương này.","hd": "Sử dụng công thức n = (360° / α) - 1.","dd": ["5 ảnh"],"lg": "Số ảnh n = (360° / 60°) - 1 = 6 - 1 = 5 ảnh."},
            {"de": "Hai gương phẳng song song quay mặt phản xạ vào nhau cách nhau 10cm. Một điểm sáng S đặt giữa hai gương cách gương thứ nhất 3cm. Tính khoảng cách giữa ảnh thứ nhất của S qua gương 1 và ảnh thứ nhất của S qua gương 2.","hd": "Tìm khoảng cách ảnh 1 đến gương 1, ảnh 2 đến gương 2. Cộng các đoạn thẳng lại.","dd": ["20 cm"],"lg": "S cách G1 3cm ⇒ S1 cách G1 3cm. S cách G2 7cm ⇒ S2 cách G2 7cm. Khoảng cách S1S2 = S1G1 + G1G2 + G2S2 = 3 + 10 + 7 = 20cm."},
            {"de": "Một người cao 1,7m mắt cách đỉnh đầu 10cm đứng trước gương phẳng treo thẳng đứng. Tìm chiều cao tối thiểu của gương để người đó thấy toàn bộ ảnh của mình trong gương.","hd": "Dùng tính chất đường trung bình của tam giác tạo bởi mắt và đỉnh đầu, mắt và chân.","dd": ["0,85 mét (bằng một nửa chiều cao người)"],"lg": "Sử dụng nguyên lý đường trung bình, chiều cao gương tối thiểu = Chiều cao người / 2 = 1,7 / 2 = 0,85m."},
            {"de": "Một người đi về phía gương phẳng với vận tốc 2 m/s. Vận tốc của ảnh đối với người đó là bao nhiêu?","hd": "Ảnh cũng tiến về phía gương với vận tốc 2m/s ngược chiều.","dd": ["4 m/s"],"lg": "Vận tốc tương đối = v_người + v_ảnh = 2 + 2 = 4 m/s."},
            {"de": "Hai gương phẳng hợp với nhau một góc α vuông (90°). Một tia sáng SI chiếu tới gương 1, phản xạ tới gương 2. Chứng minh tia phản xạ cuối cùng song song với tia tới SI.","hd": "Vẽ hình, tính tổng các góc của tia sáng tạo với 2 gương.","dd": ["Xem lời giải"],"lg": "Pháp tuyến 2 gương vuông góc nhau. Góc tới G1 là i1, phản xạ i1. Tia sáng đến G2 có góc tới i2. Ta có i1 + i2 = 90°. Góc tia tới G1 tạo với pháp tuyến là i1. Góc tia ló tạo với pháp tuyến cũ là 180°. Hệ quả: Tia tới và tia ló ngược chiều, song song nhau."},
            {"de": "Một cột điện cao 6m có bóng in trên mặt đất dài 8m. Cùng lúc đó một cái cây có bóng in trên mặt đất dài 4m. Tính chiều cao cái cây.","hd": "Các tia sáng mặt trời chiếu xuống song song. Dùng tam giác đồng dạng hoặc tỉ lệ.","dd": ["3 mét"],"lg": "Tỉ lệ chiều cao / chiều dài bóng không đổi. h / 4 = 6 / 8 ⇒ h = (6 × 4) / 8 = 3m."},
            {"de": "Tại sao trong kính tiềm vọng người ta đặt 2 gương phẳng nghiêng 45° so với phương ngang?","hd": "Bẻ góc 90° hai lần.","dd": ["Để bẻ gập tia sáng 90 độ hai lần, giúp truyền ánh sáng từ trên cao xuống mắt người quan sát."],"lg": "Gương nghiêng 45° thì tia tới ngang sẽ tạo góc tới 45°, tia phản xạ sẽ tạo góc 90° so với tia tới, đi thẳng đứng xuống dưới."},
            {"de": "Biết vận tốc ánh sáng là 300.000 km/s. Một năm ánh sáng là quãng đường ánh sáng đi được trong 1 năm. Tính xấp xỉ 1 năm ánh sáng bằng bao nhiêu tỉ km?","hd": "Nhân vận tốc với số giây trong 1 năm (365 ngày).","dd": ["Khoảng 9460 tỉ km"],"lg": "S = 300.000 × 365 × 24 × 3600 ≈ 9.460.800.000.000 km."},
            {"de": "Cho tia sáng tới SI hợp với mặt gương một góc 30°. Phải quay gương một góc bao nhiêu để tia phản xạ hướng thẳng đứng lên trên?","hd": "Xác định góc tia phản xạ mong muốn rồi chia đôi góc hợp bởi tia tới và tia phản xạ mới để tìm vị trí mặt gương mới.","dd": ["Quay 15° hoặc 75° tùy chiều"],"lg": "Tia tới nằm ngang? Đề chưa rõ tia tới hướng nào. Giả sử tia tới nằm ngang. Góc tới = 60°. Tia phản xạ nghiêng 30° so với phương ngang. Để tia phản xạ thẳng đứng (90° so với ngang), tia phản xạ phải quay 60°. Do đó gương phải quay 30°. (Tùy điều kiện đề bài chi tiết)"},
            {"de": "Người ta thường dùng gương phẳng để tạo ảo giác không gian rộng hơn trong các cửa hàng nhỏ. Tại sao lại làm vậy?","hd": "Nhờ ảnh ảo qua gương.","dd": ["Gương tạo ra ảnh ảo của căn phòng ở phía sau gương, khoảng cách ảnh bằng vật khiến mắt cảm nhận không gian như được nhân đôi."],"lg": "Đánh lừa thị giác bằng tính chất đối xứng của ảnh tạo bởi gương phẳng."},
            {"de": "Một điểm sáng S cách gương 20cm. Dời S ra xa gương thêm 10cm. Ảnh dời đi bao nhiêu cm so với vị trí ảnh ban đầu?","hd": "Khoảng cách ảnh và gương tăng thêm 10cm.","dd": ["Dời xa thêm 10 cm"],"lg": "S dời xa 10cm ⇒ S' dời xa 10cm so với gương. Vậy ảnh dời đi 10cm."},
            {"de": "Tia sáng SI đi vào mặt nước tĩnh lặng. Giao thoa phản xạ một phần, khúc xạ một phần. Góc tới = 60°. Góc tạo bởi tia phản xạ và mặt nước là bao nhiêu?","hd": "Góc phản xạ = góc tới = 60°. Góc hợp với mặt nước = 90 - 60.","dd": ["30°"],"lg": "Tia phản xạ IR nằm trong môi trường không khí. Góc i' = 60°. Góc hợp với mặt nước = 90° - 60° = 30°."},
            {"de": "Sự khác nhau giữa hiện tượng nhật thực một phần và nhật thực toàn phần nằm ở khái niệm vật lý nào?","hd": "Bóng tối và bóng nửa tối.","dd": ["Người quan sát nằm ở vùng bóng tối (toàn phần) hay vùng bóng nửa tối (một phần) của Mặt Trăng in trên Trái Đất."],"lg": "Bóng tối chặn 100% ánh sáng (toàn phần), bóng nửa tối chặn một phần (một phần)."},
            {"de": "Một phòng tối hoàn toàn. Có một con mèo đen và một con mèo trắng. Bạn bật một chiếc đèn chùm chiếu sáng mờ. Mèo nào dễ được nhìn thấy hơn? Vì sao?","hd": "Màu trắng phản xạ ánh sáng tốt.","dd": ["Mèo trắng dễ nhìn thấy hơn"],"lg": "Màu trắng phản xạ khuếch tán hầu hết ánh sáng chiếu tới, còn màu đen hấp thụ ánh sáng. Do đó có nhiều ánh sáng từ con mèo trắng đến mắt ta hơn."},
            {"de": "Góc tới tăng từ 30° lên 50°. Góc hợp bởi tia tới và tia phản xạ tăng thêm bao nhiêu độ?","hd": "Góc hợp bởi tia tới và phản xạ = 2.i.","dd": ["Tăng thêm 40°"],"lg": "Lúc đầu: 2 × 30° = 60°. Lúc sau: 2 × 50° = 100°. Độ tăng = 100° - 60° = 40°."},
            {"de": "Tại sao các tấm kính phản quang ở các tòa nhà lại gây chói mắt cho người đi đường vào những giờ nhất định?","hd": "Hiện tượng phản xạ ánh sáng chùm song song.","dd": ["Kính phản xạ ánh sáng Mặt Trời theo định luật phản xạ, tạo thành chùm phản xạ cường độ cao chiếu xuống mắt người đi đường."],"lg": "Mặt kính nhẵn bóng hoạt động như một gương phẳng khổng lồ phản xạ ánh sáng mặt trời."},
            {"de": "Một người ngắm viên bi qua một ống thẳng dài 2m. Người đó có thấy viên bi không? Đổi ống thẳng thành ống cong hình chữ U, có thấy không? Tại sao?","hd": "Định luật truyền thẳng.","dd": ["Ống thẳng: Có. Ống cong: Không."],"lg": "Trong không khí ánh sáng truyền theo đường thẳng. Ống cong cản trở đường truyền của tia sáng từ viên bi đến mắt."},
            {"de": "Mép dưới của gương treo tường cách mặt sàn bao nhiêu để một người cao 1m60 (mắt cách đỉnh đầu 10cm) nhìn thấy mũi giày của mình?","hd": "Mắt ở độ cao 1m50. Mũi giày ở độ cao 0m.","dd": ["0,75 mét (75 cm)"],"lg": "Tia sáng từ mũi giày chiếu lên gương phản xạ vào mắt. Vị trí tia sáng chạm gương nằm ở trung điểm của khoảng cách từ mắt đến mũi giày theo phương thẳng đứng. Vậy mép dưới gương = 1,50 / 2 = 0,75m."},
            {"de": "Người ta thường cắm cọc tiêu thẳng hàng bằng cách ngắm sao cho cọc cắm sau che khuất cọc cắm trước. Ứng dụng của định luật nào?","hd": "Định luật truyền thẳng.","dd": ["Định luật truyền thẳng của ánh sáng"],"lg": "Ánh sáng từ cọc phía xa truyền theo đường thẳng, bị cọc phía gần chắn lại, chứng tỏ các cọc nằm trên cùng một đường thẳng."}
        ]
    }
}
VL7["Chương 3: Ánh sáng"] = C3_VL7
# --- Chương 4: Từ trường ---
C4_VL7 = {
    "Từ trường - Nam châm - La bàn (Chuyên sâu)": {
        "ly_thuyet": """📌 1. NAM CHÂM VÀ TỪ TÍNH:
- Nam châm là những vật có từ tính (có khả năng hút được các vật bằng sắt, thép, niken, côban...).
- Mỗi nam châm luôn có hai cực từ: Cực Bắc (N - North) và Cực Nam (S - South). Cực từ là nơi từ tính mạnh nhất.
- Tương tác giữa hai nam châm: Khi đưa từ cực của hai nam châm lại gần nhau, các cực cùng tên thì đẩy nhau, các cực khác tên thì hút nhau.

📌 2. TỪ TRƯỜNG:
- Từ trường là không gian bao xung quanh nam châm (hoặc dòng điện), trong không gian đó có lực từ tác dụng lên một kim nam châm đặt trong nó.
- Ta không thể nhìn thấy từ trường bằng mắt thường, nhưng có thể nhận biết sự tồn tại của nó thông qua lực từ tác dụng lên kim nam châm thử.

📌 3. TỪ PHỔ VÀ ĐƯỜNG SỨC TỪ:
- Từ phổ: Hình ảnh các mạt sắt sắp xếp xung quanh nam châm gọi là từ phổ. Nơi mạt sắt dày đặc thì từ trường mạnh, nơi thưa thì từ trường yếu.
- Đường sức từ: Là các đường cong được vẽ dựa trên hình ảnh từ phổ. 
- Chiều của đường sức từ: Tuân theo quy ước "Ra Bắc, Vào Nam" (Các đường sức từ đi ra từ cực Bắc và đi vào ở cực Nam của nam châm).

📌 4. TỪ TRƯỜNG TRÁI ĐẤT VÀ LA BÀN:
- Trái Đất hoạt động như một thanh nam châm khổng lồ sinh ra từ trường bao quanh nó.
- Từ cực Bắc của Trái Đất nằm gần Cực Nam địa lí, và Từ cực Nam của Trái Đất nằm gần Cực Bắc địa lí (chúng không hoàn toàn trùng nhau).
- La bàn: Dụng cụ dùng để xác định phương hướng dựa vào từ trường Trái Đất. Bộ phận chính là một kim nam châm quay tự do trên một trục nhọn.""",
        
        "vi_du": """💡 VÍ DỤ 1: Tương tác giữa hai cực của nam châm
Đề bài: Có hai thanh nam châm thẳng. Khi đưa đầu A của thanh thứ nhất lại gần đầu B của thanh thứ hai thì chúng hút nhau. Nếu đầu A là cực Bắc (N), hỏi đầu B là cực gì?
- Giải: 
  + Theo tính chất của nam châm: Các cực khác tên thì hút nhau.
  + Vì đầu A là cực Bắc (N) và hút đầu B, nên đầu B phải là cực Nam (S).

💡 VÍ DỤ 2: Xác định chiều của đường sức từ
Đề bài: Xung quanh một thanh nam châm, người ta vẽ một đường sức từ là một đường cong kín. Mũi tên trên đường cong này chỉ hướng từ điểm X sang điểm Y. Điểm X nằm gần một cực từ, điểm Y nằm gần cực từ còn lại. Xác định tên các cực đó.
- Giải:
  + Theo quy ước "Ra Bắc, Vào Nam", đường sức từ đi ra từ cực Bắc và đi vào cực Nam.
  + Vì mũi tên chỉ hướng từ X sang Y (nghĩa là đi ra từ phía X và đi vào ở phía Y), nên cực từ gần X là cực Bắc (N), cực từ gần Y là cực Nam (S).

💡 VÍ DỤ 3: Sử dụng La bàn
Đề bài: Đặt một la bàn trên mặt bàn phẳng. Khi kim la bàn đứng yên, cực Bắc của kim la bàn chỉ về hướng nào về mặt địa lí? Giải thích tại sao?
- Giải:
  + Cực Bắc (N) của kim la bàn sẽ chỉ về hướng Bắc địa lí của Trái Đất.
  + Giải thích: Tại khu vực cực Bắc địa lí của Trái Đất thực chất đang tồn tại Từ cực Nam của nam châm Trái Đất. Do hai cực khác tên hút nhau, Từ cực Nam này sẽ hút Cực Bắc của kim la bàn, khiến kim la bàn định hướng chỉ về phía Bắc địa lí.""",

        "cau_hoi": [
            {"nd": "Vật liệu nào sau đây KHÔNG bị nam châm hút?","da": ["Sắt","Thép","Đồng","Niken"],"d": 2,"gt": "Đồng, nhôm, nhựa, gỗ... không có tính từ nên không bị nam châm hút."},
            {"nd": "Một thanh nam châm có mấy cực từ?","da": ["1 cực","2 cực","3 cực","Không có cực nào"],"d": 1,"gt": "Nam châm luôn có 2 cực: cực Bắc (N) và cực Nam (S)."},
            {"nd": "Khi đưa hai thanh nam châm lại gần nhau, hiện tượng gì xảy ra?","da": ["Cực cùng tên hút nhau, cực khác tên đẩy nhau","Cực cùng tên đẩy nhau, cực khác tên hút nhau","Luôn luôn hút nhau","Luôn luôn đẩy nhau"],"d": 1,"gt": "Quy luật tương tác từ: Cùng từ cực thì đẩy, khác từ cực thì hút."},
            {"nd": "Kí hiệu chữ 'N' trên nam châm có ý nghĩa là gì?","da": ["Cực Nam (South)","Cực Bắc (North)","Cực âm","Cực dương"],"d": 1,"gt": "N là viết tắt của North (hướng Bắc)."},
            {"nd": "Xung quanh nam châm có tồn tại một môi trường vô hình. Môi trường đó gọi là gì?","da": ["Điện trường","Trọng trường","Từ trường","Môi trường chân không"],"d": 2,"gt": "Không gian xung quanh nam châm sinh ra lực từ được gọi là từ trường."},
            {"nd": "Để nhận biết sự tồn tại của từ trường, người ta thường dùng dụng cụ nào?","da": ["Thước mét","Kim nam châm thử","Nhiệt kế","Lực kế"],"d": 1,"gt": "Từ trường tác dụng lực lên kim nam châm thử làm nó lệch khỏi hướng Bắc - Nam ban đầu."},
            {"nd": "Hình ảnh các đường mạt sắt rắc quanh một thanh nam châm được gọi là gì?","da": ["Từ trường","Từ phổ","Đường sức từ","Lực từ"],"d": 1,"gt": "Hình ảnh tạo bởi mạt sắt gọi là từ phổ."},
            {"nd": "Quy ước về chiều của đường sức từ bên ngoài thanh nam châm là:","da": ["Đi ra từ cực Nam, đi vào cực Bắc","Đi ra từ cực Bắc, đi vào cực Nam","Từ trái sang phải","Đi ra từ điểm giữa nam châm"],"d": 1,"gt": "Quy ước chuẩn: 'Ra Bắc, Vào Nam'."},
            {"nd": "Tại những nơi từ trường mạnh, các đường sức từ sẽ được vẽ như thế nào?","da": ["Vẽ thưa nhau","Vẽ dày đặc (mau) hơn","Vẽ song song","Vẽ cắt nhau"],"d": 1,"gt": "Độ mau, thưa của đường sức từ biểu diễn độ mạnh, yếu của từ trường."},
            {"nd": "Trái Đất có từ trường không?","da": ["Không có","Chỉ có ở xích đạo","Có từ trường bao quanh","Chỉ có ở các cực"],"d": 2,"gt": "Trái Đất là một nam châm khổng lồ nên có từ trường bao quanh."},
            {"nd": "Cực Bắc của kim la bàn chỉ về hướng nào về mặt địa lý?","da": ["Hướng Đông","Hướng Tây","Hướng Nam","Hướng Bắc"],"d": 3,"gt": "Kim nam châm luôn tự định hướng dọc theo đường sức từ Trái Đất, cực Bắc của kim chỉ về phía Bắc địa lý."},
            {"nd": "Gần Cực Bắc địa lí của Trái Đất là cực từ gì của Trái Đất?","da": ["Từ cực Bắc","Từ cực Nam","Không có cực từ","Từ cực Đông"],"d": 1,"gt": "Từ cực Nam của Trái Đất nằm gần Cực Bắc địa lí (để hút cực Bắc của kim la bàn)."},
            {"nd": "Khi một thanh nam châm bị gãy làm đôi, điều gì sẽ xảy ra?","da": ["Mỗi nửa trở thành một nam châm mới có đủ 2 cực N, S","Một nửa chỉ có cực N, một nửa chỉ có cực S","Cả hai nửa đều mất từ tính","Từ tính tăng lên gấp đôi"],"d": 0,"gt": "Không thể tách rời hai cực của nam châm. Một mảnh vỡ bất kì luôn tự tạo thành nam châm 2 cực."},
            {"nd": "Để làm giảm hoặc mất từ tính của một nam châm vĩnh cửu, ta có thể làm cách nào?","da": ["Sơn lại nam châm","Bọc nam châm trong nilon","Nung nóng nam châm ở nhiệt độ cao","Ngâm nam châm trong nước đá"],"d": 2,"gt": "Nhiệt độ cao phá vỡ sự sắp xếp trật tự của các miền từ bên trong nam châm."},
            {"nd": "Chữ 'S' trên nam châm biểu thị cực nào?","da": ["Cực Bắc","Cực Nam","Cực từ dương","Cực từ âm"],"d": 1,"gt": "S là viết tắt của South (cực Nam)."},
            {"nd": "Hai đường sức từ của cùng một nam châm có thể cắt nhau không?","da": ["Luôn cắt nhau tại cực","Có thể cắt nhau ở vùng từ trường yếu","Không bao giờ cắt nhau","Cắt nhau tại vị trí trung gian"],"d": 2,"gt": "Qua mỗi điểm trong không gian chỉ vẽ được một đường sức từ duy nhất, nên chúng không cắt nhau."},
            {"nd": "Nếu treo tự do một thanh nam châm thẳng nằm ngang, khi đứng yên nó sẽ chỉ hướng nào?","da": ["Đông - Tây","Bắc - Nam","Đông Bắc - Tây Nam","Tùy ý"],"d": 1,"gt": "Từ trường Trái Đất sẽ định hướng nam châm theo trục Bắc - Nam địa lí."},
            {"nd": "Khi để la bàn gần một dây dẫn có dòng điện mạnh chạy qua, hiện tượng gì xảy ra?","da": ["La bàn chỉ sai hướng do từ trường của dòng điện","La bàn vẫn chỉ hướng Bắc Nam chính xác","Kim la bàn bị hút chặt vào dây dẫn","Kim la bàn ngừng quay"],"d": 0,"gt": "Dòng điện sinh ra từ trường làm nhiễu từ trường Trái Đất quanh la bàn."},
            {"nd": "Ở phần giữa của một thanh nam châm thẳng dài, lực từ như thế nào so với ở hai đầu?","da": ["Mạnh nhất","Bằng 0","Yếu nhất","Bằng lực từ ở hai đầu"],"d": 2,"gt": "Từ tính mạnh nhất ở hai cực và yếu dần về phía giữa nam châm."},
            {"nd": "Tại sao vỏ của la bàn thường được làm bằng nhựa, nhôm hoặc đồng mà không làm bằng sắt?","da": ["Cho nhẹ","Sắt đắt tiền hơn","Vỏ sắt sẽ bị nhiễm từ và cản trở kim la bàn định hướng","Nhựa và nhôm bền hơn"],"d": 2,"gt": "Sắt có tính từ, nếu dùng vỏ sắt sẽ làm kim nam châm bị hút lệch, la bàn không còn chỉ đúng hướng."},
            {"nd": "Chim bồ câu có khả năng tìm đường về tổ cách xa hàng trăm kilomet là nhờ khả năng nào?","da": ["Cảm nhận nhiệt độ","Thị lực siêu phàm","Cảm nhận từ trường Trái Đất","Dựa vào chiều gió"],"d": 2,"gt": "Trong não một số loài chim có các hạt từ tính giúp chúng định vị theo từ trường Trái Đất."},
            {"nd": "Cực Bắc địa lí và Từ cực Nam của Trái Đất có trùng khít lên nhau không?","da": ["Trùng khít 100%","Không trùng, chúng lệch nhau một góc nhỏ","Từ cực Nam nằm ở xích đạo","Từ cực Nam nằm ở hướng Đông"],"d": 1,"gt": "Chúng lệch nhau một góc gọi là góc từ thiên."},
            {"nd": "Trong tự nhiên, loại quặng nào có từ tính mạnh nhất, được xem là nam châm tự nhiên?","da": ["Quặng bô-xít","Quặng man-he-tit (Magnetite)","Đồng sunfat","Than đá"],"d": 1,"gt": "Magnetite (Fe3O4) là đá nam châm tự nhiên."},
            {"nd": "Từ trường đều là từ trường có đặc điểm gì?","da": ["Các đường sức từ là những đường cong khép kín","Các đường sức từ là những đường thẳng song song, cách đều nhau","Từ trường thay đổi theo thời gian","Từ trường của Trái Đất"],"d": 1,"gt": "Định nghĩa từ trường đều (như từ trường giữa 2 nhánh nam châm chữ U)."},
            {"nd": "Trên một đường sức từ, làm thế nào để xác định chiều của từ trường tại một điểm?","da": ["Là hướng của cực Nam kim nam châm thử đặt tại đó","Là hướng từ cực Bắc đến cực Nam của kim nam châm thử đặt tại đó","Vuông góc với đường sức từ","Không thể xác định"],"d": 1,"gt": "Chiều đường sức từ tại một điểm là chiều dọc theo kim nam châm thử định hướng tại đó (từ Nam sang Bắc của kim)."},
            {"nd": "Người ta ứng dụng nam châm để làm gì trong đời sống?","da": ["Làm ruột bút chì","Sản xuất loa điện, động cơ điện, cần cẩu từ","Lọc nước sinh hoạt","Chế tạo pin năng lượng mặt trời"],"d": 1,"gt": "Nam châm là lõi quan trọng của các thiết bị âm thanh và điện từ."},
            {"nd": "Làm thế nào để tạo ra một nam châm tạm thời từ một chiếc đinh sắt?","da": ["Cọ xát đinh sắt nhiều lần vào len","Nung nóng đinh sắt","Chà xát một cực của nam châm vĩnh cửu theo một chiều dọc thân đinh sắt","Ngâm đinh sắt vào nước muối"],"d": 2,"gt": "Cách nhiễm từ cho kim loại là vuốt nam châm theo một chiều."},
            {"nd": "Một chiếc tàu đang đi trên đại dương, thuyền trưởng dùng la bàn thấy kim cực Bắc chỉ về phía trước tàu. Con tàu đang đi về hướng nào?","da": ["Hướng Nam","Hướng Bắc","Hướng Tây","Hướng Đông"],"d": 1,"gt": "Cực Bắc của kim chỉ hướng Bắc, kim hướng về mũi tàu tức là tàu đang tiến về phương Bắc."},
            {"nd": "Nếu đặt hai cực Nam của hai nam châm lại gần nhau, hình ảnh từ phổ ở khoảng giữa hai cực sẽ có đặc điểm gì?","da": ["Các đường mạt sắt nối liền hai cực với nhau","Các đường mạt sắt không nối liền mà uốn cong đẩy xa nhau","Mạt sắt biến mất","Tạo thành các vòng tròn khép kín"],"d": 1,"gt": "Hai cực cùng tên đẩy nhau nên đường sức từ không nối qua lại mà tản ra hai bên."},
            {"nd": "Kim la bàn thực chất là vật gì?","da": ["Một thanh đồng nhỏ","Một nam châm vĩnh cửu nhỏ, nhẹ","Một thanh sắt chưa nhiễm từ","Một thanh nhôm"],"d": 1,"gt": "Kim la bàn là một thanh nam châm nhẹ được đặt trên trục quay."}
        ],

        "bt_co_ban": [
            {"de": "Người ta đánh rơi một cây kim khâu bằng thép xuống các khe sàn nhà bằng gỗ. Nêu một cách đơn giản để lấy cây kim lên mà không phải tháo sàn gỗ.","dd": ["Dùng một cục nam châm mạnh rà sát trên mặt khe hở để hút cây kim lên."],"gt": "Thép là vật liệu từ tính nên bị nam châm hút xuyên qua các khe hẹp."},
            {"de": "Một thanh nam châm bị mất lớp sơn đánh dấu các cực. Bạn có một kim nam châm nhỏ đã biết rõ cực Bắc (N) và cực Nam (S). Hãy nêu cách để xác định lại cực của thanh nam châm đó.","dd": ["Đưa cực N của kim nam châm lại gần 1 đầu của thanh nam châm. Nếu bị hút, đầu đó là cực S. Nếu bị đẩy, đầu đó là cực N."],"gt": "Ứng dụng định luật tương tác từ: Khác cực thì hút, cùng cực thì đẩy."},
            {"de": "Theo quy ước, chiều của đường sức từ bên ngoài một thanh nam châm đi từ cực nào đến cực nào?","dd": ["Từ cực Bắc (N) đến cực Nam (S)."],"gt": "Quy ước 'Ra Bắc, Vào Nam'."},
            {"de": "Giải thích vì sao cực Bắc của kim la bàn lại luôn chỉ về hướng Bắc địa lí của Trái Đất.","dd": ["Vì tại cực Bắc địa lí của Trái Đất tồn tại Từ cực Nam, lực từ này sẽ hút cực Bắc của kim la bàn."],"gt": "Trái Đất là nam châm, từ cực và địa cực ngược tên nhau để tạo lực hút tương ứng cho la bàn."},
            {"de": "Cắt một thanh nam châm thẳng ở đoạn giữa, ta sẽ thu được hai vật gì?","dd": ["Ta thu được 2 thanh nam châm mới ngắn hơn, mỗi thanh đều có đầy đủ 1 cực Bắc và 1 cực Nam."],"gt": "Nam châm không tồn tại đơn cực. Khi gãy, phần mặt đứt gãy tự động hình thành các cực mới."},
            {"de": "Trong các vật dụng sau: Cửa tủ lạnh, La bàn, Loa phát thanh, Cốc thủy tinh, Bàn ủi điện. Những thiết bị nào có sử dụng nam châm?","dd": ["Cửa tủ lạnh, La bàn, Loa phát thanh."],"gt": "Cửa tủ lạnh có dải nam châm cao su để dính chặt. La bàn dùng kim nam châm. Loa có nam châm điện/vĩnh cửu."},
            {"de": "Vẽ phác thảo hình dạng đường sức từ xung quanh một thanh nam châm thẳng. Từ trường mạnh nhất ở đâu?","dd": ["Đường sức từ là các đường cong nối 2 đầu nam châm. Từ trường mạnh nhất ở hai từ cực."],"gt": "Ở 2 cực, số lượng đường sức từ đi qua (độ mau) là dày đặc nhất."},
            {"de": "Đưa thanh nam châm A lại gần thanh nam châm B, thấy chúng đẩy nhau. Kết luận gì về từ cực của hai đầu đang gần nhau?","dd": ["Hai đầu đó là hai cực cùng tên (cùng là cực Bắc hoặc cùng là cực Nam)."],"gt": "Hiện tượng đẩy nhau chỉ xảy ra khi cùng từ cực."},
            {"de": "Tại sao không nên đặt thẻ tín dụng (ATM) hoặc ổ cứng máy tính ngay sát nam châm mạnh?","dd": ["Vì từ trường mạnh của nam châm sẽ làm nhiễu hoặc xóa mất dữ liệu từ tính lưu trên dải từ của thẻ hoặc ổ cứng."],"gt": "Thiết bị lưu trữ dùng từ tính để ghi dữ liệu, gặp từ trường ngoài mạnh sẽ bị sắp xếp lại miền từ, gây mất dữ liệu."},
            {"de": "Đồng, nhôm, bạc có phải là vật liệu từ không? Có làm vỏ la bàn được không?","dd": ["Không phải vật liệu từ. Có thể làm vỏ la bàn được."],"gt": "Vì không có tính từ nên chúng không bị nam châm hút và không làm nhiễu kim la bàn."}
        ],

        "bt_nang_cao": [
            {"de": "Một thanh sắt non và một thanh nam châm thẳng giống hệt nhau về hình dạng, kích thước và màu sắc. Chỉ dùng hai thanh này (không dùng thêm bất cứ dụng cụ nào khác), làm thế nào để biết thanh nào là nam châm?","hd": "Dựa vào đặc điểm lực từ của nam châm phân bố không đều (mạnh ở 2 đầu, yếu ở giữa).","dd": ["Cầm 1 đầu thanh này chạm vào điểm giữa của thanh kia. Phân tích kết quả."],"lg": "Lấy thanh A chạm vào điểm chính giữa của thanh B. Nếu có lực hút mạnh, thì A là nam châm (vì đầu A có từ tính mạnh hút được sắt B). Nếu không hút (hoặc hút rất yếu), thì B là nam châm (vì điểm giữa của nam châm B không có từ tính, không hút được đầu sắt A)."},
            {"de": "Tại sao một cây kim khâu quần áo bình thường để cạnh một nam châm lâu ngày, khi lấy ra cây kim đó lại có thể hút được các mạt sắt nhỏ?","hd": "Hiện tượng nhiễm từ.","dd": ["Cây kim đã bị nhiễm từ và trở thành một nam châm nhân tạo tạm thời."],"lg": "Khi đặt trong từ trường của nam châm, các miền từ (nam châm phân tử) lộn xộn bên trong cây kim thép bị sắp xếp lại theo một hướng nhất định, làm cây kim có từ tính."},
            {"de": "Xung quanh Trái Đất có từ trường, vậy tại sao thanh sắt ở ban công nhà bạn không tự nhiên bay lên và dính vào cực Bắc của Trái Đất?","hd": "Độ lớn của lực từ so với khoảng cách và trọng lực.","dd": ["Vì từ trường Trái Đất trải rộng nhưng cường độ rất yếu, không đủ lực hút để thắng được trọng lực của thanh sắt."],"lg": "Từ trường Trái Đất đủ để làm xoay một chiếc kim la bàn rất nhẹ ít ma sát, nhưng lực từ quá nhỏ để nhấc bổng các vật nặng chống lại lực hút Trái Đất."},
            {"de": "Có hai thanh nam châm đặt trên bàn tạo thành một đường thẳng nằm ngang. Từ phổ giữa hai đầu gần nhau của chúng xuất hiện các đường mạt sắt nối liền từ cực này sang cực kia. Hai cực đó cùng tên hay khác tên? Vẽ chiều đường sức từ nếu một cực là N.","hd": "Các đường mạt sắt nối liền chứng tỏ có lực hút.","dd": ["Hai cực khác tên. Chiều đi từ cực N sang cực S."],"lg": "Vì có các đường sức nối liền nên hai cực hút nhau, suy ra chúng khác tên. Chiều đường sức từ sẽ đi ra khỏi cực N và hướng thẳng chạy vào cực S của nam châm đối diện."},
            {"de": "Góc từ thiên là gì? Ý nghĩa của nó trong hàng hải và hàng không?","hd": "Sự sai lệch giữa trục địa lí và trục từ.","dd": ["Là góc lệch giữa phương Bắc thực (địa lí) và phương Bắc từ (do la bàn chỉ)."],"lg": "Vì Từ cực và Cực địa lý không trùng khít nhau, la bàn chỉ hướng Bắc Từ chứ không phải hướng Bắc Thực. Phi công và thuyền trưởng phải cộng/trừ góc từ thiên trên bản đồ để tàu bay đúng hướng."},
            {"de": "Một nam châm chữ U có hình dạng móng ngựa. Từ trường mạnh nhất nằm ở vị trí nào? Đường sức từ ở khoảng không gian giữa hai nhánh nam châm có đặc điểm gì?","hd": "Hai nhánh là 2 cực N, S.","dd": ["Mạnh nhất ở hai đầu nhánh. Từ trường giữa 2 nhánh là từ trường đều."],"lg": "Từ trường mạnh nhất ở hai cực (đầu móng ngựa). Ở khoảng hẹp giữa hai nhánh, các đường sức từ là những đường thẳng song song cách đều nhau đi từ cực N sang cực S, tạo ra từ trường đều."},
            {"de": "Giải thích vì sao khi bọc một thanh nam châm bằng một ống sắt dày, từ trường bên ngoài ống sắt trở nên rất yếu (Hầu như không hút được đinh bên ngoài)?","hd": "Hiện tượng 'màn chắn từ'.","dd": ["Sắt có độ từ thẩm cao, dẫn từ tốt. Hầu hết các đường sức từ sẽ khép kín ngay bên trong lớp vỏ sắt chứ không thoát ra ngoài."],"lg": "Lớp vỏ sắt hoạt động như một 'đường cao tốc' cho từ trường. Thay vì đi qua không khí, các đường sức từ chọn đi qua vỏ sắt để vòng về cực kia, làm từ trường rò rỉ ra ngoài môi trường giảm đáng kể."},
            {"de": "Nếu đốt nóng một thanh nam châm liên tục trên ngọn lửa đèn cồn, từ tính của nó có thay đổi không? Tại sao?","hd": "Tác động của nhiệt năng.","dd": ["Từ tính bị suy giảm và cuối cùng mất hoàn toàn."],"lg": "Nhiệt năng làm các nguyên tử dao động hỗn loạn dữ dội. Điều này phá vỡ cấu trúc trật tự định hướng của các miền từ bên trong thanh nam châm, khiến chúng quay lung tung và triệt tiêu từ tính của nhau."},
            {"de": "Một học sinh khẳng định: 'Nếu dùng búa đập vỡ cực Bắc của một thanh nam châm, ta sẽ loại bỏ được cực Bắc và thanh nam châm đó chỉ còn lại cực Nam'. Lời khẳng định này đúng hay sai? Lập luận.","hd": "Khái niệm từ cực đôi.","dd": ["Sai. Bất kỳ mảnh vỡ nào cũng tự động tái tạo cực N và S mới tại mặt đứt gãy."],"lg": "Trong nam châm, tính chất hai cực có nguồn gốc từ cấu tạo nguyên tử (spin electron). Không có 'đơn cực từ' trong tự nhiên. Mặt đứt gãy sẽ ngay lập tức trở thành cực Bắc mới cho đoạn còn lại."},
            {"de": "Nam châm điện là gì? Ưu điểm lớn nhất của nam châm điện so với nam châm vĩnh cửu trong ứng dụng cần cẩu phế liệu thép?","hd": "Lõi sắt non cuốn dây điện.","dd": ["Nam châm điện có thể bật/tắt từ tính bằng công tắc và điều chỉnh lực hút."],"lg": "Khi đóng điện, cần cẩu biến thành nam châm hút khối lượng lớn thép. Khi cần thả thép xuống bãi, chỉ việc ngắt dòng điện, từ trường biến mất và thép tự rơi xuống. Nam châm vĩnh cửu không làm được việc nhả ra này."},
            {"de": "Cực Bắc từ của Trái Đất (hiện nằm ở phía Bắc Canada/Nga) đang di chuyển liên tục mỗi năm. Nguyên nhân chính gây ra từ trường của Trái Đất và sự dịch chuyển này là gì?","hd": "Lõi Trái Đất cấu tạo bởi kim loại lỏng.","dd": ["Do sự chuyển động của các dòng kim loại lỏng (sắt, niken) nóng chảy ở lõi ngoài Trái Đất."],"lg": "Chuyển động đối lưu của chất lỏng dẫn điện kết hợp với sự tự quay của Trái Đất sinh ra hiệu ứng dynamo tạo ra từ trường. Do dòng chất lỏng này luôn biến động, nên các từ cực cũng liên tục dịch chuyển."},
            {"de": "Vẽ hình chữ nhật biểu diễn nam châm thẳng. Bên trái là N, bên phải là S. Đặt 1 kim la bàn nhỏ ở ngay phía trên thanh nam châm. Hỏi cực N của kim la bàn sẽ hướng về phía bên nào (Trái hay Phải)?","hd": "Đường sức từ đi ra từ N vòng sang S. Kim la bàn sẽ dọc theo đường tiếp tuyến.","dd": ["Cực N của kim la bàn sẽ hướng về phía bên phải (Về phía cực S của nam châm thẳng)."],"lg": "Phía trên nam châm, đường sức từ đi từ N (Trái) sang S (Phải). Kim nam châm thử luôn có chiều cực N chỉ theo chiều đường sức từ. Do đó cực N của kim la bàn bị hút hướng về phía cực S bên phải."},
            {"de": "Trong các phòng khám chụp cộng hưởng từ (MRI), các bác sĩ yêu cầu bệnh nhân tháo bỏ mọi đồ trang sức, đồng hồ, dây nịt bằng kim loại trước khi vào phòng máy. Lý do liên quan đến từ trường là gì?","hd": "Máy MRI là nam châm siêu dẫn khổng lồ.","dd": ["Máy MRI tạo ra từ trường cực mạnh, nó sẽ hút văng các vật từ tính với tốc độ cao gây sát thương, hoặc làm hỏng thiết bị."],"lg": "Lực từ của máy MRI gấp hàng chục nghìn lần từ trường Trái Đất. Vật liệu sắt từ sẽ biến thành viên đạn nếu bị hút vào máy. Mảnh kim loại trong cơ thể có thể bị sinh nhiệt hoặc dịch chuyển gây nguy hiểm."},
            {"de": "Động vật di cư như rùa biển, chim én tìm đường đi chính xác hàng nghìn km. Giải thuyết khoa học hiện nay về khả năng định hướng của chúng liên quan đến kiến thức nào của Chương 4?","hd": "Cảm nhận từ trường Trái Đất.","dd": ["Sinh vật có khả năng cảm nhận từ trường Trái Đất (Magnetoreception)."],"lg": "Trong cơ thể chúng chứa các tinh thể magnetite nhỏ, hoặc có cơ chế hóa học nhạy cảm với sự thay đổi của độ nghiêng và cường độ đường sức từ Trái Đất, giúp chúng có 'GPS sinh học'."},
            {"de": "Lực từ có tác dụng xuyên qua chân không hay không? Giải thích hiện tượng thực tế.","hd": "Bản chất của từ trường không cần vật chất trung gian.","dd": ["Có. Môi trường chân không không cản trở từ trường."],"lg": "Nếu đặt một nam châm ngoài vỏ tàu vũ trụ và một vật bằng sắt bên trong cửa sổ kính (có lớp chân không), nam châm vẫn hút vật sắt bình thường. Ánh sáng (sóng điện từ) truyền được trong chân không thì từ trường cũng vậy."},
            {"de": "Hai thanh nam châm thẳng đặt vuông góc với nhau (chữ T). Cực N của thanh 1 chạm vào điểm chính giữa của thanh 2. Có hiện tượng hút/đẩy xảy ra không?","hd": "Điểm giữa nam châm (trung hòa từ).","dd": ["Không có lực hút đáng kể (hoặc rất yếu)."],"lg": "Tại điểm chính giữa (đường trung hòa từ) của thanh 2, các miền từ đã tự triệt tiêu từ tính của nhau ra bên ngoài. Nên cực N của thanh 1 không chịu tác dụng lực hút/đẩy rõ rệt từ thanh 2."},
            {"de": "Để bảo quản hai thanh nam châm chữ U, người ta thường ghép ngược cực hai nhánh của chúng lại với nhau (N chạm S, S chạm N). Tại sao cách này giữ từ tính lâu hơn?","hd": "Tạo vòng từ kín.","dd": ["Để tạo thành một mạch từ khép kín, giữ cho các đường sức từ không bị khuếch tán ra ngoài môi trường."],"lg": "Các đường sức từ sẽ truyền trực tiếp từ N của nam châm này sang S của nam châm kia và ngược lại, tạo thành vòng lặp vững chắc, bảo vệ các miền từ bên trong không bị rối loạn do môi trường."},
            {"de": "Trái Đất mất đi từ trường, hậu quả nghiêm trọng nhất đối với sự sống trên mặt đất là gì? (Kiến thức tích hợp Vật lí - Địa lí).","hd": "Tác dụng lá chắn của từ trường đối với Bão mặt trời.","dd": ["Sự sống có thể bị tiêu diệt do bức xạ vũ trụ và gió mặt trời thổi bay bầu khí quyển."],"lg": "Từ trường Trái Đất hoạt động như một lá chắn (Từ quyển), làm lệch hướng các hạt mang điện năng lượng cao từ Mặt Trời. Không có nó, bầu khí quyển sẽ bị bào mòn và bức xạ gây ung thư sẽ chiếu thẳng xuống mặt đất."},
            {"de": "Có ý kiến cho rằng: 'Nếu ta ở đúng tại Cực Bắc địa lý của Trái Đất, cầm một chiếc la bàn trên tay, kim la bàn sẽ quay loạn xạ không xác định được hướng'. Ý kiến này đúng hay sai theo góc nhìn Vật lý?","hd": "Các đường sức từ đi cắm thẳng xuống đất tại cực từ. Cực địa lí và cực từ cách nhau một khoảng.","dd": ["Ý kiến có phần đúng về hiện tượng kim không chỉ phương ngang, nhưng lí do vật lí sâu xa là do đường sức từ cắm thẳng đứng."],"lg": "Tại khu vực gần cực, các đường sức từ của Trái Đất không đi song song với mặt đất mà đâm thẳng góc xuống lòng đất (Góc từ khuynh). Kim la bàn thông thường chỉ quay theo mặt phẳng ngang nên lực từ kéo một đầu kim cắm xuống dưới, gây ma sát làm nó khó quay ngang chính xác. Hơn nữa Mọi hướng ngang lúc này đều là hướng Nam."},
            {"de": "Đọc bản vẽ kỹ thuật: S - N ... N - S. Vẽ đường sức từ giữa hai cực N và N đứng đối diện nhau. Có điểm nào ở giữa chúng mà kim nam châm thử đứng yên không chịu lực tác dụng không?","hd": "Từ trường triệt tiêu nhau.","dd": ["Có 1 điểm gọi là điểm trung hòa từ."],"lg": "Các đường sức từ đẩy nhau uốn cong ra ngoài. Tại điểm chính giữa khoảng cách nối 2 cực N, hai véc-tơ cảm ứng từ ngược chiều, cùng độ lớn sẽ cộng lại bằng 0. Đặt kim la bàn nhỏ tại điểm chính xác đó, nó sẽ không chịu lực quay."}
        ]
    }
}

VL7["Chương 4: Từ trường"] = C4_VL7

VATLY["Lớp 7"] = VL7