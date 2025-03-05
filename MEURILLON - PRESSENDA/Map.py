import turtle
from random import *
from math import *

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()


############################################

# fonction qui permet d'aller à un point sans tracer de trait.
def vasy(x,y):
    t1.up()
    t1.goto(x,y)
    t1.down()

    


#Boule de Noël:
def boule():
    couleur=["grey", "brown", "orange", "pink", "purple", "red", "blue", "yellow", "green"]
    t1.color(choice(couleur))
    for i in range(4):
        t1.forward(25)
        t1.left(90)
    t1.forward(12.5)
    t1.left(90)
    t1.forward(25)
    t1.left(180)
    t1.forward(12.5)
    t1.left(90)
    t1.forward(12.5)    
    t1.left(180)
    t1.forward(25)
    t1.left(180)
    t1.forward(12.5)
    t1.left(90)
    t1.forward(17.5)
    t1.circle(5)
    t1.left(180)
    t1.circle(5)


#Etoile:
# L'ensemble des étoiles se dessinent en deux temps. Dans la fonction etoile(), un nombre
# aléatoire d'étoiles (entre 3 et 6) est tiré au sort. Chacunes de celles-ci ont un nombre
# aléatoires de branches.
def etoile():
    nb_etoiles=randint(3,6)
    couleur_etoile=["brown", "pink", "purple", "yellow", "green"]
    t1.color(choice(couleur_etoile))
    t1.pensize(2)
    for i in range(nb_etoiles):
        taille_etoile=randint(10,25)
        x=randint(-150,290)
        y=randint(220,290)
        branche=[3,12]
        nombre_branche=choice(branche)
        rotation=randint(20,30)
        bout=randint(3,11)
        etoileT(taille_etoile,rotation,bout,x,y)

## Fonction qui permet de tracer une étoile


def etoileT(longueur,angle,npointes,x,y):
    vasy(x,y)
    t1.begin_fill()
    a=180-angle
    for i in range(npointes):
        t1.forward(longueur)
        t1.left(a)
        t1.forward(longueur)
        t1.right(a-360/npointes)
    t1.end_fill()


def boule_guirlande(x,y):
    couleur_boule=["firebrick","coral","chocolate",
"turquoise","royalblue","indigo","crimson"]
    vasy(x,y)
    t1.setheading(270)
    t1.pensize(2)
    t1.color("black")
    t1.fd(10)
    t1.color(choice(couleur_boule))
    t1.right(90)
    t1.begin_fill()
    t1.circle(5)
    t1.end_fill()
    vasy(x,y)
    t1.setheading(0)
    
    






def ensemble_guirlande(a):

# Cette liste de position permet de placer les boules sur les guirlandes appropriées sur le sapin.
# Sur la première (la plus haute sur le sapin) guirlande, on retrouve jusqu'à 4 boules.
# 2ème guirlande : 4 boules
# 3ème guirlande : 6 boules
# 4ème guirlande : 6 boules
# Toutes les positions ont été regroupées sous une seule liste ce qui permet d'avoir
# a (nombre random du script principal) positions pour a  boules de départ.
    position=[[23,-10],[41,-10],[59,-10],[77,-10],[11,-90],[37,-90],
[63,-90],[89,-90],[-11,-170],[13,-170],[37,-170],[62,-170],[85,-170],
[110,-170],[-25,-250],[5,-250],[35,-250],[65,-250],[95,-250],[125,-250]]
    #trouvez méthode pour importer le nombre d'allumettes de départ du fichier mère.
    position[:a]
    for i in range(a):
        boule_guirlande(position[i][0],position[i][1])
    return position







##############
# Partie ciel, composé de la nuit et de la lune

def ciel():
    vasy(-450,200)
    t1.begin_fill()
    t1.color("darkblue")
    for i in range(2):
        t1.forward(900)
        t1.left(90)
        t1.forward(250)
        t1.left(90)
    t1.end_fill()


def lune():
    vasy(-300,350)
    t1.dot(60,"yellow")
    vasy(-286,350)
    t1.dot(60,"darkblue")



###############
#Partie sol, on tracer les pavés au sol
    


def ligne_pave_verticale():
    t1.pensize(3)
    t1.color("gray")
    for i in range(4):
      vasy(-450+225*i,200)
      t1.setheading(270)
      t1.fd(650)




