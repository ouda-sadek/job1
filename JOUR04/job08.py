def My_primeur(type, saison):

    if type == "fruits" and saison == "hiver":
        return ("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "été":
        return ("Poire, fraise, cassis")

    elif type == "légume" and saison == "hiver":
        return ("carotte, topinambour, endive")

    elif type == "légume" and saison == "été":
        return ("artichaut, aubergine,navet")

print(My_primeur("fruits", "été"))
print(My_primeur("fruits", "hiver"))