# Création de graphiques avec Pyplot
# =============================================================================
# Histogramme
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

men_salaries = [61, 74, 54, 45, 47, 56, 57, 68, 70, 43, 55, 59, 56, 64]
women_salaries = [59, 76, 46, 49, 51, 68, 67, 62, 63, 72, 55, 49, 46, 52]

plt.figure()
plt.hist([men_salaries, women_salaries], rwidth=0.95, bins=[40,50,60,70,80], label=["Hommes", "Femmes"], color=["blue", "purple"])

plt.xlabel("Salaires en k€")
plt.ylabel("Fréquence")
plt.legend()

# =============================================================================
# Pie chart
# =============================================================================

plt.figure()
labels = ["Chaussures", "Vestes", "Pantalons", "Sous-vêtements"]
values = [53, 20, 15, 42]

plt.pie(values, labels = labels)


# =============================================================================
# Subplotting
# =============================================================================

x = np.linspace(0,10,1000)

# Plot 1
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.subplot(2,2,1)
plt.plot(x, y1, label="Sinus")
plt.plot(x, y2, label="Cosinus")
plt.legend()

# Plot 2
y3 = x**2
y4 = -x**2+10

plt.subplot(2,2,2)
plt.plot(x, y3, label="Parabole 1")
plt.plot(x, y4, label="Parabole 2")
plt.legend()

# Plot 3
y1 = np.exp(x)
y2 = x**4

plt.subplot(2,2,3)
plt.plot(x, y1, label="Exponentielle")
plt.plot(x, y2, label="X puissance 4")
plt.legend()

# Plot 4
y3 = 2*x**2
y4 = 2*x**2-30

plt.subplot(2,2,4)
plt.plot(x, y3, label="Parabole 3")
plt.plot(x, y4, label="Parabole 4")
plt.legend()
