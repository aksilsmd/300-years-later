---
name: legal-compliance
description: Tient à jour le corpus juridique complet du projet (legal/) — CGU/CLUF, confidentialité, AIPD, registre, cookies, mentions légales, DSA et modération, mineurs (RGPD/COPPA/Children's Code), monnaies virtuelles (principes CPC 2025), accessibilité (EAA), créateurs, playtests, contrats freelances, sécurité, transparence IA, éthique, classification d'âge, fiscalité et redevances, marque, licences Epic/Fab/MetaHuman. Produit des brouillons à faire relire par un professionnel. Utiliser en phase P7, avant toute mise en ligne, ou quand on parle de « légal », « RGPD », « licence », « marque ».
---

# Skill : legal-compliance

**Tu n'es pas avocat. Chaque document produit porte en tête : « Brouillon — à faire valider par un professionnel du droit ».**

## Sources de vérité
`docs/design/60_LEGAL_COMPLIANCE.md` (cartographie des données, modèles, clauses), `PRIVACY.md`, `SECURITY.md`.

## Livrables
Le corpus complet existe dans **`legal/`** (22 documents, index et matrice des obligations dans `legal/README.md`). Ton travail :
1. **Mettre à jour** chaque document à partir du code réel : traitements effectivement présents, durées, prestataires, options d'accessibilité réellement livrées.
2. Remplacer les champs `[…]` uniquement avec des informations **fournies par l'humain** ; ne jamais inventer d'identité, d'adresse ou de numéro.
3. Ne jamais mettre de coordonnées personnelles de l'humain dans le dépôt public : utiliser une adresse dédiée au projet.
4. Générer `legal/steam-content-survey.md` (réponses proposées au questionnaire Steam, dont la section IA) et `legal/trademark-check.md` (résultats saisis par l'humain).
5. Préparer, pour l'avocat, un dossier `legal/REVIEW_PACKET.md` : liste des documents, questions ouvertes (applicabilité du DSA et de l'EAA, AIPD, cessions), changements depuis la dernière revue.
6. Après validation, intégrer les textes dans le jeu (menus Confidentialité, Crédits, CGU au premier lancement en ligne) et sur la landing page (pied de page, `/.well-known/security.txt`).

## Contrôles à exiger de `game-qa`
Télémétrie no-op sans consentement ; voix jamais écrite ; capsules sans donnée personnelle ; lobbies amis par défaut ; outils de signalement accessibles ; aucun achat réel ni monnaie payante ; aucun traceur ni ressource externe sur la landing (`tools/privacy_scan.py`) ; aucun asset Epic/Fab/MetaHuman dans le dépôt public.

## Points à signaler à l'humain (jamais à trancher seul)
Contrat de travail éventuel ; choix de la structure ; licences Fab/Remotion selon la taille de la structure ; seuils de redevance Unreal ; classification d'âge ; applicabilité DSA/EAA ; médiateur de la consommation.
