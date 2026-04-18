# Request Summary
Refactor luong bo loc tuong tac theo yeu cau: bo UI bo loc tuong tac cu, dong bo truc tiep chart tab 1 voi sidebar multiselect bang co che toggle add/remove.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-crossfilter-toggle-sync-chart-sidebar.md
- docs/ai/2026-04-19-crossfilter-toggle-sync-chart-sidebar.md

# Key Decisions
- Session state keys duoc chuan hoa ve:
  - quoc_gia_chon
  - ngon_ngu_chon
  - the_loai_chon
- Them helper cap_nhat_loc_toggle(key_state, new_items) de toggle item theo click.
- dong_bo_loc_tuong_tac_tu_tab1 chi trigger rerun khi thuc su co thay doi danh sach chon.
- bo_loc_toan_cuc chuyen Quoc gia/Ngon ngu sang multiselect va doc gia tri tu session_state.
- Xoa hoan toan ham hien_thi_trang_thai_loc_tuong_tac va loi goi trong main.

# Next Steps
- Test tay voi click 1 item, click lai item do, va multi-select tren tung chart (Map/Treemap/Bar) de xac nhan toggle dung.
- Neu can tranh dao trang thai do event lap lai, co the them co che de-dup theo dau van tay selection o lan tiep theo.