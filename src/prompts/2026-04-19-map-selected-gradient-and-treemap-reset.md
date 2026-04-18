# Objective
Nang cap 2 tuong tac:
1) Country map: khi da chon quoc gia thi cac quoc gia selected duoc to theo gradient, khong chi 1 mau phang.
2) Language treemap: tranh bi zoom kẹt 1 o sau click, cho phep tiep tuc chon ngon ngu khac.

# Context
User muon map selected quoc gia co gradient de de nhin muc do; va treemap ngon ngu khong bi "phong to chiem tron" lam mat kha nang chon tiep.

# Final Prompt
- Trong mode co country selection:
  - Dat gia_tri_mau = -1 cho unselected (xam nhat),
  - Dat gia_tri_mau = log10(count) cho selected,
  - Dung color_continuous_scale co gradient do va an colorbar.
- Treemap:
  - Dung key dong theo danh sach ngon_ngu_chon de remount chart sau moi lan toggle, reset trang thai zoom.

# Expected Output
- Chon nhieu quoc gia: cac quoc gia selected hien gradient do, con lai nhat mau.
- Click English khong con bi "ket zoom"; sau rerun van chon tiep ngon ngu khac duoc.