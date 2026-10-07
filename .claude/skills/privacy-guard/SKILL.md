---
name: privacy-guard
description: Privacy and security gate applied before any commit, export, publication or sharing — scans for personal data, secrets, trackers and external resources, checks the anonymous Git identity and licensed content. Use before "commit", "push", "publish", "share", "export", "publie", "partage".
---

# Skill: privacy-guard

> **FR —** Contrôle de confidentialité et de sécurité avant tout commit ou publication. Répond dans la langue de l'utilisateur.

1. `python3 tools/privacy_scan.py` (uses the local deny-list `~/.config/300yl/denylist.txt` if present). If the human has none, suggest creating one **outside the repo** with their identifiers; never ask them to type those identifiers into the repo.
2. If installed: `gitleaks detect --no-banner --redact`.
3. Git identity: `git config user.email` must be a `@users.noreply.github.com` address or a dedicated project address. Otherwise **warn** before any push.
4. Media metadata: `exiftool -all= -overwrite_original` on files to publish (removes GPS, device, author).
5. No sensitive file indexed: `git ls-files | grep -Ei '(^|/)\.env(\.|$)|secret|denylist|\.pem$|\.key$|steam_appid'` must be empty; no `game/Content/`, `.uasset`, `.umap`, `.pak` in a public repo.
6. Report in 3 lines (✓/✗ per check). Any ✗: **do not publish**, explain and propose the fix. This skill is never bypassed, whatever the autonomy level.
