# 11 — Scripts et dialogues
Propriétaire : Product Owner · v1.0 · Format : `CLÉ | FR | EN | contexte pour traducteurs`
Règles : chaque ligne ≤ 110 caractères (lisible sur Steam Deck). Les PNJ parlent en « charabia » synthétique sous-titré. Les `{PLACEHOLDERS}` sont remplis par le jeu ; les traducteurs doivent les conserver.

## 1. Tutoriel (Solo Relais, 3 minutes)
| Clé | FR | EN | Contexte |
|---|---|---|---|
| TUT_01 | Bienvenue chez Temporis Intérim ! Vous êtes notre nouvelle recrue… temporaire, évidemment. | Welcome to Temporis Temps! You're our newest hire… temporary, obviously. | Odile, écran d'agence |
| TUT_02 | Notre client veut de l'ombre en l'an 300. Vous, vous partez en l'an 0. Vous voyez où je veux en venir ? | Our client wants shade in year 300. You're going to year 0. See where this is going? | Odile |
| TUT_03 | Prenez la pelle. Creusez. Plantez. C'est la Loi de la Trace : tout ce que vous laissez vieillit. | Grab the shovel. Dig. Plant. That's the Law of Trace: whatever you leave behind ages. | Objectif : planter 1 graine |
| TUT_04 | Et maintenant, le Synchro. Accrochez-vous, on saute trois siècles. | And now, the Sync. Hold on, we're jumping three centuries. | Transition E0→E1 |
| TUT_05 | Regardez-moi cet arbre. Vous l'avez planté il y a cinq secondes. Ou trois cents ans. Les deux. | Look at that tree. You planted it five seconds ago. Or three hundred years. Both. | « Aha » obligatoire < 60 s |
| TUT_06 | Petite question : si vous empilez des pierres ici, à votre avis, ça devient quoi ? | Quick question: if you stack stones here, what do you think they become? | Objectif : cairn |
| TUT_07 | Un monument. Les gens d'ici le vénèrent déjà. Ils ne savent pas pourquoi. Ils ne sauront jamais. | A monument. The locals already worship it. They don't know why. They never will. | E2 |
| TUT_08 | Montez sur le socle et prenez la pose. N'importe laquelle. Je vous déconseille n'importe laquelle. | Step on the plinth and strike a pose. Any pose. I advise against any pose. | Objectif : statue |
| TUT_09 | Et voilà votre statue en l'an 900. Elle a l'air… très vous. | And there's your statue in year 900. It looks… very you. | E3 |
| TUT_10 | Attention : si le futur contredit le passé, ça fait des Non-conformités. Et les Non-conformités attirent les Chronomites. | Careful: if the future contradicts the past, you get Non-compliances. And those attract Chronomites. | Jauge affichée |
| TUT_11 | Le micro ? Facultatif. Les pings et les emotes font très bien le travail. Chez nous, on respecte le silence. | The mic? Optional. Pings and emotes do the job just fine. We respect silence here. | Accessibilité |
| TUT_12 | Formation terminée. Votre prime : 50 Chronos. Votre contrat : renouvelable. Peut-être. | Training complete. Your bonus: 50 Chronos. Your contract: renewable. Maybe. | Fin |

## 2. Hub de l'agence — Odile (aléatoire)
| Clé | FR | EN |
|---|---|---|
| HUB_01 | Le client est content. Enfin, il a dit « bof », mais chez lui c'est content. | The client is happy. Well, he said "meh", but for him that's happy. |
| HUB_02 | On a reçu une plainte de l'an 600. Un troupeau. Dans une usine. Je ne veux pas savoir. | We got a complaint from year 600. A herd. In a factory. I don't want to know. |
| HUB_03 | Petite question : vous avez signé la décharge pour les Chronomites ? Non ? Signez. | Quick question: did you sign the Chronomite waiver? No? Sign it. |
| HUB_04 | Mamie Horloge a encore refusé sa retraite. Neuf cents ans d'ancienneté, vous imaginez la prime. | Granny Clock refused retirement again. Nine hundred years of seniority, imagine the bonus. |
| HUB_05 | Le Bail interdit d'aller avant l'an 0. Quelqu'un a essayé. On ne parle plus de Jean-Michel. | The Lease forbids going before year 0. Someone tried. We no longer speak of Jean-Michel. |
| HUB_06 | Rappel : les statues obscènes sont déduites de la paie. Les statues ridicules, non. Nuance. | Reminder: obscene statues are docked from pay. Ridiculous ones aren't. Nuance. |

