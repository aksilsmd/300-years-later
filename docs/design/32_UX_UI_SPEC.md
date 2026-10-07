# 32 — Spécification UX / UI
Propriétaire : Product Owner · v1.0 · Résolution de référence 1920×1080, testée à 1280×800 (Steam Deck) et 3840×2160. Tout texte via `tr()`.

## 1. Flux d'écrans
```
Démarrage → [1er lancement : Confidentialité & consentement] → Menu principal
Menu principal → Jouer → { Héberger | Rejoindre (amis / code / public) | Solo Relais | Capsule | Défi du jour }
Héberger/Rejoindre → Lobby (équipe, époques, modificateurs, chapeaux) → Brief du contrat (Odile)
Partie : Manche → Pause café (cinématique, vote, rotation) ×3 → Évaluation (Lendemain) → Musée (ARCHIVE) → Carte-récap → Lobby
Menu principal → Agence (progression, boutique Chronos, chapitres) · Options · Crédits & licences · Quitter
Pause en jeu → Reprendre · Options · Confidentialité · Quitter la mission
```
Règle : **jamais plus de 2 clics** entre le menu principal et une partie avec des amis (Jouer → Héberger → inviter via overlay Steam).

## 2. Les 60 premières secondes (onboarding)
| Seconde | Événement | Objectif UX |
|---|---|---|
| 0-5 | Consentement en 1 écran, 2 boutons égaux (« Jouer sans rien partager » / « Aider avec des stats anonymes ») | Confiance |
| 5-15 | Menu : un seul gros bouton « JOUER », le reste discret | Zéro friction |
| 15-45 | Solo Relais tutoriel auto-lancé la 1re fois : planter une graine | Action en < 30 s |
| 45-60 | Saut E0→E1, l'arbre apparaît : **le « aha »** | Compréhension du cœur |
| après | Proposition : « Inviter des amis » (overlay Steam) | Social |

## 3. HUD en partie (1080p)
| Zone | Élément | Spécification |
|---|---|---|
| Haut gauche | Badge d'époque (icône + nom + couleur) | 64 px, toujours visible, motif d'accessibilité |
| Haut centre | Chrono de manche + numéro de manche | 48 px ; passe orange à 60 s, rouge à 10 s |
| Haut droite | Carte du contrat (repliable, touche Tab) | objectif principal + bonus cochés en direct |
| Bas centre | Jauge de non-conformité | 0-100, 3 seuils marqués, animation grincement |
| Bas gauche | Inventaire 3 + 1 lourd | icônes 56 px |
| Bas droite | Indicateurs de voix (4 joueurs, couleur d'époque, bouche animée) + état micro | |
| Monde | Fantômes avec icône d'époque au-dessus (world-space, 1,2 m) ; pings (icône + anneau au sol, 8 s) ; noms des joueurs à moins de 15 m | |
| Centre | Réticule contextuel : nom de l'action (Creuser, Planter, Poser…) + touche | |
| Flottant | Notifications de recette : « Votre graine (an 0) est devenue un arbre (an 300) » 3 s, max 1 toutes les 2 s | lisibilité cause→effet |

## 4. Écrans clés
- **Lobby :** 4 cartes joueur (chapeau, couleur, époque assignée glissable), modificateurs à droite, code d'invitation masquable (icône œil), bouton « Prêt ». Hôte : « Lancer » actif quand tous prêts.
- **Brief :** Odile (portrait animé), carte cartonnée du contrat, tampon « URGENT », bouton « Compris » (compte à rebours 15 s).
- **Pause café :** plein écran, timeline des 4 époques en bandes horizontales qui se remplissent ; vote spectateurs (si actif) ; annonce de rotation avec flèches.
- **Évaluation :** hologramme de Lendemain, étoiles qui tombent une par une (0,3 s), détail des points.
- **Musée :** caméra sur rails, sous-titres d'ARCHIVE, bouton « Capturer » (mode photo), « Marquer le moment » (Timeline).
- **Carte-récap :** image 1080×1350 (format portrait réseaux) + 16:9 : titre de la mission, 4 avatars, statue la plus drôle, 3 phrases de Chronique, note, QR/code capsule optionnel. Boutons : Enregistrer, Copier, Partager (overlay Steam).

## 5. Contrôles
| Action | Clavier/souris | Manette |
|---|---|---|
| Déplacer / caméra | ZQSD (azerty auto) / souris | stick G / stick D |
| Courir | Maj | L3 |
| Sauter | Espace | A/✕ |
| Interagir / ramasser | E | X/□ |
| Poser / lâcher | F | B/○ |
| Utiliser l'outil | clic gauche | RT/R2 |
| Viser (pistolet à graines) | clic droit | LT/L2 |
| Roue de pings | maintenir R | maintenir RB/R1 |
| Emotes | maintenir T | maintenir LB/L1 |
| Inventaire | 1-2-3 / molette | croix directionnelle |
| Contrat | Tab | Back/Share |
| Parler (PTT, si activé) | V | stick D (clic) |
| Mode photo | P | croix bas (maintenir) |
| Pause | Échap | Start |
Remappage complet, détection automatique azerty/qwerty, icônes de manette selon le fabricant.

## 6. Accessibilité (options)
| Catégorie | Options |
|---|---|
| Vision | taille de texte 100-200 %, contraste élevé, motifs de fantômes, indicateurs d'époque par forme, contour renforcé, désactivation du smog visuel (remplacé par bordure d'écran), réduction du bloom/néon |
| Audio | sous-titres (taille, fond), sous-titres de sons importants, mono, volumes par bus, visualisation des voix |
| Moteur | caméra stable, assistance de visée, maintien → basculement, tempo réduit (mode Détente), vibrations on/off |
| Cognitif | rappel d'objectif permanent, flèche vers l'objectif, tutoriel rejouable, durée de manche 7 min |
| Photosensibilité | « réduire les clignotements » : glitch/Chronomites sans flash, transitions douces |
| Social | micro jamais requis, texte rapide, blocage/mute en 1 clic, mode « amis seulement » par défaut |

## 7. États d'erreur et messages (ton Odile, jamais technique à l'écran)
Exemples : perte de connexion → NET_RECONNECT avec roue 10 s puis NET_HOST_LEFT ; version différente → NET_VERSION avec bouton « Ouvrir Steam » ; code invalide → CAPSULE_INVALID. Les détails techniques vont dans `user://logs/` (sans données personnelles).

## 8. Localisation UI
- +30 % de place réservée ; aucune image avec du texte ; dates/nombres via `TranslationServer` ; polices avec repli CJK ; pseudo-localisation testée (voir 51_QA).

## 9. Métriques UX (opt-in)
Temps jusqu'à la première graine plantée (cible < 30 s), taux d'abandon du tutoriel (< 10 %), taux de partage de la carte-récap (cible 15 %), temps médian au musée.
