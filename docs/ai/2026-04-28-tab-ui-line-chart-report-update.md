# Request Summary

- Make the dashboard tabs look clearly like tabs.
- Add detail to the genre-by-year line chart without removing existing charts.
- Finish baseline sections in the LaTeX report.

# Files Changed

- src/utils/style.py
- src/tabs/overview.py
- latex/Report datavis midterm/content/group-info.tex
- latex/Report datavis midterm/content/introduction-data.tex
- latex/Report datavis midterm/content/what-why.tex
- latex/Report datavis midterm/content/how-dashboard.tex
- latex/Report datavis midterm/content/discussion.tex
- latex/Report datavis midterm/content/references.tex
- src/prompts/2026-04-28-tab-ui-line-chart-report-update.md
- docs/ai/2026-04-28-tab-ui-line-chart-report-update.md

# Key Decisions

- Replaced pill-style tabs with a clear tab strip and active underline.
- Expanded the genre trend chart with top-N controls, optional "Khac" aggregation, and a total line.
- Added several chart descriptions in the report using existing images and updated references.

# Next Steps

- Run the Streamlit app to confirm tab visuals.
- Compile the LaTeX report to verify figures and references.
