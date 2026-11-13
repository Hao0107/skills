#!/usr/bin/env python3
"""Validate a skill directory: frontmatter, name/folder match, placeholders, referenced files.

Usage: python3 validate_skill.py <skill_dir>
Exit 0 = valid, 1 = problems found (listed on stderr).
"""
import re
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: validate_skill.py <skill_dir>", file=sys.stderr)
        sys.exit(2)
    root = Path(sys.argv[1]).resolve()
    skill = root / "SKILL.md"
    errors = []

    if not skill.is_file():
        print(f"[ERROR] {skill} not found", file=sys.stderr)
        sys.exit(1)
    text = skill.read_text(encoding="utf-8")

    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("Missing YAML frontmatter")
        fm = ""
    else:
        fm = m.group(1)

    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name:
        errors.append("Frontmatter: missing 'name'")
    else:
        n = name.group(1).strip()
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", n):
            errors.append(f"name '{n}' must be kebab-case")
        if n != root.name:
            errors.append(f"name '{n}' != folder '{root.name}'")
    if not desc:
        errors.append("Frontmatter: missing 'description'")
    else:
        d = desc.group(1).strip()
        if len(d) > 1024:
            errors.append(f"description too long ({len(d)} > 1024)")
        if re.search(r"<trigger \d>|<easily confused case>|<other-skill>", d) and root.name != "skill-template":
            errors.append("description still contains template placeholders")

    if root.name != "skill-template" and re.search(r"<placeholder>|^# Skill Title\s*$|<trigger \d>|<easily confused case>", text, re.M):
        errors.append("SKILL.md still contains template placeholder text")

    for ref in set(re.findall(r"`((?:scripts|references|assets)/[^`\s]+)`", text)):
        if not (root / ref).exists():
            errors.append(f"Referenced file missing: {ref}")

    if errors:
        for e in errors:
            print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
