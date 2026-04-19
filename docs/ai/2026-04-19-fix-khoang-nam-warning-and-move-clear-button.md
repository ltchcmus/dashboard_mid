# Request Summary
- Sửa warning Streamlit của slider `khoang_nam_chon`.
- Di chuyển nút xóa lọc xuống dưới các dropdown trong sidebar.

# Files Changed
- `src/main.py`

# Key Decisions
- Tránh warning widget policy bằng cách:
  - Khởi tạo `khoang_nam_chon` trong session state chỉ khi key chưa tồn tại.
  - Bỏ tham số `value` khỏi `st.sidebar.slider(...)` khi đã dùng `key`.
- Di chuyển nút `Xóa tất cả bộ lọc` xuống sau 3 dropdown theo yêu cầu UI.
- Vì nút bấm ở dưới widgets, không set trực tiếp các key widget trong cùng lượt chạy.
  - Thay vào đó đẩy reset vào `pending_filter_updates` (bao gồm cả `khoang_nam_chon`) và `st.rerun()` để áp dụng ở đầu run kế tiếp.
- Giữ reset event chart (`chart_event_signature`, `chart_event_skip_once`) để tránh tác động từ selection cũ.

# Next Steps
- Chạy lại app và bấm nút reset trong vài trạng thái filter khác nhau để xác nhận:
  - không còn warning,
  - slider năm về full range,
  - dropdown về rỗng,
  - tương tác chart-tab vẫn ổn định sau reset.