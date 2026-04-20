# Objective

- Tổng hợp toàn bộ nội dung hiện có thành gói thuyết trình 30 phút cho 5 thành viên.
- Bảo đảm công bằng thời lượng nói, có chuyển cảnh mượt, có kịch bản hỏi đáp.
- Tạo thêm bộ câu hỏi mức vừa để đưa cho team khác hỏi lại nhóm.

# Context

- Đã có bộ slide 20 trang và script ngắn theo slide.
- Đã có bộ 10 câu hỏi và nội dung trả lời nhóm câu 1-10.
- Các file đích cần điền còn trống:
  - scripts/final/summary.md
  - scripts/individual/cong.md
  - scripts/individual/thinh.md
  - scripts/individual/de.md
  - scripts/individual/hieu.md
  - scripts/individual/quan.md
- Cần sinh thêm bộ câu hỏi phản biện ở docs/human/question_for_other_team.
- Yêu cầu trình bày thực tế: không nói quá lệch với dashboard hiện tại và dữ liệu đã xử lý.

# Final Prompt

Tổng hợp lại tất cả nội dung đang có thành 1 gói trình bày 30 phút cho nhóm 5 người. Viết bản kịch bản tổng ở scripts/final/summary.md, tách kịch bản riêng cho từng người ở scripts/individual, và tạo bộ câu hỏi mức vừa để đưa cho team khác hỏi team mình ở docs/human/question_for_other_team. Bảo đảm công bằng thời lượng và chuyển cảnh mượt.

# Expected Output

- scripts/final/summary.md có run-of-show 30 phút đầy đủ: mở đầu, dữ liệu, phân tích, demo, hỏi đáp.
- 5 file scripts/individual/\*.md có lời thoại theo đúng vai trò từng người, mỗi người 5 phút chính + 1 phút hỏi đáp.
- 1 file câu hỏi mức vừa trong docs/human/question_for_other_team để dùng phản biện chéo.
- Nội dung bám đúng dashboard hiện có và số liệu xử lý hiện hành.
