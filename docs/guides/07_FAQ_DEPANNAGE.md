# FAQ et dépannage

**Le dépôt contient-il des images du jeu ?**
Non, volontairement. Le jeu n'existe pas encore : toutes les images seront rendues dans Unreal Engine selon `docs/design/33_VISUAL_TARGETS.md` et `data/shotlist.json`, puis validées par un humain. Les schémas du dépôt expliquent le fonctionnement, ils ne montrent pas le jeu.

**L'IA peut-elle faire un jeu du niveau de GTA ?**
Non. Ces productions mobilisent des centaines de personnes et des budgets de centaines de millions. Le kit vise un jeu indépendant réaliste de très haute qualité, avec des professionnels pour l'art organique (créatures, jeu d'acteur, musique). Voir `docs/guides/03_TEMPS_ET_COUTS.md`.

**Combien ça coûte ?**
De ≈ 40 000 € (solo + IA) à plus de 500 000 € (petite équipe), hors salaire du porteur. Détails dans le guide 03.

**Puis-je vendre le jeu que je crée avec ce kit ?**
Oui (licences MIT et CC BY 4.0, avec attribution). Respectez le CLUF Unreal, les licences Fab/MetaHuman, et choisissez votre propre titre.

**Le serveur MCP Unreal ne répond pas.**
L'éditeur doit être ouvert, les plugins Model Context Protocol et AllToolsets activés, le serveur démarré (`ModelContextProtocol.StartServer`), et Git Bash sur le `PATH` sous Windows.

**La compilation est très lente.**
Exclure les dossiers du projet de l'antivirus (avec prudence), activer le cache DDC partagé, ajouter de la RAM. Compiler en `Development Editor` pendant le développement.

**`privacy_scan.py` bloque mon commit.**
Il a trouvé un e-mail, un numéro, un jeton, un traceur ou un terme de votre liste locale. Corrigez le fichier indiqué ; ne contournez pas le contrôle.

**Les tests Robot Framework échouent localement.**
Lancez `rfbrowser init` une fois après l'installation (télécharge les navigateurs de test).

**Puis-je utiliser des images générées par IA pour aller plus vite ?**
Le kit l'interdit par défaut : risque juridique (droits), perception des joueurs, obligation de déclaration Steam. Si vous le décidez malgré tout, consignez-le dans un ADR, déclarez-le sur Steam et dans `legal/17_transparence-ia.md`.
