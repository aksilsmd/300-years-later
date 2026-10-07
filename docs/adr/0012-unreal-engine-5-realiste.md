# ADR 0012 — Passage à Unreal Engine 5.8 et à une direction artistique réaliste

- **Statut :** Accepté — remplace ADR 0001 (Godot 4.7) et la direction « low-poly » de la v1
- **Date :** 2026-10-07
- **Décideur :** Product Owner

## Contexte
Le porteur du projet vise un rendu **3D réaliste** comparable aux grandes productions (environnements photoréalistes, personnages crédibles, éclairage cinématographique). Godot ne fournit pas l'équivalent industriel de l'éclairage global dynamique, de la géométrie virtualisée, des humains numériques et de la génération procédurale à grande échelle.

## Options envisagées
1. **Godot 4.7** — libre, léger, mais rendu réaliste limité et outillage AAA absent.
2. **Unity 6 (HDRP)** — rendu de qualité, mais HDRP en retrait et écosystème humain numérique moins intégré.
3. **Unreal Engine 5.8** — Lumen (et Lumen Lite / Medium pour machines modestes), Nanite et Nanite Foliage, MegaLights, PCG prêt pour la production, World Partition + Data Layers, MetaHuman Creator intégré à l'éditeur, Movie Render Graph, Iris (réplication), Chaos, Niagara, MetaSounds ; plugin **officiel Epic** pour piloter l'éditeur depuis Claude Code via MCP.

## Décision
**Unreal Engine 5.8** (dernière version majeure de la génération 5), C++ pour le cœur (event sourcing déterministe), Blueprints pour l'assemblage et le contenu, Python d'éditeur pour l'automatisation.

## Conséquences
- **Licence moteur :** gratuit jusqu'à 1 M$ de revenus bruts cumulés par produit, puis 5 % de redevance ; ventes sur l'Epic Games Store exonérées. À intégrer au plan d'affaires.
- **Assets réalistes :** MetaHuman gratuit sous 1 M$ de revenus annuels ; Megascans **payants via Fab depuis 2025** ; budget d'assets et d'artistes à prévoir (`docs/guides/03_TEMPS_ET_COUTS.md`).
- **Dépôt public :** les assets Fab/Megascans/MetaHuman et le code du moteur **ne doivent jamais être publiés** dans un dépôt public (licences). Le contenu binaire vit dans un dépôt privé (Git LFS ou Perforce) ; le dépôt public ne contient que conception, code du projet, données et outils.
- **Matériel :** PC Windows 10/11 64 bits, GPU RTX 3070/4070 ou mieux, 32-64 Go de RAM, SSD NVMe 1 To.
- **CI :** runner Windows auto-hébergé (les compilations UE dépassent les runners GitHub gratuits).
- **Steam Deck :** objectif « jouable » en 30 i/s avec Lumen Medium ; la vérification Deck devient un objectif secondaire.
- **Taille du jeu :** 15-30 Go.
- **Réécrits :** `30_ART_BIBLE.md`, `33_VISUAL_TARGETS.md` (nouveau), `40_TECHNICAL_DESIGN.md`, `80_CLAUDE_CODE_PLAYBOOK.md`, tous les skills.
- **Inchangés :** concept, histoire, scripts, scénarios, recettes, contrats, règles d'event sourcing et de conformité.
- **Aucune image de jeu n'est fournie dans le dépôt** : toutes les images sont produites par l'IA dans Unreal à partir des cahiers de rendu (`33_VISUAL_TARGETS.md`, `data/shotlist.json`), puis validées par un humain.
