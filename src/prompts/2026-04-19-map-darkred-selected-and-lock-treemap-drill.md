# Objective
Tinh chinh 2 tuong tac:
1) Country map: khi co selected countries thi gradient cua nhom duoc chon ket thuc o do dam hon (khong dung Netflix red trung gian).
2) Language treemap: ngan hanh vi zoom/drill vao 1 tile khi click, de click chi dong vai tro chon filter.

# Context
User muon selected countries tren map scale den mau do dam tuong tu phong cach gradient mode. Dong thoi treemap ngon ngu dang bi phong to 1 ngon ngu va khong co duong quay lai.

# Final Prompt
- Doi endpoint cua selected-country gradient tren map sang do dam (#80060B).
- Cau hinh treemap update_traces(maxdepth=1, pathbar invisible) de tranh drill/zoom.

# Expected Output
- Khi co selected countries, quoc gia selected hien gradient den do dam.
- Click vao treemap ngon ngu khong con bi zoom full 1 tile; tiep tuc click ngon ngu khac de toggle filter.