# Objective

- Replace English filter placeholder text in sidebar multiselects with Vietnamese text.

# Context

- User reported sidebar filters still display English placeholder "Choose options".
- Labels are already Vietnamese; only placeholder needed localization.
- File impacted: src/main.py.

# Final Prompt

oke rồi nha, nhưng mà bộ lọc việc vẫn còn tiếng anh

# Expected Output

- Sidebar filter placeholders become Vietnamese:
  - Quốc gia -> Chọn quốc gia
  - Thể loại -> Chọn thể loại
  - Ngôn ngữ -> Chọn ngôn ngữ
- No behavioral change in filtering logic.
