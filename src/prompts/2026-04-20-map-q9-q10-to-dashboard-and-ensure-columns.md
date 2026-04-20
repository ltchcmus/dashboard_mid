# Objective

- Refer to existing answer style from docs/human/answer/{1-2-3,4-5-6,7-8}.docx.
- Determine which dashboard tab/charts should answer question 9 and 10.
- Produce a markdown guidance file explaining how to answer Q9 and Q10, and explicitly state if any chart is not fully suitable.
- Verify whether processed data has 17 or 18 columns after dropping duration.

# Context

- Question file is docs/human/question/question.md.
- Dashboard logic is implemented in src/main.py.
- User asked for a practical answer plan and a separate ensured answer for the duration-column issue.

# Final Prompt

tham khảo cách trả lời trong 3 file docx và dựa vào data + code dashboard để xác định tab/biểu đồ cho câu 9,10; viết ra markdown cách trả lời 2 câu đó, nếu biểu đồ không phù hợp thì phải nói rõ. Đồng thời trả lời riêng việc sau tiền xử lý bỏ duration thì còn 17 hay 18 cột.

# Expected Output

- New markdown file in docs/human/answer for Q9-Q10.
- Clear mapping: question -> tab -> chart -> how to read -> answer wording.
- Explicit suitability assessment and limitation notes for each question.
- Verified column-count explanation backed by current dataset.
