# Audit de la livraison v1 (GDD + CLAUDE.md du 7 oct. 2026, 13h41)

Méthode : relecture critique selon la grille de pré-production d'un studio (concept, narration, design, monde, art, audio, UX, technique, production, QA, juridique, marketing, live). Chaque écart est classé **Bloquant / Majeur / Mineur** et pointe vers le document v2 qui le corrige.

## 1. Ce qui était solide (à conserver)
- Étude de marché sourcée et conclusion claire (friendslop + profondeur sandbox).
- Concept réellement différenciant (moteur de vieillissement, rotation des époques, musée-machine à clips, capsule asynchrone).
- Choix techniques sobres et cohérents (Godot 4.7, GodotSteam, event sourcing, hôte autoritaire, tests, CI).
- Cadre juridique correct dans ses grandes lignes (RGPD, licences, IA, marque, structure).
- Plan en phases avec critères d'acceptation.

## 2. Écarts constatés
| # | Écart | Gravité | Correction v2 |
|---|---|---|---|
| 1 | **Aucune histoire** : pas d'arc, pas d'antagoniste, pas de raison de jouer plus de 3 parties hors sandbox | Bloquant | `10_NARRATIVE_BIBLE.md` (monde, lore du temps, 10 personnages, arc en 5 chapitres, fin) |
| 2 | **Aucun script** : zéro ligne de dialogue, pas de modèles de phrases pour le musée | Bloquant | `11_SCRIPTS_DIALOGUES.md` (tutoriel, briefs, notes du Client, 25 modèles de chronique, barks, conseils, erreurs) FR + EN |
| 3 | **Aucun scénario joué** : on ne sait pas à quoi ressemble une partie minute par minute | Bloquant | `12_SCENARIOS.md` (séance type, 12 contrats détaillés, cas limites, streaming, solo, capsule) |
| 4 | **Pas de paramètres chiffrés** (durées, vitesses, jauges, scores, économie) → Claude Code aurait inventé | Bloquant | `20_GAME_DESIGN_PARAMETERS.md` (tables de réglage complètes) |
| 5 | Répartition des époques à 2 et 3 joueurs non définie ; époques « sans joueur » non simulées | Majeur | `20` §2 (règles d'allocation, simulation des époques vides) |
| 6 | Pas de level design (taille de carte, repères, génération procédurale, lisibilité) | Majeur | `21_WORLD_LEVEL_DESIGN.md` |
| 7 | Direction artistique réduite à 5 lignes (pas de palettes hex, proportions, caméra, VFX, UI) | Majeur | `30_ART_BIBLE.md` |
| 8 | Audio sans spécification (pas de structure musicale, liste SFX, mixage, voix procédurale) | Majeur | `31_AUDIO_DESIGN.md` |
| 9 | UX/UI absente (flux d'écrans, HUD, manette, onboarding 60 s, accessibilité concrète) | Majeur | `32_UX_UI_SPEC.md` |
| 10 | TDD incomplet : pas de schémas de données, format du journal, contrat RPC, algorithme de propagation, format capsule, gestion de la physique | Bloquant | `40_TECHNICAL_DESIGN.md` + `data/schemas/` |
| 11 | Pas de données d'exemple (recettes, contrats, phrases) → Claude Code n'a pas de référence de format | Majeur | `data/recipes/*.json`, `data/contracts/*.json`, `data/phrases/*.json` |
| 12 | Processus de production non formalisé (pas de gates, DoR/DoD, sprints, backlog, rituels) | Bloquant | `50_PRODUCTION_PLAN.md` |
| 13 | **Aucun plan QA** : pas de stratégie, de critères d'entrée/sortie, de cas de test, de matrice de machines, de protocole de playtest | Bloquant | `51_QA_TEST_PLAN.md` (Gherkin FR, matrice, réseau, perf, loc, accessibilité, sécurité) |
| 14 | Registre des risques sommaire | Mineur | `52_RISK_REGISTER.md` |
| 15 | Juridique sans textes : pas de politique de confidentialité, d'EULA, d'écran de consentement, de réponses au questionnaire Steam, d'auto-évaluation PEGI, de clauses freelance | Majeur | `60_LEGAL_COMPLIANCE.md` |
| 16 | Marketing sans livrables (page Steam, trailer, personas, programme créateurs, communauté) | Majeur | `70_MARKETING_GTM.md` |
| 17 | Aucun plan post-lancement | Majeur | `71_LIVE_OPS.md` |
| 18 | Playbook Claude Code trop court (2 prompts), pas de templates ADR/PR/issues, pas de stratégie d'agents parallèles | Majeur | `80_CLAUDE_CODE_PLAYBOOK.md` + `.github/` + `docs/adr/` + `CLAUDE.md` v2 |

## 3. Corrections factuelles / techniques
| Sujet | v1 | v2 |
|---|---|---|
| Marqueurs d'enregistrement Steam | « Steam Game Recording » | API **Steam Timeline** via GodotSteam ; disponibilité à vérifier dans la version installée, repli : capture d'écran interne |
| Lecture du chat Twitch | « anonyme » sans détail | Connexion IRC anonyme en lecture seule (méthode courante mais non garantie) ; alternative EventSub avec OAuth du streamer en opt-in ; vérifier les conditions développeur Twitch |
| Départ de l'hôte | non traité | Pas de migration d'hôte en Early Access : fin de session avec récompense partielle et capsule de reprise générée automatiquement |
| Version Godot | « 4.7.2 » | Vérifier la dernière 4.7.x stable au démarrage et **l'épingler** dans `project.godot` et la CI |
| Nom « Century Temps » | retenu | Jeu de mots anglais illisible en français : conservé comme **nom de code** ; 5 candidats publics à vérifier (INPI/EUIPO) |
| Physique vs déterminisme | « figer en fin de manche » | Spécifié : positions quantifiées au centimètre, gel en fin de manche, recettes évaluées sur une grille de 2 m |
| Télémétrie | « désactivée par défaut » | Spécifiée : liste exacte des événements, anonymisation, hébergement UE, écran opt-in |

## 4. Hypothèses encore à valider par l'humain
1. Le fun du prototype « graine → arbre » (aucun document ne remplace un playtest).
2. Les conditions du contrat de travail actuel (exclusivité, propriété intellectuelle, cumul d'activité).
3. Le titre public et sa disponibilité.
4. Le budget réel disponible (3 000 à 7 000 € hors temps) et le temps hebdomadaire (hypothèse : 10 à 15 h).
5. La disponibilité des API dans la version de GodotSteam installée (voix, Timeline, classements).

## 5. Addendum v3 (7 oct. 2026, après demande de réalisme)
| Constat | Correction |
|---|---|
| Le rendu low-poly ne répond pas à l'ambition « 3D réaliste de grande production » | ADR 0012 : Unreal Engine 5.8, `30_ART_BIBLE.md` v2, `33_VISUAL_TARGETS.md`, `40_TECHNICAL_DESIGN.md` v2 |
| Des maquettes générées hors moteur risquaient de tromper l'IA et le public | **Aucune image de jeu dans le dépôt** ; images produites dans le moteur selon `data/shotlist.json` puis validées par un humain |
| Budget et calendrier sous-estimés pour du réalisme | `docs/guides/03_TEMPS_ET_COUTS.md` |
| Cadre juridique insuffisant pour une distribution large | corpus `legal/` (CGU, CGV, confidentialité, AIPD, DSA, mineurs, monnaies virtuelles, accessibilité, éthique) |
