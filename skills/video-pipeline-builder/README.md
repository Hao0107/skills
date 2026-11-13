# video-pipeline-builder

Agent skill: script -> `scenes.json` -> Remotion project -> MP4.

```bash
python3 scripts/script_to_scenes.py -i assets/example-script.md -o /tmp/demo/scenes.json
python3 scripts/scaffold_project.py -s /tmp/demo/scenes.json -o /tmp/demo
cd /tmp/demo && npm install && npm run render
```

See [SKILL.md](SKILL.md) for the agent workflow and `references/` for the script format and Remotion notes.
