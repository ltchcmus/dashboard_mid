# Objective
Loại bỏ warning Streamlit liên quan widget `khoang_nam_chon` và dời nút xóa lọc xuống dưới các dropdown trong sidebar.

# Context
- Warning xuất hiện khi slider có `key="khoang_nam_chon"` nhưng đồng thời truyền `value=` trong lúc key này cũng được set qua Session State.
- Người dùng muốn nút `Xóa tất cả bộ lọc` nằm dưới các dropdown.
- Cần tránh lỗi mutate widget-bound keys sau khi widget đã được tạo trong cùng lượt chạy.

# Final Prompt
Sửa `bo_loc_toan_cuc` trong `src/main.py`:
1. Khởi tạo `st.session_state["khoang_nam_chon"]` chỉ khi chưa tồn tại.
2. Slider năm chỉ dùng `key`, không truyền `value` để tránh warning policy.
3. Dời nút `Xóa tất cả bộ lọc` xuống dưới 3 dropdown.
4. Khi bấm nút reset, dùng `pending_filter_updates` để reset cả `quoc_gia_chon`, `the_loai_chon`, `ngon_ngu_chon`, `khoang_nam_chon`, rồi `st.rerun()`.

# Expected Output
- Không còn warning: widget key `khoang_nam_chon` vừa có default value vừa set qua Session State.
- Nút xóa lọc hiển thị bên dưới các dropdown.
- Reset filter hoạt động ổn định, không phát sinh lỗi session state.