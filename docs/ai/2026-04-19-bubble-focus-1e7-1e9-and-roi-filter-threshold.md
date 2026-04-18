# Request Summary
Dieu chinh bubble chart o tab Tai chinh de focus vao vung 10^7-10^9 tren ca hai truc, va cap nhat toan bo logic tinh ROI theo dieu kien chat luong du lieu: budget > 5,000 USD va revenue > 0.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-bubble-focus-1e7-1e9-and-roi-filter-threshold.md
- docs/ai/2026-04-19-bubble-focus-1e7-1e9-and-roi-filter-threshold.md

# Key Decisions
- Bubble chart Q9:
  - Co dinh shared log range = [7.0, 9.0] cho x va y.
  - Duong y=x ve theo visible_min=10^7 va visible_max=10^9 de can doi voi viewport.
- ROI filtering:
  - KPI ROI tong quan: budget > 5,000 va revenue > 0.
  - ROI trong Q4/Q5 va tab Tai chinh: cung dieu kien tren de tranh chia cho budget gan 0/0.

# Next Steps
- Neu can mo/rut gon viewport bubble chart theo feedback, co the doi range [7.0, 9.0] thanh [7.2, 9.1] hoac [6.8, 9.2].
- Theo doi so luong mau sau loc ROI de dam bao khong qua it diem cho mot so bo loc hep.