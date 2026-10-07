---
name: game-build
description: Develops "300 Years Later" in Unreal Engine 5.8 (C++, Blueprints, editor Python, driven through Epic's official MCP plugin) phase by phase (P0 → P8), tests first, following the normative technical design docs/design/40 and data/tuning.json. Use for any game development task in game/ ("code", "implement", "phase", "développe", "code la phase").
---

# Skill: game-build

> **FR —** Développe le jeu dans Unreal Engine 5.8, phase par phase, tests d'abord. Répond dans la langue de l'utilisateur.

## Before coding
1. Read `CLAUDE.md`, `docs/design/40_TECHNICAL_DESIGN.md`, `docs/adr/0012-*`, `docs/design/20_GAME_DESIGN_PARAMETERS.md`, then the phase prompt in `docs/design/80_CLAUDE_CODE_PLAYBOOK.md` §4.
2. `python3 tools/doctor.py`: Unreal 5.8, dotnet, git-lfs required; editor open with the MCP server for editor work.
3. Plan: files touched, tests written first, acceptance criteria, risks. In `autonomous` mode, do not wait for approval of the plan — log it in `DECISIONS.md` and proceed.
4. Commit before each batch of MCP actions.

## Tool split
| Need | Tool |
|---|---|
| Deterministic temporal core | pure C++ in `Source/TemporalCore` + Automation Spec |
| Gameplay, networking, UI | C++ in `Source/TemporalValley` + thin Blueprints |
| Actors, PCG, materials, Niagara, Sequencer | Epic MCP toolsets or editor Python (`game/Scripts/`) |
| Game data | `data/` (validated JSON) — no hard-coded values |

## Phases and required evidence
| Phase | Evidence |
|---|---|
| P0 | Development Editor build OK; empty Automation Specs green with `-nullrhi`; Windows CI green; ADR 0013-0020 |
| P1 | TemporalCore specs + golden test green; 30 s capture seed → tree (internal, not for publication) |
| P2 | Gauntlet 1+3 clients: identical hashes after 200 actions; out-of-range rejection test |
| P3 | one test per edge case (`docs/design/12` §4); full bot match |
| P4 | `validate_data.py`; 10 seeds without PCG failure; Insights report on 3 profiles |
| P5 | capsule round-trip test; "no personal data" test |
| P6 | static + runtime "no audio on disk" test |
| P7 | `legal-compliance` and `game-qa` reports green |
| P8 | BuildCookRun Shipping; G6 report |

## Reference commands (Windows)
```bat
"%UE_ROOT%\Engine\Build\BatchFiles\Build.bat" TemporalValleyEditor Win64 Development -Project="%CD%\game\TemporalValley.uproject"
"%UE_ROOT%\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" "%CD%\game\TemporalValley.uproject" -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -nosplash -log
"%UE_ROOT%\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project="%CD%\game\TemporalValley.uproject" -platform=Win64 -clientconfig=Shipping -build -cook -stage -pak -archive -archivedirectory="%CD%\build"
```

## Unreal-specific rules
- `Content/` lives in the **private** repo; check `git status` before every commit of the public repo.
- No Fab/Megascans/MetaHuman asset added unless acquired by the human and recorded in `THIRD_PARTY_LICENSES.md`. Until then use free Epic content or blockout.
- No `FMath::Rand`, `FPlatformTime` or `float` in `TemporalCore` (review + test).
- Player-facing strings via `FText` / string tables (FR + EN at minimum).

## End of phase
Evidence in `docs/qa/phase-N.md`; `STUDIO_STATE.md`, `CHANGELOG.md`, `DECISIONS.md` updated; tag `phase-N`; queue the human playtest in `QUESTIONS.md` (non-blocking in autonomous mode) and continue.
