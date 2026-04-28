# Objective

Refactor cấu trúc code để tách main.py thành các module rõ ràng và đưa toàn bộ cấu hình sang config.yaml (đọc bằng YAML).

# Context

Code hiện tại tập trung trong src/main.py, cần tách thành các lớp/chức năng nhỏ để repo sạch và chuyên nghiệp hơn.

# Final Prompt

"Refactor lại repo cho clean: tách src/main.py thành các module (utils/services/tabs/visualization/config), chuyển settings và thông số sang config.yaml và dùng YAML để đọc."

# Expected Output

- config.yaml ở root và module load YAML.
- Các module tách theo đúng vai trò (utils/services/tabs/visualization).
- src/main.py chỉ còn entrypoint gọn.
- README cập nhật để phản ánh config.yaml.
