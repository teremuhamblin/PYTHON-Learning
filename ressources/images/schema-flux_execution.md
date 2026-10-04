📄 schema-flux_execution.md

`markdown

Schéma — Flux d'exécution d'un programme Python

```text
        ┌──────────────────────────┐
        │   Début du programme     │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Lecture du code        │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Exécution ligne par ligne
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Appels de fonctions    │
        └──────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │   Fin du programme       │
        └──────────────────────────┘
```

---
