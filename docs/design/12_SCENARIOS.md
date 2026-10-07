# 12 — Scénarios de jeu
Propriétaire : Product Owner · v1.0

## 1. Séance type à 4 joueurs (20 minutes)
Joueurs : Alex (E0), Noa (E1), Kim (E2), Lou (E3). Contrat : *« Le client veut un pont fonctionnel au-dessus du canyon de la Brume en l'an 900. Bonus : une statue à l'entrée du pont. Bonus : un troupeau visible depuis le pont. Exigence absolue : le pont doit être rouge. »*

| Temps | Ce qui se passe | Ce que le joueur voit/entend |
|---|---|---|
| 0:00 | Lobby : choix des chapeaux, Odile lit le brief | Carte de contrat, 4 silhouettes |
| 0:30 | **Manche 1** commence. Il n'y a pas de canyon : seulement la rivière. Alex (E0) creuse une tranchée au nord pour dévier l'eau | Noa (E1) voit un ruisseau apparaître en direct, le fantôme ocre d'Alex creuse devant elle |
| 1:10 | Kim (E2) : « Y a un lac qui se forme chez moi, c'est normal ? » Alex a barré la Brume avec des branches | Lou (E3) : « Chez moi c'est une station balnéaire, y a des parasols. » |
| 2:00 | Noa pose des pierres rouges (pigment) le long du futur canyon ; Fiscalin confisque la moitié | Bark BRK_FISCALIN_TAX ; Noa donne une cuillère brillante (MH_04) |
| 3:30 | Kim redirige un Automate pour transformer les troncs d'Alex en planches ; smog | Valve trouvée, bark BRK_SMOG |
| 4:40 | Lou tente de placer un objet néon dans le passé via la cabine : anachronisme, Chronomites | PARADOX_25 |
| 5:00 | **Pause café** : cinématique accélérée. La tranchée devient canyon, les planches deviennent un pont de bois rouge délavé | Vote des spectateurs (si streaming) : `!pluie` → le pigment s'étale |
| 5:30 | **Rotation** : Alex → E1, Noa → E2, Kim → E3, Lou → E0 | CAFE_ROTATE |
| 5:30-10:30 | **Manche 2**. Lou en E0 nourrit Bouloche (troupeau pour le bonus). Kim en E3 découvre que le pont est rose (délavé) : il faut repeindre en amont | Interdépendance obligatoire : Alex (E1) repeint |
| 10:30 | Pause café 2 ; jauge paradoxe à 45 (Kim a renforcé le pont en E3, Alex a changé les planches en E1) | PARADOX_50, Chronomites |
| 11:00-16:00 | **Manche 3**. Lou (E1) prend la pose « salut » sur le socle à l'entrée du pont. Noa (E3) fabrique un faux certificat contre la Brigade | BRK_BRIGADE_FAKE |
| 16:00 | Fin. Évaluation : pont ✅ rouge ✅ statue ✅ troupeau ✅ (mascotte « Petit Bouloche ») → **5 étoiles** | RATE_5_A |
| 16:30-19:00 | **Musée** : ARCHIVE guide ; CHR_HOLE_01 sur le canyon, CHR_STATUE_01 « Statue du Saluant », CHR_HERD_01 | Rires, captures, marqueur Timeline |
| 19:00 | Carte-récap : « Statue la plus drôle : Lou », 4 moments forts, bouton Partager, +180 Chronos chacun | Retour lobby |

**Ce que ce scénario exige des systèmes :** rivière déviable (terrain déformable sur grille), recettes tranchée→ruisseau→canyon, branches→étang→lac→station, troncs→planches (Automate), pigment→délavage, pose→statue, anachronisme→Chronomites, paradoxe amont/aval, vote spectateurs, musée généré.

