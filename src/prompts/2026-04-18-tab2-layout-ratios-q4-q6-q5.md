# Objective
Điều chỉnh bố cục Tab 2 để các biểu đồ nằm đúng hàng và đúng tỉ lệ theo yêu cầu mới.

# Context
- Người dùng yêu cầu:
  - Hàng 1: 2 biểu đồ Q4 cùng một dòng, Donut:Bar = 4:6.
  - Hàng 2: 2 biểu đồ còn lại cùng một dòng, Q6:Q5 = 6:4.
- Không thay đổi logic dữ liệu của từng biểu đồ, chỉ đổi layout.

# Final Prompt
ở tab 2, tôi muốn 2 biểu đồ của Q4 nằm trên cùng 1 dòng. và 2 biểu đồ còn lại nằm trên 1 dòng. tôi muốn tỉ lệ như sau: donut chiếm 4: bar chart chiếm 6; Q6 chiếm 6: Q5 chiếm 4.

# Expected Output
- Q4 Donut và Q4 Bar nằm trên cùng một hàng với `st.columns([4, 6])`.
- Q6 và Q5 nằm trên cùng một hàng với `st.columns([6, 4])`.
- App không lỗi cú pháp sau khi thay đổi bố cục.