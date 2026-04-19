# Objective
- Build ready-to-use slide content for topic introduction and data/EDA section, aligned with current dashboard code and actual dataset metrics.

# Context
- User is preparing intro + data slides in netflix_presentation_slides.md.
- Dashboard source of truth is src/main.py (4 tabs: Toan canh, Chat luong, Tai chinh, Sang tao).
- Raw/processed counts and missing-value statistics were verified from data files.

# Final Prompt
gio toi dang lam slide ve muc gioi thieu de tai cung nhu gioi thieu ve du lieu a, ban nen doc code de biet ro va xem file netflix_presentation_slides.md de biet them
...
y la ban doc xong roi ban dua ra giup toi noi dung can hien thi len slide, phan gioi thieu de tai (co nhung gi: li do chon ....), roi EDA data cac kieu nua

# Expected Output
- Revised, presenter-ready markdown content for intro/topic and EDA slides.
- Accurate metrics for raw/processed dataset, missing values, and bridge-table stats.
- Corrections for any slide claims that do not match current app logic (e.g., ROI formula, unsupported analyses).
