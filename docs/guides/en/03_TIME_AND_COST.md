# Time, cost and consumption

🇫🇷 [Version française](../03_TEMPS_ET_COUTS.md)

> Order-of-magnitude estimates as of 7 October 2026, for a **realistic 3D** co-op game in Unreal Engine 5.8 as described in `docs/design/`. They are for deciding, not promising. Measure your real figures at each gate and adjust.

## 1. Three scenarios
| | A — Solo + AI | B — Small studio | C — Small team |
|---|---|---|---|
| Team | project owner (part-time) + Claude Code + occasional freelancers | full-time owner + 2-3 regular freelancers (3D art, animation, sound) | 5-8 people (gameplay programmer, tech artist, 2 artists, animator, producer/QA) + AI |
| Time to Early Access | 30-48 months | 18-30 months | 15-24 months |
| Budget excluding owner's pay | **≈ €40,000 – 80,000** | **≈ €150,000 – 300,000** | **≈ €500,000 – 1.2M** |
| Achievable visual level | realistic thanks to purchased assets, mostly library animations | consistent realism, custom creatures and NPCs | polished realism, performance capture, richer content |
| Main risk | duration and scope | cash flow | monthly fixed cost |

## 2. Cost items (ranges)
| Item | Scenario A | Scenario C | Notes |
|---|---|---|---|
| Workstation (if needed) | €2,000 – 3,500 | €2,500 × people | RTX 4070+ GPU, 64 GB advised |
| Unreal Engine | €0 | €0 | 5 % above $1M lifetime gross revenue (Epic Games Store sales exempt) |
| Fab / Megascans assets | €1,000 – 6,000 | €8,000 – 30,000 | Megascans paid since 2025 |
| Creatures (sculpt, groom, rig) | €3,000 – 10,000 | €15,000 – 40,000 | Bouloche, goats, Chronomites |
| Facial / body capture | €0 – 3,000 | €15,000 – 60,000 | MetaHuman Animator (video) vs mocap studio |
| Music (6 tracks + stingers) | €3,000 – 8,000 | €10,000 – 30,000 | rights assignment included |
| Additional sound design | €1,000 – 4,000 | €8,000 – 25,000 | |
| Steam capsule, logo, illustrations | €1,500 – 4,000 | €5,000 – 15,000 | |
| Trailer editing and grading | €1,000 – 3,000 | €5,000 – 20,000 | |
| Localisation (≈ 15,000 words × 7 languages) | €8,000 – 16,000 | €12,000 – 25,000 | professional per-word rates; native review |
| Legal (terms, privacy, contracts, DPIA) | €2,000 – 6,000 | €8,000 – 20,000 | |
| Trademark (EU, 1-3 classes) | €850 – 1,500 | €2,000 – 5,000 | + international if needed |
| Accountant, professional liability insurance | €1,500 – 3,500/yr | €4,000 – 10,000/yr | |
| Steam Direct | ≈ $100 | ≈ $100 | per game |
| Playtests and external QA | €500 – 3,000 | €10,000 – 40,000 | |
| Marketing (events, PR, ads) | €2,000 – 10,000 | €30,000 – 150,000 | |
| AI assistant subscription | depends on plan | plan × people | see plans on support.claude.com |
| Team salaries | — | €400,000 – 900,000 | main item of scenario C |

Possible support in France: video game tax credit (strict conditions), CNC video game fund, Bpifrance, regional grants (`legal/20_fiscalite-redevances.md`). Elsewhere, check your national and regional schemes.

## 3. Calendar by phase (scenario B)
| Phase | Duration | Gate | What happens |
|---|---|---|---|
| A-C Diagnosis, setup, customisation | 1-2 weeks | — | workstation ready, title chosen |
| P0 Foundations | 2-3 weeks | — | Unreal project, CI, ADRs |
| P1 Fun prototype | 4-8 weeks | **G1** | playable seed → tree, 5 testers |
| P2 Multiplayer | 6-10 weeks | G2 | 4 players online without desync |
| P3 Game loop | 8-12 weeks | **G3** | full match, Steam page, first clips |
| P4 Realistic world and content | 6-12 months | — | the longest: assets, PCG, prefabs, MetaHumans |
| P5 Clip machine | 6-10 weeks | — | museum, capsules, solo |
| P6 Voice, streamer, saboteur | 6-8 weeks | G4 | alpha |
| P7 Compliance, accessibility, localisation | 8-12 weeks | **G5** | beta, legal review |
| P8 Demo and Early Access | 8-12 weeks | G6 | demo, Next Fest, launch |

## 4. AI consumption (order of magnitude)
- **Agent time**: a code phase typically takes 20 to 80 Claude Code work sessions, from 30 minutes to a few hours each; P4 is the hungriest (many editor operations via MCP).
- **Tokens**: highly variable with project size, caching and the number of editor operations. Expect several million tokens per intensive working day. Measure your real consumption (your tool's cost/usage command) from P0 and record it in `STUDIO_STATE.md` to extrapolate.
- **Savings**: one phase per session, plan mode first, small PRs, targeted tests, avoid re-reading the whole repository each session (`game-studio` reads `STUDIO_STATE.md` first).
- **Incompressible human time**: PR reviews (≈ 20-30 % of agent time, lower in autonomous mode), playtests, asset purchases, art direction, media and copy approval, gate decisions.

## 5. What blows up estimates
Scope (adding an era, a biome, a mode), the quality of realistic humans, motion capture, late localisation, and no early playtests. The cut rule of `docs/design/50_PRODUCTION_PLAN.md` §6 applies before any budget extension.
