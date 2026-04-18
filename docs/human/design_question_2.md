# 📊 Tài liệu Đặc tả: Dashboard Phân tích Dữ liệu Netflix (Streamlit)

Tài liệu này mô tả chi tiết các yêu cầu kỹ thuật và nghiệp vụ cho dashboard phân tích dữ liệu Netflix xây dựng bằng Streamlit. Dashboard tập trung khai thác insight về chất lượng nội dung, hiệu quả tài chính và tác động toàn cầu.

---

## 🎨 1. Hệ thống Thiết kế (Design System)

* **Giao diện:** Chế độ sáng (Nền trắng `#F8F9FA`).
* **Bảng màu chủ đạo:** 
    * `#E50914` (Đỏ Netflix): Dùng cho tiêu đề, nút chính và điểm dữ liệu quan trọng.
    * `#008080` (Xanh ngọc hiện đại): Dùng cho chỉ số tài chính và thành phần phụ.
    * `#2E4057` (Xám xanh đậm): Dùng cho văn bản và nhãn trục.
* **Bộ lọc Toàn cục (Thanh bên):**
    * `Năm phát hành`: Thanh trượt (chọn khoảng).
    * `Thể loại`: Chọn nhiều (có tùy chọn "Chọn tất cả").
    * `Ngôn ngữ`: Danh sách thả xuống (Top 20 + "Khác").
    * `Quốc gia`: Chọn nhiều (tùy chọn, dùng cho phân tích sâu).
* **Chỉ số KPI (Đầu trang Dashboard):**
    * **Tổng doanh thu** → `${df['revenue'].sum()/1e9:.1f} Tỷ USD`
    * **Điểm đánh giá trung bình** → `{df['vote_average'].mean():.1f}/10`
    * **Thể loại phổ biến nhất** → `{top_genre}`
    * **Tỷ suất lợi nhuận trung bình (ROI)** → `{avg_roi:.1%}`

---

## 📑 2. Cấu trúc Tab & Mạch kể chuyện (Storytelling)

### Tab 1: 🌍 Toàn cảnh Netflix toàn cầu
**Mục tiêu:** Hiểu rõ phạm vi địa lý và sự đa dạng ngôn ngữ trong thư viện nội dung.

* **Câu hỏi 1: Quốc gia nào là "công xưởng" sản xuất nội dung chính?**
    * **Loại biểu đồ:** 🗺️ **Bản đồ nhiệt thế giới** (Choropleth Map)
    * **Dữ liệu:** `country` (ánh xạ mã ISO), `số lượng phim`, `điểm đánh giá trung bình` (làm thang màu)
    * **Insight:** Xác định các trung tâm sản xuất ngoài Hollywood (ví dụ: Hàn Quốc, Ấn Độ, Tây Ban Nha). Di chuột hiển thị thống kê chi tiết.
    * **Tương tác:** Nhấn vào quốc gia để lọc toàn bộ dashboard (cross-filtering).

* **Câu hỏi 2: Sự đa dạng ngôn ngữ trên nền tảng thể hiện thế nào?**
    * **Loại biểu đồ:** 🌳 **Biểu đồ cây** (Treemap)
    * **Dữ liệu:** `ngôn ngữ` → `thể loại` → `số lượng`, tô màu theo `độ phổ biến trung bình`
    * **Insight:** Trực quan hóa tỷ trọng nội dung bản địa hóa. Kết hợp ngôn ngữ - thể loại nào thu hút tương tác mạnh nhất?

* **Câu hỏi 3: Thể loại nào đang "thống trị" về mặt số lượng?**
    * **Loại biểu đồ:** 📊 **Biểu đồ cột ngang** (kèm phân tách theo quốc gia)
    * **Dữ liệu:** `genres` (đã tách), `country` (xếp chồng hoặc tô màu)
    * **Insight:** Hiểu rõ xu hướng thể loại theo khu vực: ví dụ "Hành động thống trị tại Mỹ, Lãng mạn chiếm ưu thế tại Hàn Quốc".

---

