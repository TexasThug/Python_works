import numpy as np

# --- EXERCICE 1 : Le Slicing (Découpage) ---
# 1.1 Crée un vecteur 'v' contenant les entiers de 0 à 9.
v = np.arange(0,10)
print(v)
# 1.2 Affiche les éléments de l'index 3 à 7 (inclus).
print(v[3:8])
# 1.3 Affiche les éléments de 'v' dans l'ordre inverse (astuce : [::-1]).
print(v[::-1])

# --- EXERCICE 2 : Le Slicing 2D (Cœur de l'analyse de données) ---
# Soit la matrice suivante :
m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# 2.1 Récupère la deuxième ligne (index 1).
print(m[1])
# 2.2 Récupère la troisième colonne (toutes les lignes, index 2).
print(m[:,2])
# 2.3 Récupère le bloc de 2x2 en haut à gauche (lignes 0-1, col 0-1).
print(m[0:2, 0:2])

# --- EXERCICE 3 : Le Masquage Booléen (Filtrage) ---
# 3.1 Crée un array 'notes' avec ces valeurs : [8, 12, 18, 9, 15, 2, 20].
notes = np.array([8, 12, 18, 9, 15, 2, 20])
# 3.2 Crée un nouveau tableau 'rattrapage' qui ne contient que les notes < 10.
rattrapage = notes [notes < 10]
print( rattrapage)
# 3.3 Remplace toutes les notes < 10 par la valeur 0 dans le tableau d'origine.
notes[notes < 10] = 0
print(notes)

# --- EXERCICE 4 : Statistiques et Agrégation ---
# 4.1 Crée une matrice 3x3 remplie de nombres aléatoires entre 0 et 50.
np.random.seed(42)
matrice = np.random.randint(0,50,(3,3))
print(matrice)
# 4.2 Calcule la moyenne de TOUTE la matrice.
moyenne = matrice.mean()
print(moyenne)
# 4.3 Calcule la somme de chaque colonne (indice : axis=0).
somme_colonnes = matrice.sum(axis=0)
print(somme_colonnes)
# 4.4 Trouve la valeur maximale de chaque ligne (indice : axis=1).
max_value_lines = matrice.max(axis=1)
print(max_value_lines)

# --- EXERCICE 5 : La "Data Augmentation" simple ---
# 5.1 Crée un array de 5 images factices (juste des nombres) : img = np.array([1, 2, 3, 4, 5])
img = np.array([1, 2, 3, 4, 5])
# 5.2 Normalise cet array pour que ses valeurs soient comprises entre 0 et 1.
img_normalisee = (img - img.min()) / (img.max() - img.min())
print(img_normalisee)