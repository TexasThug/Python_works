import numpy as np 
import pandas as pd 

np.random.seed(10)
usine = np.random.randint(20, 120,(4,8))

operateurs = ["OP1","OP2", "OP3", "OP4"]
jours=[f"Jour {i+1}" for i in range(8)]

df = pd.DataFrame(usine, index=operateurs, columns = jours)
print(df)

total_par_operateur = np.sum(usine, axis=1)
for i, total in enumerate(total_par_operateur):
    print(f"L'opérateur {operateurs[i]} a produit {total}au total.")

total_par_jour = np.sum(usine, axis=0)
for i, total in enumerate(total_par_jour):
    print(f"Les opérateurs ont produit {total} au {jours[i]}")

best_operateur = np.argmax(total_par_operateur)
print(f"le meilleur operateur est {operateurs[best_operateur]} car il a produit {total_par_operateur[best_operateur]} produits.")

best_day = np.argmax(total_par_jour)
print(f"le meilleur jours est {jours[best_day]} car il y a eut {total_par_jour[best_day]} produits crées.")

total_global = np.sum(usine)
print(f"\n Il y a eut {total_global} livraisons en tout.")

moy_global = np.mean(usine)
print(f"Moyenne globale : {moy_global:.1f} unités")

ecart_type_global = np.std(usine)
print(f"Ecart Type global : {ecart_type_global:.1f} unités")

print(f"\n La part de chaque opérateur est de :")
part_par_operateur = (total_par_operateur/total_global)*100
for i, total in enumerate(part_par_operateur):
    print(f"{operateurs[i]} > {total:.1f}% du total")

print("Totaux par jour :", total_par_jour)

nbr_jour_incr = np.sum(total_par_jour >400)
print(f"\nNombre de jours forts (>400 unités) : {nbr_jour_incr}")

nbr_jour_nul = np.sum(total_par_jour <250)
print(f"\nNombre de jours nuls (>250 unités) : {nbr_jour_nul}")





