# Request Summary

Cap nhat README va dockerfile de phu hop voi cau truc repo, du lieu dau vao, va cach chay Streamlit/Docker.

# Files Changed

- README.md
- dockerfile
- src/prompts/2026-04-29-readme-dockerfile-alignment.md
- docs/ai/2026-04-29-readme-dockerfile-alignment.md

# Key Decisions

- Bo sung huong dan chay local, danh sach file du lieu can co, va lenh Docker co ban.
- Them bien moi truong Streamlit (headless, address, port, disable usage stats) de dong bo voi cong bo cong 8501.

# Next Steps

- Chay `streamlit run src/main.py` de kiem tra dashboard.
- Build va run image Docker de xac nhan cong 8501.
