# Objective
Khac phuc hien tuong click chon 1 quoc gia tren map nhung lai co nhieu quoc gia khac cung bi to mau do phim dong san xuat.

# Context
Sau khi chon quoc gia, dashboard loc movies theo show_id co chua quoc gia do. Tuy nhien map dang aggregate lai country bridge tu tap show_id da loc, nen cac nuoc dong san xuat cung hien len, gay nham la filter sai.

# Final Prompt
- Trong ve_tab_toan_canh, neu da co quoc_gia_chon trong session_state thi map chi aggregate va render tren danh sach quoc gia da chon.
- Khong thay doi logic loc movies toan cuc.

# Expected Output
- Chon Albania/Brazil tren map se chi highlight dung cac quoc gia da chon.
- Khong con hien tuong quoc gia khac bi to mau theo co-production spillover.