# Decision log / Journal des décisions

> EN — Every decision the AI takes on its own (autonomous mode) is logged here so the human can review or reverse it. Irreversible decisions are never taken autonomously.
> FR — Chaque décision prise seule par l'IA (mode autonome) est notée ici pour que l'humain puisse la relire ou l'annuler. Les décisions irréversibles ne sont jamais prises seule.

| Date | Step / Étape | Decision / Décision | Alternatives | Reason / Raison | Reversible? |
|---|---|---|---|---|---|
| 2026-10-07 | G0 | Unreal Engine 5.8 instead of Godot (ADR 0012) | Godot 4, Unity 6 | realistic AAA target requested | yes, before P0 |
| 2026-10-08 | G0 | Public title **Afterloom** applied repository-wide (ADR 0021), by the owner's instruction | keep "300 Years Later", CENTURY TEMPS, TEMPORIS, PATINA, BRUMECOMBE | invented word: no search collision, registrable, says what the game is in one word | yes — `tools/apply_public_title.py --to "300 Years Later"` |
| 2026-10-08 | G0 | Repository slug `300-years-later` and the licence attribution entity "The 300 Years Later contributors" left unchanged | rename both with the title | the slug carries the plugin path, the badges and every shared link; the attribution entity is who the two licences grant from | n/a — nothing was changed |
| 2026-10-07 | design | Le Product Owner a demandé explicitement d'enrichir la conception (peuples, civilisations, dieux, prophètes, religions, météo, catastrophes, phénomènes). Les documents de `docs/design/` ont donc été **modifiés directement**, par exception à la règle « un agent ne modifie jamais un document de design » (`AGENTS.md` §5.8) : le message de l'utilisateur prime sur cette règle, seul le contrat de sécurité est absolu. | déposer la proposition dans `docs/backlog.md` et attendre | demande directe du propriétaire du produit, qui est l'autorité sur la conception | oui — `git revert` du commit |
| 2026-10-07 | design | Garde-fou de `10_NARRATIVE_BIBLE.md` §10 remplacé : « jamais de vocabulaire religieux » devient « fiction intégrale, vocabulaire inventé de la vallée, satire des institutions et jamais des croyants, aucune violence de croyance, PEGI 7-12 » (`13` §0) | garder l'interdiction totale et refuser la demande | la demande est légitime ; l'intention protectrice de la règle est conservée et rendue plus précise | oui |
| 2026-10-07 | data | Schéma de recette v2 : `input.with` (recettes croisées), `priority` explicite, `faith`. Départage par `priority` puis identifiant alphabétique, plus jamais par l'ordre du fichier | laisser le schéma mono-entrée | sans recettes croisées, la promesse de combinatoire du GDD §3.3 est inexprimable (revue joueur M1) | oui |

