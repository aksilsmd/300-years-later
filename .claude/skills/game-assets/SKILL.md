---
name: game-assets
description: Produces and integrates the realistic content of the game in Unreal Engine 5.8 — environments (Landscape, PCG, Nanite Foliage), Fab/Megascans assets, MetaHumans, ageing prefabs, materials, Niagara, MetaSounds — following the visual specs docs/design/30 and 33, with licence traceability and performance budgets. Use for any asset creation or integration ("assets", "monde", "décor", "MetaHuman").
---

# Skill: game-assets

> **FR —** Produit et intègre le contenu réaliste (monde, végétation, humains, effets) selon les cahiers de rendu, avec traçabilité des licences. Répond dans la langue de l'utilisateur.

## Sources of truth
`docs/design/30_ART_BIBLE.md` (pipeline, budgets), `docs/design/33_VISUAL_TARGETS.md` (era looks, characters, shots), `data/recipes/` (each recipe × hop = one prefab).

## Acquisition (human buys, you prepare)
1. Write `docs/assets/SHOPPING_LIST.md`: each need, proposed Fab asset (name, link), licence type, estimated cost, free Epic alternative.
2. In autonomous mode, **start with free Epic content** (samples, free Fab items, MetaHuman) so work never waits; mark items to upgrade later.
3. Purchases are a hard stop: list them in `QUESTIONS.md` with total cost and `monthly_asset_budget_eur` from the config.
4. After acquisition: line in `THIRD_PARTY_LICENSES.md` and `SOURCE.md` in the content folder (private repo).

## Production
| Item | Method |
|---|---|
| Valley terrain | Landscape following `docs/design/21` (5 landmarks), Megascans material layers, per-era masks |
| Vegetation | deterministic PCG graphs (world seed) reading `FEraState` density; Nanite Foliage |
| Per-era scenery | Level Instances `LI_Era0..3` from modular kits; follow `33` §2 |
| Trace prefabs | Packed Level Actors `PLA_<recipe>_hop<n>`; 0.4 s transition (WPO + dissolve + Niagara + MetaSound) |
| Humans | MetaHuman Creator in-editor; 12 diverse, respectful presets; Temporis outfits + era accessory |
| Creatures | **commissioned to an artist** (sculpt, groom, rig); you write the brief from `33` §3 |
| Special materials | ghost (Fresnel + accessibility pattern), glitch (no-flash variant), neon, appear |
| Audio | MetaSounds per recipe and hazard; music delivered by the composer |

## Automatic checks
Editor Python `game/Scripts/validate_assets.py`: naming, budgets (non-Nanite triangles, textures), LODs, collision, no references to forbidden folders. Every capture for visual review goes through `media/APPROVALS.md`.

## Forbidden
Generative-AI images or models without written approval (and Steam disclosure); assets imitating existing works, brands or identifiable real places; licensed content in the public repo.
