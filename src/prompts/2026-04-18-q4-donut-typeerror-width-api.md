# Objective
Khắc phục lỗi runtime ở Q4 sau khi chuyển sang Donut + Bar và đồng thời xử lý cảnh báo API mới của Streamlit về `use_container_width` trong `st.plotly_chart`.

# Context
- Runtime báo lỗi tại Q4: `TypeError: '>' not supported between instances of 'str' and 'int'`.
- Lỗi xuất hiện khi lọc `donut_data["Số lượng phim"] > 0` do cột bị rename nhầm từ nhãn bucket (chuỗi).
- Streamlit cảnh báo thay `use_container_width=True` bằng `width='stretch'` cho plotly chart.

# Final Prompt
Fix traceback ở Q4 và cập nhật API hiển thị width cho plotly chart.

# Expected Output
- Q4 không còn lỗi TypeError khi lọc donut_data.
- Cột `Số lượng phim` của donut được tạo đúng kiểu số.
- Các lệnh `st.plotly_chart(..., use_container_width=True)` trong file được chuyển sang `width="stretch"`.
- File compile thành công.