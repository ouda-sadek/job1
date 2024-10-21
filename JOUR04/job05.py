def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        return num1 % num2
    else:
        return "Erreur : Opérateur non valide"


resultat = calcule(5, '+', 2)
print(resultat) 

resultat = calcule(5, '*', 2)
print(resultat) 

resultat = calcule(5, '/', 2)
print(resultat) 

resultat = calcule(5, '/', 0)
print(resultat) 
