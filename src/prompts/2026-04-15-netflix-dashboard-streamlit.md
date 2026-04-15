# Prompt Log - Netflix Dashboard Streamlit

## Objective
Xay dung dashboard Streamlit ke chuyen du lieu Netflix theo tai lieu thiet ke voi 4 tab, 12 bieu do, bo loc toan cuc, KPI va giao dien tieng Viet.

## Context
- Nguon du lieu: data/processed/movies.csv, movie_countries.csv.
- Rang buoc: su dung streamlit, pandas, plotly.express.
- Cac bieu do theo thoi gian bat buoc dung mean thay vi sum.
- Cac cot genres va cast can duoc tach bang str.split(',').explode() khi phan tich.
- UI chi dung tone sang, diem nhan Netflix do #E50914 va teal #008080.

## Final Prompt
"Lap trinh dashboard Python + Streamlit theo docs/human/design_question.md, su dung bo loc nam/the loai/ngon ngu, KPI tong quan, giao dien tieng Viet 100%, xu ly loi co ban khi du lieu trong sau loc."

## Expected Output
- Ung dung Streamlit chay tu src/main.py.
- Co 4 tab: Toan canh, Chat luong, Tai chinh ROI, Sang tao.
- Day du 12 bieu do theo logic tai lieu.
- Co thong bao than thien khi khong co du lieu.
