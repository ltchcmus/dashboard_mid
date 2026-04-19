# Request Summary
User asked for 3 things: PPTX readability capability, dashboard review comments focused on analytical content (not UI), and new slides explaining What-Why abstraction with 10 categorized questions.

# Files Changed
- data/outputs/slides/markdown/2026-04-19-nhan-xet-dashboard.md
- data/outputs/slides/markdown/2026-04-19-abstraction-what-why-10-cau-hoi.md
- src/prompts/2026-04-19-pptx-review-and-abstraction-what-why.md
- docs/ai/2026-04-19-pptx-review-and-abstraction-what-why.md

# Key Decisions
- Rewrote dashboard review to emphasize insights delivered by each tab (market, quality, finance, creativity) and removed UI-style commentary emphasis.
- Kept image-placement instructions because user still needs per-slide image insertion guidance.
- Created a dedicated What-Why slide script including brief methodology explanation and 10 non-overlapping, practical questions grouped into 4 main themes.
- Preserved project topic exactly as previously defined, without inventing a new one.

# Next Steps
1. If user provides PPTX file, parse and align this markdown directly to existing slide order.
2. Optionally compress question list into 1 summary slide + 1 appendix slide depending on presentation time.
3. In the next section of the deck, answer each question using corresponding dashboard tabs.
