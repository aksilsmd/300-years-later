---
name: privacy-guard
description: Garde-fou de confidentialité et de sécurité appliqué avant tout commit, export, publication ou partage — recherche de données personnelles, secrets, traceurs et ressources externes ; vérifie l'identité Git anonyme. Utiliser avant « commit », « push », « publie », « partage », « exporte ».
---

# Skill : privacy-guard

1. `python3 tools/privacy_scan.py` (utilise la liste locale `~/.config/300yl/denylist.txt` si elle existe). Si l'humain n'en a pas, propose-lui d'en créer une **hors du dépôt** avec ses identifiants ; ne lui demande pas de te les dicter dans le dépôt.
2. Si `gitleaks` est installé : `gitleaks detect --no-banner --redact`.
3. Vérifie l'identité Git : `git config user.email` doit être une adresse `@users.noreply.github.com` ou une adresse dédiée au projet. Sinon, **alerte** avant tout push.
4. Vérifie les métadonnées des médias : `exiftool -all= -overwrite_original media/**/*` si disponible (supprime GPS, appareil, auteur) ; les PNG générés par le kit n'en contiennent pas.
5. Vérifie qu'aucun fichier ignoré sensible n'est indexé : `git ls-files | grep -Ei '(^|/)\.env(\.|$)|secret|denylist|\.pem$|\.key$|steam_appid'` doit être vide.
6. Rapport en 3 lignes : ✓/✗ par contrôle. Au moindre ✗ : **ne publie pas**, explique et propose la correction.
