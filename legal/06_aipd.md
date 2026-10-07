# Analyse d'impact relative à la protection des données (AIPD / DPIA)
> BROUILLON — méthode inspirée de la CNIL (outil PIA). À compléter avec les choix techniques définitifs et à faire valider.

## 1. Pourquoi une AIPD
Deux critères de la liste du Comité européen de la protection des données peuvent être réunis : **personnes vulnérables** (mineurs susceptibles de jouer) et **communication entre personnes** (voix en ligne). Même si l'obligation formelle (article 35 RGPD) reste à confirmer, l'AIPD est réalisée par précaution.

## 2. Description
| Élément | Description |
|---|---|
| Traitements | jeu en ligne, voix en direct, noms de statues, signalements, statistiques facultatives |
| Personnes concernées | joueurs (dont potentiellement des mineurs), spectateurs en mode streamer |
| Données | identifiants de plateforme, flux vocal (non conservé), textes courts, événements anonymisés |
| Supports | clients de jeu, relais Valve, hébergeur UE pour les statistiques facultatives |

## 3. Nécessité et proportionnalité
Minimisation (aucun compte propre, aucun texte libre au-delà de 16 caractères, aucune conservation de la voix), finalités déterminées, bases légales (§ politique), durées courtes, information claire, droits effectifs, opt-in pour le facultatif.

## 4. Risques
| Risque | Source | Vraisemblance | Gravité | Mesures | Risque résiduel |
|---|---|---|---|---|---|
| Harcèlement vocal d'un mineur par un inconnu | lobbies publics | modérée | importante | amis par défaut, mute/blocage en 1 clic, signalement, parties publiques en opt-in, rappel au code de conduite | limité |
| Exposition d'un pseudo ou d'un code d'invitation en stream | mode streamer | modérée | limitée | masquage automatique, filtre de noms | négligeable |
| Contenu offensant dans les noms de statues | joueurs | modérée | limitée | filtre, longueur ≤ 16, signalement, suppression | négligeable |
| Ré-identification via les statistiques | télémétrie | faible | limitée | opt-in, pas d'identifiant, agrégation, hébergement UE | négligeable |
| Fuite des enregistrements de playtest | stockage interne | faible | importante | chiffrement, accès restreint, suppression à 3 mois | limité |
| Accès illégitime à l'éditeur via l'IA de développement | outils | faible | importante | aucun accès de l'IA aux données des joueurs, contrat de sécurité des skills | négligeable |

## 5. Validation
Avis du délégué/conseil : [ ] · Décision du responsable : [ ] · Date de révision : à chaque ajout de fonction sociale.
