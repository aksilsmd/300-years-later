---
name: game-qa
description: Assurance qualité de niveau studio pour le jeu Unreal Engine 5.8 et sa landing page — Automation Spec, Functional Tests, Gauntlet (multi-clients et charge), Unreal Insights (performance), fuzzing réseau, sécurité (gitleaks, semgrep, OWASP ZAP), conformité (RGPD, licences, accessibilité, Steam, DSA, mineurs), revue visuelle, E2E Robot Framework, k6, Lighthouse et rapports go/no-go. Utiliser à chaque fin de phase, avant une porte, ou pour « teste », « audit », « sécurité », « charge ».
---

# Skill : game-qa

Référentiel : `docs/design/51_QA_TEST_PLAN.md`. Ce skill dit **comment exécuter**.

## 1. Pyramide et commandes
| Niveau | Commande / outil | Seuil |
|---|---|---|
| Unitaire cœur | `UnrealEditor-Cmd.exe <projet> -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -log` | 100 % verts, golden OK |
| Fonctionnel | `-ExecCmds="Automation RunTests Project.Functional;Quit"` | 100 % verts |
| Réseau multi-clients | `RunUAT.bat RunUnreal -test=TemporalValley.NetDeterminism -clients=3` | 0 désync, confirmation p95 < 400 ms à 250 ms de latence (Network Emulation : `-NetEmulation.PktLag=250 -NetEmulation.PktLoss=2`) |
| **Charge** | Gauntlet `TemporalValley.LoadTest` : 8 sessions × 4 bots, 10 min | hôte < 4 ms/tick logique, < 30 ko/s/joueur, 0 crash |
| **Fuzzing RPC** | test `TemporalValley.RpcFuzz` (10 000 requêtes malformées) | 0 crash, rejets comptés, kick à 20/min |
| **Performance** | Unreal Insights + `csvprofile` sur la scène de stress, 3 profils du TDD §10 | budgets TDD §10 et `30_ART_BIBLE.md` §4 |
| Mémoire | `memreport -full` au début et après 2 h | fuite < 200 Mo |
| Sécurité dépôt | `gitleaks detect --no-banner --redact` · `semgrep --config p/default --error` · `python3 tools/privacy_scan.py` | 0 fuite, 0 alerte haute |
| Licences / données | `python3 tools/license_audit.py && python3 tools/validate_data.py` + contrôle « aucun asset Fab/MetaHuman dans le dépôt public » | vert |
| Revue visuelle | captures des plans `data/shotlist.json` comparées aux critères de `33_VISUAL_TARGETS.md` ; validation humaine | 100 % des plans publiés validés |
| E2E landing | `robot --outputdir results tests/robot` | 100 % verts |
| Charge landing | `k6 run -e BASE_URL=<url> tests/load/landing_smoke.js` | p95 < 500 ms, erreurs < 1 % |
| Web perf / a11y | Lighthouse | ≥ 90 / 95 / 95 / 90 |
| Sécurité web | OWASP ZAP baseline (workflow `security.yml`) | 0 alerte haute |

## 2. Conformité exécutable
- **RGPD** : télémétrie no-op sans consentement (test) ; aucun audio dans `Saved/` (test) ; capsule sans pseudo ni SteamID (test) ; écran de consentement à boutons équivalents (capture).
- **Mineurs / DSA** : lobbies amis par défaut ; mute, blocage, signalement accessibles en ≤ 2 actions ; textes libres filtrés ; procédure de signalement reliée à `legal/moderation-policy.md`.
- **Accessibilité** : chaque option de `32_UX_UI_SPEC.md` §6 testée ; partie terminable sans micro, sans son, en mode daltonien, en « réduire les clignotements » ; vérification de photosensibilité des effets glitch (aucun flash > 3 Hz en mode réduit).
- **Monnaie virtuelle** : le jeu n'en vend pas — test qu'aucun achat réel n'existe dans le build.
- **Steam** : succès, Cloud, overlay, Deck (texte ≥ 9 px à 1280×800).
- **Localisation** : pseudo-loc +30 %, aucune chaîne en dur, placeholders identiques.

## 3. Playtests
Prépare le kit (build, formulaire `legal/playtest-consent.md`, grille, questionnaire). L'humain conduit les playtests et te transmet des résultats anonymisés.

## 4. Rapport go/no-go
`docs/qa/<porte>.md` : périmètre, résultats par campagne, anomalies S1-S4, mesures (perf, réseau, charge, web), conformité (RGPD, licences, accessibilité, DSA/mineurs, Steam), risques résiduels, recommandation. **Jamais GO** avec un S1 ouvert, une fuite de données, un asset sous licence exposé ou une alerte de sécurité haute.
