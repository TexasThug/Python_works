import numpy as np

# --- EXERCICE 1 : La Création manuelle ---
# 1.1 Crée un array 1D (vecteur) nommé 'vec' contenant les chiffres de 10 à 15.
vec = np.arange(10,16)
print(vec)
# 1.2 Crée un array 2D (matrice) nommé 'mat' de 2 lignes et 3 colonnes.
mat = np.random.rand(2,3)
print(mat)

# --- EXERCICE 2 : L'inspection (Le réflexe à avoir) ---
# Utilise des attributs NumPy (pas des fonctions) sur ta matrice 'mat' pour afficher :
# 2.1 Le nombre total d'éléments.
print("Nombre total d'éléments :",mat.size)
# 2.2 La forme (nombre de lignes, nombre de colonnes).
print("Forme de l'array :",mat.shape)
# 2.3 Le type de données stockées (int64, float64 ?).
print("Type de données :",mat.dtype)

# --- EXERCICE 3 : Les tableaux automatiques ---
# En IA, on initialise souvent des matrices de départ.
# 3.1 Crée un array de taille 10 rempli uniquement de zéros.
ar = np.zeros(10)
print(ar)
# 3.2 Crée une matrice 3x5 remplie uniquement de uns.
uno = np.ones((3,5))
print(uno)
# 3.3 Crée une matrice identité (1 en diagonale, 0 ailleurs) de taille 4x4.
identity = np.eye(4)
print(identity)

# --- EXERCICE 4 : La suite logique ---
# 4.1 Utilise une fonction spécifique pour créer un array de tous les entiers de 0 à 100 inclus.
# (Indice : c'est l'équivalent de range() en Python mais version NumPy).
ent = np.arange(0,101)
print(ent)

# --- EXERCICE 5 : Calcul vectoriel vs Listes ---
# 5.1 Crée a = np.array([1, 2, 3]) et b = np.array([10, 20, 30]).
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
# 5.2 Additionne-les (a + b) et affiche le résultat.
c = a + b 
print(c)
# 5.3 Multiplie 'a' par 2.
d = a * b
print(d)
# 5.4 Question en commentaire : Pourquoi NumPy est-il plus puissant qu'une liste [1,2,3] pour ces calculs ?