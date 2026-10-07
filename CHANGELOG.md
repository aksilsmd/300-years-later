# Changelog / Journal des modifications

All notable changes to this kit are recorded here. The format follows
[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) — only the six headings *Added, Changed,
Deprecated, Removed, Fixed, Security* — and the versioning follows [Semantic Versioning](https://semver.org).
The kit is deliberately in **`0.y.z`**: the game it builds does not exist yet, so nothing here is a stable
public API. Dates are ISO 8601.

## [Unreleased]

### Added
- **La couche vivante du jeu** — nouveau document normatif
  [`docs/design/13_PEUPLES_DIEUX_ET_PHENOMENES.md`](docs/design/13_PEUPLES_DIEUX_ET_PHENOMENES.md) :
  **Peuples** qui bifurquent d'une époque à l'autre selon l'eau, les vivres, l'abri, la ferveur et la rancune
  (neuf civilisations d'arrivée possibles en l'an 900) ; **Figures** nées des objets abandonnés par les joueurs,
  avec leur domaine, leur Bienfait et leur Serment ; quatre **Porte-Voix** (Petit Moss, Dame Orielle,
  Contremaître Bouilly, Vé-7) ; **météo** dérivée du couvert forestier et de la pollution ; sept
  **catastrophes** annoncées, jamais létales, qui transforment les traces au lieu de les détruire ; cinq
  **phénomènes** dont *la Résonance* (20 s où les quatre époques se superposent) ; et la révélation qui tient
  l'arc narratif — le Synchro fonctionne à la Ferveur — avec trois fins possibles au Vernissage.
  Garde-fous en §0 : fiction intégrale, vocabulaire inventé, satire des institutions jamais des croyants,
  aucune violence de croyance, PEGI 7-12, photosensibilité.
- Données : schéma de recette **v2** (`input.with` pour les recettes croisées, `priority` explicite, `faith`),
  10 recettes croisées et événementielles (35 au total), 4 contrats (16 au total), 5 modèles de Chronique,
  et les blocs `peoples`, `faith`, `weather`, `disasters`, `phenomena` dans `data/tuning.json`.
- Scénario de référence « La Cuillère et la Sécheresse » (`12` §4bis) et tests de déterminisme,
  d'accessibilité et de sensibilité pour ces systèmes (`51`).
- **Discoverability**: `llms.txt` at the repository root and served by both landings (a compact map for
  language models, including the facts a model must not get wrong about this project); canonical, Open Graph,
  `hreflang`, `robots.txt`, `sitemap.xml` and JSON-LD `VideoGame` structured data on both landings — all
  self-hosted, still zero trackers; a section in `marketing/launch-plan.md` on how the **kit** (as opposed to
  the game) gets found.
- **Player review** of the design dossier: [`docs/reviews/2026-10-07-revue-joueur.md`](docs/reviews/2026-10-07-revue-joueur.md)
  — eight gaps ranked, one strategic contradiction, the questions the dossier leaves open and five minor
  inconsistencies. Eleven entries filed in `docs/backlog.md` for the human to decide.
- **[`ARCHITECTURE.md`](ARCHITECTURE.md)** — the repository's map in the matklad shape: bird's-eye view, entry
  points, codemap, and the invariants stated inline where they apply (determinism, authoritative host, no
  licensed content, no media outside the engine, no trackers). Named files, never line links.
- **Installable as a Claude Code plugin**: `.claude-plugin/plugin.json` + `marketplace.json`, so the eight
  skills can be added to any project with `/plugin marketplace add aksilsmd/300-years-later`.
  Verified with `claude plugin validate`.
- `tools/validate_skills.py`: the skills checked against the Agent Skills specification — closed frontmatter
  field set (so they still load on claude.ai and the Skills API), name rules and directory match, description
  length and third person, the 500-line progressive-disclosure budget, link targets, and this project's
  bilingual `FR —` rule. In CI and pre-commit.
- `tests/skills/`: a 56-query bilingual trigger corpus (should-trigger and deliberate near-misses) with
  `run_trigger_eval.sh`, so a change to a skill's description can be measured instead of guessed.
- `.editorconfig`, `.github/release.yml` (categorised release notes with no third-party action), numbered
  issue forms so the chooser order is deliberate.

### Changed
- `GDD` : encadré assumant l'écart avec l'étude de marché (photoréalisme et 19,99 € contre « ≤ 10 € et
  graphismes modestes »), sixième pilier de design, mode principal corrigé en 1-4 joueurs.
- Départage des recettes par `priority` puis identifiant alphabétique — plus jamais par l'ordre du fichier.
- **`AGENTS.md` is now the single contract** for every agent — the open standard other tools read — and
  `CLAUDE.md` is a short pointer that imports it, following the convention in ruff, next.js, rust and node.
  No more drift between two near-identical files.
- READMEs: architecture link in the nav, plugin install path, repository map replaced by a pointer to
  `ARCHITECTURE.md`, tighter command block.
- `CHANGELOG.md` conforms to Keep a Changelog 1.1.0 — the six canonical headings, an `[Unreleased]` section,
  and an explicit statement that the kit stays on `0.y.z` until there is a shippable game.

### Security
- `tools/repo_audit.py` now also refuses: untrusted `${{ github.event.* }}` interpolation inside a workflow
  step, `pull_request_target` combined with a checkout, and any workflow without a top-level `permissions:`
  block.

## [0.4.2] — 2026-10-07
### Added
- **Evidence-backed project state**: `STUDIO_STATE.md` now carries a machine-readable `yaml state` block
  (status vocabulary `planned → … → released` plus an `evidence` path per system) enforced by
  `tools/validate_state.py` in CI and pre-commit. An agent can no longer declare a system `implemented`,
  `tested` or `validated` without a file that proves it. The `game-studio` skill states the rule.
- `tools/repo_audit.py`: structural audit — required files, skills with front matter, internal links,
  every GitHub Action pinned to a commit SHA, no floating container tag, no `latest` in `tools/versions.env`,
  no licensed Unreal content. Wired into CI and the pre-commit hook.
- `.github/CODEOWNERS`; `marketing/README.md` stating which landing is production and which is the tested
  reference, and the rule that forbids them diverging silently.
### Changed
- `tools/doctor.py` separates a missing **core** tool (exit 1) from a missing optional one (reported, exit 0),
  with `--strict` for CI and release checks.
- npm dependencies declared as exact versions instead of ranges, pending committed lockfiles.
### Security
- gitleaks container pinned to `v8.30.1` instead of `latest`; `K6_VERSION` and `GITLEAKS_VERSION` pinned in
  `tools/versions.env`, and the audit fails if the workflow and the declared version drift apart.
- The semgrep gate now also fails on fatal scan errors instead of only on findings.

## [0.4.1] — 2026-10-07
### Added
- Community files in both languages: issue forms (bug, feature, run report), PR checklist, `SUPPORT.md`,
  `GOVERNANCE.md`, `ROADMAP.md`, `CITATION.cff`, `docs/runs/` for real run reports; English sections added to
  `SECURITY.md` (including private vulnerability reporting) and `CODE_OF_CONDUCT.md`.
- Repository presentation: banner (`docs/assets/banner.png`), badges, English + French READMEs rewritten,
  `docs/README.md` documentation index, `ROADMAP.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CITATION.cff`.
- `.github`: Dependabot (actions + npm), issue template chooser, structured run-report form, `.gitattributes`
  for correct language statistics.
- `tools/setup_repo.sh`: one command for the repository description, topics, features and Pages.
### Security
- Every GitHub Action pinned to a commit SHA (mutable tags can be repointed), Dependabot cooldown of 7 days,
  semgrep results published as SARIF in the Security tab with a blocking `p/ci` gate, guide captures no longer
  run through a shell.
### Fixed
- PR checklist referenced Godot tools (`gdlint`) left over from before ADR 0012.
- CI: gitleaks runs from its official container instead of the licensed action; `npm audit` scoped to shipped
  dependencies; the Unreal workflow no longer fails when no self-hosted runner exists; semgrep telemetry off.

## [0.4.0] — 2026-10-07
### Added / Ajouté
- **Bilingual, autonomous studio**: `studio.config.yaml` (autonomy `guided`/`autonomous`/`full`, hard stops, defaults, `extra_instructions`), `DECISIONS.md`, `QUESTIONS.md`; precedence user message > config > defaults, safety contract above all.
- All 8 skills rewritten in English with a French summary; replies in the user's language.
- `README.md` (EN) + `README.fr.md`; bilingual `CLAUDE.md` / `AGENTS.md`; `GEMINI.md`; `.github/copilot-instructions.md`; English guides in `docs/guides/en/`; PDF guide in FR and EN (`--lang`).
- Cinematic landing: spec `docs/design/34_LANDING_CINEMATIQUE.md`, shots L00–L04, components `CinematicHero` and `EraSequence` (scroll-scrubbed, Framer Motion), automatic switch from typographic mode once renders are approved; `tools/check_media_approvals.py` in CI.
- `.claude/settings.json`: Epic Unreal plugin and `frontend-design` pre-declared in `enabledPlugins`.

## [0.3.0] — 2026-10-07
### Modifié
- Bascule vers **Unreal Engine 5.8** et une direction artistique **réaliste** (ADR 0012) : TDD, bible artistique, playbook et skills réécrits.
- Aucune image de jeu dans le dépôt : cahier de rendu (`docs/design/33_VISUAL_TARGETS.md`) et liste de plans exécutable (`data/shotlist.json`).
### Ajouté
- Corpus juridique complet (`legal/`, 22 documents).
- Landing page de référence testée et version React + Vite + TypeScript + Framer Motion ; projet Remotion pour les titrages.
- Tests Robot Framework, Playwright, k6 ; CI données/confidentialité/landing, sécurité (gitleaks, semgrep, ZAP), publication manuelle, CI Unreal (runner Windows).
- Guides A→Z, installation, temps et coûts, sécurité, personnalisation, autres IA, FAQ ; schémas ; guide PDF.

## [0.2.0] — 2026-10-07
- Dossier de production (bible narrative, scripts, scénarios, paramètres, monde, audio, UX, production, QA, risques, juridique, marketing, live ops) et données de jeu.

## [0.1.0] — 2026-10-07
- Étude de marché et concept.
