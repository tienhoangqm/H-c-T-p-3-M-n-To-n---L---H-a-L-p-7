# -*- coding: utf-8 -*-
"""
DỮ LIỆU TIẾNG ANH LỚP 7 — phiên bản 2 (bám bộ Global Success / Kết nối tri thức)

Cấu trúc:
  KIEN_THUC_NEN      : kiến thức nền lớp 4–6, dùng để ôn tập
  ANH                : 12 Unit, mỗi Unit 2 bài (Language / Skills)
  TU_DIEN            : từ điển Anh–Việt offline, tự gộp từ vựng của các Unit
  DS_TU_NANG_CAO     : từ vựng nâng cao cho học sinh khá, giỏi
  tao_de()           : sinh đề ngẫu nhiên, đáp án được xáo trộn đúng
  tra_tu_offline()   : tra từ tức thì, có gợi ý khi gõ sai
  tu_cua_ngay()      : từ nâng cao của ngày
  kiem_tra_du_lieu() : kiểm tra lỗi dữ liệu (đáp án ngoài phạm vi, đáp án trùng...)

Quy ước:
  - Trắc nghiệm: cau(nd, da, d, gt, kho) — d là chỉ số đáp án đúng trong da.
  - Bài tập điền/chuyển đổi: bt(de, dap_an, gt) — dap_an là danh sách các đáp án được chấp nhận.
  - Tự luận: tl(de, goi_y).
  - kho (độ khó): 1 = cơ bản, 2 = vận dụng, 3 = nâng cao.
  - cap của từ: "co_ban" hoặc "nang_cao".
"""
import random
import datetime
import difflib


# ============================================================
# 0. HÀM TẠO CẤU TRÚC DỮ LIỆU
# ============================================================
def tu(w, pa, loai, nghia, vd, vd_dich, cap="co_ban"):
    return {"tu": w, "pa": pa, "loai": loai, "nghia": nghia,
            "vd": vd, "vd_dich": vd_dich, "cap": cap}

def cau(nd, da, d, gt="", kho=1):
    return {"nd": nd, "da": da, "d": d, "gt": gt, "kho": kho}

def bt(de, dap_an, gt=""):
    return {"de": de, "dap_an": dap_an, "gt": gt}

def tl(de, goi_y):
    return {"de": de, "goi_y": goi_y, "kieu": "tu_luan"}

def bai(ten, ly_thuyet, tu_vung, cau_hoi, bai_tap, nang_cao, on_tap=None):
    return {"ten": ten, "ly_thuyet": ly_thuyet, "tu_vung": tu_vung,
            "cau_hoi": cau_hoi, "bai_tap": bai_tap, "nang_cao": nang_cao,
            "on_tap": on_tap or []}


# ============================================================
# 1. NGÂN HÀNG KIẾN THỨC NỀN (LỚP 4–6)
# ============================================================
KIEN_THUC_NEN = {
    "to_be": {
        "ten": "Động từ To Be (am/is/are) — ôn lớp 4",
        "ly_thuyet": "I am; You/We/They are; He/She/It is. Phủ định: am not / isn't / aren't.",
        "cau_hoi": [
            cau("She ___ my best friend.", ["am", "is", "are", "be"], 1),
            cau("They ___ from Da Nang.", ["is", "am", "are", "be"], 2),
            cau("I ___ twelve years old.", ["is", "are", "am", "be"], 2),
        ],
    },
    "so_dem": {
        "ten": "Số đếm 1–100 — ôn lớp 4–5",
        "ly_thuyet": "Số từ 13–19 kết thúc bằng -teen; 20, 30, 40... kết thúc bằng -ty.",
        "cau_hoi": [
            cau("Chọn số 'twenty-five':", ["25", "52", "15", "35"], 0),
            cau("'Forty' là số mấy?", ["14", "40", "4", "44"], 1),
        ],
    },
    "mau_sac": {
        "ten": "Màu sắc — ôn lớp 4",
        "ly_thuyet": "red (đỏ), blue (xanh dương), green (xanh lá), yellow (vàng), black, white.",
        "cau_hoi": [
            cau("Từ 'blue' nghĩa là màu gì?", ["Đỏ", "Xanh dương", "Vàng", "Tím"], 1),
            cau("Màu 'red' là màu gì?", ["Xanh lá", "Đen", "Đỏ", "Trắng"], 2),
        ],
    },
    "gia_dinh": {
        "ten": "Gia đình — ôn lớp 4",
        "ly_thuyet": "father/mother, brother/sister, uncle/aunt, grandmother/grandfather, cousin.",
        "cau_hoi": [
            cau("My mother's mother is my ___.", ["aunt", "grandmother", "sister", "cousin"], 1),
            cau("My father's brother is my ___.", ["uncle", "grandfather", "cousin", "nephew"], 0),
        ],
    },
    "hien_tai_don": {
        "ten": "Hiện tại đơn — ôn lớp 5–6",
        "ly_thuyet": "Diễn tả thói quen. He/She/It + V thêm -s/-es. VD: He plays, She watches.",
        "cau_hoi": [
            cau("He ___ football every Sunday.", ["play", "plays", "playing", "played"], 1),
            cau("She ___ TV every evening.", ["watch", "watchs", "watches", "watching"], 2),
        ],
    },
    "do_an": {
        "ten": "Đồ ăn cơ bản — ôn lớp 5",
        "ly_thuyet": "breakfast (bữa sáng), lunch (bữa trưa), dinner (bữa tối), rice, bread, noodles.",
        "cau_hoi": [
            cau("We have ___ in the morning: bread and eggs.", ["lunch", "breakfast", "dinner", "snack"], 1),
            cau("'Rice' nghĩa là gì?", ["Phở", "Cơm", "Bánh mì", "Cháo"], 1),
        ],
    },
    "thoi_tiet": {
        "ten": "Thời tiết & mùa — ôn lớp 5",
        "ly_thuyet": "sunny, rainy, cloudy, windy, hot, cold; spring, summer, autumn, winter.",
        "cau_hoi": [
            cau("It's ___ in summer.", ["cold", "hot", "warm", "cool"], 1),
            cau("It often rains in ___.", ["spring", "winter", "the rainy season", "autumn"], 2),
        ],
    },
    "wh_questions": {
        "ten": "Câu hỏi Wh- — ôn lớp 6",
        "ly_thuyet": "What (cái gì), Where (ở đâu), When (khi nào), Who (ai), How (như thế nào).",
        "cau_hoi": [
            cau("___ do you live? – In Hanoi.", ["What", "Where", "When", "Who"], 1),
            cau("___ is that man? – He's my teacher.", ["What", "Where", "Who", "How"], 2),
        ],
    },
    "qk_don_co_quy_tac": {
        "ten": "Quá khứ đơn (động từ có quy tắc) — ôn lớp 6",
        "ly_thuyet": "Thêm -ed: play → played, watch → watched. Đuôi -e chỉ thêm -d: live → lived.",
        "cau_hoi": [
            cau("I ___ football yesterday.", ["play", "plays", "played", "playing"], 2),
            cau("She ___ TV last night.", ["watchs", "watched", "watching", "watch"], 1),
        ],
    },
    "so_sanh_hon": {
        "ten": "So sánh hơn — ôn lớp 6",
        "ly_thuyet": "Tính từ ngắn + er; tính từ dài: more + adj. Kèm 'than'.",
        "cau_hoi": [
            cau("My brother is ___ than me.", ["tall", "taller", "more tall", "tallest"], 1),
            cau("English is ___ than Math.", ["easy", "easier", "more easy", "easiest"], 1),
        ],
    },
}


