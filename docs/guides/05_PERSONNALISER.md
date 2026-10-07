# Personnaliser le projet (ou en faire votre propre jeu)

🇬🇧 [English version](en/05_CUSTOMISE.md)

Tout est conçu pour être modifié. Licence : code MIT, contenus CC BY 4.0 (créditez « The 300 Years Later contributors »). Le titre et la marque ne sont pas couverts par la licence.

## 0. Dire à l'IA ce que vous voulez
- **Une fois pour toutes :** `extra_instructions` dans `studio.config.yaml` (ex. « anglais d'abord, Steam Deck vérifié prioritaire, pas de chat vocal »).
- **Pour une session :** ajoutez vos consignes après le prompt de démarrage. Elles l'emportent sur le fichier ; seul le contrat de sécurité ne peut pas être levé.

## 1. Changer le titre
1. Choisissez un titre et faites la recherche de marque (`legal/21_marque-pi.md`).
2. Demandez à l'IA : « Remplace le titre public "300 Years Later" par "<NOUVEAU TITRE>" partout où il est public (README, landing, Remotion, docs/design/70), sans toucher au nom de code CENTURY TEMPS ni aux identifiants techniques. »
3. Vérifiez : `python3 tools/privacy_scan.py` et les tests de la landing.

## 2. Modifier le jeu sans coder
| Vous voulez… | Modifiez | Vérifiez |
|---|---|---|
| ajouter une transformation dans le temps | `data/recipes/*.json` (format : `data/schemas/recipe.schema.json`) + un modèle de Chronique dans `data/phrases/` | `python3 tools/validate_data.py` |
| ajouter un contrat | `data/contracts/*.json` | idem |
| régler la durée des manches, les vitesses, le score | `data/tuning.json` | playtest |
| changer le look d'une époque | `docs/design/33_VISUAL_TARGETS.md` §2 puis demander à l'IA d'appliquer | revue visuelle |
| ajouter un plan de trailer | `data/shotlist.json` | rendu + validation |

## 2 bis. Changer le titre public du jeu

Le projet porte trois noms distincts et c'est volontaire : le **nom de code** (CENTURY TEMPS), le **titre
public** (« 300 Years Later » aujourd'hui) et l'**identifiant du dépôt** (`300-years-later`, qui apparaît dans
toutes les URL). Pour ne changer que le deuxième :

```bash
python3 tools/apply_public_title.py --to "Mon Titre"           # aperçu fichier par fichier
python3 tools/apply_public_title.py --to "Mon Titre" --apply   # écrit
python3 tools/repo_audit.py && python3 tools/privacy_scan.py && python3 -m pytest tests/web -q
```

L'outil ne touche jamais l'identifiant du dépôt, le nom de code, le nom de la vallée, l'accroche « 300 ans plus
tard » ni l'entité d'attribution des licences ; il affiche ce qu'il a laissé et pourquoi. **Renommer le dépôt
lui-même est une autre affaire** : GitHub garde les redirections, mais cela casse le chemin du plugin, les
badges et les liens déjà partagés — voir [ADR 0021](../adr/0021-titre-public-afterloom.md).

## 2 ter. L'encart « About » du dépôt

La description, le site et les mots-clés visibles en haut de la page GitHub ne sont **pas** dans le code : ce
sont des réglages du dépôt. Aucune IA ne peut les écrire, et aucun `git push` ne les change. Leur source de
vérité est [`.github/about.yml`](../../.github/about.yml) ; `bash tools/setup_repo.sh` les applique avec votre
propre jeton, et affiche le texte à coller si une écriture est refusée.

## 3. Réutiliser le studio pour un autre jeu
Les skills (`.claude/skills/`) sont génériques à 80 % : remplacez `docs/design/` par votre propre conception (en gardant la même structure de fichiers), adaptez `CLAUDE.md`, puis lancez `game-studio`. Gardez le contrat de sécurité, les portes de décision et le corpus juridique comme base.