def pave():
    vasy(-450,200)
    t1.begin_fill()
    t1.color("wheat")
    for i in range(2):
        t1.fd(900)
        t1.right(90)
        t1.fd(650)
        t1.right(90)
    t1.end_fill()
    t1.setheading(0)
    t1.pensize(3)
    ligne_pave_horizontale()
    ligne_pave_verticale()


def ligne_pave_horizontale():
  t1.color("gray")
  for i in range(6):
    t1.fd(900)
    vasy(-450,200-130*i)



#################
# Partie création du sapin

# On définit une guirlande telle qu'une ligne droite, orientée, dans le plan cartésien.


def guirlande(x,y,a,aInit=0):
    vasy(x,y)
    t1.setheading(0)
    t1.left(aInit)
    t1.pensize(3)
    t1.color("black")
    t1.fd(a)

# Fonction qui trace un rectangle, dont le tronc du sapin

def rec(x,y,l,h,couleur):
    vasy(x,y)
    t1.setheading(0)
    t1.color(couleur)
    t1.begin_fill()
    for i in range(2):
        t1.fd(l)
        t1.right(90)
        t1.fd(h)
        t1.right(90)
    t1.end_fill()

# Fonction qui permet de dessiner le sapin, sans les boules de Noël
    
def sapin():
    rec(35,-250,40,80,"brown")
    t1.color("lightgreen")
    etoileT(120,60,3,50,-280)
    t1.color("forestgreen")
    etoileT(100,60,3,50,-200)
    t1.color("green")
    etoileT(80,60,3,50,-120)
    t1.color("limegreen")
    etoileT(60,60,3,50,-40)








########### Fonction qui dessine les cadeaux au pied du sapin


def cadeau(x,y):
    couleur=["grey", "brown", "orange", "pink", "purple", "red", "blue", "green"]
    for i in range(5):
        j=randint(0,7)
        vasy(x,y)
        t1.setheading(0)
        polygone(36,90,4,couleur[j])
        vasy(x+18,y+18)
        croix(36,couleur[j])
        t1.up()
        t1.goto(x+7,y+41)
# t1.dot(taille, color) : Dessine un point circulaire de diamètre 12, de la couleur color.
        t1.dot(12,couleur[j])
        t1.goto(x+20,y+41)
        t1.dot(12,couleur[j])
        x=x+80

def croix(longueur,couleur):
    t1.color(couleur)
    t1.forward(longueur/2)
    t1.bk(longueur)
    t1.fd(longueur/2)
    t1.right(90)
    t1.fd(longueur/2)
    t1.bk(longueur)


    
def polygone(longueur,angle,cote,couleur):
    t1.color(couleur)
    for i in range(cote):
        t1.forward(longueur)
        t1.left(angle)



############### Fonction qui crée les bonhommes de neige




def bonhomme_de_neige(x,y):
    vasy(x,y)
    t1.setheading(0)
#1ere boule de neige
    t1.color("grey")
    t1.begin_fill()
    t1.circle(15)
    t1.end_fill()
    t1.color("black")
#replacement pour la 2ème boule de neige
    t1.up()
    t1.left(90)
    t1.fd(30)
    t1.right(90)
    t1.down()
#2ème boule de neige
    t1.color("grey")
    t1.begin_fill()
    t1.circle(10)
    t1.end_fill()
    t1.color("black")
#Replacement pour le sourire
    t1.up()
    t1.bk(6)
    t1.left(90)
    t1.fd(6)
    t1.left(200)
#Dessin du sourire
    t1.down()
    t1.pensize(2)
    for i in range(150):
        t1.forward(0.1)
        t1.left(1)
    t1.up()
    t1.pensize(1)
    t1.setheading(180)
    t1.fd(5)
    t1.right(90)
    t1.fd(2)
    t1.right(90)
#Replacement pour la carotte
    t1.down()
#Dessin de la carotte
    t1.begin_fill()
    polygone(3,120,3,"orange")
    t1.end_fill()
    t1.color("black")
