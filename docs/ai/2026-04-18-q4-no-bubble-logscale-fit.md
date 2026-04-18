# Request Summary
Người dùng yêu cầu tinh chỉnh Q4: bỏ bubble chart behavior và làm log-scale trục popularity hiển thị vừa đủ, tránh khoảng trống lớn phía phải.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-no-bubble-logscale-fit.md
- docs/ai/2026-04-18-q4-no-bubble-logscale-fit.md

# Key Decisions
- Bỏ hoàn toàn mapping kích thước điểm theo biến số; dùng marker size cố định (9) cho scatter Q4.
- Giữ `log_x=True` trong `px.scatter` để đúng yêu cầu.
- Giữ custom tick format dạng mũ 10 bằng Unicode superscript (10⁰, 10¹, ...).
- Áp dụng style log-axis tương tự cách xử lý ở tab ROI (`exponentformat`, `showexponent`, `dtick`).
- Giảm khoảng trống phải bằng cách chặn vị trí annotation quadrant trong phạm vi dữ liệu thực (`x_right` và `x_left`) thay vì dùng giá trị có thể vượt quá max dữ liệu.
- Giữ opacity nhóm `Khác` thấp hơn để giảm nhiễu trực quan.

# Next Steps
1. Chạy Streamlit và quan sát Q4 với nhiều bộ lọc để xác nhận không còn khoảng trắng lớn bên phải.
2. Nếu vẫn còn dư trục ở một số filter cực đoan, cân nhắc đặt annotation theo `xref='paper'` thay vì tọa độ dữ liệu X.