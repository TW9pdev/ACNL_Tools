
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

def save():
    with open('dep_save.txt', 'r') as f:
        read_dep = f.read()
    if read_dep == str(0):
        with open('save.txt', 'w') as f:
            f.write(choix)
            f.write(" - ")
            f.write(price_write)
            dep_save()
    else:
        with open('save.txt', 'a') as f:
            f.write("\n")
            f.write(choix)
            f.write(" - ")
            f.write(price_write)
            dep_save()    

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