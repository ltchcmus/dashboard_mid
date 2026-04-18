# Request Summary
User bao 2 issue con lai tren map:
- Chon US xong chon China thi US bi nhat mau du van selected.
- Click lai US lan 2 thi map reset mau nhung US van selected.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-click-toggle-visual-state-fix.md
- docs/ai/2026-04-19-map-click-toggle-visual-state-fix.md

# Key Decisions
- Dedupe event refine:
  - Them chart_event_skip_once theo tung key.
  - Khi signature trung va skip_once=True: chi skip 1 lan, sau do ha skip_once=False.
  - Click lai cung signature lan sau se duoc xu ly toggle binh thuong.
- Dong bo visual map:
  - Tao map_key_suffix theo danh sach quoc_gia_chon.
  - Dung key dong cho st.plotly_chart map de remount widget khi selection doi, tranh stale selected visual state gay nhat mau sai.

# Next Steps
- Test chuoi thao tac: US -> China -> click lai US.
- Xac nhan sidebar va map color state khop nhau sau moi thao tac.