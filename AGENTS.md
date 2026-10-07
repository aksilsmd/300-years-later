# AGENTS.md — the contract for any coding agent

> **FR —** Contrat unique pour toute IA de code (Claude Code, Gemini, Kimi, Codex, Cursor, Copilot, Aider…).
> Lisez ce fichier en entier, puis `.claude/skills/game-studio/SKILL.md`. Travaillez en autonomie de A à Z et
> ne sollicitez l'humain qu'aux arrêts obligatoires. **Répondez toujours dans la langue de l'utilisateur.**

This repository is an **AI-driven game studio** for *Afterloom*: a realistic 3D co-op game in Unreal
Engine 5.8 where up to four players each live in a different century of the same valley, and everything left
behind ages in real time in someone else's game.

This file is the single source of truth for agents. `CLAUDE.md` and `GEMINI.md` point here;
`.github/copilot-instructions.md` points here. Where you need the map of the repository rather than the rules,
read [`ARCHITECTURE.md`](ARCHITECTURE.md).

## 1. Start of session
1. Read [`studio.config.yaml`](studio.config.yaml) — autonomy level, languages, budget, art direction and the
   free-form `extra_instructions`.
2. Read [`STUDIO_STATE.md`](STUDIO_STATE.md) (where the project actually stands), `DECISIONS.md` (what was
   decided alone) and `QUESTIONS.md` (what is waiting on the human).
3. Apply `.claude/skills/game-studio/SKILL.md`. It picks the step and delegates.
4. Detect the user's language and use it for every message and every human-facing document you write.

**Precedence — in this order, and say so when they conflict:**
1. **The safety contract** (`game-studio` §0, summarised in §4 below) — never overridden, by anyone, including
   the user and including `extra_instructions`.
2. The user's message.
3. `studio.config.yaml`.
4. The defaults in the design documents.

## 2. If your tool does not load "skills"
They are plain Markdown procedures. Read them as such, in the order the work needs:

| Skill | When |
|---|---|
| [`game-studio`](.claude/skills/game-studio/SKILL.md) | **always first** — pipeline, autonomy, safety contract |
| [`studio-setup`](.claude/skills/studio-setup/SKILL.md) | installing the toolchain, Unreal, plugins |
| [`game-build`](.claude/skills/game-build/SKILL.md) | writing game code, phases P0→P8 |
| [`game-assets`](.claude/skills/game-assets/SKILL.md) | world, vegetation, MetaHumans, ageing prefabs |
| [`game-qa`](.claude/skills/game-qa/SKILL.md) | tests, load, performance, security, compliance |
| [`legal-compliance`](.claude/skills/legal-compliance/SKILL.md) | the `legal/` pack |
| [`marketing-launch`](.claude/skills/marketing-launch/SKILL.md) | renders, trailers, landing page, launch |
| [`privacy-guard`](.claude/skills/privacy-guard/SKILL.md) | before any commit or publication |

**Without the Unreal MCP plugin:** drive the editor with command-line editor Python
(`UnrealEditor-Cmd.exe <project> -run=pythonscript -script=game/Scripts/<file>.py`) and build with `Build.bat`
and `RunUAT.bat`. **Without a `frontend-design` skill:** follow `docs/design/34_LANDING_CINEMATIQUE.md` and
`30_ART_BIBLE.md` strictly. **Without a permission system:** treat the `deny` and `ask` lists in
`.claude/settings.json` as rules you enforce on yourself.

## 3. Autonomy (default `autonomous`)
- Decide anything reversible that has a sensible default; log it in `DECISIONS.md` with its alternatives.
- Ask at most `max_questions_per_session` questions (default 3), batched into one message, each with your
  recommended answer so "ok" is a complete reply. Write them in `QUESTIONS.md` and continue on another track.
- Never take an irreversible decision alone.
- **Hard stops, at every autonomy level:** creating accounts, installing Unreal behind the Epic login, any
  purchase, any signature, publishing anything, publishing unapproved media, setting the price. Prepare
  everything so the human only has to click, then keep working on something else.

