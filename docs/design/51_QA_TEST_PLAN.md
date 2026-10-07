# 51 — Plan de test et assurance qualité
Propriétaire : QA Lead · v1.0 · Référentiels : ISTQB (vocabulaire), ISO/IEC/IEEE 29119 (structure), checklists de certification Steam Deck, Game Accessibility Guidelines.

## 1. Stratégie
| Niveau | Quoi | Outil | Qui | Quand |
|---|---|---|---|---|
| Unitaire | Propagator, recettes, RNG, ActionLog, capsule, score, paradoxes | Automation Spec (C++) | Claude Code | chaque PR |
| Intégration | Recettes chaînées, contrats, simulation des époques vides | Functional Tests (cartes de test, -nullrhi) | Claude Code | chaque PR |
| Réseau | 1 hôte + 3 clients ENet, hash identique | script headless `tools/run_local_4p.sh --bot` | CI | chaque PR (version courte), nightly (longue) |
| Golden | graine + journal → hash attendu | Automation Spec | CI | chaque PR |
| Multi-clients / charge | 4 clients, 8 sessions parallèles, bots | Gauntlet | CI nightly | nightly |
| Rendu / visuel | conformité des plans à `33_VISUAL_TARGETS.md`, régressions visuelles | captures automatisées + revue humaine | QA Lead | fin de phase |
| Performance | propagation ×1 000, fps Deck | test perf + profiler | CI + QA Lead | nightly + fin de phase |
| Système | parcours joueur complets | campagnes manuelles (Gherkin) | QA Lead | fin de phase |
| Exploratoire | sessions chronométrées de 45 min, charte par thème | — | QA Lead + testeurs | chaque sprint |
| Playtest | fun, compréhension, rétention | protocole §7 | 5-12 personnes | gates |
| Conformité | RGPD, licences, accessibilité, Steam | checklists §9 | QA Lead + juriste | G5, G6 |
| Localisation | pseudo-loc, débordements, polices CJK | §8 | QA Lead + traducteurs | G5 |

**Gestion des anomalies :** GitHub Issues avec template `bug_report.md` ; sévérité (S1 crash/désync/perte de données/conformité, S2 fonction cassée, S3 gêne, S4 cosmétique) × priorité (P0-P3). Cycle : Nouveau → Confirmé → En cours → Corrigé → Vérifié → Fermé. Chaque S1/S2 corrigé reçoit un test de non-régression.

## 2. Critères d'entrée / sortie par campagne
- **Entrée :** build CI verte, notes de version, environnement de test prêt (2 PC + Deck).
- **Sortie (fin de phase) :** 100 % des cas P0/P1 exécutés, 0 S1 ouvert, ≤ 3 S2 ouverts avec contournement, taux de réussite ≥ 95 %.
- **Sortie (G6) :** 0 S1, 0 S2, ≤ 10 S3 ; 2 h de session à 4 sans crash ; perf conforme au TDD §12.

## 3. Cas de test d'acceptation (Gherkin, extrait — à compléter par phase dans `tests/acceptance/*.feature`)
```gherkin
# language: fr
Fonctionnalité: Vieillissement d'une graine

  Scénario: Une graine plantée en l'an 0 devient un arbre en l'an 300
    Étant donné une partie avec la graine de monde 42
    Et un joueur en époque 0 sur une cellule ensoleillée loin de l'eau
    Quand il plante une graine
    Alors l'époque 1 contient une entité "tree" dont l'origine est cette graine
    Et l'arbre apparaît visuellement en moins de 0,5 seconde
    Et la notification "Votre graine (an 0) est devenue un arbre (an 300)" s'affiche

  Scénario: Une graine dans la grotte ne pousse pas
    Étant donné un joueur en époque 0 dans la Grotte Qui Ronfle
    Quand il plante une graine
    Alors les époques 1 et 2 ne contiennent aucune entité dérivée
    Et l'époque 3 contient une entité "fossil_seed"

  Scénario: Déterminisme sur deux machines
    Étant donné deux clients avec la graine 42 et le même journal de 200 actions
    Quand chaque client rejoue le journal
    Alors les hachages des 4 époques sont identiques sur les deux clients

Fonctionnalité: Non-conformités

  Scénario: Modifier en amont une trace revendiquée en aval
    Étant donné un arbre en époque 1 issu d'une graine de l'époque 0
    Et un joueur en époque 1 qui a gravé l'arbre (trace revendiquée)
    Quand le joueur en époque 0 arrache la graine
    Alors la jauge de non-conformité augmente de 25
    Et l'arbre de l'époque 1 clignote 3 secondes puis disparaît

  Scénario: Effondrement
    Étant donné une jauge de non-conformité à 95
    Quand une non-conformité mineure survient
    Alors la partie se termine en Effondrement
    Et chaque joueur reçoit 50 % des Chronos acquis
    Et le musée affiche "Cette aile est fermée pour cause d'Effondrement"

Fonctionnalité: Réseau et sécurité

  Scénario: L'hôte rejette une action hors de portée
    Étant donné un client à 10 mètres d'une pierre
    Quand il envoie une requête de ramassage de cette pierre
    Alors l'hôte rejette la requête
    Et aucune action n'est ajoutée au journal

  Scénario: Départ de l'hôte
    Étant donné une partie à 3 joueurs en manche 2
    Quand l'hôte quitte la partie
    Alors chaque client affiche "L'hôte a quitté la mission"
    Et chaque client reçoit un code capsule de reprise valide

Fonctionnalité: Confidentialité

  Scénario: Premier lancement
    Étant donné un profil vierge
    Quand le jeu démarre
    Alors l'écran de consentement s'affiche avant le menu
    Et les deux boutons ont la même taille et le même style
    Et aucune donnée de télémétrie n'est envoyée tant qu'aucun choix n'est fait

  Scénario: La voix n'est jamais écrite sur disque
    Étant donné une session de 10 minutes avec voix active
    Quand on inspecte le dossier user:// et les journaux
    Alors aucun fichier audio ni aucune donnée vocale n'est présent

  Scénario: Le code capsule ne contient pas de donnée personnelle
    Étant donné une partie jouée par des joueurs nommés "Alex" et "Noa"
    Quand un code capsule est généré puis décodé
    Alors le contenu décodé ne contient ni pseudo, ni SteamID
```

