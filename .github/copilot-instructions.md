# Copilot instructions

Read and follow **[AGENTS.md](../AGENTS.md)** and **[CLAUDE.md](../CLAUDE.md)**. Entry point: `.claude/skills/game-studio/SKILL.md`. Settings: `studio.config.yaml`.
Key rules: Unreal Engine 5.8; deterministic `TemporalCore` (no `FMath::Rand`, no `float`, no system time); zero hard-coded gameplay values (`data/tuning.json`); no trackers; no game image outside the engine; no Epic/Fab/MetaHuman asset in a public repo; run `python3 tools/privacy_scan.py && python3 tools/validate_data.py` before committing.
FR — Lisez AGENTS.md et CLAUDE.md ; répondez dans la langue de l'utilisateur.
