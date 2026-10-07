# 20 — Design détaillé et paramètres de réglage
Propriétaire : Product Owner · v1.0 · Toutes les valeurs sont des **valeurs initiales** exposées dans `data/tuning.json` et modifiables sans recompilation. Aucune valeur de gameplay en dur dans le code.

## 1. Structure d'une partie
| Paramètre | Valeur | Note |
|---|---|---|
| Manches par partie | 3 (Solo Relais : 4) | Mode Défi : 3 |
| Durée d'une manche | 300 s (Solo : 240 s) | Avertissements à 60 s et 10 s |
| Pause café | 30 s | 10 s cinématique siècles + 15 s vote/rotation + 5 s compte à rebours |
| Rotation | +1 époque par joueur (E3 → E0) | Option lobby : « pas de rotation » |
| Visite du musée | 120 s max, skippable à l'unanimité | |
| Durée totale cible | 15-20 min | Mesurée par télémétrie opt-in |

## 2. Joueur
| Paramètre | Valeur |
|---|---|
| Vitesse marche / course | 4,5 m/s / 7,5 m/s |
| Endurance course | 6 s, régénération 4 s |
| Saut | 1,2 m ; pas de double saut |
| Rayon d'interaction | 2,5 m ; cône 90° |
| Inventaire | 3 emplacements petits objets + 1 objet lourd porté à deux mains (vitesse ×0,7) |
| Objets lourds à deux joueurs | Tronc, menhir, Bouloche bébé : portés à deux (vitesse ×0,5), un seul joueur = traîné (×0,3) |
| Temps de creusage | 1,5 s par cellule (grille 2 m) ; profondeur max 3 cellules |
| Temps de plantation | 0,5 s |
| Collision entre joueurs | Désactivée (anti-griefing) ; les fantômes n'ont pas de physique |
| Chute | Pas de dégâts ; étourdissement 1,5 s si > 6 m (comique) |
| Points de vie | Aucun. Les dangers **étourdissent** (2 s) ou **confisquent**, jamais ne tuent |

## 3. Grille et monde
| Paramètre | Valeur |
|---|---|
| Taille de la vallée | 400 × 400 m, grille de cellules de 2 m (200 × 200 = 40 000 cellules) |
| Hauteur de terrain | Carte de hauteur 8 bits par cellule, modifiable (creuser/remblayer) ; pente max marchable 35° |
| Eau | Simulation cellulaire simple : niveau par cellule, écoulement vers le voisin le plus bas, mise à jour 4 Hz, déterministe (ordre de parcours fixe) |
| Zones | Rivière, Mont, Grotte, Plateau, Marais + 6 à 10 points d'intérêt procéduraux |
| Capacité de traces | 2 000 entités persistantes par époque (budget) |

## 4. Le moteur de vieillissement
### 4.1 Tags de trace
`organic`, `mineral`, `metal`, `crafted`, `living`, `symbolic`, `liquid`, `fire`, `anachronism`, `protected` (ancre/grotte).

### 4.2 Conditions d'environnement évaluées sur la grille (cellule + voisinage 1 à 3)
`near_water(r)`, `in_cave`, `in_marsh`, `on_plateau`, `altitude`, `count_tag(tag, r)`, `has_path_wear(n)`, `near_rail(r)` (E2), `near_museum(r)` (E3), `sunlight` (non-cave), `era`.

