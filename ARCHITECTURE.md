# Architecture

> **EN —** The map of this repository: what lives where, which rules hold everywhere, and where a change belongs.
> Written for the contributor — human or agent — who knows *what* to change but not *where*.
> **FR —** La carte du dépôt : ce qui vit où, les règles qui tiennent partout, et où une modification doit aller.
>
> Following [matklad's convention](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html): coarse-grained,
> stable, revisited a few times a year. It names files and modules instead of linking to lines, because line
> links go stale and a stale map is worse than none.

## Bird's-eye view

This repository is **not a game**. It is the machine that builds one: a complete game design, a legal corpus,
and eight skills that let an autonomous coding agent run the studio — install the toolchain, write the Unreal
Engine code, test it, keep it compliant, render the media, build the landing page — stopping only where a human
is legally or financially required to act.

Two artefacts come out of it. **The kit** (what you clone) is documentation, data and tooling, and it is
complete today. **The game** (`game/`, created in phase P0) does not exist yet. Everything here is organised
around keeping that distinction honest: the kit's gates exist to stop an agent claiming the game is further
along than it is.

Read [`docs/design/00_README_INDEX.md`](docs/design/00_README_INDEX.md) for the design dossier,
[`AGENTS.md`](AGENTS.md) for the contract an agent follows, this file for where things are.

## Entry points

| You are… | Start at |
|---|---|
| a human meeting the project | [`README.md`](README.md) → [`docs/guides/en/00_QUICK_START.md`](docs/guides/en/00_QUICK_START.md) |
| an agent asked to run the studio | [`AGENTS.md`](AGENTS.md) → `.claude/skills/game-studio/SKILL.md` |
| wondering what is actually done | [`STUDIO_STATE.md`](STUDIO_STATE.md) — status **and** evidence per system |
| about to change something | this file, then [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| checking the project is sane | `python3 tools/repo_audit.py` and the other gates in `tools/` |

## Codemap

### `.claude/skills/` — the product
Eight `SKILL.md` procedures, one directory each, conforming to the Agent Skills specification. `game-studio` is
the director: it owns the A→Z pipeline, the autonomy protocol and the safety contract, and delegates to the
seven others. The rest never call each other; they are called.

**Architecture Invariant:** a skill is a procedure, never a fact store. Facts live in `docs/design/` and
`data/`; a skill that starts restating parameters has become a document and must be split.

**Architecture Invariant:** the safety contract lives in `game-studio` §0 and is duplicated nowhere, because
duplicated rules drift. Other skills reference it; they do not restate it.

`.claude/settings.json` holds the permission lists (deny / ask / allow) and the plugins to pre-install.
`.claude-plugin/` turns the whole repository into an installable Claude Code plugin — `plugin.json` lists the
eight skills, `marketplace.json` publishes them.

### `docs/design/` — the normative dossier
Numbered documents, read in the order stated in `00_README_INDEX.md`. `40_TECHNICAL_DESIGN.md` is **normative**:
when documents disagree, it wins, then `20_GAME_DESIGN_PARAMETERS.md`, then the GDD, then the rest.

**Architecture Invariant:** agents do not edit design documents. A proposed change goes to
[`docs/backlog.md`](docs/backlog.md) and a human decides. This is what keeps the specification from drifting
under the thing that implements it.

### `docs/adr/` — decisions, with their reasons
One file per structural decision, `NNNN-kebab-title.md`, from `0000-template.md`. ADR 0012 chose Unreal Engine
5.8 and realism; ADR 0002 chose event sourcing. A decision that changes the engine, the architecture, the
licensing posture or the safety contract is written here **before** the code.

### `data/` — every number the game plays by
Ageing recipes, contracts, tuning, Chronicle phrases, and `shotlist.json` (the shots to render in Unreal).
Validated against JSON Schema by `tools/validate_data.py`.

**Architecture Invariant:** no gameplay value is hard-coded. If a number appears in code, it belongs here.

### `game/` — the Unreal project (absent until phase P0)
`Source/TemporalCore` is pure, deterministic C++: PCG32, integers, sorted containers.

**Architecture Invariant:** `TemporalCore` never calls `FMath::Rand`, never reads system time, never uses
`float`, never touches physics. The world is a seed plus an action log plus the recipes; the same inputs must
produce the same world on every machine, or the four players desynchronise.

**Architecture Invariant:** `game/Content/` — every `.uasset`, `.umap`, `.pak` — lives in a **private**
repository. Epic's licences forbid redistributing Fab, Megascans and MetaHuman content. CI fails if one appears.

**API Boundary:** the host is authoritative. Clients send requests; the host validates and broadcasts. Nothing
a client says is trusted.

### `tools/` — the gates
Each is a single-purpose script, read-only except where it writes a build artefact, and each returns non-zero
when the repository is in a state that must not be published:

| Script | Refuses |
|---|---|
| `repo_audit.py` | missing required files, broken internal links, an action not pinned to a SHA, a floating `latest`, a GitHub About box past GitHub's own limits |
| `validate_skills.py` | a skill that breaks the Agent Skills specification or this project's bilingual rule |
| `validate_state.py` | a system claimed `implemented` or beyond without an evidence file that exists |
| `validate_data.py` | data that does not match its schema |
| `privacy_scan.py` | personal data, a secret, a tracker — using a deny-list kept **outside** the repository |
| `license_audit.py` | third-party content without a recorded licence |
| `check_media_approvals.py` | a media file used before a human approved it |
| `doctor.py` | nothing — it reports the environment (`--strict` makes optional tools fatal) |
| `build_guide_pdf.py` | — builds the FR and EN PDF guides from real captures |
| `render_brand_assets.py` | — renders `docs/assets/*.png` from `design-system/tokens.json`; `--check` refuses an image that no longer matches the tokens or the title |
| `build_book_pdf.py` | — typesets `book/<lang>/*.md` as a 148×210 mm PDF: cover, front matter, folios |
| `build_book_reader.py` | — builds the self-contained web reader; fails if the page gains a remote reference |
| `apply_public_title.py` | — renames the public title across git-tracked files, never the repository slug, the codename or the licence attribution entity |
| `setup_repo.sh`, `publish.sh` | — the human-only GitHub operations, driven by `.github/about.yml` |

**Architecture Invariant:** a gate never phones home, never reads outside the repository, and never writes
outside it. `privacy_scan.py` reads the deny-list from `~/.config/300yl/denylist.txt` precisely so that the
user's name and email are never committed to prove that they are not committed.

### `legal/` — 22 drafts
Terms, privacy, DPIA, DSA, minors, accessibility, creators, contracts, AI transparency, tax. Every file carries
a "DRAFT — to be validated by a legal professional" header, and `legal/README.md` is the obligations matrix.

**Architecture Invariant:** a legal draft is never presented as validated, and the human's personal contact
details never appear in it — a dedicated project address is used instead.

### `marketing/` — two landings, one video project
`landing-react/` is production; `landing/` is the dependency-free reference that the tests and the PDF guides
use. `video/` is Remotion. See [`marketing/README.md`](marketing/README.md) for the rule that stops the two
landings diverging.

**Architecture Invariant:** no game image is produced outside Unreal Engine, and no media is published before a
human approves it in `media/APPROVALS.md`. The landing ships in typographic mode until renders exist; filling
`marketing/landing-react/src/media.ts` is the single switch that turns on cinematic mode.

**Architecture Invariant:** zero trackers, cookies, external CDNs or third-party fonts — on either landing.

### `tests/` — what runs in CI
Playwright (`web/`), Robot Framework (`robot/`), k6 (`load/`), and `skills/` for the trigger corpus.

## Cross-cutting concerns

**Precedence.** The safety contract beats everything. Then the user's message. Then `studio.config.yaml`. Then
the defaults in the design documents. An agent that finds a conflict says so rather than silently picking.

**Autonomy and hard stops.** `guided` / `autonomous` (default) / `full` change how often an agent asks, never
*what it may do*. Creating accounts, installing Unreal behind the Epic login, buying, signing, publishing,
approving media and setting the price are hard stops at **every** level. An agent prepares them and continues
on another track; it does not perform them.

**Evidence over assertion.** `STUDIO_STATE.md` is the only place that says where the project stands, and every
claim beyond `planned` names a file that proves it. This is the structural answer to an agent that reports
success it did not achieve.

**Traceability.** need → `docs/backlog.md` · decision → `docs/adr/` or `DECISIONS.md` · specification →
`docs/design/` · implementation → `game/` or `tools/` · proof → `docs/qa/` and `STUDIO_STATE.md` evidence
paths · release → `CHANGELOG.md`.

**Bilingualism.** Everything a human reads exists in French and English: `README.md`/`README.fr.md`,
`docs/guides/` and `docs/guides/en/`, the legal pack, the skills (English body, `FR —` summary, answering in
the user's language). Code, identifiers, commit messages and file names stay English.

**Determinism as a product requirement.** It is not an implementation detail: four players in four centuries
share one world computed from a seed. Determinism is what makes that possible, which is why it is an invariant
rather than a guideline.

## What this file is not

It is not a changelog, not a tutorial, and not a per-module reference. It does not track the code closely — it
is revisited a few times a year, and when it disagrees with the code, the code is probably right and this file
is stale. Fix it then.
