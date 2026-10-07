# Revue joueur — 7 octobre 2026

> **EN —** A player's review of the design dossier: what would make someone buy it, what would make them stop
> playing at hour 10, and the gaps found by reading the specification as if the game already existed.
> This is a **review**, not a design document: nothing here is normative. Accepted items move to
> [`docs/backlog.md`](../backlog.md), and only a human decides.
>
> **FR —** Revue du dossier comme si le jeu existait et qu'on venait d'y jouer. Ce document ne décide rien :
> les points retenus passent dans `docs/backlog.md`, et l'humain tranche.

Lu pour cette revue : GDD, `10` bible narrative, `12` scénarios, `20` paramètres, `21` monde, `32` UX,
`71` live ops, `data/schemas/recipe.schema.json`, `data/recipes/`.

---

## 1. Ce que je ressens en tant que joueur

**Les deux premières heures sont excellentes.** La promesse se comprend en une phrase, le « aha » arrive avant
la soixantième seconde, et la boucle est saine : j'agis, mon ami hurle trois cents ans plus tard. Le musée de
fin et la carte-récap transforment chaque partie en anecdote — c'est exactement ce qui fait circuler un jeu.
La voix de proximité entre époques est une idée que je n'ai vue nulle part ailleurs et qui, à elle seule,
vaut l'achat. Le mode Capsule asynchrone est le genre de mécanique dont on parle à ses collègues.

**L'heure dix m'inquiète.** À ce stade j'ai vu les douze contrats, la vallée est la même qu'au premier jour,
j'ai acheté tous les outils, et il ne me reste que des chapeaux à débloquer. Le jeu m'a promis de la
profondeur systémique ; ce que j'ai, c'est une collection de règles que je connais désormais par cœur. C'est
là que se joue la différence entre « marrant une soirée » et « quatre-vingts heures ».

**Ce que je ne comprends jamais bien :** pourquoi *ça* a donné *ça*. Je plante, je reviens, c'est devenu
autre chose, et je n'ai aucun endroit où aller vérifier la règle. Au bout de dix parties, je joue au hasard
en espérant une bonne surprise, au lieu de jouer en connaissance de cause.

---

## 2. Les manques, par ordre d'importance

### M1 — Les recettes croisées sont promises mais impossibles à écrire *(bloquant)*
Le GDD §3.3 dit : « Les recettes croisées (deux objets qui interagissent en vieillissant) sont la principale
source de surprises. » Le schéma `data/schemas/recipe.schema.json` n'a qu'un seul `input.type`, et les
conditions ne savent compter que des étiquettes à proximité (`count_tag_min`). Sur les 25 recettes écrites,
deux seulement regardent autre chose qu'elles-mêmes (`animals_pair`, `fire_near_hut`).

Conséquence : « graine + statue → bosquet sacré avec idole », « barrage + feu → forge », « cairn + tombe →
nécropole » ne sont pas exprimables. Or c'est précisément la combinatoire qui fait durer un bac à sable. Sans
elle, le contenu est additif (30 recettes = 30 surprises) au lieu d'être multiplicatif.

**Proposition :** ajouter au schéma un `input.with` (second type requis dans un rayon) et un
`outputs[].replaces` (les deux entrées fusionnent). Dix recettes croisées valent mieux que trente linéaires.

### M2 — Une seule vallée, pour toujours *(majeur)*
400 × 400 m, cinq repères fixes, quatre époques fixes. La graine fait varier la rivière et six à dix points
d'intérêt. Après vingt parties je connais chaque pli du terrain. Les concurrents cités dans l'étude de marché
ont tous une variété spatiale (lunes, montagnes, cartes). Les biomes arrivent en « saison 1 », donc après la
sortie, donc après les avis Steam.

**Proposition :** soit deux vallées au lancement, soit une génération de terrain réellement différente par
graine (relief, climat, densité des repères), les cinq repères gardant leur rôle sans garder leur position.

