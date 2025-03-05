import turtle
from random import *
from time import *

# Fonction qui permet d'exporter dans le fichier decor.py le nombre de boules de départ.
# Utile pour les guirlandes et notamment le nombre de boules à mettre dessus

def nb_allumettes_depart():
    a=randint(10,20)
    return a


# Permet de connaître le nombre de chiffres dans la règle et leur valeur
def regle():
    nb_regle_num=turtle.numinput("Jeu des boules","Saisissez le nombre de chiffres dans la règle : ", default=None, minval=1, maxval=9)
    regle_num=[]
    nb_regle_num=int(nb_regle_num)
    for i in range(nb_regle_num):
        new_value=turtle.numinput("Jeu des boules","Saisissez la règle de la partie (Séparé d'espace) ", default=None, minval=1, maxval=9)
        new_value=int(new_value)
        regle_num.append(new_value)
    regle_num.sort()
    return regle_num





# Renvoie une liste d'éléments saisies par l'utilisateur sous forme de liste d'entiers
# séparés par des espaces.
def lireListeEntier(message):
    liste = input(message)
    listeChaine = liste.split()
    resultat = []
    for nombre in listeChaine :
        resultat.append(int(nombre))
    return resultat   
    




def joueur(nbAllumettes,r):
# Nombre à choisir parmis les nombres de la règle incrites par l'utilisateur
    nombreAEnleve=turtle.numinput("Jeu des boules","Combien de boules à enlever ?", default=None, minval=1, maxval=9)
# On vérifie si le nombreAEnleve fait partie de la règle et qu'il n'enlève pas un nombre supérieur d'allumettes.
# - présentes dans le jeu. Si une de ces deux conditions ne sont pas respectées, on redemande de saisir 
# - un nouveau nombre.
    while (nombreAEnleve not in r) or (nbAllumettes-nombreAEnleve<0):
        if nombreAEnleve not in r:
# Nombre non compris dans la règle.
            #nombreAEnleve=int(input("Votre nombre ne fait pas partie de la règle, veuillez en saisir un nouveau =>"))
            nombreAEnleve=turtle.numinput("Jeu des boules","Votre nombre ne fait pas partie de la règle, veuillez en saisir un nouveau", default=None, minval=1, maxval=9)
        else:
            if nbAllumettes-nombreAEnleve<0:
# Nombre supérieur au nombre d'allumettes présentes dans le jeu.
                #nombreAEnleve=int(input("Votre nombre est trop grand. Saisissez un nouveau =>"))
                nombreAEnleve=turtle.numinput("Jeu des boules","Votre nombre est trop grand. Saisissez un nouveau", default=None, minval=1, maxval=9)
            
    return int(nombreAEnleve)

    

   
    

def soustraction(nombreAEnleve,nbAllumettes):
#On soustrait le nombre choisi, vérifié dans la fonction joueur() pour être compatible avec le nombre
# -précédent d'allumettes.
        nbAllumettes-=nombreAEnleve
        #print("Il reste donc", nbAllumettes, "allumettes")
        return nbAllumettes
        




def nList(nbAllumettes,r):
# On crée une nouvelle liste avec les nombres de règles compatibles au nombre d'allumettes.
#- Si un nombre de la règle est trop grand par rapport au nombre d'allumettes, celui-ci sera
#- retiré. Idem pour les nombres suivants jusqu'à ce qu'une valeur convienne.
# On copie la nouvelle liste, pour le moment, identique à celle de la règle.
    new_List=r.copy()
    n=1
    while nbAllumettes-r[len(r)-n]<0:
        newValue=len(r)-n
        new_List.remove(r[newValue])
        n+=1
    return new_List



# Renvoie la valeur d'une pile d'allumettes
def valPileAllumettes(n,r):
    if n==0:
        return 0
    res=[]
    for i in r:
        if n>=i:
            res.append(valPileAllumettes(n-i,r))
    return mex(res)
        
# Renvoie le MEX de la liste l        
def mex(l):
    if l==[]:
        return 0
    for i in range(0,len(l)+1):
        if i not in l:
            return i


# Renvoie la valeur en binaire de n XOR m
def sumNimXOR(n,m):
    return n^m

# Renvoie la valeur du jeu d'allumettes            
def valJeuAllumettes(a,r):
    res=0
    for i in a:
        res=sumNimXOR(valPileAllumettes(i,r),res)
    return res
    

# Permet de savoir si l'ordi a la SG (=0), sinon renvoie un nombre au hasard dans la liste. 
# Ce second cas n'est pas censé se produire puisque l'ordinateur a toujours la SG, mais dans un soucis
# d'amélioration, on laisse.    
def afficheJoueurStratGagnanteAllumettes(a,r):
    if not valJeuAllumettes(a,r)==0:
        for i in range(len(a)):
            for k in range(len(r)):
                a[i]-=r[k]
                if valJeuAllumettes(a,r)==0:
                    return int(r[k])
                a[i]+=r[k]
    else:
        return choice(r)
        
        

# Permet de faire jouer l'ordinateur 
def ordi(nbAllumettes,r):
    liste_jeu=nList(nbAllumettes,r)
    nb_enleve=strategie_gagnante_ordi(nbAllumettes,liste_jeu)
    nbAllumettes-=nb_enleve
    sleep(2.0)
    return nbAllumettes,nb_enleve



# Permet de savoir si l'ordi a la SG dès le début du jeu (=0) ou pas
def strategie_gagnante_ordi(nbAllumettes,liste_jeu):
    nbAllumettes_list=[]
    nbAllumettes_list.append(nbAllumettes)
    return afficheJoueurStratGagnanteAllumettes(nbAllumettes_list,liste_jeu)