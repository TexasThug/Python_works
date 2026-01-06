import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(21)

teams = ["Nord", "Sud", "Est", "Ouest"]
months = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]

sales = np.random.randint(9000, 22000, (4, 6))

df = pd.DataFrame(sales, index=teams, columns=months)
print(df)

#1. Exploration données 
#Forme Df
print(df.shape)
#Print 2 premières lignes 
print(df.head(2))
#Noms des colonnes
print(df.columns)
#Noms des équipes
print(df.index)

#2. KPI Globaux 
#Total ventes 
ventes_totales = df.values.sum()
print("Ventes totales :", ventes_totales)

# Moyenne des ventes mensuelles globales
moyenne_ventes = df.values.mean()
print("Moyenne :", moyenne_ventes)

# Écart-type des ventes mensuelles globales
std_ventes = df.values.std() 
print("Écart-type :", std_ventes)

# 3. KPI par équipe et par mois
# Total des ventes par mois
ventes_mois = df.sum(axis=0)
print("Ventes par mois :", ventes_mois)

# Total des ventes par équipe
ventes_equipes = df.sum(axis=1)
print("Ventes par équipe :", ventes_equipes)

#Moyenne par équipe 
moyenne_equipe = df.mean(axis=1)
print("Moyenne par équipe :", moyenne_equipe)

# 4. Comparaison clés 
#Equipe la plus performante 
best_team = df.sum(axis=1).idxmax()
print("Best team :", best_team)

#Mois le plus performant 
worst_mois = df.sum(axis=0).idxmin()
print("Worst month : ", worst_mois)

#Equipe la plus régulière 
most_regular_team = df.std(axis=1).idxmin()
print("Most regular team : ", most_regular_team)

#Mois le plus performant 
best_month = df.sum(axis=0).idxmax()
print("Best Month : ", best_month)

# 5. Analyse par seuil 
#Meilleurs mois (> 65 000€)
good_months = ventes_mois[ventes_mois > 55000]
print("Good months :", good_months)

#Pire mois (< 60 000€)
bad_months = ventes_mois[ventes_mois < 45000]
print("Bad months :", bad_months)

# 6. Part Relative 
part_equipes = (ventes_equipes / ventes_totales) * 100
print("Part des ventes par équipe (%):")
print(part_equipes.round(2))

# 7. Visualitions 
# A. Bar Chart 
plt.figure()
ventes_equipes.plot(kind="bar")

plt.title("Ventes totales par équipe")
plt.xlabel("Équipe")
plt.ylabel("Ventes (€)")

plt.show()

# B. Line Chart 
plt.figure()
ventes_mois.plot(kind="line", marker = "x")

plt.title("Ventes totales par mois")
plt.xlabel("Mois")
plt.ylabel("Ventes(€)")
 
plt.show()

# C. Heatmap 
plt.figure()
plt.imshow(df)

plt.colorbar(label="Ventes (€)")
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.index)), df.index)

plt.title("Heatmap des ventes par équipe et par mois")
plt.show()

print("====== RÉSUMÉ VENTES ======")
print("🏆 Meilleure équipe : ", best_team )
print("📉 Moins performante : ...", worst_mois)
print("⚖️ Équipe la plus régulière : ...", most_regular_team)
print("📅 Meilleur mois : ...", best_month)
print("📈 Mois forts : ...", good_months)
print("📉 Mois faibles : ...", bad_months)
print("💰 Ventes totales : ...", ventes_totales)
print("==========================")
