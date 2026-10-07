# CENTURY TEMPS — Cahier des charges complet
### Étude de marché · Concept · Game design · Architecture · Conformité · Plan de réalisation pour Claude Code

> Titre de travail : **CENTURY TEMPS** (FR : « Intérim Temporel »). Jeu de pun anglais : *temps* = intérimaires.
> Version du document : **2.0 — 7 octobre 2026**. Titre public de travail : **300 Years Later** (à valider juridiquement, §6.6).
> **v2 :** moteur **Unreal Engine 5.8** et direction artistique **réaliste** (ADR 0012). Les détails normatifs sont dans `30_ART_BIBLE.md`, `33_VISUAL_TARGETS.md`, `40_TECHNICAL_DESIGN.md`, `80_CLAUDE_CODE_PLAYBOOK.md` et `docs/guides/03_TEMPS_ET_COUTS.md`.

---

## 0. Résumé exécutif

**Pitch en une phrase :** *Jusqu'à 4 amis, chacun bloqué dans un siècle différent du même endroit : tout ce que tu fais dans le passé vieillit en direct chez ton pote dans le futur.*

**Accroche virale (la phrase qu'on doit lire sous chaque clip TikTok) :**
> « J'ai planté une graine. Mon pote, 300 ans plus tard, s'est fait écraser par un chêne. »

**Pourquoi ce jeu peut percer :**
1. Il épouse la tendance la plus puissante du marché Steam 2025-2026 : le **coop social pas cher (« friendslop »)**, qui a placé plusieurs titres dans le top des ventes.
2. Il ajoute ce qui manque au genre : une **mécanique systémique profonde** (le moteur de vieillissement) qui génère des situations différentes à chaque partie → durée de vie et contenu infini pour les streamers.
3. Chaque scène se comprend en 3 secondes (avant/après sur deux époques) → **format parfait pour les clips courts**, comme Meccha Chameleon.
4. Le jeu **fabrique lui-même ses clips** : statues de tes poses, musée final qui raconte ta partie de façon absurde, carte-récap partageable.
5. Réalisable par **une petite équipe pilotée par l'IA** (Claude Code + plugin officiel Unreal) : rendu réaliste Unreal Engine 5.8, monde procédural (PCG), logique pilotée par données ; les éléments artistiques organiques (créatures, capture de jeu d'acteur, musique) sont confiés à des professionnels.

**Positionnement :** coop 1-4 joueurs, **3D réaliste**, PC Windows (Steam Deck « jouable » visé), Steam d'abord, prix indicatif **19,99 €** (à valider), Early Access, démo pour un Steam Next Fest.

---

## 1. Étude de marché (octobre 2026)

### 1.1 Les chiffres qui comptent
| Donnée | Valeur | Ce que ça implique |
|---|---|---|
| Revenus Steam 2026 (au 5 sept.) | > 15 Md$ (≈ +15 % vs 2025 entier) | Le marché PC grandit encore |
| Jeux sortis sur Steam 2026 (au 1er sept.) | 17 200 | Surproduction : la visibilité est le vrai problème |
| Revenu médian d'un jeu sorti en 2026 | ≈ 1 728 $ | La majorité des jeux échouent : il faut un hook exceptionnel |
| Part des revenus captée par le top 1 % | 84,6 % | Économie « tout ou rien » |
| Genres au meilleur « taux de hit » (> 100 k$) | Sandbox 27,3 %, FPS 21,6 %, RPG 19,4 % | Le **sandbox** est le genre le plus sûr |
| Genres au pire revenu médian | Course, puzzle, arcade, plateforme | À éviter comme genre principal |
| Meccha Chameleon (juin 2026) | 2 devs, ~2 mois de dev, 4,79 $, 15 M ventes en < 1 mois, ~90 M$ | Concept simple + lisible en clip + prix bas + viewers qui jouent |
| Schedule I (2025) | Dev solo, ~8 M ventes, 460 k joueurs simultanés | Profondeur systémique > graphismes |
| Friendslop 2025 | 4 des 10 meilleures ventes Steam (en copies) | Le coop social est LA tendance |
| Gamble With Your Friends (2026) | 1 M ventes la 1re semaine | La tendance continue en 2026 |
| Slay the Spire 2 (mars 2026) | Pic 574 k joueurs, ~148 M$ | Rejouabilité = longévité |

