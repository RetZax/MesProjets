#1. Demandez le prix unitaire des pommes.
price = input("Veuillez entrer le prix de la pommes")
#Demandez le poids des pommes
weigth = input("Veuillez entrer le poids des pommes")

#calculer le montant
#Convertir le prix unitaire d'une pomme et le poids de la pomme en décimal
money = float(price) * float(weigth)
print(type(money))
print("Veuillez payer :" + str(money), "euros")