## 2. Douze contrats de référence (Early Access)
| # | Contrat (Lendemain veut…) | Chemin « prévu » | Dépendances inter-époques | Vecteurs de chaos | Exigence absurde type |
|---|---|---|---|---|---|
| C01 | Un arbre qui fait de l'ombre à la place du marché (E1) | Graine en E0 au bon endroit | E0→E1 | Bouloche mange la pousse ; graine trop près de l'eau = forêt qui bloque le marché | L'arbre doit avoir une balançoire |
| C02 | Un monument vénéré sur le Mont Têtu (E2) | Cairn en E0 ou E1 | 2 sauts | Fiscalin confisque les pierres ; Automate pave le cairn | Le monument doit être « un peu penché » |
| C03 | Le Trésor du Baron retrouvé (E3) | Se faire confisquer volontairement des objets brillants en E1 | E1→E3 | Enterrer au mauvais endroit ; Brigade recycle | Le trésor doit contenir une cuillère |
| C04 | Un port fluvial (E2) | Élargir la Brume en E0 (tranchées) + barrage | E0→E2 | Lac trop grand = usine inondée | Le port doit s'appeler comme un joueur |
| C05 | Un troupeau légendaire (E2) | Nourrir Bouloche en E0, le protéger en E1 | 2 sauts | Fiscalin taxe le mammouth | Le troupeau doit porter des chapeaux (anachronisme !) |
| C06 | Une forêt là où il y a une usine (E3) | Planter en E0/E1 dans la zone industrielle future | 3 sauts | Automates rasent ; Brigade « nettoie » | La forêt doit cacher la cheminée |
| C07 | Une statue de canard géante vénérée (E3) | Pose « canard » sur socle en E0, fan-club en E1 | 3 sauts | Pose mal faite = statue « inquiétante » | La statue doit regarder vers l'ouest |
| C08 | Un canyon avec un pont rouge (E3) | Tranchée E0, planches E2, pigment E1 | 3 sauts croisés | Délavage, paradoxe | Le pont doit être rouge |
| C09 | Un champ de pommiers (E1) | Feu « contrôlé » en E0 (sol fertile) + graines | E0→E1 | Le feu brûle la hutte des Voisins ; Bouloche | Les pommes doivent être bleues (pigment) |
| C10 | Un objet du futur adoré en l'an 300 (E1) | Cabine temporelle depuis E3 | E3→E1 (anachronisme volontaire) | Chronomites ; Brigade en E3 | L'objet doit être élu maire (fan-club ≥ 10) |
| C11 | **Une vallée propre** (E3) — chapitre 4 | Retirer traces ; ou saboter avec style | tous | Dilemme ; Mamie Horloge | Aucun arbre visible depuis le musée |
| C12 | **Le Vernissage** (E3) — chapitre 5 | ≥ 12 traces distinctes de ≥ 3 types dans chaque époque | tous | Tout à la fois | Le musée doit « déborder » (score de richesse ≥ seuil) |

