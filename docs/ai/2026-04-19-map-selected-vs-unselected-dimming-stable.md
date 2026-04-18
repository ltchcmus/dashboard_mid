# Request Summary
User yeu cau: khi click chon US thi cac vung khac phai bi lam mo on dinh, khong quay lai mau goc.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-selected-vs-unselected-dimming-stable.md
- docs/ai/2026-04-19-map-selected-vs-unselected-dimming-stable.md

# Key Decisions
- Map color logic co 2 mode:
  - Co selected countries: dung color categorical theo `Trạng thái chọn`.
    - Đang chọn -> NETFLIX_RED
    - Khác -> #E5E7EB
  - Khong co selected countries: giu color continuous theo `Số lượng phim (log10)` nhu ban dau.
- Cach nay tach biet visual state khoi selected style tam cua Plotly, giu mau on dinh qua rerun.

# Next Steps
- Test chuoi thao tac: US -> China -> bo US -> bo China.
- Kiem tra map luon the hien dung selected/unselected theo sidebar state.