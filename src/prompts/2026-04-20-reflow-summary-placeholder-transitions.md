# Objective

- Chia lại flow trong summary.md theo yêu cầu mới của user.
- Giữ nguyên cách trả lời nội dung chính, chỉ chỉnh phân vai và câu chuyển cảnh.
- Đưa luồng về dạng: 1 người nói mở + slide 1-18, rồi 10 câu hỏi theo A/B/C/D, sau đó mới quay lại kết luận và QA.

# Context

- User phản hồi summary.md đang lệch so với script-for-slide.md và answer style hiện có.
- User yêu cầu không đổi cách trả lời, chỉ đổi chuyển cảnh và cấu trúc người nói.
- Ràng buộc phân vai mới:
  - Người Slide: mở + slide 1-18.
  - A/B/C/D: chia 10 câu hỏi theo 3-3-2-2.
  - Công: chỉ đọc kết luận cuối, dẫn QA, và chốt buổi.

# Final Prompt

#file:summary.md giờ chia lại đi với lại nội dung có vẻ khác với bên file #file:script-for-slide.md và các câu trả lời trong mấy cái #file:answer tôi kêu bạn đừng thay đổi cách trả lời mà chỉ chuyển sau cho chuyển cảnh phù hợp để thuyết trình thôi mà, giờ việc thì mở + toàn bộ slide (sẽ không đi tới phần kết luận -> kết luận khi nào xong thuyết trình dashboard thì mới quay lại slide QA (tôi chưa thêm sẽ thêm sau)) sẽ là 1 người (chưa biết ai sẽ nói nên không cần ghi tên), 10 câu hỏi thì (trừ Công) ra thì còn 4 người sẽ có 2 người 3 câu và 2 người 2 câu chưa biết ai nên để A,B,C,D để tôi phân sau, rồi kết luận thì tôi s người nói cuối sẽ dẫn tới kết luận rồi mới tới Công nói phần kết luận, sẽ chiếu lại cái slide kết luận đọc rồi đọc cái gì khúc này, sau đó sẽ quay slide QA thì nên dẫn sau rồi trả lời xong thì dẫn sao để kết, thì bạn giúp tôi

# Expected Output

- scripts/final/summary.md được chia lại đúng luồng mới bằng placeholder (Người Slide, A, B, C, D, Công).
- Không thay đổi nội dung trả lời cốt lõi của 10 câu; chỉ đổi cấu trúc chuyển cảnh.
- Có câu dẫn rõ cho 3 điểm: D dẫn về slide kết luận, Công dẫn sang slide QA, Công chốt buổi sau QA.
