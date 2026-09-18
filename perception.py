from memoire import actualiserCarte

#renvoie le contenu de la case a la position 'position'
def getCase(grille, position):
    return grille[position[0]][position[1]]

#renvoie ce que percoit l'agent a 1 case orthogonallement
def see(grille, position):
    posN= [position[0]-1, position[1]]
    posS= [position[0]+1, position[1]]
    posE= [position[0], position[1]+1]
    posO= [position[0], position[1]-1]
    charN=getCase(grille, posN)
    charS=getCase(grille, posS)
    charE=getCase(grille, posE)
    charO=getCase(grille, posO)
    actualiserCarte(posN, charN)
    actualiserCarte(posS, charS)
    actualiserCarte(posE, charE)
    actualiserCarte(posO, charO)
    return charN, charS, charE, charO