### 1.2 Ce que les hits ont en commun (analyse croisée)
| Facteur | Meccha Chameleon | Peak | R.E.P.O. | Schedule I | Lethal Company |
|---|---|---|---|---|---|
| Coop / social 2-6 joueurs | ✅ | ✅ | ✅ | ✅ | ✅ |
| Compréhensible en 1 image/3 s | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| Échecs drôles = clips | ✅ | ✅ | ✅ | ✅ | ✅ |
| Prix ≤ 10 € | ✅ | ✅ | ✅ | ❌ (≈ 20 €) | ✅ |
| Graphismes modestes assumés | ✅ | ✅ | ✅ | ✅ | ✅ |
| Petite équipe (1-3) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Profondeur systémique | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |

**Conclusion :** la case vide la plus intéressante est **« friendslop + profondeur sandbox »** : la lisibilité virale d'un party-game, avec la profondeur qui retient les joueurs 50 heures (comme Schedule I).

### 1.3 Idées étudiées puis écartées (et pourquoi)
| Idée | Verdict | Raison |
|---|---|---|
| « Ta voix est ta lampe » (coop horreur au micro) | ❌ Écartée | Déjà saturée : Shut Up It's Here, Echo Mates, VeinLight, Cursed Companions, There Won't Be Light… |
| Cache-cache / prop hunt | ❌ | Meccha Chameleon a pris le terrain, effet « clone » garanti |
| Coop horreur extraction + quota | ❌ | Lethal Company, R.E.P.O. et des dizaines de clones |
| Coop d'escalade / physique ragdoll | ❌ | Peak, Human Fall Flat |
| Jeu « usine/automatisation » solo | ⚠️ | Très rentable en médiane mais long à produire et peu viral en clip |
| **Coop à travers les siècles + vieillissement systémique** | ✅ **Retenue** | Précédents uniquement en puzzle point-and-click ou game jams ; aucun sandbox coop commercial |

### 1.4 Vérification d'originalité
Précédents connus du thème « coop entre époques » :
- *Day of the Tentacle* (1993, solo, puzzle) — l'ancêtre du concept.
- *The Past Within* (Rusty Lake, 2022) — coop 2 joueurs passé/futur, **énigmes statiques**.
- *TimeSplitters: Future Perfect* — voyage temporel en FPS, pas de propagation systémique.
- Prototypes de game jam / itch.io (*Friends Across Time*, *Splitstream*) — non commerciaux.

**Ce qui est inédit dans CENTURY TEMPS :**
1. Un **moteur de vieillissement systémique** : tout objet laissé dans une époque évolue selon des règles (pousse, rouille, érosion, culte, reproduction…) et apparaît transformé dans les époques suivantes, **en temps réel**.
2. **3 à 4 joueurs empilés sur 4 siècles du même lieu**, en sandbox physique (pas des énigmes scriptées).
3. **Rotation des époques** entre les manches : tu hérites du chaos que tes amis t'ont laissé.
4. **Statues de pose** et **musée final généré** qui racontent la partie (machine à clips intégrée).
5. **Mode Capsule asynchrone** : tu joues le passé, tu envoies un code, ton ami joue le futur plus tard.

> Action obligatoire avant annonce : refaire une recherche Steam/itch/YouTube « co-op past future sandbox » et noter les résultats dans `docs/originalite.md`.

---

## 2. Le concept

### 2.1 Univers et ton
L'agence **Temporis Intérim** envoie des intérimaires sous-payés réparer (ou « optimiser ») l'histoire d'un lieu fictif, **la Vallée de Brumecombe**, pour satisfaire des clients exigeants du futur. Ton : comédie absurde bienveillante (PEGI 7-12), pas d'horreur gore. Monde 100 % fictif : pas de vraie période historique, pas de vraie culture caricaturée.

