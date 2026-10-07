# 30 — Bible artistique (réaliste, Unreal Engine 5.8)
Propriétaire : Product Owner · v2.0 (remplace la v1 low-poly — voir ADR 0012)

## 1. Intention
« Réalisme cinématographique chaleureux » : un monde photoréaliste qu'on regarde vieillir sur 900 ans. Les fiches détaillées des époques, des personnages et la liste des plans sont dans **`33_VISUAL_TARGETS.md`** (normatif).

## 2. Pipeline de contenu
| Catégorie | Source | Outil | Licence / contrainte |
|---|---|---|---|
| Terrain | Landscape UE (+ Mesh Terrain expérimental à évaluer) sculpté et peint ; masques par époque | UE Landscape, PCG | contenu propre |
| Végétation | Fab (Megascans / packs Nanite Foliage) + variantes procédurales | PCG graphs, Nanite Foliage | **licence Fab payante** ; jamais dans le dépôt public |
| Roches, sols, textures | Fab / Megascans | Material Layers | idem |
| Architecture par époque | kits modulaires Fab achetés ou modélisés (Blender) | Blender → glTF/FBX → Nanite | vérifier chaque licence Fab (Standard vs Professional) |
| Humains | MetaHuman Creator (dans l'éditeur 5.8) | MetaHuman, Groom | gratuit < 1 M$ de revenus annuels |
| Créatures | sculpt + groom + rig par un artiste | ZBrush/Blender, Groom, Control Rig | contrat de cession |
| Animations | Motion Matching (pack d'animations libres d'Epic) + capture | MetaHuman Animator, Control Rig | licences Epic |
| Effets | Niagara | — | contenu propre |
| Matériaux spéciaux | fantôme (Fresnel + motif), glitch (bandes, sans flash en mode accessibilité), apparition (WPO + dissolve), néon | Material Editor | contenu propre |
| Interface | UMG + Common UI, style « agence d'intérim » réaliste (papier, tampons, badges) | UMG | polices OFL |

## 3. Éclairage et rendu
- Lumen GI + réflexions (High sur PC recommandé, **Medium** sur config minimale et Steam Deck), MegaLights pour les nombreuses sources de l'an 900, Virtual Shadow Maps, Sky Atmosphere + Volumetric Clouds + Exponential Height Fog volumétrique.
- Un **préréglage d'éclairage par époque** (Data Layer « Lighting_E*n* ») : soleil, ciel, brume, post-process, LUT (valeurs dans `33_VISUAL_TARGETS.md` §2).
- TSR (Temporal Super Resolution) ; options DLSS/FSR via plugins officiels des fabricants (licences à vérifier).

## 4. Budgets (PC recommandé, 1440p, 60 i/s)
| Élément | Budget |
|---|---|
| Temps GPU | ≤ 16,6 ms (recommandé) ; ≤ 33 ms (minimum, Deck) |
| Instances végétation visibles | gérées par Nanite Foliage, densité PCG par époque |
| MetaHumans à l'écran | 4 joueurs + ≤ 12 PNJ (LOD MetaHuman adaptés) |
| Mémoire texture (streaming pool) | 3 Go (rec.) / 1,5 Go (min.) |
| Taille installée | 15-30 Go |

## 5. Lisibilité (rappel des piliers)
Couleur d'époque, changement de silhouette à chaque saut, contraste de valeurs, fantômes identifiables. Une capture qui viole un pilier est refusée en revue.

## 6. Interdits
Aucun élément reprenant une œuvre, une marque, un personnage, un lieu réel identifiable ou un symbole religieux/national réel. Aucune image d'IA générative (texte→image) livrée ou utilisée en marketing comme si c'était le jeu. Aucun asset Fab/Megascans/MetaHuman dans le dépôt public.
