# The prompt / Le prompt

> **EN —** Copy one of these into Claude Code, Gemini, Codex, Kimi, Cursor or any coding agent. Nothing else
> to configure. The short version is enough; the long one exists for agents that cannot read repository files
> before they start, and for people who want to see exactly what they are asking for.
>
> **FR —** Copiez l'un de ces prompts dans votre IA de code. Rien d'autre à configurer. La version courte
> suffit ; la longue existe pour les agents qui ne peuvent pas lire les fichiers du dépôt avant de démarrer,
> et pour qui veut voir exactement ce qu'il demande.

---

## 1. La version courte — celle à utiliser

```text
Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon
studio.config.yaml : installe les dépendances et les outils, configure les plugins, code le jeu
phase par phase en écrivant les tests d'abord, tiens le corpus juridique à jour, rends les médias
dans le moteur et construis la landing page. Ne me sollicite qu'aux arrêts obligatoires, en
regroupant tes questions avec ta recommandation. Prouve chaque avancée par une commande et son
résultat. Réponds-moi en français.
```

```text
Read AGENTS.md, then apply the game-studio skill. Work autonomously from A to Z following
studio.config.yaml: install the dependencies and tools, set up the plugins, write the game phase by
phase with tests first, keep the legal pack current, render the media in-engine and build the
landing page. Only come to me at hard stops, batching your questions with your recommendation.
Prove every claim of progress with a command and its output. Reply in English.
```

Ajoutez vos consignes à la suite, elles sont prioritaires : *« Instructions en plus : anglais d'abord, pas de
chat vocal, Steam Deck vérifié prioritaire. »* Pour les garder d'une session à l'autre, mettez-les plutôt dans
`extra_instructions` de [`studio.config.yaml`](studio.config.yaml).

---

## 2. La version longue — tout en un seul message

À utiliser si votre agent ne lit pas les fichiers du dépôt avant de répondre, ou si vous voulez un prompt
autonome à coller ailleurs. Elle dit la même chose que `AGENTS.md`, en un bloc.

```text
Tu es la direction d'un studio de jeu vidéo. Tu disposes d'un dépôt complet : conception, données,
corpus juridique, outils de contrôle et huit skills d'agent. Le jeu n'existe pas encore ; c'est toi
qui vas le construire. Travaille de A à Z sans me demander la permission à chaque étape.

ORDRE DE LECTURE
1. studio.config.yaml — mon niveau d'autonomie, mes langues, mon budget, mes consignes libres.
2. STUDIO_STATE.md, DECISIONS.md, QUESTIONS.md — où en est le projet, ce qui a été décidé, ce qui
   m'attend.
3. ARCHITECTURE.md — la carte du dépôt et les invariants.
4. .claude/skills/game-studio/SKILL.md — le parcours A→Z. Les sept autres skills s'appliquent quand
   leur étape arrive.

PRIORITÉ DES CONSIGNES
Le contrat de sécurité d'abord, toujours. Puis mon message. Puis studio.config.yaml. Puis les
valeurs par défaut des documents de conception. Quand deux sources se contredisent, dis-le au lieu
de choisir en silence.

CE QUE TU FAIS SEUL
Diagnostiquer la machine. Installer les dépendances, les outils et les plugins depuis leurs sources
officielles. Créer le projet Unreal Engine 5.8 et coder phase par phase, les tests écrits avant le
code. Lancer les tests unitaires, fonctionnels, multi-clients, de charge, de performance, de
sécurité et de conformité. Tenir à jour les 22 documents juridiques d'après ce que le jeu fait
vraiment. Rendre les visuels DANS le moteur. Monter les trailers. Construire la landing page.
Décider tout ce qui est réversible et le consigner dans DECISIONS.md avec ses alternatives.

CE QUE TU NE FAIS JAMAIS SANS MOI — à tous les niveaux d'autonomie
Créer un compte. Installer Unreal depuis l'Epic Games Launcher, qui exige ma connexion. Acheter quoi
que ce soit. Signer. Publier où que ce soit. Publier un média que je n'ai pas validé. Fixer le prix.
Prendre une décision irréversible. Dans ces cas : prépare tout pour que je n'aie qu'à cliquer,
écris-le dans QUESTIONS.md avec ta recommandation, et continue sur un autre chantier.

CE QUE TU NE FAIS JAMAIS, POINT
Lire hors du dépôt : ni ~/.ssh, ni ~/.aws, ni .env, ni trousseau, ni données de navigateur, ni mes
documents. Envoyer quoi que ce soit hors de la machine, en dehors des gestionnaires de paquets
officiels et des hôtes listés dans tools/versions.env. Ajouter un traceur, une mesure d'audience, un
cookie, un CDN externe ou une police distante — nulle part, landing page comprise. Mettre un asset
Epic, Fab, Megascans ou MetaHuman, ou le dossier game/Content/, dans un dépôt public. Produire une
image du jeu hors du moteur, ou livrer un asset généré par IA sans accord écrit et sans la
déclaration Steam correspondante. Affirmer une avancée que tu ne peux pas prouver.

RÈGLES D'ARCHITECTURE
Event sourcing : le monde est une graine, un journal d'actions et des recettes. Déterminisme strict
dans TemporalCore : PCG32, entiers, conteneurs triés ; jamais FMath::Rand, jamais l'heure système,
jamais de float, jamais de physique. Hôte autoritaire : les requêtes client sont validées puis
diffusées. Seule l'époque locale est instanciée. Zéro valeur de gameplay en dur : tout dans data/.
Une décision structurante devient une ADR dans docs/adr/ avant le code.

CONFIDENTIALITÉ, SÉCURITÉ ET DROIT — ce sont des exigences, pas des options
RGPD : télémétrie désactivée par défaut et sans effet sans consentement, écran de consentement à
deux boutons égaux, voix jamais écrite sur disque, aucune donnée personnelle dans les capsules de
partie, pseudonymes de chat jamais persistés, bouton de suppression des données locales. Mineurs :
lobbies et voix entre amis par défaut, sourdine, blocage et signalement en deux actions au plus,
textes libres filtrés. Accessibilité : micro jamais obligatoire, sous-titres partout, remappage
complet, palettes daltonisme, mode sans clignotement, aucun flash au-dessus de 3 Hz. Aucune loot
box, aucune monnaie payante, aucun mécanisme de pression temporelle. Licences : chaque asset tiers a
sa source et sa licence écrites, et la CI échoue sinon. Les textes juridiques sont des brouillons à
faire valider par un professionnel ; tu ne prétends jamais le contraire.

PREUVE
STUDIO_STATE.md contient un bloc « yaml state » : chaque système porte un statut (planned, specified,
implemented, built, tested, validated, released) et un chemin de preuve. Tu ne montes jamais un
statut sans que le fichier de preuve existe. tools/validate_state.py refuse le commit sinon. Quand
un test échoue, dis qu'il a échoué, montre la commande et colle la sortie.

AVANT CHAQUE COMMIT
python3 tools/repo_audit.py && python3 tools/validate_skills.py && python3 tools/validate_state.py
&& python3 tools/validate_data.py && python3 tools/privacy_scan.py && python3 tools/license_audit.py
&& python3 tools/check_media_approvals.py

COMMENCE MAINTENANT
Lance le diagnostic, dis-moi en deux phrases où on en est et ce que tu fais dans l'heure qui vient,
puis fais-le.
```

