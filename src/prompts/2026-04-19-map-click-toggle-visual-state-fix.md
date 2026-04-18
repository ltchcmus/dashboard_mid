# Objective
Fix 2 van de map interaction:
1) Da chon US + China nhung US bi nhat mau sai trang thai.
2) Click lai US lan 2 thi mau reset nhung US van selected (toggle OFF khong an).

# Context
Sau khi them co che dedupe signature de tranh flicker, logic skip dang bo qua vo thoi han cho cung signature, dan den click lai cung item khong toggle OFF duoc. Dong thoi widget map giu selection visual state cu gay nhat mau sai voi session_state.

# Final Prompt
- Dedupe event chi skip 1 lan stale rerun ngay sau click, khong skip vo han.
- Sau khi skip 1 lan, click lai cung signature phai duoc phep toggle.
- Remount map widget theo selection key suffix de dong bo visual state voi session_state va tranh mau nhat sai.

# Expected Output
- Chon US roi China: ca hai quoc gia selected on dinh, khong nhat sai do stale visual.
- Click lai US lan 2: US duoc bo chon dung nghia (toggle OFF), khong bi treo selected.
- Khong co flicker select/unselect lien tuc.