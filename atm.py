money = 5000000
name = input("Veuillez entrer votre nom: ")


def menu():
    print("----------Menu Principal----------")
    print(name + ", bonjour, Bienvenue à ATM, veuillez sélectionner l'opération:")
    print("Verifier le solde [Entrer 1]")
    print("Dépôts            [Entrer 2]")
    print("retrait           [Entrer 3]")
    print("Menu principal    [Entrer 4]")
    choice = int(input("Veuillez entrer votre choix:"))
    return choice



def query():
    print("-----------Vérifier le solde-----------")
    print(str(name) + " bonjour, il vous rest un solde de " + str(money) + " euros")




def saving():
    global sum
    eco = input("Combien voulez-vous economiser ? Veuiller entrer: ")
    print(name + " Bonjour, votre depot de" + str(eco) + " euros à été accepté.")
    sum = int(eco) + int(money)
    print(name + " Bonjour, il vous reste un solde de " + str(sum))


def get_money():
    retirer = input("Combien voulez vous retirer ? Veuillez entrer : ")
    print(name+",bonjour, votre retrait de " + str(retirer) + " euros a été effectué.")
    sum2 = int(sum) - int(retirer)
    print(name +",bonjour, il vous reste un solde de " + str(sum2))

def exit():
    print("Sortie du programme")

while True:
    choice = menu()

    if choice == 1:
        query()
        continue

    if choice == 2:
        saving()
        continue

    if choice == 3:
        get_money()
        continue

    if choice == 4:
        exit()
        break




