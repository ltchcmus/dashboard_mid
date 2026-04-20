# Request Summary

User asked to re-split summary.md because current flow differed from script-for-slide and answer style. The key constraint was to keep answer content style unchanged and only adjust speaking flow/transitions.

# Files Changed

- scripts/final/summary.md
- src/prompts/2026-04-20-reflow-summary-placeholder-transitions.md
- docs/ai/2026-04-20-reflow-summary-placeholder-transitions.md

# Key Decisions

- Replaced fixed speaker names in main flow with placeholders per request:
  - One unnamed speaker for opening + slide 1-18.
  - A/B/C/D for 10 dashboard questions.
  - Công reserved for final conclusion + QA transition + final closing.
- Applied 10-question split as 3-3-2-2:
  - A: Q1-Q3, B: Q4-Q6, C: Q7-Q8, D: Q9-Q10.
- Kept core answer statements intact from previous summary structure and only added/rewired transitions.
- Added explicit script lines user asked for:
  - D -> return to Conclusion slide.
  - Công -> move to QA slide.
  - Final closing line after QA.

# Next Steps

1. User assigns real names to A/B/C/D.
2. User adds the QA slide and reuses existing transition lines in summary.md.
3. Optional: mirror this same placeholder flow into scripts/individual/\*.md after final role assignment.
