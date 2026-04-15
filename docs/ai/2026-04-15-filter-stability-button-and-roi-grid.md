# AI Handover - Filter Stability Button And ROI Grid

## Request Summary
Sua 3 van de cuoi cua dashboard: filter bi flicker/reset, chu nut reset khong trang on dinh, va thieu dashed guide lines tren ROI log axis.

## Files Changed
- src/main.py
- src/prompts/2026-04-15-filter-stability-button-and-roi-grid.md
- docs/ai/2026-04-15-filter-stability-button-and-roi-grid.md

## Key Decisions
- Cap nhat `dong_bo_loc_tuong_tac_tu_tab1` de bo qua chu ky su kien rong nhieu chart (empty-cycle noise), tranh viec xoa state ngoai y muon.
- Van giu duoc clear filter khi co su kien rong hop le tu 1 chart.
- Tang do uu tien CSS cho nut reset bang selector `button *` de ep text/fill mau trang.
- ROI x-axis giu log power notation va bo sung `dtick=1`, `showgrid=True`, `griddash='dash'`, `gridcolor` de hien thi cac guide lines theo 10^x.

## Validation
- Kiem tra syntax voi Problems API: khong con loi trong `src/main.py`.

## Next Steps
1. Chay thu thao tac click lien tiep: country -> language -> genre de xac nhan state khong bi mat.
2. Thu click vung trong tren tung chart de xac nhan clear filter dung chart.
3. Neu can, bo sung dong huong dan ngan trong sidebar ve cach clear filter bang click vung trong.
