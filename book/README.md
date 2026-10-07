# `book/` — le roman

> **EN —** The prose of *Le Livre des Traces*, the founding novel. Its **plan** — premise, theme, five
> parts, forty chapter synopses, character arcs, plant-and-payoff table — is normative and lives in
> [`docs/design/14_ROMAN_LIVRE_DES_TRACES.md`](../docs/design/14_ROMAN_LIVRE_DES_TRACES.md). This folder
> holds the chapters that have actually been written.

## Où en est le texte

| Partie | Époque | Chapitres | État |
|---|---|---|---|
| **I — Ce qui tombe** | an 0 | 1 à 8 | **rédigée** — `book/fr/`, ≈ 10 400 mots |
| II — Ce qui s'écrit | an 300 | 9 à 17 | planifiée, non rédigée |
| III — Ce qui se fabrique | an 600 | 18 à 28 | planifiée, non rédigée |
| IV — Ce qui se range | an 900 | 29 à 38 | planifiée, non rédigée |
| V — Ce qui tient | les quatre | 39, 40, épilogue | planifiée, non rédigée |

Le plan vise ≈ 95 000 mots pour 340 à 400 pages imprimées. Ce qui existe aujourd'hui en représente
environ un neuvième. **Aucun outil de ce dépôt n'affiche un chapitre qui n'est pas écrit** : le PDF et la
liseuse se contentent de ce qui est dans `book/<langue>/`, et le disent en toutes lettres.

## Un fichier par chapitre

```
book/fr/I-02-la-chose-plantee.md
---
part: 1            # numéro de partie
chapter: 2         # numéro de chapitre, sert au tri et au sommaire
voice: Ourse       # une seule voix par chapitre (règle de fer, 14 §2)
place: Clairière du Mont
title: La Chose Plantée
kind: veille       # facultatif : marque un chapitre de la voix-cadre
---
```

Le corps est du Markdown volontairement pauvre : des paragraphes séparés par une ligne vide, `*` seul sur
sa ligne pour un changement de scène, `*italique*` et `**gras**`. Rien d'autre n'est interprété — un
manuscrit n'a pas besoin de titres de niveau trois ni de tableaux.

Ajouter un chapitre, c'est ajouter un fichier. Les deux outils le prennent sans configuration.

## Produire le livre

```bash
python3 tools/build_book_pdf.py         # → book/build/livre-des-traces-fr.pdf
python3 tools/build_book_reader.py      # → book/build/liseuse-fr.html
```

Le **PDF** est composé au format 148 × 210 mm avec couverture, faux-titre, page de droits, sommaire,
ouverture de partie et folios. Les couleurs et la typographie viennent de `design-system/tokens.json`.

La **liseuse** est une page autonome : elle pagine le texte à l'exécution contre la vraie boîte de page,
donc elle se recompose quand la fenêtre change au lieu d'être figée à la construction. Les pages se
tournent en 3D — flèches, clic sur le bord, ou attraper le coin et tirer. `prefers-reduced-motion`
supprime l'animation. Aucune police, aucun script et aucune feuille de style distante : le fichier
s'ouvre hors ligne, et le script de construction échoue s'il trouve une URL externe.

`book/build/` n'est pas suivi par Git : ce sont des artefacts, régénérés par les deux commandes.

## Licence et garde-fous

Texte sous **CC BY 4.0**, comme le reste des contenus ; créditez « The 300 Years Later contributors ».
Les garde-fous de [`13` §0](../docs/design/13_PEUPLES_DIEUX_ET_PHENOMENES.md) s'appliquent intégralement :
peuples, croyances, figures et lieux sont entièrement inventés, aucune religion, culture, organisation ou
personne réelle n'est représentée, aucune violence de croyance, cible PEGI 7-12.

`14` §11 fixe aussi la règle d'écriture assistée : brouillons autorisés, livraison sans relecture humaine
interdite, et transparence IA selon `60_LEGAL_COMPLIANCE.md` pour tout texte qui entre dans le jeu.
