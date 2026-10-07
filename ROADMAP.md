# Roadmap / Feuille de route

> **EN —** Two tracks move in parallel: **the kit** (what you clone) and **the game** (what the AI builds with it).
> This file tracks the kit. The game's own schedule lives in [`docs/design/50_PRODUCTION_PLAN.md`](docs/design/50_PRODUCTION_PLAN.md)
> and its live status in [`STUDIO_STATE.md`](STUDIO_STATE.md).
>
> **FR —** Deux chantiers avancent en parallèle : **le kit** (ce que vous clonez) et **le jeu** (ce que l'IA construit avec).
> Ce fichier suit le kit. Le calendrier du jeu est dans `docs/design/50_PRODUCTION_PLAN.md`, son état dans `STUDIO_STATE.md`.

## Now — v0.4.x · shipped
- [x] Eight agent skills, English with French summaries, replying in the user's language
- [x] Autonomy protocol: `guided` / `autonomous` / `full`, hard stops, `DECISIONS.md`, `QUESTIONS.md`
- [x] `studio.config.yaml` with `extra_instructions`; precedence user > config > defaults
- [x] Bilingual entry points: `README` (EN/FR), `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions
- [x] Complete design dossier, 22 legal drafts, data (25 recipes, 12 contracts)
- [x] Cinematic landing spec + React components, typographic → cinematic auto-switch
- [x] CI: data, privacy, licences, media approvals, Playwright, Robot Framework, builds, gitleaks, semgrep, ZAP
- [x] PDF guide generated in FR and EN

## Next — v0.5 · make the first run effortless
- [ ] `tools/doctor.py --fix`: install what is missing, one command
- [ ] A 10-minute **demo path**: a runnable slice (data → recipe simulation in pure Python) so you can see the
      temporal core behave before installing Unreal
- [ ] Verified run reports from Claude Code, Gemini CLI and Codex, published in `docs/runs/`
- [ ] Spanish and German guide translations (community)
- [ ] `legal/en/` completed for all player-facing documents

## Later — v0.6+ · prove the pipeline end to end
- [ ] P0 reference implementation of `TemporalCore` committed as a public C++ sample (no Epic content)
- [ ] Golden-test corpus for determinism across platforms
- [ ] Gauntlet load-test harness published with reproducible numbers
- [ ] First approved in-engine renders → landing switches to cinematic mode in public
- [ ] Reusable fork of the skills for **any** game (`docs/guides/en/05_CUSTOMISE.md` §4 generalised)

## Not planned
- Shipping Epic/Fab/MetaHuman assets in this repository (licences forbid it)
- AI-generated art presented as the game
- Any telemetry, analytics or account requirement in the kit

## How to influence this list
Open a [run report](https://github.com/aksilsmd/300-years-later/issues/new?template=run_report.yml) — real friction
beats speculation. Feature ideas go to Discussions or an issue; out-of-scope proposals are recorded in
[`docs/backlog.md`](docs/backlog.md) and decided by the maintainer.
