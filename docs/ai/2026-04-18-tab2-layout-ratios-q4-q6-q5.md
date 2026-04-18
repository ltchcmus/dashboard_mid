# Request Summary
Người dùng yêu cầu chỉnh lại bố cục Tab 2 thành 2 hàng với tỉ lệ cột cụ thể cho từng nhóm biểu đồ.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-tab2-layout-ratios-q4-q6-q5.md
- docs/ai/2026-04-18-tab2-layout-ratios-q4-q6-q5.md

# Key Decisions
- Tách layout Tab 2 thành 2 phần rõ ràng:
  - Hàng 1: `q4_donut_col, q4_bar_col = st.columns([4, 6])`.
  - Hàng 2: `q6_col, q5_col = st.columns([6, 4])`.
- Giữ nguyên toàn bộ logic xử lý dữ liệu và chart config của Q4, Q5, Q6.
- Chỉ di chuyển vị trí render biểu đồ/insight theo cột mới.

# Next Steps
1. Mở dashboard và kiểm tra trực quan spacing/chiều cao của các chart trong Tab 2.
2. Nếu cần cân đối thêm trên màn hình nhỏ, cân nhắc thêm điều kiện responsive để chuyển về 1 cột trên mobile.