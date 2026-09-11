---
name: organize-pdf-notes
description: Organize loose PDF files in a folder into subject-wise subfolders with descriptive numbered names (e.g. "GO notes 2.pdf" -> "Go Programming/02-Data-Types-Conditionals-and-Loops.pdf"). Works for ANY pdfs and any subjects. Use when the user asks to arrange/organize/sort/group PDFs or notes by subject, or says "organize my notes", "arrange these pdfs", "sort notes into folders", "rename notes properly".
---

# Organize PDF Notes (general purpose)

Turns any flat pile of PDFs into `Subject/NN-Descriptive-Name.pdf` folders. Subject detection and renaming are done by the agent reading each PDF's actual content; the script only extracts text and executes the moves.

## Quick start

```powershell
python "<USER_HOME>\.agents\skills\organize-pdf-notes\scripts\organize_notes.py" "<folder>" extract
# review the report, decide subjects + names, write plan.json, then:
python "<USER_HOME>\.agents\skills\organize-pdf-notes\scripts\organize_notes.py" "<folder>" apply --map plan.json [--dry-run]
```

## Workflow

1. **Extract** — run `extract`. Prints a report: every PDF (recursively), its page-1 title line, and a text preview so subjects can be identified. PDFs with no text layer (scanned images) are flagged.
2. **Decide** — group files into subjects from the report's titles/previews (topic area, course name, etc.). Name each `NN-Descriptive-Name.pdf`: zero-padded number in lecture order (Day/Notes markers if present, else file order), descriptive topic from the content.
3. **Plan** — write `plan.json` mapping source filename to target:
   ```json
   {
     "GO notes 2.pdf": "Go Programming/02-Data-Types-Conditionals-and-Loops.pdf",
     "Intro to AI.pdf":  {"subject": "Artificial Intelligence", "name": "01-Introduction-to-Artificial-Intelligence.pdf"}
   }
   ```
   Both forms are accepted (string = full target path, object = folder + filename).
4. **Apply** — run with `--apply` (always `--dry-run` first to show the moves). Folders are created, files moved+renamed. Files whose target equals current path are skipped. Existing files are never overwritten — a collision is reported and skipped.
5. **Verify** — print the final folder tree for the user.

## Rules

- `--dry-run` by default for `apply`; always show the plan before moving anything.
- Never delete, overwrite, or edit PDF contents — only move/rename.
- Keep the `NN-` prefix zero-padded and the original extension.
- Group only — don't merge different subjects into one folder unless content is clearly the same course.
- If several PDFs are one course's lectures, keep them together in lecture order even across week/date boundaries.

