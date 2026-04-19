# Request Summary
- Sửa lỗi runtime `ValueError: Bin edges must be unique` phát sinh ở Q5 khi chia nhóm ngân sách bằng `pd.qcut`.
- Thêm nút để xóa các bộ lọc hiện tại trong sidebar.

# Files Changed
- `src/main.py`

# Key Decisions
- Q5 binning:
  - Giữ hướng tiếp cận rank-before-qcut.
  - Thêm nhánh bảo vệ theo số nhóm mục tiêu `min(4, nunique(rank))`.
  - Nếu dữ liệu không đủ tạo >=2 nhóm hoặc `qcut` trả toàn `NaN`, fallback về một nhãn duy nhất `Q1 (Thấp)` để tránh crash.
  - Dùng `duplicates="drop"` để xử lý biên quantile trùng.
- Sidebar clear filter:
  - Thêm nút `Xóa tất cả bộ lọc` trong `bo_loc_toan_cuc`.
  - Reset các state filter (`quoc_gia_chon`, `the_loai_chon`, `ngon_ngu_chon`) qua `pending_filter_updates`.
  - Reset slider năm `khoang_nam_chon` về `(nam_min, nam_max)`.
  - Reset `chart_event_signature` và `chart_event_skip_once` để tránh tác động từ event cũ.
  - Gọi `st.rerun()` ngay sau reset để đồng bộ UI.

# Next Steps
- Kiểm thử thủ công trên app:
  - Trường hợp dữ liệu Q5 rất ít (1-2 điểm) không còn lỗi.
  - Nút xóa bộ lọc trả dashboard về trạng thái chưa lọc.
  - Cross-filter từ tab 1 vẫn hoạt động bình thường sau thao tác reset.