from stock_var import*
from stock_list import*

total = []
lignes= []


def save():
    with open('save_elements/dep_save.txt', 'r') as f:
        read_dep = f.read()
    if read_dep == str(0):
        with open('save_elements/save.txt', 'w') as f:
            f.write(choix)
            f.write(" - ")
            f.write(price_write)
            dep_save()
    else:
        with open('save_elements/save.txt', 'a') as f:
            f.write("\n")
            f.write(choix)
            f.write(" - ")
            f.write(price_write)
            dep_save()       


if choix in creatures:
    price = creatures[choix]

else:
    while choix not in creatures:
        try:
            choix = input("Entre un nom d'insecte correct")
            if choix in creatures:
                price = creatures[choix]
                break
        except ValueError:
            print("Cet insecte n'existe pas")

price_write = price + "Cl"

print(price, "Cl")

quitter = input("'Exit' pour quitter, 'Save' pour sauvegarder et quitter, 'Reset' pour reset la save")
if quitter == "Exit":
    print("Vous allez quitter le programme")
    exit()
elif quitter == "Save":
    save()
    print("La sauvegarde a bien été effectué")
    exit()
#elif quitter == "Continuer":
#    tout()
elif quitter == "Reset_save":
    reset_save()
    print("La sauvegarde a bien été supprimé")
elif quitter == "Reset_dep_save":
    reset_dep_save()
    print("La sauvegarde a bien été supprimé")
elif quitter == "Reset":
    reset_all()
    print("La sauvegarde a bien été supprimé")
#elif quitter == "Save+Continuer":
#    save()
#   print("La sauvegarde a bien été effectué")
#    tout()
elif quitter != "Exit" "Save" "Reset" "Reset_save" "Reset_dep_save" "Save+Quitter":

    while quitter != "Save" "Quitter" "Reset_save" "Reset_dep_save" "Reset":
        try:
            quitter = input("'Exit' pour quitter, 'Save' pour sauvegarder et quitter, 'Reset' pour reset la save")
            if quitter == "Exit":
                print("Vous allez quitter le programme")
                exit()
            elif quitter == "Save":
                save()
                print("La sauvegarde a bien été sauvegardé")
                exit()
#            elif quitter == "Continuer":
#                tout()
            elif quitter == "Reset_save":
                reset_save()
                print("La sauvegarde a bien été supprimé")
            elif quitter == "Reset_dep_save":
                reset_dep_save()
                print("La sauvegarde a bien été supprimé")
            elif quitter == "Reset":
                reset_all()
                print("La sauvegarde a bien été supprimé")
#            elif quitter == "Save+Continuer":
#                save()
#                print("La sauvegarde a bien été effectué")
#                tout()
            elif quitter != "Exit" "Save" "Reset":
                print("Entre une des options")
        except ValueError:
            print("Entre une des options")
        