import sys

# Liste des choix possibles
choices = ['Ajouter une tâche à la liste', 'Retirer une tâche de la liste', 'Afficher les éléments de la liste de tâches', 'Vider la liste de tâches', 'Quitter le programme']
tasks = []

while True:
    # Affichage des choix possibles
    for index, choice in enumerate(choices, start=1):
        print(f'{index} - {choice}')

    # Demande de choix à l'utilisateur
    choice = input('Choisissez l\'action à effectuer : ')

    # Vérification de la validité du choix
    if not choice.isdigit() or not 1 <= int(choice) <= len(choices):
        print(f'Merci de sélectionner un nombre entre 1 et {len(choices)}')
        continue

    # Conversion du choix en entier
    choice = int(choice)

    # Ajout d'une tâche
    if choice == 1:
        new_task = input('Nouvelle tâche : ')
        tasks.append(new_task)

    # Retrait d'une tâche
    elif choice == 2:
        if len(tasks) == 0:
            print('La liste de tâches est vide.')
        else:
            print('Voici la liste des tâches :')
            for index, task in enumerate(tasks, start=1):
                print(f'{index} - {task}')
            task_to_delete = input('Entrez le numéro de la tâche à supprimer : ')
            if not task_to_delete.isdigit() or not 1 <= int(task_to_delete) <= len(tasks):
                print('Numéro de tâche invalide.')
            else:
                task_index = int(task_to_delete) - 1
                deleted_task = tasks.pop(task_index)
                print(f'La tâche "{deleted_task}" a été supprimée.')

    # Affichage des tâches
    elif choice == 3:
        if len(tasks) == 0:
            print('La liste de tâches est vide.')
        else:
            print('Voici la liste des tâches :')
            for index, task in enumerate(tasks, start=1):
                print(f'{index} - {task}')

    # Vider la liste de tâches
    elif choice == 4:
        if len(tasks) == 0:
            print('La liste de tâches est déjà vide.')
        else:
            tasks.clear()
            print('La liste de tâches a été vidée.')

    # Quitter le programme
    elif choice == 5:
        print('Au revoir !')
        sys.exit()

    print()  # Ligne vide pour séparer les actions

