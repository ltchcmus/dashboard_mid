# AI Handover - Crossfilter Persistence And ROI Log Ticks

## Request Summary
Hoan thien hanh vi cross-filter va UI theo 4 yeu cau: them khoang dem heading, giu filter khong bi mat khi click chart khac, style nut xoa loc, va doi truc ROI sang log power notation.

## Files Changed
- src/main.py
- src/prompts/2026-04-15-crossfilter-persistence-and-roi-logticks.md
- docs/ai/2026-04-15-crossfilter-persistence-and-roi-logticks.md

## Key Decisions
- Tab 1: gom de xuat selection tu 3 chart va dong bo state trong mot ham trung tam `dong_bo_loc_tuong_tac_tu_tab1`.
- Neu co chart vua chon gia tri moi, khong de event rong cua chart khac xoa filter hien tai (tranh mat country khi click language).
- Van cho phep clear filter bang event rong khi nguoi dung click vung trong chart (khong co chart nao co selection moi cung luc).
- Nut `Xóa lọc tương tác` style nen do/chu trang va hover do dam hon.
- ROI chart: loc du lieu duong, dat x-axis log va hien thi exponent theo power notation.
- Padding top main block tang them 0.5rem de tach heading khoi noi dung.

## Next Steps
1. Test thao tac click chuoi: country -> language -> genre -> click vung trong de clear tung filter.
2. Neu can, bo sung huong dan nho o sidebar mo ta quy tac clear theo click vung trong chart.
