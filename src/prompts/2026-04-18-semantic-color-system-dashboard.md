# Objective
Chuẩn hóa hệ thống màu sắc dashboard theo semantic color system thống nhất cho toàn bộ biểu đồ.

# Context
- `main.py` dùng nhiều bảng màu rời rạc theo từng chart.
- Mục tiêu là gán màu theo ngữ nghĩa dữ liệu (Sequential, Diverging, Categorical) và giữ nhận diện Netflix một cách có chủ đích.
- Yêu cầu áp dụng xuyên suốt các tab, không để màu inline rời rạc gây khó so sánh.

# Final Prompt
Chuẩn hóa Semantic Color System duy nhất cho dashboard: khai báo constants ở đầu file và thay toàn bộ color scales/maps trong charts theo ngữ nghĩa dữ liệu.

# Expected Output
- Có các hằng số màu semantic ở đầu file: `SEQ_COUNT`, `DIVERGE_QUALITY`, `CAT_GENRE`, `NEUTRAL_GREY`, cùng brand colors.
- Các chart ở Tab 1-4 dùng lại semantic constants thay vì màu inline.
- Các biểu đồ count/revenue/popularity dùng sequential scale; quality/ROI dùng diverging scale; genre/language dùng categorical.
- Mã compile thành công.