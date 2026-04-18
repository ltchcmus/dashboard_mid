# Request Summary
User muon bieu do Q6 tab 2 doi encode mau tu diem trung binh sang variance cua tung the loai.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-q6-variance-color-encoding.md
- docs/ai/2026-04-19-q6-variance-color-encoding.md

# Key Decisions
- Tinh variance don gian tu do_lech_chuan: `phuong_sai = std^2`.
- Marker color doi sang `genre_stat["phuong_sai"]`.
- Colorbar title doi thanh `Phương sai`.
- Hover bo sung gia tri phuong sai de nguoi dung de dien giai.

# Next Steps
- Neu can nhan manh “on dinh = variance thap”, co the dao nguoc colorscale de variance thap noi bat mau tich cuc hon.
- Co the them format don vi cho variance (3 chu so thap phan) tuy theo readability.