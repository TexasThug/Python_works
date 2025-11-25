import numpy as np 

np.random.seed(42)
vitesses = np.random.uniform(80, 150, 50)

moyenne = np.mean(vitesses)
mediane = np.median(vitesses)
ecart_type = np.std(vitesses)
variance = np.var(vitesses)
vitesse_max = np.max(vitesses)
vitesse_min = np.min(vitesses)
print("------------------------")
print(f"Moyenne : {moyenne:.1f} km/h")
print(f"Médiane : {mediane:.1f} km/h")
print(f"Variance : {variance:.1f}")
print(f"Écart-type : {ecart_type:.1f}")
print(f"Max : {vitesse_max:.1f} km/h")
print(f"Min : {vitesse_min:.1f} km/h")

limite = 130
exces = vitesses[vitesses>limite]
nombre_exces = len(exces)
pourcentage_exces = (len(exces) / len(vitesses)) * 100
print(pourcentage_exces)

if pourcentage_exces > 30: 
    print("Alerte !")
else : 
    print("Résultat satisfaisant.")

bruit_aleatoire = np.random.normal(0, 1, 50)
vitesse_bruit= vitesses + bruit_aleatoire

moyenne_apres = np.mean(vitesse_bruit)
mediane_apres = np.median(vitesse_bruit)
ecart_type_apres = np.std(vitesse_bruit)
variance_apres = np.var(vitesse_bruit)
vmax_apres = np.max(vitesse_bruit)
vmin_apres = np.min(vitesse_bruit)
categories = np.where(vitesse_bruit <= 130, "normal", "exces")

print("---------Vitesse_apres_bruit------------")
print(f"Moyenne : {moyenne_apres:.1f} km/h")
print(f"Médiane : {mediane_apres:.1f} km/h")
print(f"Variance : {variance_apres:.1f}")
print(f"Écart-type : {ecart_type_apres:.1f}")
print(f"Max : {vmax_apres:.1f} km/h")
print(f"Min : {vmin_apres:.1f} km/h")

trie_apres = np.sort(vitesse_bruit)
meilleures = trie_apres[:5]
pires = trie_apres[-5:] 














