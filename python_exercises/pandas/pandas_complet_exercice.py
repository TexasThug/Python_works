import numpy as np
import pandas as pd 

noms = ["Alice", "Bob", "Charlie", "David", "Emma", "Fred", "Julie", "Léo", "Mia", "Noah"]

maths = np.random.randint(0, 21, 10)
physique = np.random.randint(0, 21, 10)
histoire = np.random.randint(0, 21, 10)

tableau = {
    "Nom" : noms,
    "Maths" : maths,
    "Physique" : physique,
    "Histoire" : histoire
}

df = pd.DataFrame(tableau)
print(df)

df["Moyenne"] = np.mean(df[["Maths", "Physique", "Histoire"]], axis = 1)

df = df.sort_values(by="Moyenne", ascending=False)
print(df)

moyenne_classe = np.mean(df["Moyenne"]) 
meilleur = df.loc[df["Moyenne"].idxmax()]
pire = df.loc[df["Moyenne"].idxmin()]


df["Statut"] = np.where(df["Moyenne"] >= 10, "Réussi", "Echec")


nb_reussite = len(df[df["Statut"] == "Réussi"])
nb_echec = len(df[df["Statut"] == "Echec"])


print("------ Résumé de la classe ------")
print(f"Moyenne de la classe : {moyenne_classe:.2f}/20")
print(f"Nombre de réussites : {nb_reussite}")
print(f"Nombre d'échecs : {nb_echec}")
print(f"Meilleur élève : {meilleur['Nom']} ({meilleur['Moyenne']:.2f}/20)")
print(f"Pire élève : {pire['Nom']} ({pire['Moyenne']:.2f}/20)")



