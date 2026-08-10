def ask_choix():
    choix = input("Entre un nom d'insecte: ")

def dep_save():
    with open('dep_save.txt', 'r') as f:
            a = int(f.read())

    a += 1

    with open('dep_save.txt', 'w') as f:
        f.write(str(a))


def reset_dep_save():
    with open('dep_save.txt', 'w') as f:
        f.write(str(0))

    
def reset_save():
    with open('save.txt', 'w') as f:
        f.write(str(""))


def reset_all():
    with open('save.txt', 'w') as f:
        f.write(str(""))
    with open('dep_save.txt', 'w') as f:
        f.write(str(0))

insectes = {
    "Abeille": "2 500",
    "Abeille naine": "100",
    "Acrida cinerea": "200",
    "Agrias": "3 000",
    "Anax napolitain": "200",
    "Araignée": "300",
    "Bousier": "800",
    "Brookiana": "2 500",
    "Bupreste": "2 400",
    "Cicindèle": "1 500",
    "Cigale cercope": "200",
    "Cigale cicadelle": "400",
    "Cigale géante": "500",
    "Cigale higurashi": "550",
    "Cigale hyalessa": "300",
    "Citrin": "90",
    "Cloporte": "250",
    "Coccinelle": "200",
    "Cordulégastre": "4 500",
    "Coscinocera hercules": "1 200",
    "Criquet": "400",
    "Criquet pèlerin": "600",
    "Demoiselle": "80",
    "Dytique": "800",
    "Escargot": "250",
    "Fourmi": "80",
    "Grillon des prés": "130",
    "Grillon du Midi": "430",
    "Laternaria": "1 800",
    "Libellule géante": "8 000",
    "Ligie": "200",
    "Longicorne": "260",
    "Lucane cerf-volant": "10 000",
    "Lucane copris irisé": "10 000",
    "Lucane cyclommatus": "8 000",
    "Lucane inclinatus": "2 000",
    "Lucane lamprima": "12 000",
    "Lucane miyama": "1 000",
    "Luciole": "300",
    "Machaon": "160",
    "Mante orchidée": "2 400",
    "Mante religieuse": "430",
    "Mille-pattes": "300",
    "Monarque": "140",
    "Mormolyce": "260",
    "Morpho bleu": "2 500",
    "Mouche": "60",
    "Moustique": "130",
    "Mue de cigale": "100",
    "Nitidule": "100",
    "Ornithoptère": "4 000",
    "Papilio bianor": "220",
    "Papillon de nuit": "60",
    "Patineur": "130",
    "Phasme": "600",
    "Phyllie": "600",
    "Piéride de la rave": "90",
    "Psyché": "300",
    "Puce": "70",
    "Punaise": "120",
    "Sauterelle": "160",
    "Scarabée": "6 000",
    "Scarabée Atlas": "8 000",
    "Scarabée éléphant": "8 000",
    "Scarabée Goliath": "6 000",
    "Scarabée Hercule": "12 000",
    "Scarabée kabuto": "1 350",
    "Scorpion": "8 000",
    "Scutigère": "250",
    "Tarentule": "8 000",
    "Taupe-grillon": "280",
    "Bernard-l'ermite": "1000",
}

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
    elif quitter == "Save+Quitter":
        save()
        print("La sauvegarde a bien été effectué")
        print("Vous allez quitter le programme")
        exit()
    elif quitter != "Exit" "Save" "Reset" "Reset_save" "Reset_dep_save" "Save+Continuer" "Save+Quitter":

        while quitter != "Save" "Quitter" "Reset_save" "Reset_dep_save" "Reset":
            try:
                quitter = input("'Exit' pour quitter, 'Save' pour sauvegarder et quitter, 'Reset' pour reset la save")
                if quitter == "Exit":
                    print("Vous allez quitter le programme")
                    exit()
                elif quitter == "Save":
                    save()
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
                elif quitter == "Save+Quitter":
                    save()
                    print("La sauvegarde a bien été effectué")
                    print("Vous allez quitter le programme")
                    exit()
                elif quitter != "Exit" "Save" "Reset":
                    print("Entre une des options")
            except ValueError:
                print("Entre une des options")