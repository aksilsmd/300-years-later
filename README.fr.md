# 300 Years Later — le studio de jeu vidéo IA open source

🇬🇧 [English](README.md) · 🇫🇷 Français

**Donnez ce dépôt à Claude Code, Gemini, Kimi, Codex ou une autre IA de code : elle travaille en autonomie de A à Z — installation des dépendances, skills et plugins, code du jeu 3D réaliste sous Unreal Engine 5.8, tests, conformité, rendus, trailer et landing page cinématique — et ne vous sollicite qu'aux décisions qui vous reviennent.**

> *Jusqu'à 4 amis, chacun bloqué dans un siècle différent de la même vallée. Tu plantes une graine en l'an 0 : ton ami la retrouve 300 ans plus tard, devenue chêne… juste au-dessus de sa tête.*


---

## Ce que contient le dépôt
| | |
|---|---|
| 🎮 **Un jeu entièrement conçu** | étude de marché, bible narrative, scripts FR/EN, 12 contrats, 25 recettes de vieillissement, paramètres chiffrés, monde, audio, UX, architecture technique Unreal |
| 🧠 **8 skills pour l'IA (bilingues)** | un directeur de studio qui orchestre installation, code, assets, QA, juridique, marketing et confidentialité |
| ⚖️ **Un corpus juridique de grand éditeur** | CGU, confidentialité, AIPD, DSA, mineurs, monnaies virtuelles, accessibilité, créateurs, contrats freelances, transparence IA, éthique, fiscalité — 22 brouillons structurés |
| 🌐 **Une landing page cinématique** | React · Vite · TypeScript · Framer Motion : héros vidéo, séquence des 4 époques pilotée au défilement (`docs/design/34`) ; bascule automatique dès que les rendus Unreal sont validés ; version de référence sans dépendance ; zéro traceur |
| 🎬 **Une chaîne vidéo** | plans à rendre dans Unreal (`data/shotlist.json`) et montage des trailers avec Remotion |
| ✅ **Des tests et une CI** | Playwright, Robot Framework, k6, gitleaks, semgrep, OWASP ZAP, validation des données, scan de confidentialité, CI Unreal |
| 📘 **Des guides** | démarrage rapide, A→Z, installation, temps et coûts, sécurité, personnalisation, autres IA, FAQ — et un guide PDF |

## Honnêteté d'abord
- **Le jeu n'existe pas encore** : ce dépôt est tout ce qu'il faut pour le construire. Il ne contient **aucune image du jeu**. Les visuels sont décrits avec précision et seront rendus **dans Unreal Engine**, puis validés par un humain (`media/APPROVALS.md`).
- **Ce n'est pas GTA.** L'objectif atteignable est un jeu indépendant réaliste de très haute qualité. Budget : de ≈ 40 000 € (solo + IA) à plus de 500 000 € (petite équipe). Durée : 18 à 48 mois. Tout est chiffré dans [`docs/guides/03_TEMPS_ET_COUTS.md`](docs/guides/03_TEMPS_ET_COUTS.md).
- **L'IA ne décide pas à votre place** : pas d'achat, de publication, de signature, de choix du nom ou du prix sans vous.

## Démarrer : un seul message à votre IA
```bash
git clone <URL-DE-CE-DÉPÔT> 300-years-later && cd 300-years-later
claude        # ou gemini, kimi, codex, cursor, aider…
```
Puis collez :
> Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon studio.config.yaml ; ne me sollicite qu'aux arrêts obligatoires, en regroupant tes questions avec ta recommandation. Réponds-moi en français.
> *(facultatif)* Instructions en plus : …

Vous pouvez aussi écrire vos préférences une fois pour toutes dans [`studio.config.yaml`](studio.config.yaml) (niveau d'autonomie, langues, budget, direction artistique, `extra_instructions`). **Votre message l'emporte sur le fichier, le fichier l'emporte sur les valeurs par défaut** ; le contrat de sécurité l'emporte sur tout.

### Ce que l'IA fait seule / ce qui vous revient
| L'IA fait seule | Vous seul (arrêts obligatoires) |
|---|---|
| diagnostic, installation des outils (après un accord global), configuration des plugins (Epic MCP, frontend-design) | créer vos comptes (Epic, Steamworks, GitHub) et vous connecter |
| code C++/Blueprints phase par phase, tests, CI, rapports | installer Unreal Engine depuis l'Epic Games Launcher (connexion requise) |
| choix ayant une valeur par défaut raisonnable — notés dans [`DECISIONS.md`](DECISIONS.md) | tout achat (assets Fab, licences), toute signature |
| playtests par bots + auto-revue ; prépare le kit de playtest humain | jouer et donner votre ressenti (non bloquant en mode autonome) |
| rendus dans Unreal, montage Remotion, landing page (mode typographique puis cinématique) | valider chaque média avant publication (`media/APPROVALS.md`) |
| brouillons juridiques complets FR/EN | validation par un juriste avant sortie ; nom public, prix |
| prépare tout pour publier | publier (GitHub, Steam, site) |

Ses questions ouvertes vont dans [`QUESTIONS.md`](QUESTIONS.md) — elle continue sur d'autres chantiers en attendant. Trois niveaux : `guided` (demande souvent), `autonomous` (défaut), `full` (même l'installation sans demander).

Guide complet : [`docs/guides/00_DEMARRAGE_RAPIDE.md`](docs/guides/00_DEMARRAGE_RAPIDE.md) · Autres IA : [`docs/guides/06_AUTRES_IA.md`](docs/guides/06_AUTRES_IA.md).

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

Autres agents (Gemini CLI, Kimi, Codex, Cursor, Copilot, Aider…) : voir [`AGENTS.md`](AGENTS.md) — `GEMINI.md` et `.github/copilot-instructions.md` y renvoient.

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
