---
name: video-pipeline-builder
description: Builds a Remotion (React) video pipeline that turns a written script into a rendered MP4. Use when the user asks to create a video from a script, generate an explainer/promo/slideshow video with Remotion, or scaffold a script-to-video project. Do NOT use for editing existing video files, screen recording, or non-Remotion tools (ffmpeg-only, After Effects).
license: MIT
metadata:
  author: anhhao
  version: "1.0.0"
---

# Video Pipeline Builder

## 1. Objective
- **Input:** a script file (Markdown/plain text, see `references/script-format.md`) and optional settings (resolution, fps, output dir).
- **Process:** parse script into `scenes.json` -> scaffold a Remotion project -> (optionally) render.
- **Deliverable:** a Remotion project at `<out_dir>` and, if requested, `<out_dir>/out/video.mp4`. Report paths in the chat reply.

## 2. Preconditions
- Need the script path and output directory. If missing, ask once.
- Requires Python >= 3.8 (stdlib only) for the scripts; Node >= 18 and npm for Remotion. Check with `node -v`.
- `npm install` and rendering need network and download Chromium. Run them with the user's awareness; they can take minutes (run in background, do not wait synchronously).

## 3. Workflow
Paths are relative to this SKILL.md; resolve to absolute before running.

1. **Parse the script** into scenes:
   ```bash
   python3 scripts/script_to_scenes.py --input "<script.md>" --output "<out_dir>/scenes.json" [--fps 30] [--width 1920] [--height 1080] [--wpm 150]
   ```
   Exit `1` = script not found, `2` = script empty/invalid. Show the user the scene count and total duration from the JSON output.
2. **Scaffold the project** (copies `assets/remotion-template/`, installs `scenes.json` into `public/`):
   ```bash
   python3 scripts/scaffold_project.py --scenes "<out_dir>/scenes.json" --output "<out_dir>" [--dry-run] [--force]
   ```
   Refuses to overwrite a non-empty directory without `--force`. Use `--dry-run` first if the directory exists.
3. **Install and preview/render** (only when the user wants it):
   ```bash
   cd "<out_dir>" && npm install
   npx remotion studio            # interactive preview (long-running; run as daemon)
   npx remotion render src/index.ts ScriptVideo out/video.mp4
   ```
4. **Customize** only if asked: edit `src/Scene.tsx` (visuals/animations) or `scenes.json` (text, colors, images, audio). Read `references/remotion-notes.md` before changing the template or when rendering fails.
5. **Verify:** confirm `scenes.json` validates against `assets/scenes.schema.json` fields, and that the render produced a non-empty MP4 if rendering was requested.

## 4. Example
Input script (`assets/example-script.md`) -> `scenes.json` with 3 scenes. Output shape: `assets/example-output.json`.

## 5. Safety
- Never overwrite an existing project without `--force` and user confirmation.
- Do not put secrets/API keys in `scenes.json`; if the user wants TTS, call the TTS service outside the project and store only the resulting audio files in `public/audio/`.
- Only reference images/audio that exist under `public/`.

## 6. Output
Script tools print JSON per `assets/output-schema.json`. Final reply: scene count, total duration, project path, commands to preview/render, and any warnings.
