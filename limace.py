# Niveau 1
file = open("usine_i.txt", "r")
lignes = file.readlines()
file.close()

nbUsines = int(lignes[0].split()[0])
nbEntrepots = int(lignes[0].split()[1])

matriceCouts = lignes[1:-2]
matriceCouts = [[int(c) for c in ligne.split()] for ligne in matriceCouts]

listeDemandesEntrepots = lignes[-2].split()
listeDemandesEntrepots = [int(c) for c in listeDemandesEntrepots]

listeOffresUsines = lignes[-1].split()
listeOffresUsines = [int(c) for c in listeOffresUsines]

print (nbUsines)  
print (nbEntrepots)
print (matriceCouts)
print (listeDemandesEntrepots)
print (listeOffresUsines)

# Tant qu'il reste des pièces à livrer 
matricePiecesLivrees = [[0 for i in range(nbUsines)] for j in range(nbEntrepots)]
while (sum(listeDemandesEntrepots) > 0):
    # Trouver le couple (ligne de montage, magasin de stockage) avec le cout le plus petit
    coutMin = 1000000000
    couple = [0, 0]
    for i in range(nbEntrepots):
        for j in range(nbUsines):
            if (matriceCouts[i][j] < coutMin and matriceCouts[i][j] != -1):
                coutMin = matriceCouts[i][j]
                couple = [i, j]

    # Si l'usine a plus de pièces que l'entrepot en demande
    if (listeOffresUsines[couple[1]] > listeDemandesEntrepots[couple[0]]):
        print ("L'usine", couple[1], "livre", listeDemandesEntrepots[couple[0]], "pièces à l'entrepot", couple[0])
        matricePiecesLivrees[couple[0]][couple[1]] = listeDemandesEntrepots[couple[0]]
        listeOffresUsines[couple[1]] -= listeDemandesEntrepots[couple[0]]
        listeDemandesEntrepots[couple[0]] = 0
        for i in range(nbUsines):
            matriceCouts[couple[0]][i] = -1
    
    # Si l'usine a moins de pièces que l'entrepot en demande
    elif (listeOffresUsines[couple[1]] < listeDemandesEntrepots[couple[0]]):
        print ("L'usine", couple[1], "livre", listeOffresUsines[couple[1]], "pièces à l'entrepot", couple[0])
        matricePiecesLivrees[couple[0]][couple[1]] = listeOffresUsines[couple[1]]
        listeDemandesEntrepots[couple[0]] -= listeOffresUsines[couple[1]]
        listeOffresUsines[couple[1]] = 0
        for i in range(nbEntrepots):
            matriceCouts[i][couple[1]] = -1
        
    # Si l'usine a autant de pièces que l'entrepot en demande
    else:
        print ("L'usine", couple[1], "livre", listeOffresUsines[couple[1]], "pièces à l'entrepot", couple[0])
        matricePiecesLivrees[couple[0]][couple[1]] = listeOffresUsines[couple[1]]
        listeDemandesEntrepots[couple[0]] = 0
        listeOffresUsines[couple[1]] = 0
        for i in range(nbEntrepots):
            matriceCouts[i][couple[1]] = -1
        for i in range(nbUsines):
            matriceCouts[couple[0]][i] = -1

print (matricePiecesLivrees)
