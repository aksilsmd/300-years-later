// 300 Years Later — landing de référence. Aucun appel réseau, aucun stockage, aucun traceur.
(() => {
  const root = document.documentElement;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const yearEl = document.getElementById("year-num");
  const eraEl = document.getElementById("era-name");

  const ERAS = {
    fr: ["L'Aube", "Les Bannières", "La Vapeur", "Le Néon"],
    en: ["The Dawn", "The Banners", "The Steam", "The Neon"],
  };
  let lang = "fr";

  const EN = {
    skip: "Skip to content", ctaShort: "Wishlist", yearPrefix: "year",
    heroLine: "You plant a seed. Three hundred years later, your friend finds an oak.",
    heroSub: "A co-op game for 1 to 4 players. Each of you lives in a different century of the same valley, and everything you leave behind ages in front of the others.",
    cta: "Add to my wishlist", howLink: "How it works",
    strataTitle: "The rule fits in one sentence: everything you leave behind ages.",
    l0t: "The Dawn", l0p: "You dig and plant a seed by the river. A curious mammoth sniffs it.",
    l1t: "The Banners", l1p: "Your seed is an oak. The town built its market beneath it. Your friend hangs a swing from it.",
    l2t: "The Steam", l2p: "The oak is a giant. The factory next door spared it, nobody knows why. Workers eat lunch in its shade.",
    l3t: "The Neon", l3p: "It is the Thousand-Year Tree, covered in lanterns. The museum explains, very seriously, that you planted it \"to shade no one at all\".",
    coopTitle: "Four friends, four centuries, one valley",
    coop1: "You play in the same place, but not in the same era. You see your friends as translucent silhouettes, and their voices grow muffled as you drift apart.",
    coop2: "A demanding client from the future hands you a contract: a red bridge over a canyon that doesn't exist yet, a revered duck statue, a legendary herd. Organise yourselves across time.",
    coop3: "Between rounds, the centuries roll by and everyone moves up one era. You inherit what the others left you. Good luck.",
    ledgerTitle: "What time does to your mistakes", colAction: "You leave…",
    r1a: "three stacked stones", r1b: "a cairn", r1c: "a revered monument", r1d: "a tourist site with a gift shop",
    r2a: "a trench near water", r2b: "a brook", r2c: "a river", r2d: "a canyon",
    r3a: "a stick dam", r3b: "a pond", r3c: "a lake", r3d: "a seaside resort",
    r4a: "your pose on a plinth", r4b: "your statue", r4c: "a local legend", r4d: "your giant neon statue",
    r5a: "two mammoths together", r5b: "a herd", r5c: "a domesticated breed", r5d: "the town mascot",
    r6a: "an object from the future", r6b: "a fan club", r6c: "a giant fan club", r6d: "a paradox",
    ledgerNote: "If the future contradicts the past, time cracks and the Chronomites arrive. They are hungry.",
    museumTitle: "The end-of-game museum",
    museumQuote: "\"The Statue of the Duck. Dated year 0. Historians agree: Lou did this all the time.\"",
    museumBy: "ARCHIVE, guide of the Museum of Everything, at the end of every game",
    museumText: "Every game ends with a tour of a museum built from what you did. It is always wrong, and it is the best moment of the night.",
    modesTitle: "Ways to play",
    m1t: "Contract, 2 to 4 players", m1d: "The core game: three rounds, rotating eras, one museum.",
    m2t: "Relay, solo", m2d: "You play year 0, then inherit from yourself in year 300. \"Why did I put that there?\"",
    m3t: "Capsule, asynchronous", m3d: "You play the past, send a code, and your friend plays the future whenever they like.",
    m4t: "Time Saboteur", m4d: "One of you wants history to collapse. Unmask them at the coffee break.",
    m5t: "Time Spectators", m5d: "On stream, chat votes for disasters and names the statues.",
    faqTitle: "Frequently asked questions",
    q1: "When does the game come out?", a1: "It is in development. Wishlist it to hear about the demo.",
    q2: "Do I need a microphone?", a2: "No. Pings, emotes and quick phrases are enough to play together.",
    q3: "Are there in-game purchases?", a3: "No loot boxes, no paid currency, no ads.",
    q4: "Can I stream and monetise videos?", a4: "Yes, freely. The music won't trigger copyright claims.",
    q5: "Where are the screenshots?", a5: "They will arrive with the demo. We will only show images that genuinely come from the game.",
    finalTitle: "See you in three hundred years. Or at the demo.",
    steamNote: "The Steam page link will be added when it opens.",
    foot1: "No cookies, no trackers on this site.", fl1: "Legal notice", fl2: "Privacy", fl3: "Press and creators",
    foot2: "Working title. Unreal is a trademark of Epic Games, Inc. Steam is a trademark of Valve Corporation.",
  };
  const FR = {};
  document.querySelectorAll("[data-i18n]").forEach((el) => { FR[el.dataset.i18n] = el.textContent; });

  function setLang(l) {
    lang = l;
    root.lang = l;
    const dict = l === "en" ? EN : FR;
    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const v = dict[el.dataset.i18n];
      if (v) el.textContent = v;
    });
    document.querySelectorAll(".lang button").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.lang === l)));
    setEra(Number(root.dataset.era || 0), false);
  }
  document.querySelectorAll(".lang button").forEach((b) => b.addEventListener("click", () => setLang(b.dataset.lang)));

  function setEra(i, withYear = true) {
    root.dataset.era = String(i);
    eraEl.textContent = ERAS[lang][i];
    if (withYear) yearEl.textContent = String(i * 300);
  }

  // Moment orchestré unique : au chargement, les siècles défilent (0 → 900) puis reviennent à l'an 0.
  function countTo(target, ms) {
    return new Promise((resolve) => {
      const start = Number(yearEl.textContent) || 0;
      const t0 = performance.now();
      function tick(now) {
        const k = Math.min(1, (now - t0) / ms);
        const e = 1 - Math.pow(1 - k, 3);
        yearEl.textContent = String(Math.round(start + (target - start) * e));
        if (k < 1) requestAnimationFrame(tick); else resolve();
      }
      requestAnimationFrame(tick);
    });
  }
  async function intro() {
    if (reduce) { setEra(0); return; }
    await new Promise((r) => setTimeout(r, 700));
    for (let i = 1; i <= 3; i++) {
      root.dataset.era = String(i); eraEl.textContent = ERAS[lang][i];
      await countTo(i * 300, 900);
      await new Promise((r) => setTimeout(r, 450));
    }
    await new Promise((r) => setTimeout(r, 900));
    root.dataset.era = "0"; eraEl.textContent = ERAS[lang][0];
    await countTo(0, 1100);
  }

  // En faisant défiler les strates, la page prend la couleur de l'époque lue (action de l'utilisateur).
  const layers = document.querySelectorAll(".layer");
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) setEra(Number(en.target.dataset.era), false); });
  }, { rootMargin: "-45% 0px -45% 0px" });
  layers.forEach((l) => io.observe(l));
  const hero = document.querySelector(".hero");
  new IntersectionObserver((e) => { if (e[0].isIntersecting && !introRunning) setEra(0, false); }, { threshold: .6 }).observe(hero);

  let introRunning = true;
  intro().finally(() => { introRunning = false; });
})();
