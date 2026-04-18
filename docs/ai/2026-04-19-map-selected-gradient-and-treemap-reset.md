# Request Summary
User yeu cau:
1) Country map selected dung gradient.
2) Language treemap khong bi phong to kẹt sau khi click 1 ngon ngu.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-selected-gradient-and-treemap-reset.md
- docs/ai/2026-04-19-map-selected-gradient-and-treemap-reset.md

# Key Decisions
- Map selected-gradient mode:
  - qg_dem[gia_tri_mau] = -1 cho unselected, = log10(count) cho selected.
  - color scale: gray -> light red -> Netflix red.
  - hide colorbar de giao dien gon.
- Treemap reset behavior:
  - key chart_tree_ngon_ngu dung suffix hash tu ngon_ngu_chon.
  - moi lan selection list doi, chart remount va bo trang thai zoom cu.

# Next Steps
- Test chuoi: chon US -> China -> Brazil de xem gradient selected.
- Test treemap: click English, sau rerun click French/Spanish tiep tuc khong bi kẹt zoom.