### 2.2 Les 4 époques (même carte, 300 ans d'écart)
| Époque | Nom | Ambiance | Danger signature |
|---|---|---|---|
| E0 — An 0 | **L'Aube** | préhistoire fantaisiste, forêts, mammouths curieux | le mammouth mange tout ce qui pousse |
| E1 — An 300 | **Les Bannières** | médiéval fantaisiste, villages, châteaux | le percepteur confisque les objets |
| E2 — An 600 | **La Vapeur** | industriel, rails, cheminées | le smog et les machines déréglées |
| E3 — An 900 | **Le Néon** | futur pastel, drones, musées | les drones de nettoyage effacent les « anachronismes » |

### 2.3 Les 5 piliers de design
1. **Cause → conséquence visible** : toute action importante doit produire un effet lisible dans une époque ultérieure.
2. **Lisible en 3 secondes** : silhouettes fortes, couleurs par époque, effets exagérés.
3. **Le chaos est une récompense** : un échec doit être drôle avant d'être punitif.
4. **On a besoin des autres, et ils nous gênent** : interdépendance obligatoire entre époques.
5. **Partageable par défaut** : chaque partie produit au moins un moment montrable (statue, musée, carte-récap).

### 2.4 Boucles de jeu
| Échelle | Boucle |
|---|---|
| 30 secondes | Ramasser / planter / construire / déplacer → voir l'effet dans le futur (fantômes, annonces vocales de l'ami) |
| 1 manche (5 min) | Chacun dans son époque remplit sa part du **contrat** pendant que les dangers pèsent |
| Pause café temporelle (30 s) | Cinématique « accéléré » : les siècles défilent, la propagation se résout, les paradoxes explosent |
| 1 partie (15-20 min) | 3 manches avec **rotation** : chaque joueur avance d'une époque et hérite des actions des autres → **Musée final** |
| Méta (heures) | Siège de l'agence, déblocage d'outils, cosmétiques, nouveaux biomes, défis quotidiens par graine |

---

## 3. Game design détaillé

### 3.1 Joueurs et modes
| Mode | Joueurs | Description |
|---|---|---|
| **Coop Contrat** (cœur) | 2-4 | 1 joueur par époque (2 joueurs = 2 époques, etc.) |
| **Saboteur du Temps** | 4 | Un joueur secret veut créer un paradoxe total ; vote à la pause café |
| **Solo Relais** | 1 | Tu joues E0, puis E1 sur tes propres conséquences, etc. (naturellement solo) |
| **Capsule asynchrone** | 1 + 1 | Tu joues une époque, tu génères un **code capsule** ; un ami le charge plus tard et joue l'époque suivante |
| **Défi du jour** | 1-4 | Graine mondiale identique pour tous, classement Steam |

### 3.2 Présence entre époques (« fantômes »)
- Les joueurs d'autres époques sont visibles en **silhouette fantôme** translucide teintée de la couleur de leur époque.
- **Voix de proximité inter-époques** : tu entends clairement un ami quand vous êtes **au même endroit** (positions X/Z proches) ; plus vous êtes loin, plus sa voix est étouffée et « radio ancienne ». Le micro n'est jamais obligatoire (roue de pings + emotes + texte rapide).
- **Ping temporel** : marquer un endroit le fait clignoter dans toutes les époques.

### 3.3 Le moteur de vieillissement (cœur du jeu)
Chaque objet persistant porte une **recette temporelle** : une fonction pure qui, à partir de son état et de son environnement, calcule son état 300 ans plus tard.

Exemples (à implémenter en données, `data/recipes/`) :
| Objet posé | +300 ans | +600 ans | +900 ans |
|---|---|---|---|
| Graine | arbre | grand arbre (bloque/porte) | arbre millénaire sacré |
| Graine + eau proche | forêt | forêt dense | réserve naturelle protégée |
| Tas de pierres empilées | cairn | **monument** vénéré | site touristique avec boutique |
| Pose du joueur sur un socle | **statue** de lui dans cette pose | statue érodée + légende locale | statue géante en néon |
| Barrage de branches | étang | lac | station balnéaire |
| Tranchée creusée | ruisseau | rivière | canyon |
| Objet en fer | rouille | ferraille | artefact de musée |
| Pièces enterrées | trésor | trésor + carte au trésor (PNJ) | fouille archéologique |
| Deux animaux d'une espèce laissés ensemble | troupeau | race domestiquée | mascotte de la ville |
| Graffiti / gravure | inscription ancienne | « texte sacré » mal traduit | plaque officielle |
| Feu non éteint | zone brûlée | sol fertile | champ |
| Ordures | décharge | couche fossile | « mine » exploitable |
| Objet du futur ramené dans le passé (**anachronisme**) | culte de l'objet | religion technologique | **paradoxe** possible |

