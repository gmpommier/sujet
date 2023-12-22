# Créé par GABRIEL.POMMIER, le 19/12/2023 en Python 3.7
#exercice 2.1
def indices_maxi(tab):
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
    for i in range(len(tab)):
        if tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)

#exercice 2.2
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1
