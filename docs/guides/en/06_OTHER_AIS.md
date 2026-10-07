# Using the kit with other AIs

🇫🇷 [Version française](../06_AUTRES_IA.md)

| Tool | How |
|---|---|
| **Claude Code** | native: skills in `.claude/skills/`, rules in `CLAUDE.md`, permissions and plugins in `.claude/settings.json`, Epic's official Unreal plugin |
| Gemini CLI | reads `GEMINI.md`, which imports `AGENTS.md` |
| GitHub Copilot | reads `.github/copilot-instructions.md`, which points to `AGENTS.md` |
| Kimi, Codex, Aider, Cursor, Windsurf, others | read `AGENTS.md` (otherwise send "Read AGENTS.md" as the first message), which points to the skills as Markdown procedures |
| Agent without access to the Unreal editor | command-line editor Python: `UnrealEditor-Cmd.exe <project> -run=pythonscript -script=game/Scripts/<script>.py` and builds via `Build.bat` |

**Universal prompt:**
> Read AGENTS.md, then apply the game-studio skill. Work autonomously from A to Z following studio.config.yaml; only come to me at hard stops, batching your questions with your recommendation. Reply in English.
> *(optional)* Extra instructions: …

Whatever the tool: replicate the `deny` and `ask` rules of `.claude/settings.json` in its permission settings, and run `tools/privacy_scan.py` before every commit.

If the tool has no `frontend-design` skill, the landing strictly follows `docs/design/34_LANDING_CINEMATIQUE.md` and `30_ART_BIBLE.md`. If the tool does not support plugins, Epic's plugin is installed from Claude Code or replaced by editor Python.
