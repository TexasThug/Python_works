import numpy as np 

# Analyse de Capteurs de Pression
# Sscénario : Tu as 5 capteurs qui mesurent la pression d'une machine toutes les heures pendant une journée entière (24h)

np.random.seed(42)
pressions = np.random.uniform(1.0, 5.0,(5,24))

pression_moyenne = pressions.mean()
print(f"La pression moyenne globale est de : {pression_moyenne:.2f} bars")
pression_maximum = pressions.max()
print(f"La pression maximum globale est de : {pression_maximum:.2f} bars")
pression_minimum = pressions.min()
print(f"La pression minimum globale est de : {pression_minimum:.2f} bars")
print("--------------------------------------------------")
print("--------------------------------------------------")

# Analyse pour chaque capteur
pression_moyenne_capteurs = pressions.mean(axis=1)

print("Pressions moyennes par capteur (en bars) :")
print(pression_moyenne_capteurs.round(2))

# Valeur max pour chaque capteur
max_par_capteur = pressions.max(axis=1)

# Capteur avec la plus grosse pression
capteur_max = max_par_capteur.argmax()
print(f"Le capteur avec la pression la plus élevée est le capteur n°{capteur_max}")

# Détection anomalies
pressions_critiques = pressions > 4.8

# Compter le nombres d'anomalies
total_pressions_critiques = np.sum(pressions_critiques)

valeurs_critiques = pressions[pressions_critiques]

print(f"Nombre total de mesures critiques : {total_pressions_critiques}")
print(f"Liste des pressions relevées au-dessus du seuil : \n{valeurs_critiques}")

# Correction : on ajoute 0.2 bar à chaque cellule de la matrice
pressions_corrigees = pressions + 0.2
