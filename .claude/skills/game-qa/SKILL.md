---
name: game-qa
description: Studio-grade quality assurance for the Unreal Engine 5.8 game and its landing page — Automation Spec, Functional Tests, Gauntlet (multi-client and load), Unreal Insights (performance), network fuzzing, security (gitleaks, semgrep, OWASP ZAP), compliance (GDPR, licences, accessibility, Steam, DSA, minors), visual review, Robot Framework E2E, k6, Lighthouse and go/no-go reports. Use at each phase end, before a gate, or for "test", "audit", "security", "load", "teste", "charge", "sécurité".
---

# Skill: game-qa

> **FR —** Assurance qualité de niveau studio : tests, charge, performance, sécurité, conformité, rapports go/no-go. Répond dans la langue de l'utilisateur.

Reference: `docs/design/51_QA_TEST_PLAN.md`. This skill says **how to run**.

## 1. Pyramid and commands
| Level | Command / tool | Threshold |
|---|---|---|
| Core unit | `UnrealEditor-Cmd.exe <project> -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -log` | 100 % green, golden OK |
| Functional | `-ExecCmds="Automation RunTests Project.Functional;Quit"` | 100 % green |
| Multi-client | `RunUAT.bat RunUnreal -test=TemporalValley.NetDeterminism -clients=3` | 0 desync; p95 confirm < 400 ms at 250 ms lag (`-NetEmulation.PktLag=250 -NetEmulation.PktLoss=2`) |
| **Load** | Gauntlet `TemporalValley.LoadTest`: 8 sessions × 4 bots, 10 min | host < 4 ms logic tick, < 30 kB/s/player, 0 crash |
| **RPC fuzzing** | `TemporalValley.RpcFuzz` (10,000 malformed requests) | 0 crash, rejects counted, kick at 20/min |
| **Performance** | Unreal Insights + `csvprofile`, stress scene, 3 profiles (TDD §10) | TDD §10 and art bible §4 budgets |
| Memory | `memreport -full` at start and after 2 h | leak < 200 MB |
| Repo security | `gitleaks detect --no-banner --redact` · `semgrep --config p/default --error` · `python3 tools/privacy_scan.py` | 0 leak, 0 high |
| Licences / data | `python3 tools/license_audit.py && python3 tools/validate_data.py` + no Epic/Fab/MetaHuman asset in public repo | green |
| Visual review | shots from `data/shotlist.json` vs criteria in `33_VISUAL_TARGETS.md`; human approval | 100 % of published media approved |
| Landing E2E | `robot --outputdir results tests/robot` · `python3 -m pytest tests/web` | 100 % green |
| Landing load | `k6 run -e BASE_URL=<url> tests/load/landing_smoke.js` | p95 < 500 ms, errors < 1 % |
| Web perf / a11y | Lighthouse | ≥ 90 / 95 / 95 / 90 (cinematic mode: LCP < 2.5 s on 4G) |
| Web security | OWASP ZAP baseline (`security.yml`) | 0 high |

## 2. Executable compliance
GDPR (telemetry no-op without consent, no audio in `Saved/`, capsules without personal data, consent screen with equal buttons) · minors/DSA (friends-only default, mute/block/report ≤ 2 actions, filtered free text) · accessibility (each option of `32_UX_UI_SPEC.md` §6 tested; playable without mic, sound, in colour-blind and reduced-flashing modes; no flash > 3 Hz) · no paid currency in build · Steam (achievements, Cloud, overlay, Deck text ≥ 9 px) · localisation (pseudo-loc +30 %, no hard-coded strings, identical placeholders).

## 3. Playtests
In autonomous mode: run bot playtests and a self-review against the design pillars, then prepare the human kit (build, `legal/14_playtest-consentement.md`, grid, survey) and queue it in `QUESTIONS.md`. You never recruit people or collect data yourself.

## 4. Go/no-go report
`docs/qa/<gate>.md`: scope, results per campaign, S1-S4 defects, measurements, compliance, residual risks, recommendation. **Never GO** with an open S1, a data leak, an exposed licensed asset or a high security alert.
