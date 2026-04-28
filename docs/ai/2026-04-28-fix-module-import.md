# Request Summary

Sửa lỗi ModuleNotFoundError: No module named 'src.config' khi chạy Streamlit.

# Files Changed

- src/main.py
- src/prompts/2026-04-28-fix-module-import.md
- docs/ai/2026-04-28-fix-module-import.md

# Key Decisions

- Thêm ROOT_DIR vào sys.path ngay trong src/main.py để đảm bảo import dạng src.\* hoạt động khi chạy như script.

# Next Steps

- Chạy lại `streamlit run src/main.py` từ thư mục root để xác nhận lỗi đã hết.
