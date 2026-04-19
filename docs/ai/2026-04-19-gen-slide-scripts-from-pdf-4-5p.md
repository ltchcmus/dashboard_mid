# Request Summary

User requested generation of a full speaking script based on the designed PDF deck (TQH - Nhóm 7.pdf), with per-slide narration, saved in scripts/, and optimized for a 4-5 minute delivery.

# Files Changed

- scripts/final/2026-04-19-tqh-nhom7-script-4-5p.md
- src/prompts/2026-04-19-gen-slide-scripts-from-pdf-4-5p.md
- docs/ai/2026-04-19-gen-slide-scripts-from-pdf-4-5p.md

# Key Decisions

- Parsed the PDF deck page-by-page to mirror exact 20-slide order.
- Generated one consolidated final script in scripts/final (folder contract compliant).
- Kept each slide concise and assigned time windows to keep total runtime near 4:50.
- Preserved key facts from slides (dataset size, preprocessing reductions, 10-question conclusion framing).

# Next Steps

1. Rehearse once at natural speaking speed and adjust 2-3 longest slides if needed.
2. If presenting with multiple speakers, split this file into scripts/individual per section.
3. Optionally add speaker tags and handoff cues between presenters.
