# 35 — Charte graphique et design system
Propriétaire : Product Owner · v1.0 · 7 octobre 2026
> **EN —** The brand and the design system for everything the **public** sees outside the game engine:
> repository, documentation, landing page, press kit, social cards. Tokens live in `design-system/tokens.css`
> (and `tokens.json`). The game's in-engine art direction stays normative in `30_ART_BIBLE.md` and
> `33_VISUAL_TARGETS.md`; this document never overrides them, it harmonises with them.

## 0. Périmètre

| Couvert par ce document | Couvert ailleurs |
|---|---|
| Marque, logo, couleurs, typographie, grille, ton visuel | Direction artistique **dans le moteur** → `30_ART_BIBLE.md` |
| Landing page, README, dépôt, presskit, cartes sociales, PDF | Plans à rendre dans Unreal → `33_VISUAL_TARGETS.md` |
| HUD et UI du jeu : **grille, couleurs d'époque, règles d'accessibilité** | Maquettes et flux d'écrans → `32_UX_UI_SPEC.md` |

**Règle d'or :** aucune image de jeu ne sort du moteur. Tout ce que cette charte décrit est **typographique,
géométrique ou documentaire**. Les assets de marque livrés avec le dépôt (`docs/assets/`) ne représentent
jamais le jeu.

## 1. Le parti pris : un relevé géologique

La vallée est un lieu dont on lit l'histoire **en coupe**. Toute l'identité découle de là : une carotte
stratigraphique, quatre strates de trois cents ans, une trace qui grossit en descendant. Chaque élément de
structure **encode une information** — une bande est une époque, un disque est une trace qui a vieilli, un
filet est une limite de couche, un chiffre en chasse fixe est une mesure. Rien n'est décoratif.

Ce que la charte refuse explicitement, parce que c'est le réflexe par défaut et qu'il ne dit rien de ce
projet : fond crème chaud avec serif de titrage et accent terre cuite ; cartes arrondies identiques avec
ombre douce ; dégradés d'ambiance ; étiquettes en capitales espacées au-dessus de chaque titre ; flèche « → »
collée aux libellés de bouton.

## 2. Couleur

Valeurs normatives : `design-system/tokens.css`. Planche : [`docs/assets/palette.png`](../assets/palette.png).

| Rôle | Jeton | Valeur | Emploi |
|---|---|---|---|
| Support | `--af-paper` | `#E9E7E0` | fond de page |
| Support creusé | `--af-paper-sunk` | `#E3E1D9` | panneaux, encarts, champs de saisie |
| Encre | `--af-ink` | `#15191A` | texte principal |
| Encre pâle | `--af-ink-soft` | `#6E7169` | légendes, mesures, métadonnées |
| Filet | `--af-rule` | `rgba(21,25,26,.28)` | limites de couche, séparateurs |
| Strate an 0 | `--af-era-0` | `#76875A` | lichen — L'Aube |
| Strate an 300 | `--af-era-1` | `#8A6B1E` | ocre — Les Bannières |
| Strate an 600 | `--af-era-2` | `#4E5257` | suie — La Vapeur |
| Strate an 900 | `--af-era-3` | `#1C6F62` | vert-de-gris — Le Néon |
| Sédiments | `--af-bed-0..3` | — | fonds de bande, très désaturés |
| Signal | `--af-signal` | `#8C2F22` | **uniquement** erreur, perte, arrêt obligatoire |

**Règles.**
1. La couleur ne porte **jamais** seule une information : toujours doublée d'une icône, d'un libellé ou d'une
   forme (`32` §6, daltonisme).
2. Le rouge de relevé n'est pas une couleur de marque. S'il apparaît deux fois sur un écran, l'une des deux
   n'est pas une alerte.
3. Contraste minimum AA sur les quatre strates, en clair comme en sombre. Vérifié : encre sur papier 14,8:1 ;
   encre pâle sur papier 4,6:1 ; chaque strate sur son sédiment ≥ 4,5:1 pour du texte de 16 px et plus.
4. Le thème sombre passe le relevé en négatif et **garde les teintes d'époque** : une époque se reconnaît à sa
   couleur dans les deux thèmes.

## 3. Typographie

Deux familles, trois rôles. Pas de police distante : les piles système sont la valeur par défaut et aucun
fichier n'est chargé depuis un CDN (`AGENTS.md` §4.3).

| Rôle | Pile | Usage |
|---|---|---|
| Display et texte | `--af-sans` (grotesque système) | titres, corps, interface |
| Mesure | `--af-mono` | années, dimensions, identifiants, commandes, tout ce qui est une donnée |
| Voix du monde | `--af-serif` | **seulement** les citations in-world : Chronique, plaques de musée, extraits du roman |

Échelle : `--af-step--1` à `--af-step-4`, construite sur une progression fluide. Titrage à `-0.035em`
d'approche, corps à `1.55` d'interligne, serif à `1.65`, longueur de ligne sous 80 caractères
(`--af-measure: 68ch`).

**Interdits typographiques :** accentuer un seul mot d'un titre en italique ou en couleur ; capitales
espacées comme sur-titre ; un libellé au-dessus de chaque bloc ; la chasse fixe pour du texte courant — elle
est réservée aux mesures, c'est ce qui lui donne son sens ici.

## 4. Grille et mise en page

