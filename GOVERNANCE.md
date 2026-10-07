# Governance / Gouvernance

**EN —** How decisions are made here. **FR —** Comment les décisions sont prises ici.

## Roles
| Role | Who | Can |
|---|---|---|
| Maintainer | the repository owner | merge, release, decide design changes, arbitrate the backlog |
| Contributor | anyone with a merged PR | propose, review, discuss |
| The AI | the agent running the kit | implement, test, document; it never merges, publishes or decides anything irreversible |

## How a change gets in
1. **Discussion or issue** — state the problem before the solution.
2. **Pull request** — one subject per PR, Conventional Commits, the checks in [`CONTRIBUTING.md`](CONTRIBUTING.md) green.
3. **Review by the maintainer** — a design document is never modified in a PR; propose it in
   [`docs/backlog.md`](docs/backlog.md) and the maintainer decides.
4. **Merge and changelog** — every user-visible change is recorded in [`CHANGELOG.md`](CHANGELOG.md).

## Structural decisions
Anything that changes the engine, the architecture, the licensing posture or the safety contract needs an
**ADR** in [`docs/adr/`](docs/adr/) (template: `0000-template.md`), written before the code.
Precedent: [ADR 0012](docs/adr/0012-unreal-engine-5-realiste.md) chose Unreal Engine 5.8 and realism.

## What is not negotiable
The safety contract of the `game-studio` skill: nothing read outside the repository, no data sent out, no
trackers, no purchase, publication or signature without a human, no licensed Epic content in a public repo,
no game image produced outside the engine. A PR that weakens any of these is closed, whatever it improves.

## Releases
Semantic versioning. `main` stays green. A release is tagged `vMAJOR.MINOR.PATCH` with the changelog section
as its notes. Breaking changes to the skills' interface (file names, config keys) bump the minor version at
minimum and are documented in the upgrade notes.

## Succession
If the maintainer becomes inactive for six months, any contributor with three merged PRs may fork and announce
the fork in an issue. Code is MIT and content CC BY 4.0 precisely so the work survives its maintainer.