### Tab 2: 🎯 Chất lượng & Chiến lược nội dung
**Mục tiêu:** Đánh giá hiệu suất nội dung dưới góc nhìn chiến lược – không chỉ dừng ở tương quan, mà đưa ra định hướng hành động.

* **Câu hỏi 4: 🔄 Chất lượng phim phân bố thế nào, và thể loại nào chiếm ưu thế trong nhóm phim "chất lượng cao"?**
    * **Loại biểu đồ:** 🍩 **Kết hợp Donut Chart + Horizontal Bar Chart** (2-panel layout)
    * **Layout:** `st.columns([1, 2])` → Donut bên trái, Bar chart bên phải
    * **Panel 1 (Donut): Phân bố điểm đánh giá tổng thể**
        - Chia bucket: `0-5` (Kém), `5-6` (Trung bình), `6-7` (Khá), `7-8` (Tốt), `8-10` (Xuất sắc)
        - Màu: Gradient từ đỏ → xanh lá (`#d62728` → `#2ca02c`)
        - Insight: "% phim đạt điểm >= 7 là bao nhiêu? Có đáng để tự tin về chất lượng thư viện?"
    * **Panel 2 (Bar): Top thể loại trong nhóm phim chất lượng cao (rating >= 7.5)**
        - Lọc: `df[df['vote_average'] >= 7.5]`
        - Trục Y: `thể loại` (Top 10), Trục X: `số lượng phim`
        - Màu: Theo `avg_popularity` hoặc `avg_ROI` để thêm chiều so sánh
        - Insight: "Trong số phim chất lượng cao, thể loại nào Netflix đang làm tốt nhất? Có genre nào 'ngách nhưng chất' không?"
    * **Logic tiền xử lý:**
    ```python
    # Bucket rating cho donut chart
    bins = [0, 5, 6, 7, 8, 10]
    labels = ['Kém (0-5)', 'TB (5-6)', 'Khá (6-7)', 'Tốt (7-8)', 'Xuất sắc (8-10)']
    df_viz['rating_bucket'] = pd.cut(df_viz['vote_average'], bins=bins, labels=labels, include_lowest=True)
    donut_data = df_viz['rating_bucket'].value_counts().sort_index()
    
    # Lọc phim chất lượng cao cho bar chart
    high_quality = df_viz[df_viz['vote_average'] >= 7.5].copy()
    top_genres_hq = high_quality['genres'].value_counts().head(10)
    ```
    * **Insight kỳ vọng:**
        - 🍩 Donut: "Chỉ ~15% phim đạt điểm >= 8 → cơ hội cải thiện chất lượng vẫn lớn"
        - 📊 Bar: "Tài liệu & Chính kịch chiếm 40% phim chất lượng cao → đây là 'thế mạnh' cần duy trì"
        - 🎯 Hành động: Khi acquisition, ưu tiên genre có mặt trong top bar chart; cân nhắc đầu tư marketing cho phim rating 7-8 để đẩy lên nhóm "Xuất sắc"
    * **Tương tác:**
        - Click vào slice donut → lọc bar chart theo bucket đó (optional)
        - Hover bar chart → hiển thị avg_popularity, avg_ROI của genre

* **Câu hỏi 5: 🎯 "Điểm rơi lợi nhuận": Ngân sách nào mang lại chất lượng tốt nhất?**
    * **Loại biểu đồ:** 🧱 **Biểu đồ phân nhóm 2D / Histogram 2 chiều**
    * **Trục:** X: `Nhóm ngân sách` (Thấp/Trung bình/Cao), Y: `Nhóm điểm số` (<6 / 6-7.5 / >7.5)
    * **Màu/Kích thước:** `Số lượng phim` hoặc `ROI trung bình`
    * **Insight:** Xác định khoảng ngân sách có xác suất tạo ra phim chất lượng cao nhất. Ví dụ: "Phim ngân sách trung bình (20-80 triệu USD) có tỷ lệ đạt điểm >7.5 cao nhất".
    * **Tại sao tốt hơn ma trận tương quan?**: Ma trận chỉ nói "có liên quan hay không", biểu đồ này trả lời "nên rót vốn vào đâu".

