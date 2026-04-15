# AI Handover - Crossfilter Interactive Charts

## Request Summary
Bo sung tinh nang tuong tac de click tren chart co the loc dong bo cac chart khac trong dashboard.

## Files Changed
- src/main.py
- src/prompts/2026-04-15-crossfilter-interactive-charts.md
- docs/ai/2026-04-15-crossfilter-interactive-charts.md

## Key Decisions
- Dung st.plotly_chart(..., on_select='rerun') cho 3 chart dieu huong trong Tab 1:
  - Map quoc gia
  - Treemap ngon ngu
  - Bar the loai
- Luu lua chon vao st.session_state: selected_countries, selected_languages, selected_genres.
- Ap dung bo loc tuong tac sau bo loc sidebar, roi render lai toan bo KPI + cac tab.
- Them panel trong sidebar hien trang thai bo loc tuong tac va nut "Xoa loc tuong tac".

## Next Steps
1. Test thao tac click/bo chon tren tung chart de xac nhan hanh vi voi du lieu thuc te.
2. Neu can mo rong, co the them on_select cho cac chart o tab 2-4 va map sang cac truong domain phu hop.
