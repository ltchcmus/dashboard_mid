# Request Summary
User yeu cau fix 2 van de treemap ngon ngu:
1) Van bi zoom full tile khi click.
2) Muon color scale theo log, khong theo gia tri goc.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-treemap-no-zoom-and-log-color-scale.md
- docs/ai/2026-04-19-treemap-no-zoom-and-log-color-scale.md

# Key Decisions
- Treemap data source doi sang movies_lang (khong ap filter ngon_ngu_chon), chi ap bo loc nam/quoc_gia/the_loai.
  - Muc tieu: sau khi click 1 ngon ngu, treemap van hien cac ngon ngu con lai de click tiep.
- Them cot `Số lượng phim (log10)` cho treemap color.
- Colorbar treemap doi tick text sang don vi goc (10^x) de de hieu.

# Next Steps
- Test: click English -> click French -> click Spanish, xac nhan khong bi full 1 tile.
- Test filter quoc gia/the loai ket hop voi treemap ngon ngu, xac nhan map mau theo log van on dinh.