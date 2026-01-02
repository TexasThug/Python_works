import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

teams = ["Nord", "Sud", "Est", "Ouest"]
months = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]

sales = np.random.randint(8000, 20000, (4, 6))

df = pd.DataFrame(sales, index=teams, columns=months)
print(df)

print("---1. Info---")
print(df.shape)
print(df.head(3))
print(df.columns)

print("---2. KPI---")
ventes_totales = df.values.sum()
print("Total de ventes :", ventes_totales, "€")
moyenne_ventes = df.values.mean()
print("Moyenne globale des ventes :", moyenne_ventes, "€")
std_total = df.values.std()
print("Ecart Type des ventes :", std_total, "€")

print("---3. Comparaisons clés---")
best_team = df.sum(axis=1).idxmax()
print("La meilleure équipe est : L'équipe", best_team)
best_month = df.sum(axis=0).idxmax()
print("Le meilleur mois est :", best_month)
equipe_la_plus_reguliere = df.std(axis=1).idxmin()
print("L'équipe la plus régulière est l'équipe :", equipe_la_plus_reguliere)
equipe_la_moins_performante = df.sum(axis=1).idxmin()
print("L'équipe la moins performante est l'équipe :", equipe_la_moins_performante)

print("---4. Visualisation---")

total_par_equipe = df.sum(axis=1)

plt.figure()
total_par_equipe.plot(kind="bar")

plt.title("Ventes totales par équipe")
plt.xlabel("Équipe")
plt.ylabel("Ventes (€)")

plt.show()

print("------------------------")

total_par_mois = df.sum(axis=0)

plt.figure()
total_par_mois.plot(kind="line", marker="o")

plt.title("Ventes totales par mois")
plt.xlabel("Mois")
plt.ylabel("Ventes (€)")

plt.show()

print("------------------------")

plt.figure()
plt.imshow(df)

plt.colorbar(label="Ventes (€)")
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.index)), df.index)

plt.title("Heatmap des ventes par équipe et par mois")
plt.show()


