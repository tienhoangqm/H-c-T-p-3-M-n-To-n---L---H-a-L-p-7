import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Cấu hình trang (Luôn ở dòng đầu tiên)
st.set_page_config(
    page_title="Phòng Thí Nghiệm Hóa Sinh",
    page_icon="🔬",
    layout="wide"
)

# Tiêu đề chính
st.title("🔬 Phòng Thí Nghiệm Ảo — Vòng Tuần Hoàn Sinh Thái & Hóa Học")
st.markdown("> **Hướng dẫn:** Sử dụng các công cụ bên dưới để vẽ vật liệu, tạo ra các phản ứng hóa sinh và quan sát sự cân bằng của hệ sinh thái.")

# === TẢI VÀ NHÚNG SANDBOX GAME ===
html_path = Path(__file__).parent / "sandboxels_mini.html"

if not html_path.exists():
    st.error(f"⚠️ Không tìm thấy file game tại: `{html_path}`")
    st.info("💡 Đảm bảo file `sandboxels_mini.html` được đặt cùng thư mục với file Python này.")
    st.stop()

try:
    html_content = html_path.read_text(encoding="utf-8")
except Exception as e:
    st.error(f"⚠️ Lỗi khi đọc file HTML: {e}")
    st.stop()

# Nhúng game HTML với chiều cao lớn để hiển thị đủ không gian sinh thái
components.html(html_content, height=850, scrolling=False)

st.markdown("---")
st.header("📚 Sổ Tay Khoa Học")

# === NỘI DUNG BÀI GIẢNG ===
tab1, tab2, tab3, tab4 = st.tabs(["🌱 Sinh Học & Hệ Sinh Thái", "🧪 Hóa Học & Phản Ứng", "⚛️ Vật Lý & Biến Đổi Chất", "🎮 Thử Thách Thực Hành"])

with tab1:
    st.success("**Vòng Tuần Hoàn Carbon & Sự Sống**")
    st.markdown("""
    Trong hệ sinh thái, vật chất không tự sinh ra hay mất đi mà liên tục chuyển hóa qua các chu trình:
    
    *   **Quang hợp (Thực vật):** `Khí CO2 ➡️ Cây Xanh ➡️ Khí Oxy` 
        *   Cây cỏ hút khí Cacbonic (CO2) để quang hợp và nhả ra khí Oxy (O2) làm sạch môi trường.
    *   **Hô hấp (Động vật):** `Khí Oxy ➡️ Động Vật ➡️ Khí CO2`
        *   Cá, Chim, Thú rừng cần Oxy để sống. Quá trình hô hấp của chúng sẽ tiêu thụ Oxy và thải ngược lại CO2 cho cây.
    *   **Sinh trưởng:** Hạt giống rơi xuống **Đất** hoặc **Bùn** sẽ hút chất dinh dưỡng, nảy mầm và phát triển thành cây cổ thụ.
    *   **Phân hủy (Vi sinh vật):** `Sinh vật chết ➡️ Khuẩn/Nấm ➡️ Đất Mùn`
        *   Khi động thực vật chết đi, vi khuẩn/nấm mốc sẽ phân hủy chúng, trả lại chất mùn màu mỡ cho đất để ươm mầm thế hệ mới.
    """)

with tab2:
    st.warning("**Các Phản Ứng Hóa Học Căn Bản**")
    st.markdown("""
    Quan sát sự tương tác giữa các hợp chất hóa học đặc biệt:
    
    *   **Phản ứng ăn mòn:** `Axit + Vật chất ➡️ Khí Độc`
        *   Axit là chất lỏng có tính ăn mòn cao. Nó sẽ tiêu hủy đất đá, kim loại và sinh vật hữu cơ, đồng thời giải phóng khí độc nguy hiểm.
    *   **Phản ứng cháy trong Oxy:** `Lửa + Khí Oxy ➡️ Lửa lớn + Khí CO2`
        *   Oxy là chất duy trì sự cháy. Khi lửa gặp môi trường giàu Oxy, nó sẽ bùng phát rất mạnh và sinh ra nhiều khí CO2.
    *   **Khí Độc (Toxic Gas):** Rất nguy hiểm cho hô hấp. Bất kỳ động thực vật nào tiếp xúc với khí độc sẽ bị tiêu diệt và biến thành vi sinh vật/nấm mốc.
    """)

with tab3:
    st.info("**Sự Biến Đổi Trạng Thái Theo Nhiệt Độ & Trọng Lực**")
    st.markdown("""
    *   **Chuyển thể do Nhiệt độ (Công cụ Làm Nóng/Làm Lạnh):**
        *   `Nước (Lỏng) + Lạnh ➡️ Băng (Rắn)`
        *   `Nước (Lỏng) + Nóng ➡️ Khói/Hơi Nước (Khí)`
    *   **Tinh thể hóa (Hóa thạch):** `Cát + Dung Nham (Nhiệt cực cao) ➡️ Thủy Tinh`
        *   Nhiệt độ hàng ngàn độ của Dung nham có thể nung chảy Cát thành Thủy Tinh (Glass). Thủy tinh là vật chất trơ, **không bị Axit ăn mòn**, rất thích hợp làm bình chứa hóa chất.
    *   **Khối lượng riêng (Trọng lực):** Khí bay lên cao (tỷ trọng nhẹ), trong khi Đất, Đá, Bùn rơi xuống thấp. Dầu nổi trên mặt Nước vì Dầu nhẹ hơn Nước.
    """)

with tab4:
    st.error("**Thử thách dành cho bạn (Missions)**")
    st.markdown("""
    Hãy thử tự tay xây dựng và kiểm chứng các quy luật trên trong khung Sandbox nhé!
    1.  **Thử thách 1:** Trồng một khu rừng nhỏ (Đất + Hạt giống) và thả một bầy chim. Hãy phun **Khí CO2** vào rừng và quan sát xem lá cây có chuyển hóa nó thành Oxy cho chim thở không?
    2.  **Thử thách 2:** Tạo một bình chứa Axit an toàn. Bạn hãy vẽ một hố **Cát**, dùng công cụ **🔥 LÀM NÓNG** nung chảy Cát thành Thủy Tinh, sau đó đổ **Axit** vào xem bình có bị thủng không.
    3.  **Thử thách 3:** Tạo ra một thảm họa sinh thái nhỏ: Nhỏ 1 giọt **Khuẩn/Nấm** vào khu rừng hoặc tạo một đám cháy rừng. Quan sát chu trình phân hủy để lại Đất Mùn như thế nào.
    """)

st.markdown("---")
# Căn giữa nút điều hướng
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🏠 Hoàn Thành Bài Tập — Quay Lại Trang Chính", use_container_width=True):
        try:
            st.switch_page("Ket_Noi_Tri_Thuc.py")
        except Exception as e:
            st.error("⚠️ Không thể chuyển trang. Hãy đảm bảo file `Ket_Noi_Tri_Thuc.py` đang nằm ở thư mục gốc.")
