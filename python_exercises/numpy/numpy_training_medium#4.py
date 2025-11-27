import numpy as np 

np.random.seed(42)
production = np.random.randint(50,300,(6,7))
print(production)

cultures = ["Tomates", "Carottes", "Pommes", "Salades", "Courgettes", "Fraises"]
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

total_hebdomadaire = np.sum(production, axis=1)
for i, total in enumerate(total_hebdomadaire):
    print(f"Total hebdomadaire : {cultures[i]} : {total_hebdomadaire[i]}")

moyenne_quotidienne = np.mean(production, axis=1)
for i, total in enumerate(moyenne_quotidienne):
    print(f"Moyenne quotidienne : {cultures[i]} : {moyenne_quotidienne[i]:.1f}")

total_journalier_ferme = np.sum(production, axis=0)
for i, jour in enumerate(total_journalier_ferme):
    print(f"La ferme ramasse {total_journalier_ferme[i]} le {jours[i]} ")

j_max = np.argmax(total_journalier_ferme)
print(f"Le jour le plus productif est le {jours[j_max]}")

j_min = np.argmin(total_journalier_ferme)
print(f"Le jour le plus productif est le {jours[j_min]}")

culture_max = np.argmax(total_hebdomadaire)
print(f"La culture la plus récolté dans une semaine est : {cultures[culture_max]} ({production[culture_max]})")

total_par_culture = np.sum(production, axis=1)
total_global = np.sum(total_hebdomadaire)
part_production_total = (total_par_culture/total_global)*100
print(part_production_total)

print("Par de chaque culture dans la production totale : ")
for i, total in enumerate(part_production_total):
    print(f"{cultures[i]} représente : {part_production_total[i]:.1f}% de la part total.")

jours_exeptionnels = production > 250
nombre_jours_expetionnels = np.sum(jours_exeptionnels) 
print(f"Il y a eut {nombre_jours_expetionnels} jours où la récolte journalière a accédée 250kgs.")

jours_minables = production < 100
nombres_jours_minables = np.sum(jours_minables)
print(f"Il y a eut {nombres_jours_minables} jours où la récolte n'a pas dépassée 100kgs.")



