# AI Handover - Header Bar Title Layout

## Request Summary
Tang chieu cao thanh ngang tren cung va dat tieu de chinh vao thanh nay (chu trang), giu nguyen kich thuoc chu va bo duplicate title trong noi dung trang.

## Files Changed
- src/main.py
- src/prompts/2026-04-15-header-bar-title-layout.md
- docs/ai/2026-04-15-header-bar-title-layout.md

## Key Decisions
- Dung CSS tren data-testid='stHeader' de tăng chieu cao (92px) va canh giua theo truc dung.
- Dung pseudo-element ::before de render title ngay trong header voi font-size 2.75rem (tuong duong tieu de cu).
- Bo st.title trong than trang de tranh lap lai noi dung.
- Dieu chinh padding top cua main container de bo cuc khong bi sat header.

## Next Steps
1. Chay streamlit va xem tren man hinh thuc te de canh trai/phai cua title neu can.
2. Neu muon, them responsive rule cho man hinh nho de title khong bi tran ngang.
