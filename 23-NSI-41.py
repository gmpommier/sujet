#monnaie_récursif
valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return #[]
    v = valeurs[rang]
    if v <= #a_rendre:
        return """[v]""" + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, #rang + 1)

print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291, 1))
"""
occurence
"""
def recherche(caractere, chaine):
    total = 0
    for c in chaine:
        if c == caractere:
            total += 1
    return total

print(recherche('e', "sciences"))
print(recherche('i', "mississippi"))
print(recherche('a', "mississippi"))