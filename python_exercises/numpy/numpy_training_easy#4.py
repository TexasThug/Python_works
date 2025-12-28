import numpy as np 

#Exercice 1 — Créer un array
print("---Exercice1---")
valeurs = np.array([1,2,3,4,5])
print(valeurs)

#Exercice 2 — Infos sur un array
print("---Exercice2---")
arr = np.array([10, 20, 30, 40, 50])
print("forme :", arr.shape)
print("Type :", arr.dtype)
print("Dimensions :", arr.ndim)

#Exercice 3 — Opérations simples
print("---Exercice3---")
arr = np.array([1, 2, 3, 4])
# Multiplie chaque élément par 2
# Affiche le résultat
print(arr * 2)

print("---Exercice4---")
#Exercice 4 — Condition sur array
arr = np.array([5, 12, 7, 20, 3])
# Affiche uniquement les valeurs > 10
print(arr[arr>10])

print("---Exercice5---")
#Exercice 5 — Statistiques simples
arr = np.array([10, 15, 20, 25, 30])
# Affiche :
# - la moyenne
print(arr.mean())
# - le minimum
print(arr.min())
# - le maximum
print(arr.max())

print("---Exercice6---")
#Exercice 6 — Array + condition
scores = np.array([12, 8, 15, 6, 18, 10])
# Affiche uniquement les scores >= 10
print(scores[scores>=10])

print("---Exercice7---")
#Exercice 7 — Transformation
prices = np.array([100, 200, 300])
# Applique une réduction de 10%
print(prices*0.9)

print("---Exercice8---")
#Exercice 8 — Calcul vectorisé
quantities = np.array([2, 5, 1])
prices = np.array([10, 4, 20])
# Calcule le total par produit
total_per_prod = quantities*prices
print("Total produit :",total_per_prod)
# puis le total global
print("Total global :", total_per_prod.sum())

print("---Exercice9---")
#Exercice 9 — Array 2D
data = np.array([
    [10, 20, 30],
    [5, 15, 25]
])
# Affiche :
# - la somme par ligne
print("Somme par ligne :", data.sum(axis=1))
# - la somme totale
print("Somme totale :",data.sum())

print("---Exercice10---")
#Exercice 10 — Mini data analyst
sales = np.array([1200, 950, 1430, 800, 1600])

# Affiche :
# - la meilleure vente
print("Meilleure vente :",sales.max())
# - la moyenne
print("Moyenne des ventes :",sales.mean())
# - les ventes supérieures à la moyenne
mean_sales = sales.mean()
print("Ventes > moyenne :",sales[sales> mean_sales])