### M3 — Aucun carnet de recettes dans le jeu *(majeur)*
Rien, dans tout le dossier, ne décrit un endroit où le joueur consulte ce qu'il a découvert. Un jeu dont le
cœur est un ensemble de règles cachées a besoin d'un journal de découvertes : la règle apparaît une fois
observée, avec le nombre de fois où elle s'est déclenchée. C'est ce qui transforme « c'est aléatoire » en
« je sais ce que je fais », et c'est aussi un moteur de collection, donc de rétention.

**Proposition :** une « Chronique des Traces » dans l'Agence : 30 à 60 entrées, verrouillées, révélées à la
première observation, avec les conditions découvertes progressivement. Le sablier de poche sert d'indice, pas
de substitut.

### M4 — Le futur n'a presque aucune prise sur le passé *(majeur)*
Le passé transforme le futur en permanence ; le futur ne peut renvoyer qu'**un objet par manche** (cabine
temporelle). Le joueur de l'an 900 passe donc beaucoup de temps à subir et à nettoyer. Dans un coop, une
asymétrie d'agentivité se paie en frustration — et personne ne voudra être E3 à la deuxième partie.

**Proposition :** un canal rétrograde non matériel. Une « note du Lendemain » que l'aval épingle sur une
cellule et que l'amont voit en jeu ; un « devis » qui marque une zone comme à protéger ; un pouvoir de
l'aval qui ancre temporairement une trace. Peu coûteux, et cela rend l'aval actif.

### M5 — Rien n'est jamais perdu *(moyen)*
Pas de points de vie, pas de mort, les dangers étourdissent ou confisquent. Le ton est juste et je ne veux pas
d'horreur. Mais sans aucun enjeu, la tension retombe après la troisième partie. L'effondrement temporel est le
seul échec réel, et il est rare.

**Proposition :** un enjeu qui reste comique et réversible — un danger qui *efface une trace à laquelle on
tenait* plutôt qu'un objet quelconque, et le rend visible : le joueur doit avoir envie de protéger quelque
chose de précis.

### M6 — La vallée ne se souvient de rien entre deux parties *(moyen, mais c'est l'occasion manquée du projet)*
Le thème est « ce qu'on laisse derrière soi compte ». À la fin de la partie, tout est effacé. Un bac à sable
qui parle de traces et qui remet le monde à zéro à chaque session se contredit lui-même.

**Proposition :** une vallée d'équipe persistante, en parallèle du mode contrat : chaque partie y dépose
définitivement ses traces, et au bout de dix parties l'équipe a *sa* vallée, visitable, partageable, avec son
musée qui grossit. C'est la fonctionnalité qui différencierait le jeu de tout le reste du genre, et elle
coûte peu : le moteur est déjà un journal d'événements, c'est exactement ce qu'il faut pour cela.

### M7 — Progression sans conséquence sur le jeu *(moyen)*
Cinq rangs, vingt-quatre chapeaux, douze couleurs. Tous les outils coûtent au plus 300 Chronos, soit deux ou
trois parties. Après le rang « Chef d'équipe », plus rien ne change ma façon de jouer.

**Proposition :** des outils qui s'excluent (on en emporte trois sur sept), ou des variantes d'outil
débloquées par usage (la pelle large, la pelle profonde). La contrainte crée de la décision, donc de la
rejouabilité, sans contenu supplémentaire.

### M8 — Le solo tiendra-t-il un jeu à 20 € ? *(moyen)*
Le Solo Relais est honnêtement présenté comme un tutoriel et un mode « pause déjeuner ». Les avis Steam
jugeront autrement : un acheteur solo d'un jeu à 20 € s'attend à un contenu solo. Soit on l'assume très
clairement sur la page Steam, soit le Défi du jour devient une vraie colonne vertébrale solo (progression,
classement, objectifs hebdomadaires).

---

## 3. Une contradiction stratégique à assumer

L'étude de marché du GDD §1.2 identifie les facteurs communs aux succès cités : coop social, lisible en trois
secondes, **prix ≤ 10 €**, **graphismes modestes assumés**, petite équipe. Le projet retient le premier et le
deuxième, et contredit frontalement les deux suivants : photoréalisme Unreal 5.8 et 19,99 €.

