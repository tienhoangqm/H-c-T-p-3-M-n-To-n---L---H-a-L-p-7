# -*- coding: utf-8 -*-
"""
DỮ LIỆU MÔN TIẾNG ANH LỚP 7 — Bộ Kết nối tri thức (Global Success)
- KIEN_THUC_NEN: ngân hàng kiến thức lớp 4-6, tự động xen vào đề (30%)
- ANH: dữ liệu 12 Unit (từ vựng + ngữ pháp + trắc nghiệm + bài tập)
- TU_DIEN_OFFLINE: từ điển Anh-Việt tra tức thì (không cần mạng)
- DS_TU_CUA_NGAY: từ của ngày
"""

# ============================================================
# 1. NGÂN HÀNG KIẾN THỨC NỀN (LỚP 4–6) — gọi qua trường "on_tap"
# ============================================================
KIEN_THUC_NEN = {
    "to_be": {
        "ten": "Động từ To Be (am/is/are) — ôn lớp 4",
        "ly_thuyet": "I am; You/We/They are; He/She/It is. Phủ định: am not / isn't / aren't.",
        "cau_hoi": [
            {"nd": "She ___ my best friend.", "da": ["am", "is", "are", "be"], "d": 1},
            {"nd": "They ___ from Da Nang.", "da": ["is", "am", "are", "be"], "d": 2},
            {"nd": "I ___ twelve years old.", "da": ["is", "are", "am", "be"], "d": 2},
        ]
    },
    "so_dem": {
        "ten": "Số đếm 1–100 — ôn lớp 4–5",
        "cau_hoi": [
            {"nd": "Chọn số 'twenty-five':", "da": ["25", "52", "15", "35"], "d": 0},
            {"nd": "12 + 8 = ___", "da": ["twenty", "twelve", "thirty", "forty"], "d": 0},
            {"nd": "'Forty' là số mấy?", "da": ["14", "40", "4", "44"], "d": 1},
        ]
    },
    "mau_sac": {
        "ten": "Màu sắc — ôn lớp 4",
        "cau_hoi": [
            {"nd": "Từ 'blue' nghĩa là màu gì?", "da": ["Đỏ", "Xanh dương", "Vàng", "Tím"], "d": 1},
            {"nd": "Màu 'red' là màu gì?", "da": ["Xanh lá", "Đen", "Đỏ", "Trắng"], "d": 2},
        ]
    },
    "family": {
        "ten": "Gia đình — ôn lớp 4",
        "cau_hoi": [
            {"nd": "My mother's mother is my ___.", "da": ["aunt", "grandmother", "sister", "cousin"], "d": 1},
            {"nd": "My father's brother is my ___.", "da": ["uncle", "grandfather", "cousin", "nephew"], "d": 0},
        ]
    },
    "present_simple": {
        "ten": "Hiện tại đơn cơ bản — ôn lớp 5–6",
        "ly_thuyet": "Hành động lặp lại thường xuyên. He/She/It + động từ thêm s/es.",
        "cau_hoi": [
            {"nd": "He ___ football every Sunday.", "da": ["play", "plays", "playing", "played"], "d": 1},
            {"nd": "I ___ to school by bike.", "da": ["go", "goes", "going", "went"], "d": 0},
            {"nd": "She ___ TV every evening.", "da": ["watch", "watchs", "watches", "watching"], "d": 2},
        ]
    },
    "food_basic": {
        "ten": "Đồ ăn cơ bản — ôn lớp 5",
        "cau_hoi": [
            {"nd": "We have ___ in the morning: bread and eggs.", "da": ["lunch", "breakfast", "dinner", "snack"], "d": 1},
            {"nd": "'Rice' nghĩa là gì?", "da": ["Phở", "Cơm", "Bánh mì", "Cháo"], "d": 1},
        ]
    },
    "weather": {
        "ten": "Thời tiết & mùa — ôn lớp 5",
        "cau_hoi": [
            {"nd": "It's ___ in summer.", "da": ["cold", "hot", "warm", "cool"], "d": 1},
            {"nd": "It often rains in ___.", "da": ["spring", "winter", "the rainy season", "autumn"], "d": 2},
        ]
    },
    "wh_questions": {
        "ten": "Câu hỏi Wh- — ôn lớp 6",
        "cau_hoi": [
            {"nd": "___ do you live? – In Hanoi.", "da": ["What", "Where", "When", "Who"], "d": 1},
            {"nd": "___ is that man? – He's my teacher.", "da": ["What", "Where", "Who", "How"], "d": 2},
        ]
    },
    "past_simple_regular": {
        "ten": "Quá khứ đơn (động từ có quy tắc) — ôn lớp 6",
        "ly_thuyet": "Thêm -ed vào động từ. VD: play → played, watch → watched.",
        "cau_hoi": [
            {"nd": "I ___ football yesterday.", "da": ["play", "plays", "played", "playing"], "d": 2},
            {"nd": "She ___ TV last night.", "da": ["watchs", "watched", "watching", "watch"], "d": 1},
        ]
    },
    "comparative": {
        "ten": "So sánh hơn — ôn lớp 6",
        "ly_thuyet": "Tính từ ngắn + er; tính từ dài: more + adj. Kèm 'than'.",
        "cau_hoi": [
            {"nd": "My brother is ___ than me.", "da": ["tall", "taller", "more tall", "tallest"], "d": 1},
            {"nd": "English is ___ than Math.", "da": ["easy", "easier", "more easy", "easiest"], "d": 1},
        ]
    },
}

