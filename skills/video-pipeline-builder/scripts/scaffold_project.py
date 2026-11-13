#!/usr/bin/env python3
"""Copy the Remotion template into an output dir and install scenes.json.

Exit codes: 1 = scenes file not found, 2 = target not empty (use --force) or invalid scenes.
Stdout: JSON summary (see assets/output-schema.json).
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

SKILL_NAME = "video-pipeline-builder"
TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "remotion-template"
SKIP = {"node_modules", "out", ".git"}


def main() -> None:
    p = argparse.ArgumentParser(description="Scaffold a Remotion project from scenes.json.")
    p.add_argument("--scenes", "-s", required=True)
    p.add_argument("--output", "-o", required=True)
    p.add_argument("--force", action="store_true", help="Allow writing into a non-empty directory.")
    p.add_argument("--dry-run", action="store_true", help="List files without writing.")
    a = p.parse_args()

    scenes_path, out = Path(a.scenes), Path(a.output)
    if not scenes_path.is_file():
        print(f"[ERROR] scenes file not found: '{scenes_path}'", file=sys.stderr)
        sys.exit(1)
    try:
        data = json.loads(scenes_path.read_text(encoding="utf-8"))
        assert data["scenes"] and data["fps"] > 0 and data["width"] > 0 and data["height"] > 0
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] invalid scenes.json: {exc!r}", file=sys.stderr)
        sys.exit(2)
    if out.exists() and any(out.iterdir()) and not a.force:
        # scenes.json alone in out dir (from step 1) is fine
        others = [c for c in out.iterdir() if c.resolve() != scenes_path.resolve()]
        if others:
            print(f"[ERROR] '{out}' is not empty; pass --force to overwrite", file=sys.stderr)
            sys.exit(2)

    files = [f for f in TEMPLATE.rglob("*") if f.is_file() and not (set(f.relative_to(TEMPLATE).parts) & SKIP)]
    created = []
    for f in files:
        dest = out / f.relative_to(TEMPLATE)
        created.append(str(dest))
        if not a.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)
    public_scenes = out / "public" / "scenes.json"
    created.append(str(public_scenes))
    if not a.dry_run:
        public_scenes.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(scenes_path, public_scenes)
        (out / "public" / "audio").mkdir(exist_ok=True)

    warnings = []
    for s in data["scenes"]:
        for key in ("image", "audio"):
            if s.get(key) and not (out / "public" / s[key]).exists():
                warnings.append(f"{s.get('id')}: {key} '{s[key]}' not found in public/ yet")

    print(json.dumps({
        "skill_name": SKILL_NAME,
        "execution_status": "WARNING" if warnings else "PASS",
        "summary": f"{'Would create' if a.dry_run else 'Created'} {len(created)} files in {out}.",
        "input_target": str(scenes_path),
        "results": [{"item_id": "scaffold", "status": "PASS", "message": f"{len(files)} template files", "suggested_action": f"cd {out} && npm install"}]
                   + [{"item_id": "asset", "status": "FAIL", "message": w, "suggested_action": "Add the file under public/"} for w in warnings],
        "artifacts_created": [] if a.dry_run else created,
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
