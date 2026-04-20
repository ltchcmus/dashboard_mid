# Request Summary

User asked to reduce repetitive phrasing (especially repeated "nhóm đã đặt là") and requested a smoother delivery style, such as listing all questions first and then answering one by one.

# Files Changed

- scripts/final/summary.md
- src/prompts/2026-04-20-reduce-repetitive-question-restatement-summary.md
- docs/ai/2026-04-20-reduce-repetitive-question-restatement-summary.md

# Key Decisions

- Replaced repeated question-restatement sentence pattern with grouped question previews per section.
- Kept question cueing by section:
  - A: list 3 market questions, then answer with Trước tiên / Tiếp theo / Cuối cùng.
  - B: list 3 quality questions, then answer with Trước tiên / Tiếp theo / Cuối cùng.
  - C: list 2 finance questions, then answer with Trước tiên / Tiếp theo.
  - D: list 2 creativity questions, then answer with Trước tiên / Tiếp theo.
- Preserved existing insights, timing blocks, and speaker handoff flow.

# Next Steps

1. Rehearse once to confirm speaking rhythm and timing.
2. Optionally mirror the same transition style into scripts/individual files.
