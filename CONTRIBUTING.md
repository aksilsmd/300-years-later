# Contributing / Contribuer

**EN —** Thanks for being here. **FR —** Merci d'être là. Répondez dans la langue que vous préférez : les deux sont lues.

## The most useful contribution
A **[run report](https://github.com/aksilsmd/300-years-later/issues/new?template=01-run-report.yml)**: which agent you
used, how far it got, exactly where it stopped. Real friction from a real machine beats any amount of speculation,
and it is what shapes [the roadmap](ROADMAP.md).

## Good first contributions
| Difficulty | Task | Where |
|---|---|---|
| 🟢 easy | A new ageing recipe (object + era → what it becomes) | `data/recipes/*.json`, schema in `data/schemas/` |
| 🟢 easy | A Chronicle phrase, FR + EN, that makes someone laugh | `data/phrases/chronicle_fr_en.json` |
| 🟢 easy | Fix or clarify a guide; translate one into your language | `docs/guides/` and `docs/guides/en/` |
| 🟡 medium | A new game contract (objective scored out of 5 stars) | `data/contracts/*.json` |
| 🟡 medium | A landing-page test or accessibility fix | `tests/`, `marketing/landing*/` |
| 🔴 involved | A skill improvement, proven on a real run | `.claude/skills/*/SKILL.md` |

## Rules
1. These must pass before you open a PR:
   ```bash
   python3 tools/validate_data.py && python3 tools/privacy_scan.py \
     && python3 tools/license_audit.py && python3 tools/check_media_approvals.py
   ```
2. **No personal data** — yours or anyone's — in code, docs, commits or screenshots. Set up your local deny-list
   first: [security guide](docs/guides/en/04_SECURITY_AND_PRIVACY.md) §3.
3. **No protected content**: no existing character, brand, music, or non-free font. No game image produced
   outside Unreal Engine; no AI-generated asset without declaring it in the PR.
4. Design documents (`docs/design/`) are not edited in a PR. Propose the change in
   [`docs/backlog.md`](docs/backlog.md) — see [`GOVERNANCE.md`](GOVERNANCE.md).
5. [Conventional Commits](https://www.conventionalcommits.org): `feat:`, `fix:`, `docs:`, `chore:`…
6. Be decent: [code of conduct](CODE_OF_CONDUCT.md).

## Workflow
```bash
git clone https://github.com/aksilsmd/300-years-later.git && cd 300-years-later
git config core.hooksPath .githooks     # runs the privacy scan before each commit
git switch -c feat/my-recipe
# …change, run the checks above…
git commit -m "feat(data): add the rusting-anvil recipe"
```
Fork → branch → PR with the template → review → merge. One subject per PR; a small PR gets merged, a huge one waits.

## Reviewing an AI-written PR
State which agent wrote it and what you verified yourself. Anything generated and unverified is marked as such
in the PR description — honesty about provenance is part of this project's point.
