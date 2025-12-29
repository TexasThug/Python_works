import numpy as np
import pandas as pd

np.random.seed(123)
prod = np.random.randint(10, 160, (7, 15))   # 7 opérateurs × 15 jours

# Simule des valeurs manquantes (-1) et des outliers (9999)
prod[1, 3] = -1
prod[4, 8] = -1
prod[2, 10] = 9999
prod[6, 0] = 9999

print("Matrice brute :\n", prod)

operateurs = [f"OP{i+1}" for i in range(7)]
jours = [f"Jour {i+1}" for i in range(15)]

df_prod = pd.DataFrame(prod, index=operateurs, columns=jours)
print("\nTableau initial :")
print(df_prod)

# Masque des valeurs valides (pas -1 et pas outliers)
mask_valid = (prod != -1) & (prod < 1000)
prod_clean = prod.copy().astype(float)

# Calcul de la moyenne par opérateur (sur les valeurs valides)
moyennes = np.sum(prod_clean * mask_valid, axis=1) / np.sum(mask_valid, axis=1)

# Remplacer les -1 par la moyenne correspondante (broadcast ligne)
for i in range(prod.shape[0]):
    prod_clean[i, prod_clean[i] == -1] = moyennes[i]

print("\nAprès remplacement des -1 par la moyenne par opérateur :\n", prod_clean)

total_par_operateur = np.sum(prod_clean, axis=1)
total_par_jour = np.sum(prod_clean, axis=0)
moyenne_par_operateur = np.mean(prod_clean, axis=1)
ecart_type_par_operateur = np.std(prod_clean, axis=1)

best_op = np.argmax(total_par_operateur)
best_day = np.argmax(total_par_jour)

print("\n=== Statistiques ===")
print(f"🏆 Meilleur opérateur : {operateurs[best_op]} ({total_par_operateur[best_op]} unités)")
print(f"📅 Jour le plus productif : {jours[best_day]} ({total_par_jour[best_day]} unités)")

# Top 3 jours les plus productifs
indices_top3 = np.argsort(total_par_jour)[-3:][::-1]
top3_jours = [jours[i] for i in indices_top3]
print(f"\n🔥 Top 3 jours : {top3_jours}")

# Deux meilleurs jours par opérateur
top2_par_op = []
for i in range(prod_clean.shape[0]):
    top2 = np.argsort(prod_clean[i])[-2:][::-1]
    top2_par_op.append(top2)

print("\nMeilleurs jours par opérateur (indices) :")
for i, t in enumerate(top2_par_op):
    print(f"{operateurs[i]} → {t}")

# Normalisation z-score par opérateur
mean_row = np.mean(prod_clean, axis=1, keepdims=True)
std_row = np.std(prod_clean, axis=1, keepdims=True)
z = (prod_clean - mean_row) / std_row

# Score cumulé par opérateur
score_operateur = np.sum(z, axis=1)
classement = np.argsort(score_operateur)[::-1]

print("\nClassement par score normalisé :")
for i in classement:
    print(f"{operateurs[i]} → score {score_operateur[i]:.2f}")
    
# Cumul des totaux journaliers
cumul = np.cumsum(total_par_jour)
seuil = 0.4 * np.sum(total_par_jour)
jour_index_interior = np.where(cumul >= seuil)[0][0]

print(f"\n⚙️ Le cumul dépasse 40% du total au : {jours[jour_index_interior]}")
