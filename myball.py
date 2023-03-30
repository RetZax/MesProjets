import random
myCollection=['rouge','rose','orange','rouge','rose','jaune','rose','jaune']

bag_of_balls=['rose','bleu','vert','orange','rouge','pourpe','vert','bleu','bleu'
             'rouge','vert','pourpe','jaune','rouge','rose','rouge','vert','jaune']

balls_outputs = []

remaining_draws=5

for x in range(5):
    if remaining_draws>0:
        selection = random.choice(bag_of_balls)
        balls_outputs.append(selection)
        remaining_draws -= 1
        if selection == 'vert' :
            myCollection.append(selection)
            bag_of_balls.remove(selection)

            print("Excellent! Tu as tiré la bille verte !")
            print("Il restait" + str(remaining_draws) + "tirages")
            break
if not('vert' in myCollection):
    print("Tous les tirages sont faits. Aucune bille verte")

print("\nBilles sorties pour ce tirage:")
print(F"{balls_outputs}")
print(F"\nLa nouvelle collection contient: \n{myCollection}")