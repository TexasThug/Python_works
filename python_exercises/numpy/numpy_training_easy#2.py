import numpy as np

revenue = np.random.normal(2500, 600, 200)
nombre_revenue = len(revenue)

moyenne = np.mean(revenue)
mediane = np.median(revenue)
variance = np.var(revenue)
ecart_type = np.std(revenue)
revenue_max = np.max(revenue)
revenue_min = np.min(revenue)

revenue_sup = revenue[revenue>3000]
moyenne_revenue_sup = revenue_sup/len(revenue_sup)
nombre_revenue_sup = len(revenue_sup)
pourcentage_revenue_sup = (nombre_revenue_sup/ nombre_revenue)*100

bruit = np.random.normal(0,200,200)
revenus_bruit = bruit + revenue
moyenne_apres = np.mean(revenus_bruit)
ecart_type_apres = np.std(revenus_bruit)

print(f"Moyenne initale : {moyenne:.2f} €")
print(f"Moyenne après bruit : {moyenne_apres:.2f} €")
print(f"Ecart-type initale : {ecart_type:.2f} €")
print(f"Ecart-type après bruit : {ecart_type_apres:.2f} €")
print(f"Hauts revenus (>3000€) : {nombre_revenue_sup} ({pourcentage_revenue_sup}%)")
