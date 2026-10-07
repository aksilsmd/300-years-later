# 300 Years Later — le studio de jeu vidéo IA open source

**Donnez ce dépôt à Claude Code (ou à une autre IA), et elle construit avec vous un jeu coopératif 3D réaliste sous Unreal Engine 5.8 : installation, code, tests, conformité, trailer et landing page, en s'arrêtant à chaque décision qui vous revient.**

> *Jusqu'à 4 amis, chacun bloqué dans un siècle différent de la même vallée. Tu plantes une graine en l'an 0 : ton ami la retrouve 300 ans plus tard, devenue chêne… juste au-dessus de sa tête.*

*English summary at the bottom.*

---

## Ce que contient le dépôt
| | |
|---|---|
| 🎮 **Un jeu entièrement conçu** | étude de marché, bible narrative, scripts FR/EN, 12 contrats, 25 recettes de vieillissement, paramètres chiffrés, monde, audio, UX, architecture technique Unreal |
| 🧠 **8 skills pour l'IA** | un directeur de studio qui orchestre installation, code, assets, QA, juridique, marketing et confidentialité |
| ⚖️ **Un corpus juridique de grand éditeur** | CGU, confidentialité, AIPD, DSA, mineurs, monnaies virtuelles, accessibilité, créateurs, contrats freelances, transparence IA, éthique, fiscalité — 22 brouillons structurés |
| 🌐 **Une landing page** | version de référence testée (sans traceur ni ressource externe) + version React · Vite · TypeScript · Framer Motion |
| 🎬 **Une chaîne vidéo** | plans à rendre dans Unreal (`data/shotlist.json`) et montage des trailers avec Remotion |
| ✅ **Des tests et une CI** | Playwright, Robot Framework, k6, gitleaks, semgrep, OWASP ZAP, validation des données, scan de confidentialité, CI Unreal |
| 📘 **Des guides** | démarrage rapide, A→Z, installation, temps et coûts, sécurité, personnalisation, autres IA, FAQ — et un guide PDF |

## Honnêteté d'abord
- **Le jeu n'existe pas encore** : ce dépôt est tout ce qu'il faut pour le construire. Il ne contient **aucune image du jeu**. Les visuels sont décrits avec précision et seront rendus **dans Unreal Engine**, puis validés par un humain (`media/APPROVALS.md`).
- **Ce n'est pas GTA.** L'objectif atteignable est un jeu indépendant réaliste de très haute qualité. Budget : de ≈ 40 000 € (solo + IA) à plus de 500 000 € (petite équipe). Durée : 18 à 48 mois. Tout est chiffré dans [`docs/guides/03_TEMPS_ET_COUTS.md`](docs/guides/03_TEMPS_ET_COUTS.md).
- **L'IA ne décide pas à votre place** : pas d'achat, de publication, de signature, de choix du nom ou du prix sans vous.

## Démarrer en 5 minutes
```bash
git clone <URL-DE-CE-DÉPÔT> 300-years-later && cd 300-years-later
python3 tools/doctor.py          # ce qui est installé, ce qui manque
python3 tools/validate_data.py   # cohérence des données du jeu
python3 tools/privacy_scan.py    # aucune donnée personnelle ni secret
claude
```
Puis, dans Claude Code :
> Lis AGENTS.md puis lance le skill game-studio. Fais l'étape A (diagnostic) et présente-moi le plan de l'étape B. N'installe rien avant mon accord.

Guide complet : [`docs/guides/00_DEMARRAGE_RAPIDE.md`](docs/guides/00_DEMARRAGE_RAPIDE.md).

## Le parcours
![Parcours du studio de A à Z](docs/diagrams/01_parcours_a_z.svg)

## Les skills
![Orchestration des skills](docs/diagrams/02_orchestration_skills.svg)

| Skill | Rôle |
|---|---|
| [`game-studio`](.claude/skills/game-studio/SKILL.md) | directeur de studio : parcours A→Z, portes de décision, contrat de sécurité |
| [`studio-setup`](.claude/skills/studio-setup/SKILL.md) | poste Unreal 5.8, Visual Studio, plugin officiel Epic pour Claude Code (MCP), outils |
| [`game-build`](.claude/skills/game-build/SKILL.md) | code C++/Blueprints par phases P0→P8, tests d'abord |
| [`game-assets`](.claude/skills/game-assets/SKILL.md) | monde réaliste (Landscape, PCG, Nanite), Fab, MetaHuman, prefabs de vieillissement |
| [`game-qa`](.claude/skills/game-qa/SKILL.md) | Automation, Gauntlet, charge, performance, sécurité, conformité, rapports go/no-go |
| [`legal-compliance`](.claude/skills/legal-compliance/SKILL.md) | tenue du corpus juridique `legal/` |
| [`marketing-launch`](.claude/skills/marketing-launch/SKILL.md) | rendus Unreal, trailers, landing page, page Steam, presskit |
| [`privacy-guard`](.claude/skills/privacy-guard/SKILL.md) | contrôle avant tout commit ou publication |

Autres agents (Codex, Gemini CLI, Cursor, Aider…) : voir [`AGENTS.md`](AGENTS.md).

## Plan du dépôt
```
.claude/            skills + permissions de l'IA
docs/design/        conception du jeu (GDD, narration, scripts, scénarios, technique, art, production, QA…)
docs/guides/        guides pour les humains          docs/diagrams/  schémas
docs/adr/           décisions d'architecture         legal/          corpus juridique (brouillons)
data/               recettes, contrats, réglages, phrases, liste des plans à rendre
marketing/          landing (référence + React), vidéo (Remotion), page Steam, presskit, plan de lancement
tests/              Playwright, Robot Framework, k6  tools/          diagnostic, validation, confidentialité, licences
game/               (créé en phase P0) projet Unreal — Content/ dans un dépôt PRIVÉ
```

## Sécurité et vie privée
Le kit est conçu pour ne **jamais** exposer vos données : rien n'est lu hors du dépôt, aucune donnée n'est envoyée, aucun traceur, contrôle automatique avant chaque commit, CI de sécurité. Voir [`SECURITY.md`](SECURITY.md) et [`docs/guides/04_SECURITE_ET_CONFIDENTIALITE.md`](docs/guides/04_SECURITE_ET_CONFIDENTIALITE.md).

## Licences
Code : [MIT](LICENSE). Conception, données, schémas, guides : [CC BY 4.0](LICENSE-CONTENT.md). « 300 Years Later » est un titre de travail : choisissez et déposez votre propre titre avant toute commercialisation. Les textes de `legal/` sont des brouillons à faire valider par un professionnel.

## Contribuer
Recettes, modèles de Chronique, traductions, retours de runs complets : voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## English summary
**300 Years Later** is an open-source, AI-driven game studio kit. Give this repository to Claude Code (or another coding agent) and it will help you build a realistic 3D co-op game in **Unreal Engine 5.8** — setup, code, tests, compliance, trailer and landing page — stopping at every decision that belongs to you. It contains a complete game design (market study, story, scripts, data, technical design), 8 agent skills, a 22-document legal framework (drafts), a tested tracker-free landing page plus a React/Framer Motion version, a Remotion video pipeline, tests and CI. **There are no game images yet, by design**: every visual is specified (`docs/design/33_VISUAL_TARGETS.md`, `data/shotlist.json`) and must be rendered in-engine and approved by a human. Realistic budget: from ≈ €40k (solo + AI) to €500k+ (small team). Code is MIT, content is CC BY 4.0. Start with `AGENTS.md`.
