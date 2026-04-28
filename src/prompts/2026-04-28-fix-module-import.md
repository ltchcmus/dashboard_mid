# Objective

Fix lỗi ModuleNotFoundError khi chạy Streamlit do đường dẫn import từ package src.

# Context

Streamlit chạy file src/main.py dưới dạng script nên sys.path chưa chứa thư mục root, dẫn đến không tìm thấy module src.config.

# Final Prompt

"Fix lỗi ModuleNotFoundError: No module named 'src.config' khi chạy src/main.py bằng Streamlit."

# Expected Output

- src/main.py bổ sung sys.path để đảm bảo import từ src hoạt động khi chạy như script.
