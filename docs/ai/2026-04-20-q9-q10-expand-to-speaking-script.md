# Request Summary

User asked to rewrite and expand Q9-Q10 into direct presentation script content (not advisory language), and explicitly required grounding in final-tab source code.

# Files Changed

- docs/human/answer/9-10.md
- src/prompts/2026-04-20-q9-q10-expand-to-speaking-script.md
- docs/ai/2026-04-20-q9-q10-expand-to-speaking-script.md

# Key Decisions

- Rewrote all four core paragraphs (Design + Insight for Q9 and Q10) into speaking-friendly narrative.
- Anchored wording to implemented Creative tab logic:
  - Director scatter aggregates average revenue/rating and movie count.
  - Director filtering requires so_phim >= 2 and positive average revenue.
  - OLS trendline is based on log10(revenue) with log x-axis.
  - Actor chart uses summed revenue and top 15 contributors.
  - Genre diversity chart groups 1/2/3/4+ and compares popularity mean + rating mean.
- Removed recommendation tone ("nên làm") and replaced with direct answer script tone.
- Kept conclusions cautious for dynamic filters and included correlation-vs-causation caveat.

# Next Steps

1. Optionally sync this exact expanded style into scripts/final/summary.md for section Công (Q9-Q10).
2. Optionally create a short 30-second per-question rehearsal version.
