# Request Summary
User yeu cau Q5 tab 2:
1) Doi ten bieu do vi noi dung khong phai ROI.
2) Chia nhom ngan sach theo tu phan vi, giu nguyen nhom diem so.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-tab2-q5-rename-and-budget-quartiles.md
- docs/ai/2026-04-19-tab2-q5-rename-and-budget-quartiles.md

# Key Decisions
- Dung `pd.qcut` voi q=4 va `duplicates='drop'` de tao nhom ngan sach theo quartile an toan.
- Labels quartile: Q1(Thấp), Q2, Q3, Q4(Cao).
- Xoa tinh ROI khoi pipeline Q5 va doi title thanh "Phân bố số lượng phim theo điểm số và ngân sách".

# Next Steps
- Mo tab 2 de kiem tra truc X hien dung 4 nhom tu phan vi.
- Neu can thu gon ten nhom quartile, co the doi thanh Q1/Q2/Q3/Q4 de gon hon tren man hinh nho.