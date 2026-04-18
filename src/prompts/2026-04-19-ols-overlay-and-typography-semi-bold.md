# Objective
Đảm bảo đường OLS ở biểu đồ scatter đạo diễn luôn nhìn rõ và không bị che bởi marker; đồng thời áp dụng phân cấp typography 400-600-700 có chọn lọc cho dashboard.

# Context
- Scatter đạo diễn (tab Sáng tạo) đã có OLS nhưng người dùng phản hồi bị chìm dưới điểm dữ liệu.
- UI cần bỏ icon lạ và chuẩn hóa độ đậm chữ theo phân cấp:
  - 700: tiêu đề/tab/nút/giá trị KPI nổi bật
  - 600: KPI label, nhãn phụ trợ, axis title, legend title, caption
  - 400: body text mặc định

# Final Prompt
1. Ở scatter plot đạo diễn tab 4, bổ sung giúp tôi 1 đường OLS màu đỏ (line này phải nằm ở trên cùng, không bị che bởi các chấm).
2. Xóa đi toàn bộ các icon lạ.
3. Áp dụng font semi-bold (600) có chọn lọc theo phân cấp typography đã mô tả.

# Expected Output
- Đường OLS màu đỏ hiển thị nổi, rõ trên nền scatter.
- Không còn emoji/icon ở tab/page icon.
- CSS và layout Plotly phản ánh rõ hierarchy 400-600-700 mà không làm nặng toàn bộ giao diện.