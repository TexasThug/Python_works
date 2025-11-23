import numpy as np 

vitesses = np.random.randint(80, 150, 50)

bruit = np.random.randint(0, 5, 50)
vitesses_bruit = vitesses + bruit
print(vitesses_bruit)

moyenne_vitesse = np.mean(vitesses_bruit)
mediane_vitesse = np.median(vitesses_bruit)
variance_vitesse = np.var(vitesses_bruit)
vitesse_max = np.max(vitesses_bruit)
vitesse_min = np.min(vitesses_bruit)

exces = vitesses_bruit[vitesses_bruit > 130]
nombre_exces = len(exces)
moyenne_exces = np.mean(exces) if nombre_exces > 0 else 0

categories = np.where(
    vitesses_bruit > 130, "🚨 En excès",
    np.where(vitesses_bruit >= 110, "⚡ Rapide", "✅ Normal")
)
print("----------------------------------------")
print(f"Moyenne des vitesses : {moyenne_vitesse:.1f}km/h.")
print(f"Médiane des vitesses : {mediane_vitesse:.1f}km/h.")
print(f"Variance des vitesses : {variance_vitesse:.1f}km/h.")
print(f"Vitesse Maximum : {vitesse_max:.1f}km/h.")
print(f"Vitesse Minimum : {vitesse_min:.1f}km/h.")
print(f"Nombre d'exces : {nombre_exces}")
print(f"Moyenne des exces : {moyenne_exces:.1f}km/h.")
