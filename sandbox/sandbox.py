ram = []

def tout():
    choix = input("Entre un nom d'insecte: ")

    if choix in insectes:
        price = insectes[choix]

    else:
        while choix not in insectes:
            try:
                choix = input("Entre un nom d'insecte correct")
                if choix in insectes:
                    price = insectes[choix]
                    break
            except ValueError:
                print("Cet insecte n'existe pas")

    price_write = price + "Cl"

    print(price, "Cl")

    quitter = input("Continuer Exit Save; ou combine")
    if quitter == "Exit":
        print("Vous allez quitter le programme")
        exit()
    elif quitter == "Save":
        save()
        print("La sauvegarde a bien été effectué")
        exit()
    elif quitter == "Continuer":
        tout()
    elif quitter == "Reset_save":
        reset_save()
        print("La sauvegarde a bien été supprimé")
    elif quitter == "Reset_dep_save":
        reset_dep_save()
        print("La sauvegarde a bien été supprimé")
    elif quitter == "Reset":
        reset_all()
        print("La sauvegarde a bien été supprimé")
    elif quitter == "Save+Continuer":
        save()
        print("La sauvegarde a bien été effectué")
        tout()
    elif quitter != "Exit" "Save" "Reset" "Reset_save" "Reset_dep_save" "Save+Continuer" "Save+Quitter":

        while quitter != "Save" "Quitter" "Reset_save" "Reset_dep_save" "Reset":
            try:
                quitter = input("'Exit' pour quitter, 'Save' pour sauvegarder et quitter, 'Reset' pour reset la save")
                if quitter == "Exit":
                    print("Vous allez quitter le programme")
                    exit()
                elif quitter == "Save":
                    save()
                    print("La sauvegarde a bien été effectué")
                    exit()
                elif quitter == "Continuer":
                    tout()
                elif quitter == "Reset_save":
                    reset_save()
                    print("La sauvegarde a bien été supprimé")
                elif quitter == "Reset_dep_save":
                    reset_dep_save()
                    print("La sauvegarde a bien été supprimé")
                elif quitter == "Reset":
                    reset_all()
                    print("La sauvegarde a bien été supprimé")
                elif quitter == "Save+Continuer":
                    save()
                    print("La sauvegarde a bien été effectué")
                    tout()
                elif quitter != "Exit" "Save" "Reset":
                    print("Entre une des options")
            except ValueError:
                print("Entre une des options")