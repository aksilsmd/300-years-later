// Tout le texte de la page, en français et en anglais. Les textes publics sont validés par l'humain.
export type Lang = "fr" | "en";

export const ERA_NAMES: Record<Lang, [string, string, string, string]> = {
  fr: ["L'Aube", "Les Bannières", "La Vapeur", "Le Néon"],
  en: ["The Dawn", "The Banners", "The Steam", "The Neon"],
};

// Lien Steam : à renseigner à l'ouverture de la page Steam (null = bouton désactivé avec explication)
export const STEAM_URL: string | null = null;

export type Content = {
  skip: string; ctaShort: string; yearPrefix: string; heroLine: string; heroSub: string; cta: string; howLink: string;
  strataTitle: string; layers: { year: string; title: string; text: string }[];
  coopTitle: string; coop: string[];
  ledgerTitle: string; ledgerHead: string[]; ledger: [string, string, string, string][]; ledgerNote: string;
  museumQuote: string; museumBy: string; museumText: string; galleryTitle: string;
  eraSeqTitle: string; eraSeqHint: string; renderedLabel: string; pause: string; play: string;
  modesTitle: string; modes: [string, string][]; faqTitle: string; faq: [string, string][];
  finalTitle: string; steamNote: string; foot1: string; footLinks: [string, string][]; foot2: string;
};

