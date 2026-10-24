# -*- coding: utf-8 -*-
"""
NGÂN HÀNG DỮ LIỆU MÔN NGỮ VĂN - LỚP 7 (BẢN MỞ RỘNG)
Bộ sách: Kết nối tri thức với cuộc sống

Cấu trúc (app đọc đúng cấu trúc này):
  VAN["Lớp 7"][Chương][Văn bản] = {
      ly_thuyet, vi_du, cau_hoi, bt_co_ban, bt_nang_cao
  }
  - cau_hoi:      cau(nd, dung, sai, vi_tri_dung, gt)  -> {"nd", "da", "d", "gt"}
  - bt_co_ban:    {"de", "dd", "lg"}
  - bt_nang_cao:  {"de", "hd", "dd", "lg", "kieu"}

Ghi chú: nội dung dựa trên các chi tiết có trong bản văn giáo viên cung cấp.
Trước khi đưa vào sử dụng chính thức, giáo viên nên đối chiếu lại với
văn bản trong sách giáo khoa đang dùng.
"""


# ============================================================
# HÀM TẠO DỮ LIỆU
# ============================================================
def cau(nd, dung, sai, vi_tri_dung, gt=""):
    """Tạo câu trắc nghiệm: đáp án đúng được đặt ở vị trí vi_tri_dung."""
    phuong_an = list(sai)
    phuong_an.insert(vi_tri_dung, dung)
    return {"nd": nd, "da": phuong_an, "d": vi_tri_dung, "gt": gt}


def bt(de, dd, lg=""):
    return {"de": de, "dd": dd, "lg": lg}


def nc(de, hd, dd, lg="", kieu="tu_luan"):
    return {"de": de, "hd": hd, "dd": dd, "lg": lg, "kieu": kieu}


def bai(ly_thuyet, vi_du, cau_hoi, bt_co_ban, bt_nang_cao):
    return {
        "ly_thuyet": ly_thuyet,
        "vi_du": vi_du,
        "cau_hoi": cau_hoi,
        "bt_co_ban": bt_co_ban,
        "bt_nang_cao": bt_nang_cao,
    }


# ============================================================
# VĂN BẢN: BỒNG CHANH ĐỎ (ĐỖ CHU)
# ============================================================
BCD_LY_THUYET = """I. TÁC GIẢ, TÁC PHẨM
1. Tác giả Đỗ Chu: nhà văn Việt Nam, viết nhiều truyện ngắn và tùy bút về thiên nhiên, tuổi thơ và con người quê hương. Giọng văn đằm thắm, giàu cảm xúc.
2. Tác phẩm "Bồng chanh đỏ":
- Thể loại: truyện ngắn.
- Đề tài: tuổi thơ, thế giới loài vật và thiên nhiên.
- Ngôi kể: ngôi thứ nhất, người kể là nhân vật "tôi" (Hoài). Ngôi kể này giúp người đọc đi cùng những rung cảm, suy nghĩ và sự thay đổi trong tâm lí của nhân vật.
- Nhân vật chính: Hoài (người em, người kể chuyện), anh Hiên (người anh), đôi chim bồng chanh đỏ.

II. TÓM TẮT CÁC SỰ VIỆC CHÍNH
1. Hai anh em say mê bầy chim bồng chanh đỏ và muốn bắt chim non về nuôi.
2. Hoài háo hức, tìm cách bắt chim; anh Hiên hiểu biết về loài chim và cùng suy nghĩ về việc làm ấy.
3. Khi đã bắt được chim non, anh Hiên nhận ra việc chia cắt gia đình loài chim là điều không nên, nên khuyên thả chim về với bố mẹ.
4. Hoài ngần ngừ, tiếc nuối, nhưng cuối cùng cùng anh thả chim trở về.
5. Đôi chim bồng chanh trở lại đầm nước, sự sống của thiên nhiên tiếp tục.

III. GIÁ TRỊ NỘI DUNG
- Ca ngợi tâm hồn trong sáng, lòng nhân ái và tình yêu thiên nhiên của hai anh em.
- Thông điệp: trân trọng sự sống của muôn loài, tôn trọng quyền được sống tự do của thiên nhiên.
- Truyện cho thấy bước trưởng thành trong nhận thức của Hoài: từ ham muốn chiếm hữu đến biết yêu thương và tôn trọng.

IV. GIÁ TRỊ NGHỆ THUẬT
- Kể chuyện theo ngôi thứ nhất, giúp diễn tả chân thực cảm xúc của trẻ thơ.
- Miêu tả loài chim bằng màu sắc và hình ảnh giàu tính tạo hình (hình ảnh "đốm lửa" đỏ rực).
- Đối thoại tự nhiên, giàu tính biểu cảm; miêu tả tâm lí nhân vật tinh tế.

V. KIẾN THỨC ĐỌC HIỂU CẦN NHỚ
- Ngôi kể và điểm nhìn: ngôi thứ nhất cho phép đọc thấy suy nghĩ thật của nhân vật "tôi"; em cần phân biệt người kể và tác giả.
- Diễn biến tâm lí: đọc hành động, lời nói và suy nghĩ của nhân vật để hiểu sự thay đổi trong tâm trạng.
- Chi tiết nghệ thuật: một chi tiết nhỏ (màu chim, hành động thả chim) thường mang ý nghĩa lớn.

VI. KĨ NĂNG VIẾT ĐOẠN PHÂN TÍCH
- Nêu luận điểm (nhân vật có đặc điểm gì).
- Dẫn chứng (chi tiết trong truyện).
- Phân tích (vì sao chi tiết ấy thể hiện đặc điểm đó).
- Liên hệ hoặc rút ra bài học.
"""

