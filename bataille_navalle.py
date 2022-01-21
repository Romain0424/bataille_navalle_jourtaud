dic_colonne = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4}
largeur = 10
hauteur = 5
j1_mer1 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j1_mer2 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j1_mer3 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j2_mer1 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j2_mer2 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j2_mer3 = [[' ' for i in range(hauteur)] for j in range(largeur)]

mers_j1 = [j1_mer1, j1_mer2, j1_mer3]
mers_j2 = [j2_mer1, j2_mer2, j2_mer3]
ocean = [mers_j1, mers_j2]


def afficher(mer):
    print("mer : \n")
    print("    0   1   2   3   4   5   6   7   8   9 ")
    l = ["A", "B", "C", "D", "E"]
    for j in range(hauteur):
        print(l[j] + "  ", end=" ")
        for i in range(largeur):
            print(mer[i][j] + " | ",end="")
        print(" ")


def get_mers_joueur(joueur):
    if joueur == 1:
        return mers_j1
    else:
        return mers_j2


def get_mers_adversaire(joueur):
    if joueur == 1:
        return mers_j2
    else:
        return mers_j1


def positionner_les_bateaux(joueur):
    print("Joueur " + str(joueur) + " à vous de positionner vos bateaux \n")
    mers = get_mers_joueur(joueur)

    for i in (1, 2, 3):
        numeroMer = 0

        while not (numeroMer <= 3 and numeroMer >= 1):
            print(
                " \n Veuillez rentrer votre mer de 1 à 3 (mer1 = profondeur de 100 mètres) (mer2 = profondeur de 200 mètres) (mer3 = profondeur de 300 mètres)")
            numeroMer = int(input())
        mer = mers[numeroMer - 1]

        afficher(mer)

        position = ''
        print("Vous allez positionner votre bateau de taille " + str(i))
        while not (position == 'H' or position == 'V'):
            print(" \n Veuillez rentrer H pour le poser horizontalement ou V pour le poser verticalement")
            position = input().upper()

        if (position == 'H'):
            print(" \n Vous allez positionner votre bateau horizontalement choisissez la mer où le positionner")
            result = False
            while result == False:
                x = -1
                while not (x < 10 - (i - 1) and x >= 0):
                    print(" \n Veuillez saisir les coordonnées du début du bateau en x de 0 à 9")
                    x = int(input())
                y = -1
                while not (y >= 0 and y < 5):
                    print(" \n Veuillez saisir les coordonnées du début du bateau en x de A à E")
                    y = int(input())
                temp = True
                for j in range(i):
                    if mer[x + j][y] == 'S':
                        temp = False
                result = temp
                if temp == False:
                    print("Il y'a un bateau sous l'emplacement choisi")
                    afficher(mer)

            for j in range(i):
                mer[x + j][y] = 'S'

        if (position == 'V'):
            print(" \n Vous allez positionner votre bateau verticalement choisissez la mer où le positionner")
            result = False
            while result == False:
                x = -1
                while not (x < 10 and x >= 0):
                    print(" \n Veuillez saisir les coordonnées du début du bateau en x de 0 à 9")
                    x = int(input())
                y = -1
                while not (y >= 0 and y < 5 - (i - 1)):
                    print(" \n Veuillez saisir les coordonnées du début du bateau en x de A à E")
                    y = int(input())
                temp = True
                for j in range(i):
                    if mer[x][y + j] == 'S':
                        temp = False
                result = temp
                if temp == False:
                    print("Il y'a un bateau sous l'emplacement choisi")
                    afficher(mer)

            for j in range(i):
                mer[x][y + j] = 'S'

def remplir_annexe(mer,x,y):
    try:
        if mer[x + 1][y] == ' ':
            mer[x+1][y] = 'R'
    except IndexError:
        pass
    if mer[x - 1][y] == ' ':
        if (x == 0):
            mer[x-1][y] = ' '
        else:
            mer[x - 1][y] = 'R'
    try:
        if mer[x][y + 1] == ' ':
            mer[x][y +1] = 'R'
    except IndexError:
        pass
    if mer[x][y - 1] == ' ':
        if x == 9 and y == 5:
            mer[x][y-1] = ' '
        else:
            mer[x][y - 1] = 'R'


def remplir_mer(mer_initiale, mer_annexe,x ,y):
    if mer_initiale[x][y] == ' ':
        mer_initiale[x][y] = 'R'
        remplir_annexe(mer_initiale,x,y)
        #remplir_annexe(mer_annexe,x,y) #Probablement à supprimer ( à avoir selon l'évolution de la fonction)
        if mer_annexe[x][y] == ' ':
            mer_annexe[x][y] = 'R'
        else:
            a = 1
            #mer_annexe[x][y] = 'V'



def verifier_case(x, y, mer, mers_adversaire):
    mer_initiale = mers_adversaire.index(mer)
    deuxiezme_mere = mer_initiale + 1
    #print("ceuczuudzudz {}".format(mers_adversaire.index(deuxiezme_mere)))
    #print("INDICE MER : {} ".format(mer_initiale))
    remplir_mer(mer,mers_adversaire[deuxiezme_mere] ,x,y)
    #remplir_mer(mer, mers_adversaire[mer_initiale + 1], x, y)
    """if mer[x][y] == ' ':
        if mers_adversaire[mer_initiale - 1][x][y] == ' ':
            mers_adversaire[mer_initiale - 1][x][y] = 'R'
        if mers_adversaire[mer_initiale + 1][x][y] == ' ':
            mers_adversaire[mer_initiale + 1][x][y] = 'R'
        if mers_adversaire[mer_initiale - 1][x][y] == 'S':
            mers_adversaire[mer_initiale-1][x][y] = 'V'
        if mers_adversaire[mer_initiale + 1][x][y] == 'S':
            mers_adversaire[mer_initiale + 1][x][y] = 'V'"""
    print(mers_adversaire.index(mer))


def jouer_un_coup(joueur):
    if joueur == 1:
        nb_ocean = 1
    else:
        nb_ocean = 0
    print("\nVeuillez sélectionner la mer dans laquelle vous souhaitez tirer : ")
    nb_mer = int(input()) - 1
    mer = ocean[nb_ocean][int(nb_mer)]
    mers_adversaire = ocean[nb_ocean]
    #print("Voici la mer numéro {} de votre adversaire".format(nb_mer))
    #afficher(mer)
    print("Veuillez choisir la case dans laquelle effectuer votre tir : ")
    print("Colonne ( Choix de 0 à 9 ! ) :")
    colonne = int(input())
    while colonne < 0 or colonne > 9:
        print("Colonne ( Choix de 0 à 9 ! ) :")
        colonne = int(input())
    print("ligne ( Choix de A à E ! ) : ")
    ligne = input().upper()

    try:
        mer[colonne][int(ligne) - 1] = 'R'
        true_ligne = ligne
    except ValueError:
        true_ligne = dic_colonne[ligne]
        #mer[colonne][true_ligne] = 'R'
    verifier_case(int(colonne), int(true_ligne), mer, mers_adversaire)
    afficher(mer)


#positionner_les_bateaux(1)
#positionner_les_bateaux(2)

jouer_un_coup(1)
afficher(ocean[1][1])
afficher(ocean[1][2])