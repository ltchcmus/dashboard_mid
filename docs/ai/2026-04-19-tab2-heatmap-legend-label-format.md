# Request Summary
User yeu cau format lai legend cua heatmap tab 2 vi dang hien text mac dinh khong phu hop (sum of So_luong).

# Files Changed
- src/main.py
- src/prompts/2026-04-19-tab2-heatmap-legend-label-format.md
- docs/ai/2026-04-19-tab2-heatmap-legend-label-format.md

# Key Decisions
- Set `histfunc="sum"` ro rang trong density_heatmap.
- Them `labels` tieng Viet cho `So_luong` va `ROI_trung_binh`.
- Ep colorbar title bang `fig_hist.update_coloraxes(colorbar_title_text="Tổng số phim")` de loai bo text he thong.

# Next Steps
- Mo tab 2 va kiem tra colorbar da hien "Tổng số phim".
- Neu can, co the doi ten thanh "Số phim" cho gon hon.