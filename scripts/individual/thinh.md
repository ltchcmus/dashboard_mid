# Kịch bản cá nhân - Nguyễn Hưng Thịnh

## Vai trò và thời lượng

- Vai trò: dữ liệu và tiền xử lý.
- Trình bày chính: 5 phút (05:00-10:00).
- Hỏi đáp: 1 phút (26:00-27:00).

## Lời thoại phần chính (5 phút)

### 05:00-06:00

"Em xin trình bày nền dữ liệu nhóm sử dụng. Nguồn đầu vào là bộ phim Netflix đến năm 2025, quy mô ban đầu 16 nghìn dòng và 18 cột. Sau tiền xử lý, dữ liệu còn 15,239 dòng và 18 cột."

### 06:00-07:00

"Nhóm loại 761 dòng, tương đương 4.76 phần trăm, giữ lại hơn 95 phần trăm dữ liệu để phân tích. Phạm vi thời gian đang chạy trong dashboard là từ 2010 đến 2025, với độ phủ 133 quốc gia và 68 ngôn ngữ."

### 07:00-08:20

"Các bước làm sạch chính gồm: bỏ cột thời lượng do trống toàn bộ; loại các bản ghi thiếu trường trọng yếu như quốc gia, diễn viên, đạo diễn, mô tả, thể loại; và chuẩn hóa các cột số để biểu đồ có thể so sánh ổn định theo cùng đơn vị."

### 08:20-09:20

"Em xin nhấn mạnh một điểm dễ bị hỏi lại: có phiên bản slide cũ ghi dữ liệu sau xử lý là 17 cột. Tuy nhiên, bộ dữ liệu chạy thật của ứng dụng hiện tại là 18 cột. Lý do là cột thời lượng bị loại, nhưng thông tin ngôn ngữ được chuẩn hóa tách thành mã ngôn ngữ và tên ngôn ngữ."

### 09:20-10:00

"Vì vậy, khi nhóm phát biểu số liệu, nhóm bám dữ liệu processed đang dùng trong code để bảo đảm khớp giữa dữ liệu, dashboard và phần trình bày."

## Câu chuyển giao

"Mời Đế tiếp tục với khung Cái gì - Tại sao và nhóm câu hỏi thị trường."

## Phần hỏi đáp của Thịnh (1 phút)

### Câu hay gặp

- "Bỏ cột thời lượng có làm mất thông tin quan trọng không?"

### Trả lời ngắn

"Cột thời lượng trong dữ liệu gốc trống 100 phần trăm nên không có tín hiệu để khai thác. Việc loại bỏ giúp giảm nhiễu và không làm mất thông tin thực tế vì bản thân cột đó không có giá trị sử dụng."

## Dự phòng nếu thiếu hoặc dư thời gian

- Thiếu thời gian: rút phần giải thích số cột còn 2 câu then chốt.
- Dư thời gian: thêm 1 câu nhấn rằng nhóm không dùng dữ liệu ngoài pipeline đã công bố.
