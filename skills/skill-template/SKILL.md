---
name: skill-template
description: One-sentence summary of what the skill does. Use when the user asks to <trigger 1>, <trigger 2>, or mentions <keyword>. Do NOT use for <easily confused case>; use <other-skill> instead.
license: MIT
metadata:
  author: anhhao
  version: "1.1.0"
---

# Skill Title

## 1. Objective
- **Input:** what the user provides (file path, directory, parameters).
- **Process:** one line describing the core job.
- **Deliverable:** what is returned (chat summary, file in workspace, or artifact) and where it is written.

## 2. Preconditions
- Verify the target path exists. If a required parameter is missing, ask the user once and stop.
- Requires Python >= 3.8, standard library only. If Python is unavailable, do the checks manually using the rules in `references/guidelines.md`.

## 3. Workflow
Paths below are relative to this SKILL.md; resolve them to absolute paths before running.

1. **Run the script** (non-interactive, JSON on stdout, errors on stderr):
   ```bash
   python3 scripts/run_task.py --input "<target_path>" [--option <value>] [--dry-run]
   ```
   Use `--dry-run` first for anything that could modify files.
2. **Handle exit codes:**
   - `0` success: parse the JSON.
   - `1` input not found: re-check the path, ask the user.
   - `2` processing failed: report stderr, do not retry blindly.
3. **Load rules only if needed:** read `references/guidelines.md` when the script reports `FAIL`/`WARNING` or the task needs domain rules. Skip it otherwise.
4. **Format output** following `assets/output-schema.json` (example: `assets/example-output.json`).
5. **Verify:** confirm every result item has a status and that suggested actions are concrete before replying.

## 4. Example
Input: `Check ./src`
Output: see `assets/example-output.json`.

## 5. Safety
- Never delete or overwrite user files without confirmation.
- Write generated files only to the declared output directory.

## 6. Authoring this template
Copy the folder, rename it (kebab-case, must equal `name`), replace every `<placeholder>`, then run:
```bash
python3 scripts/validate_skill.py <new_skill_dir>
```
