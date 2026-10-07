# Studio state / État du studio

> **EN —** The single source of truth for *where the project actually stands*. The block below is machine-readable
> and enforced by `python3 tools/validate_state.py` (run in CI): **a system cannot be declared `implemented` or
> beyond without an `evidence` file that exists in the repository.** An agent may not claim progress it cannot prove.
>
> **FR —** Source de vérité unique de l'**état réel** du projet. Le bloc ci-dessous est lisible par une machine et
> vérifié par `python3 tools/validate_state.py` (lancé en CI) : **aucun système ne peut être déclaré `implemented`
> ou au-delà sans un fichier `evidence` présent dans le dépôt.** Une IA ne peut pas revendiquer ce qu'elle ne prouve pas.

## Status vocabulary / Vocabulaire des statuts
`planned` → `specified` → `implemented` → `built` → `tested` → `validated` → `released`

| Status | Means / Signifie | Evidence required / Preuve exigée |
|---|---|---|
| `planned` | decided, not described yet | — |
| `specified` | a design document defines it | the document path |
| `implemented` | code exists | — (the diff is the proof) |
| `built` | it compiles / the project builds | build log or CI run file |
| `tested` | its tests ran and passed | test report file |
| `validated` | it passed its gate (QA report, human playtest where required) | `docs/qa/<gate>.md` |
| `released` | it is in a published build | release notes |

```yaml state
project:
  phase: A                 # A diagnosis · B setup · C customisation · D..L = P0..P8 · M media · N landing · O launch
  gates_passed: [G0]
  playable: false
  build_status: not_started   # not_started | failing | passing
  updated: 2026-10-07

systems:
  temporal_core:    { status: specified, evidence: docs/design/40_TECHNICAL_DESIGN.md }
  multiplayer:      { status: specified, evidence: docs/design/40_TECHNICAL_DESIGN.md }
  game_loop:        { status: specified, evidence: docs/design/20_GAME_DESIGN_PARAMETERS.md }
  world_content:    { status: specified, evidence: docs/design/21_WORLD_LEVEL_DESIGN.md }
  ageing_recipes:   { status: specified, evidence: data/recipes }
  clip_machine:     { status: specified, evidence: docs/design/12_SCENARIOS.md }
  voice_streamer:   { status: specified, evidence: docs/design/32_UX_UI_SPEC.md }
  compliance:       { status: specified, evidence: legal/README.md }
  media_pipeline:   { status: specified, evidence: data/shotlist.json }
  landing_page:     { status: tested,    evidence: tests/web/test_landing.py }
  kit_tooling:      { status: tested,    evidence: .github/workflows/ci.yml }
```

## Human context / Contexte humain
- Public title / Titre public : 300 Years Later (working title — to confirm) · codename CENTURY TEMPS
- Engine / Moteur : Unreal Engine 5.8 (ADR 0012)
- Autonomy / Autonomie : see `studio.config.yaml` · decisions: `DECISIONS.md` · open questions: `QUESTIONS.md`
- Last session / Dernière session : 2026-10-07 — v0.4.2: evidence-backed state, supply-chain pinning, repository audit
- Waiting on the human / En attente de l'humain : public title; team scenario and budget
  (`docs/guides/en/03_TIME_AND_COST.md`); Epic and Steamworks accounts; private repository for `game/Content/`;
  GitHub description, topics and release (`bash tools/setup_repo.sh`)
- Open risks / Risques ouverts : R14 visibility, R19 realism budget, R06/R07 scope and time
  (`docs/design/52_RISK_REGISTER.md`)
- Measured time and AI usage / Temps et consommation IA mesurés : — (record from P0, see guide 03)
