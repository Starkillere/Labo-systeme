# Déclaration

complex_num:list = [int, float, complex]

class Complex:
    pass

class MatriceCarree(Complex):
    pass

class Matrice:
    pass

def somme(mat:list[Matrice]) -> Matrice:
    pass

def produit_s(mat:Matrice, scal:complex) -> Matrice:
    pass

def produit_m(mat:list[Matrice]) -> Matrice:
    pass


# Définition

class Matrice:
    """
        Objet Matrice 
    """
    
    def __init__(self, ligne:int, colonne:int) -> None:

        """

        """

        assert type(ligne) == int
        assert type(colonne) == int
        assert ligne >= 1
        assert colonne >= 1

        self.__ligne:int = ligne
        self.__colonne:int = colonne

        self.__matrice:list =  self.__creematrice()

    def __creematrice(self) -> list:
        return [[0 for j in range(self.__colonne)] for i in range(self.__ligne)]
    
    def __repr__(self) -> str:
        return f"{self.__matrice}"
    
    def __str__(self) -> str:
        return f"{self.__matrice}"
    
    def taille(self) -> tuple:
        return (self.__ligne, self.__colonne)
    
    def elmt(self, ligne:int, colonne:int) -> complex:

        assert self.__ligne >= ligne >= 1
        assert self.__colonne >= colonne >= 1

        return self.__matrice[ligne-1][colonne-1]

    def modifier(self, ligne:int, colonne:int, val:complex) -> None:
        
        assert type(val) in complex_num
        assert type(ligne) == int
        assert type(colonne) == int
        assert self.__ligne >= ligne >= 1
        assert self.__colonne >= colonne >= 1

        self.__matrice[ligne-1][colonne-1] = val

    def matrice_extraite(self, lignes:list[int], colonnes:list[int]) -> Matrice:
        
        assert type(lignes) == list and len([m for m in lignes if type(m) == int and self.__ligne >= m >= 1]) == len(lignes)
        assert type(colonnes) == list and len([m for m in colonnes if type(m) == int and self.__colonne >= m >= 1]) == len(colonnes)
        
        extract:Matrice =  Matrice(self.__ligne-len(lignes), self.__colonne-len(colonnes))

        count_ligne:int = 1
        for i in [lign for lign in range(self.__ligne) if not lign in [h-1 for h in lignes]]:
            count_colonne:int = 1
            for j in [col for col in range(self.__colonne) if not col in [h-1 for h in colonnes]]:
                extract.modifier(count_ligne, count_colonne, self.__matrice[i][j])
                count_colonne += 1
            count_ligne += 1

        return extract
    
    def transposee(self) -> Matrice:

        mat_transposee:Matrice =  Matrice(self.__colonne, self.__ligne)

        for i in range(self.__colonne):
            for j in range(self.__ligne):
                mat_transposee.elmt(i,j, self.__matrice(j,i))

        return mat_transposee
    
    def transvection_ligne(self, i:int, j:int, scal:complex) -> Matrice:

        assert self.__ligne >= i >= 1
        assert self.__ligne >= j >= 1
        assert i != j
        assert type(scal) in complex_num

        mat:Matrice = Matrice(self.__ligne, self.__colonne)

        for k in range(1, self.__ligne+1):
            for p in range(1, self.__colonne+1):
                if k == i:
                    mat.modifier(k, p, self.__matrice(k,p) + scal*self.__matrice(j, p))
                else:
                    mat.modifier(k, p, self.__matrice(k, p))
        
        return mat
    
    def dilatation_ligne(self, i:int, scal:complex):

        assert self.__ligne >= i >= 1
        assert type(scal) in complex_num

        mat:Matrice = Matrice(self.__ligne, self.__colonne)

        for k in range(1, self.__ligne+1):
            for p in range(1, self.__colonne+1):
                if p == i:
                    mat.modifier(k, p, self.__matrice(k,p) + scal*self.__matrice(k, i))
                else:
                    mat.modifier(k, p, self.__matrice(k, p))
        
        return mat
    
class MatriceCarree(Complex):

    """
    """

    def __init__(self) -> None:
        super().__init__()
    

                    
def somme(mat:list[Matrice]) -> Matrice:
    
    """
    """

    assert [type(m) for m in mat].count(Matrice) == len(mat)
    assert [m.taille() for m in mat].count(mat[0].taille()) == len(mat)

    mat_somme:Matrice =  Matrice(mat[0].taille()[0], mat[0].taille()[1])
    
    for i in range(1, mat[0].taille()[0]+1):
        for j in range(1, mat[0].taille()[1]+1):
            mat_somme.modifier(i,j, sum([m.elmt(i,j) for m in mat]))
    
    return mat_somme


def produit_s(mat:Matrice, scal:complex) -> Matrice:

    """
    """

    assert type(mat) ==  Matrice and type(scal) in complex_num
    
    produit:Matrice = Matrice(mat.taille()[0], mat.taille()[1])

    for i in range(1, mat.taille()[0]+1):
        for j in range(1, mat.taille()[1]+1):
            produit.modifier(i,j, mat.elmt(i, j))

    return produit

def produit_m(mat:list[Matrice]) -> Matrice:

    """
    """

    assert type(mat) == list and len(mat) > 0
    assert [type(m) for m in mat].count(Matrice) == len(mat)

    def produit_m_casbase(matA:Matrice, matB:Matrice) -> Matrice:

        """
        """

        assert type(matA) == Matrice and type(matB) == Matrice
        assert matA.taille()[1] == matB.taille()[0]

        produit:Matrice = Matrice(matA.taille()[0], matB.taille()[1])

        for i in range(1, matA.taille()[0]+1):
            for j in range(1, matB.taille()[1]+1):
                produit.modifier(i, j, sum([matA.elmt(i,k)*matB.elmt(k,j) for k in range(1, matA.taille()[1]+1)]))
        
        return produit
        
    if len(mat) == 2:
        return produit_m_casbase(mat[0], mat[1])
    else:
        if len(mat)%2 == 0:
            return produit_m([produit_m([m for m in range(len(mat)/2)]), produit_m([m for m in range((len(mat)/2)+1, len(mat))])])
        else:
            return produit_m([produit_m([m for m in range(len(mat)-1)]), mat[0]])
    


if __name__ ==  '__main__':
    matA =  Matrice(1, 3)
    matB =  Matrice(3, 1)
    print(matA.taille()[1], matB.taille()[0])
    matA.modifier(1,1, 1)
    matB.modifier(1,1, 1)
    matA.modifier(1, 2, 2)
    matB.modifier(2, 1, 2)
    matA.modifier(1, 3, 3)
    matB.modifier(3, 1, 3)

    print(f"A = {matA}\nB = {matB}")
    print(f"A*B = {produit_m([matA, matB])}")
    print(f"B*A = {produit_m([matB, matA])}")