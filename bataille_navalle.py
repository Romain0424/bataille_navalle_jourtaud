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
    for i in range(largeur):
        for j in range(hauteur):
            mer[i][j] = 'x'
    print("mer 1 : \n")
    print("    0   1   2   3   4   5   6   7   8   9 ")
    l = ["A", "B", "C", "D", "E"]
    for j in range(hauteur):
        print(l[j] + "  ", end=" ")
        for i in range(largeur):
            print(mer[i][j] + " | ",end="")
        print(" ")

def jouer_un_coup(joueur):
    if joueur == 1:
        nb_ocean = 1
    else:
        nb_ocean = 0
    print("\nVeuillez sélectionner la mer dans laquelle vous souhaitez tirer : ")
    nb_mer = input()
    mer = ocean[nb_ocean][int(nb_mer) - 1]
    afficher(mer)
    #print(nb_mer)


jouer_un_coup(1)