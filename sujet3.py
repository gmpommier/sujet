# Créé par GABRIEL.POMMIER, le 19/12/2023 en Python 3.7
#exercice 3.1
def moyenne(tab):
    somme = 0
    coeffs = 0
    for couple in tab:
        somme += couple[0] * couple[1]
        coeffs += couple[1]
    if coeffs == 0:
        return None
    return somme / coeffs

#exercice 3.2
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
    des " *" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(' *',end='')
            else:
                print('  ',end='')
        print()


def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
    élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois
    ET répétées k fois'''
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom
