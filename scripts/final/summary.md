# Kịch bản tổng hợp 30 phút - Bản hoàn chỉnh liền mạch

## Kịch bản chi tiết theo thời gian

### 00:00-05:00 | Người Slide (mở đầu + slide 1-18)

"Kính chào thầy và các bạn, nhóm 7 xin trình bày đề tài tối ưu chiến lược đầu tư nội dung phim Netflix toàn cầu. Trọng tâm của nhóm là cân bằng giữa độ phủ thị trường, chất lượng nội dung, hiệu quả tài chính và năng lực sáng tạo."

"Bài trình bày gồm 5 phần: giới thiệu thành viên, giới thiệu đề tài và dữ liệu, phần trừu tượng hóa What-Why, nhận xét dashboard, và kết luận."

"Nhóm gồm 5 thành viên: Nguyễn Hưng Thịnh, Lê Thành Công, Lê Thượng Đế, Vũ Nguyễn Trung Hiếu và Phan Ngọc Quân. Sau đây nhóm bắt đầu vào nội dung chính."

"Đầu tiên là phần giới thiệu đề tài và dữ liệu."

"Nhóm chọn đề tài này vì ngành streaming đang chuyển từ mở rộng số lượng sang tối ưu hiệu quả danh mục. Dữ liệu Netflix cho phép nhìn toàn chuỗi giá trị: thị trường, chất lượng, tài chính và sáng tạo. Từ đó, nhóm xây dựng dashboard tương tác để hỗ trợ kiểm thử kịch bản và ra quyết định dựa trên dữ liệu."

"Nguồn dữ liệu là Netflix movies detailed up to 2025. Dữ liệu gốc có 16.000 dòng và 18 cột, sau tiền xử lý còn 15.239 dòng và 18 cột. Mốc thời gian phân tích từ 2010 đến 2025, tập trung vào Movie, với 68 ngôn ngữ."

"Các trường dữ liệu được tổ chức để theo dõi cả thông tin mô tả nội dung lẫn chỉ số định lượng, tạo nền cho phân tích theo nhiều chiều ở các phần sau."

"Ở dữ liệu gốc, cột duration bị thiếu 100 phần trăm nên được loại bỏ. Nhóm cũng loại các dòng thiếu trường trọng yếu như quốc gia, diễn viên, đạo diễn, mô tả, thể loại, đồng thời chuẩn hóa các cột số. Kết quả là loại 761 dòng, tương đương khoảng 4,76 phần trăm, giữ lại 95,24 phần trăm dữ liệu, đủ ổn định để phân tích."

"Tiếp theo là phần trừu tượng hóa What-Why để đặt đúng câu hỏi trước khi phân tích."

"Mục tiêu của trừu tượng hóa là chuyển từ xem biểu đồ sang đặt đúng câu hỏi. "What" giúp xác định dữ liệu đang có gì. "Why" giúp xác định cần ra quyết định gì. Cách này giúp nhóm tránh phân tích cảm tính và bám chặt mục tiêu kinh doanh."

"Về What, dữ liệu gồm bảng chính movies và các bảng quan hệ, đồng thời có chiều không gian và thời gian. Thuộc tính được chia thành categorical, ordered và quantitative, bao phủ đầy đủ cho phân tích mô tả, so sánh và định lượng."

"Về Why, nhóm tập trung 5 tác vụ: Khám phá, So sánh, Xếp hạng, Tìm mối tương quan và Tổng hợp. Nghĩa là từ phát hiện trọng điểm thị trường đến xếp hạng ROI, phân tích tương quan và chốt lại thành ưu tiên đầu tư cụ thể."

"Sau đây là phần nhận xét dashboard theo 4 trục chính."

"Tab Toàn cảnh cho thấy phân bổ danh mục không đồng đều theo thị trường và ngôn ngữ. Điểm quan trọng là nhận diện nhanh cụm thị trường trọng điểm. Tuy nhiên, nơi có nhiều phim chưa chắc là nơi có chất lượng hoặc hiệu quả tài chính tốt nhất, nên cần kiểm chứng chéo với các tab sau."

"Tab Chất lượng cho thấy phần lớn nội dung nằm ở mức điểm trung bình-khá. Một số thể loại vừa có quy mô vừa có độ ổn định điểm tốt, phù hợp để mở rộng. Đồng thời, tăng ngân sách không làm điểm tăng tuyến tính, nên cần ưu tiên chất lượng bền vững hơn là doanh thu ngắn hạn."

