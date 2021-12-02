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

    print("    0   1   2   3   4   5   6   7   8   9 ")
    l = ["A", "B", "C", "D", "E"]
    for j in range(hauteur):
        print(l[j] + "  ", end=" ")
        for i in range(largeur):
            print(mer[i][j] + " | ",end="")
        print(" ")


def verifier_case(x, y, mer, mers_adversaire):
    mer_initiale = mers_adversaire.index(mer)
    if mer[x][y] ==' ':
        if mers_adversaire[mer_initiale - 1][x][y] == ' ' or mers_adversaire[mer_initiale + 1][x][y] == ' ':
            mers_adversaire[mer_initiale - 1][x][y] = 'R'
            mers_adversaire[mer_initiale + 1][x][y] = 'R'
        print(mers_adversaire.index(mer))


def jouer_un_coup(joueur):
    if joueur == 1:
        nb_ocean = 1
    else:
        nb_ocean = 0
    print("\nVeuillez sélectionner la mer dans laquelle vous souhaitez tirer : ")
    nb_mer = input()
    mer = ocean[nb_ocean][int(nb_mer) - 1]
    mers_adversaire = ocean[nb_ocean]
    print("Voici la mer numéro {} de votre adversaire".format(nb_mer))
    afficher(mer)
    print("Veuillez choisir la case dans laquelle effectuer votre tir : ")
    print("Colonne ( Choix de 0 à 9 ! ) :")
    colonne = int(input())
    while colonne < 0 or colonne >= 9:
        print("Colonne ( Choix de 0 à 9 ! ) :")
        colonne = int(input())
    print("ligne ( Choix de A à E ! ) : ")
    ligne = input().upper()
    verifier_case(int(colonne), int(ligne), mer, mers_adversaire)
    try:
        mer[colonne][int(ligne) - 1] = 'R'
    except ValueError:
        mer[colonne][dic_colonne.get(ligne)] = 'R'

    afficher(mer)



jouer_un_coup(1)