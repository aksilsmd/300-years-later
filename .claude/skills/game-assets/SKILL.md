---
name: game-assets
description: Produit et intègre le contenu réaliste du jeu dans Unreal Engine 5.8 — environnements (Landscape, PCG, Nanite Foliage), assets Fab/Megascans, MetaHumans, prefabs de vieillissement, matériaux, Niagara, MetaSounds — selon les cahiers de rendu docs/design/30 et 33, avec traçabilité des licences et budgets de performance. Utiliser pour toute création ou intégration d'asset.
---

# Skill : game-assets

## Sources de vérité
`docs/design/30_ART_BIBLE.md` (pipeline, budgets), `docs/design/33_VISUAL_TARGETS.md` (looks d'époque, personnages, plans), `data/recipes/` (chaque recette × saut = un prefab).

## Procédure d'acquisition (l'humain achète, tu prépares)
1. Produis `docs/assets/SHOPPING_LIST.md` : pour chaque besoin, l'asset Fab proposé (nom, lien), le type de licence requis, le coût estimé, l'alternative gratuite d'Epic si elle existe.
2. L'humain valide, achète et ajoute les assets au projet (Fab dans l'éditeur).
3. Tu ajoutes une ligne dans `THIRD_PARTY_LICENSES.md` et un `SOURCE.md` dans le dossier de contenu (dépôt privé).

## Production
| Élément | Méthode |
|---|---|
| Terrain de la Vallée | Landscape sculpté selon `docs/design/21` (5 repères), couches de matériaux Megascans, masques par époque |
| Végétation | graphes PCG déterministes (graine du monde) lisant la densité de `FEraState` ; Nanite Foliage |
| Décor par époque | Level Instances `LI_Era0..3` assemblées à partir de kits modulaires ; respecter les fiches §2 de `33` |
| Prefabs de traces | Packed Level Actors `PLA_<recette>_hop<n>` ; transition de 0,4 s (WPO + dissolve + Niagara + MetaSound) |
| Humains | MetaHuman Creator dans l'éditeur ; 12 préréglages divers et respectueux ; tenues Temporis + accessoire d'époque |
| Créatures | **commandées à un artiste** (sculpt, groom, rig) ; tu prépares le brief à partir de `33` §3 |
| Matériaux spéciaux | fantôme (Fresnel + motif d'accessibilité), glitch (version sans flash), néon, apparition |
| Audio | MetaSounds par recette et danger ; musique fournie par le compositeur |

## Contrôles automatiques
- Script Python d'éditeur `game/Scripts/validate_assets.py` : nommage, budgets (triangles non-Nanite, textures), présence de LOD, collision, absence de références vers des dossiers interdits.
- Toute capture produite pour validation visuelle passe par `media/APPROVALS.md` (voir `marketing-launch`).

## Interdits
Aucune image ou modèle généré par IA générative sans accord écrit (et déclaration Steam). Aucun asset reproduisant une œuvre, une marque, un lieu réel identifiable. Aucun contenu sous licence dans le dépôt public.
