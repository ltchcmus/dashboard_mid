# Kịch bản thuyết trình theo từng slide (mục tiêu 4-5 phút)

---

## Slide 1 (00:00-00:12) - Trang bìa

"Nhóm 7 xin trình bày đề tài tối ưu chiến lược đầu tư nội dung phim Netflix toàn cầu. Trọng tâm của nhóm là cân bằng giữa độ phủ thị trường, chất lượng nội dung, hiệu quả tài chính và năng lực sáng tạo."

## Slide 2 (00:12-00:22) - Nội dung chính

"Bài trình bày gồm 5 phần: giới thiệu thành viên, giới thiệu đề tài và dữ liệu, phần trừu tượng hóa What-Why, nhận xét dashboard, và kết luận kèm lời cảm ơn."

## Slide 3 (00:22-00:34) - Thành viên nhóm

"Nhóm gồm 5 thành viên: Nguyễn Hưng Thịnh, Lê Thành Công, Lê Thượng Đế, Vũ Nguyễn Trung Hiếu và Phan Ngọc Quân. Sau đây nhóm bắt đầu vào nội dung chính."

## Slide 4 (00:34-00:38) - Chuyển phần

"Đầu tiên là phần giới thiệu đề tài và dữ liệu."

## Slide 5 (00:38-00:58) - Lý do chọn đề tài

"Nhóm chọn đề tài này vì ngành streaming đang chuyển từ mở rộng số lượng sang tối ưu hiệu quả danh mục. Dữ liệu Netflix cho phép nhìn toàn chuỗi giá trị: thị trường, chất lượng, tài chính và sáng tạo. Từ đó, nhóm xây dựng interactive dashboard để hỗ trợ kiểm thử kịch bản và ra quyết định dựa trên dữ liệu."

## Slide 6 (00:58-01:18) - Tổng quan dữ liệu

"Nguồn dữ liệu là Netflix movies detailed up to 2025. Dữ liệu gốc có 16.000 dòng và 18 cột, sau tiền xử lý còn 15.239 dòng và 17 cột. Mốc thời gian phân tích từ 2010 đến 2025, tập trung vào Movie, với 68 ngôn ngữ, nổi bật là Tiếng Anh, Tiếng Pháp, Tiếng Nhật, Tiếng Hàn và Tiếng Tây Ban Nha."

## Slide 7 (01:18-01:28) - Sơ lược trường dữ liệu

"Các trường dữ liệu được tổ chức để theo dõi cả thông tin mô tả nội dung lẫn chỉ số định lượng, tạo nền cho phân tích theo nhiều chiều ở các phần sau."

## Slide 8 (01:28-01:52) - Kiểm định và tiền xử lý

"Ở dữ liệu gốc, cột duration bị thiếu 100% nên được loại bỏ. Nhóm cũng loại các dòng thiếu trường trọng yếu như quốc gia, diễn viên, đạo diễn, mô tả, thể loại, đồng thời chuẩn hóa các cột số. Kết quả là loại 761 dòng, tương đương khoảng 4,76%, giữ lại 95,24% dữ liệu, đủ ổn định để phân tích."

## Slide 9 (01:52-01:56) - Chuyển phần

"Tiếp theo là phần trừu tượng hóa What-Why để đặt đúng câu hỏi trước khi phân tích."

## Slide 10 (01:56-02:12) - Vì sao dùng Abstraction

"Mục tiêu của Abstraction là chuyển từ xem biểu đồ sang đặt đúng câu hỏi. What giúp xác định dữ liệu đang có gì; Why giúp xác định cần ra quyết định gì. Cách này giúp nhóm tránh phân tích cảm tính và bám chặt mục tiêu kinh doanh."

## Slide 11 (02:12-02:32) - What

"Về What, dữ liệu gồm bảng chính movies và các bảng quan hệ, đồng thời có chiều không gian và thời gian. Thuộc tính được chia thành categorical, ordered và quantitative, bao phủ đầy đủ cho phân tích mô tả, so sánh và định lượng."

## Slide 12 (02:32-02:48) - Why

"Về Why, nhóm tập trung 5 tác vụ: Khám phá, So sánh, Xếp hạng, Tìm mối tương quan và Tổng hợp. Nghĩa là từ phát hiện trọng điểm thị trường đến xếp hạng ROI, phân tích tương quan và chốt lại thành ưu tiên đầu tư cụ thể."

## Slide 13 (02:48-02:52) - Chuyển phần

"Sau đây là phần nhận xét dashboard theo 4 trục chính."

## Slide 14 (02:52-03:10) - Dashboard tab Toàn cảnh

"Tab Toàn cảnh cho thấy phân bổ danh mục không đồng đều theo thị trường và ngôn ngữ. Điểm quan trọng là nhận diện nhanh cụm thị trường trọng điểm. Tuy nhiên, nơi có nhiều phim chưa chắc là nơi có chất lượng hoặc hiệu quả tài chính tốt nhất, nên cần kiểm chứng chéo với các tab sau."

## Slide 15 (03:10-03:28) - Dashboard tab Chất lượng

"Tab Chất lượng cho thấy phần lớn nội dung nằm ở mức điểm trung bình-khá. Một số thể loại vừa có quy mô vừa có độ ổn định điểm tốt, phù hợp để mở rộng. Đồng thời, tăng ngân sách không làm điểm tăng tuyến tính, nên cần ưu tiên chất lượng bền vững hơn là doanh thu ngắn hạn."

## Slide 16 (03:28-03:46) - Dashboard tab Tài chính

"Tab Tài chính cho thấy có dự án ROI cao không thuộc nhóm ngân sách lớn nhất. Điều này gợi ý hiệu quả phụ thuộc cấu trúc danh mục hơn là chỉ mức chi. Vì vậy, định hướng là tái phân bổ ngân sách theo hiệu quả thực tế và độ ổn định ROI."

## Slide 17 (03:46-04:04) - Dashboard tab Sáng tạo

"Tab Sáng tạo cho thấy hiệu suất khác biệt theo đạo diễn, diễn viên và mức đa dạng thể loại. Điểm đáng chú ý là đa dạng thể loại có xu hướng đi cùng mức thành công tốt hơn, trong khi nội dung có tên tuổi lớn chưa chắc duy trì đồng thời doanh thu và chất lượng."

## Slide 18 (04:04-04:08) - Chuyển phần

"Cuối cùng là kết luận của nhóm."

## Slide 19 (04:08-04:40) - Kết luận

"Từ 10 câu hỏi theo 4 trục Thị trường, Chất lượng, Tài chính, Sáng tạo, nhóm rút ra rằng tăng trưởng bền vững không đến từ mở rộng đại trà hay tăng ngân sách đồng loạt, mà đến từ đầu tư đúng thị trường, đúng thể loại, đúng tổ hợp sáng tạo. Dashboard vì vậy trở thành công cụ ra quyết định nội dung có căn cứ và kiểm soát rủi ro."

## Slide 20 (04:40-04:50) - Cảm ơn

"Nhóm 7 xin cảm ơn thầy và các bạn đã theo dõi phần trình bày. Nhóm sẵn sàng nhận câu hỏi và góp ý."

---
