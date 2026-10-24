import importlib

MODULES = [
    ("data_toan", "TOAN"),
    ("data_vatly", "VATLY"),
    ("data_hoa", "HOA"),
    ("data_van", "VAN"),
]
BAT_BUOC = ("ly_thuyet", "cau_hoi", "bt_co_ban", "bt_nang_cao")

for ten_file, ten_bien in MODULES:
    try:
        m = importlib.import_module(ten_file)
    except Exception as e:
        print(f"[{ten_file}] LỖI IMPORT: {type(e).__name__}: {e}")
        continue

    if not hasattr(m, ten_bien):
        cac_bien_hoa = [k for k in dir(m) if k.isupper()]
        print(f"[{ten_file}] THIẾU biến '{ten_bien}'. File này đang có: {cac_bien_hoa}")
        continue

    du_lieu = getattr(m, ten_bien)
    if not du_lieu:
        print(f"[{ten_file}] biến '{ten_bien}' rỗng")
        continue

    for lop, chuongs in du_lieu.items():
        so_bai = sum(len(bs) for bs in chuongs.values())
        print(f"[{ten_file}] {lop}: {len(chuongs)} chương, {so_bai} bài")
        for chuong, bais in chuongs.items():
            for bai, d in bais.items():
                thieu = [k for k in BAT_BUOC if k not in d]
                if thieu:
                    print(f"    thiếu khóa {thieu} ở: {chuong} / {bai}")
