## What and why / Quoi et pourquoi
Closes #
Design reference / Référence design : docs/…

## Checks / Contrôles
- [ ] `python3 tools/validate_data.py` green
- [ ] `python3 tools/privacy_scan.py` green — **no personal data**, no secret, no tracker
- [ ] `python3 tools/license_audit.py` green
- [ ] `python3 tools/check_media_approvals.py` green — no unapproved media referenced
- [ ] No `game/Content/` file and no Epic/Fab/MetaHuman asset in this public repository
- [ ] Tests added or updated and passing (Automation Spec / Functional Tests / Gauntlet, or `tests/`)
- [ ] No hard-coded gameplay value (everything in `data/`)
- [ ] Determinism respected (no `FMath::Rand`, system time or `float` in `TemporalCore`)
- [ ] Player-facing strings localisable (`FText`, string tables) with FR + EN keys
- [ ] No personal data collected, stored or logged
- [ ] `CHANGELOG.md` and, if structural, an ADR in `docs/adr/` updated
- [ ] Design documents untouched (propose changes in `docs/backlog.md` instead)

## How to test / Comment tester
1.

## Provenance
- [ ] Written by a human
- [ ] Written by an AI — which one, and what I verified myself:

## Risks / Risques
