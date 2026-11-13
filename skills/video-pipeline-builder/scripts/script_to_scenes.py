#!/usr/bin/env python3
"""Parse a script (Markdown/plain text) into scenes.json for the Remotion template.

Exit codes: 1 = input not found, 2 = script empty/invalid.
Stdout: JSON summary (see assets/output-schema.json).
"""
import argparse
import json
import re
import sys
from pathlib import Path

SKILL_NAME = "video-pipeline-builder"
DIRECTIVE = re.compile(r"^@(\w+):\s*(.+)$")
HEADING = re.compile(r"^#{1,6}\s+(.+)$")
DEFAULT_BG = ["#0f172a", "#1e293b", "#312e81", "#134e4a", "#7c2d12"]
MIN_SECONDS = 2.0


def split_blocks(text: str) -> list:
    text = text.replace("\r\n", "\n").strip()
    if re.search(r"^---\s*$", text, re.M):
        parts = re.split(r"^---\s*$", text, flags=re.M)
    else:
        parts = re.split(r"\n\s*\n", text)
    return [p.strip() for p in parts if p.strip()]


def parse_scene(block: str, index: int, fps: int, wpm: int, warnings: list) -> dict:
    title, directives, body = "", {}, []
    for line in block.splitlines():
        line = line.strip()
        if not line:
            continue
        m = DIRECTIVE.match(line)
        h = HEADING.match(line)
        if m:
            directives[m.group(1).lower()] = m.group(2).strip()
        elif h and not title and not body:
            title = h.group(1).strip()
        else:
            body.append(line)
    text = " ".join(body)

    seconds = None
    if "duration" in directives:
        try:
            seconds = float(directives["duration"])
        except ValueError:
            warnings.append(f"scene {index}: invalid @duration '{directives['duration']}', using estimate")
    if seconds is None:
        words = len((title + " " + text).split())
        seconds = max(MIN_SECONDS, words / wpm * 60 + 1.0)

    return {
        "id": f"scene-{index}",
        "title": title,
        "text": text,
        "durationInFrames": max(1, round(seconds * fps)),
        "background": directives.get("bg", DEFAULT_BG[(index - 1) % len(DEFAULT_BG)]),
        "image": directives.get("image", ""),
        "audio": directives.get("audio", ""),
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Convert a script into scenes.json.")
    p.add_argument("--input", "-i", required=True)
    p.add_argument("--output", "-o", required=True)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--width", type=int, default=1920)
    p.add_argument("--height", type=int, default=1080)
    p.add_argument("--wpm", type=int, default=150, help="Narration words per minute for duration estimates.")
    p.add_argument("--dry-run", action="store_true", help="Do not write the output file.")
    a = p.parse_args()

    src = Path(a.input)
    if not src.is_file():
        print(f"[ERROR] Script not found: '{src}'", file=sys.stderr)
        sys.exit(1)
    if a.fps < 1 or a.wpm < 1 or a.width < 1 or a.height < 1:
        print("[ERROR] fps, wpm, width, height must be positive", file=sys.stderr)
        sys.exit(2)

    blocks = split_blocks(src.read_text(encoding="utf-8"))
    if not blocks:
        print("[ERROR] Script is empty", file=sys.stderr)
        sys.exit(2)

    warnings = []
    scenes = [parse_scene(b, i, a.fps, a.wpm, warnings) for i, b in enumerate(blocks, 1)]
    for s in scenes:
        if not s["title"] and not s["text"]:
            warnings.append(f"{s['id']} has no title or text")

    data = {"fps": a.fps, "width": a.width, "height": a.height, "scenes": scenes}
    created = []
    if not a.dry_run:
        out = Path(a.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        created.append(str(out))

    total = sum(s["durationInFrames"] for s in scenes)
    print(json.dumps({
        "skill_name": SKILL_NAME,
        "execution_status": "WARNING" if warnings else "PASS",
        "summary": f"{len(scenes)} scenes, {total / a.fps:.1f}s total.",
        "input_target": str(src),
        "results": [{"item_id": s["id"], "status": "PASS",
                     "message": f"{s['durationInFrames'] / a.fps:.1f}s", "suggested_action": ""} for s in scenes]
                   + [{"item_id": "warning", "status": "FAIL", "message": w, "suggested_action": "Fix the script"} for w in warnings],
        "artifacts_created": created,
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
