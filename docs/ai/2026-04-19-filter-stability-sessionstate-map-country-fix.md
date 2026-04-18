# Request Summary
Sua 2 van de:
1) Crash Streamlit do set session_state cua key da gan widget trong cung run.
2) Click map tra ve gia tri quoc gia sai (vi fallback location/code va customdata nested).

# Files Changed
- src/main.py
- src/prompts/2026-04-19-filter-stability-sessionstate-map-country-fix.md
- docs/ai/2026-04-19-filter-stability-sessionstate-map-country-fix.md

# Key Decisions
- Them state trung gian pending_filter_updates.
- cap_nhat_loc_toggle khong set truc tiep quoc_gia_chon/ngon_ngu_chon/the_loai_chon nua, ma ghi vao pending.
- bo_loc_toan_cuc goi ap_dung_pending_filter_updates() truoc khi instantiate multiselect widgets.
- trich_gia_tri_tu_su_kien_plotly duoc bo sung flatten nested list/tuple/ndarray de lay dung scalar.
- Map selection chi doc customdata (country name) de tranh nham voi location code.

# Next Steps
- Test click Albania, Brazil, United States tren map va kiem tra multiselect Quoc gia cap nhat dung ten.
- Test click lai cung 1 country de toggle off.
- Test ket hop map + treemap + bar trong cung mot session de xac nhan pending updates on dinh.