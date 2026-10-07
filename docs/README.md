# Documentation

🇬🇧 English · 🇫🇷 Les guides existent dans les deux langues ; le dossier de conception est en français.

## Start here
| I want to… | Read |
|---|---|
| Run the kit in 10 minutes | [Quick start](guides/en/00_QUICK_START.md) · [Démarrage rapide](guides/00_DEMARRAGE_RAPIDE.md) |
| See the whole journey, step by step | [A→Z guide](guides/en/01_A_TO_Z.md) · [Guide A→Z](guides/01_GUIDE_A_Z.md) |
| Set up the workstation | [Installation](guides/en/02_INSTALLATION.md) · [Installation](guides/02_INSTALLATION.md) |
| Know the time and the budget | [Time and cost](guides/en/03_TIME_AND_COST.md) · [Temps et coûts](guides/03_TEMPS_ET_COUTS.md) |
| Check what the AI can and cannot do | [Security and privacy](guides/en/04_SECURITY_AND_PRIVACY.md) · [Sécurité](guides/04_SECURITE_ET_CONFIDENTIALITE.md) |
| Change the game, or make it mine | [Customise](guides/en/05_CUSTOMISE.md) · [Personnaliser](guides/05_PERSONNALISER.md) |
| Use Gemini, Codex, Kimi, Copilot… | [Other AIs](guides/en/06_OTHER_AIS.md) · [Autres IA](guides/06_AUTRES_IA.md) |
| Fix something | [FAQ](guides/en/07_FAQ_TROUBLESHOOTING.md) · [FAQ](guides/07_FAQ_DEPANNAGE.md) |
| Read it offline | [PDF guides](guide/) — `python3 tools/build_guide_pdf.py --lang all` |

## The game design dossier (`design/`)
Read in this order; in a conflict, the technical design wins (see [`CLAUDE.md`](../CLAUDE.md)).

| # | Document | What it settles |
|---|---|---|
| 00 | [Index](design/00_README_INDEX.md) | gates, reading order, vocabulary |
| 01 | [Market audit](design/01_AUDIT_V1.md) | why this game, against what |
| — | [GDD](design/GDD_CENTURY_TEMPS.md) | the game as a whole |
| 10–12 | [Narrative bible](design/10_NARRATIVE_BIBLE.md) · [Scripts](design/11_SCRIPTS_DIALOGUES.md) · [Scenarios](design/12_SCENARIOS.md) | story, voice, situations |
| 20–21 | [Parameters](design/20_GAME_DESIGN_PARAMETERS.md) · [World](design/21_WORLD_LEVEL_DESIGN.md) | numbers, the valley, landmarks |
| 30–34 | [Art bible](design/30_ART_BIBLE.md) · [Audio](design/31_AUDIO_DESIGN.md) · [UX/UI](design/32_UX_UI_SPEC.md) · [Visual targets](design/33_VISUAL_TARGETS.md) · [Cinematic landing](design/34_LANDING_CINEMATIQUE.md) | how it looks, sounds and reads |
| 40 | [Technical design](design/40_TECHNICAL_DESIGN.md) | **normative**: determinism, networking, data |
| 50–52 | [Production plan](design/50_PRODUCTION_PLAN.md) · [QA plan](design/51_QA_TEST_PLAN.md) · [Risks](design/52_RISK_REGISTER.md) | how it gets built and verified |
| 60 | [Legal and compliance](design/60_LEGAL_COMPLIANCE.md) | obligations matrix |
| 70–71 | [Marketing](design/70_MARKETING_GTM.md) · [Live ops](design/71_LIVE_OPS.md) | launch and after |
| 80 | [Agent playbook](design/80_CLAUDE_CODE_PLAYBOOK.md) | the prompts, phase by phase |

## Decisions and diagrams
- [`adr/`](adr/) — architecture decision records. Start with [ADR 0012](adr/0012-unreal-engine-5-realiste.md) (Unreal Engine 5.8 and realism) and [ADR 0002](adr/0002-event-sourcing.md) (event sourcing).
- [`diagrams/`](diagrams/) — the journey, skill orchestration, the temporal model, data flow, the security model.
- [`backlog.md`](backlog.md) — proposals waiting for a human decision.

## Elsewhere in the repository
[`../legal/`](../legal/) legal drafts · [`../data/`](../data/) recipes, contracts, tuning, shot list ·
[`../.claude/skills/`](../.claude/skills/) the eight skills · [`../ROADMAP.md`](../ROADMAP.md) what comes next.
