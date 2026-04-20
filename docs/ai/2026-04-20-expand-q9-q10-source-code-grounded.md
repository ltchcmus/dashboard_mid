# Request Summary

User asked to expand the Q9-Q10 script so answers are better and deeper, but explicitly required grounding in the final tab source code and avoiding fabricated claims.

# Files Changed

- docs/human/answer/9-10.md
- src/prompts/2026-04-20-expand-q9-q10-source-code-grounded.md
- docs/ai/2026-04-20-expand-q9-q10-source-code-grounded.md

# Key Decisions

- Expanded both Q9 and Q10 with richer speaking flow while keeping length moderate.
- Anchored wording to actual Creative tab logic in src/main.py:
  - Director scatter uses aggregated mean revenue/rating and movie count, with filters so_phim >= 2 and doanh_thu_trung_binh > 0.
  - OLS line is fit on log10(revenue), and x-axis is log-scaled.
  - Actor bar chart uses summed revenue by actor and top 15 entries.
  - Genre diversity chart groups 1/2/3/4+ genres and compares popularity mean + rating mean.
- Removed/avoided hard numeric assertions that may change with active filters.
- Added explicit caveat about observational relationship vs causal inference for Q10.

# Next Steps

1. Optionally sync the same source-code-grounded wording into scripts/final/summary.md section for Q9-Q10.
2. Optionally provide a shorter rehearsal variant (20-30 seconds per answer).
