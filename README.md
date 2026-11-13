# skills

Repository for Agent Skills (Antigravity CLI, Claude Code).

## Layout
- `skills/skill-template/` - canonical starter; copy it to create a new skill and validate with `scripts/validate_skill.py`.
- `skills/video-pipeline-builder/` - script-to-video pipeline using Remotion.

## Working on Remotion template code
`skills/video-pipeline-builder/assets/remotion-template/` has no `node_modules`, so editors show red errors
(`Cannot find module 'remotion'`). This is expected. Don't `npm install` inside the repo; use a scratch copy:

```bash
python3 skills/video-pipeline-builder/scripts/scaffold_project.py -s <scenes.json> -o /tmp/demo
cd /tmp/demo && npm install && npm run typecheck
```

Open `/tmp/demo` in your editor (not the repo root), then copy edits back into the template.
`node_modules/` and `out/` are git-ignored.
