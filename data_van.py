# -*- coding: utf-8 -*-
"""
NGÂN HÀNG DỮ LIỆU NGỮ VĂN 7 - KẾT NỐI TRI THỨC
Cấu trúc theo mục lục sách Tập Một và Tập Hai (10 bài, 41 văn bản).
Văn bản đã có nội dung: "Bầy chim chìa vôi". Các văn bản còn lại đang chờ biên soạn.
"""

def _khung(tac_gia, the_loai):
    return {
        "ly_thuyet": f"Thể loại: {the_loai}. Tác giả: {tac_gia}. Nội dung đang được biên soạn.",
        "vi_du": "",
        "cau_hoi": [],
        "bt_co_ban": [],
        "bt_nang_cao": [],
    }

NOI_DUNG = {'Bầy chim chìa vôi': {'ly_thuyet': '📌 TRI THỨC NGỮ VĂN\n'
                                    '1. Đề tài và chi tiết\n'
                                    '- Đề tài là phạm vi đời sống được thể hiện trong tác phẩm văn học. Đề '
                                    'tài có thể dựa vào loại sự kiện được miêu tả, không gian được tái hiện, '
                                    'loại nhân vật được đặt ở vị trí trung tâm.\n'
                                    '- Chi tiết là yếu tố nhỏ nhất tạo nên thế giới hình tượng, có tầm quan '
                                    'trọng trong việc đem lại sự sinh động, lôi cuốn cho tác phẩm.\n'
                                    '\n'
                                    '2. Tính cách nhân vật\n'
                                    '- Tính cách là những đặc điểm riêng tương đối ổn định của nhân vật, '
                                    'được bộc lộ qua mọi hành động, cách ứng xử, cảm xúc, suy nghĩ.\n'
                                    '- Tính cách còn được thể hiện qua các mối quan hệ, qua lời kể và suy '
                                    'nghĩ của nhân vật khác.\n'
                                    '\n'
                                    '📌 TÓM TẮT VĂN BẢN\n'
                                    '- Văn bản tóm tắt là dạng rút gọn của văn bản gốc, dung lượng nhỏ nhưng '
                                    'vẫn phản ánh trung thành nội dung cơ bản.\n'
                                    '\n'
                                    '📌 VĂN BẢN "BẦY CHIM CHÌA VÔI"\n'
                                    '- Đề tài: tuổi thơ gắn với thiên nhiên làng quê ven sông, tình anh em '
                                    'và tình yêu thương loài vật.\n'
                                    '- Ngôi kể: ngôi thứ ba, người kể giấu mặt, có lúc đi vào suy nghĩ của '
                                    'nhân vật.\n'
                                    '- Nhân vật: hai anh em Mên (anh) và Mon (em). Cả hai hồn nhiên, nhạy '
                                    'cảm, giàu tình thương với những sinh linh nhỏ bé.\n'
                                    '- Tình huống: đêm mưa, nước sông dâng cao, bãi cát giữa sông — nơi bầy '
                                    'chim chìa vôi làm tổ — có nguy cơ bị ngập. Hai anh em lo lắng và tìm '
                                    'cách cứu chim non.\n'
                                    '- Ý nghĩa: ngợi ca tâm hồn trong sáng, lòng nhân hậu của trẻ thơ; cho '
                                    'thấy vẻ đẹp của thiên nhiên và quy luật sinh tồn của muôn loài.\n'
                                    '\n'
                                    '📌 MỞ RỘNG THÀNH PHẦN CHÍNH BẰNG CỤM TỪ\n'
                                    '- Thành phần chính và trạng ngữ của câu có thể được mở rộng bằng cụm từ '
                                    '(cụm danh từ, cụm động từ, cụm tính từ) để cung cấp thêm thông tin cho '
                                    'người đọc.\n'
                                    '- Ví dụ: "Bầy chim" → "Bầy chim chìa vôi non" (cụm danh từ mở rộng bằng '
                                    'định ngữ).\n',
                       'vi_du': '💡 VÍ DỤ 1: Đề tài và chi tiết\n'
                                'Chi tiết "bãi cát giữa sông bị nước ngập dần" làm nổi bật nỗi lo của hai '
                                'anh em. Chi tiết nhỏ này góp phần tạo nên không khí căng thẳng của đêm '
                                'mưa.\n'
                                '\n'
                                '💡 VÍ DỤ 2: Tính cách qua lời nói\n'
                                'Mon hỏi: "Em sợ những con chim chìa vôi non bị chết đuối mất." Câu nói cho '
                                'thấy Mon hồn nhiên, nhạy cảm và giàu lòng thương loài vật.\n'
                                '\n'
                                '💡 VÍ DỤ 3: Mở rộng thành phần chính\n'
                                'Câu gốc: "Chim non bay lên." Câu mở rộng: "Những con chim chìa vôi non lần '
                                'đầu tiên trong đời đập cánh bay lên." Cụm từ mở rộng cung cấp thêm thông '
                                'tin về đối tượng và thời điểm.\n',
                       'cau_hoi': [{'nd': 'Đề tài của truyện "Bầy chim chìa vôi" là gì?',
                                    'da': ['Tuổi thơ gắn với thiên nhiên làng quê ven sông',
                                           'Chiến tranh và người lính',
                                           'Đời sống thành thị hiện đại',
                                           'Lịch sử đấu tranh giai cấp'],
                                    'd': 0,
                                    'gt': 'Truyện kể về đêm mưa, nước sông dâng và hai anh em cứu bầy chim '
                                          'non ở bãi cát ven sông.'},
                                   {'nd': 'Truyện "Bầy chim chìa vôi" được kể theo ngôi thứ mấy?',
                                    'da': ['Ngôi thứ ba',
                                           'Ngôi thứ nhất',
                                           'Ngôi thứ hai',
                                           'Kết hợp ngôi thứ nhất và thứ hai'],
                                    'd': 0,
                                    'gt': 'Người kể chuyện giấu mặt, không xuất hiện như một nhân vật trong '
                                          'truyện.'},
                                   {'nd': 'Hai nhân vật chính trong truyện là ai?',
                                    'da': ['Mên và Mon', 'An và Cò', 'Hoài và Hiên', 'Dế Mèn và Dế Choắt'],
                                    'd': 0,
                                    'gt': 'Mên là anh, Mon là em; hai anh em cùng lo lắng cho bầy chim non.'},
                                   {'nd': 'Trong truyện, Mon là gì của Mên?',
                                    'da': ['Em trai', 'Anh trai', 'Bạn cùng lớp', 'Hàng xóm'],
                                    'd': 0,
                                    'gt': 'Mon gọi Mên là "anh" và Mên gọi Mon là em.'},
                                   {'nd': 'Câu chuyện diễn ra vào thời điểm nào?',
                                    'da': ['Đêm khuya, khi mưa to và nước sông dâng',
                                           'Buổi trưa nắng gắt',
                                           'Buổi chiều hè êm ả',
                                           'Ngày Tết đoàn viên'],
                                    'd': 0,
                                    'gt': 'Truyện mở đầu lúc khoảng hai giờ sáng, trời mưa và nước sông lên '
                                          'nhanh.'},
                                   {'nd': 'Khi nói về "Bầy chim chìa vôi", câu nào sau đây đúng nhất?',
                                    'da': ['Truyện thể hiện tình yêu thương loài vật của trẻ thơ',
                                           'Truyện nói về nỗi sợ hãi thiên nhiên',
                                           'Truyện tố cáo nạn săn bắt',
                                           'Truyện kể về chuyến đi xa'],
                                    'd': 0,
                                    'gt': 'Ý nghĩa chính của truyện là ngợi ca tâm hồn nhân hậu của trẻ thơ '
                                          'đối với sinh linh bé nhỏ.'},
                                   {'nd': 'Phương thức biểu đạt chính của văn bản là gì?',
                                    'da': ['Tự sự', 'Nghị luận', 'Thuyết minh', 'Biểu cảm'],
                                    'd': 0,
                                    'gt': 'Văn bản kể chuyện có nhân vật, sự việc, diễn biến rõ ràng.'},
                                   {'nd': 'Chim chìa vôi thường làm tổ ở đâu theo truyện?',
                                    'da': ['Trên bãi cát giữa sông',
                                           'Trên cành cây cao',
                                           'Trong hốc đá',
                                           'Trên mái nhà'],
                                    'd': 0,
                                    'gt': 'Các con chim chìa vôi làm tổ trên bãi cát giữa sông, nơi có đám '
                                          'rong khô để đẻ trứng.'},
                                   {'nd': 'Điều gì khiến hai anh em lo lắng giữa đêm?',
                                    'da': ['Nước sông dâng, bãi cát sắp ngập, chim non có thể chết đuối',
                                           'Trời sắp sáng mà chưa làm xong việc nhà',
                                           'Con đò bị cuốn trôi',
                                           'Bố mẹ đi vắng chưa về'],
                                    'd': 0,
                                    'gt': 'Mon nói: "Em sợ những con chim chìa vôi non bị chết đuối mất."'},
                                   {'nd': 'Hai anh em nằm ở đâu khi trò chuyện giữa đêm mưa?',
                                    'da': ['Trong chiếc chăn dạ đã rách nhiều chỗ',
                                           'Trên chiếc giường gỗ mới',
                                           'Ngoài sân dưới gốc cây',
                                           'Trên bến đò'],
                                    'd': 0,
                                    'gt': 'Hai đứa bé nằm trong chiếc chăn dạ rách nhiều chỗ, thì thầm nói '
                                          'chuyện.'},
                                   {'nd': 'Chim chìa vôi trong truyện được miêu tả là loài chim như thế nào?',
                                    'da': ['Nhỏ như chim sẻ, lông đen, đuôi và cánh có vệt trắng',
                                           'To như con gà, lông đỏ',
                                           'Có mỏ dài, lông xanh biếc',
                                           'Biết bơi lội như vịt trời'],
                                    'd': 0,
                                    'gt': 'Chú thích trong sách: chìa vôi là loài chim nhỏ như chim sẻ, lông '
                                          'đen, đuôi và cánh có vệt trắng.'},
                                   {'nd': '"Chùm" trong câu "đi kéo chùm" là gì?',
                                    'da': ['Một loại lưới vó dùng để bắt cá, tôm',
                                           'Một loại thuyền nhỏ',
                                           'Một loại cây bờ sông',
                                           'Một loại đèn thắp trên đò'],
                                    'd': 0,
                                    'gt': 'Chú thích: chùm là một loại lưới vó, thường thả ven sông, hồ, '
                                          'dùng để bắt cá, tôm.'},
                                   {'nd': 'Theo lời kể, mùa mưa năm đó như thế nào?',
                                    'da': ['Về sớm hơn mọi năm',
                                           'Kéo dài đến tận mùa hè',
                                           'Không có mưa',
                                           'Mưa rất ít và nắng nhiều'],
                                    'd': 0,
                                    'gt': 'Truyện viết: "Mùa mưa năm nay như về sớm hơn."'},
                                   {'nd': 'Khi nước dâng, mẹ con chim chìa vôi đã làm gì?',
                                    'da': ['Dẫn bầy chim non tránh nước lên cao theo từng bước',
                                           'Bay đi xa, bỏ mặc bầy con',
                                           'Đứng im không làm gì',
                                           'Chui xuống nước tìm thức ăn'],
                                    'd': 0,
                                    'gt': 'Chim bố, chim mẹ dẫn bầy chim non tránh nước, tiến dần đến phần '
                                          'cao nhất của dải cát.'},
                                   {'nd': 'Theo lời bố kể, khi nào chim non mới bay lên?',
                                    'da': ['Khi nước vừa ngập hết bãi cát',
                                           'Khi trời vừa sáng',
                                           'Khi mưa vừa tạnh',
                                           'Khi có người đến gần'],
                                    'd': 0,
                                    'gt': 'Mên kể lại lời bố: "khi nước vừa ngập hết thì chim mới bay lên."'},
                                   {'nd': 'Những con chim non bay lên lần đầu tiên trong đời có hành động '
                                          'gì?',
                                    'da': ['Đập cánh bay lên khỏi dòng nước',
                                           'Lặn xuống đáy sông',
                                           'Nằm yên trên bãi cát',
                                           'Chạy trên mặt nước'],
                                    'd': 0,
                                    'gt': 'Chim non "đập cánh bay lên" lần đầu tiên, bay vào bờ.'},
                                   {'nd': 'Khi nói về sự nguy hiểm của việc cất cánh, truyện viết điều gì?',
                                    'da': ['Nếu cất cánh sớm, chim sẽ rơi xuống dòng nước; cất cánh chậm, '
                                           'chim sẽ bị nước cuốn đi',
                                           'Chim sẽ bị bắt nếu bay lên sớm',
                                           'Chim không bao giờ bị nguy hiểm',
                                           'Chim chỉ bị đau khi cất cánh'],
                                    'd': 0,
                                    'gt': 'Đoạn văn nêu rõ: cất cánh sớm thì rơi xuống nước, cất cánh chậm '
                                          'một giây thôi thì bị dòng nước cuốn chìm.'},
                                   {'nd': 'Câu "một cảnh tượng như huyền thoại hiện ra" sử dụng biện pháp '
                                          'nghệ thuật nào?',
                                    'da': ['So sánh', 'Nhân hóa', 'Ẩn dụ', 'Điệp ngữ'],
                                    'd': 0,
                                    'gt': 'Cảnh tượng được so sánh với huyền thoại để gợi vẻ kì diệu, đẹp '
                                          'đẽ.'},
                                   {'nd': 'Cụm từ "nhảy lò cò" trong truyện gợi tả điều gì?',
                                    'da': ['Chim non nhảy trên đôi chân mảnh dẻ, còn yếu ớt',
                                           'Chim non đang múa vui',
                                           'Chim non đang ngủ say',
                                           'Chim non đang bị thương'],
                                    'd': 0,
                                    'gt': 'Chim non nhảy lò cò trên đôi chân mảnh dẻ, chưa cứng cáp, đập '
                                          'cánh suốt đêm.'},
                                   {'nd': 'Cảnh bình minh hiện ra trước mắt hai đứa trẻ như thế nào?',
                                    'da': ['Dòng nước khổng lồ nuốt chửng phần cuối của dải cát',
                                           'Mặt trời mọc đỏ rực trên đồi',
                                           'Nước sông trong vắt, lặng sóng',
                                           'Những con thuyền ra khơi đông đúc'],
                                    'd': 0,
                                    'gt': 'Khi bình minh sáng dần, dòng nước khổng lồ nuốt chửng phần còn '
                                          'lại cuối cùng của dải cát.'},
                                   {'nd': 'Những tiếng sấm sau mỗi đêm di chuyển theo hướng nào?',
                                    'da': ['Từ chân trời xa về phía bên kia sông',
                                           'Từ bên kia sông về chân trời',
                                           'Từ trên trời rơi xuống',
                                           'Đứng yên một chỗ'],
                                    'd': 0,
                                    'gt': 'Truyện viết: "Những tiếng sấm sau mỗi đêm lại chuyển dần từ một '
                                          'chân trời xa về bên kia sông."'},
                                   {'nd': 'Con sông được nhắc đến trong truyện có tên là gì?',
                                    'da': ['Sông Đáy', 'Sông Hồng', 'Sông Cửu Long', 'Sông Thương'],
                                    'd': 0,
                                    'gt': 'Truyện viết: "Con sông Đáy cựa mình lớn lên."'},
                                   {'nd': 'Chim chìa vôi làm tổ ở khúc sông nào?',
                                    'da': ['Khúc sông làng chúng',
                                           'Khúc sông lớn cuối nguồn',
                                           'Khúc sông gần biển',
                                           'Khúc sông thành phố'],
                                    'd': 0,
                                    'gt': 'Truyện viết: "Chỉ ở khúc sông làng chúng, những con chim chìa vôi '
                                          'mới làm tổ như thế."'},
                                   {'nd': 'Vì sao hai anh em nằm yên không ngủ được?',
                                    'da': ['Vì lo cho bầy chim non khi nước sông dâng cao',
                                           'Vì sợ tiếng sấm',
                                           'Vì đói bụng',
                                           'Vì đang chơi trò chơi'],
                                    'd': 0,
                                    'gt': 'Hai anh em thì thầm, lo lắng cho tổ chim trên bãi cát giữa sông.'},
                                   {'nd': 'Mên thể hiện tính cách nào qua lời nói "Bảo cái gì mà bảo lắm '
                                          'thế"?',
                                    'da': ['Nóng nảy, thẳng thắn',
                                           'Nhút nhát, rụt rè',
                                           'Lười biếng, thờ ơ',
                                           'Hiền lành, nhẫn nhịn'],
                                    'd': 0,
                                    'gt': 'Lời nói ngắn, dứt khoát, cho thấy Mên có phần nóng nảy.'},
                                   {'nd': 'Lời nói "Đợi em với. Không em chơi với anh nữa" của Mon thể hiện '
                                          'điều gì?',
                                    'da': ['Tình anh em gắn bó, hồn nhiên và quấn quýt',
                                           'Sự giận dỗi của người lớn',
                                           'Sự xa cách giữa hai anh em',
                                           'Sự ích kỉ của trẻ con'],
                                    'd': 0,
                                    'gt': 'Câu nói kết thúc cho thấy tình cảm trong sáng và sự gắn bó của '
                                          'Mon với anh.'},
                                   {'nd': 'Khi nhìn bầy chim non bay lên, hai anh em có cảm xúc gì?',
                                    'da': ['Xúc động, rơi nước mắt',
                                           'Tức giận, muốn bắt chim',
                                           'Thờ ơ, không quan tâm',
                                           'Sợ hãi, bỏ chạy'],
                                    'd': 0,
                                    'gt': 'Hai đứa bé nhận ra chúng đã khóc từ lúc nào.'},
                                   {'nd': 'Cuối truyện, hai anh em làm gì?',
                                    'da': ['Cùng quay người và chạy về phía ngôi nhà',
                                           'Ở lại bãi cát đến sáng',
                                           'Lội xuống sông bắt cá',
                                           'Đi tìm bố mẹ'],
                                    'd': 0,
                                    'gt': 'Hai đứa bé rướn mình chạy về phía ngôi nhà của chúng.'},
                                   {'nd': 'Để cứu tổ chim, hai anh em đã làm việc gì?',
                                    'da': ['Dùng đò ra bãi cát, cố kéo đò về bến để đưa chim vào bờ',
                                           'Gọi cả làng đến cứu',
                                           'Dựng lều tránh mưa trên bờ',
                                           'Đuổi hết chim đi nơi khác'],
                                    'd': 0,
                                    'gt': 'Hai anh em lấy đò của ông Hảo, kéo đò ra và tìm cách mang chim '
                                          'non vào bờ.'},
                                   {'nd': 'Ai là người nói "Tổ chim ngập mất anh ạ. Mình phải mang chúng nó '
                                          'vào bờ"?',
                                    'da': ['Mon', 'Mên', 'Bố của hai anh em', 'Ông Hảo'],
                                    'd': 0,
                                    'gt': 'Đây là lời nói của Mon trong cuộc trò chuyện với anh.'},
                                   {'nd': 'Thông điệp nổi bật mà truyện gửi gắm là gì?',
                                    'da': ['Yêu thương và trân trọng sự sống của muôn loài',
                                           'Thiên nhiên luôn đáng sợ',
                                           'Trẻ em không nên đi chơi sông',
                                           'Chỉ con người mới có quyền sống'],
                                    'd': 0,
                                    'gt': 'Hai anh em lo lắng và hành động để cứu bầy chim non, thể hiện '
                                          'tình thương với sinh linh bé nhỏ.'},
                                   {'nd': 'Ai là tác giả của văn bản "Bầy chim chìa vôi"?',
                                    'da': ['Nguyễn Quang Thiều', 'Đoàn Giỏi', 'Võ Quảng', 'Thanh Hải'],
                                    'd': 0,
                                    'gt': 'Nguyễn Quang Thiều sinh năm 1957 tại Hà Nội, là tác giả của nhiều '
                                          'truyện viết cho thiếu nhi.'},
                                   {'nd': 'Truyện "Bầy chim chìa vôi" được trích từ tập sách nào?',
                                    'da': ['Mùa hoa cải bên sông',
                                           'Đất rừng phương Nam',
                                           'Chuyện mùa hạ',
                                           'Bí mật hồ cá thần'],
                                    'd': 0,
                                    'gt': 'Chú thích trong sách: Nguyễn Quang Thiều, Mùa hoa cải bên sông, '
                                          'NXB Hội Nhà văn, 2012.'}],
                       'bt_co_ban': [{'de': 'Bài 1: Tóm tắt văn bản "Bầy chim chìa vôi" trong khoảng 5 câu.',
                                      'dd': ['Đêm mưa, nước sông dâng cao, hai anh em Mên và Mon lo cho bầy '
                                             'chim non ở bãi cát. Hai anh em đi đò ra bãi cát để cứu chim. '
                                             'Khi nước ngập hết, chim non lần đầu tiên bay lên. Hai anh em '
                                             'xúc động và chạy về nhà.'],
                                      'lg': 'Tóm tắt cần nêu đủ sự việc chính theo trình tự, không đưa ý '
                                            'kiến cá nhân.'},
                                     {'de': 'Bài 2: Xác định đề tài và ngôi kể của truyện.',
                                      'dd': ['Đề tài: tuổi thơ và thiên nhiên làng quê ven sông. Ngôi kể: '
                                             'ngôi thứ ba.'],
                                      'lg': 'Đề tài dựa vào loại sự kiện và không gian được miêu tả; ngôi kể '
                                            'dựa vào người kể có xuất hiện trong truyện hay không.'},
                                     {'de': 'Bài 3: Tìm những chi tiết cho thấy hai anh em lo lắng cho bầy '
                                            'chim non.',
                                      'dd': ['Hai anh em nằm thì thầm nói chuyện giữa đêm; Mon nói sợ chim '
                                             'non bị chết đuối; hai anh em đi đò ra bãi cát để cứu tổ chim.'],
                                      'lg': 'Chú ý lời đối thoại và hành động của nhân vật.'},
                                     {'de': 'Bài 4: Chỉ ra từ ngữ, hình ảnh miêu tả tiếng mưa và nước sông '
                                            'dâng trong đoạn văn.',
                                      'dd': ['Tiếng mưa "hình như có tiếng nước sông dâng cao, xiết xích '
                                             'chảy"; "mưa đổ xuống mái nhà"; "nước sông dâng lên rất '
                                             'nhanh".'],
                                      'lg': 'Nhận biết các chi tiết tạo không khí căng thẳng của đêm mưa.'},
                                     {'de': 'Bài 5: Tìm cụm từ mở rộng thành phần chính trong câu "Những con '
                                            'chim chìa vôi non lần đầu tiên trong đời đập cánh bay lên."',
                                      'dd': ['Cụm danh từ: "Những con chim chìa vôi non"; cụm động từ: "đập '
                                             'cánh bay lên".'],
                                      'lg': 'Cụm danh từ có định ngữ (những, chìa vôi, non) bổ sung thông '
                                            'tin cho danh từ trung tâm "chim".'},
                                     {'de': 'Bài 6: Nêu cảm xúc của Mên và Mon khi nhìn chim non bay lên.',
                                      'dd': ['Hai anh em xúc động đến rơi nước mắt, không nhận ra mình đã '
                                             'khóc từ lúc nào.'],
                                      'lg': 'Chú ý những chi tiết miêu tả nét mặt, nước mắt và hành động '
                                            'quay về nhà.'},
                                     {'de': 'Bài 7: Vì sao chim non phải cất cánh đúng lúc? Hãy chỉ ra một '
                                            'chi tiết trong truyện.',
                                      'dd': ['Cất cánh sớm thì rơi xuống nước, cất cánh chậm thì bị nước '
                                             'cuốn chìm; chi tiết: "nếu chúng cất cánh chậm một giây thôi, '
                                             'chúng sẽ bị dòng nước cuốn chìm".'],
                                      'lg': 'Đây là chi tiết thể hiện quy luật sinh tồn của tự nhiên.'}],
                       'bt_nang_cao': [{'de': 'Bài tập 1: Phân tích cảm xúc của hai anh em Mên và Mon khi '
                                              'chứng kiến chim non bay lên (viết một đoạn văn khoảng 8 đến '
                                              '10 câu).',
                                        'hd': 'Dựa vào các chi tiết: hai anh em nhìn chim bay, không kêu '
                                              'được tiếng nào, khóc, rồi chạy về nhà.',
                                        'dd': ['Đoạn văn nêu được sự xúc động, bất ngờ và tình thương của '
                                               'hai anh em; có dẫn chứng từ văn bản.'],
                                        'lg': 'Cảm xúc được thể hiện qua những chi tiết tự nhiên, không gọi '
                                              'tên cảm xúc một cách khô khan.',
                                        'kieu': 'tu_luan'},
                                       {'de': 'Bài tập 2: Viết đoạn văn ghi lại cảm xúc của em sau khi đọc '
                                              'truyện (khoảng 7 đến 10 câu).',
                                        'hd': 'Có thể nói về sự yêu thương loài vật, tình anh em, hoặc vẻ '
                                              'đẹp của thiên nhiên làng quê.',
                                        'dd': ['Đoạn văn có cảm xúc chân thật, nêu được một ấn tượng cụ thể '
                                               'và dẫn chứng từ văn bản.'],
                                        'lg': 'Đây là dạng viết ghi lại cảm xúc, nên cần chân thực và có chi '
                                              'tiết riêng.',
                                        'kieu': 'tu_luan'},
                                       {'de': 'Bài tập 3: Đóng vai Mon, kể lại đoạn hai anh em đi đò ra bãi '
                                              'cát (ngôi thứ nhất, khoảng 10 câu).',
                                        'hd': 'Chuyển sang ngôi kể thứ nhất; giữ đúng tính cách hồn nhiên, '
                                              'lo lắng của Mon.',
                                        'dd': ['Đoạn kể đúng sự việc, dùng ngôi thứ nhất, thể hiện được tâm '
                                               'trạng của Mon.'],
                                        'lg': 'Khi chuyển ngôi kể, cần suy nghĩ lại cách nhìn sự việc từ góc '
                                              'độ nhân vật.',
                                        'kieu': 'tu_luan'},
                                       {'de': 'Bài tập 4: Theo em, vì sao truyện lấy tên là "Bầy chim chìa '
                                              'vôi" mà không phải là "Hai anh em"? Trình bày ý kiến trong '
                                              'khoảng 150 chữ.',
                                        'hd': 'Suy nghĩ về vai trò của hình ảnh bầy chim trong toàn bộ câu '
                                              'chuyện.',
                                        'dd': ['Bài viết nêu được ý kiến riêng, lập luận dựa trên vai trò '
                                               'của bầy chim trong cốt truyện và chủ đề.'],
                                        'lg': 'Không có một đáp án duy nhất; quan trọng là lập luận rõ ràng '
                                              'và có căn cứ từ văn bản.',
                                        'kieu': 'tu_luan'}]}}


