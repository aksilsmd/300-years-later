# 60 — Juridique et conformité
Propriétaire : Product Owner · v1.0
> **Avertissement :** modèles de travail rédigés pour accélérer le travail d'un professionnel, pas un avis juridique. Faire relire par un avocat (droit du numérique / PI) et un expert-comptable avant G5.

## 1. Checklist par gate
| Gate | Obligation | Statut |
|---|---|---|
| G0 | Relire le contrat de travail : exclusivité, cession PI, cumul d'activité ; si doute, demande écrite à l'employeur | ☐ |
| G3 | Recherche d'antériorité du nom (INPI, EUIPO/TMview, USPTO, Steam, domaines, réseaux) ; dépôt UE classes 9 et 41 | ☐ |
| G3 | Création de la structure (micro-entreprise ou société) ; compte Steamworks au nom de la structure ; entretien fiscal Steam | ☐ |
| G3-G4 | Contrats de cession signés : illustrateur, compositeur, traducteurs | ☐ |
| G5 | Politique de confidentialité, mentions légales, CLUF publiés (FR/EN) et accessibles en jeu | ☐ |
| G5 | Registre des traitements ; analyse d'impact non requise a priori (pas de traitement à grande échelle de données sensibles) — à confirmer | ☐ |
| G6 | Questionnaire de contenu Steam (dont IA) ; auto-évaluation d'âge ; Crédits + licences tierces | ☐ |

## 2. Cartographie des données (registre des traitements simplifié)
| Traitement | Données | Finalité | Base légale (RGPD art. 6) | Destinataires | Conservation |
|---|---|---|---|---|---|
| Jeu en ligne | SteamID, pseudo Steam (traités par Steam) ; slot de joueur en session | Faire fonctionner le multijoueur | Exécution du contrat | Valve (relais), autres joueurs | Durée de la session |
| Voix | Flux audio en direct | Communication entre joueurs | Exécution du contrat | Autres joueurs de la session via Steam | Aucune (non enregistrée) |
| Progression | Chronos, déblocages, réglages | Sauvegarde | Exécution du contrat | Steam Cloud | Jusqu'à suppression |
| Télémétrie (opt-in) | Événements anonymes (TDD/20 §13) | Améliorer le jeu | Consentement | Hébergeur UE | 13 mois max |
| Rapports de crash (opt-in) | Pile d'appels, version, OS, GPU | Corriger les bugs | Consentement | Hébergeur UE | 90 jours |
| Mode streamer | Commandes de chat lues en mémoire | Votes des spectateurs | Intérêt légitime du streamer qui l'active | Aucun | Aucune |
| Playtests | Questionnaires, vidéos (si accord) | Améliorer le jeu | Consentement écrit | Product Owner | 3 mois |

Aucun cookie, aucun traceur publicitaire, aucun transfert hors UE hors Valve (qui agit selon ses propres conditions pour Steam).

## 3. Politique de confidentialité — modèle (FR, à adapter)
> **Politique de confidentialité de [TITRE]**
> Éditeur : [Structure], [adresse], [contact email dédié]. 
> **Ce que le jeu ne fait pas :** il n'enregistre jamais votre voix, n'affiche aucune publicité, ne vend aucune donnée et ne collecte rien sans votre accord en dehors du strict nécessaire au jeu en ligne.
> **Données nécessaires au jeu :** le multijoueur passe par Steam (Valve), qui traite votre identifiant Steam selon sa propre politique. Votre voix est transmise en direct aux joueurs de votre partie, sans enregistrement.
> **Données facultatives :** si vous l'acceptez, le jeu envoie des statistiques anonymes (ex. durée des parties, recettes déclenchées) et des rapports de plantage, hébergés dans l'Union européenne. Vous pouvez retirer votre accord à tout moment dans Options › Confidentialité.
> **Vos droits :** accès, rectification, effacement, opposition, limitation, retrait du consentement, réclamation auprès de la CNIL (cnil.fr). Contact : [email].
> **Mineurs :** le jeu active par défaut les parties « amis seulement » ; les parents peuvent utiliser le contrôle parental de Steam (Family View).
> Dernière mise à jour : [date].

