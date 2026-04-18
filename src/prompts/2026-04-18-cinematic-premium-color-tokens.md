# Objective
Cập nhật hệ thống biến màu ở đầu `src/main.py` theo phong cách Cinematic Premium, giảm lạm dụng tông teal và tăng nhận diện thương hiệu Netflix.

# Context
- Dashboard đang dùng semantic tokens nhưng tông teal còn xuất hiện mạnh, làm loãng brand identity.
- Yêu cầu chỉ chỉnh phần biến màu/palette ở đầu file, không thay đổi logic xử lý dữ liệu hay cấu trúc biểu đồ.

# Final Prompt
Cập nhật color variables và palettes đầu file theo hướng: NETFLIX_RED giữ nguyên, NETFLIX_TEAL đổi sang Gold/Amber, SEQ_COUNT dùng Slate Grey, DIVERGE_QUALITY đỏ-trung tính-gold, CAT_GENRE dùng muted colors, QUALITY_BUCKET_COLORS chuyển dải từ đỏ sang gold/green.

# Expected Output
- Chỉ phần constants/palettes đầu file được chỉnh sửa.
- Giữ `TEXT_DARK` và `CHART_BG` để đảm bảo giao diện sạch.
- Mã compile thành công sau thay đổi.