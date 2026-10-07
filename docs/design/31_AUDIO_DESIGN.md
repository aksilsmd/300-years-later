# 31 — Design audio
Propriétaire : Product Owner · v1.0 · Principe : **streamer-safe** (100 % original ou CC0 audité), lisibilité avant réalisme, chaque recette a un son.

## 1. Musique
### 1.1 Leitmotiv
Un thème de 8 notes (« le thème de la Trace »), ré mineur → fa majeur, réorchestré par époque. Commande au compositeur : 4 versions de 2 min 30 bouclables + 1 version « agence » (bossa de salle d'attente) + 1 « musée » (valse) + 6 stingers.
| Époque | Instruments | Tempo | Caractère |
|---|---|---|---|
| E0 | flûtes en os (fictives), percussions bois, voix bouche fermée | 80 | aube, curiosité |
| E1 | luth, vielle, tambourin, cloches | 100 | foire, bonhomie |
| E2 | cuivres, enclume, sifflet de vapeur, contrebasse pizzicato | 110 | mécanique, swing |
| E3 | synthés pastel, carillons, boîte à rythmes douce | 120 | futur naïf |

### 1.2 Musique adaptative (AudioStreamInteractive / couches)
- Couche A « base » : toujours.
- Couche B « tension » : fondu +1,5 s quand un danger est à moins de 15 m ou jauge ≥ 50.
- Couche C « pause café » : montage accéléré, le thème joué 4× plus vite avec toutes les époques superposées (effet « siècles qui défilent »).
- Stingers : contrat réussi, étoile, paradoxe, Chronomite, effondrement, Bouloche attaché.
- Transition d'époque : la mélodie continue **à la même mesure** dans l'orchestration suivante (continuité du temps).

### 1.3 Contrat compositeur (voir 60_LEGAL)
Cession de droits exclusive, tous supports (jeu, trailers, streams, bande originale vendable), monde entier, durée légale ; interdiction de samples sous licence ; livraison WAV 48 kHz 24 bits + stems.

## 2. Effets sonores (liste EA, ~70)
| Famille | Sons |
|---|---|
| Joueur | pas (terre, herbe, pierre, bois, métal, eau, marais), saut, chute, étourdissement, creuser, planter, ramasser, poser, porter lourd, pose statue (flash) |
| Recettes | pousse (0,4 s, « poing »), arbre qui grandit, pierre qui s'empile, eau qui coule, lac qui s'étend, rouille, trésor, fan-club (acclamation), statue (gong), chemin (pas multiples), feu, champ |
| Dangers | Bouloche (barrissement, mastication, trot), Fiscalin (plume, « hmpf », chèvres), Automates (bips, pinces, rails), Bouilloire (sifflet, valve), Brigade (jingle, scan, recyclage), Chronomites (grignotement, clignotement), touristes (déclic) |
| Système | pause café (horloge accélérée), rotation (whoosh), paradoxe (grincement du Bail, 3 niveaux), effondrement, étoiles (×5), Chronos, UI (clic, tampon, post-it) |
| Voix | charabia par personnage (voir §3), bouche des joueurs |

Génération : scripts `tools/sfx/*.py` (numpy, synthèse soustractive/FM + bruit filtré + enveloppes) → OGG 48 kHz ; les sons « organiques » (pas, eau) peuvent venir de packs CC0 audités.

## 3. Voix procédurale (« charabia »)
- Chaque PNJ a un profil : fréquence fondamentale (Odile 220 Hz, Lendemain 180 Hz avec vibrato, ARCHIVE 150 Hz robotique, Mamie 200 Hz lente, Fiscalin 260 Hz nasillard), vitesse de syllabes, 6 syllabes de base synthétisées (formants).
- Le texte sous-titré pilote la durée (≈ 60 ms par caractère) ; aucune langue réelle n'est imitée.
- Avantage : **zéro doublage**, localisation gratuite, aucun droit voix.

## 4. Voix des joueurs
- Capture via Steam Voice (Opus), lecture par `AudioStreamGenerator` sur un bus par joueur.
- Bus « Voix » → effets par distance/époque : passe-bas, passe-bande « radio », réverbération grotte.
- Ducking de la musique −6 dB quand une voix est active.
- Jamais enregistrée ; aucun fichier temporaire.

## 5. Mixage
| Bus | Niveau cible | Note |
|---|---|---|
| Master | −16 LUFS intégré, true peak −1 dBTP | norme streaming |
| Musique | −23 LUFS sous voix | ducking |
| SFX | priorité par catégorie, limite 32 voix simultanées | |
| Voix | priorité maximale | |
| UI | −20 dB | |
Options joueur : volume par bus, « musique off » (streamers), mono, sous-titres pour les sons importants (icônes : « Bouloche approche »).

## 6. Formats et budget
OGG Vorbis q6 pour musique, q5 pour SFX ; ≤ 120 Mo au total ; chargement en streaming pour la musique.

## 7. Tests audio (voir 51_QA)
- Aucun son > 0 dBTP ; aucune boucle avec clic ; latence voix < 250 ms en LAN ; vérification que le fichier `user://` ne contient jamais d'audio.
