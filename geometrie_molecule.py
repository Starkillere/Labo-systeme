#-*- coding:utf-8 -*-

__alle__ = ['molecule_geometrie_is', 'configuration_electronique']

def molecule_geometrie_is(nb_doublets_liant:int, nb_doublets_non_liant:int) -> str:
    assert type(nb_doublets_liant) == int
    assert type(nb_doublets_non_liant) == int

    if (nb_doublets_liant+nb_doublets_non_liant) == 4:
        if nb_doublets_non_liant == 2:
            return 'Coudée'
        elif nb_doublets_non_liant == 1:
            return 'Pyramidale à base triangulaire'
        elif nb_doublets_non_liant == 0:
            return 'Tétraédrique'   
    elif (nb_doublets_liant+nb_doublets_non_liant) == 3:
        return 'Triangulaire plane'
    elif (nb_doublets_liant+nb_doublets_non_liant) == 2:
        return 'Linéaire'
    else:
        return 'Géometrie inconnue !'

def configuration_electronique(nb_electron:int) -> str:
    assert type(nb_electron) == int

    couches = ['1s', '2s', '2p', '3s', '3p']
    capacite = [2,2,6,2,6]
    pos = 0
    configuration = ''
    while nb_electron > 0:
        value =  min(nb_electron, capacite[pos])
        configuration += couches[pos]+'^'+str(value)+'; '
        nb_electron -= value
        pos += 1
    return configuration

def main():
    texte = "Bienvenue sur Atomes-Station! Un micro logiciele qui te donne la géometrie d'une molécule en fonction du nombre de doublets liants et non liants autour de l'atome centrale.Elle te permet aussi de connaitre la configuration électronique d'un atome.Saisir 1 pour le mode géométrie molécule ! Saisir 2 pour le mode configuration électronique!"
    texte_format = ""
    compteur = 0
    for i in range(len(texte)):
        compteur += 1
        if compteur ==  32 or texte[i] in ['.', '!', '?']:
            compteur = 0
            if texte[i] != ' ':
                texte_format += texte[i]+'\n'
            else:
                texte_format += '\n'
        else:
            texte_format += texte[i]
    print(texte_format)
    mode = int(input('\n-->'))
    if mode == 1:
        print('\nmode géométrie molécule\nIndication:\nles liaisons (double, triples ou quadriple) compteront comme\ndes liaisons simplet (un doublets liant).')
        nb_doublets_liants =  int(input('\nNombre de doublets liants: '))
        nb_doublets_non_liants =  int(input('\nNombre de doublets Non liants: '))
        print('\nLa géometrie de cette molécule est : \n'+molecule_geometrie_is(nb_doublets_liants, nb_doublets_non_liants))
    elif  mode == 2:
        z =  int(input("\nNombre d'éléctrons: "))
        print(configuration_electronique(z))
if __name__ == '__main__':
    main()