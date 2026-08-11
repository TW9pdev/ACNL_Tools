
choix = input("Entre un nom d'une créature: ")

def dep_save():
    with open('save_elements/dep_save.txt', 'r') as f:
            a = int(f.read())

    a += 1

    with open('save_elements/dep_save.txt', 'w') as f:
        f.write(str(a))


def reset_dep_save():
    with open('save_elements/dep_save.txt', 'w') as f:
        f.write(str(0))

    
def reset_save():
    with open('save_elements/save.txt', 'w') as f:
        f.write(str(""))


def reset_all():
    with open('save_elements/save.txt', 'w') as f:
        f.write(str(""))
    with open('save_elements/dep_save.txt', 'w') as f:
        f.write(str(0))

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

