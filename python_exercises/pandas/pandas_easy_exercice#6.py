import numpy as np
import pandas as pd

# Produits vendus
Produits = ["Pizza", "Burger", "Wrap", "Hot Dog", "Salade", "Frites", "Tacos", "Nuggets"]

Lundi = np.random.randint(30, 150, len(Produits))
Mardi = np.random.randint(30, 150, len(Produits))
Mercredi = np.random.randint(30, 150, len(Produits))
Jeudi = np.random.randint(30, 150, len(Produits))
Vendredi = np.random.randint(30, 150, len(Produits))

data = {
    "Produits" : Produits,
    "Lundi" : Lundi,
    "Mardi" : Mardi,
    "Mercredi" : Mercredi,
    "Jeudi" : Jeudi,
    "Vendredi" : Vendredi
}

df = pd.DataFrame(data)

df["Total Semaine"] = df[["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]].sum(axis=1)

df = df.sort_values(by = "Total Semaine", ascending = False)

moyenne = df["Total Semaine"].mean()
max_ventes = df["Total Semaine"].max()
min_ventes = df["Total Semaine"].min()

best = df.loc[df["Total Semaine"].idxmax()]
worst = df.loc[df["Total Semaine"].idxmin()]

df["Statut"] = np.where(df["Total Semaine"]> moyenne, "Top Vente", "Standard")
print(df)

print("\n------ Résumé des ventes ------")
print(f"Moyenne hebdo : {moyenne:.1f} ventes")
print(f"Produit le plus vendu : {best['Produits']} ({best['Total Semaine']} ventes)")
print(f"Produit le moins vendu : {worst['Produits']} ({worst['Total Semaine']} ventes)")












