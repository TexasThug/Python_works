import numpy as np
import pandas as pd

np.random.seed(0)
data = np.random.randint(10, 100, (4, 5))

operateurs = ["OP1", "OP2", "OP3", "OP4"]
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

df = pd.DataFrame(data, index=operateurs, columns=jours)

print(df)

print("---Exercice1---")
# Affiche :
# - les 2 premières lignes
print(df.head(2))
# - les colonnes
print(df.columns)
# - les index
print(df.index)

print("---Exercice2---")
# Affiche :
# - le total par opérateur
print(df.sum(axis=1))
# - le total par jour
print(df.sum(axis=0))

print("---Exercice3---")
# Affiche :
# - la moyenne par opérateur
print(df.mean(axis=1))
# - la moyenne globale
print(df.values.mean())

print("---Exercice4---")
# Affiche uniquement :
# - les valeurs >= 50
print(df[df >= 50])

print("---Exercice5---")
# Affiche :
# opérateur le plus performant
best_operator = df.sum(axis=1).idxmax()
print("Meilleur opérateur :", best_operator)

# jour le plus productif
best_day = df.sum(axis=0).idxmax()
print("Jour le plus productif :", best_day)

