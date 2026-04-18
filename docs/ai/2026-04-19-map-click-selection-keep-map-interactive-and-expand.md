# Request Summary
User muon 2 cai tien:
1) Chon 1 quoc gia tren map xong van click them quoc gia khac duoc (khong bi trang cac nuoc con lai).
2) Map mo rong ra toi da trong o hien thi.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-click-selection-keep-map-interactive-and-expand.md
- docs/ai/2026-04-19-map-click-selection-keep-map-interactive-and-expand.md

# Key Decisions
- Map data source duoc tach khoi country filter:
  - Tao movies_map tu du_lieu goc.
  - Ap dung bo loc nam + ngon ngu + the loai tu session_state.
  - KHONG ap country filter vao data map, de giu kha nang click bo sung quoc gia.
- Them key cho slider nam (khoang_nam_chon) de map co the doc cung bo loc nam.
- Mo rong map:
  - height tang len 760
  - margin top giam con 48
  - projection_scale tang nhe 1.12
  - tat coastlines/frame de map thoang hon.

# Next Steps
- Test click lien tiep 2-3 quoc gia tren map va xac nhan multiselect duoc cong don.
- Neu can map to hon nua, co the tang height 820 va projection_scale 1.18.