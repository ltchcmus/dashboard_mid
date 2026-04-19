# Objective
Sửa lỗi `ValueError: Bin edges must be unique` ở biểu đồ Q5 (tab chất lượng) và bổ sung nút xóa toàn bộ bộ lọc đang chọn trong sidebar.

# Context
- Ứng dụng Streamlit dashboard trong `src/main.py`.
- Q5 đang dùng `pd.qcut` trên dữ liệu ngân sách đã rank để chia tứ phân vị.
- Trong các trường hợp dữ liệu rất ít hoặc biên quantile trùng nhau, `qcut` có thể ném lỗi.
- Người dùng cần thêm thao tác một chạm để xóa các filter hiện tại.

# Final Prompt
Sửa `src/main.py` theo 2 yêu cầu:
1. Ở `ve_tab_chat_luong` (Q5), làm logic chia nhóm ngân sách bằng `qcut` an toàn với trường hợp dữ liệu ít hoặc biên trùng, tránh crash runtime.
2. Ở `bo_loc_toan_cuc`, thêm một nút sidebar để xóa toàn bộ filter hiện tại (quốc gia, thể loại, ngôn ngữ) và đồng bộ lại state liên quan.

# Expected Output
- Ứng dụng không còn crash tại Q5 vì `qcut`.
- Nút “Xóa tất cả bộ lọc” hoạt động ngay, trả filter về rỗng (và reset năm về full range), UI cập nhật ổn định sau rerun.
- Không phát sinh lỗi tĩnh mới trong `src/main.py`.