# Objective
Ep buoc semi-bold (600) hien thi dung trong Streamlit + Plotly bang CSS selector cu the va !important, giam anh huong bi ghi de boi inline style.

# Context
Nguoi dung yeu cau thay the toan bo block <style> trong main.py bang mot block CSS moi chi tap trung vao font-weight hierarchy (400-600-700+), khong chen thuoc tinh weight vao Plotly Python layout.

# Final Prompt
Fix Typography: Ep buoc Semi-Bold (600) hien thi dung tren Streamlit + Plotly.
- Thay the toan bo block <style> trong main.py bang CSS duoc cung cap.
- Dung selector cu the + !important de override.
- Giu logic fallback semi-bold.
- Khong them weight/font_weight vao fig.update_layout().

# Expected Output
- CSS moi thay the hoan toan block cu.
- KPI label, caption, sidebar label, plotly axis/legend/hover text hien thi semi-bold on dinh.
- Khong loi syntax hay runtime do f-string/CSS braces.