📄 ARCHITECTURE.md

`markdown

ARCHITECTURE.md — Architecture interne du projet PYTHON-Learning

Ce document décrit l’architecture interne du projet, les conventions de code, l’organisation des modules Python et les bonnes pratiques à respecter.

---

🧱 Architecture générale

Le projet n’est pas un package Python, mais un environnement éducatif structuré.  
Chaque dossier a un rôle pédagogique précis.

---

📁 Organisation interne

cours/
- Fichiers Markdown
- Pas de code exécutable
- Contenu théorique

exercices/
- Code Python simple
- Un fichier = un exercice
- Pas de dépendances externes

projets/
- Code Python structuré
- Un dossier = un projet
- Peut contenir plusieurs fichiers .py

ressources/
- Aucun code
- Documents, images, fiches mémo

docs/
- Documentation interne
- Guides techniques

---

🧩 Architecture des projets Python

Chaque projet doit suivre cette structure :

`
projet_X/
│── README.md
│── main.py
│── modules/ (optionnel)
│── data/ (optionnel)
`

---

🧭 Conventions de code

- Noms de fichiers en minuscules  
- Noms de variables explicites  
- Fonctions courtes et claires  
- Commentaires pédagogiques  
- Respect de PEP8 (voir PYTHON_STANDARDS.md)

---

🔧 Modules Python

Les projets peuvent utiliser :

- os
- json
- random
- time
- typing

Les modules avancés (FastAPI, asyncio, sqlite3) sont réservés aux projets experts.

---

📬 Contact

Projet créé par Teremu — PYTHON-Learning
`

---