export const CONTENT: Record<Lang, Content> = {
  fr: {
    skip: "Aller au contenu",
    ctaShort: "Liste de souhaits",
    yearPrefix: "an",
    heroLine: "Tu plantes une graine. Ton ami la retrouve trois cents ans plus tard, devenue chêne.",
    heroSub:
      "Un jeu coopératif pour 1 à 4 joueurs. Chacun vit dans un siècle différent de la même vallée, et tout ce que vous laissez derrière vous vieillit sous les yeux des autres.",
    cta: "Ajouter à ma liste de souhaits",
    howLink: "Comment ça marche",
    strataTitle: "La règle tient en une phrase : tout ce que tu laisses vieillit.",
    layers: [
      { year: "an 0", title: "L'Aube", text: "Tu creuses, tu plantes une graine au bord de la rivière. Un mammouth curieux la renifle." },
      { year: "an 300", title: "Les Bannières", text: "Ta graine est un chêne. Le bourg a construit son marché dessous. Ton amie y attache une balançoire." },
      { year: "an 600", title: "La Vapeur", text: "Le chêne est géant. L'usine voisine l'a épargné, on ne sait pas pourquoi. Les ouvriers déjeunent à son ombre." },
      { year: "an 900", title: "Le Néon", text: "C'est l'Arbre millénaire, couvert de lanternes. Le musée raconte, très sérieusement, que tu l'as planté « pour faire de l'ombre à personne »." },
    ],
    coopTitle: "Quatre amis, quatre siècles, une vallée",
    coop: [
      "Vous jouez au même endroit, mais pas à la même époque. Tu vois tes amis comme des silhouettes translucides et tu les entends de plus en plus étouffés à mesure que vous vous éloignez.",
      "Un client exigeant du futur vous confie un contrat : un pont rouge au-dessus d'un canyon qui n'existe pas encore, une statue de canard vénérée, un troupeau légendaire.",
      "Entre deux manches, les siècles défilent et chacun avance d'une époque. Tu hérites de ce que les autres t'ont laissé. Bonne chance.",
    ],
    ledgerTitle: "Ce que le temps fait de vos bêtises",
    ledgerHead: ["Tu laisses…", "+300 ans", "+600 ans", "+900 ans"],
    ledger: [
      ["trois pierres empilées", "un cairn", "un monument vénéré", "un site touristique avec boutique"],
      ["une tranchée près de l'eau", "un ruisseau", "une rivière", "un canyon"],
      ["un barrage de branches", "un étang", "un lac", "une station balnéaire"],
      ["ta pose sur un socle", "ta statue", "une légende locale", "ta statue géante, en néon"],
      ["deux mammouths ensemble", "un troupeau", "une race domestiquée", "la mascotte de la ville"],
      ["un objet venu du futur", "un fan-club", "un fan-club géant", "un paradoxe"],
    ],
    ledgerNote: "Si le futur contredit le passé, le temps se fissure et les Chronomites arrivent. Elles ont faim.",
    museumQuote: "« La Statue du Canard. Datée de l'an 0. Les historiens s'accordent : Lou faisait ça tout le temps. »",
    museumBy: "ARCHIVE, guide du Musée de Tout, à la fin de chaque partie",
    museumText: "Chaque partie se termine par la visite d'un musée construit à partir de ce que vous avez fait. Il est toujours faux, et c'est le meilleur moment de la soirée.",
    galleryTitle: "Images du jeu",
    eraSeqTitle: "La même colline, quatre siècles",
    eraSeqHint: "Fais défiler : le temps passe.",
    renderedLabel: "Rendu dans le moteur du jeu",
    pause: "Mettre la vidéo en pause",
    play: "Lire la vidéo",
    modesTitle: "Façons de jouer",
    modes: [
      ["Contrat, de 2 à 4 joueurs", "Le cœur du jeu : trois manches, une rotation des époques, un musée."],
      ["Relais, en solo", "Tu joues l'an 0, puis tu hérites de toi-même en l'an 300. « Pourquoi j'ai mis ça là ? »"],
      ["Capsule, en différé", "Tu joues le passé, tu envoies un code, ton ami joue le futur quand il veut."],
      ["Saboteur du temps", "L'un de vous veut faire s'effondrer l'histoire. Démasquez-le à la pause café."],
      ["Spectateurs du temps", "En stream, le chat vote les catastrophes et baptise les statues."],
    ],
    faqTitle: "Questions fréquentes",
    faq: [
      ["Quand sort le jeu ?", "Il est en développement. Ajoute-le à ta liste de souhaits pour être prévenu de la démo."],
      ["Faut-il un micro ?", "Non. Les pings, les emotes et les phrases rapides suffisent pour jouer ensemble."],
      ["Y a-t-il des achats dans le jeu ?", "Non : pas de loot box, pas de monnaie payante, pas de publicité."],
      ["Puis-je streamer et monétiser mes vidéos ?", "Oui, librement. La musique est sans réclamation de droits d'auteur."],
      ["Où sont les images du jeu ?", "Elles arriveront avec la démo. Nous ne montrerons que des images réellement issues du jeu."],
    ],
    finalTitle: "Rendez-vous dans trois cents ans. Ou à la démo.",
    steamNote: "Le lien vers la page Steam sera ajouté à son ouverture.",
    foot1: "Aucun cookie, aucun traceur sur ce site.",
    footLinks: [["legal/mentions-legales.html", "Mentions légales"], ["legal/confidentialite.html", "Confidentialité"], ["legal/presse.html", "Presse et créateurs"]],
    foot2: "Titre de travail. Unreal est une marque d'Epic Games, Inc. Steam est une marque de Valve Corporation.",
  },
  en: {
    skip: "Skip to content",
    ctaShort: "Wishlist",
    yearPrefix: "year",
    heroLine: "You plant a seed. Three hundred years later, your friend finds an oak.",
    heroSub:
      "A co-op game for 1 to 4 players. Each of you lives in a different century of the same valley, and everything you leave behind ages in front of the others.",
    cta: "Add to my wishlist",
    howLink: "How it works",
    strataTitle: "The rule fits in one sentence: everything you leave behind ages.",
    layers: [
      { year: "year 0", title: "The Dawn", text: "You dig and plant a seed by the river. A curious mammoth sniffs it." },
      { year: "year 300", title: "The Banners", text: "Your seed is an oak. The town built its market beneath it. Your friend hangs a swing from it." },
      { year: "year 600", title: "The Steam", text: "The oak is a giant. The factory next door spared it, nobody knows why. Workers eat lunch in its shade." },
      { year: "year 900", title: "The Neon", text: "It is the Thousand-Year Tree, covered in lanterns. The museum explains, very seriously, that you planted it \"to shade no one at all\"." },
    ],
    coopTitle: "Four friends, four centuries, one valley",
    coop: [
      "You play in the same place, but not in the same era. You see your friends as translucent silhouettes, and their voices grow muffled as you drift apart.",
      "A demanding client from the future hands you a contract: a red bridge over a canyon that doesn't exist yet, a revered duck statue, a legendary herd.",
      "Between rounds, the centuries roll by and everyone moves up one era. You inherit what the others left you. Good luck.",
    ],
    ledgerTitle: "What time does to your mistakes",
    ledgerHead: ["You leave…", "+300 years", "+600 years", "+900 years"],
    ledger: [
      ["three stacked stones", "a cairn", "a revered monument", "a tourist site with a gift shop"],
      ["a trench near water", "a brook", "a river", "a canyon"],
      ["a stick dam", "a pond", "a lake", "a seaside resort"],
      ["your pose on a plinth", "your statue", "a local legend", "your giant neon statue"],
      ["two mammoths together", "a herd", "a domesticated breed", "the town mascot"],
      ["an object from the future", "a fan club", "a giant fan club", "a paradox"],
    ],
    ledgerNote: "If the future contradicts the past, time cracks and the Chronomites arrive. They are hungry.",
    museumQuote: "\"The Statue of the Duck. Dated year 0. Historians agree: Lou did this all the time.\"",
    museumBy: "ARCHIVE, guide of the Museum of Everything, at the end of every game",
    museumText: "Every game ends with a tour of a museum built from what you did. It is always wrong, and it is the best moment of the night.",
    galleryTitle: "Game images",
    eraSeqTitle: "The same hill, four centuries",
    eraSeqHint: "Scroll: time passes.",
    renderedLabel: "Rendered in the game engine",
    pause: "Pause video",
    play: "Play video",
    modesTitle: "Ways to play",
    modes: [
      ["Contract, 2 to 4 players", "The core game: three rounds, rotating eras, one museum."],
      ["Relay, solo", "You play year 0, then inherit from yourself in year 300. \"Why did I put that there?\""],
      ["Capsule, asynchronous", "You play the past, send a code, and your friend plays the future whenever they like."],
      ["Time Saboteur", "One of you wants history to collapse. Unmask them at the coffee break."],
      ["Time Spectators", "On stream, chat votes for disasters and names the statues."],
    ],
    faqTitle: "Frequently asked questions",
    faq: [
      ["When does the game come out?", "It is in development. Wishlist it to hear about the demo."],
      ["Do I need a microphone?", "No. Pings, emotes and quick phrases are enough to play together."],
      ["Are there in-game purchases?", "No loot boxes, no paid currency, no ads."],
      ["Can I stream and monetise videos?", "Yes, freely. The music won't trigger copyright claims."],
      ["Where are the screenshots?", "They will arrive with the demo. We will only show images that genuinely come from the game."],
    ],
    finalTitle: "See you in three hundred years. Or at the demo.",
    steamNote: "The Steam page link will be added when it opens.",
    foot1: "No cookies, no trackers on this site.",
    footLinks: [["legal/mentions-legales.html", "Legal notice"], ["legal/confidentialite.html", "Privacy"], ["legal/presse.html", "Press and creators"]],
    foot2: "Working title. Unreal is a trademark of Epic Games, Inc. Steam is a trademark of Valve Corporation.",
  },
};
