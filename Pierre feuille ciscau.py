
'''
import random
#Renvoyer un entier entre (1,100)
print(random.randint(1,3))
'''
import random
computer = random.randint(1,3)
player = int(input("Que voulez-vous jouer ? Pierre(1)/Ciseaux(2)/Papier(3) "))
print("Computer : " + str(computer))

if player == computer:
    #(player == 1 and computer == 1) or (player == 2 or computer == 2) or (player == 3 and computer == 3):
    print("Egalité")

elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("Le joueur gagne")

else:
    print("L'ordinateur gagne")










'''
computer = 1
player = int(input("Que voulez-vous jouer ? Pierre(1)/Ciseaux(2)/Papier(3) "))


if player == 1 and computer == 1:
    print("Les deux cotés sont à égalité")
elif player == 3 and computer == 1:
    print("Le joueur gagne")
else:
    print("L'ordinateur gagne")
    '''

'''
computer = 2
player = int(input("Que voulez-vous jouer ? Pierre(1)/Ciseaux(2)/Papier(3) "))


if player == 2 and computer == 2:
    print("Les deux cotés sont à égalité")
elif player == 1 and computer == 2:
    print("Le joueur gagne")
else:
    print("L'ordinateur gagne")
'''
'''
computer = 3
player = int(input("Que voulez-vous jouer ? Pierre(1)/Ciseaux(2)/Papier(3) "))


if player == 3 and computer == 3:
    print("Les deux cotés sont à égalité")
elif player == 2 and computer == 3:
    print("Le joueur gagne")
else:
    print("L'ordinateur gagne")
'''
