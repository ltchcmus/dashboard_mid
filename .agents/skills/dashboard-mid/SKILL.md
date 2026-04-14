---
name: dashboard-mid
version: 1.1.0
description: "Use when working on this repository for streamlit dashboard, slide storyline generation, presentation scripts, README updates, requirements/dockerfile updates, and folder-structure alignment across .agents, data, docs, scripts, and src."
---

# Dashboard Mid Skill

## Purpose

Ensure all agent work is aligned with the current folder mapping for dashboard, slide generation, and presentation scripts.

## Project intent

This repository supports:

- Dashboard rendering with Streamlit.
- Slide storyline generation.
- Presentation script generation for individuals and final merged delivery.

## Required folder contracts

- `src/`: Application source code only.
- `data/raw/`: Raw immutable input data.
- `data/outputs/slides/markdown/`: Generated slide content in markdown.
- `data/outputs/slides/pptx/`: Exported PowerPoint files.
- `scripts/individual/`: Per-person speaking scripts.
- `scripts/final/`: Final merged speaking scripts.
- `docs/ai/`: AI-facing rules and prompt guidance.
- `docs/human/`: Human-facing operation and presentation notes.

## Coding rules

- Keep each module focused on one concern.
- UI updates belong in `src/tabs/`.
- Business logic belongs in `src/services/`.
- Visualization logic belongs in `src/visualization/`.
- Domain schemas belong in `src/models/`.
- Prompt artifacts belong in `src/prompts/`.
- Shared helpers belong in `src/utils/`.

## Output rules

For slide generation:

- Output markdown first.
- Keep bullets concise and action-oriented.

For script generation:

- Include opening, core body, and closing.
- Include timing guidance in seconds.

## Change checklist

Before editing:

1. Read `README.md` and relevant folder README files.
2. Confirm the correct input and output locations.

During editing:

1. Do not mix generated outputs into `src/`.
2. Do not route speaking scripts into `data/outputs/`.
3. Keep README and skill files updated with any structure changes.

After editing:

1. Verify paths and run commands still work.
2. Verify root `README.md` matches the real tree.
3. Verify dockerfile and requirements align with Streamlit runtime.

## Definition of done

A task is complete only when:

- Folder responsibilities are preserved.
- Output routing is correct.
- Documentation reflects real structure.
- Streamlit entry workflow remains executable.
