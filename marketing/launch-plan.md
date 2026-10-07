# Plan de lancement — gabarit

| Moment | Action | Responsable |
|---|---|---|
| G3 | marque déposée, page Steam « à venir », trailer d'annonce, presskit, communauté (Discord ou équivalent) | vous + IA |
| G3 → G6 | un clip court par semaine (format vertical, idées ci-dessous), devlog mensuel | IA prépare, vous publiez |
| G4 | test fermé avec 10 créateurs (50-5 000 spectateurs), clés via une plateforme dédiée | vous |
| G6 − 6 semaines | démo publique, relances presse et créateurs | vous |
| Steam Next Fest | streams quotidiens, lobbies spectateurs | vous |
| Lancement EA | remise de lancement, pack 4 exemplaires, trailer de lancement | vous |

## 12 idées de clips « avant / après » (rendus Unreal)
1. La graine qui devient chêne… sur la tête d'un ami. 2. Trois cailloux devenus site touristique avec boutique. 3. Le barrage de branches devenu station balnéaire. 4. La pose ratée devenue statue géante en néon. 5. Le mammouth nourri devenu mascotte de la ville. 6. Le percepteur qui confisque une cuillère devenue « Trésor du Baron ». 7. Le feu « maîtrisé » devenu champ fertile. 8. L'objet du futur élu maire en l'an 300. 9. Le canyon creusé à la pelle. 10. Les Chronomites qui grignotent un pont. 11. Le musée qui se trompe sur tout. 12. Le saboteur démasqué à la pause café.

## Critères de sélection des créateurs (l'humain fait la recherche)
Jeux coop et comédie, communauté bienveillante, public majoritairement adulte ou mixte encadré, transparence sur les partenariats (loi influence commerciale), pas de contenu haineux.

## Indicateurs
Listes de souhaits par jour, conversion démo → liste de souhaits, taux de partage des clips, temps médian de démo, part des avis positifs.

## Faire connaître le **kit** (distinct du jeu)
> **EN —** The repository and the game need different channels. These are for the repository.

Le dépôt se trouve par trois chemins, dans cet ordre d'efficacité réelle :

1. **Les listes et les registres.** C'est le canal n°1 pour un dépôt de skills. Proposer l'entrée aux listes
   « awesome » du domaine (awesome-claude-code, awesome-claude-skills, awesome-agent-skills) en suivant leur
   procédure de contribution, et publier le plugin via `.claude-plugin/marketplace.json` (déjà en place :
   `/plugin marketplace add aksilsmd/300-years-later`).
2. **La recherche GitHub.** Elle pèse sur le nom, la description et les *topics* — pas sur le README. Les
   trois doivent être remplis (`bash tools/setup_repo.sh`), avec des synonymes volontaires
   (`agent-skills` **et** `ai-agents`, `unreal-engine` **et** `game-development`).
3. **Le web et les modèles de langage.** Google indexe le README et la page GitHub Pages ; les modèles lisent
   `llms.txt`, les balises JSON-LD de la landing et les READMEs. Les trois existent. Ce qui compte ensuite est
   d'être **cité ailleurs** : un billet, un fil, une démonstration vidéo valent plus que n'importe quel
   réglage de balise.

Publications ponctuelles à préparer (textes FR + EN) : un fil « j'ai fait tourner un studio de jeu avec une
IA, voici ce qui a marché et ce qui a échoué », un retour d'exécution complet dans `docs/runs/`, et une
démonstration vidéo de deux minutes du parcours A → Z. Aucune de ces publications n'annonce le jeu : elles
parlent du kit, avec la même honnêteté que le README (le jeu n'existe pas encore).
