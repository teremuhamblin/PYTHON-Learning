# 📘 cours_avancé.md

`markdown

Cours Python — Niveau Avancé 🚀

Ce module avancé te donne les outils pour écrire du code professionnel : classes, programmation orientée objet, modules standards, compréhension de listes, et gestion avancée des données.

---

1. Programmation orientée objet (POO)

La POO permet de créer des objets avec des propriétés et des comportements.

Exemple simple
```python
class Personne:
    def init(self, nom, age):
        self.nom = nom
        self.age = age

    def saluer(self):
        print("Bonjour, je suis", self.nom)

p = Personne("Teremu", 25)
p.saluer()
```

---

2. Héritage

L’héritage permet de créer une classe à partir d’une autre.

```python
class Animal:
    def parler(self):
        print("Je suis un animal.")

class Chien(Animal):
    def parler(self):
        print("Ouaf !")

c = Chien()
c.parler()
```

---

3. Compréhensions de listes

Une manière rapide de créer des listes.

```python
carres = [x*x for x in range(10)]
print(carres)
```

---

4. Fonctions lambda

Des fonctions anonymes, très courtes.

```python
double = lambda x: x * 2
print(double(5))
```

---

5. Le module os

Manipuler le système de fichiers.

```python
import os

print(os.listdir("."))   # liste les fichiers du dossier
```

---

6. Le module json

Lire et écrire des données structurées.

```python
import json

data = {"nom": "Teremu", "age": 25}

écrire
with open("data.json", "w") as f:
    json.dump(data, f)

lire
with open("data.json", "r") as f:
    contenu = json.load(f)
    print(contenu)
```

---

7. Les générateurs

Produire des valeurs une par une.

```python
def compteur():
    for i in range(5):
        yield i

for nombre in compteur():
    print(nombre)
```

---

8. Les décorateurs

Modifier le comportement d’une fonction.

```python
def decorateur(f):
    def wrapper():
        print("Début")
        f()
        print("Fin")
    return wrapper

@decorateur
def dire_bonjour():
    print("Bonjour")

dire_bonjour()
```

---

9. Les context managers

Gérer automatiquement l’ouverture et la fermeture de ressources.

```python
with open("test.txt", "w") as f:
    f.write("Hello")
```

---

Conclusion

Tu maîtrises maintenant les concepts avancés de Python : POO, héritage, décorateurs, générateurs, JSON, OS, et compréhension de listes.  
Tu es prêt à créer des projets complets et professionnels.

---
