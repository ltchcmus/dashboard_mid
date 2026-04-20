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

### 05:00-11:00 | A (câu 1-3)

"Em xin bắt đầu với nhóm câu hỏi thị trường."

"Để tránh nhìn biểu đồ theo cảm tính, nhóm dùng khung What-Why. What trả lời dữ liệu có gì và đo được gì. Why trả lời chúng ta cần quyết định gì từ dữ liệu đó."

"Từ khung này, nhóm đặt 3 câu hỏi thị trường. Câu 1: mức độ tập trung nội dung theo quốc gia hiện như thế nào. Câu 2: cơ cấu ngôn ngữ của thư viện hiện ra sao. Câu 3: khác biệt thể loại giữa các thị trường lớn đến mức nào."

"Trước tiên, với câu 1, nhóm dùng bản đồ nhiệt quốc gia theo thang log. Kết luận là thị trường vẫn tập trung mạnh vào một số trung tâm lớn, nhưng đã xuất hiện nhiều cụm tăng trưởng khu vực đủ rõ để cân nhắc ưu tiên phát hành bản địa."

"Tiếp theo, với câu 2, treemap ngôn ngữ cho thấy một ngôn ngữ chủ lực vẫn chiếm tỷ trọng cao, nhưng nhóm ngôn ngữ kế tiếp đang mở rộng đáng kể. Điều này cho thấy chiến lược nội dung không thể chỉ bám một thị trường ngôn ngữ duy nhất."

"Cuối cùng, với câu 3, khi dùng lọc quốc gia rồi nhìn lại thanh thể loại, thứ hạng thể loại thay đổi rõ rệt. Nghĩa là cùng một danh mục toàn cầu nhưng khẩu vị từng thị trường là khác nhau, nên quyết định phân phối phải có lớp tùy biến theo khu vực."

"Phần của em xin hết. Mời B tiếp tục với nhóm câu hỏi về chất lượng nội dung."

---

### 11:00-17:00 | B (câu 4-6)

"Em xin tiếp tục với trục chất lượng nội dung."

"Trong phần này, nhóm lần lượt trả lời 3 câu: Câu 4 về phân bổ chất lượng tổng thể, Câu 5 về thể loại chất lượng cao và ổn định, Câu 6 về tác động của ngân sách đến điểm chất lượng."

"Trước tiên, với câu 4, donut chất lượng cho thấy thư viện hiện nghiêng về vùng trung bình đến khá. Nhóm Khá khoảng 39.75 phần trăm, còn nhóm Xuất sắc khoảng 2.08 phần trăm. Điều này phản ánh chiến lược phủ rộng danh mục nhiều hơn là dồn toàn bộ nguồn lực vào một số rất ít siêu phẩm."

"Tiếp theo, với câu 5, nhóm kết hợp biểu đồ top thể loại chất lượng cao và biểu đồ sai số ổn định điểm. Từ đó, mình không chỉ nhìn số lượng phim tốt, mà còn nhìn độ ổn định chất lượng theo thể loại để xác định vùng đầu tư an toàn hơn."

"Cuối cùng, với câu 6, heatmap ngân sách - điểm cho thấy tăng ngân sách không tạo cải thiện điểm một cách đồng đều ở mọi phân khúc. Dòng tiền lớn giúp giảm rủi ro nhóm điểm thấp, nhưng không tự động tạo ra bứt phá tương ứng ở nhóm điểm rất cao."

"Hàm ý quản trị là: thay vì chỉ tăng ngân sách đại trà, cần ưu tiên các cụm thể loại vừa giữ được mức điểm ổn định vừa có đủ quy mô để mở rộng bền vững."

"Phần chất lượng xin kết thúc tại đây. Mời C tiếp tục với nhóm câu hỏi tài chính gồm câu 7 và câu 8."

---

### 17:00-21:00 | C (câu 7-8)

"Em xin trình bày phần tài chính."

"Phần tài chính tập trung vào 2 câu: Câu 7 về quan hệ giữa ngân sách, doanh thu và ROI; Câu 8 về dịch chuyển dòng vốn theo thời gian giữa các nhóm thể loại."

"Trước tiên, với câu 7, khi đặt biểu đồ bong bóng ngân sách - doanh thu cạnh biểu đồ tỷ suất lợi nhuận, kết luận chính là: quy mô vốn và doanh thu có đi cùng chiều về mặt tuyệt đối, nhưng tỷ suất lợi nhuận không tăng đều theo vốn. Có dự án ngân sách vừa vẫn cho hiệu quả vượt trội."

"Tiếp theo, với câu 8, đường xu hướng theo thời gian cho thấy dòng vốn đang dịch chuyển giữa các nhóm thể loại. Tuy nhiên, thể loại được bơm vốn mạnh chưa chắc là thể loại ổn định điểm cao nhất. Vì vậy, cần theo dõi đồng thời vốn, lợi nhuận và chất lượng thay vì tối ưu một biến đơn lẻ."

"Phần tài chính của em xin hết. Mời D hoàn tất 2 câu cuối trong trục sáng tạo là câu 9 và câu 10."

---

### 21:00-25:00 | D (câu 9-10)

"Em xin tiếp tục với trục sáng tạo."

"Phần này có 2 câu: Câu 9 về tác động của tổ hợp đạo diễn - diễn viên, và Câu 10 về tác động của đa dạng thể loại đến mức thành công."

"Trước tiên, với câu 9, trong tab Sáng tạo, em dùng cách đọc không cần nêu tên riêng: cụm điểm ở vùng phải-trên của biểu đồ đạo diễn là nhóm cân bằng tốt giữa doanh thu trung bình và điểm trung bình; đồng thời nhóm cột cao nhất ở biểu đồ diễn viên cho thấy lực kéo doanh thu tập trung vào một số nhân tố hạt nhân."

"Tiếp theo, với câu 10, biểu đồ cột - đường theo số thể loại cho thấy xu hướng tăng rõ từ nhóm 1 thể loại sang nhóm 4 cộng. Nói theo ngưỡng: độ phổ biến tăng gần gấp đôi và điểm trung bình tăng khoảng nửa điểm. Nghĩa là đa dạng thể loại cao hơn đi cùng tín hiệu thành công tốt hơn trong dữ liệu hiện tại."

"Kết lại toàn bộ 10 câu hỏi: tăng trưởng bền vững không đến từ mở rộng đại trà, mà đến từ phân bổ vốn đúng thị trường, đúng thể loại và đúng tổ hợp sáng tạo."

---

### 25:00-27:00 | Công (quay lại slide kết luận và chốt bài)

"Nhóm đã hoàn tất phần dashboard với 10 câu hỏi chiến lược. Xin mời thầy và các bạn nhìn lại slide Kết luận để nhóm chốt lại toàn bộ nội dung."

"Từ 10 câu hỏi theo 4 trục Thị trường, Chất lượng, Tài chính, Sáng tạo, nhóm rút ra rằng tăng trưởng bền vững không đến từ mở rộng đại trà hay tăng ngân sách đồng loạt, mà đến từ đầu tư đúng thị trường, đúng thể loại, đúng tổ hợp sáng tạo. Dashboard vì vậy trở thành công cụ ra quyết định nội dung có căn cứ và kiểm soát rủi ro."

"Tiếp theo, nhóm xin chuyển sang phần hỏi đáp để nhận câu hỏi từ thầy và các bạn."

---

### 29:30-30:00 | Kết buổi (Công)

"Nhóm 7 cảm ơn thầy và các bạn đã theo dõi và đặt câu hỏi. Nếu không còn câu hỏi thêm, nhóm xin phép kết thúc phần trình bày tại đây."