## 3. Brief de contrat (modèle)
| Clé | FR | EN |
|---|---|---|
| BRIEF_HEADER | Contrat n°{NUM} — Client : Monsieur Lendemain | Contract #{NUM} — Client: Mister Tomorrow |
| BRIEF_MAIN | Le client veut **{RESULTAT}** à **{LIEU}** en **{EPOQUE}**. | The client wants **{RESULT}** at **{PLACE}** in **{ERA}**. |
| BRIEF_BONUS | Bonus : {BONUS_1}. Bonus : {BONUS_2}. | Bonus: {BONUS_1}. Bonus: {BONUS_2}. |
| BRIEF_ABSURD | Exigence absolue du client : {ABSURDE}. Ne demandez pas pourquoi. | Client's non-negotiable: {ABSURD}. Don't ask why. |
| BRIEF_TIME | Vous avez {MANCHES} manches de {MINUTES} minutes. Le Synchro tourne. | You have {ROUNDS} rounds of {MINUTES} minutes. The Sync is running. |

## 4. Monsieur Lendemain — évaluation finale
| Étoiles | Clé | FR | EN |
|---|---|---|---|
| 5 | RATE_5_A | MAGNIFIQUE ! Lendemain est ému ! Lendemain va pleurer sur son hologramme ! | MAGNIFICENT! Tomorrow is moved! Tomorrow will cry on his hologram! |
| 5 | RATE_5_B | C'est exactement ce que Lendemain voulait sans savoir qu'il le voulait ! | This is exactly what Tomorrow wanted without knowing he wanted it! |
| 4 | RATE_4_A | Très bien ! Il manque un petit quelque chose. Un canard, peut-être. | Very good! Something small is missing. A duck, perhaps. |
| 3 | RATE_3_A | Lendemain est… satisfait. C'est le mot. Satisfait. Comme une soupe. | Tomorrow is… satisfied. That's the word. Satisfied. Like soup. |
| 2 | RATE_2_A | Lendemain avait demandé {RESULTAT}. Lendemain a reçu… ça. Lendemain réfléchit. | Tomorrow asked for {RESULT}. Tomorrow received… this. Tomorrow is thinking. |
| 1 | RATE_1_A | Lendemain n'est pas fâché. Lendemain est déçu. C'est pire, dit Lendemain. | Tomorrow isn't angry. Tomorrow is disappointed. That's worse, says Tomorrow. |
| 1 | RATE_1_B | Effondrement temporel. Lendemain retient sa commission. Lendemain retient aussi sa respiration. | Temporal collapse. Tomorrow is withholding his fee. Tomorrow is also holding his breath. |

## 5. Pause café et paradoxes
| Clé | FR | EN |
|---|---|---|
| CAFE_START | Pause café ! Le Synchro accélère : trois siècles en trente secondes. | Coffee break! The Sync is speeding up: three centuries in thirty seconds. |
| CAFE_ROTATE | Rotation ! Chacun avance d'une époque. Bonne chance avec ce que vos collègues vous ont laissé. | Rotation! Everyone moves up one era. Good luck with what your colleagues left you. |
| PARADOX_25 | Non-conformité détectée. Le Bail grince. | Non-compliance detected. The Lease is creaking. |
| PARADOX_50 | Chronomites en approche. Elles ont faim. Elles ont toujours faim. | Chronomites incoming. They're hungry. They're always hungry. |
| PARADOX_75 | Le Bail se fissure ! Réduisez les non-conformités ou l'agence rapatrie tout le monde ! | The Lease is cracking! Reduce non-compliances or the agency pulls everyone out! |
| PARADOX_100 | EFFONDREMENT. Rapatriement en cours. Prime partielle. Ne touchez à rien. | COLLAPSE. Extraction in progress. Partial bonus. Touch nothing. |
| ANACHRO_01 | Un objet de {EPOQUE_SRC} vient d'arriver en {EPOQUE_DST}. Les habitants l'adorent déjà. | An object from {ERA_SRC} just arrived in {ERA_DST}. The locals already adore it. |

