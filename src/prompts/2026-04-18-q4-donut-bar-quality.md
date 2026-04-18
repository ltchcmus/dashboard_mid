# Objective
Cập nhật Q4 theo đặc tả mới trong design_question_2.md: chuyển từ scatter plot sang bố cục 2 panel gồm Donut chart + Horizontal Bar chart.

# Context
- Đặc tả mới yêu cầu Q4 trả lời: phân bố chất lượng tổng thể và thể loại chiếm ưu thế trong nhóm phim chất lượng cao.
- Layout yêu cầu: st.columns([1,2]) với donut ở trái và bar chart ở phải.
- Dữ liệu cho bar chart: phim có vote_average >= 7.5, top 10 thể loại.

# Final Prompt
Tôi vừa thay đổi câu 4, giúp tôi chỉnh sửa lại cho phù hợp với yêu cầu.

# Expected Output
- Q4 được thay hoàn toàn theo mẫu Donut + Horizontal Bar.
- Donut dùng bucket điểm 0-5, 5-6, 6-7, 7-8, 8-10.
- Bar chart hiển thị Top 10 thể loại trong nhóm rating >= 7.5, hover có avg_popularity và avg_roi.
- Mỗi chart có phần expander insight.
- Code compile thành công.