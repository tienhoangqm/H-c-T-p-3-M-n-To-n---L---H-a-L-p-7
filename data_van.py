# -*- coding: utf-8 -*-
"""
NGÂN HÀNG DỮ LIỆU NGỮ VĂN 7 - KẾT NỐI TRI THỨC (KHUNG THEO MỤC LỤC SÁCH)

Trạng thái: khung đúng cấu trúc Tập Một và Tập Hai (10 bài, 41 văn bản).
Phần cau_hoi, bt_co_ban, bt_nang_cao đang để trống, sẽ được bổ sung
sau khi đối chiếu từng văn bản trong sách.
"""

def _khung(ten_van_ban, tac_gia, the_loai):
    return {
        "ly_thuyet": f"Thể loại: {the_loai}. Tác giả: {tac_gia}. Nội dung kiến thức đang được biên soạn theo sách.",
        "vi_du": "",
        "cau_hoi": [],
        "bt_co_ban": [],
        "bt_nang_cao": [],
    }

VAN = {
    "Lớp 7": {
        'Bài 1: Bầu trời tuổi thơ': {
            'Bầy chim chìa vôi': _khung('Bầy chim chìa vôi', 'Nguyễn Quang Thiều', 'Truyện'),
            'Đi lấy mật (trích Đất rừng phương Nam)': _khung('Đi lấy mật (trích Đất rừng phương Nam)', 'Đoàn Giỏi', 'Truyện'),
            'Ngàn sao làm việc': _khung('Ngàn sao làm việc', 'Võ Quảng', 'Thơ'),
            'Ngôi nhà trên cây (trích Tốt-tô-chan bên cửa sổ)': _khung('Ngôi nhà trên cây (trích Tốt-tô-chan bên cửa sổ)', 'Cu-rô-ya-na-gi Tê-sư-cô', 'Truyện (đọc mở rộng)'),
        },
        'Bài 2: Khúc nhạc tâm hồn': {
            'Đồng dao mùa xuân': _khung('Đồng dao mùa xuân', 'Nguyễn Khoa Điềm', 'Thơ bốn chữ'),
            'Gặp lá cơm nếp': _khung('Gặp lá cơm nếp', 'Thanh Thảo', 'Thơ năm chữ'),
            'Trở gió': _khung('Trở gió', 'Nguyễn Ngọc Tư', 'Tùy bút'),
            'Chiều sông Thương': _khung('Chiều sông Thương', 'Hữu Thỉnh', 'Thơ (thực hành đọc)'),
        },
        'Bài 3: Cội nguồn yêu thương': {
            'Vừa nhắm mắt vừa mở cửa sổ (trích)': _khung('Vừa nhắm mắt vừa mở cửa sổ (trích)', 'Nguyễn Ngọc Thuần', 'Truyện'),
            'Người thầy đầu tiên (trích)': _khung('Người thầy đầu tiên (trích)', 'Trin-ghi-dơ Ai-tơ-ma-tốp', 'Truyện'),
            'Quê hương': _khung('Quê hương', 'Tế Hanh', 'Thơ'),
            'Trong lòng mẹ (trích Những ngày thơ ấu)': _khung('Trong lòng mẹ (trích Những ngày thơ ấu)', 'Nguyên Hồng', 'Truyện (thực hành đọc)'),
        },
        'Bài 4: Giai điệu đất nước': {
            'Mùa xuân nho nhỏ': _khung('Mùa xuân nho nhỏ', 'Thanh Hải', 'Thơ'),
            'Gò Me (trích)': _khung('Gò Me (trích)', 'Hoàng Tố Nguyên', 'Truyện'),
            'Bài thơ "Đường núi" của Nguyễn Đình Thi': _khung('Bài thơ "Đường núi" của Nguyễn Đình Thi', 'Vũ Quần Phương', 'Văn bản nghị luận (bình thơ)'),
            'Chiều biên giới': _khung('Chiều biên giới', 'Lò Ngân Sủn', 'Thơ (thực hành đọc)'),
        },
        'Bài 5: Màu sắc trăm miền': {
            'Tháng Giêng, mơ về trăng non rét ngọt (trích)': _khung('Tháng Giêng, mơ về trăng non rét ngọt (trích)', 'Vũ Bằng', 'Tùy bút'),
            'Chuyện cơm hến': _khung('Chuyện cơm hến', 'Hoàng Phủ Ngọc Tường', 'Tản văn'),
            'Hội lồng tồng': _khung('Hội lồng tồng', 'Trần Quốc Vượng – Lê Văn Hảo – Dương Tất Từ', 'Văn bản thông tin'),
            'Những khuôn của dấu yêu': _khung('Những khuôn của dấu yêu', 'Trương Anh Ngọc', 'Văn bản thông tin (thực hành đọc)'),
        },
        'Bài 6: Bài học cuộc sống': {
            'Đẽo cày giữa đường': _khung('Đẽo cày giữa đường', 'Ngụ ngôn Việt Nam', 'Truyện ngụ ngôn'),
            'Ếch ngồi đáy giếng': _khung('Ếch ngồi đáy giếng', 'Trang Tử', 'Truyện ngụ ngôn'),
            'Con mối và con kiến': _khung('Con mối và con kiến', 'Nam Hương', 'Truyện ngụ ngôn'),
            'Một số câu tục ngữ Việt Nam': _khung('Một số câu tục ngữ Việt Nam', 'Tục ngữ', 'Tục ngữ'),
            'Con hổ có nghĩa': _khung('Con hổ có nghĩa', 'Vũ Trinh', 'Truyện ngụ ngôn'),
            'Thiên nga, cá măng và tôm hùm (thực hành đọc)': _khung('Thiên nga, cá măng và tôm hùm (thực hành đọc)', 'I-van Crư-lốp', 'Truyện ngụ ngôn'),
        },
        'Bài 7: Thế giới viễn tưởng': {
            'Cuộc chạm trán trên đại dương (trích Hai vạn dặm dưới biển)': _khung('Cuộc chạm trán trên đại dương (trích Hai vạn dặm dưới biển)', 'Giuyn Véc-nơ', 'Truyện khoa học viễn tưởng'),
            'Đường vào trung tâm vũ trụ (trích Thiên Mã)': _khung('Đường vào trung tâm vũ trụ (trích Thiên Mã)', 'Hà Thuỷ Nguyên', 'Truyện khoa học viễn tưởng'),
            'Dấu ấn Hồ Khanh': _khung('Dấu ấn Hồ Khanh', 'Nhật Văn', 'Truyện khoa học viễn tưởng'),
            'Chiếc đũa thần (trích Tinh vân Tiên Nữ)': _khung('Chiếc đũa thần (trích Tinh vân Tiên Nữ)', 'I. A. E-phơ-rê-mốp', 'Truyện khoa học viễn tưởng (thực hành đọc)'),
        },
        'Bài 8: Trải nghiệm để trưởng thành': {
            'Bản đồ dẫn đường': _khung('Bản đồ dẫn đường', 'Đa-ni-en Gốt-li-ép', 'Văn bản nghị luận'),
            'Hãy cầm lấy và đọc': _khung('Hãy cầm lấy và đọc', 'Huỳnh Như Phương', 'Văn bản nghị luận'),
            'Nói với con': _khung('Nói với con', 'Y Phương', 'Thơ'),
            'Câu chuyện về con đường': _khung('Câu chuyện về con đường', 'Đoàn Công Lê Huy', 'Văn bản nghị luận (thực hành đọc)'),
        },
        'Bài 9: Hòa điệu với tự nhiên': {
            'Thuỷ tiên tháng Một': _khung('Thuỷ tiên tháng Một', 'Thô-mát L. Phrít-man', 'Văn bản thông tin'),
            'Lễ rửa làng của người Lô Lô': _khung('Lễ rửa làng của người Lô Lô', 'Phạm Thuỳ Dung', 'Văn bản thông tin'),
            'Bản tin về hoa anh đào': _khung('Bản tin về hoa anh đào', 'Nguyễn Vĩnh Nguyên', 'Bản tin'),
            '"Thân thiện với môi trường"': _khung('"Thân thiện với môi trường"', 'Nguyễn Hữu Quỳnh Hương', 'Văn bản thông tin (thực hành đọc)'),
        },
        'Bài 10: Trang sách và cuộc sống': {
            'Thách thức đầu tiên': _khung('Thách thức đầu tiên', 'Chưa xác nhận tác giả', 'Đọc (cần đối chiếu sách)'),
            'Chinh phục những cuốn sách mới': _khung('Chinh phục những cuốn sách mới', 'Chưa xác nhận tác giả', 'Đọc (cần đối chiếu sách)'),
            'Thách thức thứ hai': _khung('Thách thức thứ hai', 'Chưa xác nhận tác giả', 'Viết (cần đối chiếu sách)'),
        },
    }
}

def kiem_tra_van():
    return []

if __name__ == "__main__":
    so_vb = sum(len(b) for b in VAN["Lớp 7"].values())
    print("Số bài:", len(VAN["Lớp 7"]), "| Số văn bản:", so_vb)
