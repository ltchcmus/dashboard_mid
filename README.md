# Dashboard Mid

## Cài đặt & chạy local

1. Tạo môi trường và cài thư viện:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Chạy dashboard:

```bash
streamlit run src/main.py
```

## Dữ liệu đầu vào

Ứng dụng đọc dữ liệu từ `data/processed/` theo cấu hình `app.data_dir` trong `config.yaml`.
Các file cần có tối thiểu:

- `movies.csv`
- `movie_genres.csv`
- `movie_countries.csv`
- `movie_casts.csv`
- `movie_directors.csv`

Nếu thiếu dữ liệu đã xử lý, hãy chạy `notebooks/preprocessing.ipynb` để sinh lại từ `data/raw/`.

## Cấu trúc thư mục

```text
Dashboard-Mid/
|- .agents/
|  |- SKILL.md
|  |- skills/
|     |- dashboard-mid/
|        |- SKILL.md
|- data/
|  |- raw/
|  |- outputs/
|     |- slides/
|        |- markdown/
|        |- pptx/
|- docs/
|  |- ai/
|  |- human/
|- src/
|  |- main.py
|  |- config/
|  |- tabs/
|  |- visualization/
|  |- services/
|  |- prompts/
|  |- utils/
|- config.yaml
|- requirements.txt
|- Dockerfile
```

## Mô tả ngắn gọn từng thư mục

- `.agents/`: Quy tắc và skill để agent làm đúng workflow của dự án.
- `data/raw/`: Dữ liệu gốc, giữ nguyên để truy vết.
- `data/outputs/slides/markdown/`: Nội dung slide dạng markdown.
- `data/outputs/slides/pptx/`: Slide đầu ra dạng file PowerPoint.
- `docs/ai/`: Tài liệu cho AI (prompt, quy tắc, checklist).
- `docs/human/`: Tài liệu cho người dùng và nhóm thuyết trình.
- `src/config/`: Cấu hình chung.
- `src/tabs/`: Các tab giao diện Streamlit.
- `src/visualization/`: Hàm dựng biểu đồ và trực quan hóa.
- `src/services/`: Logic nghiệp vụ cho dashboard, slide, script.
- `src/prompts/`: Prompt template và quy ước output.
- `src/utils/`: Hàm tiện ích tái sử dụng.

## Chạy bằng Docker

Build image:

```bash
docker build -f Dockerfile -t dashboard-mid .
```

Run container:

```bash
docker run --rm -p 8501:8501 dashboard-mid
```

Nếu muốn cập nhật dữ liệu trên máy host:

```bash
docker run --rm -p 8501:8501 -v ./data:/app/data dashboard-mid
```

## Chạy trực tiếp trên máy

Yêu cầu tối thiểu:

- Python 3.12 (khuyến nghị để đồng bộ với Dockerfile)
- `pip` khả dụng trong môi trường Python
- Dữ liệu đã xử lý trong `data/processed/`

Chạy:

```bash
pip install -r requirements.txt
streamlit run src/main.py
```
