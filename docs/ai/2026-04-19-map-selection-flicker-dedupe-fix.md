# Request Summary
User bao map bi nhay select/unselect lien tuc khi chon quoc gia. Nguyen nhan la event selection bi xu ly lap lai qua cac lan rerun trong khi logic dang toggle.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-selection-flicker-dedupe-fix.md
- docs/ai/2026-04-19-map-selection-flicker-dedupe-fix.md

# Key Decisions
- Khoi tao state moi chart_event_signature trong khoi_tao_loc_tuong_tac.
- Trong dong_bo_loc_tuong_tac_tu_tab1:
  - Tao signature tu danh sach values da sort.
  - Neu signature trung voi signature truoc do cua key -> skip.
  - Neu selection rong -> reset signature key ve None.
  - Chi toggle khi co event moi thuc su.

# Next Steps
- Test click map voi 1 quoc gia: khong con nhay dao trang thai.
- Test click them quoc gia thu 2, thu 3: van cong don nhu mong doi.
- Test deselect roi select lai cung quoc gia: van hoat dong dung.