BCD_VI_DU = """VÍ DỤ 1: Phân tích tâm lí qua hành động
Khi anh Hiên khuyên thả chim, Hoài ngần ngừ và tiếc nuối. Điều đó cho thấy tình cảm ban đầu của em là tự nhiên, nhưng lí trí và lòng nhân ái đã giúp em đi đến quyết định đúng đắn.

VÍ DỤ 2: Đọc hiểu hình ảnh biểu tượng
Hình ảnh "đốm lửa" đỏ rực gợi vẻ đẹp rực rỡ và sức sống mãnh liệt của thiên nhiên. Hình ảnh ấy làm cho người đọc cảm nhận rõ hơn giá trị của sự sống.

VÍ DỤ 3: Từ chi tiết đến ý nghĩa
Chi tiết "thả chim trở về" không chỉ là một hành động. Nó thể hiện bước trưởng thành của Hoài và thông điệp về sự tôn trọng tự do của muôn loài.
"""

BCD_CAU_HOI = [
    # --- Tác giả, thể loại, ngôi kể ---
    cau("Truyện ngắn \"Bồng chanh đỏ\" thuộc thể loại nào?",
        "Truyện ngắn", ["Tùy bút", "Thơ tự do", "Kịch bản"], 0,
        "Đây là một truyện ngắn có cốt truyện, nhân vật và diễn biến rõ ràng."),
    cau("Truyện được kể theo ngôi thứ mấy?",
        "Ngôi thứ nhất", ["Ngôi thứ ba", "Ngôi thứ hai", "Kết hợp nhiều ngôi"], 1,
        "Người kể là nhân vật \"tôi\" (Hoài), nên đây là ngôi thứ nhất."),
    cau("Người kể chuyện (nhân vật \"tôi\") trong truyện là ai?",
        "Hoài", ["Anh Hiên", "Bố của Hoài", "Một người bạn cùng lớp"], 2,
        "Hoài là người em, đồng thời là người kể chuyện."),
    cau("Anh Hiên trong truyện là người như thế nào đối với Hoài?",
        "Người anh", ["Người bạn học", "Người hàng xóm", "Người thầy"], 0,
        "Anh Hiên là người anh trai trong gia đình, cùng Hoài trải qua câu chuyện."),
    cau("Tác giả Đỗ Chu nổi tiếng với hai thể loại chính nào?",
        "Truyện ngắn và tùy bút", ["Kịch và thơ tự do", "Tiểu thuyết lịch sử", "Truyện cổ tích"], 0,
        "Đỗ Chu được biết đến nhiều với truyện ngắn và tùy bút."),
    cau("Nhan đề \"Bồng chanh đỏ\" gọi đến đối tượng nào?",
        "Một loài chim", ["Một loài cây", "Một địa danh", "Một nhân vật"], 0,
        "Nhan đề nêu tên loài chim là đối tượng trung tâm của câu chuyện."),
    cau("Loài chim bồng chanh đỏ trong truyện có bộ lông như thế nào?",
        "Đỏ rực", ["Trắng muốt", "Đen tuyền", "Xanh lam"], 3,
        "Hình ảnh chim được miêu tả với sắc đỏ nổi bật, như một đốm lửa."),
    cau("Bồng chanh thuộc họ chim nào?",
        "Họ bói cá", ["Họ gà", "Họ sẻ", "Họ cò"], 1,
        "Bồng chanh là loài chim nhỏ thuộc họ bói cá."),

    # --- Nội dung ---
    cau("Sự việc mở đầu của câu chuyện là gì?",
        "Hai anh em say mê bầy chim bồng chanh và muốn bắt chim non", ["Hai anh em đi học xa", "Hai anh em đi biển", "Gia đình chuyển nhà"], 2,
        "Câu chuyện bắt đầu từ sự say mê và mong muốn bắt chim của hai anh em."),
    cau("Ban đầu, thái độ của Hoài đối với đàn chim là gì?",
        "Say mê và muốn bắt chim về nuôi", ["Sợ hãi và tránh xa", "Ghét bỏ", "Thờ ơ, không quan tâm"], 0,
        "Hoài háo hức muốn bắt chim non, thể hiện khát khao sở hữu của tuổi thơ."),
    cau("Anh Hiên là người như thế nào?",
        "Am hiểu loài chim, có lòng nhân ái", ["Ích kỉ, chỉ nghĩ đến bản thân", "Lười biếng, thờ ơ", "Sợ hãi mọi thứ"], 3,
        "Anh Hiên hiểu biết về loài chim và biết nghĩ cho sự sống của muôn loài."),
    cau("Vì sao anh Hiên khuyên thả chim non về tổ?",
        "Vì chim bố mẹ còn đang chờ con nhỏ", ["Vì chim non bị bệnh", "Vì sợ bố mẹ mắng", "Vì chim không đẹp như tưởng tượng"], 1,
        "Anh Hiên nhận ra việc chia cắt gia đình loài chim là không nên."),
    cau("Quyết định cuối cùng của hai anh em là gì?",
        "Thả chim trở về với tự nhiên", ["Mang chim về nhà nuôi", "Bán chim lấy tiền", "Nhốt chim vào lồng kín"], 0,
        "Hai anh em quyết định thả chim, trả lại tự do cho chúng."),
    cau("Sự thay đổi của Hoài trong truyện được thể hiện rõ nhất ở điểm nào?",
        "Từ ham muốn chiếm hữu đến yêu thương và tôn trọng sự sống", ["Từ yêu thương đến ghét bỏ", "Từ vui vẻ đến buồn chán", "Không có sự thay đổi"], 2,
        "Hoài trưởng thành trong nhận thức, biết trân trọng tự do của loài vật."),
    cau("Cảm xúc của Hoài khi nhìn bầy chim bay đi là gì?",
        "Tiếc nuối nhưng thấy việc làm của mình là đúng", ["Hối hận muốn bắt lại", "Vui mừng vì được thưởng", "Sợ hãi và lo lắng"], 3,
        "Hoài vừa tiếc nuối vừa cảm thấy đúng đắn khi đã trả tự do cho chim."),
    cau("Chi tiết đôi chim bồng chanh trở lại đầm nước mang ý nghĩa gì?",
        "Sự sống trở lại, thiên nhiên đón nhận hành động nhân hậu", ["Cái kết buồn cho loài chim", "Chim bị săn bắt", "Chim bỏ đi biệt tích"], 0,
        "Sự trở về của đôi chim cho thấy sức sống của thiên nhiên và niềm vui cho con người."),

    # --- Nghệ thuật ---
    cau("Ngôi kể thứ nhất giúp câu chuyện có tác dụng gì?",
        "Bộc lộ chân thực rung cảm và suy nghĩ của nhân vật", ["Che giấu cảm xúc của nhân vật", "Làm câu chuyện khô khan", "Kể chuyện bằng thơ"], 1,
        "Khi kể theo ngôi thứ nhất, người đọc hiểu rõ hơn tâm trạng của nhân vật \"tôi\"."),
    cau("Phương thức biểu đạt chính của văn bản là gì?",
        "Tự sự kết hợp miêu tả và biểu cảm", ["Nghị luận", "Thuyết minh", "Hành chính"], 2,
        "Văn bản kể chuyện (tự sự), kết hợp miêu tả cảnh vật và bộc lộ cảm xúc."),
    cau("Việc miêu tả loài chim trong truyện chủ yếu dựa vào yếu tố nào?",
        "Màu sắc và hình ảnh sinh động", ["Số liệu thống kê", "Lập luận chặt chẽ", "Đối thoại với tác giả"], 3,
        "Các chi tiết về màu sắc, hình dáng giúp chim hiện lên rất sinh động."),
    cau("Lời đối thoại của nhân vật trong truyện có đặc điểm gì?",
        "Tự nhiên, giàu tính biểu cảm", ["Trang trọng như văn bản hành chính", "Toàn bằng thơ", "Không có đối thoại"], 0,
        "Đối thoại gần với lời nói hằng ngày, giúp nhân vật gần gũi với người đọc."),
    cau("Khi đọc truyện, em cần chú ý đến yếu tố nào để hiểu tâm lí nhân vật?",
        "Lời nói, hành động và suy nghĩ của nhân vật", ["Tên nhà xuất bản", "Số trang của cuốn sách", "Ngày in ấn"], 0,
        "Tâm lí nhân vật được thể hiện qua lời nói, hành động và suy nghĩ."),
    cau("Tình huống trung tâm của truyện là gì?",
        "Hai anh em gặp đàn bồng chanh và phải lựa chọn giữa bắt chim và thả chim", ["Lễ hội làng quê", "Cuộc thi học sinh giỏi", "Chuyến du lịch biển"], 1,
        "Tình huống lựa chọn ấy làm nổi bật tư tưởng nhân văn của truyện."),

    # --- Hiểu sâu và tư duy ---
    cau("Thông điệp chính của truyện là gì?",
        "Trân trọng sự sống và tự do của muôn loài", ["Thiên nhiên đáng sợ cần tránh xa", "Cần săn bắt để kiếm tiền", "Trẻ em không nên yêu động vật"], 0,
        "Truyện khuyên con người biết tôn trọng sự sống và quyền tự do của tự nhiên."),
    cau("Vì sao Hoài tiếc nuối nhưng vẫn làm điều đúng?",
        "Tình cảm ban đầu là tự nhiên, nhưng lí trí và lòng nhân ái giúp em chọn đúng", ["Vì em không biết đúng sai", "Vì em ghét anh Hiên", "Vì chim không đẹp"], 0,
        "Tiếc nuối là cảm xúc tự nhiên; điều đáng quý là Hoài đã vượt qua ham muốn của bản thân."),
    cau("Sự khác nhau giữa nuôi nhốt và yêu thương đích thực là gì?",
        "Nuôi nhốt để chiếm hữu, còn yêu thương là mong sinh vật được sống tự do", ["Hai việc giống nhau hoàn toàn", "Nuôi nhốt là cách yêu thương tốt hơn", "Không có sự khác biệt"], 0,
        "Yêu thương đích thực là tôn trọng bản chất tự do của sinh vật."),
    cau("Điều gì khiến quyết định thả chim có sức thuyết phục nhất?",
        "Nhận thức được sự chia cắt gia đình loài chim là điều đáng tiếc", ["Vì sợ bị phạt", "Vì trời đang mưa", "Vì chim đã chết"], 1,
        "Lập luận của anh Hiên dựa trên sự thấu hiểu đời sống của loài vật."),
    cau("Hình ảnh \"đốm lửa\" đỏ rực trong truyện gợi điều gì?",
        "Sức sống và vẻ đẹp rực rỡ của thiên nhiên", ["Sự nóng giận", "Nguy hiểm đang đến", "Mùa hè nắng gắt"], 0,
        "Hình ảnh ấy gợi sức sống mãnh liệt và vẻ đẹp của thiên nhiên tuổi thơ."),
    cau("Nếu bỏ đi đoạn thả chim, câu chuyện sẽ mất đi điều gì quan trọng nhất?",
        "Tính nhân văn và bước trưởng thành của Hoài", ["Tên gọi của truyện", "Ngôi kể", "Số lượng nhân vật"], 2,
        "Đoạn thả chim là bước ngoặt làm nổi bật tư tưởng và sự trưởng thành của nhân vật."),
    cau("Trong bài \"Bầy chim chìa vôi\" cùng bài học, điều gì được thể hiện tương tự \"Bồng chanh đỏ\"?",
        "Tình thương đối với loài vật và tâm hồn trong sáng của trẻ thơ", ["Nỗi sợ hãi thiên nhiên", "Sự chia li bi thảm", "Cuộc đấu tranh giữa các loài"], 0,
        "Cả hai truyện đều ca ngợi tình yêu thương của trẻ thơ với loài vật."),
    cau("Vai trò của anh Hiên trong cốt truyện là gì?",
        "Dẫn dắt, giúp Hoài nhận thức đúng về sự sống", ["Chỉ đứng xem", "Là nhân vật phản diện", "Là người lạ xuất hiện một lần"], 0,
        "Anh Hiên có vai trò quan trọng trong việc thay đổi nhận thức của Hoài."),
    cau("Điều rút ra cho bản thân sau khi đọc truyện là gì?",
        "Biết yêu thương và tôn trọng sự sống của muôn loài", ["Không cần quan tâm đến loài vật", "Chỉ cần học giỏi là đủ", "Nên bắt chim về nuôi"], 1,
        "Đây là bài học nhân văn mà truyện gửi gắm đến người đọc, đặc biệt là học sinh."),
    cau("Trong văn bản, nhân vật \"tôi\" đóng vai trò gì?",
        "Vừa là người kể chuyện, vừa là nhân vật trong truyện", ["Chỉ là người đứng ngoài quan sát", "Là tác giả của truyện", "Là một con chim"], 0,
        "Nhân vật \"tôi\" vừa kể lại câu chuyện, vừa trực tiếp tham gia vào các sự việc."),
    cau("Đặt nhan đề \"Bồng chanh đỏ\" có tác dụng gì?",
        "Gây chú ý về hình ảnh loài chim và màu sắc nổi bật", ["Cho biết địa điểm", "Cho biết tác giả", "Cho biết thời gian"], 0,
        "Nhan đề nêu bật đối tượng và màu sắc, tạo ấn tượng ban đầu cho người đọc."),
    cau("Hoài thay đổi cách nhìn về loài chim sau sự việc này. Đó là sự thay đổi từ:",
        "Muốn sở hữu sang muốn bảo vệ", ["Yêu thích sang ghét bỏ", "Sợ hãi sang tò mò", "Vui vẻ sang buồn bã"], 2,
        "Hoài từ ham muốn chiếm hữu chuyển sang tôn trọng và bảo vệ sự sống."),
    cau("Chủ đề chung của truyện là gì?",
        "Tuổi thơ, thiên nhiên và lòng nhân ái", ["Chiến tranh và hòa bình", "Kinh doanh và thương mại", "Khám phá vũ trụ"], 0,
        "Truyện xoay quanh thế giới tuổi thơ, tình yêu thiên nhiên và lòng nhân ái."),
    cau("Câu chuyện giúp người đọc hiểu ra điều gì về tự do?",
        "Mỗi sinh vật đều có quyền được sống tự do trong môi trường của mình", ["Chỉ con người mới có quyền tự do", "Tự do là sự nuôi nhốt", "Tự do không quan trọng"], 0,
        "Truyện gợi ý rằng tự do là quyền sống tự nhiên của muôn loài."),
    cau("Vì sao có thể nói truyện có kết thúc giàu ý nghĩa?",
        "Vì kết thúc khẳng định sức sống của thiên nhiên và sự thay đổi nhân ái của Hoài", ["Vì kết thúc buồn bã", "Vì kết thúc không rõ ràng", "Vì kết thúc có nhiều bạo lực"], 0,
        "Kết thúc vừa mở ra niềm vui của thiên nhiên, vừa cho thấy sự trưởng thành của nhân vật."),
]


