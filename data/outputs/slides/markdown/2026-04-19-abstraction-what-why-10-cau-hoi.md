# Slides - Phương pháp Abstraction (What-Why) và bộ 10 câu hỏi

## Chủ đề xuyên suốt (giữ nguyên, không tự bịa)
Tối ưu chiến lược đầu tư nội dung phim Netflix toàn cầu: cân bằng độ phủ thị trường, chất lượng, hiệu quả tài chính và năng lực sáng tạo.

---

## Slide W1 - Vì sao dùng Abstraction (Trừu tượng hóa)?
- Mục đích: chuyển từ xem biểu đồ sang đặt đúng câu hỏi trước khi trả lời.
- What trả lời: Dữ liệu mình có gì, kiểu nào, thuộc tính nào đo được.
- Why trả lời: Mình cần ra quyết định gì, cần so sánh/cảnh báo/ưu tiên điều gì.
- Giá trị: tránh phân tích cảm tính, giúp dashboard phục vụ mục tiêu kinh doanh rõ ràng.

Lời thoại gợi ý (15-20s):
"Abstraction giúp nhóm thống nhất từ đầu: dữ liệu đang có gì và mình cần dùng nó để làm gì. Nhờ vậy, mỗi biểu đồ đều có vai trò rõ ràng trong quyết định đầu tư nội dung."

---

## Slide W2 - What (Data): Dữ liệu đang có gì?
- Cấu trúc dữ liệu chính:
1. Table: movies (thông tin từng phim).
2. Relational tables: movie_countries, movie_genres, movie_directors, movie_casts.
3. Spatial: dữ liệu quốc gia để vẽ bản đồ.
4. Temporal: release_year để phân tích xu hướng theo thời gian.

- Thuộc tính theo kiểu:
1. Categorical: type, genre, country_name, language_name, director, cast.
2. Ordered: nhóm điểm, tứ phân vị ngân sách (Q1-Q4).
3. Quantitative: vote_average, popularity, vote_count, budget, revenue, ROI.

Lời thoại gợi ý (15-20s):
"Phần What cho thấy dữ liệu của nhóm là dữ liệu bảng nhiều bảng liên kết, có cả không gian, thời gian và chỉ số định lượng, đủ để trả lời bài toán đầu tư theo nhiều góc nhìn."

---

## Slide W3 - Why (Task): Mình cần trả lời điều gì?
- Nhóm tác vụ phân tích cần có:
1. Discover: phát hiện thị trường/thể loại/ngôn ngữ nổi trội.
2. Compare: so sánh giữa các nhóm thể loại, quốc gia, mức ngân sách.
3. Rank: xếp hạng ROI, xếp hạng thể loại chất lượng cao.
4. Correlate: tìm mối liên hệ giữa ngân sách-doanh thu, doanh thu-điểm số.
5. Summarize: tổng hợp insight để đề xuất ưu tiên đầu tư.

Lời thoại gợi ý (15-20s):
"Phần Why giúp xác định dashboard không chỉ để mô tả, mà để hỗ trợ các tác vụ so sánh, xếp hạng, tìm tương quan và đề xuất hành động."

---

## Slide W4 - Nguyên tắc đặt câu hỏi
- Câu hỏi phải có giá trị quyết định, không mô tả cho vui.
- Câu hỏi không trùng nhau, mỗi câu phục vụ một góc nhìn riêng.
- Độ khó vừa phải: đủ sâu để có insight, nhưng vẫn trả lời được bằng dữ liệu hiện có.
- Chưa trả lời ở slide này; chỉ ghi nhận bộ câu hỏi để dùng cho phần phân tích sau.

---

## Slide W5 - Bộ 10 câu hỏi phân tích (đã phân nhóm)

### Nhóm 1 - Thị trường và phân phối nội dung
1. Quốc gia nào đóng góp quy mô phim lớn nhất, và mức độ tập trung thị trường đang cao đến đâu?
2. Cơ cấu ngôn ngữ hiện tại đang đa dạng toàn cầu hay phụ thuộc vào một vài ngôn ngữ chủ đạo?
3. Ở các thị trường lớn, nhóm thể loại chủ lực có giống nhau hay khác biệt rõ nét?

### Nhóm 2 - Chất lượng nội dung
4. Thư viện phim hiện nghiêng về mức điểm nào, và khoảng chất lượng nào đang chiếm đa số?
5. Thể loại nào vừa duy trì được quy mô lớn vừa có độ ổn định điểm đánh giá tốt?
6. Tăng ngân sách có tạo ra cải thiện điểm đánh giá một cách đồng đều không, hay chỉ hiệu quả ở một số phân khúc?

### Nhóm 3 - Hiệu quả tài chính
7. Thể loại nào mang lại ROI trung bình cao và bền vững hơn so với các nhóm còn lại?
8. Xu hướng phân bổ ngân sách theo thời gian đang dịch chuyển về những thể loại nào?

### Nhóm 4 - Năng lực sáng tạo
9. Nhóm đạo diễn nào cân bằng tốt nhất giữa mục tiêu thương mại (doanh thu) và mục tiêu chất lượng (điểm đánh giá)?
10. Mức đa dạng thể loại trong từng phim tác động thế nào đến độ phổ biến và điểm đánh giá trung bình?

---

## Slide W6 - Chuyển tiếp sang phần trả lời câu hỏi
- Từ đây trở đi, mỗi tab dashboard sẽ được dùng để trả lời một nhóm câu hỏi cụ thể.
- Mục tiêu cuối cùng: đề xuất hướng đầu tư nội dung có cơ sở dữ liệu cho Netflix.

Lời kết gợi ý (10-15s):
"Như vậy, What giúp ta biết mình có dữ liệu gì; Why giúp ta biết cần trả lời điều gì. 10 câu hỏi trên sẽ là khung xuyên suốt cho phần phân tích tiếp theo."