Une feuille de relevé : marge gauche étroite pour les annotations, champ principal large, filets horizontaux
qui marquent les limites de couche.

```
┌──────────┬──────────────────────────────────────────────┐
│ an 0     │  TITRE                                        │
│  ·       │  accroche sur une ligne                       │
├──────────┼──────────────────────────────────────────────┤
│ an 300   │  corps de texte, < 80 caractères              │
│  ●       │                                               │
├──────────┼──────────────────────────────────────────────┤
│ an 600   │  ┌ commande ───────────────┐                  │
│  ⬤       │  └─────────────────────────┘                  │
├──────────┼──────────────────────────────────────────────┤
│ an 900   │  légende : 4 mesures alignées                 │
│  ⬤⬤      │                                               │
└──────────┴──────────────────────────────────────────────┘
```

Alignement : **à gauche**, toujours. Le centrage est réservé à la marque seule (carte sociale, page d'erreur).
Espacement sur l'échelle `--af-space-1..9` ; aucune valeur libre. Angles vifs (`--af-radius-0`) pour les
champs documentaires ; seuls la marque et le favicon ont un rayon.

## 5. Marque

| Asset | Fichier | Emploi |
|---|---|---|
| Marque | [`docs/assets/logo.svg`](../assets/logo.svg) | 64 px et plus |
| Favicon | [`docs/assets/favicon.svg`](../assets/favicon.svg) | 16-32 px, version simplifiée |
| Logotype | [`docs/assets/logo-wordmark.svg`](../assets/logo-wordmark.svg) | en-têtes, presskit |
| Carte sociale | [`docs/assets/social-card.png`](../assets/social-card.png) | 1280×640, aperçu de partage |
| Planche de charte | [`docs/assets/palette.png`](../assets/palette.png) | référence interne, presskit |
| Bannière historique | [`docs/assets/banner.png`](../assets/banner.png) | conservée, remplacée par la carte sociale |

**Construction de la marque :** un carré, quatre bandes égales, un disque par bande dont le rayon double à
chaque strate (1,6 → 3,4 → 5,6 → 8). Le disque n'est pas centré : il est à un tiers, comme une carotte
prélevée hors axe. Zone de protection : la hauteur d'une bande sur les quatre côtés. Taille minimale : 16 px
pour le favicon, 24 px pour la marque, 120 px de large pour le logotype.

**Interdits :** déformer, faire pivoter, changer les couleurs des strates, poser la marque sur une photo,
ajouter une ombre portée, recréer la marque avec d'autres formes.

## 6. Composants documentaires

| Composant | Règle |
|---|---|
| **Bloc de commande** | fond papier creusé, filet 1 px, **liseré gauche de 3 px en rouge de relevé**, chasse fixe. Une commande par bloc |
| **Légende de mesures** | filet supérieur, 2 à 4 colonnes, valeur en gras sur une ligne, libellé en chasse fixe pâle en dessous |
| **Bande d'époque** | fond sédiment + disque + année en chasse fixe alignée à droite |
| **Encart d'avertissement** | liseré gauche rouge de relevé, jamais de fond rouge, jamais d'icône triangulaire |
| **Tableau** | filets horizontaux seulement, en-tête en chasse fixe pâle, pas de zébrures |

## 7. Mouvement

Un seul moment orchestré par écran. Transition d'époque : 900 ms, `cubic-bezier(.22,1,.36,1)`, sur
`background-color` et `color` uniquement. Les entrées de section sont **interdites** par défaut ; le mouvement
répond à une action (ouvrir, défiler volontairement, confirmer). `prefers-reduced-motion: reduce` met toutes
les durées à zéro — c'est déjà dans les jetons, donc gratuit.

## 8. Accessibilité (plancher non négociable)

Contraste AA partout · focus visible au clavier sur tout élément interactif · aucune information portée par
la seule couleur · aucun clignotement au-dessus de 3 Hz · texte redimensionnable jusqu'à 200 % sans perte ·
`lang` correct et commuté avec la langue · cibles tactiles ≥ 44 px · mouvement réduit respecté. Le plancher
s'applique à la landing, au presskit, aux PDF et au HUD.

## 9. Comment s'en servir

```html
<link rel="stylesheet" href="design-system/tokens.css">
<style>
  body { background: var(--af-paper); color: var(--af-ink);
         font: 400 var(--af-step-0)/var(--af-leading-body) var(--af-sans); }
  .mesure { font-family: var(--af-mono); color: var(--af-ink-soft); }
</style>
```

`design-system/tokens.json` expose les mêmes valeurs pour les outils qui ne lisent pas le CSS (générateur de
PDF, Remotion, Figma). Il est **généré** depuis le CSS : on modifie le CSS, jamais le JSON.

## 10. Critères d'acceptation
- [ ] Aucune valeur de couleur, d'espacement ou de typographie en dur hors de `tokens.css`.
- [ ] Contrastes AA vérifiés en clair et en sombre sur les quatre strates.
- [ ] La marque reste lisible à 16 px et en niveaux de gris.
- [ ] Aucune ressource distante : ni police, ni image, ni script.
- [ ] La carte sociale pèse moins de 1 Mo et mesure 1280×640.
- [ ] `prefers-reduced-motion` supprime toute animation sans casser la mise en page.
