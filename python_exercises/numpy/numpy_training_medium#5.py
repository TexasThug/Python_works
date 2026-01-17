import numpy as np 
print("---Exercice1---")
#Exercice 1 — Masque + stat conditionnelle
scores = np.array([6, 12, 15, 8, 20, 9, 14])

# Calcule la moyenne des scores >= 10
max_values = scores([scores >= 10])
print(max_values.mean())