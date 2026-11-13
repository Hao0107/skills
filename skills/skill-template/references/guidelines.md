# Guidelines & Domain Rules

Loaded on demand (only when the script reports FAIL/WARNING or domain rules are needed). Keep this file focused; split large topics into separate files.

## 1. Evaluation criteria
- **Rule A: file size**
  - PASS: every source file is <= 500 lines.
  - FAIL: any file exceeds 500 lines. Suggest splitting it.
- **Rule B: naming**
  - PASS: files use kebab-case or snake_case consistently.
  - FAIL: mixed styles in one directory.

(Replace these example rules with your own.)

## 2. Edge cases
- Empty input: return `execution_status: "PASS"` with an empty `results` list and say so in `summary`.
- Conflicting configs: prefer the project's existing config over defaults.

## 3. Conventions
- Generated files go in a clearly named output directory; never overwrite existing files without confirmation.
