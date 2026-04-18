# Objective
Xóa và vẽ lại hoàn toàn biểu đồ Q4 ở Tab 2 để loại bỏ logic cũ gây khó kiểm soát scale trục X.

# Context
- Q4 trước đó đã qua nhiều lần tinh chỉnh và còn rủi ro kéo giãn trục popularity.
- Người dùng yêu cầu "xóa Q4 hiện tại và vẽ lại".
- Cần giữ storytelling theo design_question_2.md: scatter theo genre + đường trung vị + 4 góc chiến lược.

# Final Prompt
xóa đi Q4 hiện tại, và sau đó vẽ lại.

# Expected Output
- Khối Q4 được viết lại từ đầu, không giữ logic cũ chắp vá.
- Scatter dùng log_x=True với tick mũ 10 dạng Unicode superscript.
- Nhãn quadrant không làm giãn trục X (dùng paper coordinates).
- Nhóm top genre giữ opacity cao hơn nhóm "Khác".
- Ứng dụng chạy không lỗi cú pháp.