BCD_BT_CO_BAN = [
    bt("Bài 1: Tóm tắt truyện \"Bồng chanh đỏ\" trong khoảng 5 đến 7 câu.",
       ["Hai anh em say mê đàn bồng chanh; Hoài muốn bắt chim non; anh Hiên khuyên thả chim về tổ; hai anh em thả chim và đôi chim trở lại đầm nước."],
       "Tóm tắt theo đúng trình tự các sự việc chính, không đưa ý kiến cá nhân vào phần tóm tắt."),
    bt("Bài 2: Xác định nhân vật chính của truyện và nêu vai trò của từng nhân vật.",
       ["Hoài là người kể chuyện và là nhân vật chính; anh Hiên giúp Hoài nhận thức đúng; đôi chim bồng chanh là đối tượng làm nổi bật tư tưởng của truyện."],
       "Phân biệt được người kể chuyện với nhân vật chính và các nhân vật khác."),
    bt("Bài 3: Tìm những chi tiết miêu tả vẻ đẹp của con chim bồng chanh đỏ.",
       ["Bộ lông đỏ rực, như một đốm lửa; hình dáng nhỏ nhắn, bay bổng."],
       "Chú ý các từ ngữ chỉ màu sắc và hình ảnh so sánh, ẩn dụ trong câu văn."),
    bt("Bài 4: Sắp xếp các sự việc sau theo đúng trình tự câu chuyện: (a) thả chim về tổ; (b) phát hiện đàn bồng chanh; (c) anh Hiên khuyên không bắt chim; (d) đôi chim trở lại đầm nước.",
       ["b - c - a - d"],
       "Sự việc mở đầu là phát hiện đàn chim; tiếp theo là lời khuyên của anh Hiên; sau đó thả chim và kết thúc bằng sự trở lại của đôi chim."),
    bt("Bài 5: Nêu cảm xúc của Hoài ở hai thời điểm: lúc muốn bắt chim và lúc nhìn chim bay đi.",
       ["Lúc đầu: say mê, háo hức, muốn bắt chim về nuôi. Lúc sau: tiếc nuối nhưng thấy việc làm của mình là đúng đắn."],
       "So sánh hai thời điểm để thấy rõ sự thay đổi trong tâm lí nhân vật."),
    bt("Bài 6: Xác định ngôi kể trong truyện và nêu một tác dụng của ngôi kể đó.",
       ["Ngôi thứ nhất; giúp người đọc hiểu trực tiếp suy nghĩ và cảm xúc của nhân vật \"tôi\"."],
       "Ngôi kể thứ nhất gắn với người kể là một nhân vật trong truyện."),
    bt("Bài 7: Từ hình ảnh \"đốm lửa\" đỏ rực, em hiểu thế nào về vẻ đẹp của thiên nhiên?",
       ["Vẻ đẹp rực rỡ, tràn đầy sức sống của thiên nhiên, gợi niềm yêu quý và trân trọng."],
       "Hình ảnh so sánh giúp người đọc hình dung màu sắc và sức sống của chim."),
    bt("Bài 8: Nêu thông điệp chính của truyện bằng một câu.",
       ["Hãy trân trọng sự sống và tôn trọng quyền tự do của muôn loài."],
       "Thông điệp được rút ra từ hành động và sự thay đổi của nhân vật Hoài."),
]


