# Objective
Điều chỉnh Q4 (Tab 2) để bỏ bubble size và hiển thị log-scale trục popularity gọn hơn, tránh khoảng trống lớn bên phải biểu đồ.

# Context
- Người dùng phản hồi Q4 vẫn còn khoảng trắng lớn ở phía phải trục popularity.
- Nguyên nhân thực tế: điểm chú thích quadrant đặt quá xa (theo median * 1.45) có thể kéo miền trục X rộng hơn dữ liệu.
- Người dùng yêu cầu không dùng bubble cho Q4.

# Final Prompt
Ở Q4, không cần dùng bubble cho câu này. Hãy nhìn cách tab 3, câu top 10 phim có tỉ lệ lợi nhuận cao, cách dùng log để áp dụng hiển thị scale vừa đủ (vì hiện tại biểu đồ Q4, mức cao nhất là 10^4, tuy nhiên 10^4 không phải là giá trị lớn nhất trên trục, mà trục bị bỏ trống 1 khoảng bên phải lớn).

# Expected Output
- Q4 không dùng size bubble; marker có kích thước cố định.
- Trục X giữ log_x=True, tick format mũ 10 bằng Unicode superscript.
- Miền hiển thị không bị kéo giãn do annotation, giảm khoảng trắng bên phải.
- Vẫn giữ phân vùng trung vị và nhãn tiếng Việt.
- Ứng dụng chạy không lỗi cú pháp.