# Request Summary

User requested expanding the answer sections in the final summary script because they were too short for presentation. User explicitly asked to preserve key content from prepared team answer files (1-2-3.docx, 4,5,6.docx, 7-8.docx, and 9-10.md).

# Files Changed

- scripts/final/summary.md
- src/prompts/2026-04-20-expand-summary-answers-from-docx.md
- docs/ai/2026-04-20-expand-summary-answers-from-docx.md

# Key Decisions

- Kept the current summary flow and transitions (question-list first, then sequential answers).
- Expanded each answer block (Q1-Q10) to include:
  - how to read the chart/design cues,
  - core insight and decision implication.
- Preserved previously agreed terminology preference:
  - What-Why stays in English,
  - content remains mostly Vietnamese and presentation-oriented.
- Used source answer materials as semantic reference, then rewrote into consistent summary voice.

# Next Steps

1. Optional: create a shorter rehearsal variant (per answer ~25-35 seconds) if runtime exceeds 30 minutes.
2. Optional: mirror the same expanded style to scripts/individual files for consistency during Q&A.
