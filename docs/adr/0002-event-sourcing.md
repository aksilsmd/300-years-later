# ADR 0002 — Event sourcing comme modèle d'état

- **Statut :** Accepté
- **Date :** 2026-10-07
- **Décideur :** Product Owner

## Contexte
Quatre époques doivent rester identiques sur 4 machines, être rejouables (capsules, musée, débogage) et coûter peu en bande passante (TDD §1-5, GDD §5.2).

## Options envisagées
1. **Réplication d'état** (synchroniser les entités) — simple, mais lourd en réseau, pas de rejouabilité, musée difficile à reconstruire.
2. **Event sourcing** (graine + journal d'actions + recettes pures) — léger, rejouable, un seul format pour réseau/sauvegarde/capsule/musée ; exige un déterminisme strict.

## Décision
Option 2. Toute modification persistante passe par une `ActionEntry` validée par l'hôte ; l'état de chaque époque est recalculé par `Propagator` (fonction pure).

## Conséquences
- Interdits de déterminisme (CLAUDE.md règle 2) ; physique répliquée puis figée (ADR 0004).
- Tests golden et contrôle de hash toutes les 5 s obligatoires.
- Versionnage du format de journal + migrations.