BCD_BT_NANG_CAO = [
    nc("Bài tập 1: Phân tích diễn biến tâm lí của nhân vật Hoài từ lúc muốn bắt chim đến khi quyết định thả chim (viết một đoạn văn khoảng 10 đến 12 câu).",
       "Chia diễn biến thành các giai đoạn: say mê, háo hức; hụt hẫng hoặc ngần ngừ; tiếc nuối nhưng đồng tình; thức tỉnh và trân trọng sự tự do của chim.",
       ["Đoạn văn cần nêu được ba giai đoạn tâm lí của Hoài, dẫn chứng từ hành động và lời nói, và rút ra sự trưởng thành của nhân vật."],
       "Diễn biến tâm lí được thể hiện chân thực: từ bản năng muốn chiếm hữu đến tình yêu thương và sự tôn trọng thiên nhiên."),
    nc("Bài tập 2: Viết đoạn văn (7 đến 10 câu) phân tích ý nghĩa biểu tượng của hình ảnh \"đốm lửa\" đỏ rực.",
       "Liên hệ với vẻ đẹp rực rỡ của loài chim và sức sống của thiên nhiên; có thể nói đến khát vọng và niềm tin của tuổi thơ.",
       ["Đoạn văn nêu được vẻ đẹp và sức sống của thiên nhiên, có dẫn chứng từ hình ảnh chim trong truyện, và có ý nghĩa biểu tượng."],
       "Hình ảnh đốm lửa không chỉ tả màu lông mà còn gợi sức sống mãnh liệt của thiên nhiên và ngọn lửa nhân ái trong tâm hồn tuổi thơ."),
    nc("Bài tập 3: Viết đoạn văn nghị luận khoảng 200 chữ bàn về ý thức bảo vệ các loài động vật hoang dã, dựa trên thông điệp của truyện \"Bồng chanh đỏ\".",
       "Mở đoạn nêu vấn đề; thân đoạn nêu thực trạng và lí do; kết đoạn nêu hành động cụ thể của bản thân.",
       ["Đoạn văn có luận điểm rõ ràng, lập luận có dẫn chứng từ truyện, và kết thúc bằng việc làm cụ thể mà học sinh có thể thực hiện."],
       "Bài viết cần bám vào thông điệp của truyện, không đi quá xa khỏi nội dung văn bản."),
    nc("Bài tập 4: So sánh cách thể hiện lòng yêu thương loài vật trong \"Bồng chanh đỏ\" và \"Bầy chim chìa vôi\" (về điểm nhìn, nhân vật và thông điệp).",
       "Lập bảng ba cột: điểm nhìn, nhân vật, thông điệp. Sau đó viết thành đoạn văn khoảng 8 đến 10 câu.",
       ["Hai truyện đều thể hiện tình yêu thương loài vật của trẻ thơ; đều kể qua điểm nhìn của nhân vật trẻ em; đều gửi gắm thông điệp về sự sống và sự nhân hậu."],
       "Điểm chung là tình thương của trẻ thơ với loài vật; điểm riêng nằm ở tình huống và cách nhân vật thể hiện tình cảm."),
    nc("Bài tập 5: Viết đoạn đối thoại ngắn (khoảng 8 đến 10 lượt lời) giữa anh Hiên và Hoài trước khi thả chim.",
       "Lời của anh Hiên thể hiện sự hiểu biết và lòng nhân ái; lời của Hoài thể hiện sự tiếc nuối và ngần ngừ.",
       ["Đoạn đối thoại tự nhiên, thể hiện được tính cách hai nhân vật và dẫn đến quyết định thả chim."],
       "Khi viết đối thoại, cần giữ đúng tính cách: anh hiểu biết, điềm đạm; em hồn nhiên, còn tiếc nuối."),
    nc("Bài tập 6: Tưởng tượng em là Hoài, viết một đoạn nhật kí (5 đến 7 câu) sau khi thả chim về tổ.",
       "Nhật kí là lời tự bạch; hãy nói về cảm xúc, suy nghĩ và điều em rút ra được.",
       ["Đoạn nhật kí thể hiện được sự tiếc nuối, niềm vui và bài học rút ra từ việc làm của mình."],
       "Bài viết cần chân thực, thể hiện được sự trưởng thành trong suy nghĩ của nhân vật."),
    nc("Bài tập 7: Tranh luận: \"Nuôi chim trong lồng cũng là một cách yêu thương.\" Em đồng ý hay không đồng ý? Trình bày lập luận của em khoảng 150 đến 200 chữ.",
       "Nêu quan điểm rõ ràng; đưa ra ít nhất hai lí lẽ; dẫn chứng từ truyện để phản bác hoặc củng cố lập luận.",
       ["Bài viết có quan điểm rõ ràng, lập luận có lí lẽ và dẫn chứng, biết so sánh giữa yêu thương và chiếm hữu."],
       "Với bài tranh luận, không có một đáp án duy nhất; quan trọng là lập luận chặt chẽ và có căn cứ."),
    nc("Bài tập 8: Viết bài văn ngắn (khoảng 300 chữ) phân tích nhân vật anh Hiên qua các sự việc trong truyện.",
       "Dàn ý gồm: mở bài (giới thiệu nhân vật), thân bài (hiểu biết về loài chim; lòng nhân ái; vai trò với Hoài), kết bài (đánh giá và cảm nghĩ).",
       ["Bài văn có dàn ý rõ ràng, phân tích được ít nhất hai phẩm chất của anh Hiên, dẫn chứng từ truyện, và có cảm nhận cá nhân."],
       "Khi phân tích nhân vật, cần đi từ hành động và lời nói để rút ra phẩm chất, tránh chỉ kể lại truyện."),
]


