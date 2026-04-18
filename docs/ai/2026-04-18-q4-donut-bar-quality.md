# Request Summary
Người dùng cập nhật yêu cầu Q4 trong tài liệu thiết kế mới và yêu cầu sửa lại code tương ứng.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-donut-bar-quality.md
- docs/ai/2026-04-18-q4-donut-bar-quality.md

# Key Decisions
- Loại bỏ Q4 scatter cũ, thay bằng 2-panel:
  - Donut chart cho phân bố chất lượng theo bucket điểm.
  - Horizontal bar chart cho top thể loại trong nhóm phim rating >= 7.5.
- Tận dụng dữ liệu đã có trong movies_loc và genres_loc, không tạo explode toàn cục mới.
- Tính thêm ROI trung bình theo thể loại trong nhóm high-quality để bổ sung chiều insight trên hover.
- Giữ expander insight riêng cho từng panel để đáp ứng storytelling.
- Trong quá trình chỉnh sửa đã phát hiện và khôi phục một đoạn helper bị chèn nhầm ở đầu file trước đó để đảm bảo file compile được.

# Next Steps
1. Chạy Streamlit và xác nhận trực quan Q4 mới (layout, màu, hover, insight).
2. Nếu cần tương tác sâu hơn, có thể bổ sung click-filter giữa donut và bar theo bucket rating.