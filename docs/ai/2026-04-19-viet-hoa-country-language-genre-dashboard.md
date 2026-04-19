# Request Summary
User requested converting language, genre, and country values from English to Vietnamese across the dashboard and changing the dashboard header/title to Vietnamese.

# Files Changed
- src/main.py
- requirements.txt
- src/prompts/2026-04-19-viet-hoa-country-language-genre-dashboard.md
- docs/ai/2026-04-19-viet-hoa-country-language-genre-dashboard.md

# Key Decisions
- Implemented runtime translation in data-loading layer instead of rewriting source CSV files.
- Added Vietnamese mapping for genres and language conversion by language code.
- Added country translation with alias/fallback logic and preserved an English country column for choropleth location compatibility.
- Updated map logic to display/select Vietnamese country names while using English names internally for Plotly geographic matching.
- Updated dashboard page title and visual header text to Vietnamese.

# Next Steps
1. Install new dependencies from requirements (babel, pycountry) in the runtime environment.
2. Run Streamlit app and verify all country/language/genre filters and chart labels appear in Vietnamese.
3. If any specific country names remain English due alias mismatch, add them to fallback alias map for strict localization.