### 4.3 Recettes de l'Early Access (30) — extrait des principales avec paramètres
| Id | Entrée | Condition | +1 saut | +2 sauts | +3 sauts |
|---|---|---|---|---|---|
| seed | Graine | défaut | Arbre (h 6 m, bloque) | Grand arbre (h 10 m, porte) | Arbre millénaire (symbolique, fan-club) |
| seed_water | Graine | `near_water(2)` | Bosquet 3×3 | Forêt 5×5 | Réserve naturelle (zone protégée) |
| seed_marsh | Graine | `in_marsh` | Forêt 5×5 | Jungle 7×7 | Marais sacré |
| seed_cave | Graine | `in_cave` | Graine (inchangée) | Graine | Graine fossile (musée) |
| stones | Pile ≥ 3 pierres | défaut | Cairn | Monument (fan-club 5) | Site touristique (boutique, score) |
| stones_summit | Pile ≥ 5 pierres | `altitude > 80 %` | Cairn | **Grand monument** | Phare néon |
| trench | Tranchée (≥ 3 cellules reliées) | `near_water(3)` | Ruisseau | Rivière | Canyon (bloque, pont requis) |
| trench_dry | Tranchée | sinon | Fossé | Fossé effondré | Vallon |
| dam | Barrage (branches ≥ 4 sur l'eau) | — | Étang (3×3) | Lac (7×7) | Station balnéaire |
| pose | Pose sur socle | — | Statue (pose capturée) | Statue érodée + légende | Statue géante néon |
| pose_duck | Pose « canard » | — | Statue canard | Fan-club du Canard (10) | Mascotte |
| metal | Objet en fer | défaut | Rouille | Ferraille | Artefact de musée |
| metal_cave | Objet en fer | `in_cave` | Intact | Intact | Artefact « miraculeux » (score ×2) |
| coins_buried | Pièces enterrées | profondeur ≥ 1 | Trésor | Trésor + carte (PNJ) | Fouille archéologique |
| shiny_public | Objet brillant posé | E1, zone publique | Confisqué → Trésorerie | Trésor du Baron | Collection privée |
| animals_pair | 2 animaux même espèce | `count_tag(living,4) ≥ 2` | Troupeau (6) | Race domestiquée (10) | Mascotte de la ville |
| fire | Feu laissé | — | Zone brûlée (5×5) | Sol fertile (croissance ×2) | Champ |
| fire_near_hut | Feu | `count_tag(crafted,3) ≥ 1` | Hutte brûlée + rancune des Voisins | Ruine | Ruine « romantique » (score) |
| graffiti | Gravure | — | Inscription ancienne | Texte « sacré » mal traduit | Plaque officielle |
| trash | ≥ 5 déchets | — | Décharge | Couche fossile | Mine (ressources) |
| path_wear | ≥ 40 passages sur une cellule | — | Sentier | Route pavée | Tapis roulant |
| logs_rail | Troncs | E2, `near_rail(2)` | Planches (immédiat, Automate) | Pont si au-dessus d'un ruisseau/canyon | — |
| pigment | Pigment appliqué | — | Couleur délavée 50 % | Couleur « traditionnelle » (score) | Couleur protégée |
| anachronism | Objet d'une époque future | `era < origin` | Fan-club (5) | Religion techno → **fan-club géant** | Paradoxe latent (+10 jauge) |
| protected | Tout objet avec ancre | — | Inchangé | Inchangé | Inchangé |

Règle de **combinaison** : si plusieurs recettes s'appliquent, la plus spécifique (plus de conditions) gagne ; égalité → ordre du fichier. Chaque résultat peut avoir des **variantes pondérées** (ex. arbre : chêne 50 %, pin 30 %, arbre-canard 20 %) tirées au `SeededRng(seed, entity_id, hop)`.

### 4.4 Vitesse d'apparition
La propagation est calculée instantanément ; **l'apparition visuelle** dans l'époque aval prend 0,4 s (animation « pousse ») pour la lisibilité, avec un son dédié.

## 5. Paradoxes (non-conformités)
| Paramètre | Valeur |
|---|---|
| Jauge d'équipe | 0 à 100 |
| Modification aval d'une trace héritée | marque la trace « revendiquée » par l'aval |
| Changement amont d'une trace revendiquée | +15 (mineure), +25 (majeure : destruction) |
| Anachronisme sans certificat | +5 par pause café |
| Décroissance | −1 par seconde quand aucune non-conformité active |
| Chronomites | apparaissent à 50 (3), 75 (6) ; chaque Chronomite ronge une trace aléatoire (déterministe) par 20 s ; se chassent avec la corne (cooldown 10 s) ou en « réparant » la contradiction |
| Effondrement | 100 → fin de partie, 50 % des Chronos |
| Saboteur | Clé à paradoxe : +20, cooldown 60 s, 3 charges |
| Vote raté (Saboteur) | +10 |

## 6. Contrats et score
| Élément | Points |
|---|---|
| Objectif principal | 60 |
| Solution alternative (même type dans 30 m) | 36 |
| Bonus 1 et 2 | 15 chacun |
| Exigence absurde | 10 |
| Richesse du musée | +1 par trace distincte exposée (max 20) |
| Pénalité paradoxe | −0,2 × valeur max atteinte de la jauge |
| Effondrement | score plafonné à 40 |

Étoiles : ≥ 90 → 5 ; 75 → 4 ; 55 → 3 ; 35 → 2 ; sinon 1.
Chronos : 20 × étoiles + 2 × richesse ; première victoire 5 étoiles du jour ×2.

## 7. Outils
| Outil | Prix (Chronos) | Chapitre | Paramètres |
|---|---|---|---|
| Pelle | gratuit | 1 | 1,5 s/cellule |
| Pistolet à graines | gratuit | 1 | portée 15 m, 1 graine / 0,8 s, 20 graines/manche |
| Socle de statue | gratuit | 1 | 1 par joueur par manche ; capture de pose 2 s |
| Corne d'appel | 150 | 2 | attire animaux dans 20 m ; chasse Chronomites ; cooldown 10 s |
| Cabine temporelle | 300 | 2 | 1 objet par manche vers n'importe quelle époque ; crée un anachronisme |
| Ancre temporelle | 250 | 3 | 2 charges/partie ; l'objet ancré ignore les recettes |
| Sablier de poche | 200 | 3 | aperçu fantôme du +1 saut pendant 5 s ; cooldown 20 s |
| Faux certificat | 100 | 3 | neutralise la Brigade sur 1 anachronisme |
| Pigments (3 couleurs) | 50 | 1 | 10 applications |
| Clé à paradoxe | — | Saboteur | 3 charges |

## 8. Dangers (machines à états)
| Danger | Époque | Détection | Action | Contre-mesure | Vitesse |
|---|---|---|---|---|---|
| Bouloche | E0 | trace `organic` à moins de 25 m | marche, mange (3 s), repart ; 1 pousse / 12 s | pommes (3 → suit le joueur 60 s ; 10 → domestiqué) | 3 m/s |
| Sire Fiscalin | E1 | objet `shiny`/`crafted` en zone publique > 10 s | se téléporte à 20 m, marche, confisque | objet brillant posé devant lui (pot-de-vin) ; enterrer | 3,5 m/s |
| Automates | E2 | objet à moins de 4 m des rails | traite l'objet (2 s) selon table de transformation | lever le levier d'aiguillage ; valves | 4 m/s sur rails |
| Smog | E2 | Bouilloire > 80 % | visibilité 15 m pendant 40 s | 2 valves à tourner (3 s chacune) | — |
| Brigade Propreté | E3 | anachronisme sans certificat | scanne 5 s puis recycle | faux certificat ; cacher dans la grotte | 6 m/s (vol) |
| Chronomites | toutes | jauge ≥ 50 | ronge 1 trace / 20 s | corne, réparation | 2 m/s |
| Touristes | E3 | statue/monument | selfies : +1 richesse par 3 touristes | — | 2 m/s |

## 9. Voix et communication
| Paramètre | Valeur |
|---|---|
| Voix de proximité inter-époques | même position (X/Z) : claire ≤ 8 m ; 8-25 m : passe-bas 1,2 kHz + −9 dB ; > 25 m : « radio ancienne » (passe-bande 400-2 500 Hz, −15 dB) |
| Même époque | atténuation 3D standard, portée 30 m |
| Détection de voix | seuil −45 dBFS, push-to-talk optionnel (défaut : activation vocale) |
| Pings | roue de 6 pings (ici, danger, objet, eau, aide, bravo) ; visibles dans toutes les époques 8 s |
| Emotes | 8 ; texte rapide : 12 phrases prédéfinies localisées |
| Lèvres | amplitude vocale → bouche (3 états) |

## 10. Progression et économie
| Rang | Chronos cumulés | Débloque |
|---|---|---|
| Stagiaire | 0 | Tutoriel, chapeau de base |
| Intérimaire | 200 | Chapitre 2, 3 chapeaux |
| Titulaire du Bail | 800 | Chapitre 3, couleurs |
| Chef d'équipe | 2 000 | Chapitre 4, emotes rares |
| Légende de Brumecombe | 5 000 | Chapitre 5, chapeau « Mamie » |

Cosmétiques : 24 chapeaux, 12 couleurs, 8 emotes, 6 poses supplémentaires à l'EA. Prix 50-400 Chronos. **Aucun achat réel.**

## 11. Caméra
3e personne, distance 4,5 m (zoom 2,5-7 m), hauteur 1,8 m, FOV 70° (réglable 60-100), collision caméra, mode « épaule » en visée (pistolet à graines). Option « caméra stable » (réduction des secousses).

## 12. Difficulté et accessibilité de jeu
- Pas de niveaux de difficulté ; **modificateurs de lobby** : durée de manche (3/5/7 min), dangers (0,5×/1×/1,5×), paradoxe (lent/normal/rapide), rotation on/off.
- Mode « Détente » : jauge de paradoxe désactivée, dangers 0,5×, pas de classement.

## 13. Télémétrie (opt-in uniquement) — événements
`session_start{mode,players}`, `round_end{round,traces,paradox_max}`, `contract_result{stars,score,contract_id}`, `tool_used{tool}`, `recipe_fired{recipe_id,hop}`, `collapse{}`, `museum_shared{}`, `settings_accessibility{flags}`. Aucun identifiant de joueur, aucune position fine, aucun texte libre.
