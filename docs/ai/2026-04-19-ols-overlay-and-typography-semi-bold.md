# Request Summary
Người dùng yêu cầu chỉnh 2 nhóm việc: (1) đường OLS ở scatter đạo diễn phải luôn nằm trên cùng, không bị che bởi điểm; (2) áp dụng typography semi-bold có chọn lọc theo hierarchy 400-600-700 và loại bỏ icon lạ.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-ols-overlay-and-typography-semi-bold.md
- docs/ai/2026-04-19-ols-overlay-and-typography-semi-bold.md

# Key Decisions
- Giữ OLS là trace được thêm sau cùng trong figure scatter đạo diễn để đảm bảo layer hiển thị trên marker.
- Giảm opacity marker scatter để đường OLS dễ nhìn hơn tại vùng giao cắt.
- Chuẩn hóa typography:
  - KPI label: 600
  - KPI value: 700
  - Axis title và legend title (Plotly CSS): 600
  - Sidebar label/caption và caption chung: 600
  - Giữ tab/nút/header ở mức bold nổi bật.
- Bỏ emoji ở tab labels và page icon.

# Next Steps
- Kiểm tra thực tế trên giao diện desktop/mobile để xác nhận không có hiện tượng vỡ dòng ở tab và tiêu đề trục.
- Nếu cần, có thể tinh chỉnh thêm cỡ chữ tab và khoảng cách legend cho màn hình nhỏ.