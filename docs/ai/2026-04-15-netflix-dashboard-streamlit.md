# AI Handover - Netflix Dashboard Streamlit

## Request Summary
Xay dung hoan chinh dashboard Streamlit cho Netflix theo tai lieu thiet ke, giao dien tieng Viet, bo loc sidebar, KPI va 4 tab voi 12 bieu do.

## Files Changed
- src/main.py
- requirements.txt
- src/prompts/2026-04-15-netflix-dashboard-streamlit.md
- docs/ai/2026-04-15-netflix-dashboard-streamlit.md

## Key Decisions
- Dung movies.csv lam bang trung tam va movie_countries.csv cho bieu do ban do.
- Tien xu ly cot genres, cast, director bang str.split(',').explode() sau khi lam sach chuoi list.
- Bieu do theo thoi gian (ngan sach theo nam) dung mean de tranh lech do gioi han 1k phim/nam.
- Heatmap tuong quan dung seaborn + matplotlib; Word Cloud dung wordcloud.
- Them xu ly loi co ban cho truong hop thieu file du lieu va du lieu rong sau khi loc.

## Next Steps
1. Cai dat them dependency moi: matplotlib, seaborn, wordcloud.
2. Chay thu app bang streamlit run src/main.py.
3. Neu can, tich hop bo stopwords tieng Anh cho Word Cloud de tu khoa sach hon.
