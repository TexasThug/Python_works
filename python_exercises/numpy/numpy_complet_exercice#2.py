import numpy as np 

np.random.seed(42)
m_carre = np.random.randint(15,80,(8,10))

ouvriers = ["O1","O2","O3","O4","O5","O6","O7","O8"]
jours = [f"Jour {i+1}" for i in range(10)]

total_prod_ouvrier = np.sum(m_carre, axis=1)
for i, total in enumerate(total_prod_ouvrier):
    print(f"Voici le total produit par ouvrier {ouvriers[i]}: {total_prod_ouvrier[i]}m²")

total_prod_jour = np.sum(m_carre, axis=0)
for i, total in enumerate(total_prod_jour):
    print(f"Voici le total produit par jour {jours[i]}: {total_prod_jour[i]}m²")

best_ouvrier = np.argmax(total_prod_ouvrier)
print(f"\n🏆 Meilleur ouvrier : {ouvriers[best_ouvrier]} ({total_prod_ouvrier[best_ouvrier]} m²)")

best_day = np.argmax(total_prod_jour)
print(f"📅 Jour le plus productif : {jours[best_day]} ({total_prod_jour[best_day]} m²)")

prod_total = np.sum(m_carre)
print(f"Les ouvriers, au total on fait {prod_total}m².")

part_ouvrier = (total_prod_ouvrier / prod_total) * 100
print("\nParts de chaque ouvrier dans la production totale :")
for i, part in enumerate(part_ouvrier):
    print(f"{ouvriers[i]} → {part:.1f}%")

moy_prod_ouvrier = (total_prod_ouvrier/prod_total)*100
for i, part in enumerate(moy_prod_ouvrier):
    print(f"{ouvriers[i]} → {part:.1f}% de la production totale")


journees_exeptionnelles = m_carre > 70
nombre_journees_ex = np.sum(journees_exeptionnelles)
print(f"Il y a eut {nombre_journees_ex} journées exeptionnelles au dessus de 70m².")

journees_minables = m_carre < 30
nombre_journees_min = np.sum(journees_minables)
print(f"Il y a eut {nombre_journees_min} journées minables en dessous de 30m².")


print(m_carre)


