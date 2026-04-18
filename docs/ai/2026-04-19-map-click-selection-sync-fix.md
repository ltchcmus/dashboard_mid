# Request Summary
User hoi tai sao click country tren map khong vao duoc filter dropdown. Da fix parser su kien Plotly de doc duoc event payload dang object (khong chi dict).

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-click-selection-sync-fix.md
- docs/ai/2026-04-19-map-click-selection-sync-fix.md

# Key Decisions
- Trong trich_gia_tri_tu_su_kien_plotly:
  - Ho tro lay selection tu dict, object co thuoc tinh selection, hoac object co get().
  - Ho tro lay points tu dict/object.
  - Chuan hoa gia tri customdata khi la list/tuple/np.ndarray.
- Khong thay doi logic toggle/rerun; chi tang do ben parser de map click co du lieu dau vao.

# Next Steps
- Test thu click mot quoc gia tren map, click lai de deselect, va ket hop click treemap/bar de dam bao dong bo da chart hoat dong on dinh.