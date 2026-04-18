# Objective
Cap nhat Q5 (Tab 2): doi ten bieu do cho dung ngu nghia va chia nhom ngan sach theo tu phan vi, giu nguyen nhom diem so.

# Context
User phan hoi Q5 dang nhac ROI khong phu hop voi du lieu hien thi. Dong thoi yeu cau nhom ngan sach doi sang tu phan vi.

# Final Prompt
- Doi title Q5 bo nhac ROI.
- Nhom ngan sach dung `pd.qcut(..., q=4)`.
- Nhom diem so giu nguyen bins `<6`, `6-7.5`, `>7.5`.
- Loai cac truong ROI khoi agg/hover/labels cua Q5.

# Expected Output
- Bieu do Q5 co ten trung tinh: phan bo so luong phim theo diem so va ngan sach.
- Truc x la "Nhóm ngân sách (tứ phân vị)".
- Khong con thong tin ROI trong Q5.