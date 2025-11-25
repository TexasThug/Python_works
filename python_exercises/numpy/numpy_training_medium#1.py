import numpy as np 

np.random.seed(42)
production = np.random.randint(80, 200, (5, 7))
print(production)

produits = ["A", "B", "C", "D", "E"]
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# Total par produit
total_par_produit = np.sum(production, axis=1)
for i, total in enumerate(total_par_produit):
    print(f"Produit {produits[i]} → total : {total:.1f}")

# Moyenne par produit
moyenne_par_produit = np.mean(production, axis=1)
for i, moyenne in enumerate(moyenne_par_produit):
    print(f"Produit {produits[i]} → moyenne : {moyenne:.1f}")

# Total par jour
total_par_jour = np.sum(production, axis=0)
for i, total in enumerate(total_par_jour):
    print(f"{jours[i]} → total : {total}")

# Jour le plus et le moins productif
jour_plus = np.argmax(total_par_jour)
jour_moins = np.argmin(total_par_jour)

print(f"\nJour le plus productif : {jours[jour_plus]} ({total_par_jour[jour_plus]})")
print(f"Jour le moins productif : {jours[jour_moins]} ({total_par_jour[jour_moins]})")

# Total par produit (déjà calculé avant)
total_par_produit = np.sum(production, axis=1)

# Produit le plus fabriqué
index_best = np.argmax(total_par_produit)
print(f"\nProduit le plus fabriqué : {produits[index_best]} ({total_par_produit[index_best]} unités)")

# Production totale (tous produits confondus)
total_global = np.sum(total_par_produit)

# Part (%) de chaque produit
part_produits = (total_par_produit / total_global) * 100

print("\nPart de chaque produit dans la production totale :")
for i, part in enumerate(part_produits):
    print(f"{produits[i]} → {part:.1f}%")

mask_exceptionnel = production > 150
nb_jours_exceptionnels = np.sum(mask_exceptionnel)
print(f"\nNombre total de journées exceptionnelles (>150 unités) : {nb_jours_exceptionnels}")

mask_faible = production < 100
nb_jours_faibles = np.sum(mask_faible)
total_cases = production.size  # nombre total de valeurs dans la matrice

pourcentage_faibles = (nb_jours_faibles / total_cases) * 100
print(f"Pourcentage de journées faibles (<100 unités) : {pourcentage_faibles:.1f}%")