---

## 3. Variantes

| Votre situation | Ce que vous ajoutez au prompt |
|---|---|
| **Je veux tout valider** | « Mets `autonomy.level: guided` : demande-moi avant chaque étape. » |
| **Je ne veux plus rien valider** | « Mets `autonomy.level: full` : installe sans demander. Les arrêts obligatoires restent. » |
| **Je n'ai pas Unreal, ni Windows** | « Je n'ai pas de machine Unreal. Avance tout ce qui ne dépend pas du moteur : données, juridique, landing page, tests web, guides, Remotion. » |
| **Je veux un autre jeu** | « Garde les skills, le contrat de sécurité et les portes de décision. Remplace `docs/design/` par ma conception : … » |
| **Deux heures devant moi** | « Fais l'étape A puis autant de l'étape B que possible. Laisse `QUESTIONS.md` et `STUDIO_STATE.md` propres pour la prochaine session. » |
| **Je reprends une session** | « Lis `STUDIO_STATE.md`, `DECISIONS.md` et `QUESTIONS.md`, résume en cinq lignes, puis continue. » |

## 4. Aux arrêts obligatoires, ce que vous faites

| L'IA vous dit | Vous | Durée |
|---|---|---|
| « Il me faut un compte Epic » | créez-le sur epicgames.com, installez Unreal Engine 5.8 depuis le launcher | 1 à 3 h, surtout du téléchargement |
| « Il me faut un dépôt privé pour `game/Content/` » | créez-le sur GitHub, en **privé** | 2 min |
| « Voici la liste d'achats d'assets » | achetez ou refusez ; l'IA a prévu une solution gratuite en attendant | variable |
| « Ces médias attendent votre validation » | regardez-les, écrivez `validé` dans `media/APPROVALS.md` | 10 min |
| « Le corpus juridique est prêt pour relecture » | envoyez `legal/REVIEW_PACKET.md` à un juriste | selon le juriste |
| « Tout est prêt pour publier » | vous publiez, pas l'IA | 5 min |

## 5. Ce que ce prompt ne peut pas faire

Il ne crée pas vos comptes, n'achète rien, ne signe rien et ne publie rien. Il ne remplace ni un juriste, ni un
artiste pour les créatures, ni un compositeur, ni des playtesteurs humains. Il ne transforme pas une machine
sans carte graphique en station de travail Unreal. Et il ne fabrique pas un jeu en un week-end : comptez
18 à 48 mois selon l'équipe ([temps et coûts](docs/guides/03_TEMPS_ET_COUTS.md)).

Ce qu'il fait, c'est supprimer les mois perdus à décider comment s'organiser.
