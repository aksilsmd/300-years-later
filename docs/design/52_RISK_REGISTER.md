# 52 — Registre des risques
Propriétaire : Product Owner · Revue à chaque fin de sprint. Probabilité (P) et Impact (I) de 1 à 5 ; Criticité = P × I.

| ID | Risque | Catégorie | P | I | C | Réponse | Action / déclencheur | Propriétaire |
|---|---|---|---|---|---|---|---|---|
| R01 | Le cœur (vieillissement) n'est pas assez drôle | Design | 3 | 5 | 15 | Réduire | Gate G1 stricte ; 2 itérations max puis pivot | Porteur du projet |
| R02 | La propagation devient illisible (trop de changements) | Design | 3 | 4 | 12 | Réduire | Notifications limitées, sablier, recettes ≤ 3 sauts, playtest lisibilité | Porteur du projet |
| R03 | Désynchronisation réseau | Tech | 3 | 5 | 15 | Réduire | Event sourcing, hash 5 s, golden tests, resync | Claude Code |
| R04 | Complexité d'Unreal (C++, compilation, contenu lourd) pour un agent IA | Tech | 3 | 4 | 12 | Réduire | Plugin MCP officiel Epic, petites PR, revue humaine, runner Windows dédié | Claude Code |
| R05 | Performances du rendu réaliste sur config minimale/Deck | Tech | 3 | 4 | 12 | Réduire | Lumen Medium, scalabilité, budgets dès P4, Insights hebdo | Claude Code |
| R06 | Dérive du périmètre | Production | 4 | 4 | 16 | Réduire | Ordre de coupe (50 §6), DoR, phases verrouillées | Porteur du projet |
| R07 | Manque de temps (projet à temps partiel) | Production | 4 | 4 | 16 | Accepter/réduire | Calendrier avec 20 % de marge ; sprints réalistes | Porteur du projet |
| R08 | Clause d'exclusivité / PI d'un éventuel contrat de travail | Juridique | 2 | 5 | 10 | Éviter | Lecture du contrat et demande écrite à l'employeur avant G3 | Porteur du projet |
| R09 | Nom indisponible ou litige de marque | Juridique | 3 | 4 | 12 | Éviter | Recherche INPI/EUIPO avant annonce ; dépôt | Porteur du projet |
| R10 | Contenu tiers non licencié introduit par erreur | Juridique | 2 | 4 | 8 | Éviter | `license_audit.py` bloquant en CI | Claude Code |
| R11 | Non-conformité RGPD (télémétrie, Twitch) | Juridique | 2 | 4 | 8 | Éviter | Opt-in, no-op par défaut, revue juriste G5 | Porteur du projet |
| R12 | Rejet de l'IA par les joueurs (perception) | Marché | 2 | 3 | 6 | Réduire | Aucun contenu livré généré par IA ; transparence sur le code | Porteur du projet |
| R13 | Concept copié après les premiers clips | Marché | 3 | 3 | 9 | Accepter | Vitesse, profondeur du moteur, communauté | Porteur du projet |
| R14 | Visibilité insuffisante (wishlists) | Marché | 4 | 5 | 20 | Réduire | Clips hebdo dès G3, créateurs, Next Fest, capsule pro | Porteur du projet |
| R15 | Abus (pseudos, statues obscènes, harcèlement vocal) | Communauté | 3 | 3 | 9 | Réduire | Amis par défaut, mute/blocage, filtre, signalement, poses prédéfinies uniquement | Claude Code |
| R16 | Méthode Twitch anonyme indisponible | Tech | 2 | 2 | 4 | Contourner | Repli EventSub OAuth opt-in ; mode streamer coupé en dernier recours | Claude Code |
| R17 | Dépendance aux freelances (retards) | Production | 3 | 2 | 6 | Réduire | Commandes à G3/G4, jalons contractuels, placeholders procéduraux | Porteur du projet |
| R18 | Perte de code / données | Tech | 1 | 5 | 5 | Éviter | GitHub + sauvegarde locale hebdomadaire | Porteur du projet |

| R19 | Budget du réalisme (assets Fab, artistes, capture) sous-estimé | Production | 4 | 5 | 20 | Réduire | Budget par porte, achats après G3, coupe de périmètre (50 §6) | Porteur du projet |
| R20 | Fuite d'assets sous licence dans le dépôt public | Juridique | 2 | 5 | 10 | Éviter | `Content/` privé, `.gitignore`, privacy_scan + revue avant push | Claude Code |
| R21 | « Vallée de l'étrange » des humains réalistes nuisant à l'humour | Design | 3 | 3 | 9 | Réduire | Tenues lisibles, animation faciale capturée, playtests G3 | Porteur du projet |

**Top 3 à surveiller :** R14 (visibilité), R06/R07 (périmètre/temps), R01/R03 (fun et désync).
