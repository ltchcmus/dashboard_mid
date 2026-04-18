# Request Summary
User yeu cau:
1) Country map selected gradient can den mau do dam hon.
2) Treemap ngon ngu khong zoom full khi click 1 tile.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-darkred-selected-and-lock-treemap-drill.md
- docs/ai/2026-04-19-map-darkred-selected-and-lock-treemap-drill.md

# Key Decisions
- Map:
  - Giu co che gia_tri_mau cho selected/unselected.
  - Doi color_continuous_scale endpoint selected sang #80060B de cho do dam hon.
- Treemap:
  - Them update_traces(maxdepth=1, pathbar={"visible": False}, root_color=CHART_BG)
  - Muc tieu: han che drill/zoom khi click, uu tien click de chon filter.

# Next Steps
- Test thao tac: click English -> click French -> click Spanish.
- Neu moi truong Plotly van drill do han che client, can can nhac doi visualization ngon ngu sang bar chart de co click behavior on dinh 100%.