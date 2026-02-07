import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "A", "C", "B"],
    "price": [10, 15, 10, 20, 15],
    "quantity": [2, 1, 3, 5, 2]
})

print("----Exercice1----")
# 1. Afficher les 5 premières lignes
print("\n5 premières lignes :")
print(df.head())

# 2. Nombre de lignes et de colonnes
print("\nNombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

# 3. Type de chaque colonne
print("\nType de chaque colonne :")
print(df.dtypes)

print("----Exercice2----")
# 1. Garde uniquement les lignes où product == "A"
df[df["product"] == "A"]

# 2.Garde uniquement les lignes où quantity >= 2
df[df["quantity"] >= 2]

# 3. Garde les lignes où : product == "B" ET price == 15
df[(df["product"] == "B") & (df["price"] == 15)]

print("----Exercice3----")
# 1. Créer total_price
df["total_price"] = df["price"] * df["quantity"]

# 2. Valeur total des ventes 
df["total_price"].sum()

print("----Exercice4----")
# 1. Prix moyen
df["price"].mean()

# 2. Quantité totale vendue
df["quantity"].sum()

# 3. Nombre d’occurrences par produit
df["product"].value_counts()

print("----Exercice5----")
# Produit le plus vendu 
df.groupby("product")["quantity"].sum().idxmax()

# Produit avec le plus de chiffre d’affaires
df.groupby("product")["total_price"].sum().idxmax()

