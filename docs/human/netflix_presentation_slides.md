# Netflix Movies Data Analysis: Giới thiệu & Tiền xử lý dữ liệu

## 1. Phân tích Dataset (High Level)

**Mô tả tổng quan:**
Bộ dữ liệu chứa thông tin chi tiết về các bộ phim trên Netflix, bao gồm các thuộc tính về nội dung, chất lượng đánh giá, và hiệu quả tài chính.

**Các hướng phân tích chính (Đề xuất):**
*   **Time (Thời gian):** Xu hướng phát hành và bổ sung nội dung theo năm/tháng. Nền tảng đang ưu tiên nội dung mới như thế nào trong các năm gần đây?
*   **Content (Nội dung):** Phân tích sự phân bổ thể loại (genres), quốc gia sản xuất (country), và ngôn ngữ nhằm hiểu chiến lược đa dạng hóa nội dung theo khu vực.
*   **Quality (Chất lượng):** Đánh giá mức độ hài lòng của khán giả (dựa trên `vote_average`, `popularity`) và mối tương quan với các yếu tố nội dung khác.
*   **Financial (Tài chính):** Phân tích mức độ chịu chi và hiệu quả đầu tư (`budget` vs `revenue`) của các dự án được đưa lên nền tảng.

---

## 2. Thiết kế Slide: Giới thiệu & Tiền xử lý dữ liệu

### 01 - Giới thiệu bộ dữ liệu

*   **Nguồn gốc:** Dữ liệu chi tiết về thư viện phim của Netflix (đến năm 2025).
*   **Quy mô ban đầu:** 16,000 dòng (dự án phim) và 18 phân loại thông tin (cột).
*   **Đặc điểm Dữ liệu:** Chứa đầy đủ các meta-data cấu trúc (đạo diễn, diễn viên, 133 quốc gia, 19 thể loại) cùng dữ liệu tài chính (Ngân sách, Doanh thu) và đánh giá của khán giả.
*   **Ý nghĩa thực tiễn (Business Value):** Giúp hiểu rõ chiến lược phát triển kho nội dung của Netflix, xác định các yếu tố tạo nên sự thu hút và thành công của một bộ phim trên nền tảng streaming.
*   **Lý do chọn đề tài:** Streaming đang thống trị ngành giải trí. Phân tích kho nội dung của "gã khổng lồ" Netflix mở ra góc nhìn sâu sắc về thị hiếu khán giả và xu hướng công nghiệp điện ảnh thời đại số.

### 02 - Tiền xử lý dữ liệu (Data Preprocessing)

*   **Bước 1: Kiểm tra cấu trúc & Missing Values (Dữ liệu gốc)**
    *   Phát hiện cột `duration` trống 100% (16,000 missing) -> Quyết định loại bỏ hoàn toàn.
    *   Các trường hợp thiếu dữ liệu rải rác: `country` (466 dòng), `cast` (204 dòng), `director` (132 dòng), `description` (132 dòng), và `genres` (107 dòng).
*   **Bước 2: Xử lý Missing Values & Lọc dữ liệu**
    *   Kiểm tra và loại bỏ các dòng bị khuyết thông tin quá quan trọng hoặc không hợp lệ.
    *   Kết quả: Tổng cộng đã lọc bỏ 761 dòng dữ liệu bị lỗi/thiếu (chiếm ~4.76% tổng dữ liệu). Tỷ lệ hao hụt cực thấp, đảm bảo nguyên vẹn độ tin cậy của Data.
*   **Bước 3: Tách dữ liệu & Làm sạch định dạng**
    *   Bộ dữ liệu còn lại **15,239 dòng** (movies) hoàn thiện.
    *   Tách các cột đa giá trị (phân cách bởi dấu phẩy) thành bảng phụ để chuẩn hóa.
    *   *Kết quả sau phân tách: 33,953 thành viên Cast, 9,631 Đạo diễn, tại 133 Quốc gia và 19 Thể loại nội dung.*
*   **Bước 4: Feature Engineering**
    *   Tạo các biến tài chính phái sinh (ROI) để chuẩn hóa rủi ro đầu tư.
    *   Phân cụm chất lượng/Mảng dữ liệu phân cấp (Aggregation) dựa trên thực thể (Đạo diễn/Diễn viên).

---

## 3. Feature Engineering (Các biến & Phép tính tạo mới)

Dựa trên code và design dashboard, dữ liệu Netflix đã được Engineering sâu hơn để khai thác tối đa tri thức (Insights):

*   **Phân cụm chất lượng phim (Categorization - Segmentation):**
    *   `Nhóm phim`: Tính toán phân vị thứ 3 (75th percentile / Q3) của độ phổ biến (`popularity`) và điểm số (`vote_average`) để phân loại tự động thành 4 tập: 
        *   *"Vừa nổi tiếng vừa chất lượng"* (High Pop + High Vote)
        *   *"Bom tấn đại chúng"* (High Pop)
        *   *"Phim được đánh giá cao - Cult Classics"* (High Vote)
        *   *"Nhóm còn lại"*
*   **Các biến phân cực Tài chính (Financial Features):**
    *   `roi` (Return on Investment): Tính bằng phép chia `revenue / budget`. Là "chỉ số vàng" để lật tẩy những siêu phẩm kinh phí thấp thu lợi nhuận khổng lồ, chứ không chỉ nhìn vào dòng tiền lớn (Revenue).
*   **Trích xuất chỉ số Thực thể sinh lời (Entity Aggregation):**
    *   Tính toán chỉ số uy tín của **Đạo diễn**: Gộp nhóm và tính `doanh_thu_trung_binh`, `diem_danh_gia_trung_binh` (Chỉ lấy các director đạo diễn ≥ 2 phim để bỏ nhiễu).
    *   Tính toán sức hút gốc của **Diễn viên**: Gộp và tính `% Tổng doanh thu` mang về theo Diễn viên, từ đó chắt lọc ra các "Bảo chứng phòng vé" chính hiệu.
*   **Xử lý ngôn ngữ tự nhiên cơ bản (Text / NLP):**
    *   Gom nhóm trường `description` (Mô tả phim) với điều kiện là các phim cực kỳ xuất sắc (`vote_average > 8.0`). Thông qua Word Cloud, nhặt ra các Head-words (từ khóa cốt lõi) định hình chủ đề thành công.