# ============================================================
# 2. DỮ LIỆU 12 UNIT LỚP 7
# ============================================================
ANH = {
    "Lớp 7": {

        # ==================== UNIT 1 ====================
        "Unit 1: Leisure Activities": {
            "Lesson 1: Vocabulary & Grammar": bai(
                ten="Từ vựng sở thích & like/love/enjoy + V-ing",
                ly_thuyet=(
                    "CÔNG THỨC: like / love / enjoy / hate / finish / (be) fond of + V-ing.\n"
                    "VD: I love playing volleyball. She hates getting up early.\n"
                    "Lưu ý: 'want', 'hope', 'decide' đi với TO + V (want to play), KHÔNG dùng V-ing."
                ),
                tu_vung=[
                    tu("hobby", "/ˈhɒbi/", "danh từ", "sở thích", "My hobby is reading.", "Sở thích của tôi là đọc sách."),
                    tu("collect", "/kəˈlekt/", "động từ", "sưu tầm, thu thập", "I collect stamps.", "Tôi sưu tầm tem."),
                    tu("stamp", "/stæmp/", "danh từ", "con tem", "This stamp is very old.", "Con tem này rất cũ."),
                    tu("outdoor", "/ˌaʊtˈdɔː/", "tính từ", "ngoài trời", "We like outdoor activities.", "Chúng tôi thích hoạt động ngoài trời."),
                    tu("indoor", "/ˌɪnˈdɔː/", "tính từ", "trong nhà", "Chess is an indoor game.", "Cờ vua là trò chơi trong nhà."),
                    tu("fishing", "/ˈfɪʃɪŋ/", "danh từ", "câu cá", "He goes fishing on Sundays.", "Anh ấy đi câu cá vào Chủ nhật."),
                    tu("gardening", "/ˈɡɑːdnɪŋ/", "danh từ", "làm vườn", "Gardening helps me relax.", "Làm vườn giúp tôi thư giãn."),
                    tu("relax", "/rɪˈlæks/", "động từ", "thư giãn, nghỉ ngơi", "I relax by listening to music.", "Tôi thư giãn bằng cách nghe nhạc.", "nang_cao"),
                    tu("passion", "/ˈpæʃn/", "danh từ", "đam mê", "Painting is her passion.", "Vẽ tranh là niềm đam mê của cô ấy.", "nang_cao"),
                    tu("leisure", "/ˈleʒər/", "danh từ", "thời gian rảnh rỗi", "What do you do in your leisure time?", "Bạn làm gì lúc rảnh rỗi?", "nang_cao"),
                ],
                cau_hoi=[
                    cau("'Hobby' nghĩa là gì?", ["Sở thích", "Công việc", "Trò chơi", "Bài tập"], 0),
                    cau("She enjoys ___ to music.", ["listen", "listens", "listening", "listened"], 2, "enjoy + V-ing"),
                    cau("They hate ___ up early.", ["get", "gets", "getting", "got"], 2, "hate + V-ing", 2),
                    cau("My brother ___ chess every weekend.", ["play", "plays", "playing", "played"], 1, "He/She/It + V(s/es)"),
                    cau("Which is an indoor activity?", ["Fishing", "Gardening", "Reading books", "Swimming in the sea"], 2),
                    cau("I'm fond of ___ stamps.", ["collect", "collecting", "collected", "collects"], 1, "be fond of + V-ing", 2),
                    cau("I want ___ a new hobby.", ["find", "finding", "to find", "found"], 2, "want + TO V", 2),
                ],
                bai_tap=[
                    bt("Cho dạng đúng: I love ___ (read) comics.", ["reading"]),
                    bt("Cho dạng đúng: She hates ___ (do) housework.", ["doing"]),
                    bt("Hoàn thành: My father likes ___ (go) fishing on Sundays.", ["going"]),
                ],
                nang_cao=[
                    tl("Viết 3 câu về sở thích của em, dùng like/love/enjoy + V-ing.",
                       "VD: I enjoy drawing pictures on weekends."),
                ],
                on_tap=["hien_tai_don", "to_be"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /ɪ/ – /iː/ và đọc hiểu",
                ly_thuyet=(
                    "Phân biệt /ɪ/ (ngắn: ship, sit) và /iː/ (dài: sheep, seat).\n"
                    "Mẹo: /iː/ kéo môi sang hai bên, /ɪ/ thả lỏng hơn."
                ),
                tu_vung=[
                    tu("ship", "/ʃɪp/", "danh từ", "con tàu", "The ship is big.", "Con tàu rất lớn."),
                    tu("sheep", "/ʃiːp/", "danh từ", "con cừu", "The sheep are white.", "Những con cừu màu trắng."),
                    tu("hobbyist", "/ˈhɒbiɪst/", "danh từ", "người theo đuổi sở thích", "He is a stamp hobbyist.", "Anh ấy là người sưu tầm tem.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /iː/?", ["ship", "sheep", "shop", "sip"], 1),
                    cau("Từ nào có nguyên âm khác các từ còn lại: like, time, big, see?", ["like", "time", "big", "see"], 3, "like, time có /aɪ/; big có /ɪ/", 2),
                    cau("Nam's hobby is gardening. What does Nam grow?", ["Tomatoes and flowers", "Fish and birds", "Stamps", "Cars"], 0, "Đọc đoạn văn bên dưới", 2),
                    cau("Why does Nam like gardening?", ["It helps him relax", "It is expensive", "He must do it", "His mother asks him"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Đọc hiểu: Nam's hobby is gardening. He grows tomatoes and flowers in his backyard every weekend. He says gardening helps him relax. Trả lời: Where does Nam garden?", ["in his backyard", "backyard"]),
                ],
                nang_cao=[
                    tl("Viết một đoạn 4–5 câu về sở thích của bạn bè em.", "Dùng: My friend ... likes ... because ..."),
                ],
            ),
        },

        # ==================== UNIT 2 ====================
        "Unit 2: Health": {
            "Lesson 1: Vocabulary & should/shouldn't": bai(
                ten="Bệnh thường gặp & lời khuyên với should",
                ly_thuyet=(
                    "should (nên) / shouldn't (không nên) + V nguyên mẫu.\n"
                    "VD: You should drink more water. You shouldn't eat too much candy.\n"
                    "Dùng 'I have a ... ' để nói về bệnh: I have a headache / a fever / a cough."
                ),
                tu_vung=[
                    tu("headache", "/ˈhedeɪk/", "danh từ", "đau đầu", "I have a headache.", "Tôi bị đau đầu."),
                    tu("stomachache", "/ˈstʌməkeɪk/", "danh từ", "đau bụng", "She has a stomachache.", "Cô ấy bị đau bụng."),
                    tu("fever", "/ˈfiːvər/", "danh từ", "cơn sốt", "He has a fever.", "Anh ấy bị sốt."),
                    tu("cough", "/kɒf/", "danh từ/động từ", "ho; ho", "She has a bad cough.", "Cô ấy bị ho nặng."),
                    tu("toothache", "/ˈtuːθeɪk/", "danh từ", "đau răng", "I have toothache.", "Tôi bị đau răng."),
                    tu("junk food", "/ˈdʒʌŋk fuːd/", "danh từ", "đồ ăn vặt, đồ ăn nhanh", "Don't eat too much junk food.", "Đừng ăn quá nhiều đồ ăn vặt."),
                    tu("exercise", "/ˈeksərsaɪz/", "danh từ/động từ", "bài tập thể dục; tập thể dục", "I do exercise every morning.", "Tôi tập thể dục mỗi sáng."),
                    tu("balanced diet", "/ˈbælənst ˈdaɪət/", "danh từ", "chế độ ăn cân bằng", "A balanced diet is important.", "Chế độ ăn cân bằng rất quan trọng.", "nang_cao"),
                    tu("vitamin", "/ˈvɪtəmɪn/", "danh từ", "vi-ta-min", "Fruit has many vitamins.", "Trái cây có nhiều vi-ta-min.", "nang_cao"),
                    tu("recover", "/rɪˈkʌvər/", "động từ", "hồi phục", "She will recover soon.", "Cô ấy sẽ sớm hồi phục.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("'Headache' nghĩa là gì?", ["Đau bụng", "Đau đầu", "Sốt", "Đau răng"], 1),
                    cau("You ___ eat too much candy. It's bad for your teeth.", ["should", "shouldn't", "can", "must"], 1),
                    cau("You ___ do exercise every day to stay healthy.", ["shouldn't", "should", "don't", "not"], 1),
                    cau("I have a fever. I ___ see a doctor.", ["should", "shouldn't", "can", "mustn't"], 0, "Lời khuyên nên làm", 2),
                    cau("Which is NOT a healthy habit?", ["Eating vegetables", "Drinking water", "Eating junk food every day", "Doing exercise"], 2, "", 2),
                    cau("'Recover' gần nghĩa nhất với từ nào?", ["get better", "get worse", "get tired", "get up"], 0, "", 3),
                ],
                bai_tap=[
                    bt("Điền should/shouldn't: You ___ (không nên) stay up late.", ["shouldn't"]),
                    bt("Cho lời khuyên: I have a cough. You ___ drink warm water.", ["should"]),
                ],
                nang_cao=[
                    tl("Viết 3 lời khuyên cho bạn bị cảm cúm (dùng should/shouldn't).",
                       "VD: You should rest. You shouldn't go out in the cold."),
                ],
                on_tap=["so_dem"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm đuôi -s/-es và đọc hiểu",
                ly_thuyet=(
                    "Đuôi -s/-es đọc là /s/ (sau âm vô thanh: cooks), /z/ (sau âm hữu thanh: plays),\n"
                    "/ɪz/ (sau âm xì/gió: watches, buses, washes)."
                ),
                tu_vung=[
                    tu("cook", "/kʊk/", "động từ", "nấu ăn", "He cooks dinner.", "Anh ấy nấu bữa tối."),
                    tu("bed", "/bed/", "danh từ", "cái giường", "I go to bed at nine.", "Tôi đi ngủ lúc 9 giờ."),
                    tu("balance", "/ˈbæləns/", "danh từ", "sự cân bằng", "Keep a good balance.", "Hãy giữ sự cân bằng tốt.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("Từ nào có đuôi /ɪz/?", ["cooks", "plays", "watches", "talks"], 2),
                    cau("Từ nào có đuôi /s/?", ["plays", "dogs", "cooks", "buses"], 2),
                    cau("What time does Lan go to bed?", ["9.30 p.m.", "6 a.m.", "9 p.m.", "10 p.m."], 0, "Đọc đoạn văn bên dưới", 2),
                    cau("What does Lan do for 20 minutes?", ["Eats breakfast", "Does exercise", "Goes to school", "Sleeps"], 1, "", 2),
                ],
                bai_tap=[
                    bt("Đọc: Lan gets up at 6 a.m. She does exercise for 20 minutes. She eats a healthy breakfast with eggs and milk. She goes to bed at 9.30 p.m. Hỏi: What does Lan eat for breakfast?", ["eggs and milk", "eggs", "milk"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu về thói quen sống lành mạnh của em.", "Dùng hiện tại đơn và đuôi -s/-es đúng."),
                ],
            ),
        },

        # ==================== UNIT 3 ====================
        "Unit 3: Community Service": {
            "Lesson 1: Vocabulary & Past Simple": bai(
                ten="Hoạt động cộng đồng & quá khứ đơn (động từ có quy tắc)",
                ly_thuyet=(
                    "Quá khứ đơn: V + -ed. VD: clean → cleaned, help → helped, plan → planned (nhân đôi phụ âm).\n"
                    "Dấu hiệu: yesterday, last week, ago, in 2020."
                ),
                tu_vung=[
                    tu("volunteer", "/ˌvɒlənˈtɪər/", "danh từ", "tình nguyện viên", "She is a volunteer.", "Cô ấy là tình nguyện viên."),
                    tu("donate", "/dəʊˈneɪt/", "động từ", "quyên góp, hiến tặng", "We donated books to the library.", "Chúng tôi quyên góp sách cho thư viện."),
                    tu("elderly", "/ˈeldərli/", "tính từ", "cao tuổi, người già", "We help the elderly.", "Chúng tôi giúp người già."),
                    tu("community", "/kəˈmjuːnəti/", "danh từ", "cộng đồng", "Our community is friendly.", "Cộng đồng của chúng tôi thân thiện."),
                    tu("clean up", "/kliːn ʌp/", "cụm động từ", "dọn dẹp", "Let's clean up the park.", "Hãy dọn dẹp công viên."),
                    tu("plant", "/plɑːnt/", "động từ", "trồng (cây)", "We planted trees.", "Chúng tôi đã trồng cây."),
                    tu("charity", "/ˈtʃærəti/", "danh từ", "từ thiện", "She works for charity.", "Cô ấy làm việc từ thiện.", "nang_cao"),
                    tu("shelter", "/ˈʃeltər/", "danh từ", "nơi trú ẩn", "The shelter helps homeless dogs.", "Nơi trú ẩn giúp những chú chó không nhà.", "nang_cao"),
                    tu("contribute", "/kənˈtrɪbjuːt/", "động từ", "đóng góp", "Everyone can contribute to society.", "Ai cũng có thể đóng góp cho xã hội.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("We ___ trees last Sunday.", ["plant", "plants", "planted", "planting"], 2),
                    cau("She ___ money for charity yesterday.", ["donate", "donates", "donated", "donating"], 2),
                    cau("Past form of 'help' is:", ["helps", "helped", "helping", "helpped"], 1),
                    cau("Last week I ___ the park with my class.", ["clean", "cleaned", "cleans", "cleaning"], 1),
                    cau("'Volunteer' nghĩa là gì?", ["Người tình nguyện", "Người già", "Bệnh nhân", "Công nhân"], 0),
                    cau("Quá khứ của 'stop' là:", ["stoped", "stopped", "stopt", "stopping"], 1, "Nhân đôi p trước -ed", 2),
                ],
                bai_tap=[
                    bt("Quá khứ của 'clean' là gì?", ["cleaned"]),
                    bt("Quá khứ của 'study' là gì?", ["studied"], "y → ied"),
                ],
                nang_cao=[
                    tl("Viết 3 câu về một hoạt động tình nguyện em đã làm tuần trước.",
                       "VD: Last week, I cleaned the school yard with my friends."),
                ],
                on_tap=["qk_don_co_quy_tac", "wh_questions"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm đuôi -ed và đọc hiểu",
                ly_thuyet=(
                    "Đuôi -ed đọc là /t/ (sau âm vô thanh: helped), /d/ (sau âm hữu thanh: cleaned), /ɪd/ (sau t, d: wanted, planted)."
                ),
                tu_vung=[
                    tu("visit", "/ˈvɪzɪt/", "động từ", "thăm", "We visited an orphanage.", "Chúng tôi đến thăm một trại trẻ mồ côi."),
                    tu("orphanage", "/ˈɔːfənɪdʒ/", "danh từ", "trại trẻ mồ côi", "The orphanage is near my house.", "Trại trẻ mồ côi ở gần nhà tôi.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("Từ nào có đuôi -ed đọc là /ɪd/?", ["cleaned", "helped", "played", "visited"], 3),
                    cau("Where did Mai's class go?", ["A hospital", "An orphanage", "A school", "A market"], 1, "Đọc đoạn văn bên dưới", 2),
                    cau("What did they do with the children?", ["Played games", "Went shopping", "Studied English", "Sang songs"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Đọc: Mai's class visited an orphanage last month. They cooked lunch, played games with the children and cleaned the yard. Hỏi: What did they cook?", ["lunch"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu kể về một chuyến đi tình nguyện, dùng quá khứ đơn.", "Gợi ý: First, ... Then, ... After that, ... Finally, ..."),
                ],
            ),
        },

        # ==================== UNIT 4 ====================
        "Unit 4: Music and Arts": {
            "Lesson 1: Vocabulary & Comparison": bai(
                ten="Nghệ thuật & so sánh hơn, so sánh nhất",
                ly_thuyet=(
                    "So sánh hơn: tính từ ngắn + er / tính từ dài + more; kèm 'than'.\n"
                    "So sánh nhất: the + tính từ ngắn + est / the most + tính từ dài.\n"
                    "Bất quy tắc: good – better – the best; bad – worse – the worst."
                ),
                tu_vung=[
                    tu("instrument", "/ˈɪnstrəmənt/", "danh từ", "nhạc cụ", "The piano is a musical instrument.", "Đàn piano là một nhạc cụ."),
                    tu("painting", "/ˈpeɪntɪŋ/", "danh từ", "bức tranh", "This painting is beautiful.", "Bức tranh này rất đẹp."),
                    tu("exhibition", "/ˌeksɪˈbɪʃn/", "danh từ", "cuộc triển lãm", "We visited an art exhibition.", "Chúng tôi đã đi xem một cuộc triển lãm nghệ thuật."),
                    tu("artist", "/ˈɑːtɪst/", "danh từ", "họa sĩ, nghệ sĩ", "She is a talented artist.", "Cô ấy là một họa sĩ tài năng."),
                    tu("singer", "/ˈsɪŋər/", "danh từ", "ca sĩ", "He is a famous singer.", "Anh ấy là một ca sĩ nổi tiếng."),
                    tu("talented", "/ˈtæləntɪd/", "tính từ", "có tài năng", "They are talented musicians.", "Họ là những nhạc sĩ tài năng."),
                    tu("orchestra", "/ˈɔːkɪstrə/", "danh từ", "dàn nhạc giao hưởng", "The orchestra plays classical music.", "Dàn nhạc chơi nhạc cổ điển."),
                    tu("traditional", "/trəˈdɪʃənl/", "tính từ", "truyền thống", "Ca trù is traditional music.", "Ca trù là âm nhạc truyền thống.", "nang_cao"),
                    tu("masterpiece", "/ˈmɑːstəpiːs/", "danh từ", "kiệt tác", "Mona Lisa is a masterpiece.", "Mona Lisa là một kiệt tác.", "nang_cao"),
                    tu("creative", "/kriˈeɪtɪv/", "tính từ", "sáng tạo", "Children are very creative.", "Trẻ em rất sáng tạo.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("This song is ___ than that one.", ["interesting", "more interesting", "most interesting", "interestinger"], 1),
                    cau("She is the ___ singer in my class.", ["good", "better", "best", "more good"], 2),
                    cau("Tom is ___ than his brother.", ["taller", "tallest", "more tall", "tall"], 0),
                    cau("Which is the correct superlative of 'beautiful'?", ["the most beautiful", "the more beautiful", "beautifuller", "most beautiful the"], 0),
                    cau("'Good' – 'better' – '___' is the superlative form.", ["the best", "the most good", "the gooder", "the better"], 0, "Bất quy tắc", 2),
                    cau("This painting is ___ masterpiece in the gallery.", ["the most famous", "more famous", "famouser", "the famous"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Cho dạng so sánh hơn của 'big'.", ["bigger"], "Gấp đôi phụ âm g"),
                    bt("Cho dạng so sánh nhất của 'interesting' (the ___).", ["most interesting"]),
                ],
                nang_cao=[
                    tl("Viết 3 câu so sánh hai ca sĩ hoặc hai bức tranh em thích.",
                       "VD: Singer A is more popular than Singer B."),
                ],
                on_tap=["so_sanh_hon", "mau_sac"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phân biệt /ɑː/ và /æ/",
                ly_thuyet="/ɑː/ miệng mở rộng (father, car). /æ/ miệng mở hơn sang hai bên (man, hat).",
                tu_vung=[
                    tu("father", "/ˈfɑːðər/", "danh từ", "bố, cha", "My father plays guitar.", "Bố tôi chơi đàn guitar."),
                    tu("hat", "/hæt/", "danh từ", "cái mũ", "She wears a red hat.", "Cô ấy đội một chiếc mũ đỏ."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /æ/?", ["far", "car", "hat", "park"], 2),
                    cau("Where does Hoa's grandfather paint?", ["In his garden", "In a studio", "At school", "In a shop"], 0, "Đọc đoạn văn bên dưới", 2),
                ],
                bai_tap=[
                    bt("Đọc: Hoa's grandfather is a painter. He paints flowers in his garden every morning. His paintings are beautiful. Hỏi: What does he paint?", ["flowers"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu giới thiệu một nghệ sĩ em yêu thích.", "Dùng so sánh và tính từ mô tả."),
                ],
            ),
        },

        # ==================== UNIT 5 ====================
        "Unit 5: Vietnamese Food and Drink": {
            "Lesson 1: Vocabulary & Countable/Uncountable": bai(
                ten="Ẩm thực Việt & danh từ đếm được / không đếm được",
                ly_thuyet=(
                    "Đếm được: many, a few, a lot of + danh từ số nhiều (eggs, bowls).\n"
                    "Không đếm được: much, a little, some + danh từ (rice, milk).\n"
                    "Câu hỏi/phủ định thường dùng any; câu khẳng định dùng some."
                ),
                tu_vung=[
                    tu("ingredient", "/ɪnˈɡriːdiənt/", "danh từ", "nguyên liệu", "Pho has simple ingredients.", "Phở có nguyên liệu đơn giản."),
                    tu("spicy", "/ˈspaɪsi/", "tính từ", "cay", "This soup is spicy.", "Món súp này cay."),
                    tu("sweet", "/swiːt/", "tính từ", "ngọt", "The mango is sweet.", "Quả xoài rất ngọt."),
                    tu("sour", "/ˈsaʊər/", "tính từ", "chua", "Lemons are sour.", "Chanh thì chua."),
                    tu("salty", "/ˈsɔːlti/", "tính từ", "mặn", "The soup is too salty.", "Món súp quá mặn."),
                    tu("delicious", "/dɪˈlɪʃəs/", "tính từ", "ngon", "Pho is delicious.", "Phở rất ngon."),
                    tu("herb", "/hɜːb/", "danh từ", "rau thơm, thảo mộc", "Add some herbs to the soup.", "Thêm một ít rau thơm vào súp."),
                    tu("spring roll", "/sprɪŋ rəʊl/", "danh từ", "chả giò", "Spring rolls are crispy.", "Chả giò thì giòn."),
                    tu("flavour", "/ˈfleɪvər/", "danh từ", "hương vị", "The flavour is rich.", "Hương vị rất đậm đà.", "nang_cao"),
                    tu("nutritious", "/nuːˈtrɪʃəs/", "tính từ", "bổ dưỡng", "Vegetables are nutritious.", "Rau củ rất bổ dưỡng.", "nang_cao"),
                    tu("cuisine", "/kwɪˈziːn/", "danh từ", "ẩm thực", "Vietnamese cuisine is famous.", "Ẩm thực Việt Nam rất nổi tiếng.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("There is ___ milk in the fridge.", ["some", "many", "a", "few"], 0),
                    cau("There are ___ eggs on the table.", ["much", "many", "little", "some"], 1),
                    cau("I don't have ___ time.", ["many", "much", "few", "a"], 1),
                    cau("Which is uncountable?", ["egg", "rice", "bowl", "chopstick"], 1),
                    cau("'Sour' nghĩa là gì?", ["Ngọt", "Cay", "Chua", "Mặn"], 2),
                    cau("Do you have ___ rice?", ["any", "some", "many", "a"], 0, "Câu hỏi dùng any", 2),
                ],
                bai_tap=[
                    bt("Điền some/any: I need ___ rice for lunch.", ["some"]),
                    bt("Điền much/many: How ___ bowls of pho did you eat?", ["many"]),
                ],
                nang_cao=[
                    tl("Viết 3 câu giới thiệu một món ăn Việt Nam em thích.", "VD: I like bún chả. It is delicious and sweet."),
                ],
                on_tap=["do_an"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phân biệt /ʌ/ và /ɒ/ và đọc hiểu",
                ly_thuyet="/ʌ/ miệng mở vừa (cup, sun). /ɒ/ miệng tròn hơn (hot, shop).",
                tu_vung=[
                    tu("cup", "/kʌp/", "danh từ", "cái cốc, cái tách", "A cup of tea, please.", "Làm ơn cho một tách trà."),
                    tu("shop", "/ʃɒp/", "danh từ", "cửa hàng", "The shop sells noodles.", "Cửa hàng bán mì."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /ʌ/?", ["hot", "cup", "shop", "pot"], 1),
                    cau("What is pho made with?", ["Beef or chicken, rice noodles and herbs", "Fish and bread", "Pizza", "Cake"], 0, "Đọc đoạn văn bên dưới", 2),
                ],
                bai_tap=[
                    bt("Đọc: Pho is a famous Vietnamese dish. It is made with beef or chicken, rice noodles and herbs. Hỏi: Is pho famous? (Yes/No)", ["Yes"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu mô tả cách làm một món ăn đơn giản.", "Dùng First, Then, Finally và mệnh lệnh: Cut, Add, Cook."),
                ],
            ),
        },

        # ==================== UNIT 6 ====================
        "Unit 6: The First University in Vietnam": {
            "Lesson 1: Vocabulary & Irregular Past Simple": bai(
                ten="Lịch sử & quá khứ đơn bất quy tắc",
                ly_thuyet=(
                    "Động từ bất quy tắc cần học thuộc: go–went, have–had, build–built, make–made,\n"
                    "take–took, write–wrote, see–saw, become–became, know–knew.\n"
                    "Dấu hiệu: last summer, in 1070, in the past."
                ),
                tu_vung=[
                    tu("history", "/ˈhɪstəri/", "danh từ", "lịch sử", "I love Vietnamese history.", "Tôi yêu lịch sử Việt Nam."),
                    tu("king", "/kɪŋ/", "danh từ", "vua", "The king built a temple.", "Nhà vua đã xây một ngôi đền."),
                    tu("scholar", "/ˈskɒlər/", "danh từ", "học giả", "He became a famous scholar.", "Ông ấy trở thành một học giả nổi tiếng."),
                    tu("tradition", "/trəˈdɪʃn/", "danh từ", "truyền thống", "Learning is a tradition here.", "Việc học là một truyền thống ở đây."),
                    tu("temple", "/ˈtempl/", "danh từ", "đền, chùa", "We visited a temple.", "Chúng tôi đã đến thăm một ngôi đền."),
                    tu("stele", "/stiːl/", "danh từ", "bia đá", "The stele records graduates' names.", "Bia đá ghi tên những người đỗ đạt.", "nang_cao"),
                    tu("examination", "/ɪɡˌzæmɪˈneɪʃn/", "danh từ", "kỳ thi", "He passed the examination.", "Anh ấy đã đỗ kỳ thi.", "nang_cao"),
                    tu("mandarin", "/ˈmændərɪn/", "danh từ", "quan lại", "Mandarins served the king.", "Quan lại phục vụ nhà vua.", "nang_cao"),
                    tu("dynasty", "/ˈdaɪnəsti/", "danh từ", "triều đại", "The Ly dynasty ruled for a long time.", "Triều Lý trị vì trong thời gian dài.", "nang_cao"),
                    tu("preserve", "/prɪˈzɜːv/", "động từ", "bảo tồn", "We must preserve our heritage.", "Chúng ta phải bảo tồn di sản.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("We ___ to the Temple of Literature last summer.", ["go", "goes", "went", "goed"], 2),
                    cau("King Ly Thanh Tong ___ the Temple of Literature in 1070.", ["build", "built", "builded", "building"], 1),
                    cau("'Scholar' nghĩa là gì?", ["Học giả", "Nông dân", "Công nhân", "Kỹ sư"], 0),
                    cau("The stone stele ___ the names of graduates.", ["record", "recorded", "records", "recording"], 1),
                    cau("She ___ a great time in Hue.", ["have", "has", "had", "haved"], 2, "have → had (bất quy tắc)"),
                    cau("Which is the past form of 'take'?", ["took", "taked", "taken", "takes"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Quá khứ của 'write' là gì?", ["wrote"]),
                    bt("Quá khứ của 'make' là gì?", ["made"]),
                ],
                nang_cao=[
                    tl("Viết 3 câu về một di tích lịch sử em đã thăm.", "VD: Last year, I visited Hue Imperial City. It was amazing."),
                ],
                on_tap=["qk_don_co_quy_tac", "wh_questions"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /θ/ – /ð/ và đọc hiểu",
                ly_thuyet="/θ/ đặt lưỡi giữa hai hàm răng, không rung (think). /ð/ có rung (this, they).",
                tu_vung=[
                    tu("think", "/θɪŋk/", "động từ", "nghĩ", "I think history is interesting.", "Tôi nghĩ lịch sử thú vị."),
                    tu("this", "/ðɪs/", "đại từ/tính từ", "này, cái này", "This temple is old.", "Ngôi đền này rất cũ."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /θ/?", ["this", "that", "think", "they"], 2),
                    cau("When was Quoc Tu Giam founded?", ["1070", "1076", "1075", "1010"], 1, "Đọc đoạn văn bên dưới", 2),
                    cau("Why did students study at Quoc Tu Giam?", ["To become mandarins", "To become singers", "To sell food", "To travel"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Đọc: In 1076, the first university in Vietnam was founded in Hanoi. It was called Quoc Tu Giam. Students studied Confucian classics to become mandarins. Hỏi: What was the university called?", ["Quoc Tu Giam"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu về vai trò của việc học trong lịch sử Việt Nam.", "Dùng quá khứ đơn: ... was founded ... students studied ..."),
                ],
            ),
        },

        # ==================== UNIT 7 ====================
        "Unit 7: Traffic": {
            "Lesson 1: Vocabulary & must/have to": bai(
                ten="Giao thông & must / mustn't / have to",
                ly_thuyet=(
                    "must (bắt buộc, phải) / mustn't (cấm, không được) + V nguyên mẫu.\n"
                    "have to (phải, theo quy định bên ngoài) / don't have to (không cần phải).\n"
                    "VD: You must wear a helmet. You mustn't run across the road. We don't have to pay for the bus."
                ),
                tu_vung=[
                    tu("vehicle", "/ˈviːəkl/", "danh từ", "phương tiện", "A bus is a public vehicle.", "Xe buýt là phương tiện công cộng."),
                    tu("traffic jam", "/ˈtræfɪk dʒæm/", "danh từ", "kẹt xe", "There is a traffic jam.", "Đang kẹt xe."),
                    tu("accident", "/ˈæksɪdənt/", "danh từ", "tai nạn", "The accident was serious.", "Vụ tai nạn rất nghiêm trọng."),
                    tu("helmet", "/ˈhelmɪt/", "danh từ", "mũ bảo hiểm", "Always wear a helmet.", "Luôn đội mũ bảo hiểm."),
                    tu("seatbelt", "/ˈsiːtbelt/", "danh từ", "dây an toàn", "Fasten your seatbelt.", "Hãy thắt dây an toàn."),
                    tu("road sign", "/rəʊd saɪn/", "danh từ", "biển báo giao thông", "Obey the road signs.", "Hãy tuân thủ biển báo giao thông."),
                    tu("pedestrian", "/pəˈdestriən/", "danh từ", "người đi bộ", "Pedestrians use the crossing.", "Người đi bộ dùng vạch qua đường."),
                    tu("traffic light", "/ˈtræfɪk laɪt/", "danh từ", "đèn giao thông", "Stop at the red traffic light.", "Dừng lại khi đèn đỏ."),
                    tu("reckless", "/ˈrekləs/", "tính từ", "liều lĩnh", "Reckless driving causes accidents.", "Lái xe liều lĩnh gây tai nạn.", "nang_cao"),
                    tu("regulation", "/ˌreɡjuˈleɪʃn/", "danh từ", "quy định", "Traffic regulations protect everyone.", "Quy định giao thông bảo vệ mọi người.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("You ___ wear a helmet when riding a motorbike.", ["must", "mustn't", "shouldn't", "can't"], 0),
                    cau("You ___ run across the road.", ["must", "mustn't", "should", "can"], 1),
                    cau("We ___ pay for the bus. It's free.", ["mustn't", "don't have to", "must", "can't"], 1, "don't have to = không cần", 2),
                    cau("'Pedestrian' nghĩa là gì?", ["Người đi bộ", "Tài xế", "Hành khách", "Cảnh sát"], 0),
                    cau("I ___ get up early tomorrow. It's Saturday.", ["don't have to", "mustn't", "must", "have"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Điền must/mustn't: You ___ cross the road when the light is red.", ["mustn't"]),
                    bt("Điền have to: We ___ stop at the red light.", ["have to"]),
                ],
                nang_cao=[
                    tl("Viết 3 luật giao thông em biết, dùng must/mustn't.", "VD: You must stop at the red light."),
                ],
                on_tap=["so_dem"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /ɪ/ – /aɪ/ và đọc hiểu",
                ly_thuyet="/ɪ/ ngắn (ship). /aɪ/ là nguyên âm đôi (drive, light).",
                tu_vung=[
                    tu("drive", "/draɪv/", "động từ", "lái xe", "I drive to school.", "Tôi lái xe đến trường."),
                    tu("light", "/laɪt/", "danh từ", "đèn, ánh sáng", "Turn on the light.", "Bật đèn lên."),
                ],
                cau_hoi=[
                    cau("Từ nào có nguyên âm /aɪ/?", ["drive", "dig", "bus", "bin"], 0),
                    cau("What causes many accidents?", ["Riding fast and not wearing helmets", "Good weather", "New roads", "Too many trees"], 0, "Đọc đoạn văn bên dưới", 2),
                ],
                bai_tap=[
                    bt("Đọc: Every year, many accidents happen because people ride too fast or do not wear helmets. Police officers remind drivers to follow traffic rules. Hỏi: Who reminds drivers to follow rules?", ["Police officers", "police officers"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu về cách đảm bảo an toàn khi đi xe đạp đến trường.", "Dùng must/mustn't và have to."),
                ],
            ),
        },

        # ==================== UNIT 8 ====================
        "Unit 8: Films": {
            "Lesson 1: Vocabulary & Will Future": bai(
                ten="Phim ảnh & thì tương lai đơn (will)",
                ly_thuyet=(
                    "will + V nguyên mẫu: dự đoán, quyết định ngay lúc nói.\n"
                    "VD: I think it will be exciting. Oh, I'll watch it tonight.\n"
                    "be going to: dự định đã có trước, hoặc dấu hiệu rõ ràng (It is going to rain)."
                ),
                tu_vung=[
                    tu("genre", "/ˈʒɑːnrə/", "danh từ", "thể loại", "Comedy is my favourite genre.", "Hài là thể loại yêu thích của tôi."),
                    tu("actor", "/ˈæktər/", "danh từ", "diễn viên nam", "He is a good actor.", "Anh ấy là một diễn viên giỏi."),
                    tu("actress", "/ˈæktrəs/", "danh từ", "diễn viên nữ", "She is a famous actress.", "Cô ấy là một nữ diễn viên nổi tiếng."),
                    tu("director", "/dəˈrektər/", "danh từ", "đạo diễn", "The director is very creative.", "Đạo diễn rất sáng tạo."),
                    tu("exciting", "/ɪkˈsaɪtɪŋ/", "tính từ", "thú vị, hào hứng", "The film is exciting.", "Bộ phim rất hấp dẫn."),
                    tu("boring", "/ˈbɔːrɪŋ/", "tính từ", "nhàm chán", "The movie is boring.", "Bộ phim thật nhàm chán."),
                    tu("scary", "/ˈskeəri/", "tính từ", "đáng sợ", "A horror film is scary.", "Phim kinh dị rất đáng sợ."),
                    tu("documentary", "/ˌdɒkjuˈmentri/", "danh từ", "phim tài liệu", "I like nature documentaries.", "Tôi thích phim tài liệu thiên nhiên."),
                    tu("plot", "/plɒt/", "danh từ", "cốt truyện", "The plot is very simple.", "Cốt truyện rất đơn giản.", "nang_cao"),
                    tu("sequel", "/ˈsiːkwəl/", "danh từ", "phần tiếp theo", "There will be a sequel next year.", "Năm sau sẽ có phần tiếp theo.", "nang_cao"),
                    tu("review", "/rɪˈvjuː/", "danh từ", "bài đánh giá, nhận xét", "I wrote a review of the film.", "Tôi đã viết một bài nhận xét về bộ phim.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("I think the film ___ exciting tomorrow.", ["will be", "is be", "be will", "will is"], 0),
                    cau("Look at those dark clouds! It ___ rain.", ["will", "is going to", "goes", "rained"], 1, "Có dấu hiệu rõ ràng → be going to", 2),
                    cau("'Director' nghĩa là gì?", ["Đạo diễn", "Diễn viên", "Ca sĩ", "Nhà văn"], 0),
                    cau("Which is a genre of film?", ["Horror", "Director", "Actor", "Plot"], 0),
                    cau("Oh, the phone is ringing. I ___ answer it.", ["will", "am going to", "am", "was"], 0, "Quyết định ngay lúc nói → will", 2),
                ],
                bai_tap=[
                    bt("I think he ___ (win) the match.", ["will win"]),
                    bt("Look at the sky! It ___ (rain) soon.", ["is going to rain"]),
                ],
                nang_cao=[
                    tl("Viết đánh giá ngắn 3 câu về một bộ phim em đã xem.", "Dùng: The plot is... The actors are... I think it is..."),
                ],
                on_tap=["to_be", "so_sanh_hon"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /ɜː/ và đọc hiểu",
                ly_thuyet="/ɜː/ là âm 'ơ' kéo dài: girl, learn, word, bird.",
                tu_vung=[
                    tu("bird", "/bɜːd/", "danh từ", "con chim", "A bird is flying.", "Một con chim đang bay."),
                    tu("learn", "/lɜːn/", "động từ", "học", "I learn English every day.", "Tôi học tiếng Anh mỗi ngày."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /ɜː/?", ["bird", "bored", "bear", "bar"], 0),
                    cau("What genre is the movie?", ["Comedy", "Horror", "Documentary", "Cartoon"], 0, "Đọc đoạn văn bên dưới", 2),
                ],
                bai_tap=[
                    bt("Đọc: The new movie is a funny comedy. The plot is simple, but the actors are great. Many people say it is a must-see. Hỏi: Is the plot complicated? (Yes/No)", ["No"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu giới thiệu bộ phim hoạt hình bạn thích.", "Dùng will và tính từ mô tả cảm xúc."),
                ],
            ),
        },

        # ==================== UNIT 9 ====================
        "Unit 9: Festivals Around the World": {
            "Lesson 1: Vocabulary & Future Plans": bai(
                ten="Lễ hội thế giới & kế hoạch tương lai",
                ly_thuyet=(
                    "Hiện tại tiếp diễn chỉ kế hoạch đã sắp xếp: be + V-ing (We are travelling to Hue next week).\n"
                    "be going to + V: dự định. VD: I am going to visit my grandparents."
                ),
                tu_vung=[
                    tu("celebrate", "/ˈselɪbreɪt/", "động từ", "ăn mừng", "We celebrate Tet in February.", "Chúng tôi ăn Tết vào tháng Hai."),
                    tu("tradition", "/trəˈdɪʃn/", "danh từ", "truyền thống", "It is a family tradition.", "Đó là truyền thống gia đình."),
                    tu("costume", "/ˈkɒstjuːm/", "danh từ", "trang phục", "People wear colourful costumes.", "Mọi người mặc trang phục sặc sỡ."),
                    tu("firework", "/ˈfaɪəwɜːk/", "danh từ", "pháo hoa", "We watched the fireworks.", "Chúng tôi xem pháo hoa."),
                    tu("parade", "/pəˈreɪd/", "danh từ", "cuộc diễu hành", "There is a big parade.", "Có một cuộc diễu hành lớn."),
                    tu("festival", "/ˈfestɪvl/", "danh từ", "lễ hội", "Mid-Autumn is a festival for children.", "Tết Trung Thu là lễ hội của trẻ em."),
                    tu("lantern", "/ˈlæntərn/", "danh từ", "đèn lồng", "Children carry lanterns.", "Trẻ em cầm đèn lồng."),
                    tu("feast", "/fiːst/", "danh từ", "bữa tiệc lớn", "The village held a feast.", "Cả làng tổ chức một bữa tiệc.", "nang_cao"),
                    tu("ceremony", "/ˈserəməni/", "danh từ", "nghi lễ", "The opening ceremony was beautiful.", "Lễ khai mạc rất đẹp.", "nang_cao"),
                    tu("procession", "/prəˈseʃn/", "danh từ", "đám rước", "A procession passed through the street.", "Một đám rước đi qua con phố.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("We ___ to Hue this summer.", ["travel", "are travelling", "travels", "travelled"], 1, "Kế hoạch đã sắp xếp"),
                    cau("She ___ her grandparents next week.", ["visit", "visits", "is visiting", "visited"], 2),
                    cau("'Lantern' nghĩa là gì?", ["Đèn lồng", "Pháo hoa", "Trang phục", "Bữa tiệc"], 0),
                    cau("Which is a festival in Vietnam?", ["Mid-Autumn Festival", "Halloween", "Christmas", "Thanksgiving"], 0),
                    cau("They ___ going to celebrate their harvest festival next month.", ["are", "is", "am", "be"], 0, "They + are", 2),
                ],
                bai_tap=[
                    bt("Diễn tả kế hoạch: I ___ (go) to the park tomorrow.", ["am going"]),
                    bt("Diễn tả dự định: They ___ (celebrate) Tet next month.", ["are going to celebrate"]),
                ],
                nang_cao=[
                    tl("Viết 3 câu về kế hoạch cho lễ hội sắp tới của em.", "VD: We are going to have a big party."),
                ],
                on_tap=["thoi_tiet", "hien_tai_don"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /tʃ/ – /dʒ/ và đọc hiểu",
                ly_thuyet="/tʃ/ như 'ch' tiếng Việt (cheese). /dʒ/ như 'd' + 'ж' (jeans, jump).",
                tu_vung=[
                    tu("cheese", "/tʃiːz/", "danh từ", "phô mai", "I like cheese.", "Tôi thích phô mai."),
                    tu("jump", "/dʒʌmp/", "động từ", "nhảy", "Children jump in the water.", "Trẻ em nhảy xuống nước."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /dʒ/?", ["cheese", "jump", "chair", "chin"], 1),
                    cau("When is Songkran?", ["April", "July", "December", "October"], 0, "Đọc đoạn văn bên dưới", 2),
                    cau("What do people do during Songkran?", ["Splash water", "Fly kites", "Eat cakes", "Sing"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Đọc: Thailand's Songkran festival is in April. People splash water on each other to wish for good luck. Hỏi: Why do people splash water?", ["to wish for good luck", "good luck"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu về một lễ hội nước ngoài mà em biết.", "Dùng: It is celebrated in... People... It is important because..."),
                ],
            ),
        },

        # ==================== UNIT 10 ====================
        "Unit 10: Sources of Energy": {
            "Lesson 1: Vocabulary & First Conditional": bai(
                ten="Nguồn năng lượng & câu điều kiện loại 1",
                ly_thuyet=(
                    "Câu điều kiện loại 1 (có thật ở tương lai): If + hiện tại đơn, will + V.\n"
                    "VD: If we save electricity, we will save money.\n"
                    "Lưu ý: mệnh đề If KHÔNG dùng will (không nói 'If we will save')."
                ),
                tu_vung=[
                    tu("renewable", "/rɪˈnjuːəbl/", "tính từ", "tái tạo được", "Solar energy is renewable.", "Năng lượng mặt trời có thể tái tạo."),
                    tu("solar energy", "/ˈsəʊlə ˈenədʒi/", "danh từ", "năng lượng mặt trời", "We use solar energy at home.", "Chúng tôi dùng năng lượng mặt trời ở nhà."),
                    tu("wind power", "/wɪnd ˈpaʊər/", "danh từ", "điện gió", "Wind power is clean.", "Điện gió rất sạch."),
                    tu("electricity", "/ɪˌlekˈtrɪsəti/", "danh từ", "điện", "Don't waste electricity.", "Đừng lãng phí điện."),
                    tu("save", "/seɪv/", "động từ", "tiết kiệm", "Save water every day.", "Hãy tiết kiệm nước mỗi ngày."),
                    tu("waste", "/weɪst/", "động từ", "lãng phí", "Don't waste food.", "Đừng lãng phí thức ăn."),
                    tu("fossil fuel", "/ˈfɒsl fjuːəl/", "danh từ", "nhiên liệu hóa thạch", "Coal is a fossil fuel.", "Than đá là nhiên liệu hóa thạch."),
                    tu("hydropower", "/ˈhaɪdrəpaʊər/", "danh từ", "thủy điện", "Hydropower comes from rivers.", "Thủy điện đến từ sông.", "nang_cao"),
                    tu("sustainable", "/səˈsteɪnəbl/", "tính từ", "bền vững", "We need sustainable energy.", "Chúng ta cần năng lượng bền vững.", "nang_cao"),
                    tu("emission", "/ɪˈmɪʃn/", "danh từ", "khí thải", "Cars cause carbon emissions.", "Xe cộ gây ra khí thải carbon.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("If we ___ less electricity, we will save money.", ["use", "uses", "used", "using"], 0),
                    cau("If it rains, we ___ at home.", ["stay", "will stay", "stayed", "staying"], 1),
                    cau("'Renewable' nghĩa là gì?", ["Tái tạo được", "Hết sạch", "Độc hại", "Vĩnh viễn"], 0),
                    cau("Which is a renewable source?", ["Solar energy", "Coal", "Oil", "Natural gas"], 0),
                    cau("If you study hard, you ___ pass the exam.", ["will", "would", "pass", "passed"], 0, "Mệnh đề chính: will + V", 2),
                    cau("If the sun ___ bright, we will use solar panels.", ["is", "will be", "was", "be"], 0, "If + hiện tại đơn", 3),
                ],
                bai_tap=[
                    bt("Điền: If you study hard, you ___ (pass) the exam.", ["will pass"]),
                    bt("Điền: If we turn off the lights, we ___ (save) electricity.", ["will save"]),
                ],
                nang_cao=[
                    tl("Viết 2 câu điều kiện loại 1 về bảo vệ môi trường.", "VD: If we plant more trees, the air will be cleaner."),
                ],
                on_tap=["hien_tai_don", "thoi_tiet"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /z/ và đọc hiểu",
                ly_thuyet="/z/ là âm 'd' nhẹ có rung: zoo, wise, lazy.",
                tu_vung=[
                    tu("zoo", "/zuː/", "danh từ", "sở thú", "We went to the zoo.", "Chúng tôi đi sở thú."),
                    tu("panel", "/ˈpænl/", "danh từ", "tấm pin, tấm bảng", "Solar panels are on the roof.", "Các tấm pin mặt trời ở trên mái nhà."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /z/ ở đầu?", ["zoo", "sun", "cat", "fish"], 0),
                    cau("What can solar panels produce?", ["Electricity", "Water", "Food", "Cars"], 0, "Đọc đoạn văn bên dưới", 2),
                ],
                bai_tap=[
                    bt("Đọc: Solar panels on the roof can produce electricity from sunlight. If more families use them, the air will be cleaner. Hỏi: What will happen if more families use them?", ["the air will be cleaner", "air will be cleaner"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu về cách gia đình em tiết kiệm năng lượng.", "Dùng câu điều kiện loại 1."),
                ],
            ),
        },

        # ==================== UNIT 11 ====================
        "Unit 11: Travelling in the Future": {
            "Lesson 1: Vocabulary & might / will be able to": bai(
                ten="Du lịch tương lai & might / will be able to",
                ly_thuyet=(
                    "might + V: có thể (không chắc chắn). VD: We might travel by flying cars.\n"
                    "will be able to + V: sẽ có khả năng. VD: Robots will be able to clean our houses."
                ),
                tu_vung=[
                    tu("invention", "/ɪnˈvenʃn/", "danh từ", "phát minh", "The car is an invention.", "Ô tô là một phát minh."),
                    tu("aircraft", "/ˈeəkrɑːft/", "danh từ", "máy bay", "An aircraft flies in the sky.", "Máy bay bay trên bầu trời."),
                    tu("solar-powered", "/ˈsəʊlə ˈpaʊəd/", "tính từ", "chạy bằng năng lượng mặt trời", "A solar-powered car is clean.", "Ô tô chạy bằng năng lượng mặt trời rất sạch."),
                    tu("pilot", "/ˈpaɪlət/", "danh từ", "phi công", "The pilot is very skilled.", "Phi công rất giỏi nghề."),
                    tu("journey", "/ˈdʒɜːni/", "danh từ", "hành trình", "The journey took five hours.", "Hành trình kéo dài năm giờ."),
                    tu("passenger", "/ˈpæsɪndʒər/", "danh từ", "hành khách", "Passengers must wear seatbelts.", "Hành khách phải thắt dây an toàn."),
                    tu("spacecraft", "/ˈspeɪskrɑːft/", "danh từ", "tàu vũ trụ", "The spacecraft went to the Moon.", "Tàu vũ trụ đã bay tới Mặt Trăng.", "nang_cao"),
                    tu("transport", "/ˈtrænspɔːt/", "danh từ/động từ", "vận tải; vận chuyển", "Public transport is important.", "Giao thông công cộng rất quan trọng.", "nang_cao"),
                    tu("technology", "/tekˈnɒlədʒi/", "danh từ", "công nghệ", "New technology changes our lives.", "Công nghệ mới thay đổi cuộc sống.", "nang_cao"),
                    tu("underwater", "/ˌʌndəˈwɔːtər/", "tính từ/trạng từ", "dưới nước", "An underwater tunnel connects two cities.", "Một đường hầm dưới nước nối hai thành phố.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("In the future, we ___ travel by flying cars.", ["might", "must", "should", "are"], 0),
                    cau("Robots ___ help us do housework.", ["will be able to", "can to", "able to", "will can"], 0),
                    cau("I'm not sure. It ___ be sunny tomorrow.", ["might", "must", "should", "can't"], 0, "Không chắc chắn → might", 2),
                    cau("'Passenger' nghĩa là gì?", ["Hành khách", "Phi công", "Tài xế", "Du khách"], 0),
                    cau("Scientists think people ___ live on Mars one day.", ["might", "mustn't", "have to", "were"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Điền might/will be able to: In 2100, people ___ (live) on Mars.", ["might live"]),
                    bt("Điền: Students ___ (learn) online in the future.", ["will be able to learn"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 3–4 câu về thành phố của tương lai.", "Dùng might và will be able to."),
                ],
                on_tap=["to_be"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /ɔː/ – /ɒ/ và đọc hiểu",
                ly_thuyet="/ɔː/ môi tròn, kéo dài (law, door). /ɒ/ môi tròn, ngắn (lot, hot).",
                tu_vung=[
                    tu("law", "/lɔː/", "danh từ", "luật pháp", "Obey the law.", "Hãy tuân thủ pháp luật."),
                    tu("lot", "/lɒt/", "đại từ", "rất nhiều", "There are a lot of cars.", "Có rất nhiều xe."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /ɔː/?", ["lot", "law", "hot", "dog"], 1),
                    cau("What might trains do in the future?", ["Travel under the sea", "Fly", "Stop working", "Run on water"], 0, "Đọc đoạn văn bên dưới", 2),
                    cau("What do scientists believe?", ["People will be able to visit the Moon", "Cars will disappear", "People will stop travelling", "Trains will be slow"], 0, "", 2),
                ],
                bai_tap=[
                    bt("Đọc: In the future, cars may run on solar power. Trains might travel under the sea. Scientists believe that people will be able to visit the Moon for holidays. Hỏi: What may cars run on?", ["solar power"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu dự đoán về một phương tiện tương lai.", "Dùng might và will be able to."),
                ],
            ),
        },

        # ==================== UNIT 12 ====================
        "Unit 12: An Overcrowded World": {
            "Lesson 1: Vocabulary & fewer / less / more": bai(
                ten="Thế giới đông đúc & fewer / less / more",
                ly_thuyet=(
                    "fewer + danh từ đếm được; less + danh từ không đếm được; more + cả hai.\n"
                    "too many + đếm được; too much + không đếm được.\n"
                    "VD: There are fewer cars in the countryside. There is less pollution."
                ),
                tu_vung=[
                    tu("overcrowded", "/ˌəʊvəˈkraʊdɪd/", "tính từ", "quá đông đúc", "The city is overcrowded.", "Thành phố quá đông đúc."),
                    tu("population", "/ˌpɒpjuˈleɪʃn/", "danh từ", "dân số", "The population of Vietnam is large.", "Dân số Việt Nam rất đông."),
                    tu("slum", "/slʌm/", "danh từ", "khu ổ chuột", "Some families live in slums.", "Một số gia đình sống trong khu ổ chuột."),
                    tu("healthcare", "/ˈhelθkeə/", "danh từ", "chăm sóc sức khỏe", "Good healthcare is important.", "Chăm sóc sức khỏe tốt rất quan trọng."),
                    tu("education", "/ˌedʒuˈkeɪʃn/", "danh từ", "giáo dục", "Education helps children.", "Giáo dục giúp trẻ em phát triển."),
                    tu("shortage", "/ˈʃɔːtɪdʒ/", "danh từ", "sự thiếu hụt", "There is a shortage of water.", "Đang thiếu nước."),
                    tu("pollution", "/pəˈluːʃn/", "danh từ", "ô nhiễm", "Pollution is a serious problem.", "Ô nhiễm là vấn đề nghiêm trọng."),
                    tu("housing", "/ˈhaʊzɪŋ/", "danh từ", "nhà ở", "Housing is expensive in the city.", "Nhà ở ở thành phố rất đắt đỏ."),
                    tu("urbanisation", "/ˌɜːbənaɪˈzeɪʃn/", "danh từ", "đô thị hóa", "Urbanisation is growing fast.", "Đô thị hóa đang phát triển nhanh.", "nang_cao"),
                    tu("congestion", "/kənˈdʒestʃən/", "danh từ", "tắc nghẽn", "Traffic congestion wastes time.", "Tắc nghẽn giao thông làm lãng phí thời gian.", "nang_cao"),
                ],
                cau_hoi=[
                    cau("There are ___ cars in the countryside than in the city.", ["fewer", "less", "much", "little"], 0, "cars đếm được → fewer"),
                    cau("There is ___ pollution in the countryside.", ["fewer", "less", "many", "few"], 1, "pollution không đếm được → less"),
                    cau("We need ___ schools in the poor areas.", ["much", "more", "fewer", "less"], 1),
                    cau("'Shortage' nghĩa là gì?", ["Sự thiếu hụt", "Sự dư thừa", "Sự tăng trưởng", "Sự giàu có"], 0),
                    cau("There are too ___ people in the city.", ["much", "many", "few", "little"], 1),
                    cau("There is ___ water in the desert than in the river.", ["less", "fewer", "many", "few"], 0, "water không đếm được", 2),
                ],
                bai_tap=[
                    bt("Điền fewer/less: There is ___ water in summer.", ["less"]),
                    bt("Điền fewer/less: There are ___ trees now than before.", ["fewer"]),
                ],
                nang_cao=[
                    tl("Viết 3–4 câu về một vấn đề của thành phố đông dân và đề xuất giải pháp.", "VD: There are too many motorbikes. We should use public transport."),
                ],
                on_tap=["so_sanh_hon", "do_an"],
            ),
            "Lesson 2: Pronunciation & Reading": bai(
                ten="Phát âm /ʃ/ – /tʃ/ và đọc hiểu",
                ly_thuyet="/ʃ/ như 'sh' (shop, ship). /tʃ/ như 'ch' (chop, cheese).",
                tu_vung=[
                    tu("shop", "/ʃɒp/", "danh từ", "cửa hàng", "The shop is open.", "Cửa hàng đang mở cửa."),
                    tu("chop", "/tʃɒp/", "động từ", "băm, chặt", "Chop the vegetables.", "Hãy băm rau củ."),
                ],
                cau_hoi=[
                    cau("Từ nào có âm /ʃ/?", ["chop", "shop", "cheese", "chair"], 1),
                    cau("What is one problem of the big city in the passage?", ["Overcrowding", "Too few people", "Clean air", "Empty roads"], 0, "Đọc đoạn văn bên dưới", 2),
                ],
                bai_tap=[
                    bt("Đọc: Big cities are overcrowded, so there is more pollution and traffic congestion. Hỏi: Why is there more pollution? (Vì sao?)", ["because cities are overcrowded", "overcrowded"]),
                ],
                nang_cao=[
                    tl("Viết đoạn 4 câu đề xuất giải pháp giảm ô nhiễm ở thành phố.", "Dùng less, fewer, more và should."),
                ],
            ),
        },
    }
}


# ============================================================
# 3. TỪ ĐIỂN ANH–VIỆT OFFLINE
#    Gộp: (a) từ cơ bản dưới đây + (b) toàn bộ từ vựng của 12 Unit
# ============================================================
_TU_CO_BAN = [
    tu("hello", "/həˈləʊ/", "thán từ", "xin chào", "Hello, nice to meet you.", "Xin chào, rất vui được gặp bạn."),
    tu("goodbye", "/ˌɡʊdˈbaɪ/", "thán từ", "tạm biệt", "Goodbye! See you tomorrow.", "Tạm biệt! Hẹn gặp lại ngày mai."),
    tu("school", "/skuːl/", "danh từ", "trường học", "I go to school by bike.", "Tôi đi học bằng xe đạp."),
    tu("teacher", "/ˈtiːtʃər/", "danh từ", "giáo viên", "My teacher is very kind.", "Cô giáo của tôi rất tốt bụng."),
    tu("student", "/ˈstjuːdnt/", "danh từ", "học sinh, sinh viên", "She is a good student.", "Cô ấy là một học sinh giỏi."),
    tu("book", "/bʊk/", "danh từ", "quyển sách", "I am reading a book.", "Tôi đang đọc một cuốn sách."),
    tu("friend", "/frend/", "danh từ", "bạn bè", "He is my best friend.", "Anh ấy là bạn thân nhất của tôi."),
    tu("family", "/ˈfæməli/", "danh từ", "gia đình", "There are four people in my family.", "Gia đình tôi có bốn người."),
    tu("happy", "/ˈhæpi/", "tính từ", "vui vẻ, hạnh phúc", "I feel very happy today.", "Hôm nay tôi cảm thấy rất vui."),
    tu("sad", "/sæd/", "tính từ", "buồn", "She looks sad.", "Cô ấy trông có vẻ buồn."),
    tu("big", "/bɪɡ/", "tính từ", "to, lớn", "This is a big house.", "Đây là một ngôi nhà lớn."),
    tu("small", "/smɔːl/", "tính từ", "nhỏ", "I have a small cat.", "Tôi có một chú mèo nhỏ."),
    tu("run", "/rʌn/", "động từ", "chạy", "I run every morning.", "Tôi chạy bộ mỗi sáng."),
    tu("eat", "/iːt/", "động từ", "ăn", "We eat rice every day.", "Chúng tôi ăn cơm hàng ngày."),
    tu("drink", "/drɪŋk/", "động từ", "uống", "I drink milk every morning.", "Tôi uống sữa mỗi sáng."),
    tu("play", "/pleɪ/", "động từ", "chơi", "They play football after school.", "Họ chơi bóng đá sau giờ học."),
    tu("study", "/ˈstʌdi/", "động từ", "học", "I study English every day.", "Tôi học tiếng Anh mỗi ngày."),
    tu("water", "/ˈwɔːtər/", "danh từ", "nước", "Drink a lot of water.", "Hãy uống nhiều nước."),
    tu("food", "/fuːd/", "danh từ", "thức ăn", "Vietnamese food is delicious.", "Đồ ăn Việt Nam rất ngon."),
    tu("city", "/ˈsɪti/", "danh từ", "thành phố", "Hanoi is the capital city.", "Hà Nội là thủ đô."),
    tu("country", "/ˈkʌntri/", "danh từ", "đất nước", "Vietnam is a beautiful country.", "Việt Nam là một đất nước đẹp."),
    tu("morning", "/ˈmɔːnɪŋ/", "danh từ", "buổi sáng", "I get up early in the morning.", "Tôi dậy sớm vào buổi sáng."),
    tu("evening", "/ˈiːvnɪŋ/", "danh từ", "buổi tối", "We watch TV in the evening.", "Chúng tôi xem TV vào buổi tối."),
    tu("old", "/əʊld/", "tính từ", "già, cũ", "My grandfather is 70 years old.", "Ông tôi năm nay 70 tuổi."),
    tu("new", "/njuː/", "tính từ", "mới", "I have a new pen.", "Tôi có một cây bút mới."),
    tu("good", "/ɡʊd/", "tính từ", "tốt, giỏi", "She is good at Math.", "Cô ấy học Toán giỏi."),
    tu("bad", "/bæd/", "tính từ", "xấu, kém", "Smoking is bad for health.", "Hút thuốc có hại cho sức khỏe."),
    tu("hot", "/hɒt/", "tính từ", "nóng (thời tiết, nhiệt độ)", "It is hot in summer.", "Trời nóng vào mùa hè."),
    tu("cold", "/kəʊld/", "tính từ", "lạnh", "It is cold in winter.", "Trời lạnh vào mùa đông."),
    tu("beautiful", "/ˈbjuːtɪfl/", "tính từ", "đẹp", "The garden is beautiful.", "Khu vườn thật đẹp."),
    tu("interesting", "/ˈɪntrəstɪŋ/", "tính từ", "thú vị", "This book is very interesting.", "Cuốn sách này rất thú vị."),
    tu("difficult", "/ˈdɪfɪkəlt/", "tính từ", "khó", "Math is difficult for me.", "Môn Toán khó với tôi."),
    tu("important", "/ɪmˈpɔːtnt/", "tính từ", "quan trọng", "English is very important.", "Tiếng Anh rất quan trọng."),
]

TU_DIEN = {}
for _t in _TU_CO_BAN:
    TU_DIEN[_t["tu"].lower()] = _t

for _unit, _lessons in ANH["Lớp 7"].items():
    for _ls in _lessons.values():
        for _t in _ls["tu_vung"]:
            TU_DIEN.setdefault(_t["tu"].lower(), _t)


# ============================================================
# 4. TỪ NÂNG CAO CỦA NGÀY (cho học sinh khá, giỏi)
# ============================================================
DS_TU_NANG_CAO = [
    tu("adventure", "/ədˈventʃər/", "danh từ", "cuộc phiêu lưu", "A trip to the forest is an adventure.", "Chuyến đi rừng là một cuộc phiêu lưu.", "nang_cao"),
    tu("brilliant", "/ˈbrɪliənt/", "tính từ", "tuyệt vời, rực rỡ", "That was a brilliant idea.", "Đó là một ý tưởng tuyệt vời.", "nang_cao"),
    tu("curious", "/ˈkjʊəriəs/", "tính từ", "tò mò", "Children are curious about everything.", "Trẻ em tò mò về mọi thứ.", "nang_cao"),
    tu("diligent", "/ˈdɪlɪdʒənt/", "tính từ", "chăm chỉ", "She is a diligent student.", "Cô ấy là học sinh chăm chỉ.", "nang_cao"),
    tu("enormous", "/ɪˈnɔːməs/", "tính từ", "khổng lồ", "The whale is enormous.", "Con cá voi khổng lồ.", "nang_cao"),
    tu("fascinating", "/ˈfæsɪneɪtɪŋ/", "tính từ", "hấp dẫn, lôi cuốn", "The history lesson was fascinating.", "Bài học lịch sử rất hấp dẫn.", "nang_cao"),
    tu("generous", "/ˈdʒenərəs/", "tính từ", "hào phóng", "He is generous with his time.", "Anh ấy hào phóng với thời gian của mình.", "nang_cao"),
    tu("harmony", "/ˈhɑːməni/", "danh từ", "sự hài hòa", "Music creates harmony.", "Âm nhạc tạo nên sự hài hòa.", "nang_cao"),
    tu("imagine", "/ɪˈmædʒɪn/", "động từ", "tưởng tượng", "Imagine a city without cars.", "Hãy tưởng tượng một thành phố không có xe hơi.", "nang_cao"),
    tu("knowledge", "/ˈnɒlɪdʒ/", "danh từ", "kiến thức", "Knowledge is power.", "Kiến thức là sức mạnh.", "nang_cao"),
    tu("language", "/ˈlæŋɡwɪdʒ/", "danh từ", "ngôn ngữ", "English is an international language.", "Tiếng Anh là ngôn ngữ quốc tế.", "nang_cao"),
    tu("patience", "/ˈpeɪʃns/", "danh từ", "sự kiên nhẫn", "Learning a language needs patience.", "Học ngôn ngữ cần sự kiên nhẫn.", "nang_cao"),
    tu("confident", "/ˈkɒnfɪdənt/", "tính từ", "tự tin", "Speak clearly and be confident.", "Hãy nói rõ ràng và tự tin.", "nang_cao"),
    tu("determined", "/dɪˈtɜːmɪnd/", "tính từ", "quyết tâm", "She is determined to win.", "Cô ấy quyết tâm giành chiến thắng.", "nang_cao"),
    tu("essential", "/ɪˈsenʃl/", "tính từ", "thiết yếu", "Water is essential for life.", "Nước thiết yếu cho sự sống.", "nang_cao"),
    tu("gratitude", "/ˈɡrætɪtjuːd/", "danh từ", "lòng biết ơn", "I express my gratitude to my teachers.", "Tôi bày tỏ lòng biết ơn tới thầy cô.", "nang_cao"),
    tu("inspire", "/ɪnˈspaɪər/", "động từ", "truyền cảm hứng", "Great teachers inspire students.", "Những thầy cô giỏi truyền cảm hứng cho học sinh.", "nang_cao"),
    tu("persuade", "/pərˈsweɪd/", "động từ", "thuyết phục", "He tried to persuade us to join.", "Anh ấy cố thuyết phục chúng tôi tham gia.", "nang_cao"),
    tu("reliable", "/rɪˈlaɪəbl/", "tính từ", "đáng tin cậy", "This dictionary is reliable.", "Cuốn từ điển này đáng tin cậy.", "nang_cao"),
    tu("tolerate", "/ˈtɒləreɪt/", "động từ", "khoan dung, chịu đựng", "We should tolerate different opinions.", "Chúng ta nên khoan dung với ý kiến khác nhau.", "nang_cao"),
    tu("vivid", "/ˈvɪvɪd/", "tính từ", "sinh động, rõ nét", "She has a vivid imagination.", "Cô ấy có trí tưởng tượng sinh động.", "nang_cao"),
]


# ============================================================
# 5. CÁC HÀM TIỆN ÍCH
# ============================================================
def tra_tu_offline(tu_khoa):
    """Tra từ tức thì. Nếu gõ sai, trả về danh sách từ gần đúng."""
    k = tu_khoa.strip().lower()
    if k in TU_DIEN:
        return TU_DIEN[k]
    goi_y = difflib.get_close_matches(k, list(TU_DIEN.keys()), n=3, cutoff=0.6)
    return {"khong_tim_thay": True, "goi_y": goi_y}


def tu_cua_ngay(ngay=None):
    """Trả về một từ nâng cao, mỗi ngày một từ (cố định theo ngày)."""
    ngay = ngay or datetime.date.today()
    return DS_TU_NANG_CAO[ngay.toordinal() % len(DS_TU_NANG_CAO)]


def _tat_ca_cau_hoi(unit=None):
    pool = []
    for ten_unit, lessons in ANH["Lớp 7"].items():
        if unit and ten_unit != unit:
            continue
        for ls in lessons.values():
            pool.extend(ls["cau_hoi"])
    return pool


def tao_de(so_cau=10, unit=None, seed=None):
    """
    Sinh đề trắc nghiệm ngẫu nhiên. Đáp án được xáo trộn nhưng vẫn đúng.
    unit: lấy câu hỏi từ một Unit cụ thể (None = tất cả).
    seed: số ngẫu nhiên cố định để tạo lại cùng một đề.
    """
    rng = random.Random(seed)
    pool = _tat_ca_cau_hoi(unit)
    chon = rng.sample(pool, min(so_cau, len(pool)))
    de = []
    for c in chon:
        da = c["da"][:]
        dung = da[c["d"]]
        thu_tu = list(range(len(da)))
        rng.shuffle(thu_tu)
        da_moi = [da[k] for k in thu_tu]
        de.append({"nd": c["nd"], "da": da_moi, "d": da_moi.index(dung),
                   "gt": c["gt"], "kho": c["kho"]})
    return de


def kiem_tra_du_lieu():
    """Kiểm tra lỗi dữ liệu. Trả về danh sách lỗi (rỗng nếu không có lỗi)."""
    loi = []
    nguon = list(_tat_ca_cau_hoi())
    for kt in KIEN_THUC_NEN.values():
        nguon.extend(kt["cau_hoi"])
    for c in nguon:
        if not (0 <= c["d"] < len(c["da"])):
            loi.append(f"Chỉ số đáp án sai: {c['nd']}")
        if len(set(c["da"])) != len(c["da"]):
            loi.append(f"Đáp án trùng nhau: {c['nd']}")
        if c["kho"] not in (1, 2, 3):
            loi.append(f"Độ khó không hợp lệ: {c['nd']}")
    for unit, lessons in ANH["Lớp 7"].items():
        for ten_ls, ls in lessons.items():
            for kt in ls["on_tap"]:
                if kt not in KIEN_THUC_NEN:
                    loi.append(f"{unit} / {ten_ls}: không có mục ôn tập '{kt}'")
    for w, t in TU_DIEN.items():
        if not t.get("nghia") or not t.get("pa"):
            loi.append(f"Từ thiếu nghĩa hoặc phiên âm: {w}")
    return loi


if __name__ == "__main__":
    ds_loi = kiem_tra_du_lieu()
    print("Số từ trong từ điển:", len(TU_DIEN))
    print("Số câu hỏi trắc nghiệm:", len(_tat_ca_cau_hoi()))
    print("Lỗi dữ liệu:", "không có" if not ds_loi else ds_loi)
    print("Từ của hôm nay:", tu_cua_ngay()["tu"])