Chaque contrat est décrit en données (`data/contracts/`) par : résultat attendu (type d'entité + zone + époque), conditions bonus, exigence absurde (liste), seuils de score, outils requis, chapitre.

## 3. Allocation des époques selon le nombre de joueurs
| Joueurs | Époques jouées | Époques simulées | Note |
|---|---|---|---|
| 4 | E0, E1, E2, E3 | — | Rotation complète |
| 3 | E0, E1, E2 | E3 (résultat) | E3 est révélée à la pause café et visitée au musée ; la Brigade n'agit qu'en simulation |
| 2 | E0, E2 (par défaut) ou E1, E3 (option) | les deux autres | Écart de 600 ans = effets plus spectaculaires |
| 1 (Solo Relais) | E0 → E1 → E2 → E3 successivement | — | 4 manches de 4 min ; le joueur hérite de lui-même |

**Simulation des époques vides :** à la pause café, les dangers des époques vides agissent selon des règles simples et déterministes (Bouloche mange 30 % des pousses non protégées ; Fiscalin confisque 50 % des objets brillants en zone publique ; Automates traitent les objets à moins de 4 m des rails ; Brigade recycle 100 % des anachronismes sans certificat).

## 4. Cas limites et comportements attendus
| Situation | Comportement |
|---|---|
| Un joueur se déconnecte | Son époque devient « simulée » jusqu'à son retour ; ses actions passées restent ; reconnexion possible (graine + journal) |
| L'hôte quitte | Fin de mission, prime partielle (50 % des Chronos acquis), capsule de reprise générée et affichée à tous |
| Jauge de paradoxe à 100 | Effondrement : cinématique 10 s, musée « aile fermée », 50 % des Chronos, la partie compte comme jouée |
| Joueur AFK > 90 s | Icône « sieste » ; les autres peuvent voter un rapatriement (kick) à l'unanimité |
| Un joueur bloque physiquement les autres (griefing) | Pas de collision entre joueurs ; vote de rapatriement ; chaque action est validée par l'hôte (portée, cooldown) |
| Deux joueurs agissent sur la même trace la même seconde | L'hôte ordonne par tick puis par identifiant de joueur ; le second reçoit « Trop tard ! » |
| Un objet atteint le bord de la carte | Mur invisible « Lisière du Bail » + bark MH |
| Graine pas d'arbre possible (pierre partout) | La recette produit « graine fossile » (rien) ; le sablier le montre à l'avance |
| Capsule d'une version plus ancienne | Migration si possible, sinon CAPSULE_INVALID |
| Contrat impossible après le chaos | Le Client accepte une **solution alternative** : tout résultat du même type dans un rayon de 30 m donne 60 % des points |

## 5. Scénario streaming (mode Streamer activé)
1. Le streamer active « Spectateurs du Temps » (lecture anonyme du chat, aucune connexion requise) et rend son lobby public avec code masqué.
2. Pendant chaque manche, le chat **nomme** la prochaine statue (`!nom Jean-Mammouth`) ; filtre de mots + longueur ≤ 16.
3. À la pause café, vote entre 3 événements : `!meteore` (cratère → lac), `!pluie` (pousse ×2, pigments délavés), `!mammouth` (Bouloche supplémentaire). Résultat annoncé (STREAM_VOTE_RESULT).
4. Les viewers qui possèdent le jeu rejoignent par la file « Prochains intérimaires » (rotation automatique entre parties, 4 max).
5. Overlay optionnel « Chronique en direct » : les phrases d'ARCHIVE s'affichent au fur et à mesure.
6. Rien n'est stocké : ni pseudos, ni messages.

## 6. Scénario Solo Relais (12-16 minutes)
Le joueur joue E0 (4 min), puis hérite de lui-même en E1, E2, E3. La tension vient de la mémoire : « Pourquoi j'ai mis ça là ? ». Mamie Horloge est plus bavarde. Les dangers sont réduits de 30 %. Score sur le même barème. Sert de **tutoriel** et de mode « pause déjeuner ».

## 7. Scénario Capsule asynchrone
1. Alex joue E0 seul (5 min). Le jeu génère un **code capsule** (≈ 300 à 1 500 caractères) ou un lien `steam://` vers le Workshop (phase 2).
2. Il l'envoie à Noa. Elle le colle : elle joue E1 sur la vallée vieillie d'Alex, sans lui.
3. Noa renvoie une capsule E1 ; Kim joue E2 ; Lou joue E3 ; le musée final est partagé par un dernier code ou une image-récap.
4. Variante compétitive : « Capsule mystère » hebdomadaire (graine mondiale, classement du score de musée).

## 8. Scénario Saboteur du Temps (4 joueurs, 20 min)
Un joueur reçoit secrètement le rôle : créer l'Effondrement sans être démasqué. Il dispose d'un outil caché (la Clé à paradoxe : convertit une trace en non-conformité). À chaque pause café, vote de 20 s ; un joueur accusé à tort fait perdre 10 points de paradoxe à l'équipe (le Bail grince). Victoire du Saboteur si Effondrement ; victoire de l'équipe si contrat ≥ 3 étoiles ou Saboteur rapatrié.

## 9. Scénario Défi du jour
Graine mondiale quotidienne (UTC), contrat identique pour tous, 1 à 4 joueurs, 1 essai par équipe par jour. Score = points de contrat + richesse du musée − paradoxes. Classement Steam (amis et mondial). Récompense : chapeau du jour.
