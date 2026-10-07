# AGENTS.md — instructions for any coding AI / instructions pour toute IA de code

> **FR —** Ce dépôt est un studio de jeu vidéo piloté par IA. Lisez ce fichier, puis `.claude/skills/game-studio/SKILL.md`, puis `studio.config.yaml`, et travaillez en autonomie de A à Z. Répondez dans la langue de l'utilisateur. Le résumé français de chaque skill figure en tête de fichier (« FR — »).

This repository is an **AI-driven game studio** for a **realistic 3D co-op game in Unreal Engine 5.8**. It works natively with Claude Code (skills in `.claude/skills/`, plugins in `.claude/settings.json`) and with any other agent (Gemini CLI, Kimi, Codex, Cursor, Copilot, Aider, Windsurf…) that reads this file.

## 1. Start
1. Read `studio.config.yaml` (autonomy, languages, defaults, `extra_instructions`), then the user's message. **User message > config > defaults. Safety contract > everything.**
2. Read `STUDIO_STATE.md`, `DECISIONS.md`, `QUESTIONS.md`.
3. Apply `.claude/skills/game-studio/SKILL.md` (A→Z pipeline, autonomy protocol, safety contract §0).

## 2. If your tool does not load "skills"
Skills are plain Markdown procedures. Read them in this order when the step needs them:
1. `.claude/skills/game-studio/SKILL.md` — **entry point**
2. `.claude/skills/studio-setup/SKILL.md` — tools, plugins, Unreal
3. `.claude/skills/game-build/SKILL.md` — game code by phases
4. `.claude/skills/game-assets/SKILL.md` — world, assets, MetaHumans, sound
5. `.claude/skills/game-qa/SKILL.md` — tests, load, security, compliance
6. `.claude/skills/legal-compliance/SKILL.md` — GDPR, licences, Steam, legal pack
7. `.claude/skills/marketing-launch/SKILL.md` — renders, trailer, cinematic landing, launch
8. `.claude/skills/privacy-guard/SKILL.md` — before any commit or publication

Then apply `CLAUDE.md` (valid for every agent).

**Without the Unreal MCP plugin:** drive the editor with editor Python (`UnrealEditor-Cmd.exe <project> -run=pythonscript -script=game/Scripts/<file>.py`) and build from the command line (`Build.bat`, `RunUAT.bat`). **Without the frontend-design skill:** follow `docs/design/34_LANDING_CINEMATIQUE.md` and `30_ART_BIBLE.md` strictly. **Without a permission system:** treat the `deny` and `ask` lists in `.claude/settings.json` as rules you must respect yourself.

## 3. Autonomy (default `autonomous`)
- Decide when a sensible default exists; log it in `DECISIONS.md`.
- Ask at most 3 questions per session, batched, each with your recommended answer; write them in `QUESTIONS.md` and continue on another track.
- Stop only at **hard stops**: creating accounts, installing Unreal behind the Epic login, purchases, signatures, publishing, publishing unapproved media, choosing the price. Prepare everything so the human only clicks.
- Never take an irreversible decision alone.

## 4. Absolute rules (summary)
- Read no file outside the repository; no secrets; no data sent off the machine.
- No tracker, cookie or external CDN.
- No game image produced outside the engine; no AI-generated image presented as the game; no Epic/Fab/MetaHuman asset in a public repo.
- `python3 tools/privacy_scan.py && python3 tools/validate_data.py` before every commit.

## 5. Universal start prompt / Prompt de démarrage universel
**EN**
> Read AGENTS.md, then apply the game-studio skill. Work autonomously from A to Z following studio.config.yaml; only come to me at hard stops, batching your questions with your recommendation. Reply in English. Extra instructions: …

**FR**
> Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon studio.config.yaml ; ne me sollicite qu'aux arrêts obligatoires, en regroupant tes questions avec ta recommandation. Réponds-moi en français. Instructions en plus : …
