# Request Summary
User xac dinh nguyen nhan: phim co the co nhieu quoc gia, nen sau khi loc theo 1 quoc gia thi map van to cac quoc gia dong san xuat khac. Yeu cau: click/chon quoc gia nao thi map chi hien quoc gia do.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-map-country-spillover-highlight-fix.md
- docs/ai/2026-04-19-map-country-spillover-highlight-fix.md

# Key Decisions
- Them buoc filter map-level trong ve_tab_toan_canh:
  - lay countries_chon tu st.session_state["quoc_gia_chon"]
  - neu co chon, countries_loc cho map se chi giu country_name nam trong countries_chon
- Giu nguyen logic loc movies toan cuc de khong vo tinh doi nghia cac chart khac.

# Next Steps
- Test click 1 quoc gia va click nhieu quoc gia tren map:
  - map chi to cac quoc gia dang active trong multiselect.
  - click lai de deselect van hoat dong toggle dung.