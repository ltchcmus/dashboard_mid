---
name: dashboard-mid
version: 1.1.0
description: "Use when working on this repository for streamlit dashboard, slide storyline generation, presentation scripts, README updates, requirements/dockerfile updates, and folder-structure alignment across .agents, data, docs, scripts, and src."
---

# Dashboard Mid Skill (Mirror)

Canonical skill path: `./skills/dashboard-mid/SKILL.md`.

## Muc tieu

Dam bao agent thao tac dung folder, dung output path, va cap nhat tai lieu dong bo khi sua code.

## Pham vi du an

- Dashboard du lieu bang Streamlit.
- Sinh noi dung slide.
- Sinh kich ban thuyet trinh theo ca nhan va ban chot.

## Mapping thu muc bat buoc

- `src/`: Chiua ma nguon ung dung.
- `data/raw/`: Du lieu goc.
- `data/outputs/slides/markdown/`: Noi dung slide markdown.
- `data/outputs/slides/pptx/`: File slide pptx.
- `scripts/individual/`: Kich ban theo tung thanh vien.
- `scripts/final/`: Kich ban tong hop ban chot.
- `docs/ai/`: Tai lieu huong dan cho AI.
- `docs/human/`: Tai lieu huong dan cho nguoi dung.

## Quy tac chinh sua

1. Khong ghi script thuyet trinh vao `data/outputs/`.
2. Khong ghi file output vao `src/`.
3. Neu doi cau truc folder, phai cap nhat `README.md` va SKILL ngay lap tuc.
4. Uu tien mo ta ro input/output trong README truoc khi them logic moi.

## Hop dong output

Khi sinh slide:

- Tra ve markdown co cau truc.
- Moi bullet ngan gon, co tinh hanh dong.

Khi sinh script:

- Tach 3 phan: mo dau, trinh bay, ket.
- Co moc thoi gian de tap luyen.

## Checklist truoc khi ket thuc

1. Kiem tra duong dan output da dung folder.
2. Kiem tra README tong phan anh dung cau truc hien tai.
3. Kiem tra dockerfile va requirements khop voi cach chay Streamlit.