**Règles :**
- Les recettes sont **déterministes** (même entrée + même graine = même résultat sur tous les clients).
- Les recettes s'enchaînent sur 1 à 3 sauts d'époque.
- Une **règle d'environnement** modifie le résultat (eau, sol, proximité de PNJ, autres objets).
- Objectif : 30 recettes à l'Early Access, 60+ ensuite. Les recettes croisées (deux objets qui interagissent en vieillissant) sont la principale source de surprises.

### 3.4 Paradoxes
- Si un joueur du futur modifie un objet hérité et que le passé change ensuite cet objet, la modification du futur devient **instable** : l'objet clignote 3 s puis se transforme (« glitch »), avec une jauge de **Paradoxe** d'équipe.
- Jauge pleine = **Effondrement temporel** (fin de partie comique, mais on garde la récompense partielle).
- Le paradoxe est **un outil** : certains contrats l'exigent volontairement.

### 3.5 Contrats (objectifs)
Générés de façon procédurale à partir de modèles : *« Le client de l'an 900 veut [RÉSULTAT] à [LIEU] »*.
Exemples : un pont fonctionnel au-dessus du canyon ; une statue de canard géante vénérée ; un œuf de dragon qui éclot en l'an 900 ; une ville sans aucun arbre (contrat « méchant ») ; un trésor enterré au bon endroit.
- 1 objectif principal + 2 bonus + 1 « exigence absurde » (ex. : la statue doit faire un salut).
- Évaluation finale par le **Client** (PNJ) avec note de 1 à 5 étoiles.

### 3.6 Outils (déblocables)
| Outil | Effet |
|---|---|
| Pelle | creuser, enterrer |
| Pistolet à graines | planter à distance |
| Ancre temporelle | un objet ne vieillit pas (limité) |
| Sablier de poche | accélère localement le vieillissement (aperçu du futur) |
| Cabine temporelle | envoie **1 objet** d'une époque à une autre (anachronismes) |
| Socle de statue | capture ta pose → statue future |
| Corne d'appel | attire les animaux |

### 3.7 Dangers par époque
Comportements simples, lisibles, drôles (machines à états) : mammouth glouton (E0), percepteur qui confisque (E1), machines qui s'emballent et smog qui réduit la vision (E2), drones qui effacent les anachronismes (E3). Les dangers peuvent **aussi** vieillir (protéger un bébé mammouth peut créer une race domestique au futur).

### 3.8 Musée final et « Chronique »
- À la fin, l'équipe visite le **Musée de l'an 900** généré à partir du journal d'actions : statues, artefacts, frise chronologique.
- Un **guide PNJ** commente avec des textes générés par **modèles de phrases** (pas d'IA générative en jeu) : *« Ici, le Grand Trou de l'an 300, creusé par le légendaire Kévin pour une raison que la science ignore. »*
- Export d'une **carte-récap PNG** (statue la plus drôle, note du client, stats) + marqueurs de **Steam Game Recording** aux moments forts.

### 3.9 Mode Streamer (levier viral majeur)
- **Spectateurs du Temps** : lecture du chat Twitch **en lecture seule anonyme** (aucune connexion obligatoire). Les viewers votent des événements (`!meteore`, `!pluie`, `!mammouth`) pendant la pause café, nomment les statues.
- **Lobby viewers** : code d'invitation masquable, partie publique optionnelle.
- **Streamer-safe** : musique 100 % originale et déclarée sans risque DMCA, masquage des codes à l'écran, filtre de pseudonymes.

### 3.10 Progression et économie
- Monnaie in-game (« Chronos ») gagnée par contrat → outils, cosmétiques (chapeaux, couleurs, emotes), biomes.
- **Aucune microtransaction, aucune loot box** au lancement. DLC cosmétiques éventuels plus tard, achats directs uniquement.

### 3.11 Contrôles, caméra, prise en main
- Vue 3e personne, caméra libre. Clavier/souris + manette (Steam Deck « jouable » visé).
- Tutoriel de 3 minutes en Solo Relais : planter une graine en E0 → voir l'arbre en E1. Le « aha » doit arriver **avant la 60e seconde**.

---

## 4. Direction artistique et audio
- **Réalisme cinématographique chaleureux** : environnements photoréalistes (Lumen, Nanite, MegaLights, PCG, photogrammétrie Fab), humains MetaHuman, éclairage propre à chaque époque. L'humour vient des situations. Détails : `30_ART_BIBLE.md` et cahier de rendu `33_VISUAL_TARGETS.md` (plans à produire dans le moteur, critères d'acceptation).
- **Commandé à des professionnels** : créatures (Bouloche), capture de jeu d'acteur, capsule Steam, musique (`31_AUDIO_DESIGN.md`), avec contrats de cession de droits.
- **Audio** : thème de la Trace réorchestré par époque, MetaSounds adaptatifs, voix des PNJ en charabia sous-titré.

