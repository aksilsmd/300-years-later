# 20 — Spécification technique complémentaire : exigences non fonctionnelles

> **EN —** The non-functional requirements only. The normative architecture stays in 40_TECHNICAL_DESIGN.md and is not repeated here.

Propriétaire : Product Owner · v1.0 · 7 octobre 2026

> **[`40_TECHNICAL_DESIGN.md`](../design/40_TECHNICAL_DESIGN.md) reste le document normatif de
> l'architecture.** Ce fichier **ne le répète pas** : il n'y a ici ni arborescence de modules, ni modèle de
> données, ni protocole, ni choix de topologie. Il porte uniquement les exigences **non fonctionnelles** —
> performance, déterminisme, réseau, sécurité, confidentialité, accessibilité, localisation, compatibilité,
> observabilité, maintenabilité, portabilité, conformité des plateformes, licences, éthique, durabilité — et
> les rend numérotées, mesurables et vérifiables. Toute dérogation à `40` relève d'un ADR, pas de ce fichier.

**Conventions.** Même forme et mêmes priorités MoSCoW que
[`10_SPEC_FONCTIONNELLE.md`](10_SPEC_FONCTIONNELLE.md). Les sources `NN_*.md §n` désignent
`docs/design/NN_*.md` ; `GDD §n` désigne `docs/design/GDD_CENTURY_TEMPS.md`. Une mention
***À trancher :*** renvoie à [`docs/backlog.md`](../backlog.md).

