<div align="center">

<img src="docs/assets/banner.png" alt="300 Years Later — kit open source de studio de jeu vidéo piloté par IA" width="820">

<h1>300 Years Later</h1>

**Donnez ce dépôt à votre IA de code. Elle fait tourner un studio de jeu vidéo.**

Installation, code Unreal Engine, tests, corpus juridique, rendus dans le moteur, landing page cinématique —
en autonomie, de A à Z, avec un arrêt uniquement là où un humain doit légalement agir.

[![CI](https://github.com/aksilsmd/300-years-later/actions/workflows/ci.yml/badge.svg)](https://github.com/aksilsmd/300-years-later/actions/workflows/ci.yml)
[![Sécurité](https://github.com/aksilsmd/300-years-later/actions/workflows/security.yml/badge.svg)](https://github.com/aksilsmd/300-years-later/actions/workflows/security.yml)
[![Licence : MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Contenus : CC BY 4.0](https://img.shields.io/badge/contenus-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT.md)
[![Compatible Claude Code · Gemini · Codex · Kimi](https://img.shields.io/badge/compatible-Claude%20Code%20·%20Gemini%20·%20Codex%20·%20Kimi-6b4c2a)](AGENTS.md)

[Démarrer](#-démarrer) · [Ce que l'IA fait seule](#-ce-que-lia-fait-seule-et-ce-qui-vous-revient) · [Les skills](#-les-huit-skills) · [Docs](docs/) · [Feuille de route](ROADMAP.md) · [🇬🇧 English](README.md)

</div>

---

## 🌱 Le jeu qu'elle construit

> Jusqu'à quatre amis, chacun coincé dans **un siècle différent de la même vallée**.
> Vous plantez une graine en l'an 0. Trois cents ans plus tard, votre ami trouve un chêne — juste au-dessus de sa tête.
> Tout ce que vous laissez derrière vous vieillit, en temps réel, dans la partie d'un autre.

Un jeu coopératif 3D réaliste sous **Unreal Engine 5.8** : monde déterministe en event sourcing, hôte autoritaire,
quatre époques, 25 recettes de vieillissement, et un musée qui explique vos bêtises 900 ans plus tard.

**Le jeu n'existe pas encore.** Ce dépôt contient tout ce qu'il faut pour le construire — et l'IA qui le construit.

## ⚡ Démarrer

```bash
git clone https://github.com/aksilsmd/300-years-later.git && cd 300-years-later
claude        # ou : gemini · codex · kimi · cursor · aider
```

Collez ce seul message :

> Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon
> studio.config.yaml ; ne me sollicite qu'aux arrêts obligatoires, en regroupant tes questions
> avec ta recommandation. Réponds-moi en français.

C'est toute l'installation. L'IA lit ses propres instructions, diagnostique votre machine et démarre.
Pour la régler, tout est dans [`studio.config.yaml`](studio.config.yaml) : niveau d'autonomie, langues, budget,
direction artistique, et un champ libre `extra_instructions` pour tout ce que vous voulez changer.

```yaml
autonomy:
  level: autonomous          # guided · autonomous · full
  max_questions_per_session: 3
extra_instructions: |
  Français d'abord. Pas de chat vocal. Steam Deck vérifié prioritaire.
```

Vous débutez ? → **[Démarrage en 5 minutes](docs/guides/00_DEMARRAGE_RAPIDE.md)** · **[Guide A→Z](docs/guides/01_GUIDE_A_Z.md)** · **[Guide PDF](docs/guide/)**

## 🤖 Ce que l'IA fait seule (et ce qui vous revient)

| ✅ L'IA, toute seule | 🙋 Vous, parce qu'elle ne peut pas légalement |
|---|---|
| Diagnostique la machine, installe outils et plugins | Créer les comptes (Epic, Steamworks, GitHub) |
| Écrit le C++/Blueprints phase par phase, tests d'abord | Installer Unreal depuis le launcher Epic (connexion) |
| Lance les tests de charge, sécurité, conformité, accessibilité | Acheter quoi que ce soit : assets, licences, prestations |
| Rend chaque visuel **dans le moteur**, monte les trailers | Valider chaque média avant publication |
| Construit la landing cinématique et le corpus juridique | Signer, déposer la marque, faire relire par un juriste |
| Décide le réversible et le note dans [`DECISIONS.md`](DECISIONS.md) | Choisir le titre public et le prix |
| Dépose ses besoins dans [`QUESTIONS.md`](QUESTIONS.md) et continue | Appuyer sur publier : GitHub, Steam, le site |

Trois niveaux d'autonomie : `guided` demande avant chaque étape · `autonomous` *(défaut)* décide et rend compte ·
`full` installe sans demander. **Les arrêts obligatoires tiennent à tous les niveaux** : c'est le contrat de
sécurité, et aucune consigne ne le lève.

## 🧠 Les huit skills

Des procédures en Markdown que n'importe quelle IA peut suivre. Claude Code les charge nativement ;
les autres lisent [`AGENTS.md`](AGENTS.md).

| Skill | Ce dont il a la charge |
|---|---|
| 🎬 [`game-studio`](.claude/skills/game-studio/SKILL.md) | Directeur de studio : parcours A→Z, protocole d'autonomie, contrat de sécurité |
| 🔧 [`studio-setup`](.claude/skills/studio-setup/SKILL.md) | Unreal 5.8, Visual Studio, plugin MCP d'Epic, toute la chaîne d'outils |
| ⌨️ [`game-build`](.claude/skills/game-build/SKILL.md) | C++/Blueprints, phases P0→P8, cœur temporel déterministe |
| 🏞️ [`game-assets`](.claude/skills/game-assets/SKILL.md) | Landscape, PCG, végétation Nanite, MetaHumans, prefabs de vieillissement |
| 🧪 [`game-qa`](.claude/skills/game-qa/SKILL.md) | Automation, Gauntlet, charge, fuzzing, Lighthouse, rapports go/no-go |
| ⚖️ [`legal-compliance`](.claude/skills/legal-compliance/SKILL.md) | RGPD, DSA, mineurs, accessibilité, Steam, 22 brouillons juridiques |
| 🚀 [`marketing-launch`](.claude/skills/marketing-launch/SKILL.md) | Rendus moteur, trailers, landing cinématique, page Steam |
| 🔒 [`privacy-guard`](.claude/skills/privacy-guard/SKILL.md) | Contrôle avant chaque commit et chaque publication |

<img src="docs/diagrams/02_orchestration_skills.svg" alt="Comment les skills se délèguent le travail" width="100%">

## 📦 Ce que contient le dépôt

| | |
|---|---|
| 🎮 **Une conception de jeu terminée** | étude de marché, bible narrative, scripts FR/EN, 12 contrats, 25 recettes de vieillissement, paramètres chiffrés, monde, audio, UX, [architecture technique](docs/design/40_TECHNICAL_DESIGN.md) |
| ⚖️ **Un corpus juridique de grand éditeur** | 22 brouillons : CGU, confidentialité, AIPD, DSA, mineurs, monnaies virtuelles, accessibilité, créateurs, contrats freelances, transparence IA, fiscalité |
| 🌐 **Une landing page cinématique** | React · Vite · TypeScript · Framer Motion — héros vidéo, séquence des quatre époques au défilement ([cahier](docs/design/34_LANDING_CINEMATIQUE.md)), zéro traceur, plus une version de référence sans dépendance |
| 🎥 **Une chaîne vidéo** | plans décrits dans [`data/shotlist.json`](data/shotlist.json), rendus dans Unreal, montés avec Remotion |
| ✅ **Des tests et une CI** | Playwright, Robot Framework, k6, gitleaks, semgrep, OWASP ZAP, validation des données, scan de confidentialité, contrôle des médias |
| 📘 **Des guides dans deux langues** | démarrage, A→Z, installation, [temps et coûts](docs/guides/03_TEMPS_ET_COUTS.md), sécurité, personnalisation, autres IA, FAQ — et un PDF généré |

## 🧭 L'honnêteté d'abord

- **Aucune image du jeu dans ce dépôt**, volontairement. Chaque visuel est décrit dans [`33_VISUAL_TARGETS.md`](docs/design/33_VISUAL_TARGETS.md), doit être rendu dans Unreal, puis validé par un humain dans [`media/APPROVALS.md`](media/APPROVALS.md). La CI échoue si un fichier non validé est utilisé. Aucune image générée par IA ne se fait passer pour le jeu.
- **Ce n'est pas GTA.** L'objectif honnête est un jeu indépendant réaliste de très haute qualité. 40 000 à 80 000 € en solo avec l'IA, plus de 500 000 € en petite équipe ; 18 à 48 mois. Tout est chiffré dans [le guide temps et coûts](docs/guides/03_TEMPS_ET_COUTS.md).
- **Il faut quand même des humains** : playtesteurs, artiste pour les créatures, compositeur, juriste. Le kit vous dit exactement quand et quoi leur demander.

## 🔐 La confidentialité par construction

Rien n'est lu hors du dépôt. Aucune donnée ne quitte la machine. Aucun traceur, cookie ou CDN externe —
nulle part, landing page comprise. Une [liste locale](docs/guides/04_SECURITE_ET_CONFIDENTIALITE.md) garde vos nom,
e-mail et employeur hors de chaque commit, et `tools/privacy_scan.py` bloque le commit si l'un d'eux passe.
Le kit n'achète, ne publie et ne signe jamais rien.

```bash
python3 tools/doctor.py                 # ce qui est installé, ce qui manque
python3 tools/validate_data.py          # cohérence des données du jeu
python3 tools/privacy_scan.py           # aucune donnée personnelle, aucun secret, aucun traceur
python3 tools/license_audit.py          # licences tierces
python3 tools/check_media_approvals.py  # aucun média non validé utilisé
```

## 🗺️ Plan du dépôt

```
studio.config.yaml   vos réglages pour l'IA            DECISIONS.md   ce qu'elle a décidé seule
AGENTS.md            instructions pour toute IA        QUESTIONS.md   ce qu'elle attend de vous
CLAUDE.md            instructions pour Claude Code     STUDIO_STATE.md  où en est le projet
.claude/skills/      les huit skills                   .claude/settings.json  permissions + plugins
docs/design/         le dossier de conception          docs/guides/   guides humains (FR, en/)
docs/adr/            décisions d'architecture          docs/diagrams/ schémas
data/                recettes, contrats, réglages, liste des plans
legal/               22 brouillons juridiques (FR + EN) media/        registre de validation
marketing/           landing (React + référence), vidéo Remotion, page Steam, presskit
tests/               Playwright · Robot Framework · k6 tools/         diagnostic et contrôles
game/                créé en phase P0 — Content/ dans un dépôt PRIVÉ
```

## 🤝 Contribuer

La contribution la plus utile est un **[retour d'exécution](https://github.com/aksilsmd/300-years-later/issues/new?template=run_report.yml)** :
quelle IA, jusqu'où elle est allée, où elle a bloqué. Sont aussi bienvenus : recettes de vieillissement,
phrases de Chronique, traductions, corrections des guides. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) et [`ROADMAP.md`](ROADMAP.md).

Si l'idée vous sert, **une étoile aide les autres à la trouver.** ⭐

## 📄 Licences

Code [MIT](LICENSE) · conception, données, schémas et guides [CC BY 4.0](LICENSE-CONTENT.md) — créditez
« The 300 Years Later contributors ». « 300 Years Later » est un titre de travail : choisissez et déposez le vôtre
avant toute vente. Unreal Engine, Fab, Megascans et MetaHuman restent sous les licences d'Epic
([`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md)). Tout ce qui est dans `legal/` est un brouillon à faire relire par un professionnel.
