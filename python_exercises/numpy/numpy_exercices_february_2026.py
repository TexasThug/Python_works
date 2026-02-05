import numpy as np

np.random.seed(42)
temperatures = np.random.uniform(10, 35, (30, 24))

temp_max_journaliere = temperatures.max(axis=1)
print(f"Max journalier (30 jours) : \n{temp_max_journaliere}")

haute_temperature = temperatures > 30
nb_occurrences = np.sum(haute_temperature) 

print(f"Nombre d'heures au-dessus de 30°C : {nb_occurrences}")

moyenne_globale = temperatures.mean()
temperatures_centrees = temperatures - moyenne_globale

print(f"Moyenne globale : {moyenne_globale:.2f}°C")
print(f"Nouvelle moyenne (doit être proche de 0) : {temperatures_centrees.mean():.2e}")