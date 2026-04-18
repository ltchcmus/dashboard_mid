# Objective
Fix loi Streamlit session_state khi dong bo click tu chart vao multiselect sidebar, va sua sai lech gia tri quoc gia khi click map.

# Context
User gap StreamlitAPIException: khong duoc set st.session_state.<widget_key> sau khi widget da instantiate. Dong thoi click map chon Albania/Brazil lai co luc nhay sai sang United States.

# Final Prompt
1) Khong set truc tiep session_state cua widget keys trong pha render chart.
2) Dung co che pending updates va apply truoc khi render widgets.
3) Trich gia tri map uu tien customdata country name, khong fallback location code.
4) Chuan hoa customdata nested list/tuple/np.ndarray de lay dung scalar value.

# Expected Output
- Het loi StreamlitAPIException khi click chart.
- Click map se dua dung quoc gia vao multiselect Quoc gia.
- Logic toggle van hoat dong va rerun khong crash.