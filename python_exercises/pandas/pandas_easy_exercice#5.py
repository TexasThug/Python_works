import numpy as np 
import pandas as pd 

produit = ["Burger", "Wrap", "Bagnat", "Hot Dog", "Tartine", "Nuggets", "Potatoes", "Frites", "Croque Monsieur", "Croque Madame"]

Lundi = np.random.randint(50, 500, 10)
Mardi = np.random.randint(50, 500, 10)
Mercredi = np.random.randint(50, 500, 10)

data = {
    "Produit" : produit,
    "Lundi" : Lundi,
    "Mardi" : Mardi,
    "Mercredi" : Mercredi
}

df = pd.DataFrame(data)

df["Total"] = np.sum(df[["Lundi", "Mardi", "Mercredi"]], axis = 1)

df = df.sort_values(by="Total", ascending = False)

df["Statut"] = np.where(df["Total"] >700,"Best-Seller","Standard")

moyenne_ventes = np.mean(df["Total"])
best = df.loc[df["Total"].idxmax()]
worst = df.loc[df["Total"].idxmin()]

print(df)
print("\n------ Résumé des ventes ------")
print(f"Moyenne totale des ventes : {moyenne_ventes:.0f} unités")
print(f"Produit le plus vendu : {best['Produit']} ({best['Total']} ventes)")
print(f"Produit le moins vendu : {worst['Produit']} ({worst['Total']} ventes)")









