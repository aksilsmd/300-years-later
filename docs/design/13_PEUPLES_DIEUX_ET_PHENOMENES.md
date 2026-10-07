# 13 — Peuples, Figures, météo et catastrophes
Propriétaire : Product Owner · v1.0 · 7 octobre 2026
> **EN —** Peoples and civilisations, emergent gods and prophets, weather, natural disasters and phenomena.
> All of it is **made by the players** and computed deterministically from the traces they leave.
> Normative for these systems; numbers live in `data/tuning.json`, content in `data/`.

Ce document ajoute la couche vivante qui manquait : **qui habite la vallée, ce qu'ils croient, et ce que le
ciel leur fait**. Rien n'est scripté : tout est calculé à la pause café à partir des traces, avec les mêmes
règles déterministes que le moteur de vieillissement (`40_TECHNICAL_DESIGN.md` §2.4).

---

## 0. Garde-fous (non négociables)

Ce document remplace la règle « jamais de vocabulaire religieux » de `10_NARRATIVE_BIBLE.md` §10 par une
règle plus précise, qui protège la même chose :

1. **Rien de réel.** Aucune divinité, figure, écriture, symbole, rite, fête ou formule existante. Les Figures
   de la vallée naissent **d'objets laissés par les joueurs** : une cuillère, un canard de pierre, un arbre.
2. **Le vocabulaire est celui de la vallée**, inventé : *Figure*, *Ferveur*, *Porte-Voix*, *Serment*,
   *Veillée*. Jamais les noms d'institutions ou de fonctions religieuses du monde réel.
3. **La satire vise les institutions** — l'agence, la Compagnie, le percepteur — **jamais les croyants**. Les
   habitants sont sincères, chaleureux et parfois ridicules ; on rit avec eux.
