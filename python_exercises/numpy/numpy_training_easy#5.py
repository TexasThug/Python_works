import numpy as np 

print("---Exercice1---")
#Exercice 1 — Filtrage simple
arr = np.array([3, 12, 7, 25, 9, 18])

# Affiche uniquement les valeurs >= 10
print(arr[arr>=10])

print("---Exercice2---")
#Exercice 2 — Filtrage avec intervalle
arr = np.array([5, 8, 12, 17, 20, 25, 30])

# Affiche uniquement les valeurs
# comprises entre 10 et 25 inclus
print(arr[(arr >= 10) & (arr <= 25)])

print("---Exercice3---")
#Exercice 3 — Masque + calcul
scores = np.array([6, 12, 15, 8, 20, 9])

# Calcule la moyenne
moyenne = scores.mean()
print(moyenne)
# puis affiche uniquement les scores
# strictement supérieurs à la moyenne
print(scores[scores>moyenne])

print("---Exercice4---")
#Exercice 4 — Remplacement conditionnel
temps = np.array([12, 18, 25, 9, 30, 15])

# Remplace toutes les valeurs < 15
# par 15
temps[temps < 15] = 15
print(temps)

print("---Exercice5---")
#Exercice 5 — Mini data analyst 
sales = np.array([1200, 950, 1430, 800, 1600, 1100])

# Affiche :
# - les ventes >= 1000
filtered = sales[sales >= 1000]
print(filtered)
# - le nombre de ventes >= 1000
print("Nombre :", filtered.size)
# - le pourcentage de ventes >= 1000
print("Pourcentage :", (filtered.size / sales.size) * 100)