## 6. ARCHIVE — modèles de Chronique (musée)
Slots : `{JOUEUR}` (pseudo de session, jamais persisté), `{OBJET}`, `{LIEU}`, `{EPOQUE}`, `{NOMBRE}`, `{POSE}`. Chaque modèle a un **type d'événement** déclencheur.
| Clé | Déclencheur | FR | EN |
|---|---|---|---|
| CHR_TREE_01 | arbre millénaire | Ici s'élève l'Arbre de {LIEU}, planté en {EPOQUE} par {JOUEUR}, comme chacun sait, pour faire de l'ombre à personne. | Here stands the Tree of {PLACE}, planted in {ERA} by {PLAYER}, as everyone knows, to shade no one at all. |
| CHR_STATUE_01 | statue | La Statue du {POSE}. Datée de {EPOQUE}. Les historiens s'accordent : {JOUEUR} faisait ça tout le temps. | The Statue of the {POSE}. Dated {ERA}. Historians agree: {PLAYER} did this all the time. |
| CHR_STATUE_02 | statue érodée | Cette silhouette usée est, selon la légende, « quelqu'un qui saluait ». Nous ne saurons jamais qui. Nous le savons : c'est {JOUEUR}. | This worn figure is, legend says, "someone waving". We'll never know who. We know: it's {PLAYER}. |
| CHR_HOLE_01 | tranchée/canyon | Le Grand Trou de {EPOQUE}, creusé par {JOUEUR} pour une raison que la science ignore. Il est aujourd'hui un canyon. | The Great Hole of {ERA}, dug by {PLAYER} for reasons science cannot explain. It is now a canyon. |
| CHR_HERD_01 | troupeau | Le troupeau de {LIEU} descend d'une bête unique nourrie de {NOMBRE} pommes par {JOUEUR}. On l'appelle encore Bouloche. | The herd of {PLACE} descends from a single beast fed {NOMBRE} apples by {PLAYER}. It is still called Bouloche. |
| CHR_CULT_01 | fan-club d'objet | Le Fan-club de {OBJET} compte {NOMBRE} membres. Son fondateur involontaire, {JOUEUR}, a simplement oublié {OBJET} ici. | The {OBJECT} Fan Club has {NOMBRE} members. Its accidental founder, {PLAYER}, simply forgot {OBJECT} here. |
| CHR_TREASURE_01 | trésor | Le Trésor du Baron ne fut jamais au Baron. Il fut confisqué à {JOUEUR} par Sire Fiscalin, article 12 du Bail. | The Baron's Treasure was never the Baron's. It was confiscated from {PLAYER} by Sir Taxalot, Lease article 12. |
| CHR_PATH_01 | route | Cette avenue suit exactement les allers-retours de {JOUEUR} entre {LIEU} et la rivière. {NOMBRE} fois. | This avenue follows exactly {PLAYER}'s trips between {PLACE} and the river. {NOMBRE} times. |
| CHR_FIRE_01 | champ | Le Champ Fertile de {LIEU} doit tout à un feu « parfaitement maîtrisé » par {JOUEUR}. | The Fertile Field of {PLACE} owes everything to a fire "perfectly controlled" by {PLAYER}. |
| CHR_ANACHRO_01 | anachronisme | Cet objet de {EPOQUE} n'a rien à faire ici. Les habitants l'ont donc élu maire. | This {ERA} object has no business being here. So the locals elected it mayor. |
| CHR_PARADOX_01 | paradoxe | Ici, le temps a brièvement renoncé. Nous remercions {JOUEUR} pour cette expérience. | Here, time briefly gave up. We thank {PLAYER} for the experience. |
| CHR_COLLAPSE_01 | effondrement | Cette aile est fermée pour cause d'Effondrement. Merci de votre compréhension. Merci {JOUEUR}. | This wing is closed due to Collapse. Thank you for understanding. Thank you, {PLAYER}. |
| CHR_NOTHING_01 | manche sans trace | Salle vide. En {EPOQUE}, {JOUEUR} n'a rien laissé. Les historiens appellent cela « une sieste ». | Empty room. In {ERA}, {PLAYER} left nothing. Historians call this "a nap". |
| CHR_LAKE_01 | lac/station | Le Lac de {LIEU} naquit d'un barrage de branches. La station balnéaire naquit du lac. {JOUEUR} naquit avant. | The Lake of {PLACE} was born from a stick dam. The resort was born from the lake. {PLAYER} was born earlier. |
| CHR_MASCOT_01 | mascotte | La mascotte de la ville, « Petit Bouloche », pèse quatre tonnes et adore les intérimaires. | The town mascot, "Little Bouloche", weighs four tons and loves temps. |
| CHR_FINAL_5 | note 5 | Visite terminée. Monsieur Lendemain a pleuré. ARCHIVE a enregistré ses larmes pour le musée. | Tour over. Mister Tomorrow cried. ARCHIVE recorded his tears for the museum. |
| CHR_FINAL_1 | note 1 | Visite terminée. Nous vous prions d'oublier ce que vous avez vu. Nous, nous avons déjà oublié. | Tour over. Please forget what you have seen. We already have. |