* **Câu hỏi 6: Thể loại nào có chất lượng "ổn định" nhất (ít rủi ro phim dở)?**
    * **Loại biểu đồ:** 📊 **Biểu đồ cột ngang kèm thanh sai số**
    * **Dữ liệu:** 
        - Trục X: `Điểm trung bình`, Thanh sai số: `±1 độ lệch chuẩn`, Trục Y: `thể loại` (Top 15)
        - Tô màu theo `số lượng phim` (độ mờ), Sắp xếp: giảm dần theo điểm trung bình
    * **Insight:** Phim Tài liệu có điểm cao + độ lệch chuẩn thấp → rủi ro "phim tệ" thấp. Hành động có điểm trung bình nhưng dải rộng → nhiều bom tấn nhưng cũng nhiều phim lỗ.
    - **Hành động:** Khi cần nội dung "an toàn", ưu tiên thể loại có thanh sai số ngắn. Khi muốn "đánh lớn", chấp nhận rủi ro từ thể loại có dải phân tán rộng.

---

### Tab 3: 💰 Hiệu quả Đầu tư (Tài chính)
**Mục tiêu:** Phân tích dưới góc độ kinh doanh để xác định nội dung mang lại giá trị cao.

* **Câu hỏi 7: Top 10 phim có tỷ suất lợi nhuận (ROI) cao nhất?**
    * **Loại biểu đồ:** 📈 **Biểu đồ cột** (kèm thông tin khi di chuột)
    * **Công thức:** `ROI = (Doanh thu - Ngân sách) / Ngân sách`
    * **Cải tiến:** Tô màu cột theo `điểm đánh giá`, thêm họa tiết theo `độ phổ biến`
    * **Insight:** Nêu bật các tác phẩm "ngân sách thấp, lợi nhuận khủng". Chúng thuộc thể loại ngách hay ngôn ngữ cụ thể nào?

* **Câu hỏi 8: Ngân sách trung bình đầu tư cho mỗi thể loại qua các năm?**
    * **Loại biểu đồ:** 📉 **Biểu đồ đường đa tuyến** (kèm khoảng tin cậy)
    * **Logic:** Dùng **Trung bình** + dải `±1 độ lệch chuẩn` để thể hiện xu hướng và độ biến động vốn đầu tư
    * **Insight:** Theo dõi dịch chuyển vốn: ví dụ "Ngân sách phim Sci-Fi tăng gấp 3 lần từ 2020, nhưng ROI vẫn ổn định".

* **Câu hỏi 9: Ngân sách và Doanh thu theo từng nhóm ngôn ngữ?**
    * **Loại biểu đồ:** 🫧 **Biểu đồ bong bóng**
    * **Trục:** X: `Ngân sách TB`, Y: `Doanh thu TB`, Kích thước: `Số lượng phim`, Màu: `Ngôn ngữ`
    - **Insight:** Đánh giá hiệu quả kinh tế theo ngôn ngữ: ví dụ "Phim Hàn Quốc đạt 80% doanh thu phim Mỹ nhưng chỉ tốn 40% ngân sách".

* **Câu hỏi 10: 🆕 Thể loại nào có ROI "an toàn" nhất (ít biến động)?** *(Bổ sung)*
    * **Loại biểu đồ:** 📦 **Biểu đồ hộp (Box Plot) thể hiện phân phối ROI theo thể loại**
    * **Dữ liệu:** 
        - Trục X: `thể loại` (Top 12), Trục Y: `ROI`, Tô màu theo `trung vị ROI`
        - Thêm đường ngang tại `ROI = 0` (điểm hòa vốn)
        - Sắp xếp: giảm dần theo trung vị ROI
    * **Insight:** Kinh dị/Giật gân: trung vị ROI thấp nhưng "sàn" cao (hiếm khi lỗ nặng). Sci-Fi/Sử thi: trung vị cao nhưng "đuôi" kéo dài về âm → rủi ro cao, lợi nhuận lớn.
    * **Hành động:** Xây dựng danh mục đầu tư cân bằng: kết hợp thể loại "an toàn" (Kinh dị, Lãng mạn) để bù đắp rủi ro từ thể loại "mạo hiểm" (Sci-Fi, Chiến tranh).

