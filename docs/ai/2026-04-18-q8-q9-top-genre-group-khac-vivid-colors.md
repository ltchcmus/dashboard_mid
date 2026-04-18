# Request Summary
Nguoi dung yeu cau doi Q9 tu nhom ngon ngu sang nhom the loai de co insight tot hon, su dung mau noi bat hon va group cac nhom ngoai top vao "Khác". Dong thoi ap dung logic group top + "Khác" tuong tu cho Q8.

# Files Changed
- src/main.py
- src/prompts/2026-04-18-q8-q9-top-genre-group-khac-vivid-colors.md
- docs/ai/2026-04-18-q8-q9-top-genre-group-khac-vivid-colors.md

# Key Decisions
- Q8 (line chart ngan sach theo nam):
  - Dung top 7 the loai theo tan suat, con lai group thanh "Khác".
  - Group by (`release_year`, `nhom_the_loai`) de tinh ngan sach trung binh.
  - Dung palette vivid rieng (do/cam/vang/xanh/la/tim/hong...) thay vi dung bo mau cu co nhieu mau nhat.
  - Tieu de cap nhat de phan anh da gom nhom "Khác".
- Q9 (bubble chart):
  - Doi nguon nhom tu `language_name` sang `the_loai` (dua tren `genres_loc` + movies budget/revenue).
  - Dung top 8 the loai + "Khác".
  - Doi cot ten hien thi thanh "Nhóm thể loại".
  - Dung palette vivid va color map theo thu tu top + "Khác".
  - Cap nhat title va caption cho dung y nghia theo the loai.

# Verification
- Compile `src/main.py`: OK.
- Problems panel cho `src/main.py`: No errors found.

# Next Steps
1. Chay app de quan sat truc quan legend/palette khi thay doi bo loc quoc gia/the loai.
2. Neu can, co the dieu chinh so luong top (Q8:7, Q9:8) thanh mot bien cau hinh chung.
3. Neu "Khác" qua lon, can nhac tach thanh 2 nhom long-tail theo median doanh thu de giu tinh dien giai.
