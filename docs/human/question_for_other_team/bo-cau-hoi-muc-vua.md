# Bộ 6 câu hỏi chất lượng để team khác hỏi Nhóm 7

## 1. Sau khi loại 761 dòng thiếu dữ liệu trọng yếu và bỏ cột duration thiếu 100%, nhóm làm gì để bảo đảm insight không bị lệch?

**Trả lời mẫu:**

- Nhóm giữ lại 15.239 trên 16.000 dòng, tức khoảng 95,24% dữ liệu, nên quy mô mẫu vẫn đủ lớn.
- Nhóm so sánh trước và sau lọc theo các chiều chính như quốc gia, ngôn ngữ, thể loại để kiểm tra biến dạng phân bố.
- Chỉ khi xu hướng lớn không đổi thì mới dùng cho kết luận; các điểm nhạy được xem là tín hiệu tham khảo, không khẳng định mạnh.

## 2. Trên bản đồ quốc gia, vì sao nhóm chọn thang log thay vì tuyến tính, và làm sao tránh hiểu sai khi đọc log?

**Trả lời mẫu:**

- Dữ liệu phân bố lệch mạnh: một vài thị trường rất lớn, còn nhiều thị trường nhỏ nằm ở đuôi dài.
- Thang log giúp nhìn thấy đồng thời cả nhóm đầu và nhóm trung bình-thấp, tránh việc bản đồ bị "nuốt màu" bởi vài nước lớn.
- Để tránh hiểu sai, nhóm luôn đọc kèm thứ hạng, tooltip giá trị gốc và kết luận theo cụm thay vì chỉ nhìn màu tuyệt đối.

## 3. Câu 6 cho thấy tăng ngân sách không làm điểm tăng đồng đều. Vậy ngân sách trong dashboard được dùng như công cụ gì?

**Trả lời mẫu:**

- Ngân sách được xem là công cụ quản trị rủi ro danh mục, không phải "nút tăng điểm" tuyến tính.
- Nhóm ưu tiên cấp vốn cho cụm thể loại có điểm ổn định và ROI bền, thay vì dồn đều hoặc chạy theo doanh thu ngắn hạn.
- Quy tắc vận hành là phân bổ theo hiệu quả thực tế và độ ổn định, sau đó theo dõi lại qua lọc chéo giữa tab Chất lượng và Tài chính.

## 4. Câu 10 cho thấy đa dạng thể loại cao đi cùng kết quả tốt hơn. Nhóm làm gì để không nhầm tương quan thành nhân quả?

**Trả lời mẫu:**

- Nhóm chỉ kết luận ở mức tương quan trong dữ liệu quan sát, không khẳng định đa dạng thể loại là nguyên nhân trực tiếp.
- Khi ra quyết định, nhóm coi đây là giả thuyết ưu tiên kiểm thử, không phải chân lý cố định.
- Bước tiếp theo là kiểm chứng bằng thiết kế thử nghiệm hoặc so sánh theo phân khúc tương đồng trước khi mở rộng vốn lớn.

## 5. Nếu phải chọn 1 chỉ báo "go/no-go" để duyệt một hướng đầu tư nội dung mới, nhóm chọn gì và vì sao?

**Trả lời mẫu:**

- Nhóm không dùng một chỉ số đơn lẻ, mà dùng một ngưỡng tổng hợp tối thiểu gồm: ROI dương, điểm trung bình đạt chuẩn và độ ổn định chấp nhận được.
- Lý do là mỗi chỉ số riêng lẻ đều có thể gây lệch: ROI cao nhưng điểm bấp bênh, hoặc điểm cao nhưng hiệu quả vốn thấp.
- Cách này phù hợp định hướng của nhóm: tăng trưởng bền vững thay vì tối ưu một biến ngắn hạn.

## 6. Trong 4 tab hiện tại, tab nào có giá trị cảnh báo sớm rủi ro đầu tư nhất, và nhóm kết hợp với tab nào để chốt quyết định?

**Trả lời mẫu:**

- Tab Tài chính thường cho tín hiệu cảnh báo sớm nhất vì phản ánh trực tiếp hiệu quả vốn và rủi ro lợi nhuận.
- Tuy nhiên, nhóm không chốt ở một tab; bắt buộc kiểm chéo với tab Chất lượng để tránh chọn dự án có hiệu quả ngắn hạn nhưng thiếu bền vững.
- Sau cùng mới đối chiếu thêm tab Sáng tạo để bảo đảm tổ hợp nhân sự và độ đa dạng thể loại phù hợp chiến lược dài hạn.
