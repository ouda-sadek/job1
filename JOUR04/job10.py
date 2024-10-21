def est_pair_ou_impair(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        return "Erreur : veuillez entrer un entier positif."
    
    if nombre % 2 == 0:
        return f"{nombre} est pair."
    else:
        return f"{nombre} est impair."


valeurs = [4, 7, -3, 10, 15, 0, 2.5, 8]

for val in valeurs:
    resultat = est_pair_ou_impair(val)
    print(resultat)
