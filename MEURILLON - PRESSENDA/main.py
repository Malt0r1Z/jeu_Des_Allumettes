import turtle
from allumettes import *

from Map import *

# On paramètre la fenêtre d'affichage pour être certain d'obtenir la meilleure expérience de jeu possible.
turtle.setup(900,900,0,0)

# Programme principal qui fait tourner le jeu à l'aide de toutes les fonctions données ci-dessus


nbAllumettes=nb_allumettes_depart()
decor_fixe()
affichage(nbAllumettes,pos=(350, 150))
liste_position=ensemble_guirlande(nbAllumettes)
r = regle()

liste_allumettes=[]
liste_allumettes.append(nbAllumettes)

# Boucle si le second joueur à une SG, donc l'ordinateur
if valJeuAllumettes(liste_allumettes,r)==0:
    while nbAllumettes>0:
        if nbAllumettes-min(r)>=0:
            res0=joueur(nbAllumettes,r)
            liste_position=enleve_guirlande(liste_position,res0)
            res1=soustraction(res0,nbAllumettes)
            t3.clear()
            affichage(res1,pos=(350, 150))
            if res1-min(r)>=0:
                res2=ordi(res1,r)
                nbAllumettes=res2[0]
                t3.clear()
                affichage(nbAllumettes,pos=(350, 150))
                liste_position=enleve_guirlande(liste_position,res2[1])
            else:
                nbAllumettes=0
        else:
            nbAllumettes=0

# Boucle si l'ordinateur voit qu'il a une SG dès le début du jeu
else:
    while nbAllumettes>0:
        if nbAllumettes-min(r)>=0:
            res0=ordi(nbAllumettes,r)
            nbAllumettes=res0[0]
            t3.clear()
            affichage(nbAllumettes,pos=(350, 150))
            liste_position=enleve_guirlande(liste_position,res0[1])

            if nbAllumettes-min(r)>=0:
                res1=joueur(nbAllumettes,r)
                liste_position=enleve_guirlande(liste_position,res1)
                nbAllumettes=soustraction(res1,nbAllumettes)
                t3.clear()
                affichage(nbAllumettes,pos=(350, 150))
            else:
                nbAllumettes=0
        else:
            nbAllumettes=0

t4.color("black")
#Fonction pour afficher le gagnant
vasy_v4(-135,160)
t4.write("GAME OVER. L'ordi a gagné", font = ("Arial", 25, "bold"))

#############################################
# Fin du programme