## 4. Matrice de configuration
| Config | OS | GPU | RAM | Contrôle | Priorité |
|---|---|---|---|---|---|
| A — Dev | Windows 11 | GPU dédié milieu de gamme | 16 Go | clavier/souris + manette Xbox | P0 |
| B — Deck | SteamOS (Steam Deck) | APU | 16 Go | contrôles intégrés | P0 |
| C — Min | Windows 10 | GTX 1050 / iGPU récent | 8 Go | clavier/souris | P1 |
| D — Linux | Ubuntu LTS | AMD | 16 Go | manette PlayStation | P2 |
| Réseau | même LAN ; 2 réseaux différents ; 4G partagée (latence 80-150 ms) ; perte simulée 2 % (outil `clumsy`/`tc netem`) | | | | P0 |

## 5. Tests réseau spécifiques
- Latence 0 / 100 / 250 ms, perte 0 / 2 / 5 %, gigue 30 ms : pas de désync, actions confirmées < 400 ms à 250 ms.
- Déconnexion/reconnexion d'un client en pleine manche ; départ de l'hôte ; 4 joueurs qui agissent sur la même cellule au même tick.
- Fuzzing : 10 000 RPC aléatoires/malformés → aucun crash, rejets comptés, kick à 20/min.
- Bande passante mesurée < 30 ko/s moyen.

## 6. Performance
- Scène de stress : 2 000 traces par époque, 4 joueurs, smog, 6 Chronomites → 60 fps Deck.
- Propagation : 1 000 actions aléatoires, p95 < 2 ms.
- Mémoire stable sur 2 h (fuite < 50 Mo).
- Chargement partie < 8 s.

## 7. Protocole de playtest
- **Recrutement :** 5 (G1) à 12 (G3) personnes, mélange joueurs/non-joueurs, groupes d'amis réels (le jeu est social).
- **Consentement :** formulaire écrit (finalité, enregistrement écran/voix optionnel, durée de conservation 3 mois, droit de retrait). Aucun mineur sans autorisation parentale écrite.
- **Déroulé :** aucune explication → 20 min de jeu → questionnaire (5 min) → entretien (10 min).
- **Observation :** grille horodatée : temps au « aha », moments de rire, confusions, abandons.
- **Questionnaire (1-5) :** « J'ai compris le lien entre les époques », « Je me suis amusé », « Je rejouerais », « Je montrerais ce jeu à un ami », « Le jeu m'a fait rire » + 3 questions ouvertes (moment préféré, moment frustrant, ce qui manque).
- **Seuils :** voir `50_PRODUCTION_PLAN.md` §2.

## 8. Localisation
- Pseudo-localisation automatique (`[!!! Ţéxţé àççéñţûé ~30 % !!!]`) pour détecter textes en dur et débordements.
- Vérification de chaque écran à 200 % de taille de texte et en JA/ZH (polices).
- Contrôle des placeholders `{PLAYER}` etc. par script (même ensemble dans chaque langue).

## 9. Checklists de conformité (extraits)
**RGPD :** écran de consentement ; télémétrie no-op sans consentement (test) ; bouton suppression des données locales ; politique accessible depuis le menu ; registre des traitements à jour.
**Licences :** `license_audit.py` vert ; `THIRD_PARTY_LICENSES.md` affiché dans Crédits ; contrats de cession signés (musique, illustration).
**Accessibilité :** toutes les options de `32_UX_UI_SPEC.md` §6 présentes et fonctionnelles ; jeu terminable sans micro, sans son et en mode daltonien.
**Steam :** succès déclenchables ; Cloud fonctionnel ; Deck : textes ≥ 9 px à 1280×800, contrôles natifs, pas de lanceur externe ; questionnaire de contenu et IA rempli.
**Sécurité :** aucun texte libre non filtré ; validation de toutes les RPC ; aucune IP exposée (relais Steam).

## 10. Rapports
- Rapport de campagne (fin de phase) : périmètre, exécutés/réussis/échoués/bloqués, anomalies par sévérité, risques résiduels, recommandation go/no-go.
- Tableau de bord QA dans `docs/qa/` (un fichier par gate).
