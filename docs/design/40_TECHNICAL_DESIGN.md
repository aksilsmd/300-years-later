# 40 — Document de conception technique (TDD) — Unreal Engine 5.8
Propriétaire : Product Owner · v2.0 (remplace la v1 Godot — ADR 0012) · **Normatif** pour l'IA. Toute dérogation = ADR.

## 1. Vue d'ensemble
```
┌──────────────────────── Module C++ « TemporalCore » (pur, sans UObject dans le chemin chaud) ───────────────────────┐
│ SeededRng (PCG32) · ActionLog · RecipeDB (JSON data/) · Propagator · ParadoxResolver · ContractEvaluator · Chronicle │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
              ▲ appels purs                                              │ résultats (traces vieillies, paradoxes)
┌─────────────┴──────────── Module « TemporalValley » (gameplay UE) ─────┴──────────────────────────────────────────────┐
│ UTemporalWorldSubsystem (état des 4 époques) · ATemporalGameMode/GameState (hôte autoritaire) · UActionComponent (RPC) │
│ UEraViewSubsystem (vue locale : streaming de l'époque du joueur, spawn des prefabs de traces, fantômes)                │
│ Hazards (StateTree) · Contrats · Musée (Level Instance) · UI (Common UI) · Voix (Online Subsystem Steam VoIP)           │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
Principes conservés de la v1 : **event sourcing**, **déterminisme**, **hôte autoritaire**, **données dans `data/`**, **seule l'époque locale est rendue**.

## 2. Arborescence
```
game/
├─ TemporalValley.uproject
├─ Source/
│  ├─ TemporalCore/        # C++ pur + tests Automation Spec (aucune dépendance Engine dans le cœur)
│  ├─ TemporalValley/      # gameplay, réseau, UI
│  └─ TemporalValleyEditor/# outils d'éditeur, commandes Python, validations
├─ Config/                 # DefaultEngine.ini (OSS Steam, Iris, Lumen), DefaultGame.ini (staging de data/)
├─ Plugins/                # plugins projet (code uniquement dans le dépôt public)
├─ Content/                # ⚠ PRIVÉ (Git LFS/Perforce) — jamais dans le dépôt public (licences Fab/MetaHuman)
├─ Scripts/                # Python d'éditeur (génération PCG, captures, validations)
└─ Tests/Gauntlet/         # tests multi-clients et de charge
```
Le dossier `data/` à la racine est copié dans le build via `DirectoriesToAlwaysStageAsUFS=../data`.

## 3. Modèle de données (C++)
```cpp
// TemporalCore/Public/TemporalTypes.h — types POD, sérialisation canonique
struct FTraceId { uint32 Value; };
struct FTemporalEntity {
  uint32 Id; FName TypeId; uint8 Era; uint32 OriginId; uint8 OriginEra;
  FIntPoint Cell;           // grille 2 m (200×200)
  FIntVector PosCm;         // position quantifiée au cm
  uint8 YawQ;               // 0..255
  TArray<FName> Tags;       // triés
  TSortedMap<FName,int32> Props; // valeurs entières uniquement
  int8 ClaimedByEra = -1; uint32 CreatedTick;
};
struct FActionEntry { uint32 Tick; uint8 Era; uint8 PlayerSlot; uint16 Type; uint32 EntityId; FIntPoint Cell; TArray<uint8,TInlineAllocator<64>> Payload; uint16 Crc16; };
struct FEraState { TSortedMap<uint32,FTemporalEntity> Entities; TArray<uint8> Height; TArray<uint8> Water; TArray<int32> PathWear; uint64 Hash() const; };
```
Format du journal : en-tête `CTLG` + version + graine + mode + nombre de joueurs, puis entrées ; migrations versionnées. Recettes et contrats : JSON validés (`data/schemas/`) chargés au démarrage par `FJsonSerializer`, rejet explicite en cas d'erreur.

## 4. Déterminisme
- Cœur en entiers ; PCG32 avec clés `(graine, usage, id, saut)` ; conteneurs triés ; aucune lecture de la physique, de l'heure ou de `FMath::Rand`.
- La physique Chaos est **répliquée par l'hôte** ; en fin de manche, l'hôte émet une action `FREEZE` par objet dynamique (position quantifiée) — seules ces positions alimentent les recettes.
- Test « golden » : graine 42 + journal de référence → hash attendu des 4 époques (Automation Spec).

## 5. Monde et rendu par époque
- **Une carte World Partition « Valley »** : terrain commun (Landscape), eau (Water plugin).
- **Décor statique par époque** = 4 *Level Instances* (`LI_Era0`…`LI_Era3`) + 4 préréglages d'éclairage. Chargement **local** : le client charge seulement le décor et l'éclairage de son époque.
- **Collision par époque** : quatre canaux d'objet (`Era0`…`Era3`). Le pion d'un joueur en époque *e* ne collisionne qu'avec le canal *e* et le terrain. L'hôte charge la collision des 4 époques (rendu masqué) pour simuler tous les joueurs.
- **Traces** : `UEraViewSubsystem` instancie localement, pour l'époque du joueur, le *prefab* (Packed Level Actor) correspondant à chaque trace de `FEraState` (non répliqué : dérivé du journal). Transition visuelle 0,4 s.
- **Terrain modifiable** (creuser, tranchées) : modifications appliquées en jeu sur une *heightfield* de gameplay (grille 2 m) et rendues par meshes de tranchée/remblai Nanite et decals ; l'eau suit la simulation cellulaire de `TemporalCore` (rendu par Water bodies/spline). Le Landscape lui-même n'est pas modifié à l'exécution.
- **Forêts procédurales** : graphes **PCG** exécutés à l'exécution sur les masques par époque (densité issue de `FEraState`), déterministes (graine PCG = graine du monde).
- **Fantômes** : pions des autres époques rendus localement avec le matériau fantôme, sans collision.

## 6. Réseau
| Sujet | Choix |
|---|---|
| Topologie | listen server, hôte autoritaire ; **pas de migration d'hôte** (capsule de reprise) |
| Réplication | Iris (prête pour la production en 5.8) ; mouvements des pions répliqués normalement |
| Journal | RPC fiables `Server_RequestAction(bytes)` → validation → `Multicast_ApplyAction(bytes)` ; *FastArraySerializer* pour la reprise |
| Sessions & transport | Online Subsystem **Steam** (lobbies amis par défaut, Steam Sockets / relais Valve, invitations) ; build hors Steam : ENet/IpNet en LAN pour le développement |
| Contrôle d'intégrité | hash des 4 époques toutes les 5 s ; resync complète si écart |
| Validation hôte | portée ≤ 2,5 m, cooldowns, inventaire, époque du joueur, taille ≤ 128 o, ≤ 10 actions/s ; kick à 20 rejets/min |
| Texte libre | uniquement `NameStatue` (≤ 16 caractères, filtré) |
| Anti-triche | coop sans enjeu compétitif : validation serveur suffisante ; **Easy Anti-Cheat** (gratuit via Epic Online Services) envisagé si lobbies publics et classements (ADR à prendre) |

## 7. Voix
Steam VoIP via Online Subsystem Steam (données traitées par Valve). Atténuation et filtres inter-époques par *submix* audio (passe-bas / passe-bande selon `data/tuning.json`). **Aucun enregistrement** : test statique (aucune écriture de fichier dans le module voix) + test d'exécution (aucun fichier audio dans `Saved/`).

## 8. Capsules, Chronique, musée
Inchangés sur le fond (v1 §7-8) : capsule `CT1.` = graine + journal persistant compressé (Oodle/zlib) + base64url + CRC32 ; Chronique générée depuis `data/phrases` ; musée = Level Instance `LI_Museum` peuplée de statues (pose figée du squelette MetaHuman + matériau marbre/bronze/néon).

## 9. Mode streamer (opt-in)
Lecture du chat Twitch en IRC anonyme sur WebSocket (module `WebSockets`), en mémoire uniquement ; repli EventSub OAuth ; désactivé par défaut. Vérifier les conditions développeur Twitch avant implémentation.

## 10. Plateformes et performance
| Profil | Matériel de référence | Cible |
|---|---|---|
| Recommandé | RTX 3070 / RX 6800, 8 cœurs, 16 Go | 1440p 60 i/s, Lumen High |
| Minimum | GTX 1660 Super / RX 5600 XT, 6 cœurs, 16 Go | 1080p 30-60 i/s, Lumen Medium, TSR |
| Steam Deck | APU Deck | 800p 30 i/s, Lumen Medium ou GI réduite — « jouable » visé |
Budget CPU hôte : tick logique 20 Hz < 4 ms ; propagation p95 < 2 ms. Réseau : < 30 ko/s/joueur. Profilage : Unreal Insights, `csvprofile`, `stat unit`, `memreport`.

## 11. Tests
| Niveau | Outil | Commande type (Windows) |
|---|---|---|
| Unitaire cœur | Automation Spec | `UnrealEditor-Cmd.exe TemporalValley.uproject -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -nosplash -log` |
| Fonctionnel | Functional Tests (cartes de test) | `-ExecCmds="Automation RunTests Project.Functional"` |
| Multi-clients / charge | Gauntlet | `RunUAT.bat RunUnreal -project=... -test=TemporalValley.LoadTest -clients=3 -build=...` |
| Perf | Insights / CSV | traces archivées par build |
| Données | `python3 tools/validate_data.py` | — |
| Sécurité / confidentialité | gitleaks, semgrep, `tools/privacy_scan.py` | — |

## 12. Build, CI, gestion de source
- **Code + conception + données** : dépôt Git (public possible).
- **Contenu binaire** (`Content/`, assets Fab, MetaHumans) : dépôt **privé** Git LFS ou Perforce Helix Core ; jamais public.
- CI : runner **Windows auto-hébergé** (VS 2022, UE 5.8 installé) ; `RunUAT BuildCookRun -platform=Win64 -clientconfig=Shipping -build -cook -stage -pak -archive` ; cache DDC partagé.
- Branches Steam : `default`, `beta`, `demo`, `qa`. Versionnage sémantique.

## 13. Dépendances (versions dans `docs/DEPENDENCIES.md`)
UE 5.8, Visual Studio 2022 (charges « Développement Desktop C++ » + « Développement de jeux C++ ») ou JetBrains Rider, .NET 8 SDK, Windows SDK, Python 3.11+ (éditeur UE intégré), Git LFS, Blender 4.5 LTS, plugin officiel Epic pour Claude Code (MCP), plugins moteur : PCG, Water, MetaHuman, Online Subsystem Steam, Movie Render Queue / Movie Render Graph, Common UI, StateTree, Motion Matching (Pose Search), Model Context Protocol.

## 14. ADR à rédiger en phase 0
0013 Structure des modules C++ · 0014 Level Instances par époque et canaux de collision · 0015 Terrain de gameplay vs Landscape · 0016 PCG d'exécution déterministe · 0017 OSS Steam vs EOS · 0018 Dépôt de contenu privé · 0019 Iris · 0020 Anti-triche (oui/non).
