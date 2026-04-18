# Objective
Cập nhật Q4 trong dashboard để thu hẹp miền hiển thị trục popularity trên log scale, Việt hóa toàn bộ nhãn phân vùng, và bỏ chú thích "thang log".

# Context
- File triển khai chính: src/main.py (hàm ve_tab_chat_luong).
- Vấn đề người dùng gặp: trục popularity có khoảng trống lớn do giá trị max quá cao.
- Yêu cầu bổ sung: không dùng thuật ngữ tiếng Anh cho quadrant labels.

# Final Prompt
Q4, dùng log scale là tốt, nhưng nên scale độ dài rộng ra ở trục popularity, vì tôi thấy có 1 khoảng trống không có giá trị gì hết của popularity. nghĩa là bạn đang đặt max của popularity quá lớn. ngoài ra dùng toàn bộ là tiếng việt (hidden gem, unicorn,...). ngoài ra không cần chú thích (thang log), xóa đi.

# Expected Output
- Q4 dùng miền trục X log theo phân vị dữ liệu thay vì để max cực trị kéo giãn chart.
- Nhãn 4 góc được Việt hóa hoàn toàn.
- Nhãn trục X không còn cụm "thang log".
- Ứng dụng không lỗi cú pháp.