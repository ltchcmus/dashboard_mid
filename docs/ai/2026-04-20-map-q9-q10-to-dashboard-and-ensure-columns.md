# Request Summary

User asked to follow the answering style of prior DOCX files and produce a markdown guide for answering question 9 and 10 from the dashboard, including tab/chart mapping and suitability checks. User also requested a separate ensured answer about whether processed data has 17 or 18 columns after dropping duration.

# Files Changed

- docs/human/answer/9-10.md
- src/prompts/2026-04-20-map-q9-q10-to-dashboard-and-ensure-columns.md
- docs/ai/2026-04-20-map-q9-q10-to-dashboard-and-ensure-columns.md

# Key Decisions

- Used tab Sáng tạo as the primary source for both Q9 and Q10.
- For Q9, selected the director scatter plot as main chart and explicitly noted a limitation: it is strong for candidate identification but not sufficient alone for a definitive single best ranking without a composite score table.
- For Q10, selected the genre-diversity combo chart (bar + line), which directly maps to the question variables and is suitable for answering.
- Verified column count by reading both raw and processed CSV headers: duration is removed, language is split into language_code and language_name; therefore processed columns remain 18.

# Next Steps

1. Optionally add a ranking table for Q9 directly in the dashboard UI to eliminate ambiguity.
2. Optionally include confidence intervals or dispersion metrics for Q10 to strengthen statistical caution.
3. Align slide/script statements about processed column count to 18 (not 17) for consistency.
