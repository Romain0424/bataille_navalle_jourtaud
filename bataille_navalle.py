largeur = 10
hauteur = 5
j1_mer1 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j1_mer2 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j1_mer3 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j2_mer1 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j2_mer2 = [[' ' for i in range(hauteur)] for j in range(largeur)]
j2_mer3 = [[' ' for i in range(hauteur)] for j in range(largeur)]



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