Domaines : [PERF](#1-perf--performance) · [DET](#2-det--déterminisme-et-reproductibilité) ·
[RES](#3-res--réseau-et-tolérance-aux-pannes) · [SEC](#4-sec--sécurité-applicative) ·
[RGPD](#5-rgpd--confidentialité-et-protection-des-données) · [ACC](#6-acc--accessibilité) ·
[LOC](#7-loc--localisation-et-internationalisation) · [COMPAT](#8-compat--compatibilité) ·
[OBS](#9-obs--observabilité) · [MAINT](#10-maint--maintenabilité) · [PORT](#11-port--portabilité) ·
[PLAT](#12-plat--conformité-des-plateformes) · [LIC](#13-lic--licences-et-traçabilité-des-assets) ·
[ETH](#14-eth--éthique) · [DUR](#15-dur--durabilité)

---

## 1. PERF — performance

**ENF-PERF-01** — Profil **recommandé** (RTX 3070 / RX 6800, 8 cœurs, 16 Go) : 1440p à 60 i/s avec Lumen High, soit un budget GPU de 16,6 ms par image. *Source :* `40_TECHNICAL_DESIGN.md §10`, `30_ART_BIBLE.md §4`. *Critère d'acceptation :* trace Unreal Insights sur une scène de référence : 95 % des images sous 16,6 ms. *Priorité :* MUST.

**ENF-PERF-02** — Profil **minimum** (GTX 1660 Super / RX 5600 XT, 6 cœurs, 16 Go) : 1080p à 30-60 i/s, Lumen Medium, mise à l'échelle temporelle activée, budget GPU ≤ 33 ms. *Source :* `40_TECHNICAL_DESIGN.md §10`, `30_ART_BIBLE.md §4`. *Critère d'acceptation :* trace Insights sur la configuration C de `51 §4` : aucune image au-delà de 33 ms en jeu normal. *Priorité :* MUST.

**ENF-PERF-03** — Profil **Steam Deck** : 800p à 30 i/s, Lumen Medium ou éclairage global réduit, l'objectif étant « jouable ». *Source :* `40_TECHNICAL_DESIGN.md §10`. *Critère d'acceptation :* session de 30 min sur Deck : i/s médian ≥ 30 à 800p. *Priorité :* MUST. *Contradiction relevée :* `50 §2` (porte G6) et `51 §6` exigent « 60 fps Deck » ; `40 §10`, normatif, fixe 30 i/s. À arbitrer (`docs/backlog.md`).

**ENF-PERF-04** — Le tick logique de l'hôte tourne à 20 Hz en moins de 4 ms, et la propagation reste sous 2 ms au 95ᵉ centile. *Source :* `40_TECHNICAL_DESIGN.md §10`, `51_QA_TEST_PLAN.md §6`, `data/tuning.json` (`net.tick_hz`). *Critère d'acceptation :* 1 000 actions aléatoires propagées : p95 < 2 ms ; tick mesuré < 4 ms. *Priorité :* MUST.

**ENF-PERF-05** — La scène de stress (2 000 traces par époque, 4 joueurs, smog, 6 Chronomites) reste jouable, la mémoire reste stable sur 2 h (fuite < 50 Mo), et le chargement d'une partie prend moins de 8 s. *Source :* `51_QA_TEST_PLAN.md §6`. *Critère d'acceptation :* les trois mesures sont relevées et consignées au rapport de campagne. *Priorité :* MUST.

**ENF-PERF-06** — Budgets de contenu : mémoire de texture 3 Go (recommandé) / 1,5 Go (minimum) ; 4 joueurs et au plus 12 PNJ humains à l'écran ; taille installée de 15 à 30 Go ; audio ≤ 120 Mo au total. *Source :* `30_ART_BIBLE.md §4`, `31_AUDIO_DESIGN.md §6`. *Critère d'acceptation :* rapport mémoire par build : aucun budget dépassé. *Priorité :* SHOULD.

---

## 2. DET — déterminisme et reproductibilité

**ENF-DET-01** — Le cœur temporel calcule **en entiers**, avec un générateur PCG32 indexé par `(graine, usage, identifiant, saut)` et des conteneurs triés. *Source :* `40_TECHNICAL_DESIGN.md §4`, `ARCHITECTURE.md` (invariant `TemporalCore`). *Critère d'acceptation :* revue de code et test automatisé : aucun type flottant dans le chemin de calcul du cœur. *Priorité :* MUST.

**ENF-DET-02** — Le cœur temporel **ne lit jamais** la physique, l'heure système, ni un générateur pseudo-aléatoire global. *Source :* `40_TECHNICAL_DESIGN.md §4`, `AGENTS.md §5.2`. *Critère d'acceptation :* test statique : aucune occurrence de `FMath::Rand`, d'horloge système ni d'appel physique dans le module du cœur. *Priorité :* MUST.

**ENF-DET-03** — La physique est répliquée par l'hôte ; en fin de manche, l'hôte émet une action de gel par objet dynamique, avec position quantifiée, et **seules ces positions** alimentent les recettes. *Source :* `40_TECHNICAL_DESIGN.md §4`. *Critère d'acceptation :* deux parties de même journal produisent les mêmes positions gelées. *Priorité :* MUST.

**ENF-DET-04** — Un test « golden » associe une graine de référence et un journal de référence à un hachage attendu des quatre époques. *Source :* `40_TECHNICAL_DESIGN.md §4`, `51_QA_TEST_PLAN.md §1`. *Critère d'acceptation :* le test golden tourne à chaque PR et échoue à la moindre divergence de hachage. *Priorité :* MUST.

**ENF-DET-05** — Le déterminisme couvre aussi les **systèmes émergents** : peuples, Figures, météos, catastrophes et phénomènes entrent dans le hachage de monde. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §10`, `51_QA_TEST_PLAN.md` (tableau `13`). *Critère d'acceptation :* même graine et même journal sur deux machines : peuples, Figures, météos, catastrophes et phénomènes **identiques**. *Priorité :* MUST.

**ENF-DET-06** — La génération procédurale du monde est déterministe, et la validation de connexité des zones se fait par re-tirage journalisé en `graine + 1` si nécessaire. *Source :* `21_WORLD_LEVEL_DESIGN.md §4`, `40_TECHNICAL_DESIGN.md §5`. *Critère d'acceptation :* une graine donnée produit toujours la même vallée ; tout re-tirage est inscrit au journal. *Priorité :* MUST.

---

## 3. RES — réseau et tolérance aux pannes

**ENF-RES-01** — La bande passante moyenne reste sous 30 ko/s par joueur. *Source :* `40_TECHNICAL_DESIGN.md §10`, `51_QA_TEST_PLAN.md §5`. *Critère d'acceptation :* mesure sur une partie à 4 joueurs de 20 min : moyenne < 30 ko/s. *Priorité :* MUST.

**ENF-RES-02** — Un contrôle d'intégrité compare le hachage des quatre époques toutes les 5 s, et une resynchronisation complète est déclenchée en cas d'écart. *Source :* `40_TECHNICAL_DESIGN.md §6`, `data/tuning.json` (`net.hash_check_seconds`). *Critère d'acceptation :* une divergence injectée est détectée en moins de 5 s et corrigée sans fermer la session. *Priorité :* MUST.

**ENF-RES-03** — Le jeu tient les conditions de réseau dégradées : latence 0 / 100 / 250 ms, perte 0 / 2 / 5 %, gigue 30 ms, **sans désynchronisation**, et les actions sont confirmées en moins de 400 ms à 250 ms de latence. *Source :* `51_QA_TEST_PLAN.md §5`. *Critère d'acceptation :* la matrice complète est exécutée et consignée ; aucun cas de désynchronisation. *Priorité :* MUST.

**ENF-RES-04** — La déconnexion d'un client, le départ de l'hôte et quatre joueurs agissant sur la même cellule au même tick sont gérés sans plantage ni perte de progression acquise. *Source :* `51_QA_TEST_PLAN.md §5`, `12_SCENARIOS.md §4`. *Critère d'acceptation :* les trois scénarios sont rejoués et aucun ne produit de plantage ni de perte. *Priorité :* MUST.

**ENF-RES-05** — Il n'y a **pas de migration d'hôte** : le départ de l'hôte produit une capsule de reprise, qui est le mécanisme de continuité assumé. *Source :* `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* aucun code de migration n'existe ; la capsule de reprise permet de reprendre la vallée. *Priorité :* MUST.

**ENF-RES-06** — Aucune adresse IP de joueur n'est exposée à un autre joueur : le transport passe par le relais de la plateforme. *Source :* `40_TECHNICAL_DESIGN.md §6`, `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* capture réseau côté client : aucune adresse IP d'un autre joueur visible. *Priorité :* MUST.

---

## 4. SEC — sécurité applicative

**ENF-SEC-01** — L'hôte est autoritaire : chaque requête client est validée sur la portée (≤ 2,5 m), les cooldowns, l'inventaire, l'époque du joueur, une taille ≤ 128 octets et un débit ≤ 10 actions par seconde. *Source :* `40_TECHNICAL_DESIGN.md §6`, `data/tuning.json` (`net`). *Critère d'acceptation :* chaque critère est testé par une requête non conforme, qui est rejetée. *Priorité :* MUST.

**ENF-SEC-02** — Un client dépassant 20 rejets par minute est exclu de la session. *Source :* `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* le seuil est atteint artificiellement et l'exclusion est effective. *Priorité :* MUST.

**ENF-SEC-03** — Le jeu résiste au fuzzing réseau : 10 000 appels distants aléatoires ou malformés ne provoquent **aucun plantage**, les rejets sont comptés et le seuil d'exclusion s'applique. *Source :* `51_QA_TEST_PLAN.md §5`. *Critère d'acceptation :* la campagne de fuzzing est exécutée et son rapport ne comporte aucun plantage. *Priorité :* MUST.

**ENF-SEC-04** — Aucun texte libre n'est accepté sans filtre, et le seul champ de texte libre est le nom de statue (≤ 16 caractères). *Source :* `40_TECHNICAL_DESIGN.md §6`, `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* audit des entrées : aucun autre champ libre n'atteint le réseau ni l'affichage. *Priorité :* MUST.

**ENF-SEC-05** — Aucun secret, jeton, clé ni identifiant ne figure dans le dépôt : la détection de secrets et l'analyse statique sont exécutées en intégration continue. *Source :* `40_TECHNICAL_DESIGN.md §11`, `AGENTS.md §6`. *Critère d'acceptation :* `python3 tools/privacy_scan.py` et les outils de détection de secrets passent sans alerte. *Priorité :* MUST.

**ENF-SEC-06** — Une politique de divulgation responsable est publiée et un point de contact de sécurité existe. *Source :* `legal/README.md` (document 16), `60_LEGAL_COMPLIANCE.md §1`. *Critère d'acceptation :* le document existe, est daté, et nomme un contact dédié au projet (jamais une adresse personnelle). *Priorité :* MUST.

**ENF-SEC-07** — ***À trancher :*** l'anti-triche reste une décision ouverte (ADR 0020) alors qu'un classement quotidien existe. Le dossier retient que la validation serveur suffit pour un coop sans enjeu compétitif, et que la solution gratuite de l'éditeur du moteur est « envisagée » si des lobbies publics et des classements existent. *Source :* `40_TECHNICAL_DESIGN.md §6`, `§14` (ADR 0020), `docs/reviews/2026-10-07-revue-joueur.md §5`. *Critère d'acceptation :* à définir avec l'ADR 0020. *Priorité :* SHOULD.

---

## 5. RGPD — confidentialité et protection des données

**ENF-RGPD-01** — **Minimisation** : le jeu ne traite que les données du tableau de `60 §2` et rien d'autre ; aucune donnée n'est collectée au-delà du strict nécessaire au jeu en ligne sans consentement. *Source :* `60_LEGAL_COMPLIANCE.md §2`, `GDD §6.1`. *Critère d'acceptation :* un audit des traitements effectifs correspond exactement au registre, sans traitement non inscrit. *Priorité :* MUST.

**ENF-RGPD-02** — La **voix n'est jamais enregistrée**, sous aucune forme, y compris temporaire. *Source :* `GDD §6.1`, `40_TECHNICAL_DESIGN.md §7`. *Critère d'acceptation :* test statique (aucune écriture de fichier dans le module de voix) **et** test d'exécution (aucun fichier audio dans le dossier de sauvegarde après 10 min de voix active). *Priorité :* MUST.

**ENF-RGPD-03** — Télémétrie et rapports de plantage reposent sur le **consentement**, sont anonymes, hébergés dans l'Union européenne, avec adresse IP tronquée, conservation de 13 mois au maximum pour la télémétrie et 90 jours pour les rapports de plantage, et sont révocables. *Source :* `GDD §6.1`, `60_LEGAL_COMPLIANCE.md §2`. *Critère d'acceptation :* les durées et l'hébergement sont consignés au registre des traitements et vérifiables chez l'hébergeur. *Priorité :* MUST.

**ENF-RGPD-04** — Les événements de télémétrie sont exactement ceux de `20 §13` et ne contiennent **aucun identifiant de joueur, aucune position fine, aucun texte libre**. *Source :* `20_GAME_DESIGN_PARAMETERS.md §13`. *Critère d'acceptation :* inspection d'une charge utile émise : aucun des trois éléments interdits n'est présent. *Priorité :* MUST.

**ENF-RGPD-05** — Sans consentement, le sous-système de télémétrie est **inopérant** (et non seulement silencieux). *Source :* `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* test automatisé : aucun appel sortant n'est émis et aucune file d'attente ne s'accumule. *Priorité :* MUST.

**ENF-RGPD-06** — Le droit à l'effacement est exerçable depuis le jeu (suppression des données locales) et les droits d'accès, de rectification, d'opposition, de limitation et de retrait du consentement sont documentés avec un contact et le recours à l'autorité de contrôle. *Source :* `60_LEGAL_COMPLIANCE.md §3`, `GDD §6.1`. *Critère d'acceptation :* la politique publiée énonce les six droits et le contact ; le bouton de suppression fonctionne. *Priorité :* MUST.

**ENF-RGPD-07** — **Aucun cookie, aucun traceur, aucun analytics publicitaire, aucun CDN externe et aucune police tierce hébergée** — ni dans le jeu, ni sur la page d'atterrissage. *Source :* `GDD §6.1`, `AGENTS.md §4.3`, `ARCHITECTURE.md` (invariant de la landing). *Critère d'acceptation :* `python3 tools/privacy_scan.py` ne relève aucune ressource externe ni aucun traceur. *Priorité :* MUST.

**ENF-RGPD-08** — Les données du mode streamer (commandes de chat) sont traitées **en mémoire uniquement** et aucun pseudonyme n'est persisté. *Source :* `GDD §6.1`, `40_TECHNICAL_DESIGN.md §9`. *Critère d'acceptation :* après une session, aucun fichier ne contient de pseudonyme de spectateur. *Priorité :* MUST.

**ENF-RGPD-09** — Les playtests font l'objet d'un consentement écrit (finalité, enregistrement optionnel de l'écran et de la voix, conservation de 3 mois, droit de retrait) et aucun mineur n'y participe sans autorisation parentale écrite. *Source :* `51_QA_TEST_PLAN.md §7`, `60_LEGAL_COMPLIANCE.md §2`. *Critère d'acceptation :* chaque playtest dispose de ses formulaires signés, archivés et supprimés à l'échéance. *Priorité :* MUST.

**ENF-RGPD-10** — Un registre des traitements est tenu à jour, et une analyse d'impact est produite avant la mise en service de la voix en ligne. *Source :* `60_LEGAL_COMPLIANCE.md §1`, `legal/README.md` (documents 06 et 07). *Critère d'acceptation :* les deux documents existent, sont datés, et l'analyse d'impact précède la phase P6. *Priorité :* MUST.

**ENF-RGPD-11** — La protection des mineurs est effective par défaut : lobbies amis seulement, aucune publicité ciblée, aucune interaction monétaire, mute, blocage et signalement accessibles, noms de statues filtrés. *Source :* `GDD §6.2`, `60_LEGAL_COMPLIANCE.md §6`, `legal/README.md §2`. *Critère d'acceptation :* les six mesures sont vérifiables sur un profil vierge. *Priorité :* MUST.

---

## 6. ACC — accessibilité

**ENF-ACC-01** — Le jeu suit les *Game Accessibility Guidelines* comme référentiel de conception et de test. *Source :* `GDD §6.3`, `51_QA_TEST_PLAN.md` (en-tête). *Critère d'acceptation :* une grille de conformité au référentiel est remplie et versionnée avant la porte G5. *Priorité :* MUST.

**ENF-ACC-02** — Les six catégories d'options de `32 §6` sont présentes **et fonctionnelles** ; une option présente mais inopérante est une anomalie bloquante. *Source :* `32_UX_UI_SPEC.md §6`, `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* checklist d'accessibilité verte à G5, chaque option ayant un effet observable. *Priorité :* MUST.

**ENF-ACC-03** — Le jeu est **terminable sans micro, sans son et en mode daltonien**. *Source :* `51_QA_TEST_PLAN.md §9`, `GDD §6.3`. *Critère d'acceptation :* trois parcours complets sont exécutés et consignés, un par condition. *Priorité :* MUST.

**ENF-ACC-04** — L'information n'est jamais portée par la couleur seule : chaque distinction d'époque, de météo, de catastrophe et de Peuple est redondée par une forme, une icône ou un texte. *Source :* `GDD §6.3`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `21_WORLD_LEVEL_DESIGN.md §10`. *Critère d'acceptation :* revue en simulation de daltonisme : toutes les distinctions restent lisibles. *Priorité :* MUST.

**ENF-ACC-05** — Aucun contenu n'émet de flash au-delà de 3 Hz, y compris hors du mode « réduire les clignotements » : orage, météore, Résonance, glitch et Chronomites compris. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `§10`, `32_UX_UI_SPEC.md §6`. *Critère d'acceptation :* mesure image par image sur les cinq séquences. *Priorité :* MUST.

**ENF-ACC-06** — Le texte reste lisible de 100 à 200 % sans troncature, et à 1280 × 800 aucun texte ne descend sous 9 px. *Source :* `32_UX_UI_SPEC.md §6`, `§8`, `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* chaque écran est vérifié à 200 % et à 1280 × 800. *Priorité :* MUST.

**ENF-ACC-07** — Le remappage des commandes est **complet**, et une alternative existe pour toute action nécessitant un maintien. *Source :* `32_UX_UI_SPEC.md §5`, `§6`, `GDD §6.3`. *Critère d'acceptation :* chaque action du tableau `32 §5` est remappable et chaque maintien est convertible en basculement. *Priorité :* MUST.

**ENF-ACC-08** — Une déclaration d'accessibilité est publiée au lancement, et l'applicabilité de la réglementation européenne d'accessibilité à la fonction de communication vocale est vérifiée. *Source :* `GDD §6.3`, `legal/README.md` (document 11, matrice §2). *Critère d'acceptation :* la déclaration est publiée et datée ; l'analyse d'applicabilité est consignée. *Priorité :* MUST.

---

## 7. LOC — localisation et internationalisation

**ENF-LOC-01** — Les langues de l'Early Access sont FR, EN, ES, PT-BR, DE, RU, ZH-Hans et JA, en texte, avec FR et EN à 100 % à la porte G5. *Source :* `70_MARKETING_GTM.md §3`, `11_SCRIPTS_DIALOGUES.md §12`, `50_PRODUCTION_PLAN.md §2`. *Critère d'acceptation :* la couverture de FR et EN atteint 100 % à G5 ; les six autres sont intégrées avant le lancement. *Priorité :* MUST.

**ENF-LOC-02** — L'interface réserve 30 % d'expansion de texte, n'utilise **aucune image contenant du texte**, et formate dates et nombres par le système de traduction. *Source :* `32_UX_UI_SPEC.md §8`. *Critère d'acceptation :* la pseudo-localisation (`51 §8`) ne provoque aucun débordement et ne révèle aucune image textuelle. *Priorité :* MUST.

**ENF-LOC-03** — Les polices disposent d'un repli pour les écritures CJK. *Source :* `32_UX_UI_SPEC.md §8`, `51_QA_TEST_PLAN.md §8`. *Critère d'acceptation :* chaque écran est vérifié en japonais et en chinois simplifié sans glyphe manquant. *Priorité :* MUST.

**ENF-LOC-04** — Les marqueurs de substitution sont identiques dans toutes les langues, et un contrôle automatisé le vérifie. *Source :* `51_QA_TEST_PLAN.md §8`, `11_SCRIPTS_DIALOGUES.md` (en-tête). *Critère d'acceptation :* le script de contrôle échoue si un marqueur manque ou est en trop dans une langue. *Priorité :* MUST.

**ENF-LOC-05** — Aucun doublage n'est nécessaire : les PNJ parlent un charabia synthétique sous-titré, sans imiter de langue réelle. *Source :* `31_AUDIO_DESIGN.md §3`. *Critère d'acceptation :* aucune piste de voix enregistrée dans aucune langue ; chaque réplique a son sous-titre. *Priorité :* MUST.

**ENF-LOC-06** — Les documents juridiques et les textes contractuels sont disponibles en français, conformément à la loi sur l'emploi de la langue française. *Source :* `legal/README.md §2` (ligne « Langue »). *Critère d'acceptation :* CLUF, politique de confidentialité et mentions légales existent en français et sont accessibles en jeu. *Priorité :* MUST.

---

## 8. COMPAT — compatibilité

**ENF-COMPAT-01** — La matrice de configuration de `51 §4` est couverte : Windows 11 (dev, P0), Steam Deck (P0), Windows 10 sur configuration minimale (P1), Linux Ubuntu LTS (P2). *Source :* `51_QA_TEST_PLAN.md §4`. *Critère d'acceptation :* chaque configuration est testée à sa priorité et le résultat est consigné au rapport de campagne. *Priorité :* MUST (P0 et P1), SHOULD (P2).

**ENF-COMPAT-02** — Le jeu fonctionne au clavier-souris **et** à la manette, avec détection automatique du périphérique et des icônes propres au fabricant. *Source :* `32_UX_UI_SPEC.md §5`, `51_QA_TEST_PLAN.md §4`. *Critère d'acceptation :* une manette Xbox et une manette PlayStation sont reconnues et affichent leurs icônes respectives. *Priorité :* MUST.

**ENF-COMPAT-03** — Sur Steam Deck : contrôles natifs, aucun lanceur externe, et textes ≥ 9 px à 1280 × 800. *Source :* `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* checklist Deck verte ; le jeu démarre directement sans intermédiaire. *Priorité :* MUST.

**ENF-COMPAT-04** — Les conditions de réseau testées couvrent le même réseau local, deux réseaux distincts, un partage de connexion mobile (80-150 ms) et une perte simulée de 2 %. *Source :* `51_QA_TEST_PLAN.md §4`. *Critère d'acceptation :* les quatre conditions sont exécutées en priorité P0. *Priorité :* MUST.

**ENF-COMPAT-05** — ***À trancher :*** le niveau de compatibilité Steam Deck visé (« jouable » ou « vérifié ») et une éventuelle sortie macOS ou Linux via couche de compatibilité ne sont pas arbitrés. *Source :* `40_TECHNICAL_DESIGN.md §10`, `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* SHOULD.

---

## 9. OBS — observabilité

**ENF-OBS-01** — L'observabilité repose exclusivement sur des **mesures sans donnée personnelle** : les 14 événements de télémétrie de `20 §13`, agrégés et anonymes. *Source :* `20_GAME_DESIGN_PARAMETERS.md §13`, `60_LEGAL_COMPLIANCE.md §2`. *Critère d'acceptation :* la liste des événements émis est exactement celle de `20 §13`. *Priorité :* MUST.

**ENF-OBS-02** — Les métriques d'expérience suivies sont le temps jusqu'à la première graine (< 30 s), l'abandon du tutoriel (< 10 %), le taux de partage de la carte-récap (15 %) et le temps médian au musée — toutes sous consentement. *Source :* `32_UX_UI_SPEC.md §9`. *Critère d'acceptation :* les quatre métriques sont calculables à partir des événements émis, sans donnée nominative. *Priorité :* SHOULD.

**ENF-OBS-03** — Le profilage technique utilise l'instrumentation du moteur (traces, profils CSV, rapports mémoire), et les traces sont **archivées par build**. *Source :* `40_TECHNICAL_DESIGN.md §10`, `51_QA_TEST_PLAN.md §1`. *Critère d'acceptation :* chaque build de porte dispose de sa trace archivée. *Priorité :* MUST.

**ENF-OBS-04** — Les journaux techniques locaux ne contiennent **aucune donnée personnelle** et restent dans le dossier utilisateur. *Source :* `32_UX_UI_SPEC.md §7`, `GDD §6.1`. *Critère d'acceptation :* inspection après session : aucun pseudonyme, identifiant, adresse IP ni audio. *Priorité :* MUST.

**ENF-OBS-05** — Un tableau de bord qualité est tenu par porte dans `docs/qa/`, avec périmètre, résultats, anomalies par sévérité, risques résiduels et recommandation go/no-go. *Source :* `51_QA_TEST_PLAN.md §10`, `STUDIO_STATE.md`. *Critère d'acceptation :* un fichier existe par porte franchie, et `python3 tools/validate_state.py` refuse un statut `validated` sans lui. *Priorité :* MUST.

---

## 10. MAINT — maintenabilité

**ENF-MAINT-01** — **Aucune valeur de gameplay n'est codée en dur** : tout nombre de jeu vit dans `data/`. *Source :* `20_GAME_DESIGN_PARAMETERS.md` (en-tête), `AGENTS.md §5.5`, `ARCHITECTURE.md` (invariant `data/`). *Critère d'acceptation :* revue de code : toute constante de gameplay trouvée dans le code est une anomalie ; modifier `data/tuning.json` change le jeu sans recompilation. *Priorité :* MUST.

**ENF-MAINT-02** — Toute donnée est validée contre un schéma JSON, et l'intégration continue refuse une donnée non conforme. *Source :* `40_TECHNICAL_DESIGN.md §11`, `ARCHITECTURE.md` (les portes). *Critère d'acceptation :* `python3 tools/validate_data.py` passe, et échoue sur un fichier volontairement invalide. *Priorité :* MUST.

**ENF-MAINT-03** — Toute décision structurelle devient un **ADR écrit avant le code** dans `docs/adr/` ; les ADR 0013 à 0020 sont rédigés en phase P0. *Source :* `40_TECHNICAL_DESIGN.md §14`, `AGENTS.md §5.7`. *Critère d'acceptation :* les huit ADR existent à la sortie de P0 ; aucun écart à `40` n'est implémenté sans ADR. *Priorité :* MUST.

**ENF-MAINT-04** — Un sous-système porte une seule responsabilité, et les dépendances croisées sont remplacées par des événements et des délégués. *Source :* `AGENTS.md §5.6`. *Critère d'acceptation :* revue d'architecture par porte : aucune dépendance circulaire entre sous-systèmes. *Priorité :* MUST.

**ENF-MAINT-05** — La couverture de tests du cœur temporel atteint au moins 90 %, et l'intégration continue tourne en moins de 10 minutes. *Source :* `50_PRODUCTION_PLAN.md §9`. *Critère d'acceptation :* les deux indicateurs sont relevés à chaque fin de sprint. *Priorité :* MUST.

**ENF-MAINT-06** — Chaque anomalie de sévérité S1 ou S2 corrigée reçoit un **test de non-régression**. *Source :* `51_QA_TEST_PLAN.md §1`. *Critère d'acceptation :* aucune correction S1/S2 n'est fermée sans son test. *Priorité :* MUST.

**ENF-MAINT-07** — La « Definition of Done » est respectée pour chaque modification : code, tests verts, lint, audit de licences, clés de traduction créées, documentation ou ADR à jour, revue par le Product Owner, build jouée 5 minutes sans régression. *Source :* `50_PRODUCTION_PLAN.md §4`. *Critère d'acceptation :* la liste de contrôle de la demande de fusion est complétée. *Priorité :* MUST.

---

## 11. PORT — portabilité

**ENF-PORT-01** — Le cœur temporel est un module **pur, sans dépendance au moteur** dans son cœur, ce qui le rend réutilisable et testable hors jeu. *Source :* `40_TECHNICAL_DESIGN.md §1`, `§2`. *Critère d'acceptation :* les tests du cœur s'exécutent sans rendu et sans monde chargé. *Priorité :* MUST.

**ENF-PORT-02** — Le dossier `data/` est embarqué dans le build par le mécanisme de mise en scène du moteur, sans duplication de source de vérité. *Source :* `40_TECHNICAL_DESIGN.md §2`. *Critère d'acceptation :* une modification de `data/` est présente dans le build sans copie manuelle. *Priorité :* MUST.

**ENF-PORT-03** — Le contenu binaire sous licence réside dans un dépôt **privé** séparé, et aucun fichier d'asset ne figure dans le dépôt public. *Source :* `40_TECHNICAL_DESIGN.md §12`, `AGENTS.md §4.5`, `ARCHITECTURE.md`. *Critère d'acceptation :* l'intégration continue échoue si un fichier d'asset apparaît dans le dépôt public. *Priorité :* MUST.

**ENF-PORT-04** — Les dépendances sont versionnées et documentées, et aucune ne flotte sur une étiquette mobile. *Source :* `40_TECHNICAL_DESIGN.md §13`, `tools/versions.env`. *Critère d'acceptation :* `python3 tools/repo_audit.py` refuse une action non épinglée ou un conteneur sur une étiquette flottante. *Priorité :* MUST.

---

## 12. PLAT — conformité des plateformes

**ENF-PLAT-01** — Les règles de la plateforme de distribution sont respectées : succès déclenchables, sauvegarde en nuage fonctionnelle, page conforme aux règles de contenu, et questionnaire de contenu rempli. *Source :* `51_QA_TEST_PLAN.md §9`, `60_LEGAL_COMPLIANCE.md §1`. *Critère d'acceptation :* checklist plateforme verte à la porte G6. *Priorité :* MUST.

**ENF-PLAT-02** — La déclaration sur l'intelligence artificielle est remplie honnêtement : **aucun contenu livré généré par IA** et **aucun contenu généré en direct**, le code écrit avec un assistant relevant des outils de développement exclus de la déclaration. *Source :* `GDD §6.5`, `60_LEGAL_COMPLIANCE.md §8`, `legal/README.md` (document 17). *Critère d'acceptation :* le questionnaire est rempli et cohérent avec un audit des assets livrés. *Priorité :* MUST.

**ENF-PLAT-03** — Les éléments à déclarer en classification d'âge le sont honnêtement, dont les interactions en ligne avec d'autres joueurs (voix non modérée), et une classification est obtenue par le système international en cas de sortie console ou mobile. *Source :* `GDD §6.2`, `60_LEGAL_COMPLIANCE.md §6`, `legal/README.md` (document 19). *Critère d'acceptation :* l'auto-évaluation est cohérente avec le contenu réel et est datée. *Priorité :* MUST.

**ENF-PLAT-04** — Le vidéogramme de jeu présenté comme du gameplay est **réellement capturé en jeu** ; aucune cinématique pré-calculée n'est présentée comme du jeu. *Source :* `33_VISUAL_TARGETS.md §6`. *Critère d'acceptation :* chaque plan du vidéogramme de gameplay est traçable à une session jouée. *Priorité :* MUST.

**ENF-PLAT-05** — Les conditions du service de chat tiers sont vérifiées **avant** l'implémentation du mode streamer, et aucune marque de ce service n'est utilisée au-delà de la mention fonctionnelle. *Source :* `60_LEGAL_COMPLIANCE.md §10`, `40_TECHNICAL_DESIGN.md §9`. *Critère d'acceptation :* la vérification est consignée avant la phase P6. *Priorité :* MUST.

**ENF-PLAT-06** — Seuls les fichiers autorisés par l'accord de distribution sont redistribués avec le jeu. *Source :* `GDD §6.4`. *Critère d'acceptation :* l'audit de licences de la build ne relève aucun fichier non autorisé. *Priorité :* MUST.

---

## 13. LIC — licences et traçabilité des assets

**ENF-LIC-01** — Chaque asset tiers dispose d'un dossier portant sa source (adresse, auteur, date) et sa licence ; les licences acceptées sont CC0, MIT, OFL, Apache-2.0, plus les licences de l'éditeur du moteur pour son contenu propre. *Source :* `GDD §6.4`. *Critère d'acceptation :* `python3 tools/license_audit.py` passe et échoue dès qu'un asset n'a pas sa licence enregistrée. *Priorité :* MUST.

**ENF-LIC-02** — Le fichier des licences tierces est affiché dans le menu « Crédits » du jeu, avec toutes les mentions exigées. *Source :* `GDD §6.4`, `60_LEGAL_COMPLIANCE.md §7`. *Critère d'acceptation :* le menu affiche le contenu du fichier à jour. *Priorité :* MUST.

**ENF-LIC-03** — Toute œuvre commandée (musique, illustration, créature, traduction) fait l'objet d'un **contrat de cession de droits écrit** mentionnant distinctement l'étendue, la destination, le lieu et la durée, avec garantie d'originalité et interdiction d'IA générative sans accord écrit. *Source :* `60_LEGAL_COMPLIANCE.md §7`, `legal/README.md` (document 15). *Critère d'acceptation :* aucun livrable externe n'est intégré sans son contrat signé et archivé. *Priorité :* MUST.

**ENF-LIC-04** — Aucune œuvre, marque, personne, lieu réel identifiable ni symbole religieux ou national réel n'est reproduit. *Source :* `30_ART_BIBLE.md §6`, `10_NARRATIVE_BIBLE.md §2`. *Critère d'acceptation :* revue de contenu par porte, sans occurrence relevée. *Priorité :* MUST.

**ENF-LIC-05** — Aucun média représentant le jeu n'est produit hors du moteur, et aucun média n'est publié avant approbation humaine nominative. *Source :* `33_VISUAL_TARGETS.md` (en-tête), `§8`, `AGENTS.md §4.6`. *Critère d'acceptation :* `python3 tools/check_media_approvals.py` passe ; chaque média publié a sa ligne d'approbation (identifiant, date, validateur, commentaire). *Priorité :* MUST.

**ENF-LIC-06** — La redevance due à l'éditeur du moteur (5 % au-delà de 1 M$ de revenus bruts cumulés) est suivie et provisionnée. *Source :* `GDD §7.1`, `legal/README.md` (document 20). *Critère d'acceptation :* le suivi existe dès la première vente et figure dans le document de fiscalité. *Priorité :* MUST.

---

## 14. ETH — éthique

**ENF-ETH-01** — Aucune loot box, aucun achat aléatoire, aucune mécanique de jeu d'argent, aucun pass payant. *Source :* `GDD §6.2`, `§7.1`, `71_LIVE_OPS.md §5`, `legal/README.md §2`. *Critère d'acceptation :* audit des mécaniques : aucune des quatre n'existe. *Priorité :* MUST.

**ENF-ETH-02** — Aucune pression temporelle artificielle (« FOMO ») : les événements saisonniers ne donnent que des récompenses cosmétiques et ne sont jamais payants. *Source :* `71_LIVE_OPS.md §3`, `§5`. *Critère d'acceptation :* aucun contenu de jeu n'est rendu définitivement inaccessible par une date. *Priorité :* MUST.

**ENF-ETH-03** — Les éventuels contenus additionnels sont cosmétiques ou clairement décrits, à prix fixe, et achetés directement — jamais par monnaie intermédiaire payante. *Source :* `GDD §3.10`, `71_LIVE_OPS.md §5`, `legal/README.md` (document 10). *Critère d'acceptation :* aucune monnaie payante n'existe dans le jeu. *Priorité :* MUST.

**ENF-ETH-04** — La satire vise les institutions et jamais les personnes, les groupes ni les croyants ; aucune humiliation du joueur. *Source :* `10_NARRATIVE_BIBLE.md §2`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0`. *Critère d'acceptation :* revue de contenu humaine avant publication, sans occurrence contrevenante. *Priorité :* MUST.

**ENF-ETH-05** — Une charte éthique et sociale et un code de conduite des joueurs sont publiés, avec signalement et motivation des décisions de modération. *Source :* `legal/README.md` (documents 08, 13, 18), `60_LEGAL_COMPLIANCE.md §6`. *Critère d'acceptation :* les trois documents existent, sont datés et accessibles. *Priorité :* MUST.

**ENF-ETH-06** — L'usage de l'IA dans la production est documenté publiquement : le code est écrit avec un assistant, aucun asset livré n'est généré par IA. *Source :* `GDD §6.5`, `legal/README.md` (document 17). *Critère d'acceptation :* le document de transparence existe et correspond à la réalité de la production. *Priorité :* MUST.

---

## 15. DUR — durabilité

**ENF-DUR-01** — Le jeu ne dépend **d'aucun serveur propriétaire** : il reste jouable tant que la plateforme de distribution fonctionne. *Source :* `71_LIVE_OPS.md §6`, `GDD §6.1`. *Critère d'acceptation :* aucun service propre à l'éditeur n'est requis pour lancer ni terminer une partie. *Priorité :* MUST.

**ENF-DUR-02** — Un mode en réseau local est conservé, y compris en fin de vie du produit. *Source :* `71_LIVE_OPS.md §6`, `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* une partie multijoueur est jouable sur un réseau local sans aucun service en ligne. *Priorité :* MUST.

**ENF-DUR-03** — En cas d'arrêt du développement, un dernier correctif et une communication claire sont publiés. *Source :* `71_LIVE_OPS.md §6`. *Critère d'acceptation :* la procédure est écrite avant le lancement. *Priorité :* SHOULD.

**ENF-DUR-04** — Le monde est reconstituable à partir d'une graine, d'un journal et des recettes, ce qui rend une partie rejouable et archivable indépendamment de l'infrastructure. *Source :* ADR 0002, `40_TECHNICAL_DESIGN.md §1`, `§8`. *Critère d'acceptation :* une capsule archivée rejoue la même vallée sur une version compatible. *Priorité :* MUST.

---

## 16. Récapitulatif

| Domaine | Exigences | Dont points ouverts (*À trancher*) |
|---|---|---|
| PERF — performance | 6 | 0 |
| DET — déterminisme | 6 | 0 |
| RES — réseau et pannes | 6 | 0 |
| SEC — sécurité applicative | 7 | 1 |
| RGPD — confidentialité | 11 | 0 |
| ACC — accessibilité | 8 | 0 |
| LOC — localisation | 6 | 0 |
| COMPAT — compatibilité | 5 | 1 |
| OBS — observabilité | 5 | 0 |
| MAINT — maintenabilité | 7 | 0 |
| PORT — portabilité | 4 | 0 |
| PLAT — plateformes | 6 | 0 |
| LIC — licences | 6 | 0 |
| ETH — éthique | 6 | 0 |
| DUR — durabilité | 4 | 0 |
| **Total** | **93** | **2** |

Vérification et statut de chaque exigence : [`30_MATRICE_EXIGENCES.md`](30_MATRICE_EXIGENCES.md).
