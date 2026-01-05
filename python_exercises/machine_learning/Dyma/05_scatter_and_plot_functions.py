# =============================================================================
# Création de graphiques avec Pyplot
# =============================================================================
# Scatter et Plot

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 24, 1000)
y = np.sin(x)

plt.figure()
plt.scatter(x, y, marker="*", c="red")
plt.plot(x, y, linestyle="dashdot", c="blue")

plt.xlabel("Heure de la journée")
plt.ylabel("Productivité")

plt.title("Productivité au travail")

plt.grid(visible = True)