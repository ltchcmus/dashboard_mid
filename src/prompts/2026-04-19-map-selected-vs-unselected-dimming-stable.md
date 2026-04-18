# Objective
Dam bao khi da chon quoc gia tren map thi cac quoc gia chua chon luon bi lam mo on dinh, khong bi quay ve mau goc sau rerun.

# Context
Visual selection mac dinh cua Plotly co the reset sau rerun, dan den trang thai mau khong khop voi selected list trong sidebar.

# Final Prompt
- Doi map coloring sang co che dua tren session_state quoc_gia_chon:
  - Neu co selected countries: to mau do cho selected, xam nhat cho unselected.
  - Neu chua co selected countries: giu gradient theo so luong phim nhu cu.
- Giu custom_data de click/toggle van hoat dong.

# Expected Output
- Chon US: US do, cac nuoc khac nhat on dinh.
- Chon them China: US + China do, cac nuoc khac van nhat.
- Khong con hien tuong cac nuoc khac quay ve mau goc trong khi van dang selected.