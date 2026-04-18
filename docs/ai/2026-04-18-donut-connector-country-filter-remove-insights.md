# Request Summary
Nguoi dung yeu cau 3 thay doi:
1) Donut chart Q4: callout cho slice nho can the hien duong noi vao slice.
2) Bo sung bo loc dropdown Quoc gia trong sidebar, dat phia tren bo loc The loai.
3) Loai bo toan bo insight buttons va 5 dong caption storytelling cu the.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-donut-connector-country-filter-remove-insights.md
- docs/ai/2026-04-18-donut-connector-country-filter-remove-insights.md

# Key Decisions
- Donut Q4 doi text position sang outside + automargin:
  - `textposition="outside"`
  - `automargin=True`
  Cach nay giup callout o ngoai donut co duong noi den slice nho.
- Sidebar filter bo sung Quoc gia truoc The loai:
  - Tao danh sach quoc gia tu `du_lieu["countries"]`.
  - Them `st.sidebar.selectbox("Quốc gia", ["Tất cả"] + danh_sach_quoc_gia)`.
  - Loc `movies` theo `show_id` cua quoc gia da chon.
- Insight cleanup:
  - Xoa tat ca `st.expander("💡 Insight chính")` tren toan bo dashboard.
  - Xoa dong caption tong quan o dau trang va cac dong `Tab này trả lời...` trong tab 1/2/3/4.

# Verification
- Compile check `src/main.py`: OK.
- VS Code Problems cho `src/main.py`: No errors found.
- Kiem tra text-level:
  - Khong con `st.expander("💡 Insight chính")`.
  - Khong con cac caption storytelling duoc yeu cau xoa.

# Next Steps
1. Chay Streamlit va xac nhan truc quan donut callout line hien thi ro tren kich thuoc man hinh nho.
2. Neu can giu 1 so insight phuc vu presentation, co the doi sang static markdown thay vi expander/button.
3. Neu muon multi-country nhu dac ta ban dau, co the doi bo loc Quoc gia tu selectbox sang multiselect.
