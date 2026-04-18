# Request Summary
Người dùng yêu cầu xóa Q4 hiện tại và vẽ lại toàn bộ biểu đồ.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-redraw-from-scratch.md
- docs/ai/2026-04-18-q4-redraw-from-scratch.md

# Key Decisions
- Viết lại toàn bộ block Q4 trong `ve_tab_chat_luong` thay vì vá thêm.
- Giữ pipeline dữ liệu rõ ràng: lọc `popularity > 0`, `vote_count >= 50`, map top 8 genre + nhóm `Khác`.
- Giữ trục X log bằng `log_x=True` và tick format 10^n dạng superscript Unicode.
- Đặt nhãn 4 quadrant bằng `xref='paper'`, `yref='paper'` để tránh annotation kéo giãn trục X.
- Dùng marker size cố định (không bubble), giữ opacity: top genre 0.6, nhóm `Khác` 0.25.

# Next Steps
1. Chạy Streamlit và kiểm tra trực quan Q4 ở nhiều bộ lọc năm/thể loại/ngôn ngữ.
2. Nếu muốn bám sát hơn design ban đầu, có thể thêm tuỳ chọn bật/tắt bubble-size theo `vote_count`.