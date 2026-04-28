---
name: dashboard-mid
version: 1.2.0
description: "Use when working in this repository to follow a fixed workflow: inspect repo structure, implement the request, log prompts in src/prompts, and log AI handover notes in docs/ai."
---

# Dashboard Mid Skill (Mirror)

Canonical skill path: `./skills/dashboard-mid/SKILL.md`.

## Fixed Workflow (Mandatory)

1. Read and understand the repository before editing.
   - Read `README.md`.
   - Read `docs/ai/README.md` and `src/prompts/README.md`.
   - Inspect the active folder tree under `.agents/`, `data/`, `docs/`, `scripts/`, and `src/`.
2. Confirm structure and ownership.
   - `src/` is source code only.
   - `data/outputs/slides/` is for generated slide artifacts.
   - `scripts/individual/` and `scripts/final/` are for speaking scripts.
3. Implement the user request.
   - Keep modules and responsibilities separated.
   - Do not move outputs into the wrong folder.
4. Log prompts after implementation (required).
   - Save reusable prompts or final prompts in `src/prompts/`.
   - Preferred file naming: `src/prompts/YYYY-MM-DD-task-slug.md`.
   - Minimum sections: Objective, Context, Final Prompt, Expected Output.
5. Log AI handover notes after implementation (required).
   - Save concise implementation notes in `docs/ai/`.
   - Preferred file naming: `docs/ai/YYYY-MM-DD-task-slug.md`.
   - Minimum sections: Request Summary, Files Changed, Key Decisions, Next Steps.
6. Verify and synchronize docs.
   - If folder structure changes, update `README.md` and both skill files.
   - Verify paths, commands, and runtime assumptions.

## Folder Contracts

- `config.yaml`: Central configuration for dashboard settings.
- `src/`: Application source code.
- `data/raw/`: Raw immutable input data.
- `data/outputs/slides/markdown/`: Generated markdown slide content.
- `data/outputs/slides/pptx/`: Exported PowerPoint files.
- `scripts/individual/`: Per-speaker presentation scripts.
- `scripts/final/`: Final merged presentation scripts.
- `docs/ai/`: AI-facing notes and handover documents.
- `docs/human/`: Human-facing guides and presentation materials.

## Guardrails

- Never write speaking scripts into `data/outputs/`.
- Never write generated artifacts into `src/`.
- Never finish a task without updating prompt logs and AI notes.

## Definition of Done

A task is done only when:

- The requested change is implemented.
- Prompt logs are updated in `src/prompts/`.
- AI notes are updated in `docs/ai/`.
- Folder responsibilities remain correct.
- Documentation matches the current repository state.
