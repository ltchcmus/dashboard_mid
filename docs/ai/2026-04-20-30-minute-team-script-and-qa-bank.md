# Request Summary

User requested a full 30-minute presentation package for a 5-member team: one master script, five individual scripts, and a moderate question bank for cross-team Q&A. The package had to stay consistent with the current dashboard implementation and existing question-answer assets.

# Files Changed

- scripts/final/summary.md
- scripts/individual/cong.md
- scripts/individual/thinh.md
- scripts/individual/de.md
- scripts/individual/hieu.md
- scripts/individual/quan.md
- docs/human/question_for_other_team/bo-cau-hoi-muc-vua.md
- src/prompts/2026-04-20-30-minute-team-script-and-qa-bank.md
- docs/ai/2026-04-20-30-minute-team-script-and-qa-bank.md

# Key Decisions

- Built a strict 30-minute structure with equal speaking load: each member 5 minutes main + 1 minute Q&A.
- Anchored script content to actual dashboard charts in src/main.py (4 tabs, 13 visual blocks, cross-filter behavior).
- Standardized data facts for speaking consistency (16,000x18 raw, 15,239x18 processed, 761 rows removed).
- Added explicit handling note for the 17 vs 18 processed-column discrepancy to prevent live confusion.
- Kept creative-section narration in cluster/threshold style (no dependence on pronouncing specific names).
- Created a moderate-difficulty Q&A bank grouped by data, method, insight, and limitations.

# Next Steps

1. Rehearse once with a timer using scripts/final/summary.md to verify each 5-minute segment.
2. Let each member rehearse from their own scripts/individual/\*.md and keep one backup shortening line.
3. Print or share the question bank file to other teams before Q&A so question difficulty stays balanced.
