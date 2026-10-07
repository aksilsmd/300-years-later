# A to Z guide

🇫🇷 [Version française](../01_GUIDE_A_Z.md)

This guide describes the full journey, from the cloned repository to the game in Early Access, as driven by the `game-studio` skill. For each step: **who** does what, **what you check**, and the **indicative duration** ("small studio" scenario in [03_TIME_AND_COST.md](03_TIME_AND_COST.md)).

![Journey A → Z](../../diagrams/01_parcours_a_z.svg)

## Roles
- **AI**: Claude Code (or another agent) applying the skills, in `autonomous` mode by default (`studio.config.yaml`).
- **You**: the project owner, who decides, buys, approves and publishes.
- **Pro**: an external professional (lawyer, artist, composer…).

## A. Diagnosis — 1 hour
**AI** runs `tools/doctor.py`, checks the hardware, reads `STUDIO_STATE.md`.
**You** read the report. If the PC is not powerful enough, the AI can still advance the design, the landing page and the legal pack.

## B. Setup — 1 to 3 days (long downloads)
**AI** shows the installation plan (`install_windows.ps1 -Plan`), then runs it after one global consent (no question in `full` mode). Epic's plugin and `frontend-design` are already declared in `.claude/settings.json`.
**You** create the Epic account, install Unreal Engine 5.8 from the Epic Games Launcher, accept the plugin install in Claude Code, enable the MCP server in the editor. Details: [02_INSTALLATION.md](02_INSTALLATION.md).
**Check**: `doctor.py` all green; the AI lists the actors of the open map through MCP.

## C. Customisation — 1 day
**AI** reads `studio.config.yaml`; **you** only step in if the file is empty or to change the public title, languages, platforms ([05_CUSTOMISE.md](05_CUSTOMISE.md)). **Pro** (or you): trademark clearance (`legal/21_marque-pi.md`).
**Check**: `STUDIO_STATE.md` up to date.

## D. Foundations (P0) — 2-3 weeks
**AI** creates the Unreal C++ project (`game/`), the `TemporalCore` and `TemporalValley` modules, Windows CI, architecture decision records (ADR).
**You** create the **private** repository for binary content (`game/Content/`), and install a GitHub Windows runner if you want the game CI.
**Check**: green build, green automated tests.

## E. Fun prototype (P1) — 4-8 weeks · **Gate G1**
**AI** codes the temporal core (tests first) then a playable prototype: planting a seed in year 0 grows a tree in year 300. It runs bot playtests, self-reviews against the design pillars, then queues a human playtest in `QUESTIONS.md` (non-blocking in autonomous mode).
**You** run that playtest with 5 people (kit provided: `legal/14_playtest-consentement.md`, grid in `docs/design/51`).
**Decision**: if nobody laughs or is surprised within 10 minutes, iterate; two failures = pivot.

## F. Multiplayer (P2) — 6-10 weeks · Gate G2
**AI**: Steam sessions (test AppID), 4 players, 4 eras, ghosts, integrity check.
**You**: a 4-player test session with friends.
**Check**: Gauntlet test "4 identical hashes".

## G. Game loop (P3) — 8-12 weeks · **Gate G3**
**AI**: rounds, coffee break, rotation, contracts, paradoxes, hazards, HUD.
**You**: playtest with 8 people; trademark filing; Steam page (Steam Direct); capsule commission.
**Check**: "I'd play again" score ≥ 4/5.

## H. Realistic world and content (P4) — 6-12 months
**AI** prepares the asset **shopping list** (Fab, MetaHuman) with licences and costs, and starts with free Epic content so work never waits.
**You** buy and add the assets; commission the creatures from an artist; approve the art direction.
**AI** builds the landscape, eras, procedural vegetation, ageing prefabs, and measures performance.
**Check**: 10 playable world seeds; performance budgets met on the 3 profiles.

## I. Clip machine (P5) — 6-10 weeks
End-of-match museum, shareable capsules, solo mode, tutorial, photo mode.

## J. Voice, streamer, saboteur (P6) — 6-8 weeks · Gate G4 (alpha)
**AI**: cross-era voice, anti-harassment tools, streamer mode (off by default).
**Check**: "no audio on disk" test, 3 streamers in closed test.

## K. Compliance (P7) — 8-12 weeks · **Gate G5 (beta)**
**AI** updates the `legal/` pack from the real game (FR + EN) and prepares the lawyer's packet.
**Pro**: legal review. **You**: integrate the corrections.
**AI** + **you**: full accessibility, localisation, pseudo-localisation.

## L. Demo and Steam (P8) — 8-12 weeks · Gate G6
Demo build, achievements, leaderboards, Cloud, profiling, Shipping build. Steam content survey (including the AI section).

## M. Media — continuous from G3
**AI** renders the shots of `data/shotlist.json` **inside Unreal** (Movie Render Graph) and edits the trailers (Sequencer + Remotion).
**You** approve each file in `media/APPROVALS.md`. Nothing unapproved is published.

## N. Landing page — 1-2 weeks, then updates
**AI** builds the **cinematic** landing (`docs/design/34_LANDING_CINEMATIQUE.md`): animated typographic mode while no render is approved, then an automatic switch to the video hero and the scroll-driven 4-era sequence once shots L00–L04 are approved; it runs the tests (Robot Framework, Lighthouse, k6, OWASP ZAP).
**You** approve the copy and trigger publication (manual `pages.yml` workflow).

## O. Launch — 4-8 weeks
Steam Next Fest, creator programme (`legal/12_politique-createurs.md`), communication. **You** publish; the AI prepares.

## Z. After launch
Fixes within 72 h for severe issues, regular updates, seasons (`docs/design/71_LIVE_OPS.md`).

---
**During hard stops**, the AI prepares everything (click list, files) and keeps independent tracks moving (landing, legal, data, Remotion).

**Reminder:** the AI never buys, publishes, signs, or chooses the name or price on its own. See [04_SECURITY_AND_PRIVACY.md](04_SECURITY_AND_PRIVACY.md).
