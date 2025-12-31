import numpy as np
import pandas as pd

np.random.seed(1)
data = np.random.randint(20, 100, (4, 6))

teams = ["Team A", "Team B", "Team C", "Team D"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

df = pd.DataFrame(data, index=teams, columns=days)
print(df)

print("---Exercice1---")
# Affiche :
# - les 3 premières lignes
print(df.head(3))
# - le nombre de lignes et de colonnes
print(df.shape)

print("---Exercice2---")
# Affiche :
# - le total par équipe
print(df.sum(axis=1))
# - le total par jour
print(df.sum(axis=0))

print("---Exercice3---")
# Affiche :
# - la moyenne par équipe
print(df.mean(axis=1))
# - la moyenne par jour
print(df.mean(axis=0))
# - la moyenne globale
print(df.values.mean())

print("---Exercice4---")
# Affiche uniquement :
# - les valeurs >= 70
print(df[df >= 70])

print("---Exercice5---")
# Affiche :
# - l’équipe la plus performante
best_team = df.sum(axis=1).idxmax()
print("Best team :", best_team)
# - le jour le plus productif
best_day = df.sum(axis=0).idxmax()
print("Best day :", best_day)
# - le total global
total_global = df.values.sum()
print("Total global :", total_global)