---

### Tab 4: 🎬 Góc nhìn Sáng tạo
**Mục tiêu:** Khám phá vai trò của đội ngũ sản xuất và các yếu tố chủ đề trong nội dung thành công.

* **Câu hỏi 11: Những đạo diễn nào "mát tay" nhất?**
    * **Loại biểu đồ:** 🎯 **Biểu đồ phân tán (Ma trận hiệu suất đạo diễn)**
    * **Trục:** X: `Doanh thu TB`, Y: `Điểm đánh giá TB`
    * **Kích thước:** `Số lượng phim`, Màu: `Thể loại chính`
    * **Insight:** Xác định đạo diễn đảm bảo cả chất lượng nghệ thuật LẪN thành công thương mại → đối tác ưu tiên ký hợp đồng dài hạn.

* **Câu hỏi 12: Những diễn viên nào thường xuất hiện trong các phim "bom tấn"?**
    * **Loại biểu đồ:** 📊 **Biểu đồ cột ngang** (kèm phân tách thể loại)
    * **Chỉ số:** Top 15 diễn viên theo `Tổng doanh thu`
    * **Cải tiến:** Cột xếp chồng thể hiện đóng góp doanh thu theo từng thể loại
    * **Insight:** Chỉ ra "ngôi sao phòng vé" và hiểu rõ thể loại nào họ thường tỏa sáng nhất.

* **Câu hỏi 13: 🔄 Phim "đa thể loại" có dễ thành công hơn phim "thuần một thể loại"?**
    * **Loại biểu đồ:** 📈 **Biểu đồ kép: Cột nhóm + Đường**
    * **Dữ liệu:**
        - Trục X: `số thể loại` (1, 2, 3, 4+)
        - Trục Y trái (Cột): `độ phổ biến trung bình`
        - Trục Y phải (Đường): `điểm đánh giá trung bình`
        - Màu cột: `số lượng phim` (độ mờ)
    * **Insight:** Phim có 2-3 thể loại thường có độ phổ biến cao nhất (tiếp cận đa khán giả), nhưng điểm số có thể giảm nhẹ do "khó làm hài lòng tất cả". Phim 1 thể loại có điểm cao hơn nhưng phạm vi tiếp cận hẹp.
    * **Hành động:** Chiến lược nội dung: Phim hướng đại chúng → pha trộn 2-3 thể loại. Phim ngách/chuẩn giải thưởng → tập trung sâu vào 1 thể loại chất lượng.

---

## 🛠 3. Hướng dẫn Triển khai Kỹ thuật

