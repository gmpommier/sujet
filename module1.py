# inversion de caractère
"""
def inverser_chaine(chaine):
    chaine_inverse = chaine[::-1]
    return chaine_inverse

chaine_originale = "chevalerie"
chaine_inverse = inverser_chaine(chaine_originale)
print(chaine_inverse)
"""
#pgdc
"""
def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

nombre1 = 24
nombre2 = 36
resultat = pgcd(nombre1, nombre2)
print("Le PGCD de", nombre1, "et", nombre2, "est", resultat)
"""