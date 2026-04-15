# Prompt Log - Filter Stability Button And ROI Grid

## Objective
Hoan tat 3 yeu cau con lai: giu cross-filter on dinh khong tu reset, ep mau chu nut reset thanh trang, va bo sung duong luoi net dut theo moc 10^x tren truc ROI log.

## Context
- User bao filter co hien tuong nhay 1 giay roi mat.
- Mau chu trong nut reset van hien den tren mot so lan render.
- ROI da la log axis nhung chua co dashed guide lines theo cap so nhan.

## Final Prompt
"Fix triet de 3 loi con lai: reset button text phai trang, cross-filter khong bi flicker/reset, va ROI chart co dashed guide lines tai cac moc 10^x."

## Expected Output
- Cross-filter giu duoc state sau moi click chart.
- Click vung trong chart van xoa filter theo dung y nghia.
- Nut reset luon hien chu trang tren nen do.
- ROI chart co luoi net dut ro rang theo decade log scale.