## 5. Architecture technique
Voir **`40_TECHNICAL_DESIGN.md` (v2, Unreal Engine 5.8)** : module C++ `TemporalCore` déterministe (event sourcing : graine + journal + recettes), hôte autoritaire (listen server, Iris, Online Subsystem Steam), une carte World Partition avec décor et éclairage par époque chargés localement, PCG d'exécution, tests Automation Spec / Functional Tests / Gauntlet, contenu binaire dans un dépôt **privé**.

## 6. Conformité juridique et normes

> Ce chapitre est un cadre de travail, pas un avis juridique. Faire valider par un professionnel (avocat en droit du numérique / expert-comptable) avant la mise en vente.

### 6.1 RGPD — protection des données (privacy by design)
| Donnée | Traitement | Base légale | Mesure |
|---|---|---|---|
| SteamID / pseudo Steam | Connexion réseau, lobbies, classements | Exécution du contrat (fournir le jeu) | Jamais stocké hors Steam ; pas de serveur propre |
| Voix | Transmise en direct entre joueurs via Steam | Exécution du contrat | **Jamais enregistrée** ; mute/blocage ; amis seulement par défaut |
| Télémétrie de jeu | Désactivée par défaut | **Consentement** (opt-in) | Anonyme, hébergée UE, IP tronquée, révocable |
| Rapports de crash | Désactivés par défaut | Consentement | Sans données personnelles, hébergés UE |
| Chat Twitch | Lecture anonyme des commandes en mémoire | Intérêt légitime / contrat | Rien n'est stocké, pseudos non persistés |
| Codes capsule | Graine + actions | — | Aucune donnée personnelle incluse |

À produire : politique de confidentialité (FR/EN), mentions légales (LCEN), CLUF/EULA, écran de consentement au 1er lancement, bouton « Supprimer mes données locales », registre des traitements (`docs/privacy/registre.md`). **Pas d'analytics tiers publicitaires.**

### 6.2 Mineurs et sécurité
- Cible PEGI 7-12 (violence cartoon légère). Obtenir une classification via **IARC** si sortie consoles/stores mobiles.
- Voix et lobbies : **amis uniquement par défaut**, parties publiques en opt-in, mute/blocage/signalement, filtre de pseudos et de textes.
- Aucune mécanique de jeu d'argent, aucune loot box (conformité Belgique/Pays-Bas et éthique).

### 6.3 Accessibilité
- Micro **jamais obligatoire** (pings, emotes, texte rapide).
- Sous-titres de tous les dialogues, taille de texte réglable, palettes daltonisme (les époques se distinguent aussi par formes et icônes), remappage complet, réduction des mouvements de caméra/effets glitch, mode « sans clignotements » (épilepsie).
- Suivre les *Game Accessibility Guidelines* ; vérifier l'applicabilité de l'*European Accessibility Act* à la fonction de communication vocale.