| Hạng mục | Giải pháp đề xuất |
| :--- | :--- |
| **Xử lý dữ liệu** | • Dùng `df.explode()` cho `genres`, `cast`, `country` **chỉ trong hàm vẽ biểu đồ** (tránh explode toàn bộ gây tràn bộ nhớ)<br>• Tạo cột phụ lúc tiền xử lý: `nhóm_ngân_sách`, `nhóm_điểm_số`, `roi`, `so_the_loai` |
| **Logic tính toán** | • Luôn dùng `.mean()` + `.std()` cho chuỗi thời gian để xử lý bias do dataset giới hạn ~1k phim/năm<br>• Công thức ROI có kiểm tra chia cho 0: `np.where(budget>0, (revenue-budget)/budget, np.nan)`<br>• Thanh sai số: `y_error = df.groupby('genres')['vote_average'].std()` |
| **Trực quan hóa tương tác** | • Dùng **Plotly Express** cho mọi biểu đồ (hover, zoom, toggle legend)<br>• Dùng `st.plotly_chart(fig, use_container_width=True)`<br>• Thêm `st.expander("💡 Insight chính")` dưới mỗi biểu đồ để dẫn dắt câu chuyện |
| **Triển khai Bản đồ** | • Dùng `plotly.express.choropleth` với `locationmode="country names"`<br>• Ánh xạ tên quốc gia sang mã ISO3 bằng từ điển tra cứu<br>• Xử lý sự kiện click: `st.session_state.quoc_gia_chon = point.country` để lọc chéo |
| **Phân tích Phân vùng** | • Tính trung vị của `popularity` và `vote_average`<br>• Vẽ `vline`/`hline` tại giá trị trung vị kèm chú thích<br>• Dùng `fig.add_annotation()` để đặt tên 4 góc chiến lược + biểu tượng cảm xúc |
| **Biểu đồ Hộp ROI** | • Lọc bỏ ngoại lệ cực trị (>99th percentile) để biểu đồ dễ đọc<br>• Thêm `fig.add_hline(y=0, line_dash="dash", annotation_text="🎯 Điểm hòa vốn")`<br>• Tô màu hộp theo trung vị ROI |
| **Bố cục** | • `st.tabs(["🌍 Toàn cảnh", "🎯 Chất lượng", "💰 Tài chính", "🎬 Sáng tạo"])`<br>• Dùng `st.columns([2,1])` để xếp cặp biểu đồ + insight<br>• Bộ lọc sidebar dùng `st.session_state` để giữ trạng thái giữa các tab |
| **Tối ưu hiệu năng** | • Dùng `@st.cache_data` cho tải dữ liệu & tiền xử lý<br>• Giới hạn thao tác nặng (explode, groupby) trên tập con đã lọc<br>• Dùng `plotly.graph_objects` cho biểu đồ phức tạp để giảm dung lượng tải trang |

---

## ✅ Danh sách Kiểm tra Xác thực (AI Validation Checklist)

### Yêu cầu cốt lõi
- [ ] Bản đồ Choropleth tương tác, hỗ trợ nhấn quốc gia để lọc toàn dashboard
- [ ] Mọi biểu đồ đều có `st.expander("💡 Insight chính")` với 1-2 câu kết luận mang tính hành động
- [ ] Tính toán Ngân sách/Doanh thu xử lý an toàn giá trị NaN và lỗi chia cho 0
- [ ] Cột đa giá trị (`genres`, `cast`) chỉ được tách (explode) trong phạm vi hàm vẽ biểu đồ
- [ ] Lọc chéo hoạt động: chọn quốc gia/thể loại ở tab này ảnh hưởng đến tab khác (qua `st.session_state`)
- [ ] Giao diện sáng + màu chủ đạo Netflix áp dụng đồng nhất
- [ ] Code chạy độc lập với `pd.read_csv("netflix.csv")` và thư viện tối thiểu

### Xác thực theo Tab
- [ ] **Tab 2 Câu 6**: Biểu đồ cột kèm thanh sai số thể hiện `±1 độ lệch chuẩn`, sắp xếp giảm dần theo điểm trung bình
- [ ] **Tab 3 Câu 10**: Biểu đồ hộp ROI theo thể loại có đường hòa vốn tại y=0, loại bỏ ngoại lệ cực trị
- [ ] **Tab 4 Câu 13**: Biểu đồ kép vẽ chính xác độ phổ biến (cột) + điểm số (đường) theo số thể loại
- [ ] Tất cả biểu đồ mới dùng ánh sáng màu đồng nhất: hiệu suất cao=`#2ca02c`, thấp=`#d62728`
- [ ] Thanh sai số & khoảng tin cậy tính toán có xử lý NaN đúng chuẩn

### Trải nghiệm & Kể chuyện
- [ ] Mỗi tab có tiêu đề phụ ngắn: `"Tab này trả lời: [1-2 câu hỏi then chốt]"`
- [ ] Hover template hiển thị thông tin liên quan: tên phim, năm, thể loại, chỉ số chính
- [ ] Trạng thái không có dữ liệu khi lọc hiển thị thông báo thân thiện: `"Không có dữ liệu phù hợp với bộ lọc hiện tại. Vui lòng điều chỉnh lựa chọn."`
- [ ] Thẻ KPI cập nhật động theo bộ lọc thanh bên

---

## 📦 Phụ lục: requirements.txt

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.17.0