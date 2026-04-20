# Netflix Movies Data Analysis

## A. Nội dung hiển thị cho cụm slide "Giới thiệu đề tài"

### Slide 1 - Tên đề tài và bối cảnh

**Tên đề tài đề xuất:**
Tối ưu chiến lược đầu tư nội dung phim Netflix toàn cầu: cân bằng độ phủ thị trường, chất lượng, hiệu quả tài chính và năng lực sáng tạo.

**Thông điệp mở đầu (1-2 câu):**
Trong bài toán streaming, Netflix không chỉ cần nhiều nội dung mà cần danh mục nội dung "đúng thị trường - đúng chất lượng - đúng suất đầu tư". Dự án này dùng dữ liệu phim đến năm 2025 để tìm ra các đòn bẩy ra quyết định nội dung.

### Slide 2 - Lý do chọn đề tài

- Ngành streaming đang chuyển từ "tăng trưởng theo số lượng" sang "tăng trưởng theo hiệu quả danh mục"; mỗi quyết định đầu tư nội dung đều tốn kém và ảnh hưởng trực tiếp đến tăng trưởng lẫn tỷ lệ giữ chân người dùng.
- Bộ dữ liệu cho phép nhìn trọn chuỗi giá trị nội dung: thị trường phân phối (quốc gia, ngôn ngữ, thể loại), mức độ đón nhận (vote_average, popularity), hiệu quả kinh doanh (budget, revenue), và vai trò của đội ngũ sáng tạo (đạo diễn, diễn viên).
- Đề tài có tính ứng dụng cao vì đã được triển khai thành dashboard tương tác theo 4 trụ cột, giúp nhà quản lý kiểm thử kịch bản đầu tư và ưu tiên danh mục dựa trên dữ liệu thay vì cảm tính.

### Slide 3 - Mục tiêu và câu hỏi nghiên cứu

**Mục tiêu tổng quát:**
Xác định đặc điểm danh mục phim mang lại cân bằng giữa quy mô phân phối, chất lượng nội dung và hiệu quả đầu tư.

**Câu hỏi cụ thể:**

- Thị trường nào (quốc gia, ngôn ngữ, thể loại) đang đóng góp quy mô nội dung lớn nhất?
- Mức ngân sách có liên quan thế nào đến chất lượng đánh giá?
- Thể loại nào cho ROI tốt và ổn định chất lượng hơn?
- Nhân tố sáng tạo (đạo diễn, diễn viên, độ đa dạng thể loại) tác động ra sao đến thành công?

---

## B. Nội dung hiển thị cho cụm slide "Giới thiệu dữ liệu + EDA"

### Slide 4 - Tổng quan dữ liệu

- **Nguồn dữ liệu:** Netflix movies detailed up to 2025. (href link = https://www.kaggle.com/datasets/bhargavchirumamilla/netflix-movies-and-tv-shows-till-2025?select=netflix_movies_detailed_up_to_2025.csv)
- **Quy mô dữ liệu gốc:** 16,000 dòng x 18 cột.
- **Sau tiền xử lý:** 15,239 dòng x 18 cột.
- **Mốc thời gian:** release_year từ 2010 đến 2025.
- **Loại nội dung trong bộ phân tích:** Movie (15,239 bản ghi).
- **Số ngôn ngữ:** 68 ngôn ngữ (top: English, French, Japanese, Korean, Spanish).

### Slide 4A - Summary feature trước tiền xử lý

- **Mục tiêu hiển thị:** cho người xem thấy dataset gốc có những feature nào và mức độ đầy đủ dữ liệu của từng feature trước khi đi vào các bước làm sạch.
- **Cấu trúc feature chính:** Định danh, Nội dung, Phân phối, Chất lượng, Tài chính, Nhân sự sáng tạo, Thời gian.
- **Điểm cần nhấn mạnh khi thuyết trình:** đa số feature đạt độ đầy đủ rất cao; các cột cần xử lý trọng tâm là duration, country, cast, director, description, genres.

![Tổng quan feature trước tiền xử lý](data/outputs/slides/eda_images/00_feature_overview_raw.png)

### Slide 5 - Kiểm định chất lượng dữ liệu và tiền xử lý

**Missing values trong dữ liệu gốc:**

- duration: 16,000
- country: 466
- cast: 204
- director: 132
- description: 132
- genres: 107

**Xử lý đã thực hiện:**

- Bỏ cột duration vì trống 100%.
- Loại các dòng thiếu trường trọng yếu: country, cast, director, description, genres.
- Chuẩn hóa cột số: release_year, vote_average, popularity, vote_count, budget, revenue.

**Kết quả:**

- Loại 761 dòng (~4.76%), giữ lại 95.24% dữ liệu -> đủ ổn định để phân tích.

th

### Slide 7 - EDA nhanh (các insight mở đề)

- **Độ phủ ngôn ngữ:** English chiếm ưu thế, sau đó là French, Japanese, Korean, Spanish.
- **Độ đầy đủ biến phân tích:** vote_average, popularity, budget, revenue đều đầy đủ trên 15,239 bản ghi.
- **Tập phim đủ điều kiện tính ROI:** 3,524 phim có budget > 5,000 và revenue > 0.
- **Hàm ý ban đầu:** có đủ mẫu để so sánh hiệu quả đầu tư theo thể loại và theo nhân tố sáng tạo.

---

## C. Feature engineering (bản nội dung ngắn gọn trên slide)

### Slide 8 - Biến và phép tính được dùng trong dashboard

- **ROI:**
  ROI = (revenue - budget) / budget
  (chỉ tính cho phim có budget > 5,000 và revenue > 0).
- **Nhóm chất lượng phim:** chia vote_average thành 5 mức
  Kém (0-5), TB (5-6), Khá (6-7), Tốt (7-8), Xuất sắc (8-10).
- **Nhóm ngân sách tứ phân vị (Q1-Q4):** dùng qcut để so sánh phân bố điểm số theo mức ngân sách.
- **Thực thể sáng tạo:**
  - Đạo diễn: tổng hợp doanh thu trung bình, điểm đánh giá trung bình, số phim (lọc đạo diễn >= 2 phim).
  - Diễn viên: tổng doanh thu theo diễn viên.
  - Đa dạng thể loại: số thể loại/phim và tác động đến popularity + điểm trung bình.

---

## D. Lưu ý để slide khớp 100% với code hiện tại

- Không nên nói ROI = revenue / budget; công thức đúng trong app là (revenue - budget) / budget.
- Không nên đưa Word Cloud vào phần hiện tại nếu bạn không trình bày notebook riêng, vì dashboard Streamlit chưa render Word Cloud.
- Không nên mô tả segmentation Q3 "High Pop + High Vote" nếu slide này theo sát dashboard hiện tại, vì logic này không phải trụ cột đang hiển thị trên app.

---

## E. Mẫu kết nối sang phần dashboard (1 slide chuyển)

Từ dữ liệu đã được làm sạch và chuẩn hóa, dashboard triển khai 4 góc nhìn để trả lời bài toán đầu tư nội dung:

1. Toàn cảnh thị trường (quốc gia - ngôn ngữ - thể loại)
2. Chất lượng nội dung
3. Hiệu quả tài chính
4. Năng lực sáng tạo

Đây là cơ sở để đưa ra khuyến nghị đầu tư nội dung cho Netflix theo hướng "đúng thị trường, đúng chất lượng, đúng hiệu quả".
