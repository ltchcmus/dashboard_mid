# Request Summary

User requested enhancing the ROI top-project chart tooltip to show more information than ROI, specifically budget and revenue.

# Files Changed

- src/main.py
- src/prompts/2026-04-20-roi-hover-budget-revenue.md
- docs/ai/2026-04-20-roi-hover-budget-revenue.md

# Key Decisions

- Kept existing ROI filtering and ranking logic unchanged.
- Added Plotly custom_data (budget, revenue) to the ROI bar chart.
- Defined a custom hovertemplate so tooltip explicitly shows movie title, ROI, budget, and revenue.
- Preserved existing layout, axis configuration, and max-ROI annotation.

# Next Steps

1. Optionally format budget/revenue in tooltip using compact units (million/billion) for readability.
2. Optionally add absolute profit (revenue - budget) to tooltip as an extra metric.
3. Validate visual output on small-screen layout to ensure tooltip readability.
