# 📘 cours_intermediaire.md

Cours Python — Niveau Intermédiaire 🐍

Ce module intermédiaire te permet d’aller plus loin après les bases.  
Tu vas apprendre à mieux structurer ton code, manipuler les listes, gérer les erreurs, et utiliser les modules.

---

1. Les listes

Une liste permet de stocker plusieurs valeurs.

```python
fruits = ["pomme", "banane", "orange"]
print(fruits[0])      # pomme
print(len(fruits))    # 3
```

Ajouter / retirer
```python
fruits.append("kiwi")
fruits.remove("banane")
```

---

2. Les dictionnaires

Un dictionnaire stocke des informations sous forme clé → valeur.

```python
personne = {
    "nom": "Teremu",
    "age": 25
}

print(personne["nom"])
```

---

3. Les boucles avancées

Parcourir une liste
```python
for fruit in fruits:
    print(fruit)
```

Parcourir un dictionnaire
```python
for cle, valeur in personne.items():
    print(cle, valeur)
```

---

4. Les exceptions (gestion des erreurs)

```python
try:
    x = int("abc")
except ValueError:
    print("Erreur : impossible de convertir en nombre.")
```

---

5. Les modules

Un module est un fichier Python que tu peux importer.

Exemple
Créer maths.py :
```python
def addition(a, b):
    return a + b
```

Puis l’utiliser :
```python
import maths

print(maths.addition(3, 5))
```

---

6. Les fichiers (lecture / écriture)

Écrire dans un fichier
```python
with open("notes.txt", "w") as f:
    f.write("Bonjour Python")
```

Lire un fichier
```python
with open("notes.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

---

7. Les fonctions avancées

Valeur de retour
```python
def carre(x):
    return x * x

print(carre(4))
```

Paramètres par défaut
```python
def saluer(nom="inconnu"):
    print("Bonjour", nom)
```

---

Conclusion

Tu maîtrises maintenant les bases intermédiaires de Python : listes, dictionnaires, exceptions, modules et fichiers.  
Tu es prêt pour le niveau avancé.

---