### 6.4 Droits d'auteur et licences
- **Aucun contenu tiers protégé** : pas de personnages, marques, musiques ou polices sous licence restrictive.
- Chaque asset tiers : dossier avec `SOURCE.md` (URL, auteur, date) + `LICENSE`. Licences acceptées : **CC0, MIT, OFL (polices), Apache-2.0**, plus les licences **Fab, MetaHuman et le CLUF Unreal Engine** pour le contenu Epic — jamais redistribués dans un dépôt public. Script `tools/license_audit.py` qui bloque la CI si un asset n'a pas sa licence.
- Fichier `THIRD_PARTY_LICENSES.md` affiché dans le menu « Crédits » (mentions requises par le CLUF Unreal Engine, Fab, MetaHuman, polices OFL).
- Musique et capsule commandées : **contrat de cession de droits** écrit, précisant étendue, durée, territoires et supports (exigence du Code de la propriété intellectuelle).
- SDK Steamworks : redistribuer uniquement les fichiers autorisés par l'accord Steamworks.

### 6.5 IA générative
- Le code écrit avec Claude Code relève des **outils de développement**, que Valve a exclus de la déclaration depuis la refonte de janvier 2026.
- Si un **contenu livré** est généré par IA (texture, texte, voix), le déclarer dans le questionnaire Steam (« pré-généré »). Recommandation : **ne pas en livrer** (assets procéduraux + humains), car la perception des joueurs reste sensible.
- Aucune IA générative en temps réel dans le jeu (évite la catégorie « live-generated » et ses obligations de garde-fous).

### 6.6 Marque et nom
- Vérifier « Century Temps » et alternatives sur : **INPI**, **EUIPO / TMview**, **USPTO**, Steam, itch.io, stores mobiles, noms de domaine, réseaux sociaux.
- Déposer la marque (au minimum UE, classes 9 et 41) avant l'annonce publique.

### 6.7 Structure, fiscalité, emploi
- Créer une structure adaptée (micro-entreprise ou société) avant les premières ventes ; remplir l'**entretien fiscal Steam** (formulaire W-8BEN pour un non-Américain). Valve collecte et reverse la TVA dans l'UE. Faire valider par un expert-comptable.
- **Contrat de travail salarié** : vérifier la clause d'exclusivité / de propriété intellectuelle et les règles de cumul d'activité avant de commercialiser.

### 6.8 Plateformes tierces
- Respecter l'accord de distribution Steamworks, les règles de contenu de la page Steam, et les conditions développeur Twitch (lecture du chat sans authentification, aucun stockage).

---

## 7. Business et lancement

### 7.1 Modèle
- **Premium, prix indicatif 19,99 €** (à valider selon le contenu réel ; prix régionaux Steam activés), Early Access, -10 % au lancement. Redevance Unreal : 5 % au-delà de 1 M$ de revenus bruts cumulés (ventes Epic Games Store exonérées).
- Pas de free-to-play, pas de pub, pas de microtransactions.
- **Démo jouable en multi** (1 carte, 2 époques) pour Steam Next Fest : les joueurs de la démo peuvent rejoindre des amis.

### 7.2 Calendrier indicatif
Voir `50_PRODUCTION_PLAN.md` (portes G0-G7) et `docs/guides/03_TEMPS_ET_COUTS.md` : **18 à 36 mois** selon l'équipe.

### 7.3 Indicateurs de décision
| Étape | Seuil de « go » |
|---|---|
| Prototype (M1) | 5 testeurs sur 5 rient ou s'exclament dans les 10 premières minutes |
| Page Steam avant Next Fest | ≥ 7 000 wishlists |
| Next Fest | ≥ 20 000 wishlists, temps médian démo ≥ 20 min |
| Lancement EA | Évaluations ≥ 85 % positives |

### 7.4 Marketing
- Vidéos courtes hebdomadaires « avant/après des siècles » (TikTok, Shorts, Reels) dès le prototype.
- Programme créateurs (clés, lobby viewers, mode streamer mis en avant).
- Serveur communautaire, Steam Workshop pour graines/capsules (phase 2).

### 7.5 Budget estimé
Le passage au réalisme multiplie les coûts. Trois scénarios détaillés dans `docs/guides/03_TEMPS_ET_COUTS.md` : **solo + IA ≈ 40 000 – 80 000 €**, **studio réduit ≈ 150 000 – 300 000 €**, **petite équipe ≈ 500 000 € – 1,2 M€**, hors rémunération du porteur.