#Replacement pour les yeux
    t1.up()
    t1.bk(3)
    t1.left(90)
    t1.fd(2)
    t1.right(90)
    t1.down()
    t1.begin_fill()
    t1.circle(3)
    t1.end_fill()
    t1.up()
    t1.fd(8)
    t1.down()
    t1.begin_fill()
    t1.circle(3)
    t1.end_fill()
    t1.up()
    t1.bk(3)
    t1.right(90)
    t1.fd(11.5)
    t1.left(90)
#Replacement pour les deux boutons
    t1.right(90)
    t1.fd(10)
    t1.left(90)
    t1.down()
    t1.circle(2)
    t1.up()
    t1.right(90)
    t1.fd(6)
    t1.left(90)
    t1.down()
    t1.circle(2)
    t1.up()
    t1.left(90)
    t1.fd(17)
    t1.right(120)
    t1.down()
    bras_bonhomme_de_neige()
    t1.up()
    t1.left(180)
    t1.fd(5)
    t1.left(75)
    t1.fd(25)
    t1.left(60)
    t1.down()
    bras_bonhomme_de_neige()

def bras_bonhomme_de_neige():
    t1.pensize(2)
    t1.fd(25)
    t1.left(75)
    t1.fd(5)
    t1.bk(5)
    t1.right(75)
    t1.fd(5)
    t1.bk(5)
    t1.right(75)
    t1.fd(5)


# Fonction qui permet de dessiner un bonnet de Noël. Utilisé pour les bonhommes de neige

def bonnet(x,y):
    x=x-5
    y=y+51
    t1.setheading(0)
    
# Partie rouge du bonnet
    vasy(x,y)
    t1.color("red")
    t1.begin_fill()
    for i in range(3):
        t1.forward(10)
        t1.left(120)
    t1.end_fill()

# Pompon
    vasy(x+5,y+8)
    t1.color("grey")
    t1.begin_fill()
    t1.circle(4/7)
    t1.end_fill()

# Partie basse du bonnet
    vasy(x+3/5,y-4/5)
    t1.begin_fill()
    for i in range(18):
        t1.circle(4/7)
        t1.up()
        t1.forward(4/7)
        t1.down()
    t1.end_fill()







######################

#Zone immeuble


def principal():
    sol()
    rectangle()
    porte()
    toit()

    
    
def sol():
    vasy(-400,-300)
    t1.setheading(0)
    t1.pensize(5)
    t1.color("black")
    t1.forward(200)

def rectangle():
    couleur=["grey", "brown", "orange", "pink", "purple", "red", "blue", "green"]
    t1.color(choice(couleur))
    t1.pensize(1)
    t1.begin_fill()
    t1.left(90)
    t1.forward(500)
    t1.left(90)
    t1.forward(200)
    t1.left(90)
    t1.fd(500)
    t1.end_fill()

        
def porte(i,j):
    vasy(-400+25+40*i,-300)
    t1.setheading(90)
    t1.color("white")
    t1.begin_fill()
    t1.forward(50)
    t1.right(90)
    t1.fd(30)
    t1.right(90)
    t1.fd(50)
    t1.end_fill()
    i+=1
    vasy(-400+25+40*j,-300)
    t1.pensize(2)
    t1.setheading(90)
    t1.color("black")
    t1.forward(50)
    t1.right(90)
    t1.fd(30)
    t1.right(90)
    t1.fd(50)
    j+=1
    return i,j


    

def toit():
    t1.pensize(3)
    vasy(-410,200)
    t1.begin_fill()
    t1.setheading(0)
    t1.forward(220)
    t1.left(150)
    t1.forward(220*sqrt(3)/3)
    t1.left(60)
    t1.forward(220*sqrt(3)/3)
    t1.end_fill()
    t1.setheading(0)

def fenetre():
    t1.up()
    t1.fd(25)
    t1.left(90)
    t1.fd(10)
    t1.right(90)
    for i in range(4):
        t1.down()
        t1.begin_fill()
        polygone(30,90,4,"white")
        t1.end_fill()
        t1.up()
        t1.fd(40)
    t1.up()
    t1.bk(185)
    t1.fd(25)
    for i in range(4):
        t1.down()
        polygone(30,90,4,"black")
        t1.up()
        t1.fd(40)
    

