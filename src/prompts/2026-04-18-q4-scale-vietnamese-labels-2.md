# Objective
Tinh chỉnh biểu đồ Q13 (biểu đồ kép số thể loại vs performance) để cải thiện khả năng đọc trục, giảm rối grid và chuẩn hóa màu theo semantic system.

# Context
- Người dùng phản ánh Q13 còn mờ nhãn trục Y phải, nhiều grid chồng gây rối và chưa đồng bộ màu.
- Yêu cầu bổ sung: hover/legend gọn, bố cục tiết kiệm không gian, giữ line nổi bật.

# Final Prompt
Fix Q13: chỉnh màu chữ trục, grid, màu bar/line, hover/legend và layout theo danh sách yêu cầu chi tiết.

# Expected Output
- Tick labels, axis titles dùng TEXT_DARK.
- Chỉ giữ grid trục Y trái (màu #E5E7EB, dot), ẩn grid trục Y phải.
- Bar màu rgba(0,128,128,0.7), line + marker màu NETFLIX_RED.
- Hover bar/line gọn theo mẫu yêu cầu.
- Legend đặt góc trên phải, nền trắng, viền nhẹ.
- Mã compile thành công.