(ARCHIVE dispose de 25 modèles à l'Early Access ; 60 visés. Chaque modèle existe en 2 variantes pour éviter la répétition.)

## 7. Barks des dangers (charabia + sous-titre court)
| Clé | Personnage | FR | EN |
|---|---|---|---|
| BRK_BOULOCHE_EAT | Bouloche | *miam* (Bouloche a mangé votre pousse.) | *nom* (Bouloche ate your sprout.) |
| BRK_BOULOCHE_LOVE | Bouloche | *brr* (Bouloche vous suit maintenant. Pour toujours.) | *brr* (Bouloche follows you now. Forever.) |
| BRK_FISCALIN_TAX | Sire Fiscalin | Taxe de Dépôt, article 12 ! Objet confisqué ! | Deposit Tax, article 12! Object confiscated! |
| BRK_FISCALIN_BRIBE | Sire Fiscalin | Oh. Ça brille. Je n'ai rien vu. | Oh. Shiny. I saw nothing. |
| BRK_AUTOMATE | Automate | *bip* Traitement en cours. Ne pas insérer de collègue. | *beep* Processing. Do not insert colleagues. |
| BRK_SMOG | Bouilloire | La Grande Bouilloire siffle. Visibilité réduite. Trouvez une valve ! | The Great Kettle whistles. Low visibility. Find a valve! |
| BRK_BRIGADE_SCAN | Brigade | Nettoyage ! Anachronisme détecté ! Recyclage dans 5… 4… | Cleanup! Anachronism detected! Recycling in 5… 4… |
| BRK_BRIGADE_FAKE | Brigade | Certificat d'authenticité accepté. Bonne journée ! | Authenticity certificate accepted. Have a nice day! |
| BRK_CHRONOMITE | Chronomites | *grignote* (Une Chronomite dévore la non-conformité.) | *nibble* (A Chronomite is eating the non-compliance.) |

## 8. Mamie Horloge — indices (déclenchés par contexte)
| Clé | Contexte | FR | EN |
|---|---|---|---|
| MH_01 | près de l'eau | Ce qui pousse près de l'eau pousse deux fois. Ce qui pousse dans les marais, trois. | What grows by water grows twice. What grows in the marsh, thrice. |
| MH_02 | grotte | Dans la grotte, rien ne vieillit. Tout s'y souvient. | In the cave, nothing ages. Everything remembers. |
| MH_03 | paradoxe | Le futur n'aime pas qu'on le contredise. Il boude, puis il mord. | The future hates being contradicted. It sulks, then it bites. |
| MH_04 | Fiscalin | Fiscalin aime ce qui brille. Donnez-lui une cuillère, gardez votre trésor. | Taxalot loves shiny things. Give him a spoon, keep your treasure. |
| MH_05 | chapitre 4 | On m'a demandé de nettoyer, moi aussi, un jour. J'ai planté un arbre à la place. | They asked me to clean up too, once. I planted a tree instead. |
| MH_06 | chapitre 5 | Vous voulez savoir qui a planté le premier arbre ? Regardez ma pelle. | Want to know who planted the first tree? Look at my shovel. |

## 9. Cinématiques de chapitre (panneaux, 20 s max)
**Ch.1** — Panneau 1 : l'agence. « Temporis Intérim : votre passé, notre avenir, leur présent. » Panneau 2 : la cabine. Panneau 3 : la vallée au lever du soleil.
**Ch.2** — « Monsieur Lendemain a visité le Musée de Tout. Il était vide. Monsieur Lendemain n'aime pas le vide. »
**Ch.3** — « Quelque chose grignote le Bail. » (première Chronomite en gros plan, mignonne et inquiétante)
**Ch.4** — « Le client trouve votre histoire… désordonnée. » Mamie Horloge, de dos, regarde l'arbre du Mont.
**Ch.5** — « Le Synchro sera éteint à l'ouverture. La vallée sera remise à zéro. Sauf si… » Puis fin : la foule dans la vallée-musée, ARCHIVE perdu, Lendemain qui pleure, Odile qui tend un contrat. Dernier panneau : la pelle de Mamie Horloge plantée près d'une jeune pousse.

## 10. Conseils de chargement (15)
LOAD_01 Les statues se souviennent de la pose, pas de l'intention. · LOAD_02 Deux animaux laissés ensemble ne restent jamais deux. · LOAD_03 Un objet du futur dans le passé devient célèbre, puis dangereux. · LOAD_04 Les chemins se creusent là où l'on marche. · LOAD_05 Le smog se calme avec les valves, pas avec les cris. · LOAD_06 Sire Fiscalin ne voit pas ce qui est enterré. · LOAD_07 Le sablier montre le futur, il ne le promet pas. · LOAD_08 L'ancre temporelle protège un objet, pas vos erreurs. · LOAD_09 Bouloche aime les pommes. Bouloche aime tout, en fait. · LOAD_10 Une graine dans la grotte reste une graine. · LOAD_11 Le micro est facultatif. Le ping est éternel. · LOAD_12 Un contrat refusé avec style vaut parfois plus qu'un contrat réussi. · LOAD_13 Les Chronomites mangent les paradoxes, puis le reste. · LOAD_14 Le feu fertilise. Le feu brûle aussi. Dans cet ordre, ou l'inverse. · LOAD_15 Mamie Horloge connaît votre prénom. Ne demandez pas comment.

## 11. Messages système et réseau
| Clé | FR | EN |
|---|---|---|
| NET_HOST_LEFT | L'hôte a quitté la mission. Prime partielle versée. Une capsule de reprise a été générée. | The host left the mission. Partial bonus paid. A resume capsule was generated. |
| NET_RECONNECT | Reconnexion au Synchro… | Reconnecting to the Sync… |
| NET_LOBBY_FULL | Cette équipe est complète (4 intérimaires). | This team is full (4 temps). |
| NET_VERSION | Version différente de celle de l'hôte. Mettez le jeu à jour. | Different version from the host. Please update the game. |
| NET_KICKED | Vous avez été rapatrié par vote de l'équipe. | You were extracted by team vote. |
| CAPSULE_INVALID | Code capsule invalide ou d'une version incompatible. | Invalid or incompatible capsule code. |
| PRIVACY_TITLE | Vos données, votre choix | Your data, your choice |
| PRIVACY_BODY | Le jeu ne collecte rien sans votre accord. La voix n'est jamais enregistrée. Vous pouvez tout changer dans Options › Confidentialité. | The game collects nothing without your consent. Voice is never recorded. Change anything in Options › Privacy. |
| STREAM_VOTE_OPEN | Spectateurs du Temps : votez ! !meteore !pluie !mammouth | Time Spectators: vote! !meteor !rain !mammoth |
| STREAM_VOTE_RESULT | Les spectateurs ont choisi : {EVENEMENT}. Désolé. | The spectators chose: {EVENT}. Sorry. |

## 12. Notes de localisation
- Langue source : FR. Langues EA : EN, ES, PT-BR, DE, RU, ZH-Hans, JA. Prévoir +30 % d'expansion de texte.
- Les noms propres (Bouloche, Fiscalin, Lendemain, ARCHIVE, Mamie Horloge) sont adaptables par langue (EN : Bouloche, Sir Taxalot, Mister Tomorrow, ARCHIVE, Granny Clock).
- Le charabia vocal est généré par syllabes neutres : aucune langue réelle, donc aucun doublage.