# ============================================================
# GỘP VÀO CẤU TRÚC APP
# ============================================================
VAN = {
    "Lớp 7": {
        "Chương 1: Bầu trời tuổi thơ": {
            "Văn bản 1: Bồng chanh đỏ (Đỗ Chu)": bai(
                ly_thuyet=BCD_LY_THUYET,
                vi_du=BCD_VI_DU,
                cau_hoi=BCD_CAU_HOI,
                bt_co_ban=BCD_BT_CO_BAN,
                bt_nang_cao=BCD_BT_NANG_CAO,
            ),
        }
    }
}


# ============================================================
# KIỂM TRA DỮ LIỆU
# ============================================================
def kiem_tra_van():
    loi = []
    for chuong, bais in VAN["Lớp 7"].items():
        for ten_bai, d in bais.items():
            for i, c in enumerate(d["cau_hoi"], 1):
                if not (0 <= c["d"] < len(c["da"])):
                    loi.append(f"{ten_bai} / câu {i}: chỉ số đáp án sai")
                if len(set(c["da"])) != len(c["da"]):
                    loi.append(f"{ten_bai} / câu {i}: đáp án trùng nhau")
            for i, b in enumerate(d["bt_co_ban"], 1):
                if not b["dd"]:
                    loi.append(f"{ten_bai} / bài cơ bản {i}: thiếu đáp án")
            for i, b in enumerate(d["bt_nang_cao"], 1):
                if not b["dd"]:
                    loi.append(f"{ten_bai} / bài nâng cao {i}: thiếu đáp án")
    return loi


if __name__ == "__main__":
    tong_cau = sum(len(b["cau_hoi"]) for c in VAN["Lớp 7"].values() for b in c.values())
    tong_cb = sum(len(b["bt_co_ban"]) for c in VAN["Lớp 7"].values() for b in c.values())
    tong_nc = sum(len(b["bt_nang_cao"]) for c in VAN["Lớp 7"].values() for b in c.values())
    print("Số chương:", len(VAN["Lớp 7"]))
    print("Số câu trắc nghiệm:", tong_cau)
    print("Số bài tập cơ bản:", tong_cb)
    print("Số bài tập nâng cao:", tong_nc)
    ds_loi = kiem_tra_van()
    print("Lỗi dữ liệu:", "không có" if not ds_loi else ds_loi)