Ce n'est pas forcément une erreur — Schedule I est cité à ~20 € — mais le dossier ne l'assume nulle part. Il
juxtapose une étude qui recommande A et une décision B, sans le paragraphe qui explique pourquoi B. Un
lecteur extérieur (investisseur, éditeur, journaliste) le verra immédiatement.

**Proposition :** un paragraphe explicite dans le GDD §0 ou l'ADR 0012 : ce que le réalisme achète (lisibilité
du vieillissement, crédibilité des quatre époques, captures vendeuses), ce qu'il coûte (budget ×5 à ×10,
délai, dépendance à des artistes), et pourquoi le prix de 19,99 € en découle.

---

## 4. Ce qui est déjà très bon, et qu'il ne faut pas casser

Le musée et la Chronique générée par modèles de phrases. La voix de proximité inter-époques. Le mode Capsule.
Le Saboteur. L'absence de points de vie et le parti pris « l'échec est drôle ». L'accessibilité (micro jamais
requis, daltonisme, sans clignotements, remappage). L'honnêteté du registre des risques. Les cas limites du
`12` §4 — déconnexion, hôte qui part, griefing, deux joueurs sur la même trace — sont traités avec un soin
qu'on voit rarement à ce stade.

---

## 5. Questions restées sans réponse dans le dossier

**Rejouabilité et contenu :** combien d'heures avant d'avoir vu les douze contrats ? Que fait un joueur au
bout de vingt heures ? Y a-t-il une raison de rejouer un contrat déjà réussi cinq étoiles ?

**Social :** comment je trouve des gens si je n'ai pas trois amis disponibles en même temps ? (Les lobbies
sont « amis seulement par défaut », les parties publiques en option, mais aucun appariement n'est décrit.)
Que voit un joueur qui rejoint en cours de partie ? Peut-on jouer à quatre si un seul possède le jeu
(la démo multi est mentionnée pour le Next Fest — est-ce permanent) ?

**Plateformes :** manette seulement ou aussi Steam Deck vérifié ? Crossplay ? Consoles ? Une sortie Mac ou
Linux via Proton est-elle testée ?

**Technique :** l'anti-triche est une ADR encore ouverte (0020) alors qu'il y a un classement quotidien.
Comment une capsule survit-elle à un changement de recettes entre deux versions, au-delà de
`CAPSULE_INVALID` ? Que devient la vallée d'une partie dont l'hôte a une connexion instable ?

**Confort :** la cinématique de pause café (siècles qui défilent) est-elle couverte par le mode « sans
clignotements » ? La caméra sur rails du musée peut-elle provoquer du mal des transports ? Le texte de la
Chronique s'affiche-t-il assez longtemps pour une lecture lente ?

**Modération :** les noms de statues votés par le chat Twitch sont du contenu créé par des tiers affiché à
tous les joueurs. Le filtre de mots suffit-il, et qui modère un signalement en direct ?

---

## 6. Incohérences mineures relevées

| Point | Où | Remarque |
|---|---|---|
| « Coop Contrat 2-4 » | GDD §3.1 vs §0 « 1-4 joueurs » | Le Solo Relais couvre le 1 joueur, mais la table du mode principal dit 2-4 : à harmoniser |
| Solo Relais : 4 manches × 240 s = 16 min | `20` §1 vs `12` §6 « 12-16 minutes » | Les 16 minutes de manches seules dépassent déjà la borne haute annoncée, musée non compris |
| Rotation sur 3 manches | `20` §1 | Avec +1 époque par manche, un joueur ne voit que 3 des 4 époques dans une partie : intentionnel ? à dire explicitement |
| Départage des recettes « ordre du fichier » | `20` §4.3 | Fragile dès que des contributeurs ajoutent des recettes ; une `priority` explicite dans le schéma serait déterministe et lisible |
| 30 recettes visées, 25 écrites | `data/recipes/` | Déjà noté au backlog ; les 5 manquantes devraient être des recettes croisées (voir M1) |
