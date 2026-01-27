stock = {"Jordan 1": 5, "Dunk Low": 2, "Air Max": 10}

def vendre_chaussure(modele):
    if modele in stock and stock[modele] > 0 : 
        stock[modele] -= 1
        return f"Vendu ! Il reste {stock[modele]} {modele}."
    else : 
        return f"Rupture de stock ou modele inconnu : {modele}"
print(vendre_chaussure("Jordan 1"))

def afficher_inventaire():
    print("--- INVENTAIRE ACTUEL ---")
    for modele, quantite in stock.items():
        print(f"{modele} : {quantite} paires en stock.")
    print("----------------------------")
afficher_inventaire()

stock = {"Jordan 1": 5, "Dunk Low": 2, "Air Max": 10}

def calculer_valeur_totale(prix_moyen):
    toutes_les_quantites = stock.values() 
    
    total_chaussures = sum(toutes_les_quantites)
    
    valeur_en_euros = total_chaussures * prix_moyen
    
    return valeur_en_euros

resultat = calculer_valeur_totale(100)
print(f"La valeur totale du stock est de : {resultat}€")