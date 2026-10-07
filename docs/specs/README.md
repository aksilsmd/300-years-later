# docs/specs — le cahier des charges et les exigences

> **EN —** The contractual, testable view of the project: one requirements index over the design dossier, which stays normative.

Ce dossier ne décide rien et n'invente rien. Il **indexe** le dossier de conception
([`docs/design/`](../design/00_README_INDEX.md)) sous la forme d'exigences numérotées, falsifiables et
traçables, pour les lecteurs qui ont besoin d'un engagement plutôt que d'une intention : un client, un
éditeur, un prestataire, une banque, un auditeur, un testeur.

## 1. Les quatre fichiers

| Fichier | Ce qu'il est | Qui le lit |
|---|---|---|
| [`00_CAHIER_DES_CHARGES.md`](00_CAHIER_DES_CHARGES.md) | Objet, périmètre, rôles, objectifs mesurables, contraintes, livrables par phase, jalons, modalités de recette, budget et délais | Client, éditeur, financeur, prestataire, porteur du projet |
| [`10_SPEC_FONCTIONNELLE.md`](10_SPEC_FONCTIONNELLE.md) | Ce que le système **fait**, domaine par domaine, en exigences `EF-…` (MoSCoW) | Qui implémente, qui teste, qui recette |
| [`20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md`](20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md) | Exigences **non fonctionnelles** `ENF-…` : performance, déterminisme, réseau, sécurité, RGPD, accessibilité, localisation, compatibilité, observabilité, maintenabilité, portabilité, conformité plateformes, licences, éthique, durabilité | Qui implémente, QA, juriste, conformité |
| [`30_MATRICE_EXIGENCES.md`](30_MATRICE_EXIGENCES.md) | Matrice de traçabilité exigence → source → moyen de vérification → statut, et la **liste honnête** des exigences encore sans vérification | QA Lead, auditeur, revue de porte |

## 2. La règle de préséance (inchangée)

Ces fichiers **ne sont pas normatifs pour la conception**. En cas de désaccord, l'ordre de
[`AGENTS.md`](../../AGENTS.md) §7 s'applique sans modification :

[`40_TECHNICAL_DESIGN.md`](../design/40_TECHNICAL_DESIGN.md) **>**
`20_GAME_DESIGN_PARAMETERS.md` **>** `GDD_CENTURY_TEMPS.md` **>** le reste du dossier
**>** `docs/specs/`.

Autrement dit : `docs/design/` dit *ce que le jeu est*, `docs/specs/` dit *ce qui est dû et comment on le
vérifie*. Une exigence d'ici qui contredirait un document de conception est un **défaut de ce dossier-ci** :
elle est corrigée ici, et la contradiction est signalée dans [`docs/backlog.md`](../backlog.md) pour que
l'humain tranche. Aucun agent ne modifie `docs/design/`
([`ARCHITECTURE.md`](../../ARCHITECTURE.md), invariant du dossier de conception).

## 3. Comment lire une exigence

```
**EF-VIEIL-03** — Une recette ne s'applique jamais au-delà de 3 sauts d'époque.
*Source :* `20_GAME_DESIGN_PARAMETERS.md §4.3`. *Critère d'acceptation :* <observable>. *Priorité :* MUST.
```

- **Source** — le document et la section de `docs/design/` (ou `data/`) qui porte la décision. Rien ici n'a
  d'autre origine.
- **Critère d'acceptation** — un fait observable, mesurable ou vérifiable par un test. Si on ne peut pas
  l'observer, l'exigence est mal écrite.
- **Priorité** — MoSCoW : **MUST** (sans quoi le jeu n'est pas livrable), **SHOULD** (prévu, sacrifiable
  selon l'ordre de coupe de [`50_PRODUCTION_PLAN.md`](../design/50_PRODUCTION_PLAN.md) §6), **COULD**
  (confort ou après-lancement).
- ***À trancher :*** — là où le dossier de conception est réellement silencieux, l'exigence est écrite comme
  un **point ouvert** et renvoie à [`docs/backlog.md`](../backlog.md). Elle n'est jamais complétée par une
  invention.

## 4. Statut et preuve

Aucune exigence n'est « faite ». Le jeu n'existe pas encore : `game/` est créé en phase P0. Le statut réel,
système par système, est dans [`STUDIO_STATE.md`](../../STUDIO_STATE.md), vérifié par
`python3 tools/validate_state.py`, qui refuse tout statut au-delà de `specified` sans fichier de preuve
présent dans le dépôt. La matrice de ce dossier porte donc `spécifié` partout, et le dira jusqu'à ce qu'un
rapport de test existe.