VAN = {
    "Lớp 7": {
        'Bài 1: Bầu trời tuổi thơ': {
            'Bầy chim chìa vôi': NOI_DUNG.get('Bầy chim chìa vôi') or _khung('Nguyễn Quang Thiều', 'Truyện'),
            'Đi lấy mật (trích Đất rừng phương Nam)': NOI_DUNG.get('Đi lấy mật (trích Đất rừng phương Nam)') or _khung('Đoàn Giỏi', 'Truyện'),
            'Ngàn sao làm việc': NOI_DUNG.get('Ngàn sao làm việc') or _khung('Võ Quảng', 'Thơ'),
            'Ngôi nhà trên cây (trích Tốt-tô-chan bên cửa sổ)': NOI_DUNG.get('Ngôi nhà trên cây (trích Tốt-tô-chan bên cửa sổ)') or _khung('Cu-rô-ya-na-gi Tê-sư-cô', 'Truyện (đọc mở rộng)'),
        },
        'Bài 2: Khúc nhạc tâm hồn': {
            'Đồng dao mùa xuân': NOI_DUNG.get('Đồng dao mùa xuân') or _khung('Nguyễn Khoa Điềm', 'Thơ bốn chữ'),
            'Gặp lá cơm nếp': NOI_DUNG.get('Gặp lá cơm nếp') or _khung('Thanh Thảo', 'Thơ năm chữ'),
            'Trở gió': NOI_DUNG.get('Trở gió') or _khung('Nguyễn Ngọc Tư', 'Tùy bút'),
            'Chiều sông Thương': NOI_DUNG.get('Chiều sông Thương') or _khung('Hữu Thỉnh', 'Thơ (thực hành đọc)'),
        },
        'Bài 3: Cội nguồn yêu thương': {
            'Vừa nhắm mắt vừa mở cửa sổ (trích)': NOI_DUNG.get('Vừa nhắm mắt vừa mở cửa sổ (trích)') or _khung('Nguyễn Ngọc Thuần', 'Truyện'),
            'Người thầy đầu tiên (trích)': NOI_DUNG.get('Người thầy đầu tiên (trích)') or _khung('Trin-ghi-dơ Ai-tơ-ma-tốp', 'Truyện'),
            'Quê hương': NOI_DUNG.get('Quê hương') or _khung('Tế Hanh', 'Thơ'),
            'Trong lòng mẹ (trích Những ngày thơ ấu)': NOI_DUNG.get('Trong lòng mẹ (trích Những ngày thơ ấu)') or _khung('Nguyên Hồng', 'Truyện (thực hành đọc)'),
        },
        'Bài 4: Giai điệu đất nước': {
            'Mùa xuân nho nhỏ': NOI_DUNG.get('Mùa xuân nho nhỏ') or _khung('Thanh Hải', 'Thơ'),
            'Gò Me (trích)': NOI_DUNG.get('Gò Me (trích)') or _khung('Hoàng Tố Nguyên', 'Truyện'),
            'Bài thơ "Đường núi" của Nguyễn Đình Thi': NOI_DUNG.get('Bài thơ "Đường núi" của Nguyễn Đình Thi') or _khung('Vũ Quần Phương', 'Văn bản nghị luận (bình thơ)'),
            'Chiều biên giới': NOI_DUNG.get('Chiều biên giới') or _khung('Lò Ngân Sủn', 'Thơ (thực hành đọc)'),
        },
        'Bài 5: Màu sắc trăm miền': {
            'Tháng Giêng, mơ về trăng non rét ngọt (trích)': NOI_DUNG.get('Tháng Giêng, mơ về trăng non rét ngọt (trích)') or _khung('Vũ Bằng', 'Tùy bút'),
            'Chuyện cơm hến': NOI_DUNG.get('Chuyện cơm hến') or _khung('Hoàng Phủ Ngọc Tường', 'Tản văn'),
            'Hội lồng tồng': NOI_DUNG.get('Hội lồng tồng') or _khung('Trần Quốc Vượng – Lê Văn Hảo – Dương Tất Từ', 'Văn bản thông tin'),
            'Những khuôn của dấu yêu': NOI_DUNG.get('Những khuôn của dấu yêu') or _khung('Trương Anh Ngọc', 'Văn bản thông tin (thực hành đọc)'),
        },
        'Bài 6: Bài học cuộc sống': {
            'Đẽo cày giữa đường': NOI_DUNG.get('Đẽo cày giữa đường') or _khung('Ngụ ngôn Việt Nam', 'Truyện ngụ ngôn'),
            'Ếch ngồi đáy giếng': NOI_DUNG.get('Ếch ngồi đáy giếng') or _khung('Trang Tử', 'Truyện ngụ ngôn'),
            'Con mối và con kiến': NOI_DUNG.get('Con mối và con kiến') or _khung('Nam Hương', 'Truyện ngụ ngôn'),
            'Một số câu tục ngữ Việt Nam': NOI_DUNG.get('Một số câu tục ngữ Việt Nam') or _khung('Tục ngữ', 'Tục ngữ'),
            'Con hổ có nghĩa': NOI_DUNG.get('Con hổ có nghĩa') or _khung('Vũ Trinh', 'Truyện ngụ ngôn'),
            'Thiên nga, cá măng và tôm hùm (thực hành đọc)': NOI_DUNG.get('Thiên nga, cá măng và tôm hùm (thực hành đọc)') or _khung('I-van Crư-lốp', 'Truyện ngụ ngôn'),
        },
        'Bài 7: Thế giới viễn tưởng': {
            'Cuộc chạm trán trên đại dương (trích Hai vạn dặm dưới biển)': NOI_DUNG.get('Cuộc chạm trán trên đại dương (trích Hai vạn dặm dưới biển)') or _khung('Giuyn Véc-nơ', 'Truyện khoa học viễn tưởng'),
            'Đường vào trung tâm vũ trụ (trích Thiên Mã)': NOI_DUNG.get('Đường vào trung tâm vũ trụ (trích Thiên Mã)') or _khung('Hà Thuỷ Nguyên', 'Truyện khoa học viễn tưởng'),
            'Dấu ấn Hồ Khanh': NOI_DUNG.get('Dấu ấn Hồ Khanh') or _khung('Nhật Văn', 'Truyện khoa học viễn tưởng'),
            'Chiếc đũa thần (trích Tinh vân Tiên Nữ)': NOI_DUNG.get('Chiếc đũa thần (trích Tinh vân Tiên Nữ)') or _khung('I. A. E-phơ-rê-mốp', 'Truyện khoa học viễn tưởng (thực hành đọc)'),
        },
        'Bài 8: Trải nghiệm để trưởng thành': {
            'Bản đồ dẫn đường': NOI_DUNG.get('Bản đồ dẫn đường') or _khung('Đa-ni-en Gốt-li-ép', 'Văn bản nghị luận'),
            'Hãy cầm lấy và đọc': NOI_DUNG.get('Hãy cầm lấy và đọc') or _khung('Huỳnh Như Phương', 'Văn bản nghị luận'),
            'Nói với con': NOI_DUNG.get('Nói với con') or _khung('Y Phương', 'Thơ'),
            'Câu chuyện về con đường': NOI_DUNG.get('Câu chuyện về con đường') or _khung('Đoàn Công Lê Huy', 'Văn bản nghị luận (thực hành đọc)'),
        },
        'Bài 9: Hòa điệu với tự nhiên': {
            'Thuỷ tiên tháng Một': NOI_DUNG.get('Thuỷ tiên tháng Một') or _khung('Thô-mát L. Phrít-man', 'Văn bản thông tin'),
            'Lễ rửa làng của người Lô Lô': NOI_DUNG.get('Lễ rửa làng của người Lô Lô') or _khung('Phạm Thuỳ Dung', 'Văn bản thông tin'),
            'Bản tin về hoa anh đào': NOI_DUNG.get('Bản tin về hoa anh đào') or _khung('Nguyễn Vĩnh Nguyên', 'Bản tin'),
            '"Thân thiện với môi trường"': NOI_DUNG.get('"Thân thiện với môi trường"') or _khung('Nguyễn Hữu Quỳnh Hương', 'Văn bản thông tin (thực hành đọc)'),
        },
        'Bài 10: Trang sách và cuộc sống': {
            'Thách thức đầu tiên': NOI_DUNG.get('Thách thức đầu tiên') or _khung('Chưa xác nhận tác giả', 'Đọc (cần đối chiếu sách)'),
            'Chinh phục những cuốn sách mới': NOI_DUNG.get('Chinh phục những cuốn sách mới') or _khung('Chưa xác nhận tác giả', 'Đọc (cần đối chiếu sách)'),
            'Thách thức thứ hai': NOI_DUNG.get('Thách thức thứ hai') or _khung('Chưa xác nhận tác giả', 'Viết (cần đối chiếu sách)'),
        },
    }
}

def kiem_tra_van():
    loi = []
    for bai, vbs in VAN["Lớp 7"].items():
        for ten, d in vbs.items():
            for i, c in enumerate(d["cau_hoi"], 1):
                if not (0 <= c["d"] < len(c["da"])) or len(set(c["da"])) != len(c["da"]):
                    loi.append(f"{ten} / câu {i}")
    return loi

if __name__ == "__main__":
    so_vb = sum(len(b) for b in VAN["Lớp 7"].values())
    co_noi_dung = sum(1 for b in VAN["Lớp 7"].values() for v in b.values() if v["cau_hoi"])
    print("Số bài:", len(VAN["Lớp 7"]), "| Số văn bản:", so_vb, "| Văn bản đã có câu hỏi:", co_noi_dung)
    print("Lỗi:", kiem_tra_van() or "không có")
