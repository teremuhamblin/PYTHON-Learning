# 📘 cours_expert.md

Cours Python — Niveau Expert ⚡

Ce module expert te donne les compétences nécessaires pour développer des applications Python professionnelles, robustes, performantes et maintenables.  
Il couvre l’architecture, les design patterns, l’asynchronisme, les tests, la sécurité, l’optimisation et les bonnes pratiques avancées.

---

1. Architecture d’un projet Python

Un projet expert doit être organisé clairement.

Structure recommandée
```text
mon_projet/
│── src/
│   ├── modules/
│   ├── utils/
│   └── main.py
│── tests/
│── requirements.txt
│── config.yaml
│── README.md
```

Principes clés
- Séparer le code en modules
- Utiliser un dossier tests/
- Externaliser la configuration (.env, YAML, JSON)
- Documenter chaque module

---

2. Programmation orientée objet avancée

Classes abstraites
```python
from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def rouler(self):
        pass
```

Polymorphisme
```python
class Voiture(Vehicule):
    def rouler(self):
        print("La voiture roule.")

class Moto(Vehicule):
    def rouler(self):
        print("La moto roule.")
```

Propriétés
```python
class Personne:
    def init(self, nom):
        self._nom = nom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        self._nom = valeur
```

---

3. Design Patterns essentiels

Singleton
```python
class Singleton:
    _instance = None

    def new(cls):
        if cls._instance is None:
            cls.instance = super().new_(cls)
        return cls._instance
```

Factory
```python
class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Ouaf"

class Chat(Animal):
    def parler(self):
        return "Miaou"

def animal_factory(type):
    if type == "chien":
        return Chien()
    if type == "chat":
        return Chat()
```

Observer
```python
class Sujet:
    def init(self):
        self.observateurs = []

    def ajouter(self, obs):
        self.observateurs.append(obs)

    def notifier(self):
        for obs in self.observateurs:
            obs.update()
```

---

4. Programmation asynchrone (async / await)

L’asynchronisme permet d’exécuter plusieurs tâches sans bloquer le programme.

```python
import asyncio

async def tache():
    print("Début")
    await asyncio.sleep(1)
    print("Fin")

asyncio.run(tache())
```

Plusieurs tâches en parallèle
```python
async def travail(n):
    await asyncio.sleep(1)
    print("Tâche", n)

asyncio.run(asyncio.gather(travail(1), travail(2), travail(3)))
```

---

5. Gestion avancée des données

JSON
```python
import json
data = json.loads('{"nom": "Teremu"}')
```

YAML
```python
import yaml
config = yaml.safe_load(open("config.yaml"))
```

SQLite
```python
import sqlite3

conn = sqlite3.connect("base.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
```

---

6. Tests unitaires et automatisation

Test simple
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

if name == "main":
    unittest.main()
```

Pytest (recommandé)
```python
def test_carres():
    assert 3*3 == 9
```

---

7. Sécurité en Python

Ne jamais stocker des secrets dans le code
Utiliser .env :
```env
API_KEY=123456
```

Puis :
```python
from dotenv import load_dotenv
import os

load_dotenv()
cle = os.getenv("API_KEY")
```

Validation des données
```python
def valider_age(age):
    if not isinstance(age, int):
        raise TypeError("Age doit être un entier.")
```

Protection des fichiers
- Utiliser with open(...)
- Vérifier les chemins (os.path.abspath)
- Éviter les injections dans les commandes système

---

8. Optimisation et performance

Profiling
```python
import cProfile
cProfile.run("sum(range(100000))")
```

LRU Cache
```python
from functools import lru_cache

@lru_cache
def calcul(x):
    return x * x
```

Multiprocessing
```python
from multiprocessing import Pool

def carre(x):
    return x*x

with Pool() as p:
    print(p.map(carre, [1,2,3,4]))
```

---

9. Bonnes pratiques professionnelles

- Respecter PEP8
- Nommer clairement les variables
- Documenter chaque fonction
- Tester chaque module
- Séparer logique / interface / données
- Utiliser des environnements virtuels (venv)
- Versionner le code (Git)
- Écrire un README clair
- Utiliser des exceptions personnalisées

---

Conclusion

Tu maîtrises maintenant les concepts experts de Python :  
architecture, POO avancée, design patterns, asynchronisme, tests, sécurité, optimisation et bonnes pratiques professionnelles.

Tu es prêt à développer des applications Python complètes, fiables et de niveau professionnel.

---
