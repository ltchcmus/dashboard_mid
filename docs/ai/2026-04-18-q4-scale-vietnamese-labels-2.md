# Request Summary
Người dùng yêu cầu sửa phần Q13 để biểu đồ kép dễ đọc hơn: trục rõ, grid bớt rối, màu semantic nhất quán, hover/legend gọn, bố cục tối ưu.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-scale-vietnamese-labels-2.md
- docs/ai/2026-04-18-q4-scale-vietnamese-labels-2.md

# Key Decisions
- Cập nhật bar màu `rgba(0, 128, 128, 0.7)` và hover text theo mẫu yêu cầu.
- Cập nhật line màu `NETFLIX_RED`, width=3 và marker đỏ size=8.
- Tất cả axis titles + tick labels chuyển sang `TEXT_DARK`.
- Giữ grid chỉ ở Y trái với màu `#E5E7EB`, kiểu `dot`; tắt grid Y phải.
- Cố định Y phải range [0,10] để tránh line bị dẹt theo auto-scale không ổn định.
- Legend đặt top-right, nền trắng mờ, viền xám nhẹ, font màu TEXT_DARK.
- Thêm `barmode="group"` và giảm margin dưới để tiết kiệm không gian.

# Next Steps
1. Chạy Streamlit để kiểm tra trực quan Q13 ở các filter khác nhau.
2. Nếu line vẫn cảm giác dẹt ở vài filter, có thể thêm dynamic range cho Y trái hoặc chuẩn hóa popularity trước khi vẽ.