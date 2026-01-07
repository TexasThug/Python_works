import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(33)

sites = ["Usine A", "Usine B", "Usine C", "Usine D"]
months = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]

production = np.random.randint(7000, 18000, (4, 6))

df = pd.DataFrame(production, index=sites, columns=months)
print(df)

#1. Exploration des données 
#Forme du Df
print(df.shape)
#2 première lignes 
print(df.head(2))
#colonnes
print(df.columns)
#noms usines 
print(df.index)

#2. KPI 
# Production totale 
total_production = df.values.sum()
print("Total production :", total_production,"€")

# Moyenne globale
moyenne_globale = df.values.mean()
print("Moyenne globale :", moyenne_globale,"€")

# Ecart-type global 
std_global = df.values.std().round(2)
print("Ecart-type global :", std_global,"€")

# KPI usine et mois 
# Production totale par usines 
prod_tot_usine = df.sum(axis=1)
print("Production totale par usine :", prod_tot_usine, "€")

# Production totale par mois 
prod_tot_mois = df.sum(axis=0).round(2)
print("Production totale par mois :", prod_tot_mois, "€")

# Moyenne par usines 
moyenne_usines = df.mean(axis=1).round(2)
print("Moyenne par usines :", moyenne_usines,"€")

# 4. Comparaison métiers 
# Usine la plus productive 
best_usine = df.sum(axis=1).idxmax()
print("La meilleure usine est l'usine :", best_usine, "€")

# Usine la moins productive 
worst_usine = df.sum().idxmin()
print("Pire usine :", worst_usine)

# Usine la plus stable 
most_stable_usine = df.std().idxmin()
print("Usine la plus stable :", most_stable_usine)

# Mois le plus productif 
best_month = df.sum(axis=0).idxmax()
print("Best month :", best_month)

# 5. Analyse par seuils
# Liste mois forts 
mois_forts = prod_tot_mois[prod_tot_mois > 49000]
print("Mois forts :", mois_forts)

# Liste mois faibles 
mois_faibles = prod_tot_mois[prod_tot_mois<40000]
print("Mois faibles :", mois_faibles)

# 6. Standardisation
# écart-type global
std_global = df.values.std()

# DataFrame centré-réduit
df_standardized = (df - moyenne_globale) / std_global

# Affichage arrondi
print(df_standardized.round(2))

# 7. Part relative (%)
# Part de chaque usine
part_usine = (df.sum(axis=1) / total_production) * 100

# Affichage arrondi
print(part_usine.round(2))

# 8. Visualisation
# Boxplot
plt.figure()
df.boxplot(column = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"])
plt.show()

plt.figure()
df.boxplot(column = ["Usine A", "Usine B", "Usine C", "Usine D"])  
plt.show()

