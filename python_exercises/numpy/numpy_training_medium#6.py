<<<<<<< HEAD
import numpy as np
import pandas as pd 

np.random.seed(42)
livraisons = np.random.randint(20,100,(6,12))

chauffeurs = ["C1", "C2", "C3", "C4", "C5", "C6"]
jours = [f"Jour {i+1}" for i in range(12)]

df = pd.DataFrame(livraisons, index=chauffeurs, columns=jours)
print(df)

total_colis_par_chauffeurs = np.sum(livraisons, axis=1)
for i, total in enumerate(total_colis_par_chauffeurs): 
    print(f"Le chauffeur {chauffeurs[i]} a livré :{total_colis_par_chauffeurs[i]} colis.")

print("\n---------------")

total_colis_par_jour = np.sum(livraisons, axis=0)
for i, total in enumerate(total_colis_par_jour):
    print(f"{jours[i]}, il a été livré : {total_colis_par_jour[i]} colis.")

print("\n---------------")

best_chauffeur = np.argmax(total_colis_par_chauffeurs)
print(f"Le chauffeur {chauffeurs[best_chauffeur]} a livré le plus de colis. Il a livré {total_colis_par_chauffeurs[best_chauffeur]} colis.")

best_day = np.argmax(total_colis_par_jour)
print(f"Le {jours[best_chauffeur]} est le jour qui a le plus de livraisons. Il a été livré {total_colis_par_jour[best_day]} colis.")

livraisons_totales = np.sum(livraisons)
print(f"Il y a eut {livraisons_totales} livraisons au total.")

part_chauffeurs = (total_colis_par_chauffeurs/livraisons_totales)*100
for i, total in enumerate(part_chauffeurs):
    print(f"Le chauffeur {chauffeurs[i]} a livré {part_chauffeurs[i]:.1f} % des livraisons totales.")

nbr_jours_incr = np.sum(total_colis_par_jour > 90)
print(f"Il y a eut {nbr_jours_incr} jours avec un taux de livraisons incroyable.")

nbr_jours_faible = np.sum(total_colis_par_jour < 40)
print(f"Il y a eut {nbr_jours_faible} jours avec un taux de livraisons incroyable.")

moy_total_livraisons = np.mean(livraisons)
print(f"la moyenne de livraisons au total est de :{moy_total_livraisons}")

ecart_type = np.std(livraisons)
=======
import numpy as np
import pandas as pd 

np.random.seed(42)
livraisons = np.random.randint(20,100,(6,12))

chauffeurs = ["C1", "C2", "C3", "C4", "C5", "C6"]
jours = [f"Jour {i+1}" for i in range(12)]

df = pd.DataFrame(livraisons, index=chauffeurs, columns=jours)
print(df)

total_colis_par_chauffeurs = np.sum(livraisons, axis=1)
for i, total in enumerate(total_colis_par_chauffeurs): 
    print(f"Le chauffeur {chauffeurs[i]} a livré :{total_colis_par_chauffeurs[i]} colis.")

print("\n---------------")

total_colis_par_jour = np.sum(livraisons, axis=0)
for i, total in enumerate(total_colis_par_jour):
    print(f"{jours[i]}, il a été livré : {total_colis_par_jour[i]} colis.")

print("\n---------------")

best_chauffeur = np.argmax(total_colis_par_chauffeurs)
print(f"Le chauffeur {chauffeurs[best_chauffeur]} a livré le plus de colis. Il a livré {total_colis_par_chauffeurs[best_chauffeur]} colis.")

best_day = np.argmax(total_colis_par_jour)
print(f"Le {jours[best_chauffeur]} est le jour qui a le plus de livraisons. Il a été livré {total_colis_par_jour[best_day]} colis.")

livraisons_totales = np.sum(livraisons)
print(f"Il y a eut {livraisons_totales} livraisons au total.")

part_chauffeurs = (total_colis_par_chauffeurs/livraisons_totales)*100
for i, total in enumerate(part_chauffeurs):
    print(f"Le chauffeur {chauffeurs[i]} a livré {part_chauffeurs[i]:.1f} % des livraisons totales.")

nbr_jours_incr = np.sum(total_colis_par_jour > 90)
print(f"Il y a eut {nbr_jours_incr} jours avec un taux de livraisons incroyable.")

nbr_jours_faible = np.sum(total_colis_par_jour < 40)
print(f"Il y a eut {nbr_jours_faible} jours avec un taux de livraisons incroyable.")

moy_total_livraisons = np.mean(livraisons)
print(f"la moyenne de livraisons au total est de :{moy_total_livraisons}")

ecart_type = np.std(livraisons)
>>>>>>> 52447dc1ca6365f255affe452ebba08745f13a4d
print(f"l'écart type des livraisons au total est de :{ecart_type}")