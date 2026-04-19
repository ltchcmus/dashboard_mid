# Request Summary
User reported that the sidebar filters still showed English placeholder text and asked to make them Vietnamese.

# Files Changed
- src/main.py
- src/prompts/2026-04-19-sidebar-filter-placeholder-vietnamese.md
- docs/ai/2026-04-19-sidebar-filter-placeholder-vietnamese.md

# Key Decisions
- Localized placeholder text directly in each `st.sidebar.multiselect` call.
- Kept labels, keys, and filter logic unchanged to avoid regressions.
- Added explicit Vietnamese placeholders for country, genre, and language selectors.

# Next Steps
1. Refresh Streamlit app and verify placeholders in sidebar controls.
2. If any BaseWeb internal tooltips remain English, add CSS/UI-level override if needed.
