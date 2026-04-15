# AI Handover - Tab1 Layout And Header Overlap Fix

## Request Summary
Sua viec header cao che mot phan chu va bo tri lai Tab 1 theo yeu cau trinh bay: map full-width hang tren, hai bieu do con lai nam ngang ben duoi. Treemap ngon ngu doi sang tone do.

## Files Changed
- src/main.py
- src/prompts/2026-04-15-tab1-layout-and-header-overlap-fix.md
- docs/ai/2026-04-15-tab1-layout-and-header-overlap-fix.md

## Key Decisions
- Tang padding top cho main block container len 4.5rem de tranh noi dung bi header che.
- Tai Tab 1, tach map ra thanh block rieng full-width, tang chieu cao map de trong tam storytelling ro hon.
- Chuyen 2 chart con lai vao st.columns(2) o hang duoi.
- Treemap ngon ngu chuyen color scale sang do: [#FFE5E8, #E50914].

## Next Steps
1. Chay streamlit va kiem tra thuc te tren cac kich thuoc man hinh.
2. Neu can, tinh chinh them height map/treemap/bar de can doi bo cuc khi trinh chieu.
