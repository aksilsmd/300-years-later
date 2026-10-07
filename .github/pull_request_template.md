## Quoi et pourquoi
Ticket : #
Référence design : docs/XX §Y

## Definition of Done
- [ ] Tests ajoutés/à jour et verts (Automation Spec / Functional Tests / Gauntlet)
- [ ] Aucun fichier de `Content/` ni asset Epic/Fab/MetaHuman dans ce dépôt public
- [ ] `gdlint` / `gdformat --check` verts
- [ ] `tools/validate_data.py` et `tools/license_audit.py` verts
- [ ] Aucune valeur de gameplay en dur (tout dans `data/`)
- [ ] Déterminisme respecté (pas de randi/randf/heure/float non quantifié dans le cœur temporel)
- [ ] Chaînes joueur localisables (`FText`, tables de chaînes) + clés FR/EN ajoutées
- [ ] Aucune donnée personnelle collectée, stockée ou journalisée
- [ ] `CHANGELOG.md` et `docs/architecture.md` (ou ADR) à jour
- [ ] Build jouée 5 minutes sans régression

## Comment tester (pour l'humain)
1.

## Risques / points d'attention