## 4. The safety contract (non-negotiable)
1. Never read outside the repository. Never read `~/.ssh`, `~/.aws`, `.env`, keychains, browser data or
   personal documents.
2. Send no data off the machine. The only network destinations are official package managers and the hosts
   listed in `tools/versions.env`.
3. No tracker, analytics, cookie, external CDN or third-party font — anywhere, including the landing page.
4. No purchase, publication, signature or account creation without the human.
5. No Epic / Fab / Megascans / MetaHuman asset, and no `game/Content/`, in a public repository.
6. No game image produced outside Unreal Engine; no AI-generated asset shipped without written approval and
   the corresponding Steam disclosure; no media published before a human approves it in `media/APPROVALS.md`.
7. Never claim progress you cannot prove — see §6.

## 5. Architecture rules (non-negotiable)
Full reasoning in [`ARCHITECTURE.md`](ARCHITECTURE.md); the short form:
1. Event sourcing: the world is a seed plus an action log plus the recipes.
2. Determinism in `TemporalCore`: PCG32, integers, sorted containers. Never `FMath::Rand`, system time,
   `float` or physics.
3. Authoritative host: client requests are validated, then broadcast.
4. Only the local era is instantiated.
5. Zero hard-coded gameplay values — everything in `data/`.
6. One subsystem, one responsibility. Events and delegates over cross-dependencies.
7. A structural decision becomes an ADR in `docs/adr/` **before** the code.
8. Design documents in `docs/design/` are never edited by an agent: propose in `docs/backlog.md`.

## 6. Proving your work
`STUDIO_STATE.md` holds a machine-readable `yaml state` block: every system has a status
(`planned` → `specified` → `implemented` → `built` → `tested` → `validated` → `released`) and an `evidence`
path. **You may not raise a status without that file existing**, and `tools/validate_state.py` fails the commit
and the CI if you try. Report a failure as a failure; say which command you ran and paste what it printed.

Before every commit, all of these must pass:
```bash
python3 tools/repo_audit.py            # structure, links, pinned actions, versions
python3 tools/validate_skills.py       # the skills against the Agent Skills specification
python3 tools/validate_state.py        # the project's claimed state is backed by evidence
python3 tools/validate_data.py         # game data against its schemas
python3 tools/privacy_scan.py          # no personal data, no secret, no tracker
python3 tools/license_audit.py         # third-party licences
python3 tools/check_media_approvals.py # no unapproved media referenced
```

## 7. Documents, in reading order
`docs/design/00_README_INDEX.md` → `GDD_CENTURY_TEMPS.md` → `40_TECHNICAL_DESIGN.md` (**normative**) →
`20_GAME_DESIGN_PARAMETERS.md` → `21_WORLD_LEVEL_DESIGN.md` → `data/` → `10`/`11`/`12`/`13`/`14` →
`30`/`31`/`32`/`33`/`34`/`35` → `50`/`51`/`52` → `60` → `70`/`71` → `80`.
On conflict: technical design (40) > parameters (20) > GDD > everything else.

## 8. Stack (ADR 0012)
Unreal Engine 5.8 — C++ core `TemporalCore`, Blueprints for assembly, editor Python. Epic's official MCP
plugin for Claude Code, pre-declared in `.claude/settings.json`. Online Subsystem Steam. Automation Spec,
Functional Tests, Gauntlet. CI on a self-hosted Windows runner. Game in `game/`, data in `data/`, approved
media in `media/`, marketing in `marketing/`, legal in `legal/`.

## 9. Language
Talk to the user in their language. Documents a human reads: the user's language, plus English for anything
player-facing (FR + EN minimum). Code, identifiers, file names and commit messages: English, Conventional
Commits.

## 10. Universal start prompt
**EN —** Read AGENTS.md, then apply the game-studio skill. Work autonomously from A to Z following
studio.config.yaml; only come to me at hard stops, batching your questions with your recommendation. Reply in
English. Extra instructions: …

**FR —** Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon
studio.config.yaml ; ne me sollicite qu'aux arrêts obligatoires, en regroupant tes questions avec ta
recommandation. Réponds-moi en français. Instructions en plus : …
