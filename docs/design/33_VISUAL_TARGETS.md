# 33 — Cibles visuelles et cahier de rendu (référence pour l'IA)
Propriétaire : Product Owner · v1.0 · Normatif pour `game-assets` et `marketing-launch`

> **Important — aucune image dans le dépôt.** Ce document décrit précisément chaque image et chaque plan qui doivent être produits **dans Unreal Engine 5.8** par l'IA. Une image qui ne respecte pas ces descriptions ne doit pas être publiée. Aucune image générée par IA générative (texte→image) ne peut remplacer une capture du moteur.

## 1. Intention générale
**« Réalisme cinématographique chaleureux. »** Des environnements photoréalistes (photogrammétrie, éclairage global dynamique, atmosphère volumétrique) habités par des humains crédibles aux tenues très lisibles. L'humour vient des **situations**, jamais d'un style caricatural. Références de qualité (niveau visé, aucun élément repris) : la densité végétale des grands mondes ouverts récents, la lumière des productions UE5 à Lumen, la lisibilité des personnages d'un jeu de simulation de vie.

### Piliers de lisibilité (non négociables malgré le réalisme)
1. **Couleur d'époque** portée par l'éclairage et une pièce de vêtement (brassard, foulard) : ambre (an 0), or (an 300), cuivre (an 600), vert néon (an 900).
2. **Silhouettes** : chaque trace vieillie change de silhouette à chaque saut (pousse → arbre → géant).
3. **Contraste de valeurs** : le sujet est toujours plus clair ou plus saturé que son fond (règle des 3 secondes).
4. **Fantômes** : silhouette translucide à Fresnel, teinte d'époque, motif d'accessibilité.

## 2. Les quatre époques — fiches de look
| | An 0 — L'Aube | An 300 — Les Bannières | An 600 — La Vapeur | An 900 — Le Néon |
|---|---|---|---|---|
| Heure / soleil | aube, élévation 6°, azimut est | midi, 55° | crépuscule, 8°, ouest | nuit, lune haute, 35° |
| Température de couleur | 3 200 K + ciel 9 000 K | 5 600 K | 2 800 K + smog | éclairage urbain 4 000-6 500 K, néons saturés |
| Atmosphère | brume au sol épaisse 0-6 m, rayons volumétriques entre les arbres | ciel bleu, cumulus, air limpide | smog brun (Volumetric Fog densité 0,04), suie, braises | air humide, bloom des néons, reflets sur sol mouillé |
| Végétation | forêt primaire dense (chênes, pins, fougères géantes), mousses | bocage, champs en patchwork, vergers | arbres rares, troncs noircis, herbes sèches | parcs urbains taillés, arbres bioluminescents |
| Architecture | huttes de fougères et de peaux, menhirs couchés | bourg à colombages, tuiles rouges, Fort Têtu en bois, moulins | usines en brique, charpentes métalliques, cheminées, rails, Grande Bouilloire | tours de verre et céramique pastel, Musée de Tout (dôme), passerelles |
| Eau (la Brume) | rivière sauvage, galets, cascades | rivière + moulins, lavoirs | canal en pierre, eau trouble irisée | quais éclairés, reflets néon |
| Matériaux clés | bois brut, peaux, os, pierre moussue | chaux, colombages, tuiles, laine teinte | brique, fonte, cuivre oxydé, verre sale | verre, aluminium anodisé, céramique, LED |
| Post-process | grain léger, contraste doux | neutre | LUT chaude, vignettage | LUT froide, bloom contrôlé, aberration chromatique 0,2 |
| Bande son de référence | `31_AUDIO_DESIGN.md` E0 | E1 | E2 | E3 |

