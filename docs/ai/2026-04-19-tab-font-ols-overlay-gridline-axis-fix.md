# Request Summary
User yeu cau 3 sua nhanh giao dien/plotly:
- Tang co chu va do dam cho tab labels.
- Xu ly OLS line tab 4 khong bi che boi data points.
- Khoi phuc gridline va x/y axis cho chart tuong quan ngan sach-doanh thu o tab 3.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-tab-font-ols-overlay-gridline-axis-fix.md
- docs/ai/2026-04-19-tab-font-ols-overlay-gridline-axis-fix.md

# Key Decisions
- Tab labels: set font-size lon hon va weight cao hon, selected tab nhan manh hon.
- OLS tab 4: doi sang ve line bang shape voi layer='above' de chac chan nam tren marker.
- Tab 3 bubble: ep showgrid + showline + linecolor cho ca xaxis/yaxis, dat title truc ro rang.

# Next Steps
- Kiem tra lai tren browser sau hard refresh de cap nhat CSS/Plotly cache.
- Neu can, tinh chinh tiep do day OLS line hoac do dam tab labels theo gu nhin slide.