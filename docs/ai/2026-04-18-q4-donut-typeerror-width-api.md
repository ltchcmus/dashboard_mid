# Request Summary
Người dùng gửi traceback khi chạy app sau khi cập nhật Q4; lỗi phát sinh tại bước lọc dữ liệu donut chart. Đồng thời có cảnh báo Streamlit về `use_container_width` trong `st.plotly_chart`.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-donut-typeerror-width-api.md
- docs/ai/2026-04-18-q4-donut-typeerror-width-api.md

# Key Decisions
- Sửa pipeline tạo `donut_data` theo cách an toàn kiểu dữ liệu:
  - Dùng `rename_axis(...).reset_index(name='Số lượng phim')` thay vì rename thủ công dễ lệch cột.
  - Ép kiểu `Số lượng phim` sang số bằng `pd.to_numeric(..., errors='coerce').fillna(0)` trước khi lọc `> 0`.
- Chuyển các `st.plotly_chart(..., use_container_width=True)` sang `width="stretch"` để khớp cảnh báo API mới.
- Giữ nguyên `st.button(..., use_container_width=True)` để tránh thay đổi API không cần thiết cho widget khác.

# Next Steps
1. Chạy lại `streamlit run src/main.py` để xác nhận Q4 render bình thường, không còn traceback.
2. Nếu muốn đồng bộ toàn codebase theo API width mới, rà thêm các widget khác (không chỉ plotly chart).