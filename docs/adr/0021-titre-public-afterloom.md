# ADR 0021 — Titre public : AFTERLOOM

- **Statut :** proposé (attend la décision de l'humain et la recherche d'antériorité)
- **Date :** 2026-10-07
- **Décideurs :** Product Owner · **Remplace :** le titre de travail « 300 Years Later » (GDD §6.6)

## Contexte

Le projet porte trois noms : le nom de code **CENTURY TEMPS**, le titre de travail public
**« 300 Years Later »**, et le nom du dépôt `300-years-later`. Le titre de travail pose trois problèmes
mesurables :

1. **Référencement nul.** « 300 years later » est une tournure courante et entre en collision frontale avec la
   franchise *28 Years Later*. Un titre générique ne se trouve ni sur Steam, ni sur GitHub, ni dans un moteur
   de recherche, ni dans un modèle de langage.
2. **Pas de marque possible.** Une suite de mots descriptifs est difficile à déposer, et le GDD §6.6 exige un
   dépôt avant l'annonce publique.
3. **Il décrit un intervalle, pas une expérience.** Les succès coopératifs récents portent des noms courts,
   concrets et un peu étranges — c'est ce qui se retient et se cherche.

## Décision

Le titre public devient **AFTERLOOM**.

**Pourquoi ce mot.** *After* (ce qui vient après) et *loom* (le métier à tisser, et le verbe « se profiler »)
donnent, en un mot, le sujet exact du jeu : quelque chose se tisse après votre passage et finit par se dresser
devant quelqu'un d'autre. Il contient *heirloom*, l'objet transmis de génération en génération, qui est
littéralement la mécanique centrale.

**Pourquoi c'est bon opérationnellement :**
- **Mot inventé** : aucune concurrence dans les résultats de recherche, donc un référencement qui part de zéro
  mais sans plafond. Une recherche du terme ne renvoie aujourd'hui aucun jeu.
- **Déposable** : un néologisme est exactement ce qu'un office de marques accepte le plus facilement.
- **Prononçable en français et en anglais**, huit lettres, pas d'accent, pas d'apostrophe, pas de chiffre.
- **Disponible comme identifiant** : nom de dépôt, domaine, pseudonymes de réseaux à vérifier d'un coup.

Le reste de l'onomastique ne bouge pas : nom de code **CENTURY TEMPS**, agence **Temporis Intérim**, vallée
**Brumecombe**. Le sous-titre descriptif, lui, porte le référencement sémantique :
**« Afterloom — un jeu coopératif à travers quatre siècles »**.

## Alternatives étudiées

| Titre | Pour | Contre | Verdict |
|---|---|---|---|
| **300 Years Later** (actuel) | descriptif, clair | générique, collision *28 Years Later*, indéposable | abandonné |
| **CENTURY TEMPS** | jeu de mots bilingue (temps / intérimaires) | ne se comprend qu'expliqué ; « temps » prête à confusion | reste le nom de code |
| **TEMPORIS** | court, fort | **marque existante** d'une agence d'intérim française | écarté, risque juridique |
| **BRUMECOMBE** | ancre le lieu | imprononçable hors du français, invendable à l'international | reste le nom de la vallée |
| **PATINA** | juste thématiquement | mot courant, déjà utilisé dans plusieurs produits | écarté |
| **AFTERLOOM** | inventé, thématique, déposable, introuvable ailleurs | ne décrit pas le jeu sans sous-titre | **retenu** |

## Conséquences

**Immédiat, sans risque :** les nouveaux artefacts portent le titre — marque, favicon, logotype, carte
sociale, charte graphique (`35_DESIGN_SYSTEM.md`), `docs/assets/`.

**Après votre accord**, une seule commande, qui existe déjà et qui ne touche que ce qui est public :

```bash
python3 tools/apply_public_title.py --to "Afterloom"           # aperçu, ne modifie rien
python3 tools/apply_public_title.py --to "Afterloom" --apply   # écrit les 55 occurrences
python3 tools/repo_audit.py && python3 tools/privacy_scan.py && python3 -m pytest tests/web -q
```

Elle remplace le titre dans les READMEs, la landing, Remotion, la page Steam, le presskit, `llms.txt`, les
skills et les tests. Elle ne touche **ni** le nom de code CENTURY TEMPS, **ni** la vallée Brumecombe, **ni**
l'identifiant `300-years-later` et les URL qui en découlent, **ni** l'accroche française « 300 ans plus tard »,
**ni** l'entité d'attribution « The 300 Years Later contributors » des deux licences — ce dernier point est une
décision juridique distincte, à prendre d'un seul coup sur `LICENSE`, `LICENSE-CONTENT.md`, `CITATION.cff` et
`.claude-plugin/`. Cet ADR lui-même garde l'ancien titre, puisqu'il consigne la décision.

**Le nom du dépôt reste `300-years-later` jusqu'à ce que vous le renommiez.** Un renommage GitHub conserve les
redirections, mais il casse le chemin du plugin
(`/plugin marketplace add aksilsmd/300-years-later`), les URL de badges et les liens déjà partagés. Si vous
renommez, il faut reprendre `.claude-plugin/marketplace.json`, les badges des READMEs, `llms.txt`,
`CITATION.cff` et `tools/setup_repo.sh`.

**Avant toute annonce publique**, recherche d'antériorité obligatoire — c'est un arrêt humain, pas une tâche
d'agent : INPI, EUIPO/TMview, USPTO, Steam, itch.io, les stores mobiles, les noms de domaine et les réseaux
sociaux. Procédure dans [`legal/21_marque-pi.md`](../../legal/21_marque-pi.md). Dépôt visé : Union
européenne, classes 9 et 41.

## Textes prêts à coller

**Description GitHub** (350 caractères, à mettre dans *About*) :

> Afterloom — give this repo to Claude Code, Gemini or Codex and it runs a game studio: it installs the
> toolchain, writes an Unreal Engine 5.8 co-op game where four friends each live in a different century of
> the same valley, tests it, keeps it GDPR-compliant, renders the trailer and builds the landing page.
> 8 agent skills, bilingual FR/EN, MIT.

**Variante courte** (si le champ est tronqué à 160 caractères) :

> Give this repo to your coding agent and it runs a game studio — Unreal Engine 5.8, tests, GDPR, trailer,
> landing page. 8 skills, FR/EN, MIT.

**Mots-clés GitHub** (20 maximum, ceux-ci sont choisis pour la recherche réelle) :
`ai-agents` · `agent-skills` · `claude-code` · `claude-skills` · `unreal-engine` · `unreal-engine-5` ·
`game-development` · `game-design` · `gamedev` · `coop-game` · `multiplayer` · `autonomous-agents` ·
`ai-game-development` · `gdpr` · `open-source` · `developer-tools` · `llm-agents` · `framer-motion` ·
`qa-automation` · `game-studio`

**Titre de la carte sociale et des partages :**
> Afterloom — un studio de jeu vidéo que votre IA fait tourner
> Afterloom — the game studio your AI runs
