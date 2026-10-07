# Corpus juridique et conformité — Afterloom

> ⚠️ **BROUILLONS DE TRAVAIL — NE PAS PUBLIER SANS RELECTURE PAR UN PROFESSIONNEL DU DROIT.**
> Ces documents sont des modèles structurés pour gagner du temps. Ils ne constituent pas un avis juridique. Les champs `[ENTRE CROCHETS]` doivent être complétés par l'éditeur. Droit de référence : droit français et droit de l'Union européenne ; les obligations d'autres pays sont signalées mais doivent être vérifiées localement.

## 1. Index
| # | Document | Public visé | Quand le publier |
|---|---|---|---|
| 01 | [Conditions générales d'utilisation / CLUF](01_cgu-eula.md) | joueurs | avant la démo publique |
| 02 | [Conditions de vente directe](02_conditions-de-vente.md) | acheteurs hors Steam | seulement si vente hors plateformes |
| 03 | [Politique de confidentialité](03_politique-confidentialite.md) | joueurs, visiteurs | avant la démo / mise en ligne du site |
| 04 | [Politique cookies et traceurs](04_politique-cookies.md) | visiteurs du site | mise en ligne du site |
| 05 | [Mentions légales](05_mentions-legales.md) | visiteurs du site | mise en ligne du site |
| 06 | [Analyse d'impact (AIPD/DPIA)](06_aipd.md) | interne, autorité de contrôle | avant la voix en ligne (P6) |
| 07 | [Registre des traitements](07_registre-traitements.md) | interne | dès le premier traitement |
| 08 | [Modération, signalements et DSA](08_moderation-dsa.md) | joueurs | avant la démo |
| 09 | [Protection des mineurs](09_protection-mineurs.md) | joueurs, parents | avant la démo |
| 10 | [Achats, monnaies virtuelles, DLC](10_achats-monnaies-virtuelles.md) | joueurs | avant toute vente de contenu |
| 11 | [Déclaration d'accessibilité](11_accessibilite.md) | joueurs | lancement |
| 12 | [Politique créateurs (streaming, vidéos, partenariats)](12_politique-createurs.md) | créateurs | annonce publique |
| 13 | [Code de conduite des joueurs](13_code-de-conduite.md) | joueurs | avant la démo |
| 14 | [Consentement aux playtests](14_playtest-consentement.md) | testeurs | avant chaque playtest |
| 15 | [Contrats freelances : clauses de cession de droits](15_contrats-freelances.md) | prestataires | avant chaque commande |
| 16 | [Politique de sécurité et divulgation responsable](16_securite-divulgation.md) | chercheurs | mise en ligne du site |
| 17 | [Transparence sur l'intelligence artificielle](17_transparence-ia.md) | joueurs, Steam | page Steam / lancement |
| 18 | [Charte éthique et sociale](18_charte-ethique-sociale.md) | tous | annonce publique |
| 19 | [Classification d'âge](19_classification-age.md) | plateformes | avant la page Steam |
| 20 | [Fiscalité, redevances, sanctions](20_fiscalite-redevances.md) | interne | création de la structure |
| 21 | [Marque, nom et propriété intellectuelle](21_marque-pi.md) | interne | avant l'annonce |
| 22 | [Licences tierces et obligations Epic/Fab/MetaHuman](22_licences-tierces.md) | interne, joueurs (crédits) | en continu |

## 2. Matrice des obligations (synthèse)
| Domaine | Texte principal | Ce que le jeu fait | Document |
|---|---|---|---|
| Données personnelles | RGPD (UE 2016/679), loi Informatique et Libertés | minimisation, opt-in, voix non enregistrée, droits | 03, 06, 07 |
| Traceurs | art. 82 loi Informatique et Libertés, lignes directrices CNIL | aucun traceur sur le site ni dans le jeu sans consentement | 04 |
| Mineurs | RGPD art. 8 (France : 15 ans), COPPA (États-Unis, < 13 ans), Children's Code (Royaume-Uni) | amis par défaut, aucune publicité ciblée, contrôle parental | 09 |
| Services numériques | Règlement sur les services numériques (DSA, UE 2022/2065) | signalement, motivation des décisions, point de contact (applicabilité à confirmer) | 08 |
| Consommation | Code de la consommation, directive 2019/770 (contenus numériques), principes CPC 2025 sur les monnaies virtuelles | prix clairs, pas de monnaie payante, rétractation via la plateforme | 01, 02, 10 |
| Jeux d'argent | législations nationales (ex. Belgique sur les loot boxes) | **aucune loot box** | 10 |
| Accessibilité | European Accessibility Act (directive 2019/882) — applicabilité aux jeux à confirmer | options étendues, déclaration | 11 |
| Communication commerciale | loi n° 2023-451 (influence commerciale), règles des plateformes | mention « collaboration commerciale » exigée des créateurs rémunérés | 12 |
| Langue | loi n° 94-665 (Toubon) | textes et conditions disponibles en français | tous |
| IA | Règlement IA (UE 2024/1689), règles Steam de déclaration | aucun contenu livré généré par IA ; transparence | 17 |
| Propriété intellectuelle | Code de la propriété intellectuelle (L131-3), droit des marques | cessions écrites, dépôt de marque | 15, 21, 22 |
| Plateformes | accord de distribution Steamworks, CLUF Unreal, licences Fab/MetaHuman | respect des conditions, crédits | 19, 20, 22 |

## 3. Procédure de validation
1. L'IA (skill `legal-compliance`) complète ce qui peut l'être à partir du code réel (traitements effectifs, durées, prestataires).
2. Le porteur du projet remplit les champs `[…]`.
3. Un avocat valide ; ses corrections sont intégrées ; la version publiée est datée et archivée.
4. Toute évolution du jeu touchant aux données, aux achats ou à la communication entre joueurs déclenche une revue.
