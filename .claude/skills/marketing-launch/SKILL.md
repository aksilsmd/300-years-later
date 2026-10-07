---
name: marketing-launch
description: Lancement et marketing du jeu comme un grand éditeur — rendu des visuels et du trailer DANS Unreal Engine (Movie Render Graph, Sequencer, captures haute résolution) à partir de data/shotlist.json, motion design Remotion, landing page React + Vite + TypeScript + Framer Motion sans traceur, tests Robot Framework/Lighthouse/k6, presskit, page Steam, plan créateurs. Utiliser pour « landing page », « trailer », « vidéo », « captures », « marketing », « lancement ».
---

# Skill : marketing-launch

## 0. Règles d'honnêteté et de sécurité
- **Toutes les images et vidéos du jeu sont rendues dans Unreal Engine** selon `docs/design/33_VISUAL_TARGETS.md` et `data/shotlist.json`. Aucune image d'IA générative, aucun montage trompeur, aucune cinématique présentée comme du gameplay.
- Avant que des rendus validés existent, la landing page et les documents n'affichent **aucune** image de jeu (typographie, couleurs et textes seulement).
- Chaque média publié est listé dans `media/APPROVALS.md` avec validation humaine.
- Zéro traceur, cookie, CDN ; polices et médias auto-hébergés ; `tools/privacy_scan.py` vert.
- Textes publics, prix, date : proposés par toi, validés par l'humain. Publication : par l'humain.

## 1. Rendus depuis le moteur
1. Ouvre la carte indiquée par chaque plan, applique l'époque (Data Layers / Level Instances + préréglage d'éclairage).
2. Place la caméra (CineCameraActor) d'après `camera` (position, cible, focale, ouverture) via le plugin MCP ou `game/Scripts/render_shots.py`.
3. **Fixes** : capture haute résolution (`HighResShot` ou Movie Render Graph une image) en 3840×2160, EXR 16 bits → PNG.
4. **Séquences** : Level Sequence + Movie Render Graph (anti-crénelage temporel 16, flou de mouvement, 24 i/s), sortie ProRes ou image par image puis `ffmpeg`.
5. Contrôle automatique (résolution, pixels NaN, métadonnées supprimées), puis ajout à `media/APPROVALS.md` avec statut « à valider ».
6. Versions verticales 9:16 (S12) en respectant les zones de sécurité TikTok/Shorts.

## 2. Trailers
| Trailer | Contenu | Outils |
|---|---|---|
| Annonce 60 s | storyboard `docs/design/70` §4 | Sequencer + Movie Render Graph, titrages Remotion |
| Gameplay 90 s | séquences jouées réellement, HUD visible | capture en jeu (`-MovieSceneCaptureType` ou capture OBS par l'humain) |
| Teaser vertical 15 s | S02 → S03 → logo | Remotion `TrailerVertical` sur les rendus |
Le projet Remotion (`marketing/video/`) assemble les rendus validés, ajoute titres, sous-titres FR/EN et musique fournie par le compositeur : `npm ci && npx remotion render Trailer out/trailer.mp4`.

## 3. Landing page
- **Production** : `marketing/landing-react/` (React 18, Vite, TypeScript, Framer Motion). Contenu dans `src/content.ts`, médias dans `public/media/` (uniquement des fichiers listés « validé » dans `media/APPROVALS.md`).
- **Référence sans dépendance** : `marketing/landing/` (HTML/CSS/JS) — sert de maquette fonctionnelle et de repli.
- Sections : héros (vidéo trailer en boucle muette quand elle existe, sinon titre animé), promesse, « comment ça marche » (frise des 4 époques animée au défilement), époques, modes, galerie (rendus validés), FAQ, créateurs/presse, appel à l'action Steam, pied de page légal (liens vers `legal/`).
- Exigences : `prefers-reduced-motion`, contraste AA, clavier, `lang`, Open Graph local, < 300 Ko hors médias, vidéo < 6 Mo, aucun cookie.
- Tests : `robot --outputdir results tests/robot`, Lighthouse, `k6 run tests/load/landing_smoke.js`.
- Déploiement (après accord) : workflow `pages.yml` ou hébergeur statique européen.

## 4. Page Steam, presskit, plan de lancement
- `marketing/steam/page.md`, `marketing/presskit/index.md` (fiche, descriptions, 8 rendus validés, logo, trailer, contact projet dédié).
- `marketing/launch-plan.md` : calendrier `docs/design/70` §5 adapté, 12 idées de clips « avant/après », critères de sélection de créateurs (l'humain fait la recherche), checklist Next Fest, KPI.
- Capsules Steam : dimensions `docs/design/30`/`70` ; la capsule principale est commandée à un illustrateur ou composée à partir du rendu S01 validé.