## 4. CLUF (EULA) — points à couvrir
Licence d'utilisation personnelle non exclusive ; interdictions (triche, revente de comptes, rétro-ingénierie sauf exceptions légales) ; contenu créé par les joueurs (noms de statues, capsules) : licence non exclusive accordée à l'éditeur pour l'affichage en jeu ; conduite en ligne (harcèlement interdit, signalement) ; Early Access (contenu évolutif, sauvegardes possiblement réinitialisées avec préavis) ; **autorisation explicite de streamer et monétiser des vidéos du jeu** (politique créateurs) ; responsabilité limitée dans les limites du droit français de la consommation ; droit applicable français, sans préjudice des droits impératifs du consommateur.

## 5. Écran de consentement (texte en jeu)
Voir `11_SCRIPTS_DIALOGUES.md` (PRIVACY_TITLE, PRIVACY_BODY). Exigences : deux boutons de même poids visuel (« Jouer sans rien partager » / « Aider avec des statistiques anonymes ») ; lien vers la politique ; choix modifiable à tout moment ; aucune case pré-cochée.

## 6. Mineurs et sécurité en ligne
- Cible d'âge : tout public à partir de 7-12 ans (violence cartoon légère, aucune interaction monétaire). Steam ne requiert pas de classification PEGI pour le PC, mais l'auto-évaluation du questionnaire Steam doit être cohérente ; si sortie console : questionnaire **IARC**.
- Éléments PEGI à déclarer honnêtement : interactions en ligne avec d'autres joueurs (voix non modérée) → mention « interactions en ligne non classées ».
- Mesures : lobbies amis par défaut, mute/blocage en 1 clic, signalement (vers Steam + lien contact), noms de statues filtrés, poses prédéfinies uniquement (pas de pose libre détournable), aucune loot box.

## 7. Propriété intellectuelle
- **Nom :** « Century Temps » reste nom de code. Candidats publics à vérifier : *Temporis*, *Intérim Temporel*, *300 Ans Plus Tard*, *Chronotemps*, *Temporis Intérim*. Critères : prononçable en FR/EN, disponible en classes 9/41, domaine .com/.fr libre, handle réseaux libre, pas de confusion avec un jeu existant.
- **Œuvres commandées** (art. L131-3 CPI : chaque droit cédé doit être mentionné distinctement, avec étendue, destination, lieu, durée) — clauses minimales :
  - Objet : [liste des livrables].
  - Droits cédés : reproduction, représentation, adaptation, traduction, exploitation commerciale (jeu, DLC, bande originale, marketing, produits dérivés).
  - Étendue : monde entier ; durée : durée légale de protection ; tous supports connus et à venir prévisibles.
  - Rémunération forfaitaire (cas autorisés par l'art. L131-4 pour les logiciels/jeux et œuvres de commande publicitaire — à valider par l'avocat) ou proportionnelle.
  - Garantie d'originalité et d'absence d'éléments tiers ; interdiction d'utiliser de l'IA générative sans accord écrit.
  - Droit moral : mention au générique.
- **Code et données :** propriété de la structure ; dépôt de code daté conseillé (ex. enveloppe Soleau ou horodatage).
- **Licences tierces :** CLUF Unreal Engine (redevance 5 % au-delà de 1 M$), licences Fab (Megascans payants depuis 2025), licence MetaHuman, polices OFL → `THIRD_PARTY_LICENSES.md`. Le corpus juridique complet est dans `legal/`.

## 8. IA générative — déclaration Steam (proposition de réponses)
- **Contenu pré-généré :** « Non » si aucun asset livré n'est généré par IA (recommandé). Le code écrit avec un assistant relève des outils de développement exclus de la déclaration depuis la mise à jour de janvier 2026 — vérifier le libellé exact du formulaire au moment de remplir.
- **Contenu généré en direct :** « Non » (textes du musée = modèles de phrases écrits à la main, combinés de façon procédurale).
- Si un asset IA est un jour utilisé : le déclarer, décrire précisément l'usage, garder les preuves de droits.

## 9. Consommateur et commerce
- Prix TTC affichés par Steam ; TVA UE collectée par Valve. Remboursements : politique Steam.
- Early Access : page Steam conforme aux règles (état actuel, feuille de route, prix futur).
- Facturation des freelances, déclarations de revenus : expert-comptable.

## 10. Twitch et créateurs
- Mode streamer : lecture du chat sans stockage ; vérifier les conditions développeur Twitch avant la phase 6 ; aucun usage des marques Twitch dans le jeu au-delà de la mention fonctionnelle.
- Politique créateurs publique : streaming et monétisation autorisés, musique sans risque de réclamation.