## 3. Personnages
- **Intérimaires (joueurs)** : MetaHumans (Creator intégré à l'éditeur), proportions réalistes, visages expressifs, **12 préréglages** variés (âges, morphologies, carnations, coiffures) — diversité respectueuse, aucune caricature. Tenue de base : combinaison d'intérim « Temporis » (tissu technique gris clair, logo fictif), avec un élément d'époque coloré. Chapeaux : 24 modèles réalistes (casque de chantier, béret, chapeau melon, couronne de foire, casque néon…).
- **PNJ** : Odile Chronique (cinquantaine, tailleur, badge géant, sourire fixe), Mamie Horloge (très âgée, châle à motif d'horloge, panier), Sire Fiscalin (silhouette longue, plume, registre, deux chèvres réalistes), ARCHIVE (robot guide en céramique blanche et laiton, chapeau melon, une roue), Monsieur Lendemain (hologramme volumétrique de tête géante, scanlines).
- **Créatures** : Bouloche (mammouth juvénile réaliste, fourrure groom, yeux expressifs — sculpté et rigué par un artiste, voir §7) ; Chronomites (petites créatures à six pattes, chitine grise, grands yeux, émissives quand elles grignotent) ; drones de la Brigade Propreté (pastel, balais rotatifs).
- **Animation** : locomotion par Motion Matching ; poses de statue = 8 poses de capture (salut, canard, penseur, étoile, super-héros, sieste, pointer, danse) ; expressions faciales par MetaHuman Animator (capture vidéo).

## 4. Traces et vieillissement (exigence visuelle)
Chaque recette (`data/recipes`) a, pour chaque saut, un **prefab réaliste** (Packed Level Actor) : ex. `seed` → pousse avec terre retournée → chêne de 8 m → chêne de 18 m → arbre millénaire de 35 m dont les racines soulèvent le sol, couvert de lanternes au néon en an 900. La transition visuelle (0,4 s) combine croissance par World Position Offset, particules Niagara (feuilles, poussière) et son MetaSounds.

## 5. Liste des plans à produire (« shot list »)
La version exécutable est `data/shotlist.json` (caméra, objectif, lumière, éléments). Résumé :
| ID | Usage | Description précise | Critères d'acceptation |
|---|---|---|---|
| S01 | Capsule / héros | Même colline vue des 4 époques en 4 bandes verticales ; intérimaires alignés au premier plan ; la pousse (an 0) devient l'arbre millénaire (an 900) de gauche à droite | même cadrage exact pour les 4 rendus (caméra verrouillée), raccords invisibles, titre lisible à 231 px |
| S02 | Accroche « graine » | Gros plan au ras du sol, objectif 35 mm, f/2,8 : une main d'intérimaire plante une graine dans la terre humide, brume dorée de l'aube | profondeur de champ réelle, gouttes visibles, mains MetaHuman crédibles |
| S03 | Accroche « 300 ans » | Même cadrage que S02 en an 300 : chêne adulte, un ami (autre intérimaire) écrasé comiquement sous une branche tombée | raccord parfait S02/S03 (même caméra), humour lisible sans texte |
| S04 | Gameplay an 300 | Vue troisième personne, HUD complet (`32_UX_UI_SPEC.md` §3), notification de recette visible, fantôme an 0 en Fresnel ambre | HUD net en 1080p et 1280×800 |
| S05 | Le bourg | Plan large du bourg médiéval à midi, foire, bannières au vent, Sire Fiscalin confisquant une cuillère | ≥ 6 PNJ animés, vent visible (Niagara, tissu Chaos) |
| S06 | L'usine | Crépuscule, smog volumétrique, Automate sur rails transformant des troncs en planches, braises | volumétrique sans bruit visible, 2 sources de lumière chaudes |
| S07 | Ville néon | Nuit, sol mouillé, reflets néon, drones de la Brigade scannant un objet ancien (anneau lumineux) | reflets Lumen/MegaLights propres, pas de scintillement |
| S08 | Bouloche | Le mammouth juvénile mange une pousse sous le regard désespéré d'un joueur, an 0 | fourrure groom, regard expressif |
| S09 | Paradoxe | Chronomites grignotant un pont qui « glitche » (matériau à bandes), jauge à 75 % | effet lisible en option « réduire les clignotements » (version sans flash également produite) |
| S10 | Musée de Tout | Intérieur du dôme, quatre statues des joueurs sur socles, ARCHIVE pointe une statue en pose « canard », sous-titre visible | statues = poses réelles capturées, matériau marbre/bronze/néon |
| S11 | Carte-récap | Image générée par le jeu lui-même (1080×1350) en fin de partie | produite par le système du jeu, pas par montage |
| S12 | Vertical 9:16 | Versions verticales de S02→S03 et S07 pour TikTok/Shorts | sujet centré, zones de sécurité des interfaces sociales respectées |

## 6. Trailers (Movie Render Graph + Sequencer)
- **Annonce (60 s)** : storyboard `70_MARKETING_GTM.md` §4. Rendu en 4K/24 i/s, anti-crénelage temporel élevé (spatial 1 × temporel 16), motion blur réel, format ProRes 422 HQ puis H.264/H.265 pour le web.
- **Gameplay (90 s)** : uniquement des séquences jouées (capture en jeu, pas de cinématique pré-calculée présentée comme du gameplay — règle Steam et honnêteté).
- **Teaser vertical (15 s)** : S02 → S03 → logo.
- Titrages, sous-titres et motion design : composition Remotion (`marketing/video/`) appliquée sur les rendus UE.

## 7. Ce que l'IA ne peut pas faire seule (à commander à des humains)
| Élément | Pourquoi | Prestataire |
|---|---|---|
| Sculpt, groom et rig de Bouloche et des chèvres | créature organique de qualité AAA | artiste créature (freelance) |
| Capture faciale et corporelle des PNJ | jeu d'acteur crédible | comédiens + MetaHuman Animator (vidéo) ou studio de mocap |
| Direction artistique finale, étalonnage du trailer | goût et cohérence | directeur artistique / coloriste |
| Capsule Steam et logo | vitrine commerciale | illustrateur |
| Musique | identité sonore | compositeur |
Contrats de cession de droits obligatoires (`legal/`).

## 8. Procédure de validation des images
1. Rendu par l'IA via `marketing-launch` (Movie Render Graph ou capture haute résolution).
2. Contrôle automatique : résolution, absence d'artefacts (script de détection de pixels morts/NaN), métadonnées supprimées.
3. **Validation humaine** obligatoire (case cochée dans `media/APPROVALS.md` : ID, date, validateur, commentaire).
4. Seules les images validées sont copiées dans la landing page, la page Steam et le guide PDF.
