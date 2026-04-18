# Request Summary
Người dùng yêu cầu chuẩn hóa hệ thống màu dashboard Netflix bằng semantic color system thống nhất, thay thế các màu rời rạc trong `main.py`.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-semantic-color-system-dashboard.md
- docs/ai/2026-04-18-semantic-color-system-dashboard.md

# Key Decisions
- Khai báo bộ màu semantic ở đầu file:
  - `SEQ_COUNT` cho dữ liệu tuần tự (số lượng, mức độ phổ biến, doanh thu).
  - `DIVERGE_QUALITY` cho dữ liệu chất lượng/ROI (thấp -> trung tính -> cao).
  - `CAT_GENRE` cho phân loại danh mục (genre/language/director groups).
  - `NEUTRAL_GREY` cho nhóm "Others".
- Thay các `color_continuous_scale`, `color_discrete_map`, `color_discrete_sequence` rải rác trong các tab để dùng semantic constants.
- Chuẩn hóa các chart quan trọng:
  - Tab 1 choropleth/treemap/bar: chuyển sang `SEQ_COUNT`.
  - Tab 2 donut/bar/heatmap/error-bar: dùng `QUALITY_BUCKET_COLORS`, `DIVERGE_QUALITY`, `SEQ_COUNT` theo đúng ý nghĩa.
  - Tab 3 ROI/bar/line/bubble/box: dùng `DIVERGE_QUALITY`, `CAT_GENRE`, `NEUTRAL_GREY`.
  - Tab 4 director/cast/genre-mix: dùng semantic scales thay cho màu hardcode.
- Giữ nguyên logic dữ liệu và chỉ refactor về mặt biểu diễn màu.

# Next Steps
1. Chạy Streamlit và rà trực quan từng tab để kiểm tra tính nhất quán màu theo ngữ nghĩa.
2. Nếu muốn nâng thêm accessibility, có thể bổ sung pattern/hatching hoặc legend phụ cho các biểu đồ màu gần nhau.