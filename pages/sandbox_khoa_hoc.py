import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Cấu hình trang luôn phải là lệnh Streamlit đầu tiên được gọi
st.set_page_config(
    page_title="Sandbox Khoa Học",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Sandbox Khoa Học — Khám Phá Vật Chất")

# === Đường dẫn file an toàn ===
html_path = Path(__file__).parent / "sandboxels_mini.html"

if not html_path.exists():
    st.error(f"⚠️ Không tìm thấy file game tại: `{html_path}`")
    st.info("💡 Đảm bảo file `sandboxels_mini.html` được đặt cùng thư mục với file Python này.")
    st.stop()

# Đọc file an toàn với khối Try-Except
try:
    html_content = html_path.read_text(encoding="utf-8")
except Exception as e:
    st.error(f"⚠️ Lỗi khi đọc file HTML: {e}")
    st.stop()

st.markdown("> **Hướng dẫn:** Nhấn & kéo chuột để đặt vật liệu. Quan sát Nước chảy, Lửa cháy, Cát chìm, Khói bay...")

# Tắt scrolling (scrolling=False) rất quan trọng để người dùng không bị cuộn trang khi đang kéo chuột vẽ trong game
components.html(html_content, height=560, scrolling=False)

st.markdown("---")
st.subheader("📚 Liên hệ bài học")

tab1, tab2, tab3 = st.tabs(["Vật Lý", "Hóa Học", "Sinh Học"])

with tab1:
    st.info("""
    **Vật Lý:**
    - **Nước chảy:** Chất lỏng không có hình dạng cố định.
    - **Cát chìm:** Khối lượng riêng của cát lớn hơn nước.
    - **Khói bay lên:** Khối lượng riêng của khói nhỏ hơn không khí.
    """)

with tab2:
    st.info("""
    **Hóa Học:**
    - **Gỗ + Lửa:** Phản ứng oxi hóa, sinh ra nhiệt và khói.
    - **Nước dập lửa:** Cách ly oxy và làm giảm nhiệt độ của vật liệu cháy.
    - **Dầu nổi trên nước:** Khối lượng riêng của dầu nhỏ hơn nước và không hòa tan.
    """)

with tab3:
    st.info("""
    **Sinh Học:**
    - **Sinh trưởng:** Thực vật cần nước để trao đổi chất và phát triển.
    - **Hủy diệt:** Lửa phá hủy cấu trúc tế bào và thiêu rụi thực vật.
    - **Môi trường:** Khói làm giảm chất lượng không khí, tác động đến hô hấp.
    """)

st.markdown("---")

# Căn giữa và mở rộng nút bấm quay lại để giao diện cân đối hơn
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🏠 Quay lại Trang Chính", use_container_width=True):
        # Lưu ý: Lệnh này yêu cầu Streamlit >= 1.30.0
        # File "Ket_Noi_Tri_Thuc.py" phải tồn tại trong thư mục gốc hoặc định nghĩa đúng route
        try:
            st.switch_page("Ket_Noi_Tri_Thuc.py")
        except Exception as e:
            st.error("⚠️ Không thể chuyển trang. Hãy kiểm tra lại tên file `Ket_Noi_Tri_Thuc.py` trong dự án.")
