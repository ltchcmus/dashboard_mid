# Objective

Cap nhat README va dockerfile de phu hop voi cau truc repo va cach chay dashboard hien tai.

# Context

- Entrypoint chay Streamlit nam trong src/main.py.
- Du lieu doc tu data/processed theo config.yaml (app.data_dir).
- Dockerfile dang dung python:3.12-slim va chay streamlit run.

# Final Prompt

Hay chinh sua README.md va dockerfile de bo sung huong dan chay local, mo ta du lieu dau vao can thiet, va huong dan build/run Docker. Dockerfile can co cac bien moi truong Streamlit co ban va lenh CMD gon.

# Expected Output

- README.md co them muc cai dat, chay local, du lieu dau vao, Docker.
- dockerfile bo sung bien moi truong Streamlit va CMD don gian.
