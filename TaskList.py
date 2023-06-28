import sys
import os
import json

# PWD du fichier
CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")


# Liste des choix possibles
MENU = """Choisissez une option parmi les 5 suivantes :
1: Ajouter une tâche à la liste
2: Retirer une tâche de la liste
3: Afficher votre liste de tâches
4: Vider la liste de tâches
5: Quitter le programme
? Votre choix : """

# Choix utilisateur
MENU_CHOICES = ['1', '2', '3', '4', '5']

# Récupération du JSON si no JSON on crée une liste
if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []

while True:
    # Validation du choix
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    # Différents cas 
    if user_choice == "1":  # Ajouter un élément
            item = input("Entrez le nom d'une tâche à ajouter à la liste : ")
            LISTE.append(item)
            print(f"La tâche '{item}' a bien été ajouté à la liste.")

    elif user_choice == "2":  # Retirer un élément
            item = input("Entrez le nom d'une tâche à retirer de la liste : ")
            if item in LISTE:
                LISTE.remove(item)
                print(f"La tâche '{item}' a bien été supprimée de la liste.")
            else:
                print(f"La tâche '{item}' n'est pas dans la liste.")

    elif user_choice == "3":  # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucune tâche.")

    elif user_choice == "4":  # Vider la liste
        LISTE.clear()
        print("La liste de tâches a été vidée de son contenu.")

    elif user_choice == "5":  # Sauvegarder et quitter
        with open(LISTE_PATH, "w") as f:
            json.dump(LISTE, f, indent=4)
        print("À bientôt !")
        sys.exit()

    print("-" * 50)
    