# Importation des modules, de l'API et attribution des variables de prix
import sys
import time
ts = time.gmtime()
horodatage = time.strftime("%d-%m-%Y %H:%M", ts)

sys.path.append("api.py")
from api import *

sp98 = sp98()
sp95 = sp95()
e10 = e10()
e85 = e85()
diesel = diesel()
gpl = gpl()

# Début du script
capacite_reservoir = float(input("Entrez la capacité de votre réservoir : "))
km_parcourus = float(input("Entrez le nombre de kilomètres parcourus avec un plein : "))
conso_moyenne = capacite_reservoir * 100 / km_parcourus
print("Votre consommation moyenne est de" , round(conso_moyenne,2) , "L/100 km.")

selection_carburant = int(input("Sélectionnez votre carburant : \n 1. SP98 \n 2. SP95 \n 3. E10 \n 4. E85 \n 5. Diesel \n 6. GPL \n "))

if selection_carburant == 1:
    print("A l'heure actuelle (" , horodatage , "), le prix moyen du litre de SP98 en France est de" , sp98 , "€.")
elif selection_carburant == 2:
    print("A l'heure actuelle (" , horodatage , "), le prix moyen du litre de SP95 en France est de" , sp95 , "€.")
elif selection_carburant == 3:
    print("A l'heure actuelle (" , horodatage , "), le prix moyen du litre de E10 en France est de" , e10 , "€.")
elif selection_carburant == 4:
    print("A l'heure actuelle (" , horodatage , "), le prix moyen du litre de E85 en France est de" , e85 , "€.")
elif selection_carburant == 5:
    print("A l'heure actuelle (" , horodatage , "), le prix moyen du litre de Diesel en France est de" , diesel , "€.")
elif selection_carburant == 6:
    print("A l'heure actuelle (" , horodatage , "), le prix moyen du litre de GPL en France est de" , gpl , "€.")

question_calcul = (input("Souhaitez-vous calculer le prix moyen de votre consommation par km (o/n) ? "))

if question_calcul == "o" and selection_carburant == 1:
    calcul = conso_moyenne * sp98 / 100
    print("Vous dépensez en moyenne " , round(calcul,2) , "€ par km.")
elif question_calcul == "o" and selection_carburant == 2:
    calcul = conso_moyenne * sp95 / 100
    print("Vous dépensez en moyenne " , round(calcul,2) , "€ par km.")
elif question_calcul == "o" and selection_carburant == 3:
    calcul = conso_moyenne * e10 / 100
    print("Vous dépensez en moyenne " , round(calcul,2) , "€ par km.")
elif question_calcul == "o" and selection_carburant == 4:
    calcul = conso_moyenne * e85 / 100
    print("Vous dépensez en moyenne " , round(calcul,2) , "€ par km.")
elif question_calcul == "o" and selection_carburant == 5:
    calcul = conso_moyenne * diesel / 100
    print("Vous dépensez en moyenne " , round(calcul,2) , "€ par km.")
elif question_calcul == "o" and selection_carburant == 6:
    calcul = conso_moyenne * gpl / 100
    print("Vous dépensez en moyenne " , round(calcul,2) , "€ par km.")

quitter_programme = (input("Pour quitter, appuyez sur n'importe quelle touche."))