4. **Aucune violence de croyance.** Pas de guerre sainte, pas de sacrifice, pas de martyr, pas de damnation.
   Les conflits de Figures sont **bureaucratiques et comiques** (procès en authenticité, concours d'affluence).
5. **PEGI 7-12.** Les catastrophes ne tuent personne : elles déplacent, transforment, désorganisent. Les PNJ
   s'en relèvent, parfois améliorés.
6. **Accessibilité.** Toute météo et toute catastrophe respecte `32_UX_UI_SPEC.md` §6 : option « réduire les
   clignotements » (pas d'éclair stroboscopique, pas de flash > 3 Hz), signalement **sonore + icône + texte**
   en plus de la couleur, option « intempéries douces » qui réduit les effets d'écran sans changer les règles.

---

## 1. Les Peuples — la vallée est habitée, et son histoire bifurque

### 1.1 Principe
Un **Peuple** est une lignée qui traverse les époques. À chaque passage d'époque, le Peuple ne se contente pas
de vieillir : il **bifurque** selon l'état que les joueurs lui ont laissé. C'est la réponse à « une seule
vallée pour toujours » : la carte est la même, la civilisation qu'on y trouve ne l'est pas.

### 1.2 Les cinq jauges d'un Peuple (0-100, entiers, calculées à chaque pause café)
| Jauge | Alimentée par | Lue par |
|---|---|---|
| **Eau** | cellules d'eau à moins de 40 m de l'habitat, étangs, lacs, rivières | survie, agriculture, bifurcations |
| **Vivres** | champs, forêts, bosquets, troupeaux, sol fertile | population, prospérité |
| **Abri** | huttes, murs, cairns, ponts, routes | résistance aux catastrophes |
| **Ferveur** | traces `symbolic`, fan-clubs, statues, monuments (voir §2) | Figures, miracles, Porte-Voix |
| **Rancune** | huttes brûlées, traces détruites par l'aval, confiscations, pollution, anachronismes imposés | révoltes, bifurcations sombres |

Toutes sont des **sommes d'entiers** sur la grille, bornées à 100. Aucune dépend de l'horloge ou du hasard
non graine : même partie, même résultat (contrainte `TemporalCore`).

### 1.3 L'arbre des civilisations (Early Access)
Chaque flèche est une règle lisible, évaluée à la pause café. En cas d'égalité, la branche **par défaut** gagne.

**E0 — Les Premiers Voisins** (toujours le point de départ : clan paisible, peintures de mains, vénération du brillant)
- Vivres ≥ 40 et Eau ≥ 30 → **E1 · Le Bourg de Brumecombe** *(défaut)* — marché, foire, Fort Têtu, Sire Fiscalin
- Eau < 30 → **E1 · Les Nomades du Plateau** — tentes, pas de marché fixe ; Fiscalin devient itinérant et rate la moitié de ses prises ; les objets posés survivent mieux
- Ferveur ≥ 60 → **E1 · Les Gardiens de la Figure** — le bourg s'organise autour de la trace la plus fervente ; les objets *proches de la Figure* sont intouchables (même par Fiscalin), ceux qui en sont loin sont négligés

**E1 → E2**
- Rancune ≥ 50 → **Les Ateliers Libres** — pas d'Automates sur rails mais des artisans lents : les transformations sont **choisies** par les PNJ, pas subies ; moins de smog
- Ferveur ≥ 60 → **Les Fumées Dévotes** — la Grande Bouilloire est elle-même une Figure ; la Compagnie protège les traces ferventes et détruit les autres
- sinon → **La Compagnie des Fumées** *(défaut)* — rails, Automates, smog

**E2 → E3**
- Pollution ≥ 60 → **Brumecombe-Park / Le Lendemain** *(défaut)* — parc d'attractions, Brigade Propreté, touristes-robots
- Ferveur ≥ 60 et Pollution < 40 → **La Commune du Jardin** — pas de Brigade ; les touristes sont des visiteurs respectueux ; les anachronismes sont « des reliques », donc tolérés ; le musée est en plein air
- Vivres < 20 ou Abri < 15 → **Le Musée Vide** — la vallée s'est vidée ; plus aucun PNJ, le musée est automatique, la Chronique devient mélancolique et **le score de richesse compte double** (l'histoire est tout ce qui reste)

Soit **neuf états d'arrivée possibles** en l'an 900 à partir des mêmes quatre époques. Chaque état change les
dangers, les PNJ, la musique et le musée. C'est la variété que le contenu seul ne pouvait pas payer.

### 1.4 Ce que le joueur voit
À la pause café, une **frise des peuples** s'affiche sous la frise des époques : un bandeau par époque avec le
nom du Peuple, son icône, et la jauge qui a basculé la bifurcation (« Eau 28 → Nomades »). Trois secondes,
lisible, et surtout **on comprend que c'est nous qui l'avons fait**.

---

## 2. Les Figures — les dieux sont nos déchets

### 2.1 Comment une chose devient une Figure
Toute trace accumule de la **Ferveur** quand les PNJ l'approchent, la contemplent, la contournent, s'y
abritent. La Ferveur est un entier porté par la trace, propagé par les recettes comme le reste.

| Ferveur | Statut | Ce qui change |
|---|---|---|
| 0-29 | Trace ordinaire | rien |
| 30-69 | **Figure locale** | un nom généré apparaît sur une plaque ; les PNJ font un détour ; Fiscalin n'ose plus confisquer |
| 70-100 | **Figure majeure** | un **Porte-Voix** apparaît (§3) ; la Figure accorde un **Bienfait** et réclame un **Serment** (§2.3) |

Sources de Ferveur (par pause café) : +3 par PNJ passé à moins de 3 m · +5 si la trace a survécu à une
catastrophe · +8 si elle est la plus haute/la plus ancienne de sa zone · +10 si un contrat la cite · −5 si
une trace concurrente du même domaine monte plus vite · −15 si elle est détruite puis reconstruite ailleurs
(« ce n'est plus la vraie »).

### 2.2 Le domaine, hérité de l'objet
Le domaine d'une Figure n'est pas choisi : il vient des étiquettes de la trace d'origine. C'est ce qui rend le
système lisible — on sait toujours *pourquoi* ce truc est devenu important.

| Trace d'origine | Domaine | Nom type (généré) |
|---|---|---|
| arbre, forêt, graine | **Croissance** | « Le Grand Ombrageux », « La Mère des Pommes » |
| rivière, étang, barrage | **Eau** | « Celle Qui Coule En Rond » |
| statue d'une pose de joueur | **Geste** | « Le Saluant », « L'Accroupi Éternel » |
| cuillère, objet brillant confisqué | **Éclat** | « La Cuillère Qui Ne Sert Plus » |
| feu, forge, Bouilloire | **Chaleur** | « La Grande Tiède » |
| objet anachronique (cabine) | **Ailleurs** | « Le Machin Venu d'Après » |
| cairn, monument, tombe | **Mémoire** | « L'Empilé » |

Les noms sont assemblés par modèles de phrases (`data/phrases/`), jamais générés par IA en jeu.

### 2.3 Bienfaits et Serments
Chaque Figure majeure donne **un Bienfait** (effet passif dans les époques suivantes) et demande **un
Serment** (une contrainte). Le Serment n'est jamais une obligation morale : c'est une habitude du Peuple, et
la rompre fait **bouder** la Figure, pas punir le joueur.

| Domaine | Bienfait | Serment (si rompu : Bienfait inversé pendant une manche, et les PNJ boudent avec des répliques comiques) |
|---|---|---|
| Croissance | pousse ×1,5 dans un rayon de 30 m | aucun feu dans ce rayon |
| Eau | la sécheresse épargne la zone | ne pas assécher la source d'origine |
| Geste | les statues de la zone résistent à l'érosion | une pose identique doit exister à chaque époque |
| Éclat | Fiscalin et la Brigade ignorent la zone | y laisser un objet brillant à chaque manche |
| Chaleur | le gel épargne la zone ; feux contrôlés plus sûrs | la Bouilloire ne doit jamais s'éteindre |
| Ailleurs | les anachronismes de la zone ne sont pas recyclés | il doit en rester **exactement un** (un deuxième annule tout) |
| Mémoire | les traces de la zone ne peuvent pas être effacées par une catastrophe | ne jamais déplacer la trace d'origine |

**Pourquoi c'est bon pour le jeu :** c'est la première mécanique où le joueur *protège* quelque chose. Les
dangers n'enlevaient que des objets interchangeables ; maintenant on a une Figure à soi, avec un nom, que
l'on a envie de garder. Cela répond au manque « rien n'est jamais perdu » (`reviews/2026-10-07`, M5).

### 2.4 Conflits de Figures (comiques, jamais violents)
Deux Figures du même domaine à moins de 60 m → **Procès en Authenticité** à l'époque suivante : les PNJ se
divisent, une affiche apparaît, et à la pause café suivante celle qui a le plus de Ferveur absorbe l'autre
(l'absorbée devient « site annexe », garde 30 % de sa Ferveur et une plaque vexée). Zéro affrontement : une
querelle de clocher, des pancartes, et beaucoup de mauvaise foi.

---

## 3. Les Porte-Voix — des personnages à aimer

Un **Porte-Voix** apparaît quand une Figure dépasse 70. C'est un PNJ nommé, visible, bavard, qui suit la
Figure, en parle à tout le monde, et dont le comportement change le jeu. Il peut être aidé (il accélère la
Ferveur) ou gêné (il se vexe, part ailleurs, revient fâché). Il est **le visage** du système.

| Porte-Voix | Époque | Ce qu'il fait | Voix (guide d'écriture) | Comment il change la partie |
|---|---|---|---|---|
| **Petit Moss** | E0 | Enfant des Premiers Voisins, toujours barbouillé, a « vu la Figure bouger » | Phrases courtes, s'emballe, se contredit, finit chaque phrase par « …je crois » | Suit le joueur qui nourrit Bouloche. Double la Ferveur gagnée, mais raconte **n'importe quoi** : une chance sur deux que le domaine soit mal transmis à E1 (quiproquo durable et drôle) |
| **Dame Orielle** | E1 | Chroniqueuse du bourg, tient un registre rival de celui de Fiscalin | Précieuse, ironique, adore les détails inutiles ; parle en listes | Si on lui montre une trace, elle l'inscrit : +10 Ferveur garantis. Si Fiscalin confisque devant elle, Rancune +15 pour tout le bourg |
| **Contremaître Bouilly** | E2 | A décrété que la Grande Bouilloire est vivante ; lui parle, la borde le soir | Chaleureux, bourru, tutoie les machines, s'inquiète pour elles | Tant qu'il est content, les Automates **épargnent** les traces ferventes. Si la Bouilloire s'éteint, il se tait pendant une manche entière et les Automates deviennent zélés |
| **Vé-7** | E3 | Drone de la Brigade **déserteur**, qui s'est pris d'affection pour une statue | Jingle de la Brigade joué trop lentement ; vocabulaire d'entreprise qu'il détourne mal | Protège une Figure contre ses anciens collègues. On peut le « recharger » : il devient alors l'allié le plus utile du jeu — ou être dénoncé par Lendemain |
| **Mamie Horloge** | toutes | Déjà présente (`10` §6). Elle **ne commente jamais les Figures** — sauf au chapitre 5 | inchangée | Son silence est un indice : elle sait d'où vient la Ferveur (§6) |

---

## 4. La météo — une conséquence, pas un décor

### 4.1 Principe
La météo d'une époque n'est pas tirée au sort : elle découle d'un **Indice Climatique** calculé sur la vallée
(couvert forestier, surface d'eau, pollution, sol nu), plus la graine. Déboiser en l'an 0 se voit en l'an 900
par un ciel différent. C'est la règle « cause → conséquence visible » appliquée au ciel.

| Météo | Apparaît quand | Effet de jeu | Signe visuel et sonore |
|---|---|---|---|
| **Clair** | défaut | — | — |
| **Pluie** | Eau élevée, forêt ≥ 40 % | pousse ×2, pigments délavés ×2, feux impossibles | gouttes, sol qui brille, son de pluie |
| **Brume** | près de l'eau, matin, Marais | visibilité 25 m ; les fantômes des autres époques sont **plus** visibles | nappe basse, sons étouffés |
| **Vent du Plateau** | Plateau nu, forêt < 25 % | objets légers déplacés d'1 cellule, érosion ×2, les graines se plantent 3 m plus loin | poussière horizontale, sifflement |
| **Canicule** | forêt < 20 % et Eau < 30 | risque d'incendie ×3, l'eau baisse d'un niveau | air qui tremble, cigales, lumière dure |
| **Gel** | altitude + saison + Eau élevée | l'eau devient praticable, la pousse s'arrête, les traces organiques sont **préservées** | givre, craquements |
| **Pluie acide** | pollution ≥ 60 (E2/E3) | le métal rouille d'un cran par manche, les plantes non protégées meurent | gouttes vertes, grésillement |

La météo change **au maximum une fois par manche**, annoncée 15 s à l'avance (nuage qui arrive, son), pour
rester lisible et jamais injuste.

### 4.2 Dérive climatique entre époques
L'Indice Climatique se transmet d'une époque à l'autre comme une trace. Une vallée déboisée en E0 arrive en E3
avec un ciel permanent de Canicule et une rivière maigre — et le Musée en parle. Une vallée reboisée arrive
verte, et la Commune du Jardin devient possible (§1.3). **Le climat est un score que l'équipe fabrique.**

---

## 5. Les catastrophes — l'enjeu qui manquait

### 5.1 Règles communes
Chaque catastrophe est **annoncée** (signes pendant la manche), **évitable ou atténuable** (une action claire
existe), **non létale** (personne ne meurt, jamais), et **transformatrice** (elle ne détruit pas au hasard :
elle rebat les traces et crée des histoires). Elle se déclenche à la pause café quand un indice dépasse son
seuil — donc **toujours par la faute, ou grâce, à quelqu'un**.

| Catastrophe | Déclencheur | Signes avant-coureurs | Effet | Atténuation | Ce qu'elle crée |
|---|---|---|---|---|---|
| **Crue** | barrages ≥ 3 ou pluie 2 manches | la rivière monte, les oiseaux partent | l'eau monte de 2 niveaux pendant une manche ; objets légers emportés en aval **et redéposés ailleurs** | ouvrir une tranchée de délestage | des objets voyagent : le meilleur générateur d'anecdotes du jeu |
| **Sécheresse** | forêt < 20 % et Canicule 2 manches | l'eau baisse, la terre craque | pousse ÷2, l'eau recule de 2 cellules, Vivres −20 | planter, creuser un puits, barrage | les Nomades du Plateau (§1.3) |
| **Incendie** | Canicule + feu non éteint | fumée, crépitement, herbe jaune | se propage de cellule en cellule sur l'organique sec, s'arrête à l'eau et au sol nu | coupe-feu (tranchée), pluie, étouffer | sol fertile ensuite : la catastrophe **enrichit** |
| **Glissement de terrain** | pente creusée > 2 cellules sous le Mont | cailloux qui roulent, grondement | la pente s'effondre, enfouit les traces **sans les détruire** (elles deviennent fossiles, trouvables en E2/E3) | remblayer, planter (les racines tiennent) | fouille archéologique, trésors |
| **Grand Gel** | Gel + Abri < 30 | givre qui monte, silence | tout s'arrête une manche : pousse 0, PNJ à l'abri, traces organiques **conservées intactes** | feux, huttes, Figure de la Chaleur | une époque « figée » qui arrive intacte 300 ans plus tard |
| **Chute de météore** | vote des spectateurs, ou 1 fois sur 8 à la graine | point lumineux dans le ciel pendant une manche | cratère de 7×7, devient lac en +1 saut ; tout ce qui était là devient « artefact céleste » (Ferveur +40) | aucune — mais on peut **déplacer** ce qu'on tient à sauver | la Figure la plus vénérée du jeu, en une seconde |
| **Tempête de la Compagnie** | pollution ≥ 70 (E2) | ciel orange, sirène de la Bouilloire | vent + pluie acide une manche ; les Automates s'arrêtent | valves, dépolluer | les Ateliers Libres (§1.3) |

### 5.2 Pourquoi ce n'est jamais punitif
Aucune catastrophe ne fait perdre la partie. Elle coûte du temps et déplace des choses. Le contrat prévoit
déjà la « solution alternative » (`20` §6). Et surtout : **une Figure de Mémoire protège ses traces**, ce qui
donne enfin une raison d'investir dans la Ferveur.

---

## 6. Les phénomènes — les moments qu'on filme

| Phénomène | Quand | Ce qui se passe |
|---|---|---|
| **La Résonance** | une fois par partie, à la 2e pause café | Pendant 20 secondes, les quatre époques se superposent : chacun voit les trois autres en calques translucides, **au même endroit**, et toute action se propage instantanément et visiblement. C'est le plan signature du jeu, et le meilleur clip possible |
| **La Brume Remontante** | météo Brume + Ferveur ≥ 50 | les fantômes deviennent nets et **audibles sans distance** : on s'entend comme dans la même pièce. Dure une manche |
| **La Nuit Sans Ombre** | Gel + ciel clair | éclairage bleu, les Figures brillent faiblement : on voit d'un coup d'œil tout ce que la vallée vénère |
| **L'Aurore des Traces** | après une catastrophe survécue | le ciel prend la couleur de l'époque dominante ; +10 Ferveur à toute trace ayant survécu |
| **Le Silence** | graine spéciale, 1 partie sur 50 | pendant 15 s, **aucun son**, les PNJ s'arrêtent et regardent le Mont Têtu. Rien d'autre. Personne n'explique. (Amorce de la Saison 1, `71` §2) |

---

## 7. L'arc narratif, renforcé

L'arc de `10_NARRATIVE_BIBLE.md` §7 reste, et gagne sa colonne vertébrale : **le Synchro fonctionne à la
Ferveur.**

| Ch. | Ce qui s'ajoute |
|---|---|
| 1 | Petit Moss suit les joueurs et nomme leur première trace. On rit de ses approximations. |
| 2 | Dame Orielle propose un marché : inscrire une trace au registre contre un objet brillant. Première Figure. |
| 3 | Les Chronomites s'attaquent **en priorité aux Figures** : le paradoxe menace ce à quoi on tient. Contremaître Bouilly supplie qu'on sauve la Bouilloire. |
| 4 | « Le Grand Nettoyage » prend son sens : Lendemain ne veut pas seulement une vallée propre, il veut **une vallée sans Figures**, parce qu'une histoire trop aimée est difficile à vendre. Vé-7 déserte à ce moment précis. |
| 5 | **Révélation :** Mamie Horloge explique que le Synchro n'a jamais été une invention comptable. Les quatre époques tiennent ensemble parce que quelqu'un, quelque part, **tient à quelque chose** ; la Ferveur est l'énergie du Bail. Lendemain le sait : le Vernissage doit siphonner la Ferveur de la vallée pour alimenter d'autres Bails ailleurs. |

**Le choix final (et il compte) :** au Vernissage, l'équipe décide, à l'unanimité ou à la majorité :
- **Livrer** — les Figures sont « archivées », le musée est parfait, 5 étoiles, Lendemain exulte, la vallée
  est magnifique et vide. Fin « Employé du mois ».
- **Garder** — on fait déborder le musée de Figures vivantes : le contrat échoue (1 étoile), le Synchro
  s'éteint faute de rendement… et les quatre époques, libérées, continuent sans l'agence. Fin « La vallée se
  garde toute seule », Mamie Horloge sourit pour la première fois, déblocage de la Saison 1.
- **Tricher** — ceux qui ont une Figure d'Ailleurs peuvent cacher une Figure dans la Grotte Qui Ronfle :
  livrer *et* garder. 4 étoiles, fin secrète, et un succès qui s'appelle « Comptabilité créative ».

Aucune fin n'est « la bonne ». Le thème du jeu est que ce qu'on laisse derrière soi compte — y compris quand
on choisit de le laisser à quelqu'un d'autre.

---

## 8. Branchements sur l'existant

| Système existant | Ce que ce document y ajoute |
|---|---|
| Recettes (`20` §4) | Ferveur portée par la trace ; nouvelles recettes **croisées** (`input.with`, voir `data/schemas/recipe.schema.json` v2) : Figure = trace + Porte-Voix + lieu |
| Paradoxe (`20` §5) | Les Chronomites visent d'abord les Figures ; rompre un Serment ajoute +10 à la jauge |
| Contrats (`12` §2) | Deux contrats de référence ajoutés (C13 « Faire pleuvoir », C14 « Un dieu discret ») |
| Musée (`GDD` §3.8) | Une **salle des Figures** ; la Chronique raconte le Peuple, ses bifurcations et ses catastrophes |
| Carnet (manque M3) | Le **Panthéon** : les Figures rencontrées, leur domaine, leur Bienfait, leur Serment. Collection, donc rétention |
| Progression (`20` §10) | Les rangs débloquent des **Serments d'agence** (modificateurs de lobby), pas seulement des chapeaux |
| Mode Streamer (`GDD` §3.9) | Le chat vote la météo et **nomme les Figures** (filtre déjà spécifié) |
| Accessibilité | §0.6 ci-dessus ; la frise des peuples est lisible en daltonisme (icône + texte, jamais la couleur seule) |

---

## 9. Paramètres (valeurs initiales, dans `data/tuning.json`)
`peoples.gauge_max` 100 · seuils de bifurcation : `water_min` 30, `food_min` 40, `faith_branch` 60,
`pollution_branch` 60, `food_collapse` 20, `shelter_collapse` 15 · `faith.figure_min` 30, `faith.major_min` 70,
gains +3/+5/+8/+10, pertes −5/−15 · `weather.change_per_round_max` 1, `weather.warning_seconds` 15 ·
`disasters.*_threshold` (crue 3 barrages, sécheresse forêt < 20 %, incendie, glissement 2 cellules,
gel abri < 30, météore 1/8, tempête pollution ≥ 70) · `phenomena.resonance_seconds` 20.

## 10. Critères d'acceptation
- [ ] Deux parties avec la même graine et les mêmes actions produisent **exactement** les mêmes peuples,
      Figures, météos et catastrophes (test déterminisme, `51_QA_TEST_PLAN.md`).
- [ ] Les neuf états de civilisation sont atteignables ; un test automatisé en atteint au moins six.
- [ ] Une catastrophe ne retire jamais plus de 20 % des traces d'une époque, et aucune trace protégée par une
      Figure de Mémoire.
- [ ] Mode « réduire les clignotements » : aucun flash > 3 Hz pendant orage, météore et Résonance.
- [ ] Un joueur sait dire, après une partie, **pourquoi** sa Figure est née (test de compréhension au playtest).
- [ ] Aucun nom, symbole ou rite ne renvoie à une religion réelle (revue humaine obligatoire avant publication).

## 11. Risques
| Risque | Parade |
|---|---|
| Surcharge : trop de systèmes à comprendre d'un coup | Tout est **passif** : on peut gagner sans jamais s'en occuper. La frise des peuples et le Panthéon expliquent après coup |
| La Ferveur devient la seule stratégie optimale | Les Serments coûtent ; les contrats ne récompensent la Ferveur que dans 2 cas sur 14 |
| Les catastrophes frustrent | Toujours annoncées, jamais létales, « solution alternative » du contrat ; mode Détente les réduit de moitié |
| Dérapage de ton sur les croyances | §0, revue humaine, vocabulaire inventé, satire dirigée vers les institutions |
| Coût de production | Les peuples réutilisent les PNJ existants (variantes de tenue) ; les catastrophes réutilisent l'eau, le feu et le terrain déjà spécifiés ; seuls les 4 Porte-Voix sont de nouveaux personnages |
