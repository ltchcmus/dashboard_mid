# Prompt Log - Logscale Map Scatter Header

## Objective
Improve readability of key charts and reduce header vertical space in the Streamlit dashboard.

## Context
- World map color was dominated by US counts, hiding differences among mid/low countries.
- Popularity vs vote scatter had severe overplotting near x ~ 0 with long-tail outliers.
- Top header bar consumed too much vertical space.

## Final Prompt
"Apply log color scale for country choropleth, use log x-axis plus lower point opacity for popularity scatter, and reduce header bar height."

## Expected Output
- Choropleth uses logarithmic color mapping with readable colorbar labels in original count scale.
- Scatter chart uses log x-axis, lower opacity for better density perception, and handles non-positive popularity values safely.
- Header bar height and top padding are reduced while preserving title visibility.
