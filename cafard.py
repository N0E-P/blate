# Niveau 0
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