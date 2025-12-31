import numpy as np
import pandas as pd

np.random.seed(2)
data = np.random.randint(30, 120, (5, 7))

employees = ["Alice", "Bob", "Charlie", "Diane", "Eve"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame(data, index=employees, columns=days)
print(df)

print("---Exercice1---")
# Affiche :
# - les 2 dernières lignes
print(df.tail(2))
# - le nombre total de valeurs dans le DataFrame
print(df.size)

print("---Exercice2---")
# Affiche :
# - le total par employé
print(df.sum(axis=1))
# - le total par jour
print(df.sum(axis=0))

print("---Exercice3---")
# Calcule la moyenne globale
moyenne_globale = df.values.mean()
print(moyenne_globale)
# Affiche uniquement les valeurs supérieures à cette moyenne
print(df[df >moyenne_globale])

print("---Exercice4---")
# Affiche :
# - l’employé le plus productif sur la semaine
best_employee = df.sum(axis=1).idxmax()
print("Best employee :",best_employee)
# - le jour le plus productif
best_day = df.sum(axis=0).idxmax()
print("Best day :",best_day)

print("---Exercice5---")
# Affiche :
# - le total global
total_global = df.values.sum()
print("Total global :",total_global)
# - la moyenne par employé
employee_mean = df.mean(axis=1)
print("Employee mean :",employee_mean)
# - la part (%) de chaque employé dans le total global
parts = (df.sum(axis=1) / df.values.sum()) * 100
print(parts)


