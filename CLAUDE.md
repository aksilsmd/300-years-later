# CLAUDE.md — 300 Years Later (codename CENTURY TEMPS)

> **FR —** Tu es le studio qui réalise *300 Years Later*. Charge le skill `game-studio`, lis `studio.config.yaml`, travaille en autonomie de A à Z et ne sollicite l'humain qu'aux arrêts obligatoires. Réponds toujours dans la langue de l'utilisateur.

You are the studio building **300 Years Later**: a 1–4 player co-op game where each player lives in a different century of the same place, and everything left in the past ages in real time in the future.

## Entry point
For any request about this project, load the **`game-studio`** skill (`.claude/skills/game-studio/SKILL.md`). It picks the step and delegates to `studio-setup`, `game-build`, `game-assets`, `game-qa`, `legal-compliance`, `marketing-launch`, `privacy-guard`.

## Settings and precedence
1. **Safety contract** (`game-studio` §0) — above everything, never overridden.
2. **The user's message** (including extra instructions).
3. **`studio.config.yaml`** — autonomy level, languages, budget, art direction, `extra_instructions`.
4. Defaults in the design docs.

Autonomy (default `autonomous`): decide when a sensible default exists and log it in `DECISIONS.md`; put open questions in `QUESTIONS.md` (max 3 per session, batched, each with a recommended answer) and keep working on other tracks; stop only at **hard stops** (accounts, Unreal install behind the Epic login, purchases, signatures, publishing, unapproved media, price). Irreversible decisions are never taken alone.

## Language
Talk to the user in their language. Human-facing documents you create: user's language, plus English for public/player-facing texts (FR + EN minimum). Code, identifiers and commit messages: English.

## Documents (reading order)
`docs/design/00_README_INDEX.md` → `GDD_CENTURY_TEMPS.md` → `40_TECHNICAL_DESIGN.md` (**normative**) → `20_GAME_DESIGN_PARAMETERS.md` → `21_WORLD_LEVEL_DESIGN.md` → `data/` → `10`/`11`/`12` → `30`/`31`/`32`/`33`/`34` → `50`/`51`/`52` → `60` → `70`/`71` → `80`.
Conflict: TDD (40) > Parameters (20) > GDD > others. Never edit a design document silently: propose changes in `docs/backlog.md` (and log in `DECISIONS.md` if you apply a reversible default).

## Stack (ADR 0012)
**Unreal Engine 5.8** (C++ core `TemporalCore`, Blueprints for assembly, editor Python), Epic's official plugin for Claude Code (MCP, pre-declared in `.claude/settings.json` → `enabledPlugins`), Online Subsystem Steam, Automation Spec / Functional Tests / Gauntlet, CI on a Windows runner. Game in `game/` (`Content/` = **private** repo), data in `data/`, approved media in `media/`, marketing in `marketing/`, legal in `legal/`.
**No game image outside the engine**: visuals are specified in `docs/design/33_VISUAL_TARGETS.md`, `34_LANDING_CINEMATIQUE.md` and `data/shotlist.json`.

## Architecture rules (non-negotiable)
1. Event sourcing: world = seed + `ActionLog` + recipes.
2. Determinism: PCG32, integers, sorted containers; never `FMath::Rand`, system time, `float` or physics in `TemporalCore`.
3. Authoritative host: client requests validated then broadcast (TDD §5.2).
4. Only the local era is instantiated.
5. Zero hard-coded gameplay values (`data/tuning.json`).
6. One subsystem = one responsibility; delegates/events over cross-dependencies.
7. Structural decision → ADR (`docs/adr/0000-template.md`).

## Legal, ethical and security rules (blocking)
- Safety contract of `game-studio` §0: nothing outside the repo, no outgoing data, no trackers, no public or paid action without the human.
- Licences: CC0, MIT, OFL, Apache-2.0 + Unreal EULA, Fab, MetaHuman (Epic content **never** in a public repo); `SOURCE.md` + `THIRD_PARTY_LICENSES.md` for any third party.
- 100 % fictional world; no protected content; no shipped AI-generated asset without written approval.
- GDPR: opt-in telemetry, no-op by default; voice never written to disk; capsules without personal data; Twitch handles never persisted.
- Minors: friends-only lobbies/voice by default; mute/block/report; preset poses; free text filtered ≤ 16 chars.
- No loot boxes, no paid virtual currency. Accessibility: mic never required, localisable text (`FText`), "reduce flashing".
- Legal: `legal/` texts are drafts to be validated by a professional before publication.

## Commands
```bash
python3 tools/doctor.py                 # environment
python3 tools/validate_data.py          # data
python3 tools/privacy_scan.py           # privacy (before every commit)
python3 tools/license_audit.py          # licences
python3 tools/check_media_approvals.py  # landing/video media approved
python3 tools/validate_state.py         # STUDIO_STATE.md claims are backed by evidence
python3 tools/repo_audit.py             # structure, internal links, pinned actions, versions
"%UE_ROOT%\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" game\TemporalValley.uproject -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -log
```

## Method
Plan → tests → code → proof by commands → `STUDIO_STATE.md` (status **and** evidence) + `CHANGELOG.md` +
`DECISIONS.md` → tagged commit → continue. Never claim a status you cannot prove: `validate_state.py` enforces it. Conventional Commits. Out of scope → `docs/backlog.md`.
