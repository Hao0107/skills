# Remotion notes (read when customizing or debugging)

## Architecture of the template
- `public/scenes.json` is fetched in `calculateMetadata` (Root.tsx), which sets total duration, fps, size, and props. Changing `scenes.json` needs no code edits.
- `Video.tsx` chains scenes with `<Series>`; `Scene.tsx` renders one scene (fade in/out, title, text, optional image/audio).

## Commands
- Preview: `npx remotion studio src/index.ts` (long-running; run as daemon).
- Render: `npx remotion render src/index.ts ScriptVideo out/video.mp4`.
- Still frame check: `npx remotion still src/index.ts ScriptVideo out/frame.png --frame=30`.
- Typecheck: `npm run typecheck`.

## Troubleshooting
- **Version mismatch error**: all `remotion` and `@remotion/*` packages must be the exact same version. Run `npx remotion versions` and pin them.
- **Chromium download fails / render hangs**: needs network on first run; on Linux ensure shared libs (e.g. `libnss3`, `libatk1.0-0`, `libgbm1`).
- **Missing asset**: files must be under `public/` and referenced with `staticFile()`, never absolute paths.
- **Audio longer than scene**: raise `@duration` or `durationInFrames` for that scene.
- **Slow renders**: lower `--concurrency`, use `--scale 0.5` for drafts.
- Use `useCurrentFrame()`/`interpolate()` for animation; do not use CSS transitions or `setTimeout` (they are not frame-deterministic).

## Extending
- New visual style: add a component and choose it per scene via a new optional field (e.g. `layout`) in `scenes.json`; update `types.ts` and `assets/scenes.schema.json`.
- Subtitles/word timing: add a `words` array per scene and highlight by frame.