def fenetre_rdc(i,j):
    t1.pensize(1)
    while i<4:
        vasy(-400+25+40*i,-260)
        t1.begin_fill()
        polygone(30,90,4,"white")
        t1.end_fill()
        i+=1
    while j<4:
        vasy(-400+25+40*j,-260)
        t1.pensize(2)
        polygone(30,90,4,"black")
        j+=1

    

    
def etage():
    for i in range(1,8):
        facade(i)
        fenetre()

def rdc():
    i=0
    j=0
    res=porte(i,j)
    fenetre_rdc(res[0],res[1])

    

def facade(c):
    t1.up()
    t1.goto(-400,-300)
    t1.setheading(90)
    t1.fd(c*60)
    t1.right(90)
    t1.down()
    t1.fd(200)
    t1.up()
    t1.bk(200)


def immeuble():
    sol()
    rectangle()
    rdc()
    etage()
    toit()
    



####################################
# Fonction principal qui dessine le décor fixe à partir de toutes les fonctions écrites ci-dessus.



def decor_fixe():
    turtle.tracer(0)
    ciel()
    lune()
    etoile()
    pave()
    immeuble()
    bonhomme_de_neige(-250,240)
    bonnet(-250,240)
    bonhomme_de_neige(250,-240)
    bonnet(250,-240)
    sapin()
    guirlande(60,45,335,aInit=255)
    guirlande(95,-60,230,aInit=255)
    guirlande(120,-150,135,aInit=255)
    guirlande(5,-10,90,aInit=0)
    guirlande(-15,-90,130,aInit=0)
    guirlande(-35,-170,170,aInit=0)
    guirlande(-55,-250,210,aInit=0)
    cadeau(-75,-400)



####################################
# Fin du décor fixe.


####################################
# Début du décor temporaire avec la deuxième et troisième tortue.

# La deuxième tortue permet d'afficher les boules sur le sapin de Noël
# et de dessiner l'étoile en cas de victoire du joueur



def vasy_v2(x,y):
    t2.up()
    t2.goto(x,y)
    t2.down()

def boule_guirlande_v2(x,y):
    vasy_v2(x,y)
    t2.setheading(270)
    t2.pensize(2)
    t2.color("black")
    t2.fd(10)
    t2.color("white")
    t2.right(90)
    t2.begin_fill()
    t2.circle(5)
    t2.end_fill()
    vasy_v2(x,y)
    t2.setheading(0)


def etoileT2(longueur,angle,npointes,x,y):
    vasy_v2(x,y)
    t2.begin_fill()
    a=180-angle
    for i in range(npointes):
        t2.forward(longueur)
        t2.left(a)
        t2.forward(longueur)
        t2.right(a-360/npointes)
    t2.end_fill()



##################
# Fonction qui enlève de la liste des positions, la position qui vient d'être retirer par le joueur
# ou l'ordinateur. 

def enleve_guirlande(l,nombreAEnleve):
    nombreAEnleve=int(nombreAEnleve)
    for i in range(nombreAEnleve):
        boule_guirlande_v2(l[0][0],l[0][1])
        a=l[0]
        l.remove(a)
    return l


########
# Fonction qui trace l'étoile final en cas de victoire du joueur

def etoile_final():
    t2.color("yellow")
    vasy_v2(50,65)
    t2.setheading(90)
    t2.pensize(6)
    t2.fd(20)
    etoileT2(25,15,11,50,130)



#################################
# Fin de l'utilisation de la deuxième tortue.

# Début de l'utilisation de la troisème tortue.
# Cette tortue permet d'afficher en temps réel le nombre de boules restantes sur le sapin en commentaire



def vasy_v3(x,y):
    t3.up()
    t3.goto(x,y)
    t3.down()



def affichage(nombre_allumettes, pos):
    t3.color("black")
#Fonction pour afficher le nombre d'allumettes
    vasy_v3(pos[0],pos[1])
    nombre_allumettes=int(nombre_allumettes)
    t3.write("Il y a {} allumette(s)".format(nombre_allumettes),
                 align = "center",
                 font = ("Arial", 15, "normal"))


#########################
# Fin de l'utilisation de la tortue 3
# Utilisation de la tortue 4 pour afficher que l'ordinateur a gagné



def vasy_v4(x,y):
    t4.up()
    t4.goto(x,y)
    t4.down()


# Fin de l'utilisation de la tortue 4