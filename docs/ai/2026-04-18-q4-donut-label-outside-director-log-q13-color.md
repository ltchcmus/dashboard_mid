# Request Summary
Cap nhat 3 khu vuc trong dashboard:
1) Q4 donut: cai thien hien thi chu thich cho nhom nho va sap xep thu tu bucket theo logic chat luong.
2) Tab sang tao - chart dao dien: bat log scale cho truc doanh thu trung binh va bo ma hoa mau gradient theo diem danh gia.
3) Q13: doi mau cot sang bien mau da dinh nghia (khong hardcode mau RGBA).

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q4-donut-label-outside-director-log-q13-color.md
- docs/ai/2026-04-18-q4-donut-label-outside-director-log-q13-color.md

# Key Decisions
- Q4 donut:
  - Them `donut_order` de hien thi theo thu tu: Xuat sac -> Tot -> Kha -> TB -> Kem.
  - Dung `category_orders` + `sort=False` de giu dung thu tu, khong bi sap theo gia tri.
  - Chuyen `textposition` sang `auto` de Plotly day label ra ngoai khi slice qua nho.
  - Dung `uniformtext_minsize`/`uniformtext_mode` de tranh label bi roi mat.
- Director scatter:
  - Loc du lieu co `doanh_thu_trung_binh > 0` de log axis hop le.
  - Bo `color=diem_danh_gia_trung_binh` va `color_continuous_scale`.
  - Dung marker 1 mau tu bien `NETFLIX_GOLD` va dat x-axis `type=log`.
- Q13 bar:
  - Thay `marker_color` hardcode bang `marker={"color": NETFLIX_GOLD, "opacity": 0.72}`.

# Verification
- Chay compile check: `python3 -m py_compile src/main.py` (thuc hien bang script inline) -> OK
- VS Code Problems cho src/main.py -> No errors found

# Next Steps
1. Chay app va kiem tra bang mat thuong tren cac bo loc de xac nhan label donut nho da de doc hon.
2. Neu can, tinh chinh them nguong hiển thi label (texttemplate hoac pull) cho cac slice rat nho (<3%).
3. Can nhac dong bo mau bar Q13 voi mot semantic token rieng neu doi palette tiep theo.