"Tab Tài chính cho thấy có dự án ROI cao không thuộc nhóm ngân sách lớn nhất. Điều này gợi ý hiệu quả phụ thuộc cấu trúc danh mục hơn là chỉ mức chi. Vì vậy, định hướng là tái phân bổ ngân sách theo hiệu quả thực tế và độ ổn định ROI."

"Tab Sáng tạo cho thấy hiệu suất khác biệt theo đạo diễn, diễn viên và mức đa dạng thể loại. Điểm đáng chú ý là đa dạng thể loại có xu hướng đi cùng mức thành công tốt hơn, trong khi nội dung có tên tuổi lớn chưa chắc duy trì đồng thời doanh thu và chất lượng."

"Nhóm xin tạm dừng phần slide tại đây và chuyển sang phần thuyết trình dashboard theo 10 câu hỏi chiến lược.

---

### 05:00-11:00 | Quân (câu 1-3)

**giới thiệu tương tác dashboard**

"Em xin bắt đầu với nhóm câu hỏi thị trường."

"Để tránh nhìn biểu đồ theo cảm tính, nhóm dùng khung What-Why. What trả lời dữ liệu có gì và đo được gì. Why trả lời chúng ta cần quyết định gì từ dữ liệu đó."

"Từ khung này, nhóm đặt 3 câu hỏi thị trường. Câu 1: mức độ tập trung nội dung theo quốc gia hiện như thế nào. Câu 2: cơ cấu ngôn ngữ của thư viện hiện ra sao. Câu 3: khác biệt thể loại giữa các thị trường lớn đến mức nào."

.......

"Phần của em xin hết. Mời Hiếu tiếp tục với nhóm câu hỏi về chất lượng nội dung."

---

### 11:00-17:00 | Hiếu (câu 4-6)

"Em xin tiếp tục với trục chất lượng nội dung."

"Phần chất lượng nội dung này tập trung vào 3 câu hỏi:
....

"Hàm ý quản trị là: thay vì chỉ tăng ngân sách đại trà, cần ưu tiên các cụm thể loại vừa giữ được mức điểm ổn định vừa có đủ quy mô để mở rộng bền vững."

"Phần chất lượng xin kết thúc tại đây. Mời Thịnh tiếp tục với nhóm câu hỏi tài chính gồm câu 7 và câu 8."

---

### 17:00-21:00 | Thịnh (câu 7-8)

"Em xin trình bày phần tài chính."

"Phần tài chính tập trung vào 2 câu: Câu 7 về quan hệ giữa ngân sách, doanh thu và ROI; Câu 8 về dịch chuyển dòng vốn theo thời gian giữa các nhóm thể loại."

.....

"Phần tài chính của em xin hết. Mời Công hoàn tất 2 câu cuối trong trục sáng tạo là câu 9 và câu 10."

---

### 21:00-25:00 | Công (câu 9-10)

"Em xin tiếp tục với tab sáng tạo."

"Phần này có 2 câu: Câu 9 về tác động của tổ hợp đạo diễn - diễn viên, và Câu 10 về tác động của đa dạng thể loại đến mức thành công."

...

---

### 25:00-27:00 | Công (quay lại slide kết luận và chốt bài)

"Nhóm đã hoàn tất phần dashboard với 10 câu hỏi chiến lược. Xin mời thầy và các bạn nhìn lại slide Kết luận để nhóm chốt lại toàn bộ nội dung."

"Từ 10 câu hỏi theo 4 trục Thị trường, Chất lượng, Tài chính, Sáng tạo, nhóm rút ra rằng tăng trưởng bền vững không đến từ mở rộng đại trà hay tăng ngân sách đồng loạt, mà đến từ đầu tư đúng thị trường, đúng thể loại, đúng tổ hợp sáng tạo. Dashboard vì vậy trở thành công cụ ra quyết định nội dung có căn cứ và kiểm soát rủi ro."

"Tiếp theo, nhóm xin chuyển sang phần hỏi đáp để nhận câu hỏi từ thầy và các bạn."

---

### 29:30-30:00 | Kết buổi (Công)

"Nhóm 7 cảm ơn thầy và các bạn đã theo dõi và đặt câu hỏi. Nếu không còn câu hỏi thêm, nhóm xin phép kết thúc phần trình bày tại đây."
