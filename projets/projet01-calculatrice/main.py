🐍 projet01-calculatrice/main.py

`python

!/usr/bin/env python3
"""
Projet 01 — Calculatrice Python
PYTHON-Learning — Teremu
"""

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par zéro interdite.")
    return a / b

def demander_nombre(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Entrée invalide. Merci de saisir un nombre.")

def demander_operation():
    print("\nChoisissez une opération :")
    print("[+] Addition")
    print("[-] Soustraction")
    print("[*] Multiplication")
    print("[/] Division")
    op = input("Opération (+, -, *, /) : ").strip()
    if op not in ["+", "-", "*", "/"]:
        print("Opération inconnue.")
        return None
    return op

def calculatrice():
    print("=== Calculatrice Python — PYTHON-Learning ===")

    while True:
        op = demander_operation()
        if op is None:
            continue

        a = demander_nombre("Premier nombre : ")
        b = demander_nombre("Deuxième nombre : ")

        try:
            if op == "+":
                resultat = addition(a, b)
            elif op == "-":
                resultat = soustraction(a, b)
            elif op == "*":
                resultat = multiplication(a, b)
            elif op == "/":
                resultat = division(a, b)
            else:
                print("Opération non gérée.")
                continue

            print(f"Résultat : {resultat}")
        except ZeroDivisionError as e:
            print("Erreur :", e)

        continuer = input("\nVoulez-vous continuer ? (o/n) : ").strip().lower()
        if continuer != "o":
            print("Fin de la calculatrice. Merci d'avoir utilisé PYTHON-Learning.")
            break

if name == "main":
    calculatrice()
`
