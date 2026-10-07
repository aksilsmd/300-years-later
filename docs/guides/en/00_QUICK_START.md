# Quick start (10 minutes)

🇫🇷 [Version française](../00_DEMARRAGE_RAPIDE.md)

## What you get
An **AI-driven game studio**: the complete design of a realistic 3D co-op game (*Afterloom*), a legal pack, a cinematic landing page, tests, and above all **skills** that let Claude Code (or another AI) build the game in Unreal Engine 5.8 autonomously from A to Z, only coming to you for the decisions that are yours.

## What you need
- A Windows 10/11 PC with a recent GPU (RTX 3070/4070 or better), 32 GB RAM, 300 GB free — details in [02_INSTALLATION.md](02_INSTALLATION.md).
- Claude Code (or another coding agent) and an Epic Games account.
- Realistic time and budget: read [03_TIME_AND_COST.md](03_TIME_AND_COST.md) before you start.

## One message to your AI
```bash
git clone <THIS-REPO-URL> 300-years-later && cd 300-years-later
claude        # or gemini, kimi, codex, cursor, aider…
```
Then paste:
> Read AGENTS.md, then apply the game-studio skill. Work autonomously from A to Z following studio.config.yaml; only come to me at hard stops, batching your questions with your recommendation. Reply in English.
> *(optional)* Extra instructions: …

Prefer to stay in control? Set `autonomy.level: guided` in `studio.config.yaml` (the AI asks before each step). Want it to install tools without asking too? `full`.

## Configure the AI once: `studio.config.yaml`
| Key | Effect |
|---|---|
| `autonomy.level` | `guided` · `autonomous` (default) · `full` |
| `autonomy.max_questions_per_session` | maximum questions per session (default 3) |
| `project.languages` | game and public-text languages (default fr, en) |
| `defaults.*` | team scenario, monthly asset budget, art direction, landing mode… |
| `extra_instructions` | your free-form instructions, applied every session |

Your message always overrides this file.

## Then
The AI moves forward on its own and keeps three files up to date: `STUDIO_STATE.md` (where we are), `DECISIONS.md` (what it decided alone, reversible), `QUESTIONS.md` (what it needs from you, with its recommendation — reply "ok" to accept). Hard stops (accounts, Unreal installation, purchases, publishing…) are described in the [A to Z guide](01_A_TO_Z.md).
