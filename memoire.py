#a finir
class memoire:
    def __init__(self):
        carte= []

    #initialisation de la taille de la carte
    def initCarte(self, hauteur, largeur, position_depart):
        self.carte= [("." for _ in range(largeur)) for _ in range(hauteur)]
        #carte[position_depart[0]][position_depart[1]]= 'R'
        return self.carte

    #remplace le caractere 'char' a la position 'position' dans la carte mentale
    def actualiserCarte(self, position, char):
        self.carte[position[0]][position[1]]= char
        return self.carte

    #affichage de la carte mentale
    def printCarte(self):
        print(self.carte)