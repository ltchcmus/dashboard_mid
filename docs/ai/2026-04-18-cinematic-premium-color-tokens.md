# Request Summary
Người dùng yêu cầu điều chỉnh hệ thống màu sang phong cách Cinematic Premium và chỉ thay phần biến màu/palette ở đầu file, không chạm logic dữ liệu.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-cinematic-premium-color-tokens.md
- docs/ai/2026-04-18-cinematic-premium-color-tokens.md

# Key Decisions
- Giữ nguyên `NETFLIX_RED` (#E50914) làm màu thương hiệu.
- Đổi `NETFLIX_TEAL` thành amber/gold (#FFB100) để giảm cảm giác teal-heavy.
- Đổi `SEQ_COUNT` sang Slate Grey gradient: #F1F5F9 -> #94A3B8 -> #334155.
- Giữ `DIVERGE_QUALITY` theo cấu trúc semantic: đỏ -> trung tính -> gold.
- Thiết kế lại `CAT_GENRE` thành 8 màu muted, tránh neon/chói.
- Cập nhật `QUALITY_BUCKET_COLORS` theo dải đỏ -> trung tính -> gold/green, với "Xuất sắc" = emerald (#00A651).
- Không thay đổi bất kỳ logic biểu đồ/xử lý dữ liệu nào ngoài phần constants.

# Next Steps
1. Chạy dashboard và kiểm tra cảm nhận thị giác tổng thể giữa các tab.
2. Nếu muốn tăng nhất quán thương hiệu hơn nữa, có thể đồng bộ thêm CSS gradient/background sang bộ token mới.