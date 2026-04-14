# Dashboard Mid

Dự án Streamlit phục vụ 3 mục tiêu liền mạch:

1. Render dashboard dữ liệu.
2. Sinh nội dung slide (storyline).
3. Sinh kịch bản thuyết trình theo từng người.

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
|- scripts/
|  |- individual/
|  |- final/
|- src/
|  |- main.py
|  |- config/
|  |- tabs/
|  |- visualization/
|  |- services/
|  |- models/
|  |- prompts/
|  |- utils/
|- requirements.txt
|- dockerfile
```

## Mô tả ngắn gọn từng thư mục

- `.agents/`: Quy tắc và skill để agent làm đúng workflow của dự án.
- `data/raw/`: Dữ liệu gốc, giữ nguyên để truy vết.
- `data/outputs/slides/markdown/`: Nội dung slide dạng markdown.
- `data/outputs/slides/pptx/`: Slide đầu ra dạng file PowerPoint.
- `docs/ai/`: Tài liệu cho AI (prompt, quy tắc, checklist).
- `docs/human/`: Tài liệu cho người dùng và nhóm thuyết trình.
- `scripts/individual/`: Kịch bản nói theo từng thành viên.
- `scripts/final/`: Kịch bản tổng hợp bản chốt.
- `src/config/`: Cấu hình chung.
- `src/tabs/`: Các tab giao diện Streamlit.
- `src/visualization/`: Hàm dựng biểu đồ và trực quan hóa.
- `src/services/`: Logic nghiệp vụ cho dashboard, slide, script.
- `src/models/`: Schema/model dùng chung.
- `src/prompts/`: Prompt template và quy ước output.
- `src/utils/`: Hàm tiện ích tái sử dụng.

## Luồng làm việc đề xuất

1. Đưa dữ liệu đầu vào vào `data/raw/`.
2. Phân tích trên dashboard Streamlit.
3. Sinh nội dung slide vào `data/outputs/slides/markdown/`.
4. Xuất slide vào `data/outputs/slides/pptx/` khi chốt.
5. Viết kịch bản theo người ở `scripts/individual/`.
6. Gộp bản chốt ở `scripts/final/`.

## Quy ước quan trọng

- Không đặt file output sinh tự động vào `src/`.
- Mọi thay đổi quy trình cần cập nhật lại skill ở `.agents/skills/dashboard-mid/SKILL.md`.
- `.agents/SKILL.md` là bản mirror để đọc nhanh trong repo.
