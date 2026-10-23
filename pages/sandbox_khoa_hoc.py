import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Sandbox Khoa Hoc",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Sandbox Khoa Hoc — Kham Phat Vat Chat")

# === Tai game HTML ===
html_path = Path(__file__).parent.parent / "assets" / "games" / "sandboxels_mini.html"
try:
    html_content = html_path.read_text(encoding="utf-8")
except FileNotFoundError:
    st.error("⚠️ Chua tim thay file game!")
    st.stop()

st.markdown("""
> Dat vat lieu va quan sat: Nuoc chay, Lua chay, Cat chim, Khoi bay...
""")

components.html(html_content, height=540, scrolling=True)

# === Noi dung lien ket ===
st.subheader("📚 Lien he bai hoc")
st.info("""
- Vật Lý: Khối lượng riêng, trạng thái vật chất
- Hóa Học: Phản ứng cháy, ngăn cháy
- Sinh Học: Thực vật, môi trường
""")

if st.button("🏠 Quay lai Trang Chu"):
    st.switch_page("Ket_Noi_Tri_Thuc.py")
