import pandas as pd
import os
import csv
from datetime import datetime
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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌱 Sinh Học & Hệ Sinh Thái", 
    "🧪 Hóa Học & Phản Ứng", 
    "⚛️ Vật Lý & Biến Đổi Chất", 
    "🎮 Thử Thách Thực Hành",
    "🏆 Bảng Xếp Hạng"
])

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
    st.markdown("Hãy thử tự tay xây dựng và kiểm chứng các quy luật trên trong khung Sandbox. Đánh dấu vào ô bên cạnh khi bạn đã làm thành công nhé!")

    # 1. Tính toán tiến độ
    m1_done = st.session_state.get("m1", False)
    m2_done = st.session_state.get("m2", False)
    m3_done = st.session_state.get("m3", False)
    
    total_missions = 3
    completed_missions = sum([m1_done, m2_done, m3_done])
    progress_percent = int((completed_missions / total_missions) * 100)

    # 2. Hiển thị thanh tiến trình
    st.markdown(f"**Tiến độ hoàn thành: {completed_missions}/{total_missions} ({progress_percent}%)**")
    st.progress(progress_percent)

    if "mission_celebrated" not in st.session_state:
        st.session_state.mission_celebrated = False

    st.markdown("---")
    
    # 3. Giao diện Checkbox thử thách
    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown("**Thử thách 1: Phổi xanh của Trái Đất**  \nTrồng rừng, thả chim và phun **Khí CO2** để quan sát lá cây quang hợp tạo ra **Oxy**.")
    with col2:
        m1 = st.checkbox("Hoàn thành", key="m1")

    st.markdown("---")
    
    with col1:
        st.markdown("**Thử thách 2: Chế tạo bình chứa Axit**  \nVẽ **Cát**, dùng công cụ **🔥 LÀM NÓNG** nung chảy thành **Thủy Tinh**, sau đó đổ **Axit** vào.")
    with col2:
        m2 = st.checkbox("Hoàn thành", key="m2")

    st.markdown("---")
    
    with col1:
        st.markdown("**Thử thách 3: Vòng tuần hoàn phân hủy**  \nNhỏ **Khuẩn/Nấm** vào khu rừng hoặc tạo đám cháy. Quan sát sinh vật biến thành **Đất Mùn**.")
    with col2:
        m3 = st.checkbox("Hoàn thành", key="m3")

    st.markdown("---")

    # 4. Kiểm tra điều kiện chiến thắng
    if completed_missions == total_missions:
        if not st.session_state.mission_celebrated:
            st.balloons()
            st.toast("🎉 Bạn đã hoàn thành tất cả thử thách!", icon="🏆")
            st.session_state.mission_celebrated = True
        st.success("🏆 **XUẤT SẮC!** Bạn đã nắm vững các quy luật Hóa Sinh cơ bản và trở thành một nhà Khoa học thực thụ!")
    else:
        st.session_state.mission_celebrated = False

    # 5. Giao diện Lưu Kết Quả
    st.markdown("### 💾 Lưu kết quả học tập")
    col_name, col_btn = st.columns([3, 1])
    
    with col_name:
        student_name = st.text_input("Nhập Họ và Tên của em:", placeholder="Ví dụ: Nguyễn Văn A")
    
    with col_btn:
        st.write("") # Dùng để căn chỉnh nút bấm ngang hàng với ô nhập text
        st.write("")
        if st.button("Lưu Tiến Độ", use_container_width=True):
            if not student_name.strip():
                st.warning("⚠️ Em cần nhập tên trước khi lưu kết quả nhé!")
            else:
                csv_file = "ket_qua_thuc_hanh.csv"
                file_exists = os.path.isfile(csv_file)
                
                # Ghi dữ liệu vào file CSV (utf-8-sig để Excel đọc không lỗi font)
                try:
                    with open(csv_file, mode="a", encoding="utf-8-sig", newline="") as f:
                        writer = csv.writer(f)
                        # Nếu file chưa tồn tại, tạo dòng tiêu đề (Header)
                        if not file_exists:
                            writer.writerow(["Thời Gian", "Tên Học Sinh", "Thử thách 1", "Thử thách 2", "Thử thách 3", "Hoàn Thành (%)"])
                        
                        # Ghi dữ liệu của học sinh
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        writer.writerow([
                            current_time, 
                            student_name.strip(), 
                            "Đạt" if m1_done else "Chưa", 
                            "Đạt" if m2_done else "Chưa", 
                            "Đạt" if m3_done else "Chưa", 
                            f"{progress_percent}%"
                        ])
                    st.success(f"✅ Đã lưu thành công tiến độ của học sinh **{student_name}**!")
                except Exception as e:
                    st.error(f"⚠️ Lỗi khi lưu file: {e}")
with tab5:
    st.header("🏆 Bảng Vàng Thành Tích")
    st.markdown("Cùng theo dõi tiến độ hoàn thành thử thách phòng thí nghiệm của cả lớp!")

    csv_file = "ket_qua_thuc_hanh.csv"
    
    # Kiểm tra xem file CSV đã được tạo chưa (đã có ai nộp bài chưa)
    if os.path.exists(csv_file):
        try:
            # Đọc dữ liệu từ file CSV
            df = pd.read_csv(csv_file)
            
            # Xử lý sắp xếp (Sorting): Ưu tiên % cao lên trước, nếu bằng % thì ai nộp sớm hơn sẽ xếp trên
            if "Hoàn Thành (%)" in df.columns and "Thời Gian" in df.columns:
                # Tạo cột phụ dạng số nguyên từ chuỗi "100%" để sắp xếp
                df["Tỷ lệ (Số)"] = df["Hoàn Thành (%)"].str.replace("%", "").astype(int)
                # Sắp xếp: Tỷ lệ (Giảm dần) -> Thời gian (Tăng dần)
                df = df.sort_values(by=["Tỷ lệ (Số)", "Thời Gian"], ascending=[False, True])
                # Xóa cột phụ sau khi đã sắp xếp xong
                df = df.drop(columns=["Tỷ lệ (Số)"])

            # Đánh số thứ tự (Hạng) tự động
            df.insert(0, "Hạng", range(1, len(df) + 1))
            
            # Hiển thị bảng dữ liệu
            # hide_index=True giúp giấu cột index mặc định (0, 1, 2,...) của Pandas cho đẹp mắt
            st.dataframe(
                df, 
                use_container_width=True, 
                hide_index=True,
                height=400 # Cố định chiều cao để không bị đẩy giao diện nếu lớp có quá đông học sinh
            )
            
            # Thêm nút làm mới (refresh) để cập nhật dữ liệu nếu có bạn khác vừa nộp bài
            if st.button("🔄 Làm mới Bảng Xếp Hạng", use_container_width=True):
                st.rerun()
                
        except Exception as e:
            st.error(f"⚠️ Đã có lỗi xảy ra khi tải bảng xếp hạng: {e}")
    else:
        st.info("Trang giấy trắng! Chưa có nhà khoa học nào nộp kết quả. Hãy quay lại Tab **Thử Thách Thực Hành** để trở thành người dẫn đầu nhé!")
