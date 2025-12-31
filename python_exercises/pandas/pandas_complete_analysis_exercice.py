import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(7)

teams = ["Nord", "Sud", "Est", "Ouest"]
months = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"]

sales = np.random.randint(5000, 20000, (4, 6))

df = pd.DataFrame(sales, index=teams, columns=months)
print(df)

print("---1. KPI de Base---")
print("---A. Ventes totales---")
print("---Ventes Totales par Equipe---")
print(df.sum(axis=1))
print("---Ventes Totales par Mois---")
print(df.sum(axis=0))
print("---Ventes Totales---")
total_ventes = df.values.sum()

print("---B. Moyennes---")
print("---Moyenne par Equipe ")
print(df.mean(axis=1).round(2))
print("---Moyenne par Mois ")
print(df.mean(axis=0).round(2))

print("---2. Performance---")
print("---A. Meilleurs Elements")
print("---Equipe la plus performante---")
best_team = df.sum(axis=1).idxmax()
best_team_total = df.sum(axis=1).max()
print(best_team, "->", best_team_total)
print("---Mois le plus performant---")
best_month = df.sum(axis=0).idxmax()
best_month_total = df.sum(axis=0).max()
print(best_month, "->", best_month_total)

print("---B. Stabilité---")
print(df.std(axis=1).round(2))
print(df.std(axis=1).idxmin(), "->", df.std(axis=1).min().round(2))

print("---3. Analyse par Seuil---")
total_mois = df.sum(axis=0)
mois_forts = total_mois[total_mois > 55000].index.tolist()
mois_faibles = total_mois[total_mois < 40000].index.tolist()
print("Mois forts :", mois_forts)
print("Mois faibles :", mois_faibles)

print("---4. Standardisation---")
moyenne_globale = df.values.mean()
print("Moyenne globale :",moyenne_globale.round(2))
std_global = df.values.std()
print("Ecart-type global :", std_global.round(2))
print("---DataFrame centré réduit :---")
df_standardized = (df - moyenne_globale) / std_global
print(df_standardized.round(2))

print("---5. Part Relative---")
part_par_equipe = (df.sum(axis=1) / total_ventes) * 100
print("Part de chaque équipe (%):")
print(part_par_equipe.round(2))


print("---6. Résumé---")
print("====== RÉSUMÉ VENTES ======")
print("🏆 Meilleure équipe :", best_team)
print("📈 Mois forts :", mois_forts)
print("📉 Mois faibles :", mois_faibles)
print("💰 Ventes totales :", total_ventes,"€.")
print("==========================")

print("---Visualisation---")
total_par_equipe = df.sum(axis=1)

plt.figure()
total_par_equipe.plot(kind="bar")
plt.title("Ventes totales par équipe")
plt.xlabel("Équipe")
plt.ylabel("Ventes (€)")
plt.show()

