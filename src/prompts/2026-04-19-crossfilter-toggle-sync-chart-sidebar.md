# Objective
Loai bo block bo loc tuong tac cu trong sidebar va thay bang co che dong bo truc tiep chart Tab 1 <-> widget sidebar theo kieu toggle add/remove.

# Context
User muon bo giao dien trang thai bo loc tuong tac (caption + button reset), chuyen ca 3 bo loc sang multiselect, va khi click chart thi item duoc them/bo khoi danh sach chon trong sidebar.

# Final Prompt
- Xoa ham hien_thi_trang_thai_loc_tuong_tac() va moi loi goi.
- Chuyen Quoc gia + Ngon ngu tu selectbox sang multiselect.
- Dung session_state keys: quoc_gia_chon, ngon_ngu_chon, the_loai_chon.
- Sua dong_bo_loc_tuong_tac_tu_tab1 theo toggle add/remove va st.rerun() chi khi co thay doi.
- Giu options day du, [] thi xem nhu khong loc.

# Expected Output
- Sidebar khong con block “Bo loc tuong tac tu bieu do”.
- 3 widget loc deu la multiselect.
- Click chart tab 1 se toggle item trong sidebar.
- Khong co loi session state, khong co crash, va bo loc hoat dong dung voi cac item active.