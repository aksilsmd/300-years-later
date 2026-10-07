# FAQ and troubleshooting

🇫🇷 [Version française](../07_FAQ_DEPANNAGE.md)

**Does the repository contain game images?**
No, on purpose. The game does not exist yet: every image will be rendered in Unreal Engine following `docs/design/33_VISUAL_TARGETS.md` and `data/shotlist.json`, then approved by a human. The diagrams in the repository explain how things work; they do not show the game.

**Does the AI really do everything on its own?**
Almost: installation, code, tests, renders, landing, documents. It only stops where law, licences or your money require it: creating your accounts, installing Unreal from the launcher (Epic login), buying, signing, publishing, approving media, setting the price. It prepares everything so each of these is a few clicks, and keeps other tracks moving meanwhile. A game of this ambition also needs humans (playtesters, a creature artist, a composer, a lawyer).

**Can I add my own instructions?**
Yes: in your message (takes priority) or in `extra_instructions` in `studio.config.yaml`. Only the safety contract cannot be lifted.

**Can the AI make a game on the level of GTA?**
No. Those productions involve hundreds of people and budgets in the hundreds of millions. The kit aims at a very high-quality realistic indie game, with professionals for organic art (creatures, acting, music). See [03_TIME_AND_COST.md](03_TIME_AND_COST.md).

**How much does it cost?**
From ≈ €40,000 (solo + AI) to €500,000+ (small team), excluding the owner's pay. Details in guide 03.

**Can I sell the game I make with this kit?**
Yes (MIT and CC BY 4.0 licences, with attribution). Respect the Unreal EULA, the Fab/MetaHuman licences, and choose your own title.

**The Unreal MCP server does not answer.**
The editor must be open, the Model Context Protocol and AllToolsets plugins enabled, the server started (`ModelContextProtocol.StartServer`), and Git Bash on the `PATH` on Windows.

**Compilation is very slow.**
Exclude project folders from the antivirus (carefully), enable a shared DDC cache, add RAM. Compile in `Development Editor` during development.

**`privacy_scan.py` blocks my commit.**
It found an email, a number, a token, a tracker or a term from your local list. Fix the reported file; do not bypass the check.

**Robot Framework tests fail locally.**
Run `rfbrowser init` once after installation (downloads the test browsers).

**Can I use AI-generated images to go faster?**
The kit forbids it by default: legal risk (rights), player perception, Steam disclosure duty. If you decide otherwise, record it in an ADR and disclose it on Steam and in `legal/17_transparence-ia.md`.
