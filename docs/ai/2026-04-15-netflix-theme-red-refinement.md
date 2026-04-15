# AI Handover - Netflix Theme Red Refinement

## Request Summary
Cap nhat theme UI de phu hop huong dan thiet ke: mau chu dao sang + do Netflix, heading va filter nhan manh do, thong tin chart tren nen trang de doc.

## Files Changed
- src/main.py
- src/prompts/2026-04-15-netflix-theme-red-refinement.md
- docs/ai/2026-04-15-netflix-theme-red-refinement.md

## Key Decisions
- Bo sung helper theme Plotly de dong nhat: title do, axis/legend/tick mau toi, nen chart trang.
- Tinh chinh CSS cho KPI: label va value mau do de nhan con so chinh.
- Sidebar widgets (selectbox/multiselect/slider chips) duoc accent do va dam bao tuong phan chu.
- Giu nen tong the sang, khong dung tone den.

## Next Steps
1. Chay streamlit run src/main.py de kiem tra do tuong thich CSS giua cac phien ban Streamlit.
2. Neu can, giam do dam/chieu day border filter de toi uu tham my khi present.
