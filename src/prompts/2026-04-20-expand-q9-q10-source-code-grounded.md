# Objective

- Expand Q9-Q10 answers to be deeper and more presentation-ready.
- Keep explanations grounded in the actual implementation of the Creative tab (no fabricated logic).

# Context

- User requested expanding 9-10 answer script, but explicitly asked to rely on the canonical source code of the final tab.
- Target file: docs/human/answer/9-10.md.
- Source of truth checked: src/main.py, function ve_tab_sang_tao.

# Final Prompt

#file:9-10.md hiện việc trả lời quá ngắn, bạn có thể giúp tôi mở rộng ra để trả lời hay hơn nữa không, khai thác sâu một tí nhưng đừng quá dài nha

(dựa vào source code chuẩn của tab cuối nha không bịa)

# Expected Output

- Q9 and Q10 sections are expanded moderately (deeper but not overly long).
- Wording explicitly reflects chart logic implemented in code (data construction, filters, axis behavior).
- Avoid hard claims not guaranteed by code or current filter state.
