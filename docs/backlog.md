# Backlog des propositions
Les agents notent ici toute proposition hors périmètre ou toute modification souhaitée d'un document de design. L'humain tranche. Revue complète : [`reviews/2026-10-07-revue-joueur.md`](reviews/2026-10-07-revue-joueur.md).

| Date | Proposé par | Proposition | Document concerné | Décision |
|---|---|---|---|---|
| 2026-10-07 | conception | Compléter les 5 recettes manquantes (30 visées) dont 10 croisées | data/recipes | à faire en P4 |
| 2026-10-07 | revue joueur | **M1** Schéma de recette mono-entrée : les recettes croisées promises au GDD §3.3 sont inexprimables. Ajouter `input.with` + `outputs[].replaces` | data/schemas/recipe.schema.json, 20 §4 | partiel 2026-10-07 : schéma v2 livré, 4 recettes croisées sur 35 (6 autres sont événementielles, pas croisées). Viser 10 croisées en P4 |
| 2026-10-07 | revue joueur | **M2** Une seule vallée au lancement : variété spatiale par graine, ou une 2e vallée en EA | 21_WORLD_LEVEL_DESIGN | atténué 2026-10-07 (9 civilisations d'arrivée, `13` §1) |
| 2026-10-07 | revue joueur | **M3** Aucun carnet de recettes en jeu : « Chronique des Traces » dans l'Agence, entrées révélées à la découverte | 32_UX_UI_SPEC, 20 §10 | fait 2026-10-07 (Panthéon + carnet, `13` §8) |
| 2026-10-07 | revue joueur | **M4** L'aval n'a qu'un objet par manche vers l'amont : ajouter un canal rétrograde non matériel (note épinglée, zone à protéger) | 20 §7, GDD §3.2 | à trancher |
| 2026-10-07 | revue joueur | **M5** Aucun enjeu de perte : un danger qui efface une trace *désignée comme précieuse*, en restant comique | 20 §8 | fait 2026-10-07 (catastrophes + Figures à protéger, `13` §5) |
| 2026-10-07 | revue joueur | **M6** La vallée est remise à zéro à chaque partie : mode « vallée persistante d'équipe » (le moteur est déjà un journal d'événements) | GDD §2.4, 71_LIVE_OPS | à trancher |
| 2026-10-07 | revue joueur | **M7** Progression sans effet sur le jeu : outils mutuellement exclusifs (3 sur 7) ou variantes débloquées à l'usage | 20 §7, §10 | partiel 2026-10-07 (Serments d'agence, `13` §8) |
| 2026-10-07 | revue joueur | **M8** Valeur solo d'un jeu à 19,99 € : assumer sur la page Steam ou faire du Défi du jour une colonne vertébrale solo | GDD §7.1, 70_MARKETING_GTM | à trancher |
| 2026-10-07 | revue joueur | Contradiction assumée à écrire : l'étude §1.2 recommande ≤ 10 € et des graphismes modestes ; le projet choisit le photoréalisme à 19,99 € | GDD §0, ADR 0012 | fait 2026-10-07 (encadré GDD §0) |
| 2026-10-07 | revue joueur | Incohérences mineures : « 2-4 » vs « 1-4 » ; durée du Solo Relais ; rotation qui ne couvre que 3 époques ; départage des recettes par ordre de fichier | GDD §3.1, 20 §1 et §4.3, 12 §6 | partiel 2026-10-07 (1-4 joueurs, départage des recettes) |
| 2026-10-07 | revue joueur | Questions ouvertes : appariement sans amis, rejoindre en cours, crossplay, anti-triche (ADR 0020) vs classement, migration des capsules, confort (cinématique café, caméra musée), modération des noms votés | 12, 32, 40, 60 | à instruire |
| 2026-10-07 | spécification | Steam Deck : `50` §2 et `51` §6 exigent 60 i/s, `40` §10 (normatif) dit 800p 30 i/s « jouable visé ». Les trois ne peuvent pas tenir | 40, 50, 51 | à trancher |
| 2026-10-07 | spécification | `51` §1 référence `tools/run_local_4p.sh --bot`, qui n'existe pas ; 14 exigences réseau s'y appuient | 51, tools/ | à corriger |
| 2026-10-07 | spécification | `51` n'a aucune famille de tests audio alors que `31` §7 y renvoie ; 5 exigences sans vérification | 31, 51 | à corriger |
| 2026-10-07 | spécification | Aucun contrôle ne vérifie l'invariant « aucune valeur de gameplay en dur » (ARCHITECTURE.md) : un script d'analyse statique serait l'outil manquant le plus utile | tools/ | à faire |
| 2026-10-07 | spécification | C15 et C16 existent dans `data/contracts/` mais dans aucun document de conception ; `12` §2 et `71` §2 annoncent 12 contrats, il y en a 16 | 12, 13, 71 | à corriger |
| 2026-10-07 | spécification | `13` §11 affirme « la Ferveur n'est récompensée que dans 2 cas sur 14 » : les données en comptent 4 sur 16 | 13 | à corriger |
| 2026-10-07 | spécification | Chemins référencés mais absents : `docs/originalite.md` (GDD §1.4), `docs/DEPENDENCIES.md` (40 §13), `docs/privacy/registre.md` (GDD §6.1), `docs/store/presskit.md` (70 §5) | GDD, 40, 70 | à corriger |
