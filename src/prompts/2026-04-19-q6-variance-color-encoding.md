# Objective
Doi logic encode mau cua bieu do Q6 (Top the loai co diem danh gia on dinh nhat) tu diem trung binh sang phuong sai cua the loai.

# Context
User yeu cau gradient color phai phan anh variance (do on dinh) thay vi mean rating.

# Final Prompt
- Them cot `phuong_sai = do_lech_chuan ** 2` trong bang thong ke the loai.
- Marker color cua bar chart Q6 dung `phuong_sai`.
- Doi tieu de colorbar thanh `Phương sai`.
- Cap nhat hover de hien thi phuong sai cung so phim.

# Expected Output
- Mau gradient cua Q6 phan anh variance.
- Legend/colorbar khong con mang y nghia diem trung binh.
- Hover hien thong tin lien quan den do on dinh (variance, std, so phim).