# Request Summary
Người dùng yêu cầu tinh chỉnh riêng Q4: giảm khoảng trống ở trục popularity (log scale), đổi toàn bộ nhãn quadrant sang tiếng Việt, và xóa chú thích "thang log".

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-scale-vietnamese-labels.md
- docs/ai/2026-04-18-q4-scale-vietnamese-labels.md

# Key Decisions
- Dùng dải hiển thị trục X theo phân vị 1%-99% của popularity để tránh bị kéo giãn bởi outlier.
- Giữ dữ liệu điểm, chỉ điều chỉnh range hiển thị của trục log.
- Tạo tick log động theo miền hiển thị thực tế, vẫn giữ định dạng mũ 10^n bằng chữ số superscript.
- Việt hóa toàn bộ nhãn phân vùng:
  - 🟢 Kỳ lân
  - 🔵 Viên ngọc ẩn
  - 🟡 Đại chúng
  - 🔴 Hiệu suất thấp
- Bỏ cụm "(thang log)" ở label/title trục X theo yêu cầu.

# Next Steps
1. Chạy streamlit và kiểm tra trực quan Q4 với vài bộ lọc khác nhau để xác nhận khoảng trống đã giảm.
2. Nếu cần giữ lại outlier trên màn hình, có thể thêm toggle "Hiển thị outlier" để đổi giữa full range và quantile range.