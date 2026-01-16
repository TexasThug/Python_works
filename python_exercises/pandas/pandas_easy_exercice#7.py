import numpy as np
import pandas as pd

# Données de base
noms = ["Alice", "Bob", "Charlie", "David", "Emma", "Fred", "Julie", "Léo", "Mia", "Noah"]
departements = ["Ventes", "Marketing", "RH", "Tech", "Ventes", "Tech", "Comptabilité", "RH", "Tech", "Marketing"]

np.random.seed(42)
salaires = np.random.randint(2500, 7000, len(noms))
primes = np.random.randint(200, 1000, len(noms))
note_perf = np.random.randint(1, 21, len(noms))

df = pd.DataFrame({
    "Nom": noms,
    "Departements" : departements,
    "Salaires" : salaires,
    "Primes" : primes,
    "Note Performance" : note_perf
})

df["Revenu_total"] = df["Salaires"] + df["Primes"]

moyenne_salaire = df["Salaires"].mean()
moyenne_perf = df["Note Performance"].mean()
print(df)

df["Statut"] = np.where(df["Note Performance"] >= moyenne_salaire, "Excellent", "Standard")
df = df.sort_values(by = "Revenu_Total", ascending = False)

best = df.loc[df["Revenu_Total"].idxmax()]
worst = df.loc[df["Revenu_Total"].idxmin()]

print("\n------ RAPPORT RH ------")
print(f"Salaire moyen : {moyenne_salaire:.2f} €")
print(f"Performance moyenne : {moyenne_perf:.2f}/20")
print(f"Meilleur employé : {best['Nom']} ({best['Performance']}/20 - {best['Departement']})")
print(f"Moins bon employé : {worst['Nom']} ({worst['Performance']}/20 - {worst['Departement']})")
