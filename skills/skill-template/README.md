# skill-template

Starter for Antigravity Agent Skills (also works with Claude Code).

```
skill-template/
├── SKILL.md                    # trigger metadata + short workflow (loaded when skill activates)
├── scripts/
│   ├── run_task.py             # deterministic helper: argparse, --dry-run, JSON stdout, exit codes
│   └── validate_skill.py       # checks frontmatter, name == folder, placeholders, referenced files
├── references/guidelines.md    # detailed rules, loaded on demand
└── assets/
    ├── output-schema.json      # JSON Schema of the result
    └── example-output.json     # sample conforming output
```

## Create a new skill
1. `cp -r skills/skill-template skills/my-skill`
2. Set `name: my-skill` (must equal the folder name), write an English `description` (<= 1024 chars: what it does, when to use, when not to).
3. Replace placeholders, rules, and script logic.
4. `python3 skills/skill-template/scripts/validate_skill.py skills/my-skill`

## Authoring tips
- The `description` is the only text the agent sees before activation; make triggers explicit.
- Keep SKILL.md short; put detail in `references/` and tell the agent *when* to read it.
- Scripts must be non-interactive and print JSON to stdout, errors to stderr.
