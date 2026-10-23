import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Sandbox Khoa Học",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Sandbox Khoa Học — Khám Phá Vật Chất")

# === Đường dẫn đơn giản — cùng thư mục ===
html_path = Path(__file__).parent / "sandboxels_mini.html"

if not html_path.exists():
    st.error(f"⚠️ Không tìm thấy file game tại: {html_path}")
    st.info("Đảm bảo file `sandboxels_mini.html` đặt cùng thư mục với file `.py`")
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

st.markdown("""
> Đặt vật liệu & quan sát: Nước chảy, Lửa cháy, Cát chìm, Khói bay...
""")

components.html(html_content, height=560, scrolling=True)

st.markdown("---")
st.subheader("📚 Liên hệ bài học")
tab1, tab2, tab3 = st.tabs(["Vật Lý", "Hóa Học", "Sinh Học"])

with tab1:
    st.info("""
    **Vật Lý:**
    - Nước chảy → chất lỏng không hình dạng cố định
    - Cát chìm → khối lượng riêng cát > nước
    - Khói bay lên → khối lượng riêng khói < không khí
    """)

with tab2:
    st.info("""
    **Hóa Học:**
    - Gỗ + Lửa → phản ứng oxi hóa, tạo khói
    - Nước dập lửa → ngăn tiếp xúc oxy
    - Dầu nổi trên nước → khối lượng riêng dầu < nước
    """)

with tab3:
    st.info("""
    **Sinh Học:**
    - Cây cần nước phát triển
    - Lửa ảnh hưởng thực vật
    - Khói tác động môi trường
    """)

st.markdown("---")
if st.button("🏠 Quay lại Trang Chính"):
    st.switch_page("Ket_Noi_Tri_Thuc.py")
