# Guide de A à Z

🇬🇧 [English version](en/01_A_TO_Z.md)

Ce guide décrit le parcours complet, du dépôt cloné au jeu en accès anticipé, tel que le pilote le skill `game-studio`. Pour chaque étape : **qui** fait quoi, **ce que vous devez vérifier**, et **la durée indicative** (scénario « studio réduit » de [03_TEMPS_ET_COUTS.md](03_TEMPS_ET_COUTS.md)).

![Parcours A → Z](../diagrams/01_parcours_a_z.svg)

## Légende des rôles
- **IA** : Claude Code (ou un autre agent) appliquant les skills, en mode `autonomous` par défaut (`studio.config.yaml`).
- **Vous** : le porteur du projet, qui décide, achète, valide et publie.
- **Pro** : un professionnel externe (juriste, artiste, compositeur…).

## A. Diagnostic — 1 heure
**IA** lance `tools/doctor.py`, vérifie le matériel, lit `STUDIO_STATE.md`.
**Vous** lisez le rapport. Si le PC est insuffisant, l'IA peut quand même avancer la conception, la landing page et le juridique.

## B. Installation — 1 à 3 jours (téléchargements longs)
**IA** affiche le plan d'installation (`install_windows.ps1 -Plan`), puis l'exécute après un accord global unique (sans demander en mode `full`). Le plugin Epic et `frontend-design` sont déjà déclarés dans `.claude/settings.json`.
**Vous** créez le compte Epic, installez Unreal Engine 5.8 depuis l'Epic Games Launcher, installez le plugin officiel Epic dans Claude Code, activez le serveur MCP dans l'éditeur. Détails : [02_INSTALLATION.md](02_INSTALLATION.md).
**Vérification** : `doctor.py` tout vert ; l'IA liste les acteurs de la carte ouverte via MCP.

## C. Personnalisation — 1 jour
**IA** lit `studio.config.yaml` ; **vous** n'intervenez que si le fichier est vide ou si vous voulez changer le titre public, les langues, les plateformes ([05_PERSONNALISER.md](05_PERSONNALISER.md)). **Pro** (ou vous) : recherche d'antériorité de la marque (`legal/21_marque-pi.md`).
**Vérification** : `STUDIO_STATE.md` à jour.

## D. Fondations (P0) — 2-3 semaines
**IA** crée le projet Unreal C++ (`game/`), les modules `TemporalCore` et `TemporalValley`, la CI Windows, les décisions d'architecture (ADR).
**Vous** créez le dépôt **privé** pour le contenu binaire (`game/Content/`), installez un runner GitHub Windows si vous voulez la CI du jeu.
**Vérification** : compilation verte, tests automatiques verts.

## E. Prototype du fun (P1) — 4-8 semaines · **Porte G1**
**IA** code le cœur temporel (tests d'abord) puis un prototype jouable : planter une graine en l'an 0 fait pousser un arbre en l'an 300.
**IA** fait jouer des bots et s'auto-évalue sur les piliers de design, puis place dans `QUESTIONS.md` un playtest humain (non bloquant en mode autonome). **Vous** organisez ce playtest avec 5 personnes (kit fourni : `legal/14_playtest-consentement.md`, grille dans `docs/design/51`).
**Décision** : si personne ne rit ni ne s'étonne en 10 minutes, on itère ; deux échecs = pivot.

## F. Multijoueur (P2) — 6-10 semaines · Porte G2
**IA** : sessions Steam (AppID de test), 4 joueurs, 4 époques, fantômes, contrôle d'intégrité.
**Vous** : session de test à 4 avec des amis.
**Vérification** : test Gauntlet « 4 hash identiques ».

## G. Boucle de partie (P3) — 8-12 semaines · **Porte G3**
**IA** : manches, pause café, rotation, contrats, paradoxes, dangers, HUD.
**Vous** : playtest de 8 personnes ; dépôt de la marque ; ouverture de la page Steam (Steam Direct) ; commande de la capsule.
**Vérification** : note « je rejouerais » ≥ 4/5.

## H. Monde réaliste et contenu (P4) — 6-12 mois
**IA** prépare la **liste d'achats** d'assets (Fab, MetaHuman) avec licences et coûts.
**Vous** achetez et ajoutez les assets ; commandez les créatures à un artiste ; validez la direction artistique.
**IA** construit le paysage, les époques, la végétation procédurale, les prefabs de vieillissement, mesure les performances.
**Vérification** : 10 graines de monde jouables ; budgets de performance tenus sur les 3 profils.

## I. Machine à clips (P5) — 6-10 semaines
Musée de fin de partie, capsules partageables, mode solo, tutoriel, mode photo.

## J. Voix, streamer, saboteur (P6) — 6-8 semaines · Porte G4 (alpha)
**IA** : voix inter-époques, outils anti-harcèlement, mode streamer (désactivé par défaut).
**Vérification** : test « aucun audio sur disque », 3 streamers en test fermé.

## K. Conformité (P7) — 8-12 semaines · **Porte G5 (bêta)**
**IA** met à jour le corpus `legal/` d'après le jeu réel et prépare le dossier pour l'avocat.
**Pro** : relecture juridique. **Vous** : intégrez les corrections.
**IA** + **vous** : accessibilité complète, localisation, pseudo-localisation.

## L. Démo et Steam (P8) — 8-12 semaines · Porte G6
Build démo, succès, classements, Cloud, profilage, build Shipping. Questionnaire de contenu Steam (dont la section IA).

## M. Médias — en continu dès G3
**IA** rend les plans de `data/shotlist.json` **dans Unreal** (Movie Render Graph), monte les trailers (Sequencer + Remotion).
**Vous** validez chaque image dans `media/APPROVALS.md`. Aucune image non validée n'est publiée.

## N. Landing page — 1-2 semaines, puis mises à jour
**IA** construit la landing **cinématique** (`docs/design/34_LANDING_CINEMATIQUE.md`) : mode typographique animé tant qu'aucun rendu n'est validé, puis bascule automatique vers le héros vidéo et la séquence des 4 époques au défilement dès que les plans L00–L04 sont validés ; elle lance les tests (Robot Framework, Lighthouse, k6, OWASP ZAP).
**Vous** validez les textes et déclenchez la publication (workflow manuel `pages.yml`).

## O. Lancement — 4-8 semaines
Steam Next Fest, programme créateurs (`legal/12_politique-createurs.md`), communication. **Vous** publiez ; l'IA prépare.

## Z. Après le lancement
Correctifs sous 72 h pour les problèmes graves, mises à jour régulières, saisons (`docs/design/71_LIVE_OPS.md`).

---
**Pendant les arrêts obligatoires**, l'IA prépare tout (liste de clics, fichiers) et continue les chantiers indépendants (landing, juridique, données, Remotion).

**Rappel :** l'IA ne fait jamais seule un achat, une publication, une signature, ni ne choisit le nom ou le prix. Voir [04_SECURITE_ET_CONFIDENTIALITE.md](04_SECURITE_ET_CONFIDENTIALITE.md).
