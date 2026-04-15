# Netflix Data Storytelling Dashboard Design Document

This document outlines the technical and functional specifications for a Netflix data analysis dashboard built with Streamlit. The dashboard focuses on extracting insights regarding quality, financial performance, and global impact.

---

## 🎨 1. Design System

* **Theme:** Light Mode (White background).
* **Accent Colors:** * `#E50914` (Netflix Red): Used for titles and primary data points.
    * `#008080` (Modern Teal): Used for financial metrics and secondary elements.
* **System Filters (Sidebar):**
    * `Release Year`: Slider.
    * `Genres`: Multiselect.
    * `Language`: Dropdown.
* **Header KPIs:**
    * **Tổng doanh thu** (Total Revenue).
    * **Điểm đánh giá trung bình** (Avg Vote).
    * **Thể loại phổ biến nhất** (Top Genre).
    * **Tỷ lệ lợi nhuận trung bình (ROI)** (Avg ROI).

---

## 📑 2. Tab Structure & Storytelling Logic

### Tab 1: Toàn cảnh Netflix toàn cầu (Global Footprint)
**Objective:** Understand Netflix's geographic influence and linguistic diversity.

* **Question 1: Những quốc gia nào là "công xưởng" nội dung chính?**
    * **Chart Type:** Bản đồ nhiệt thế giới (World Choropleth Map).
    * **Features:** `Quốc gia`, `Mã phim`.
    * **Insight:** Identify key markets outside the US (e.g., South Korea, India, Spain).
* **Question 2: Sự đa dạng ngôn ngữ trên nền tảng như thế nào?**
    * **Chart Type:** Biểu đồ vùng (Treemap).
    * **Features:** `Tên ngôn ngữ`, `Số lượng phim`.
    * **Insight:** Visualize the proportion of localized content and the weight of non-English languages.
* **Question 3: Thể loại nào đang "thống trị" về mặt số lượng?**
    * **Chart Type:** Biểu đồ cột ngang (Horizontal Bar Chart).
    * **Features:** `Thể loại`.
    * **Insight:** Understand Netflix's production strategy and genre focus.

### Tab 2: Chất lượng & Sự đón nhận (Quality & Engagement)
**Objective:** Evaluate the correlation between popularity and critical/audience reception.

* **Question 4: Mối quan hệ giữa độ nổi tiếng và điểm số thực tế?**
    * **Chart Type:** Biểu đồ phân tán (Scatter Plot).
    * **Axes:** Trục X: `Độ phổ biến`, Trục Y: `Điểm đánh giá trung bình`.
    * **Insight:** Classify movies into "Blockbusters" (High Popularity), "Cult Classics" (High Score), or "Hidden Gems".
* **Question 5: Ma trận tương quan giữa chất lượng và tài chính?**
    * **Chart Type:** Biểu đồ nhiệt tương quan (Correlation Heatmap).
    * **Features:** `Độ phổ biến`, `Số lượt bình chọn`, `Điểm đánh giá`, `Ngân sách`, `Doanh thu`.
    * **Insight:** Verify if higher budgets actually lead to higher ratings or popularity.
* **Question 6: Phân bố điểm số theo từng thể loại?**
    * **Chart Type:** Biểu đồ hộp (Box Plot / Violin Plot).
    * **Features:** `Thể loại`, `Điểm đánh giá trung bình`.
    * **Insight:** Determine which genres have consistent quality versus those with polarizing reviews.

### Tab 3: Hiệu quả Đầu tư (Financial ROI)
**Objective:** Analyze data from a business perspective to identify high-value content.

* **Question 7: Top 10 phim có tỷ lệ lợi nhuận (ROI) cao nhất?**
    * **Chart Type:** Biểu đồ cột (Bar Chart).
    * **Formula:** `ROI = Doanh thu / Ngân sách`.
    * **Insight:** Highlight "low-budget, high-return" masterpieces with extreme commercial efficiency.
* **Question 8: Ngân sách trung bình đầu tư cho mỗi thể loại qua các năm?**
    * **Chart Type:** Biểu đồ đường (Multi-line Chart).
    * **Logic:** Use **Mean** (Trung bình) to avoid bias from the 1k records/year limit.
    * **Insight:** Track the shift of Netflix's capital investment across genres over time.
* **Question 9: Ngân sách và Doanh thu theo từng nhóm ngôn ngữ?**
    * **Chart Type:** Biểu đồ bong bóng (Bubble Chart).
    * **Axes:** X: `Ngân sách`, Y: `Doanh thu`, Size: `Doanh thu`.
    * **Insight:** Evaluate the economic efficiency of investing in multi-language content.

### Tab 4: Góc nhìn Sáng tạo (Creative Insights)
**Objective:** Explore the role of production teams and common themes in successful content.

* **Question 10: Những đạo diễn nào "mát tay" nhất?**
    * **Chart Type:** Biểu đồ phân tán (Scatter Plot).
    * **Axes:** X: `Doanh thu trung bình`, Y: `Điểm đánh giá trung bình`.
    * **Insight:** Identify directors who guarantee both artistic quality and commercial success.
* **Question 11: Những diễn viên nào thường xuất hiện trong các phim "bom tấn"?**
    * **Chart Type:** Biểu đồ cột ngang (Horizontal Bar Chart).
    * **Metric:** Top 15 by `Tổng doanh thu`.
    * **Insight:** Pinpoint "box office stars" who drive the most revenue on the platform.
* **Question 12: Đặc điểm chủ đề của các phim thành công (Rating > 8.0)?**
    * **Chart Type:** Đám mây từ ngữ (Word Cloud).
    * **Feature:** `Mô tả phim`.
    * **Insight:** Discover recurring keywords or themes found in highly-rated masterpieces.

---

## 🛠 3. Technical Implementation Guidelines

| Category | Proposed Solution |
| :--- | :--- |
| **Data Processing** | Use `df.explode('genres')` and `df.explode('cast')` for comma-separated string columns. |
| **Calculation Logic** | Always prioritize `.mean()` over `.sum()` for time-series charts to handle the 1k movies/year data constraint. |
| **Interactive Visualization** | Use **Plotly** (`plotly.express`) for hover effects, zooming, and dynamic legends. |
| **Statistical Charts** | Use **Seaborn/Matplotlib** for static charts like the Correlation Heatmap for precise aesthetic control. |
| **Layout** | Utilize `st.tabs()` for main navigation and `st.columns()` to place 2-3 charts side-by-side per row. |
