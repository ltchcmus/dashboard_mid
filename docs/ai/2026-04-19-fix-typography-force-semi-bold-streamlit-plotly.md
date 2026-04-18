# Request Summary
Thay toan bo CSS block trong main.py de ep buoc semi-bold (600) hien thi dung cho cac thanh phan phu tro tren Streamlit + Plotly, tranh bi ghi de boi inline style.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-fix-typography-force-semi-bold-streamlit-plotly.md
- docs/ai/2026-04-19-fix-typography-force-semi-bold-streamlit-plotly.md

# Key Decisions
- Thay the 100% block <style> theo noi dung user cung cap.
- Giu dung huong dan: KHONG chen cac key weight/font_weight vao fig.update_layout vi Plotly Python khong on dinh voi cac key nay.
- Dung selector .plotly svg text cung cac selector cu the de tang kha nang override.
- Dung !important cho cac nhom KPI label/caption/sidebar/plotly text de dam bao uu tien.

# Next Steps
- Hard reload trinh duyet (Ctrl+Shift+R) de xoa CSS cache cu.
- Kiem tra lai tren desktop/mobile de xac nhan hierarchy thi giac 400 -> 600 -> 700+ van ro rang.