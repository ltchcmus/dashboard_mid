# Request Summary
Người dùng yêu cầu 2 thay đổi: (1) làm trục điểm đánh giá của Q13 dễ nhìn biến thiên hơn, (2) xóa Q10 ở Tab 3.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q13-rating-axis-and-remove-q10.md
- docs/ai/2026-04-18-q13-rating-axis-and-remove-q10.md

# Key Decisions
- Xóa toàn bộ block Q10 (ROI box plot theo thể loại) trong `ve_tab_tai_chinh` để Tab 3 chỉ còn Q7-Q9.
- Ở Q13, thay range cố định `[0,10]` của trục Y phải bằng range động:
  - Tính `diem_min`, `diem_max` từ dữ liệu hiện tại.
  - Thêm `padding` theo biên độ dữ liệu (`max(0.15, range*0.25)`).
  - Clamp trong [0, 10] để tránh vượt ngưỡng hợp lệ của điểm.
  - Có fallback khi khoảng quá hẹp để tránh trục bằng nhau.

# Next Steps
1. Chạy dashboard và xác nhận đường điểm Q13 nhìn rõ biến thiên hơn ở nhiều bộ lọc.
2. Nếu muốn nhấn mạnh hơn nữa sự thay đổi, có thể thêm marker text hiển thị giá trị điểm theo từng nhóm số thể loại.