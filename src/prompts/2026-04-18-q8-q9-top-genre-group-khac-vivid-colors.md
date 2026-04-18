# Objective
Dieu chinh Tab Tai chinh de tang kha nang tao insight:
- Q9: chuyen tu nhom ngon ngu sang nhom the loai.
- Group top the loai + "Khác" cho Q9.
- Ap dung cung logic group top the loai + "Khác" cho Q8.
- Doi bang mau sang bo mau noi bat hon de tranh mau xam/mo nhat.

# Context
- File chinh sua: src/main.py
- Pham vi: ham ve_tab_tai_chinh (Q8, Q9)
- Muc tieu UX: de phan biet nhom, giam qua tai legend, giu thong diep top vs long-tail.

# Final Prompt
"ở Q9, tôi muốn thay vì theo ngôn ngữ, thì theo genre để có insight tốt hơn. không bắt buộc chỉ dùng các màu như hiện tại, vì có nhiều màu xám, mờ nhạt, nhìn không thấy. có thể bổ sung thêm 1 số màu khác nổi bật cũng được. Và có thể chỉ cần lọc ra top các thể loại thôi, các nhóm còn lại group chung vào nhóm 'Khác'. áp dụng group tương tự cho Q8."

# Expected Output
- Q9 bubble chart:
  - Truc/nhom theo the loai (khong theo ngon ngu).
  - Top 8 the loai + nhom "Khác".
  - Legend/mau de nhin, han che mau xam mo.
- Q8 line chart:
  - Group top the loai + "Khác" cung logic.
  - Mau duong noi bat va de phan biet.
- src/main.py compile OK.
