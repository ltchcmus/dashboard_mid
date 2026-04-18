# Objective
Sua loi click vao quoc gia tren ban do Tab 1 nhung khong duoc cap nhat vao filter sidebar.

# Context
Sau khi chuyen sang co che crossfilter chart -> sidebar, user bao click map khong add selected item vao multiselect. Nguyen nhan kha nang cao la parser su kien Plotly chi xu ly dict, trong khi payload co the la object state.

# Final Prompt
Fix parser event trong trich_gia_tri_tu_su_kien_plotly de:
- Ho tro ca dict va object event payload.
- Lay duoc selection.points an toan.
- Xu ly customdata/location dang list/tuple/np.ndarray.

# Expected Output
- Click vao map se trich duoc country value va toggle vao session_state quoc_gia_chon.
- Sidebar multiselect Quoc gia duoc cap nhat ngay sau rerun.
- Khong phat sinh loi type khi event payload khac kieu.