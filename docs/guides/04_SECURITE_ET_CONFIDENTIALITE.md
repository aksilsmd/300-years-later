# Sécurité et confidentialité : comment le kit vous protège

![Modèle de sécurité](../diagrams/05_modele_securite.svg)

## 1. Ce que l'IA peut faire seule
Lire et écrire **dans le dépôt**, installer des outils **depuis les sources officielles après votre accord**, compiler, tester, piloter l'éditeur Unreal via MCP sur une branche, préparer des documents et des médias.

## 2. Ce que l'IA ne fait jamais seule
| Action | Pourquoi |
|---|---|
| Acheter (assets, Steam Direct, prestataires) | votre argent |
| Créer un compte, saisir un identifiant | votre identité |
| Publier (GitHub public, Steam, réseaux, site) | votre responsabilité d'éditeur |
| Signer, déposer une marque | engagement juridique |
| Choisir le titre, le prix, les textes publics | décisions d'éditeur |
| Lire vos fichiers personnels, clés SSH, `.env`, trousseaux | règles `deny` de `.claude/settings.json` |
| Envoyer vos données vers un service tiers | aucun appel réseau hors sources officielles |
| Ajouter un traceur, un cookie, un CDN | interdit et détecté par `privacy_scan.py` |
| Publier `game/Content/` ou des assets Epic/Fab/MetaHuman | interdit par les licences, bloqué par la CI |

## 3. Protéger vos données personnelles
1. Créez `~/.config/300yl/denylist.txt` (hors du dépôt) avec vos nom, prénom, e-mail, pseudo, employeur, ville. `tools/privacy_scan.py` refusera tout fichier qui les contient.
2. Configurez Git avec l'adresse anonyme GitHub : `git config user.email "<id>+<pseudo>@users.noreply.github.com"`.
3. Activez le contrôle avant commit : `git config core.hooksPath .githooks`.
4. Utilisez une adresse e-mail dédiée au projet pour tous les textes publics (CGU, mentions légales, presse).
5. Supprimez les métadonnées des médias avant publication (`exiftool -all=`), ce que fait le skill `privacy-guard`.

## 4. Vérifier vous-même
```bash
python3 tools/privacy_scan.py
cat .claude/settings.json
git ls-files | grep -Ei '\.(uasset|umap|pak)$|^game/Content/'   # doit être vide
```

## 5. Les joueurs
Le jeu applique la protection par défaut (`legal/03`, `legal/09`) : voix jamais enregistrée, statistiques en opt-in, parties entre amis par défaut, aucun achat intégré.
