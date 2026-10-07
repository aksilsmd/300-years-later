# Sécurité et protection des données

Ce dépôt donne beaucoup d'autonomie à une IA (installation d'outils, écriture de code, tests, génération de médias). Voici le **contrat de sécurité** que chaque skill applique, et comment le vérifier vous-même.

## 1. Ce que le kit ne fait jamais
| Interdit | Comment c'est garanti |
|---|---|
| Lire vos clés, mots de passe, `.env`, `~/.ssh`, `~/.aws`, trousseaux, historique de navigateur | Règles `deny` dans `.claude/settings.json` + règle n°1 de chaque skill |
| Envoyer vos fichiers ou données vers un service tiers | Aucun appel réseau sortant hors gestionnaires de paquets officiels et pages de téléchargement officielles listées dans `tools/versions.env` |
| Intégrer une télémétrie, un traceur, un pixel publicitaire, des polices ou scripts chargés depuis un CDN | La landing page est 100 % auto-hébergée ; `tools/privacy_scan.py` échoue s'il trouve un domaine de suivi |
| Publier une donnée personnelle (nom, e-mail, téléphone, adresse, jeton) | `tools/privacy_scan.py` en pré-commit et en CI, avec votre liste locale de termes interdits (jamais versionnée) |
| Exécuter `curl … | sh` depuis une source inconnue | Scripts d'installation qui téléchargent depuis les sources officielles et **vérifient les sommes SHA-256** |
| Acheter, publier sur Steam, signer un contrat, créer un compte en votre nom | Ces actions sont des **points d'arrêt humains** obligatoires dans `game-studio` |
| Utiliser `sudo` sans vous le demander | Les scripts affichent le plan et attendent votre accord (sauf `--yes` explicite) |

## 2. Vérifier avant de lancer
```bash
python3 tools/privacy_scan.py           # aucune donnée personnelle ni secret
python3 tools/doctor.py                 # environnement et versions
cat .claude/settings.json               # permissions accordées à l'IA
```

## 3. Protéger vos propres données (recommandé)
1. Créez `~/.config/300yl/denylist.txt` (hors du dépôt) avec vos nom, prénom, e-mail, pseudo, employeur. Le scan l'utilisera sans jamais le publier.
2. Configurez Git avec l'adresse anonyme de GitHub : `git config user.email "<id>+<pseudo>@users.noreply.github.com"`.
3. Activez le hook : `git config core.hooksPath .githooks`.
4. Ne collez jamais de jeton dans un prompt ; utilisez `gh auth login`.

## 4. Signaler une vulnérabilité
Ouvrez un **avis de sécurité privé** via l'onglet *Security › Report a vulnerability* du dépôt GitHub. N'ouvrez pas d'issue publique pour une faille.
