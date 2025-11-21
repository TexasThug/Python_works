import numpy as np 

temp = np.random.uniform(5,35,30)

bruit = np.random.normal(1,2,30)
temp_bruit = temp + bruit 

moyenne = np.mean(temp_bruit)
mediane = np.median(temp_bruit)
variance = np.var(temp_bruit)
max = np.max(temp_bruit)
min = np.min(temp_bruit)

canicule = temp_bruit[temp_bruit>30]
nombre_canicule = len(canicule)

print(f"Moyenne :{moyenne:.1f}C°")
print(f"Medane :{mediane:.1f}C°")
print(f"Variance :{variance:.1f}C°")
print(f"Température maximum :{max:.1f}C°")
print(f"Température minimum :{min:.1f}C°")
print(f"Journées au dessus de 30 degrés :{nombre_canicule:.1f}C°")
print(f" A quelle température ? :{canicule}C°")