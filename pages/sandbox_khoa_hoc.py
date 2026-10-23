import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import csv
import os
from datetime import datetime
import pandas as pd
import plotly.express as px

# === 1. CẤU HÌNH TRANG ===
st.set_page_config(
    page_title="Phòng Thí Nghiệm Hóa Sinh",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Phòng Thí Nghiệm Ảo — Vòng Tuần Hoàn Sinh Thái & Hóa Học")
st.markdown("> **Hướng dẫn:** Sử dụng các công cụ bên dưới để vẽ vật liệu, tạo ra các phản ứng hóa sinh và quan sát sự cân bằng của hệ sinh thái.")

# === 2. TẢI VÀ NHÚNG SANDBOX GAME ===
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

components.html(html_content, height=850, scrolling=False)

st.markdown("---")
st.header("📚 Sổ Tay Khoa Học")

# === 3. KHAI BÁO CÁC TABS ===
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌱 Sinh Học & Hệ Sinh Thái", 
    "🧪 Hóa Học & Phản Ứng", 
    "⚛️ Vật Lý & Biến Đổi Chất", 
    "🎮 Thử Thách Thực Hành",
    "🏆 Bảng Xếp Hạng"
])

# === NỘI DUNG TỪNG TAB ===
with tab1:
    st.success("**Vòng Tuần Hoàn Carbon & Sự Sống**")
    st.markdown("""
    Trong hệ sinh thái, vật chất không tự sinh ra hay mất đi mà liên tục chuyển hóa qua các chu trình:
    *   **Quang hợp (Thực vật):** `Khí CO2 ➡️ Cây Xanh ➡️ Khí Oxy` 
    *   **Hô hấp (Động vật):** `Khí Oxy ➡️ Động Vật ➡️ Khí CO2`
    *   **Sinh trưởng:** Hạt giống rơi xuống **Đất** hoặc **Bùn** sẽ hút chất dinh dưỡng, nảy mầm và phát triển.
    *   **Phân hủy (Vi sinh vật):** `Sinh vật chết ➡️ Khuẩn/Nấm ➡️ Đất Mùn`
    """)

with tab2:
    st.warning("**Các Phản Ứng Hóa Học Căn Bản**")
    st.markdown("""
    Quan sát sự tương tác giữa các hợp chất hóa học đặc biệt:
    *   **Phản ứng ăn mòn:** `Axit + Vật chất ➡️ Khí Độc`
    *   **Phản ứng cháy trong Oxy:** `Lửa + Khí Oxy ➡️ Lửa lớn + Khí CO2`
    *   **Khí Độc (Toxic Gas):** Rất nguy hiểm cho hô hấp. Động thực vật tiếp xúc với khí độc sẽ bị tiêu diệt.
    """)

with tab3:
    st.info("**Sự Biến Đổi Trạng Thái Theo Nhiệt Độ & Trọng Lực**")
    st.markdown("""
    *   **Chuyển thể do Nhiệt độ:** `Nước + Lạnh ➡️ Băng` | `Nước + Nóng ➡️ Khói`
    *   **Tinh thể hóa (Hóa thạch):** `Cát + Dung Nham ➡️ Thủy Tinh`. Thủy tinh là vật chất trơ, **không bị Axit ăn mòn**.
    *   **Khối lượng riêng:** Khí bay lên cao, Dầu nổi trên mặt Nước, Đất Đá chìm xuống đáy.
    """)

with tab4:
    st.error("**Thử thách dành cho bạn (Missions)**")
    st.markdown("Hãy thử tự tay xây dựng và kiểm chứng các quy luật trên trong khung Sandbox. Đánh dấu vào ô bên cạnh khi bạn đã làm thành công nhé!")

    # Tính toán tiến độ
    m1_done = st.session_state.get("m1", False)
    m2_done = st.session_state.get("m2", False)
    m3_done = st.session_state.get("m3", False)
    
    total_missions = 3
    completed_missions = sum([m1_done, m2_done, m3_done])
    progress_percent = int((completed_missions / total_missions) * 100)

    # Hiển thị thanh tiến trình
    st.markdown(f"**Tiến độ hoàn thành: {completed_missions}/{total_missions} ({progress_percent}%)**")
    st.progress(progress_percent)

    if "mission_celebrated" not in st.session_state:
        st.session_state.mission_celebrated = False

    st.markdown("---")
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

    # Kiểm tra điều kiện chiến thắng
    if completed_missions == total_missions:
        if not st.session_state.mission_celebrated:
            st.balloons()
            st.toast("🎉 Bạn đã hoàn thành tất cả thử thách!", icon="🏆")
            st.session_state.mission_celebrated = True
        st.success("🏆 **XUẤT SẮC!** Bạn đã nắm vững các quy luật Hóa Sinh cơ bản và trở thành một nhà Khoa học thực thụ!")
    else:
        st.session_state.mission_celebrated = False

    # Giao diện Lưu Kết Quả
    st.markdown("### 💾 Lưu kết quả học tập")
    col_name, col_btn = st.columns([3, 1])
    with col_name:
        student_name = st.text_input("Nhập Họ và Tên của em:", placeholder="Ví dụ: Nguyễn Văn A")
    
    with col_btn:
        st.write("") 
        st.write("")
        if st.button("Lưu Tiến Độ", use_container_width=True):
            if not student_name.strip():
                st.warning("⚠️ Em cần nhập tên trước khi lưu kết quả nhé!")
            else:
                csv_file = "ket_qua_thuc_hanh.csv"
                file_exists = os.path.isfile(csv_file)
                try:
                    with open(csv_file, mode="a", encoding="utf-8-sig", newline="") as f:
                        writer = csv.writer(f)
                        if not file_exists:
                            writer.writerow(["Thời Gian", "Tên Học Sinh", "Thử thách 1", "Thử thách 2", "Thử thách 3", "Hoàn Thành (%)"])
                        
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
    
    if os.path.exists(csv_file):
        try:
            df = pd.read_csv(csv_file)
            
            # Vẽ biểu đồ tròn Plotly
            st.subheader("📊 Thống kê tỷ lệ hoàn thành")
            pie_data = df['Hoàn Thành (%)'].value_counts().reset_index()
            pie_data.columns = ['Mức độ hoàn thành', 'Số lượng học sinh']
            
            fig = px.pie(
                pie_data, 
                values='Số lượng học sinh', 
                names='Mức độ hoàn thành',
                hole=0.4,
                color_discrete_sequence=px.colors.sequential.Teal_r 
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")

            # Hiển thị bảng chi tiết
            st.subheader("📋 Chi tiết bảng xếp hạng")
            if "Hoàn Thành (%)" in df.columns and "Thời Gian" in df.columns:
                df["Tỷ lệ (Số)"] = df["Hoàn Thành (%)"].str.replace("%", "").astype(int)
                df = df.sort_values(by=["Tỷ lệ (Số)", "Thời Gian"], ascending=[False, True])
                df = df.drop(columns=["Tỷ lệ (Số)"])

            df.insert(0, "Hạng", range(1, len(df) + 1))
            st.dataframe(df, use_container_width=True, hide_index=True, height=350)
            
            if st.button("🔄 Làm mới dữ liệu", use_container_width=True):
                st.rerun()
                
        except Exception as e:
            st.error(f"⚠️ Đã có lỗi xảy ra khi tải dữ liệu: {e}")
    else:
        st.info("Trang giấy trắng! Chưa có nhà khoa học nào nộp kết quả. Hãy quay lại Tab **Thử Thách Thực Hành** để trở thành người dẫn đầu nhé!")