# ============================================================
# 2. DỮ LIỆU 12 UNIT LỚP 7 (Global Success)
# ============================================================
ANH = {
    "Lớp 7": {
        # ============ UNIT 1: LEISURE ACTIVITIES ============
        "Unit 1: Leisure Activities": {
            "Lesson 1: Vocabulary & Ôn To Be": {
                "ly_thuyet": (
                    "TỪ VỰNG: hobby (sở thích), indoor (trong nhà), outdoor (ngoài trời), "
                    "collect stamps (sưu tem), go fishing (đi câu cá), play chess (chơi cờ), "
                    "make models (lắp mô hình), do gardening (làm vườn).\n"
                    "🔄 ÔN TỪ LỚP 4: Động từ to be — I am / You are / He is. My hobby IS reading."
                ),
                "vi_du": "My hobby is collecting stamps. It is an indoor activity.",
                "nghe": [
                    {"tu": "hobby", "phi_en_am": "/ˈhɒbi/", "nghia": "sở thích"},
                    {"tu": "outdoor", "phi_en_am": "/ˌaʊtˈdɔː/", "nghia": "ngoài trời"},
                    {"tu": "collect stamps", "phi_en_am": "/kəˈlekt stæmps/", "nghia": "sưu tem"},
                ],
                "on_tap": ["to_be", "so_dem"],
                "cau_hoi": [
                    {"nd": "'Hobby' nghĩa là gì?", "da": ["Sở thích", "Công việc", "Trò chơi", "Bài tập"], "d": 0},
                    {"nd": "Hoạt động nào là 'outdoor'?", "da": ["Đọc sách", "Chơi cờ", "Chơi bóng đá", "Lắp mô hình"], "d": 2},
                    {"nd": "My hobby ___ reading books.", "da": ["am", "is", "are", "be"], "d": 1, "gt": "My hobby (it) + is"},
                ],
                "bt_co_ban": [
                    {"de": "Điền từ đúng: My ___ (sở thích) is playing badminton.", "dd": ["hobby"]},
                    {"de": "Chọn từ khác loại: swimming / reading / book / fishing.", "dd": ["book"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 3 câu nói về sở thích của em (bắt đầu: My hobby is...).", "dd": ["VD: My hobby is playing football."], "kieu": "tu_luan"},
                ]
            },
            "Lesson 2: Grammar — like/love/enjoy/hate + V-ing": {
                "ly_thuyet": (
                    "CÔNG THỨC: like / love / enjoy / hate / (be) fond of + V-ing.\n"
                    "VD: I love playing volleyball. She hates getting up early. They enjoy fishing.\n"
                    "🔄 ÔN TỪ LỚP 5–6: Hiện tại đơn — He plays football every Sunday (chú ý thêm 's')."
                ),
                "vi_du": "I enjoy listening to music in my free time.",
                "on_tap": ["present_simple"],
                "cau_hoi": [
                    {"nd": "She enjoys ___ to music.", "da": ["listen", "listens", "listening", "listened"], "d": 2, "gt": "enjoy + V-ing"},
                    {"nd": "They hate ___ up early.", "da": ["get", "gets", "getting", "got"], "d": 2},
                    {"nd": "My brother ___ chess every weekend.", "da": ["play", "plays", "playing", "played"], "d": 1, "gt": "He/She/It + V(s/es)"},
                ],
                "bt_co_ban": [
                    {"de": "Cho dạng đúng: I love ___ (read) comics.", "dd": ["reading"]},
                    {"de": "Cho dạng đúng: She hates ___ (do) housework.", "dd": ["doing"]},
                ],
                "bt_nang_cao": [
                    {"de": "Nối: 'I am fond of' + ?  A. play piano  B. playing piano  C. plays piano", "dd": ["B. playing piano"]},
                ]
            }
        },
        # ============ UNIT 2: HEALTH ============
        "Unit 2: Health": {
            "Lesson 1: Vocabulary & should/shouldn't": {
                "ly_thuyet": (
                    "TỪ VỰNG: headache (đau đầu), stomachache (đau bụng), fever (sốt), "
                    "sore throat (đau họng), toothache (đau răng), junk food (đồ ăn vặt), "
                    "exercise (tập thể dục).\n"
                    "NGỮ PHÁP: should (nên) / shouldn't (không nên) + động từ nguyên mẫu.\n"
                    "VD: You should drink more water. You shouldn't eat too much candy.\n"
                    "🔄 ÔN: Đồ ăn cơ bản (lớp 5) + bộ phận cơ thể."
                ),
                "vi_du": "I have a headache. I should take a rest.",
                "on_tap": ["food_basic", "to_be"],
                "cau_hoi": [
                    {"nd": "'Headache' nghĩa là gì?", "da": ["Đau bụng", "Đau đầu", "Sốt", "Đau răng"], "d": 1},
                    {"nd": "You ___ eat too much candy. It's bad for your teeth.", "da": ["should", "shouldn't", "can", "must"], "d": 1},
                    {"nd": "You ___ do exercise every day to stay healthy.", "da": ["shouldn't", "should", "don't", "not"], "d": 1},
                ],
                "bt_co_ban": [
                    {"de": "Điền: You ___ (nên) drink lots of water.", "dd": ["should"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 lời khuyên cho bạn bị cảm cúm (dùng should/shouldn't).", "dd": ["You should rest. You shouldn't go out."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 3: COMMUNITY SERVICE ============
        "Unit 3: Community Service": {
            "Lesson 1: Past Simple (regular verbs)": {
                "ly_thuyet": (
                    "TỪ VỰNG: volunteer (tình nguyện viên), help (giúp đỡ), donate (quyên góp), "
                    "elderly (người già), community (cộng đồng), clean up (dọn dẹp).\n"
                    "NGỮ PHÁP: Quá khứ đơn — động từ có quy tắc thêm -ed. "
                    "VD: clean → cleaned, help → helped, watch → watched.\n"
                    "🔄 ÔN TỪ LỚP 6: Quá khứ đơn cơ bản (played, watched)."
                ),
                "vi_du": "Last week, we helped the elderly clean their houses.",
                "on_tap": ["past_simple_regular", "wh_questions"],
                "cau_hoi": [
                    {"nd": "We ___ trees last Sunday.", "da": ["plant", "plants", "planted", "planting"], "d": 2},
                    {"nd": "She ___ money for charity yesterday.", "da": ["donate", "donates", "donated", "donating"], "d": 2},
                    {"nd": "'Volunteer' nghĩa là gì?", "da": ["Người tình nguyện", "Người già", "Bệnh nhân", "Công nhân"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Quá khứ của 'clean' là gì?", "dd": ["cleaned"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 1 câu về hoạt động tình nguyện em đã làm tuần trước.", "dd": ["VD: I cleaned the park last week."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 4: MUSIC AND ARTS ============
        "Unit 4: Music and Arts": {
            "Lesson 1: Comparative & Superlative": {
                "ly_thuyet": (
                    "TỪ VỰNG: instrument (nhạc cụ), painting (bức tranh), exhibition (triển lãm), "
                    "artist (họa sĩ), singer (ca sĩ), talented (tài năng).\n"
                    "NGỮ PHÁP: So sánh hơn (adj + er / more + adj) + than; "
                    "So sánh nhất (the + adj + est / the most + adj).\n"
                    "VD: This painting is more beautiful than that one. It is the most beautiful.\n"
                    "🔄 ÔN TỪ LỚP 6: So sánh hơn cơ bản (taller, bigger)."
                ),
                "vi_du": "Mozart is one of the most talented musicians in the world.",
                "on_tap": ["comparative", "mau_sac"],
                "cau_hoi": [
                    {"nd": "This song is ___ than that one.", "da": ["interesting", "more interesting", "most interesting", "interestinger"], "d": 1},
                    {"nd": "She is the ___ singer in my class.", "da": ["good", "better", "best", "more good"], "d": 2},
                    {"nd": "'Painting' nghĩa là gì?", "da": ["Bức tranh", "Bài hát", "Nhạc cụ", "Vũ điệu"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "So sánh hơn của 'tall' là gì?", "dd": ["taller"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu so sánh hai ca sĩ em thích.", "dd": ["VD: A is taller than B."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 5: VIETNAMESE FOOD AND DRINK ============
        "Unit 5: Vietnamese Food and Drink": {
            "Lesson 1: Countable / Uncountable nouns": {
                "ly_thuyet": (
                    "TỪ VỰNG: ingredients (nguyên liệu), spicy (cay), sweet (ngọt), "
                    "delicious (ngon), noodle soup (phở), spring roll (chả giò).\n"
                    "NGỮ PHÁP: Danh từ đếm được (a/an, many, few) / không đếm được (much, little, some).\n"
                    "VD: There is some rice. There are many eggs.\n"
                    "🔄 ÔN TỪ LỚP 5: Từ vựng đồ ăn cơ bản (rice, bread, milk)."
                ),
                "vi_du": "Pho is the most delicious noodle soup in Vietnam.",
                "on_tap": ["food_basic", "to_be"],
                "cau_hoi": [
                    {"nd": "There ___ some milk in the fridge.", "da": ["is", "are", "am", "be"], "d": 0, "gt": "milk không đếm được + is"},
                    {"nd": "There ___ many eggs on the table.", "da": ["is", "are", "am", "be"], "d": 1},
                    {"nd": "'Spicy' nghĩa là gì?", "da": ["Ngọt", "Cay", "Mặn", "Chua"], "d": 1},
                ],
                "bt_co_ban": [
                    {"de": "Điền a/an/some: I need ___ rice.", "dd": ["some"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu giới thiệu món ăn Việt Nam em thích.", "dd": ["VD: I like pho. It is delicious."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 6: THE FIRST UNIVERSITY IN VIETNAM ============
        "Unit 6: The First University in Vietnam": {
            "Lesson 1: Past Simple (irregular verbs)": {
                "ly_thuyet": (
                    "TỪ VỰNG: history (lịch sử), king (vua), scholar (học giả), "
                    "tradition (truyền thống), temple (đền), stele (bia đá).\n"
                    "NGỮ PHÁP: Quá khứ đơn động từ BẤT QUY TẮC: go→went, have→had, "
                    "see→saw, take→took, build→built, become→became.\n"
                    "🔄 ÔN TỪ LỚP 6: Quá khứ đơn có quy tắc + câu hỏi Wh-."
                ),
                "vi_du": "King Ly Thanh Tong built the Temple of Literature in 1070.",
                "on_tap": ["past_simple_regular", "wh_questions"],
                "cau_hoi": [
                    {"nd": "We ___ to the Temple of Literature last summer.", "da": ["go", "goes", "went", "goed"], "d": 2},
                    {"nd": "She ___ a great time in Hanoi.", "da": ["have", "has", "had", "haved"], "d": 2},
                    {"nd": "'Scholar' nghĩa là gì?", "da": ["Học giả", "Nông dân", "Công nhân", "Kỹ sư"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Quá khứ của 'go' là gì?", "dd": ["went"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu về di tích lịch sử em đã thăm.", "dd": ["VD: I went to Hoan Kiem Lake."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 7: TRAFFIC ============
        "Unit 7: Traffic": {
            "Lesson 1: must / mustn't & imperatives": {
                "ly_thuyet": (
                    "TỪ VỰNG: vehicle (phương tiện), traffic jam (kẹt xe), accident (tai nạn), "
                    "helmet (mũ bảo hiểm), seatbelt (dây an toàn), road sign (biển báo).\n"
                    "NGỮ PHÁP: must (phải) / mustn't (cấm) + động từ nguyên mẫu.\n"
                    "VD: You must wear a helmet. You mustn't run across the road.\n"
                    "🔄 ÔN TỪ LỚP 4–5: Số đếm + tên phương tiện (bus, bike, car, train)."
                ),
                "vi_du": "You must look left and right before crossing the road.",
                "on_tap": ["so_dem", "present_simple"],
                "cau_hoi": [
                    {"nd": "You ___ wear a helmet when riding a motorbike.", "da": ["must", "mustn't", "shouldn't", "can't"], "d": 0},
                    {"nd": "You ___ play football on the street.", "da": ["must", "mustn't", "should", "can"], "d": 1},
                    {"nd": "'Traffic jam' nghĩa là gì?", "da": ["Kẹt xe", "Tai nạn", "Biển báo", "Đường sá"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Điền must/mustn't: You ___ drive fast in town.", "dd": ["mustn't"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 luật an toàn giao thông em biết.", "dd": ["VD: You must stop at the red light."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 8: FILMS ============
        "Unit 8: Films": {
            "Lesson 1: Will future & adjectives of feeling": {
                "ly_thuyet": (
                    "TỪ VỰNG: genre (thể loại), actor (diễn viên nam), actress (diễn viên nữ), "
                    "director (đạo diễn), exciting (thú vị), boring (nhàm chán), scary (kinh dị).\n"
                    "NGỮ PHÁP: Tương lai đơn (will + V) để dự đoán/đưa ra quyết định.\n"
                    "VD: I think this film will be exciting. I will watch it tonight.\n"
                    "🔄 ÔN TỪ LỚP 6: Tính từ cảm xúc (happy, sad, tired)."
                ),
                "vi_du": "I think she will become a famous actress one day.",
                "on_tap": ["to_be", "comparative"],
                "cau_hoi": [
                    {"nd": "I think the film ___ interesting.", "da": ["will be", "is be", "be will", "will is"], "d": 0},
                    {"nd": "We ___ go to the cinema tonight.", "da": ["will", "are", "do", "were"], "d": 0},
                    {"nd": "'Director' nghĩa là gì?", "da": ["Diễn viên", "Đạo diễn", "Ca sĩ", "Võ sĩ"], "d": 1},
                ],
                "bt_co_ban": [
                    {"de": "Diễn tả tương lai: I (visit) ___ my grandmother tomorrow.", "dd": ["will visit"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu về bộ phim em sẽ xem cuối tuần.", "dd": ["VD: I will watch a cartoon."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 9: FESTIVALS AROUND THE WORLD ============
        "Unit 9: Festivals Around the World": {
            "Lesson 1: Present continuous (future meaning)": {
                "ly_thuyet": (
                    "TỪ VỰNG: celebrate (ăn mừng), tradition (truyền thống), costume (trang phục), "
                    "firework (pháo hoa), parade (diễu hành), festival (lễ hội).\n"
                    "NGỮ PHÁP: Hiện tại tiếp diễn diễn tả tương lai đã có kế hoạch (be + V-ing).\n"
                    "VD: We are visiting Da Lat this summer. I am meeting my friends tomorrow.\n"
                    "🔄 ÔN TỪ LỚP 5: Mùa & thời tiết (spring, summer, sunny, rainy)."
                ),
                "vi_du": "Tet is the most important festival in Vietnam.",
                "on_tap": ["weather", "present_simple"],
                "cau_hoi": [
                    {"nd": "We ___ to Hue this summer.", "da": ["travel", "are travelling", "travels", "travelled"], "d": 1},
                    {"nd": "She ___ her grandparents next week.", "da": ["visit", "visits", "is visiting", "visited"], "d": 2},
                    {"nd": "'Festival' nghĩa là gì?", "da": ["Lễ hội", "Chợ", "Trường học", "Bãi biển"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Diễn tả kế hoạch: I (go) ___ to the park tomorrow.", "dd": ["am going"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu về kế hoạch lễ hội tới của em.", "dd": ["VD: We are having a party."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 10: SOURCES OF ENERGY ============
        "Unit 10: Sources of Energy": {
            "Lesson 1: Conditional type 1 (If...)": {
                "ly_thuyet": (
                    "TỪ VỰNG: renewable (tái tạo), solar energy (năng lượng mặt trời), "
                    "wind power (điện gió), electricity (điện), save (tiết kiệm), waste (lãng phí).\n"
                    "NGỮ PHÁP: Câu điều kiện loại 1: If + hiện tại đơn, will + V.\n"
                    "VD: If we save electricity, we will save money.\n"
                    "🔄 ÔN: Hiện tại đơn + tương lai đơn (will)."
                ),
                "vi_du": "If it is sunny, we will use solar energy.",
                "on_tap": ["present_simple", "weather"],
                "cau_hoi": [
                    {"nd": "If we ___ less electricity, we will save money.", "da": ["use", "uses", "used", "using"], "d": 0},
                    {"nd": "If it rains, we ___ at home.", "da": ["stay", "will stay", "stayed", "staying"], "d": 1},
                    {"nd": "'Renewable' nghĩa là gì?", "da": ["Tái tạo", "Hết sạch", "Độc hại", "Vĩnh viễn"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Điền: If you study hard, you (pass) ___ the exam.", "dd": ["will pass"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu điều kiện về bảo vệ môi trường.", "dd": ["VD: If we plant trees, the air will be cleaner."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 11: TRAVELLING IN THE FUTURE ============
        "Unit 11: Travelling in the Future": {
            "Lesson 1: might / will be able to": {
                "ly_thuyet": (
                    "TỪ VỰNG: invention (phát minh), aircraft (máy bay), solar-powered (chạy bằng năng lượng mặt trời), "
                    "traffic jam (kẹt xe), pilot (phi công), journey (hành trình).\n"
                    "NGỮ PHÁP: might (có lẽ) + V; will be able to (sẽ có thể) + V.\n"
                    "VD: In the future, we might travel by flying cars. We will be able to go to space.\n"
                    "🔄 ÔN: Tương lai đơn will + phương tiện giao thông."
                ),
                "vi_du": "People might live on the Moon in 2050.",
                "on_tap": ["so_dem", "to_be"],
                "cau_hoi": [
                    {"nd": "In the future, we ___ travel by flying cars.", "da": ["might", "must", "should", "are"], "d": 0},
                    {"nd": "Robots ___ help us do housework.", "da": ["will be able to", "can to", "able to", "will can"], "d": 0},
                    {"nd": "'Invention' nghĩa là gì?", "da": ["Phát minh", "Khám phá", "Cuộc phiêu lưu", "Khoa học"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Điền might/will: It ___ rain tomorrow (không chắc chắn).", "dd": ["might"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu về phương tiện giao thông tương lai.", "dd": ["VD: We might travel by solar planes."], "kieu": "tu_luan"},
                ]
            }
        },
        # ============ UNIT 12: AN OVERCROWDED WORLD ============
        "Unit 12: An Overcrowded World": {
            "Lesson 1: fewer / less / more (ôn tổng hợp)": {
                "ly_thuyet": (
                    "TỪ VỰNG: overcrowded (quá đông), population (dân số), slum (khu ổ chuột), "
                    "healthcare (chăm sóc sức khỏe), education (giáo dục), shortage (sự thiếu hụt).\n"
                    "NGỮ PHÁP: fewer + danh từ đếm được; less + danh từ không đếm được; more + cả hai.\n"
                    "VD: There are fewer cars. There is less pollution. We need more schools.\n"
                    "🔄 ÔN TỔNG HỢP: to be, hiện tại đơn, quá khứ đơn, so sánh hơn."
                ),
                "vi_du": "Big cities are overcrowded, so there is more pollution.",
                "on_tap": ["to_be", "present_simple", "comparative", "food_basic"],
                "cau_hoi": [
                    {"nd": "There are ___ cars in the countryside than in the city.", "da": ["fewer", "less", "much", "little"], "d": 0, "gt": "cars đếm được → fewer"},
                    {"nd": "There is ___ pollution in the countryside.", "da": ["fewer", "less", "many", "few"], "d": 1, "gt": "pollution không đếm được → less"},
                    {"nd": "'Population' nghĩa là gì?", "da": ["Dân số", "Tình nguyện", "Công nghiệp", "Nông nghiệp"], "d": 0},
                ],
                "bt_co_ban": [
                    {"de": "Điền fewer/less: There is ___ water in summer.", "dd": ["less"]},
                ],
                "bt_nang_cao": [
                    {"de": "Viết 2 câu về vấn đề thành phố quá đông.", "dd": ["VD: There are too many people."], "kieu": "tu_luan"},
                ]
            }
        },
    }
}

# ============================================================
# 3. TỪ ĐIỂN ANH-VIỆT OFFLINE (tra tức thì, không cần mạng)
# ============================================================
TU_DIEN_OFFLINE = {
    "hello":      {"pa": "/həˈləʊ/", "loai": "thán từ", "nghia": "xin chào",
                   "vi_du": "Hello, nice to meet you.", "vi_du_dich": "Xin chào, rất vui được gặp bạn."},
    "goodbye":    {"pa": "/ˌɡʊdˈbaɪ/", "loai": "thán từ", "nghia": "tạm biệt",
                   "vi_du": "Goodbye! See you tomorrow.", "vi_du_dich": "Tạm biệt! Hẹn gặp lại bạn ngày mai."},
    "school":     {"pa": "/skuːl/", "loai": "danh từ", "nghia": "trường học",
                   "vi_du": "I go to school by bike.", "vi_du_dich": "Tôi đi học bằng xe đạp."},
    "teacher":    {"pa": "/ˈtiːtʃər/", "loai": "danh từ", "nghia": "giáo viên, thầy/cô giáo",
                   "vi_du": "My teacher is very kind.", "vi_du_dich": "Cô giáo của tôi rất tốt bụng."},
    "student":    {"pa": "/ˈstjuːdnt/", "loai": "danh từ", "nghia": "học sinh, sinh viên",
                   "vi_du": "She is a good student.", "vi_du_dich": "Cô ấy là một học sinh giỏi."},
    "book":       {"pa": "/bʊk/", "loai": "danh từ", "nghia": "quyển sách, cuốn sách",
                   "vi_du": "I am reading a book.", "vi_du_dich": "Tôi đang đọc một cuốn sách."},
    "friend":     {"pa": "/frend/", "loai": "danh từ", "nghia": "bạn bè, người bạn",
                   "vi_du": "He is my best friend.", "vi_du_dich": "Anh ấy là bạn thân nhất của tôi."},
    "family":     {"pa": "/ˈfæməli/", "loai": "danh từ", "nghia": "gia đình, con nhà",
                   "vi_du": "There are four people in my family.", "vi_du_dich": "Gia đình tôi có bốn người."},
    "happy":      {"pa": "/ˈhæpi/", "loai": "tính từ", "nghia": "vui vẻ, hạnh phúc",
                   "vi_du": "I feel very happy today.", "vi_du_dich": "Hôm nay tôi cảm thấy rất vui."},
    "sad":        {"pa": "/sæd/", "loai": "tính từ", "nghia": "buồn, buồn bã",
                   "vi_du": "She looks sad.", "vi_du_dich": "Cô ấy trông có vẻ buồn."},
    "big":        {"pa": "/bɪɡ/", "loai": "tính từ", "nghia": "to, lớn",
                   "vi_du": "This is a big house.", "vi_du_dich": "Đây là một ngôi nhà to."},
    "small":      {"pa": "/smɔːl/", "loai": "tính từ", "nghia": "nhỏ, bé",
                   "vi_du": "I have a small cat.", "vi_du_dich": "Tôi có một chú mèo nhỏ."},
    "beautiful":  {"pa": "/ˈbjuːtɪfl/", "loai": "tính từ", "nghia": "đẹp, xinh đẹp",
                   "vi_du": "The garden is beautiful.", "vi_du_dich": "Khu vườn thật đẹp."},
    "run":        {"pa": "/rʌn/", "loai": "động từ", "nghia": "chạy, đạp (xe máy)",
                   "vi_du": "I run every morning.", "vi_du_dich": "Tôi chạy bộ mỗi sáng."},
    "eat":        {"pa": "/iːt/", "loai": "động từ", "nghia": "ăn",
                   "vi_du": "We eat rice every day.", "vi_du_dich": "Chúng tôi ăn cơm hàng ngày."},
    "drink":      {"pa": "/drɪŋk/", "loai": "động từ", "nghia": "uống; đồ uống",
                   "vi_du": "I drink milk every morning.", "vi_du_dich": "Tôi uống sữa mỗi sáng."},
    "play":       {"pa": "/pleɪ/", "loai": "động từ", "nghia": "chơi, chơi (thể thao/nhạc cụ)",
                   "vi_du": "They play football after school.", "vi_du_dich": "Họ chơi bóng đá sau giờ học."},
    "study":      {"pa": "/ˈstʌdi/", "loai": "động từ", "nghia": "học, nghiên cứu",
                   "vi_du": "I study English every day.", "vi_du_dich": "Tôi học tiếng Anh mỗi ngày."},
    "work":       {"pa": "/wɜːk/", "loai": "động từ/danh từ", "nghia": "làm việc; công việc",
                   "vi_du": "My father works in a hospital.", "vi_du_dich": "Bố tôi làm việc ở bệnh viện."},
    "love":       {"pa": "/lʌv/", "loai": "động từ/danh từ", "nghia": "yêu; tình yêu",
                   "vi_du": "I love my family.", "vi_du_dich": "Tôi yêu gia đình của mình."},
    "like":       {"pa": "/laɪk/", "loai": "động từ", "nghia": "thích; giống như",
                   "vi_du": "I like listening to music.", "vi_du_dich": "Tôi thích nghe nhạc."},
    "want":       {"pa": "/wɒnt/", "loai": "động từ", "nghia": "muốn, ao ước",
                   "vi_du": "I want to be a doctor.", "vi_du_dich": "Tôi muốn trở thành bác sĩ."},
    "have":       {"pa": "/hæv/", "loai": "động từ", "nghia": "có; ăn (bữa ăn)",
                   "vi_du": "I have a new bike.", "vi_du_dich": "Tôi có một chiếc xe đạp mới."},
    "go":         {"pa": "/ɡəʊ/", "loai": "động từ", "nghia": "đi, đi lại",
                   "vi_du": "We go to school at 6.30.", "vi_du_dich": "Chúng tôi đi học lúc 6 giờ 30."},
    "come":       {"pa": "/kʌm/", "loai": "động từ", "nghia": "đến, tới",
                   "vi_du": "She comes from Da Nang.", "vi_du_dich": "Cô ấy đến từ Đà Nẵng."},
    "see":        {"pa": "/siː/", "loai": "động từ", "nghia": "thấy, nhìn thấy",
                   "vi_du": "I can see the sea.", "vi_du_dich": "Tôi có thể nhìn thấy biển."},
    "know":       {"pa": "/nəʊ/", "loai": "động từ", "nghia": "biết, quen biết",
                   "vi_du": "Do you know this word?", "vi_du_dich": "Bạn có biết từ này không?"},
    "new":        {"pa": "/njuː/", "loai": "tính từ", "nghia": "mới, mới mẻ",
                   "vi_du": "I have a new pen.", "vi_du_dich": "Tôi có một cây bút mới."},
    "old":        {"pa": "/əʊld/", "loai": "tính từ", "nghia": "già; cũ",
                   "vi_du": "My grandfather is 70 years old.", "vi_du_dich": "Ông tôi năm nay 70 tuổi."},
    "good":       {"pa": "/ɡʊd/", "loai": "tính từ", "nghia": "tốt, giỏi",
                   "vi_du": "She is good at Math.", "vi_du_dich": "Cô ấy học Toán giỏi."},
    "bad":        {"pa": "/bæd/", "loai": "tính từ", "nghia": "xấu, kém",
                   "vi_du": "Smoking is bad for health.", "vi_du_dich": "Hút thuốc lá có hại cho sức khỏe."},
    "many":       {"pa": "/ˈmeni/", "loai": "tính từ", "nghia": "nhiều (danh từ đếm được)",
                   "vi_du": "There are many books on the desk.", "vi_du_dich": "Có nhiều sách trên bàn."},
    "much":       {"pa": "/mʌtʃ/", "loai": "tính từ", "nghia": "nhiều (danh từ không đếm được)",
                   "vi_du": "I don't have much time.", "vi_du_dich": "Tôi không có nhiều thời gian."},
    "water":      {"pa": "/ˈwɔːtər/", "loai": "danh từ", "nghia": "nước",
                   "vi_du": "Drink a lot of water.", "vi_du_dich": "Hãy uống nhiều nước."},
    "food":       {"pa": "/fuːd/", "loai": "danh từ", "nghia": "thức ăn, đồ ăn",
                   "vi_du": "Vietnamese food is delicious.", "vi_du_dich": "Đồ ăn Việt Nam rất ngon."},
    "house":      {"pa": "/haʊs/", "loai": "danh từ", "nghia": "ngôi nhà",
                   "vi_du": "My house is near the school.", "vi_du_dich": "Nhà tôi gần trường."},
    "city":       {"pa": "/ˈsɪti/", "loai": "danh từ", "nghia": "thành phố",
                   "vi_du": "Hanoi is the capital city.", "vi_du_dich": "Hà Nội là thủ đô."},
    "country":    {"pa": "/ˈkʌntri/", "loai": "danh từ", "nghia": "đất nước; nông thôn",
                   "vi_du": "Vietnam is a beautiful country.", "vi_du_dich": "Việt Nam là một đất nước đẹp."},
    "day":        {"pa": "/deɪ/", "loai": "danh từ", "nghia": "ngày; ban ngày",
                   "vi_du": "Today is a sunny day.", "vi_du_dich": "Hôm nay là một ngày nắng."},
    "night":      {"pa": "/naɪt/", "loai": "danh từ", "nghia": "đêm; ban đêm",
                   "vi_du": "I sleep at night.", "vi_du_dich": "Tôi ngủ vào ban đêm."},
    "morning":    {"pa": "/ˈmɔːnɪŋ/", "loai": "danh từ", "nghia": "buổi sáng",
                   "vi_du": "I get up early in the morning.", "vi_du_dich": "Tôi dậy sớm vào buổi sáng."},
    "evening":    {"pa": "/ˈiːvnɪŋ/", "loai": "danh từ", "nghia": "buổi tối",
                   "vi_du": "We watch TV in the evening.", "vi_du_dich": "Chúng tôi xem TV vào buổi tối."},
    "year":       {"pa": "/jɪər/", "loai": "danh từ", "nghia": "năm",
                   "vi_du": "I am twelve years old.", "vi_du_dich": "Tôi mười hai tuổi."},
    "time":       {"pa": "/taɪm/", "loai": "danh từ", "nghia": "thời gian; giờ",
                   "vi_du": "What time is it?", "vi_du_dich": "Bây giờ là mấy giờ?"},
    "people":     {"pa": "/ˈpiːpl/", "loai": "danh từ", "nghia": "người; nhân dân",
                   "vi_du": "There are many people in the park.", "vi_du_dich": "Có nhiều người trong công viên."},
    "child":      {"pa": "/tʃaɪld/", "loai": "danh từ", "nghia": "trẻ em (số ít); số nhiều: children",
                   "vi_du": "The child is playing.", "vi_du_dich": "Đứa trẻ đang chơi."},
    "man":        {"pa": "/mæn/", "loai": "danh từ", "nghia": "người đàn ông; số nhiều: men",
                   "vi_du": "The man is a doctor.", "vi_du_dich": "Người đàn ông đó là bác sĩ."},
    "woman":      {"pa": "/ˈwʊmən/", "loai": "danh từ", "nghia": "người phụ nữ; số nhiều: women",
                   "vi_du": "The woman is my mother.", "vi_du_dich": "Người phụ nữ đó là mẹ tôi."},
    "word":       {"pa": "/wɜːd/", "loai": "danh từ", "nghia": "từ; lời nói",
                   "vi_du": "Learn new words every day.", "vi_du_dich": "Học từ mới mỗi ngày."},
    "english":    {"pa": "/ˈɪŋɡlɪʃ/", "loai": "danh từ/tính từ", "nghia": "tiếng Anh; người Anh",
                   "vi_du": "I study English at school.", "vi_du_dich": "Tôi học tiếng Anh ở trường."},
    "vietnam":    {"pa": "/ˌvjetˈnæm/", "loai": "danh từ", "nghia": "Việt Nam",
                   "vi_du": "I love Vietnam.", "vi_du_dich": "Tôi yêu Việt Nam."},
    "hobby":      {"pa": "/ˈhɒbi/", "loai": "danh từ", "nghia": "sở thích",
                   "vi_du": "My hobby is reading.", "vi_du_dich": "Sở thích của tôi là đọc sách."},
    "music":      {"pa": "/ˈmjuːzɪk/", "loai": "danh từ", "nghia": "âm nhạc",
                   "vi_du": "I like pop music.", "vi_du_dich": "Tôi thích nhạc pop."},
    "sport":      {"pa": "/spɔːt/", "loai": "danh từ", "nghia": "thể thao",
                   "vi_du": "Football is my favourite sport.", "vi_du_dich": "Bóng đá là môn thể thao yêu thích của tôi."},
    "movie":      {"pa": "/ˈmuːvi/", "loai": "danh từ", "nghia": "bộ phim",
                   "vi_du": "We watch a movie every weekend.", "vi_du_dich": "Chúng tôi xem phim mỗi cuối tuần."},
    "delicious":  {"pa": "/dɪˈlɪʃəs/", "loai": "tính từ", "nghia": "ngon, ngon lành",
                   "vi_du": "Pho is delicious.", "vi_du_dich": "Phở rất ngon."},
    "interesting":{"pa": "/ˈɪntrəstɪŋ/", "loai": "tính từ", "nghia": "thú vị, hay",
                   "vi_du": "This book is very interesting.", "vi_du_dich": "Cuốn sách này rất thú vị."},
    "difficult":  {"pa": "/ˈdɪfɪkəlt/", "loai": "tính từ", "nghia": "khó, khó khăn",
                   "vi_du": "Math is difficult for me.", "vi_du_dich": "Môn Toán khó với tôi."},
    "easy":       {"pa": "/ˈiːzi/", "loai": "tính từ", "nghia": "dễ, dễ dàng",
                   "vi_du": "This exercise is easy.", "vi_du_dich": "Bài tập này dễ."},
    "important":  {"pa": "/ɪmˈpɔːtnt/", "loai": "tính từ", "nghia": "quan trọng",
                   "vi_du": "English is very important.", "vi_du_dich": "Tiếng Anh rất quan trọng."},
    "healthy":    {"pa": "/ˈhelθi/", "loai": "tính từ", "nghia": "khỏe mạnh, lành mạnh",
                   "vi_du": "Eat healthy food.", "vi_du_dich": "Hãy ăn đồ ăn lành mạnh."},
    "tired":      {"pa": "/ˈtaɪəd/", "loai": "tính từ", "nghia": "mệt, mệt mỏi",
                   "vi_du": "I feel tired after school.", "vi_du_dich": "Tôi cảm thấy mệt sau giờ học."},
    "busy":       {"pa": "/ˈbɪzi/", "loai": "tính từ", "nghia": "bận rộn",
                   "vi_du": "My mother is busy every day.", "vi_du_dich": "Mẹ tôi bận rộn mỗi ngày."},
    "clever":     {"pa": "/ˈklevər/", "loai": "tính từ", "nghia": "thông minh, khéo léo",
                   "vi_du": "He is a clever boy.", "vi_du_dich": "Cậu ấy là một cậu bé thông minh."},
    "kind":       {"pa": "/kaɪnd/", "loai": "tính từ", "nghia": "tốt bụng, tử tế",
                   "vi_du": "She is kind to everyone.", "vi_du_dich": "Cô ấy tốt bụng với mọi người."},
    "young":      {"pa": "/jʌŋ/", "loai": "tính từ", "nghia": "trẻ, trẻ trung",
                   "vi_du": "My sister is young.", "vi_du_dich": "Em gái tôi còn trẻ."},
    "fast":       {"pa": "/fɑːst/", "loai": "tính từ/trạng từ", "nghia": "nhanh, nhanh chóng",
                   "vi_du": "He runs very fast.", "vi_du_dich": "Anh ấy chạy rất nhanh."},
    "slow":       {"pa": "/sləʊ/", "loai": "tính từ/trạng từ", "nghia": "chậm, chậm chạp",
                   "vi_du": "The bus is slow today.", "vi_du_dich": "Xe buýt hôm nay chạy chậm."},
    "hot":        {"pa": "/hɒt/", "loai": "tính từ", "nghia": "nóng, nóng bức",
                   "vi_du": "It is hot in summer.", "vi_du_dich": "Trời nóng vào mùa hè."},
    "cold":       {"pa": "/kəʊld/", "loai": "tính từ", "nghia": "lạnh, lạnh lẽo",
                   "vi_du": "It is cold in winter.", "vi_du_dich": "Trời lạnh vào mùa đông."},
    "sunny":      {"pa": "/ˈsʌni/", "loai": "tính từ", "nghia": "nắng, có nắng",
                   "vi_du": "It is sunny today.", "vi_du_dich": "Hôm nay trời nắng."},
    "rainy":      {"pa": "/ˈreɪni/", "loai": "tính từ", "nghia": "mưa, có mưa",
                   "vi_du": "It is rainy in July.", "vi_du_dich": "Tháng 7 thường có mưa."},
}

# ============================================================
# 4. TỪ CỦA NGÀY + CACHE TRA TỪ
# ============================================================
DS_TU_CUA_NGAY = [
    ("adventure", "/ədˈventʃər/", "cuộc phiêu lưu"),
    ("brilliant", "/ˈbrɪliənt/", "tuyệt vời, rực rỡ"),
    ("curious", "/ˈkjʊəriəs/", "tò mò"),
    ("diligent", "/ˈdɪlɪdʒənt/", "chăm chỉ"),
    ("enormous", "/ɪˈnɔːməs/", "khổng lồ"),
    ("fascinating", "/ˈfæsɪneɪtɪŋ/", "hấp dẫn, mê hoặc"),
    ("generous", "/ˈdʒenərəs/", "hào phóng"),
    ("harmony", "/ˈhɑːməni/", "sự hài hòa"),
    ("imagine", "/ɪˈmædʒɪn/", "tưởng tượng"),
    ("journey", "/ˈdʒɜːni/", "hành trình"),
    ("knowledge", "/ˈnɒlɪdʒ/", "kiến thức"),
    ("language", "/ˈlæŋɡwɪdʒ/", "ngôn ngữ"),
]

TRA_TU_CACHE = {}   # cache trong bộ nhớ, tránh gọi lại API/Gemini

def tra_tu_offline(tu_khoa):
    """Hàm hỗ trợ tra cứu nhanh từ vựng trong từ điển offline."""
    t = tu_khoa.strip().lower()
    return TU_DIEN_OFFLINE.get(t, None)