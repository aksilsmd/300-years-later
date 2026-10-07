# 21 — Monde et level design
Propriétaire : Product Owner · v1.0

## 1. Principes
1. **Même géographie, quatre habillages** : le terrain (hauteur, eau) est partagé par les époques ; seuls le décor, l'éclairage et les PNJ changent. Les traces vieillies s'insèrent dans des « emplacements » calculés à partir de la grille.
2. **Lisibilité en 3 secondes** : chaque zone a une silhouette unique (Mont = plateau sommital plat, Grotte = bouche ronfleuse, Marais = brume basse, Plateau = moulins/éoliennes).
3. **Tout est cause** : il n'y a pas de décor inerte ; chaque élément a un tag de trace ou une fonction.
4. **Dix graines, dix vallées** : la génération procédurale varie le tracé de la rivière, la position des points d'intérêt et les ressources, jamais les cinq repères.

## 2. Carte de base (400 × 400 m)
```
N
┌──────────────────────────────┐
│  Grotte Qui Ronfle   Plateau │
│      ◠◠◠             des Vents│
│   ~~~~ Brume ~~~~~~~~~~~~~~  │ ← la rivière traverse O→E, tracé procédural
│          Mont Têtu           │
│          ▲▲▲▲ (sommet plat)  │
│   Bourg / Usine / Musée      │ ← « zone bâtie » : évolue selon l'époque
│      Marais Flous            │
└──────────────────────────────┘
S
```
- **Zone bâtie** (centre-sud, 80 × 80 m) : huttes (E0) → bourg + Fort Têtu (E1) → usine + rails (E2) → musée + chantier du parc (E3).
- **Rails** (E2 uniquement) : boucle de 300 m autour de la zone bâtie avec 2 aiguillages.
- **Trésorerie** (E1) : bâtiment fermé à clé, accessible par le toit (secret).
- **Musée de Tout** (E3) : bâtiment extensible : ses ailes apparaissent selon la richesse de la Chronique.

## 3. Points d'intérêt procéduraux (6 à 10 par graine)
| POI | Tag | Ressources | Utilité |
|---|---|---|---|
| Verger sauvage | organic | pommes, graines | nourrir Bouloche |
| Carrière | mineral | pierres, pigment ocre | cairns, pigments |
| Mine de fer (E1+) | metal | objets en fer | trésors, artefacts |
| Marché (E1) | crafted/shiny | cuillères, cloches | pots-de-vin |
| Entrepôt (E2) | crafted | caisses, planches | ponts, construction |
| Dépôt de la Brigade (E3) | anachronism | objets néon | cabine temporelle |
| Socles abandonnés | symbolic | — | statues sans outil |
| Source | liquid | eau | déviations |

## 4. Génération procédurale (déterministe)
1. `SeededRng(seed)` → tracé de la rivière : courbe de Bézier à 5 points dans une bande O→E, largeur 6-10 m.
2. Carte de hauteur : bruit de Perlin (fréquence 0,01, 4 octaves) + masque des cinq repères (Mont : +40 m, Marais : −3 m, Plateau : +15 m).
3. Placement des POI par échantillonnage de Poisson (distance min 35 m), contraintes de zone (verger près de l'eau, carrière sur pente).
4. Décor d'époque : instanciation par chunks de 50 × 50 m autour du joueur local, LOD à 80/160 m.
5. **Validation** : chemin garanti entre toutes les zones (test A* à la génération) ; sinon re-tirage avec `seed+1` (journalisé).

## 5. Emplacements de traces (« slots »)
- Une trace vieillie occupe des cellules selon sa taille (arbre 1×1, forêt 5×5, lac 7×7).
- Si l'emplacement aval est occupé par un bâtiment d'époque, la recette produit la variante « contrariée » (arbre → arbre dans la cour ; lac → quartier inondé = non-conformité +10).
- Les bâtiments d'époque sont eux-mêmes des traces à tag `crafted/protected` pour permettre les contrats « forêt à la place de l'usine » (il faut planter avant la construction, c'est-à-dire en E0/E1).

## 6. Usure des chemins
Chaque cellule compte les passages de joueurs (toutes époques). Seuils : 40 → sentier (E+1), 120 → route (E+2), 300 → tapis roulant (E+3, vitesse +50 %). Les chemins apparaissent **à la pause café** (et pas en direct) pour ne pas distraire.

## 7. Éclairage et météo par époque
| Époque | Heure fixe | Lumière clé | Ambiance | Météo (événements spectateurs) |
|---|---|---|---|---|
| E0 | aube | orange chaud, 20° | brume rose au sol | pluie (croissance ×2) |
| E1 | midi | neutre, 60° | drapeaux, fumées de cheminées | vent (moulins, pigments s'étalent) |
| E2 | crépuscule | ambre, lampes | smog variable | brouillard |
| E3 | nuit pastel | néons, lune | hologrammes | météore (cratère → lac) |

## 8. Métriques de parcours
- Traversée O→E à pied : ~90 s en marchant ; aucun objectif à plus de 60 s d'un autre.
- Points de téléportation : 4 « cabines » fixes (une par repère) utilisables 1 fois par manche (pour les grandes cartes et l'accessibilité).

## 9. Biomes (phase 4 : 2 biomes)
| Biome | Variations | Recettes spécifiques |
|---|---|---|
| Vallée (défaut) | rivière, marais, grotte | toutes |
| Côte (Saison 1) | plage, falaise, marée | sable → dune → forteresse de sable → château ; marée découvre des trésors |

## 10. Checklist de lisibilité (à valider en playtest)
- [ ] Un nouveau joueur nomme les 5 repères après 1 manche.
- [ ] Depuis n'importe quel point, le Mont est visible.
- [ ] Les fantômes d'autres époques sont identifiables (couleur + icône d'époque au-dessus).
- [ ] Toute trace vieillie est **différente de silhouette** de l'objet d'origine (graine ≠ arbre ≠ forêt).
- [ ] Le smog n'empêche jamais de voir le HUD ni les pings.
