#exercice 9.1
def multiplication(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    resultat = 0
    for _ in range(n2):
        resultat += n1
    return resultat

#exercice 9.2
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab) :
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if tab[m] < n :
        return chercher(tab, n, m+1 , j)
    elif tab[m] > n :
        return chercher(tab, n, i , m-1 )
    else :
        return m