---

## 8. Plan de réalisation pour Claude Code
Voir **`80_CLAUDE_CODE_PLAYBOOK.md` (v2)** et les skills du dépôt (`.claude/skills/`). Le skill `game-studio` pilote les phases P0 → P8 et les portes de décision.

---

## 9. Risques et parades
| Risque | Probabilité | Parade |
|---|---|---|
| Le concept est copié après les premiers clips | Moyenne | Montrer tôt quand même (wishlists), mais garder le moteur de recettes profond et les modes inédits pour le lancement |
| La propagation devient incompréhensible | Moyenne | Règle des « 3 secondes », aperçu au sablier, recettes limitées à 3 sauts |
| Désynchronisation réseau | Moyenne | Event sourcing + hash de contrôle + golden tests |
| Jeu fun à 4 mais vide en solo | Moyenne | Solo Relais et Capsule conçus dès la phase 5 |
| Saturation des voix/micros | Faible | Micro facultatif, voix seulement en bonus |
| Dépassement de périmètre | Élevée | Phases verrouillées, critères d'acceptation, playtests obligatoires |
| Aucun hit n'est garanti | Certaine | Seuils go/no-go §7.3, budget limité, réutilisation du moteur pour un 2e jeu |

---

## 10. Sources de l'étude
- KitGuru / Alinea Analytics — revenus Steam 2026 et meilleures sorties : https://www.kitguru.net/?p=746129
- Khel Now — titres les plus rentables 2026 : https://khelnow.com/gaming/steams-highest-grossing-games-202609
- Digital Citizen — Meccha Chameleon 15 M ventes : https://www.digitalcitizen.life/meccha-chameleon-sells-15-million-copies-on-steam-in-less-than-a-month/
- OneStream — Meccha Chameleon et lobbies viewers : https://onestream.live/blog/meccha-chameleon-twitch-viewer-lobbies/
- Wemade Stories — diffusion par formats courts : https://stories.wemade.com/en/en-mecha-chameleon-viewpoint/
- Game World Observer — revenu médian Steam 2026 et taux de hit par genre : https://gameworldobserver.com/2026/09/01/the-median-revenue-of-games-on-steam-has-been-declining-for-12-consecutive-years
- WN Hub — benchmark des genres S1 2026 : https://wnhub.io/news/stores-and-publishing/item-51469
- Refurbo — classements indés 2026 : https://refurbo.in/blogs/best-indie-games-of-2026-whats-topping-steam-charts
- Wikipedia — Friendslop : https://en.wikipedia.org/wiki/Friendslop
- Game Industry Library — évolution du friendslop : https://gameindustrylibrary.com/research/shared/6-how-has-the-friendslop-genre-evolved
- Cinevva — design coop 2026 : https://app.cinevva.com/guides/co-op-game-design
- GameGeeker — Schedule I : https://gamegeeker.com/it/games/schedule-i-3164500/review
- Notebookcheck / VGC — politique IA de Steam (janvier 2026) : https://www.notebookcheck.net/Steam-updates-AI-disclosure-form-requiring-developers-to-report-visible-and-in-game-AI-but-not-background-tools.1206103.0.html
- Steam — jeux « voix = lumière » existants : https://store.steampowered.com/app/4655570/ , https://store.steampowered.com/app/3270450
- Précédents coop inter-époques : https://www.pocketgamer.com/the-past-within/review/ , https://traveler3114.itch.io/splitstream , https://chemist02.itch.io/friends-across-time
- Unreal Engine — licence : https://www.unrealengine.com/en-US/license
- Unreal Engine 5.8 (17 juin 2026) : https://80.lv/articles/unreal-engine-5-8-is-out-today-with-big-optimization-improvements-and-mesh-terrain
- Plugin officiel Epic pour Claude Code : https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin
- MetaHuman — licence : https://www.cgchannel.com/2025/06/you-can-now-sell-metahumans-or-use-them-in-unity-or-godot/
- Megascans payants après 2024 : https://80.lv/articles/megascans-no-longer-free-after-2024/
