# -*- coding: utf-8 -*- 
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from  tkinter import Tk,Label,Button,Entry,StringVar,Canvas,PhotoImage
from random import randint
import random

#Fonction qui va permettre de trier une liste
def Tri(Liste):
   return len(Liste), Liste.lower()


#Fonction qui ouvre le fichier et prend les mots qui vont constituer une liste



def MotsFichier():
    Liste = []    
    Fichier = open("pendule.txt")
    for ligne in Fichier :
        Liste.append(ligne)
    Liste=sorted(Liste, key=Tri)    
    Indice = randint(0,len(Liste)-1)
    Fichier.close()
    Mot = Liste[Indice].upper()
    Mot = Mot[:-1]
    Fichier.close()
    return Liste

def ChoixMot(Liste):#Fonction qui va choisir un mot aléatoire dans la liste des mots importée
    Mot=random.choice(MotsFichier()) 
    return Mot

def AffichageMot(Mot,LettresTrouver):#Cette fonction va afficher les lettres trouvées et remplacer celles non trouvées par des underscore
    underscore = ""
    for i, Lettre in enumerate(Mot[:-1]):
        if i==0 or Lettre in LettresTrouver: 
            underscore+=Lettre
        else: 
            underscore+=" _"
    Vrai.set(underscore)
    return underscore

def GagnerPartie(Mot,LettresTrouver):#Fonction qui permet de savoir si la partie est gagnée ou non
    LettreBonne=0
    for Lettre in Mot:
        if Lettre in LettresTrouver: 
            LettreBonne+=1
    if LettreBonne==len(Mot[:-1]): 
        return True

def AffichageBonhomme():#Fonction qui va afficher une image du pendu en fonction du nombre de tentatives restantes à l'utilisateur
    global tentative
    if tentative==6:
        item = Canevas.create_image(150,150,image=image7)
    if tentative==5:
        item = Canevas.create_image(150,150,image=image6)
    if tentative==4:
        item = Canevas.create_image(150,150,image=image5)
    if tentative==3:
        item = Canevas.create_image(150,150,image=image4)
    if tentative==2:
        item = Canevas.create_image(150,150,image=image3)
    if tentative==1:
        item = Canevas.create_image(150,150,image=image2)
    if tentative==0:
        item = Canevas.create_image(150,150,image=image1)      
   
def ListeLettresFausses(LettresFausses):#Fonction qui va récapituler les lettres,saisies par l'utilisateur, non incluses dans le mot
    A=""
    for Lettre in LettresFausses:
        A+=Lettre
        A+=","
    Faux.set("Lettres fausses : "+A)
    return A
    
def VerificationLettre():#Fonction qui vérifie si la lettre saisie par l'utilisateur est incluse dans le mot à trouver ou non
    """
    Cette fonction vérifie que la lettre donnée par l'utilisateur est bien dans le mot
    """
    global LettresTrouver,LettresFausses,Mot,tentative
    l=Lettre.get()
    Lettre.set('')
    if l in LettresTrouver or l in LettresFausses: #si la lettre a déja été trouvée
        message.set("La lettre a déjà été saisi")
    elif l in Mot: #si la lettre est incluse dans le mot
        LettresTrouver.append(l)
        AffichageMot(Mot,LettresTrouver)
        message.set("Veuillez saisir une lettre ")
    elif len(l)!=1:
        message.set("Veuillez saisir une lettre et non autre chose")
    else :#si la lettre n'est pas incluse le mot
        tentative=tentative-1 
        LettresFausses.append(l) 
        AffichageBonhomme()
        coup.set("Nombre de coups restants: "+str(tentative))
        message.set("Lettre non incluse dans le mot")
        ListeLettresFausses(LettresFausses) 


def Pendu():#Fonction qui va permettre de lancer le jeu du Pendu
    global Mot,LettresTrouver,LettresFausses,tentative
    AffichageMot(Mot,LettresTrouver)
    if tentative>0:
        VerificationLettre()
        if GagnerPartie(Mot,LettresTrouver)==True: 
            Score(scoremax,tentative)
            message.set("Vous avez gagné, bien joué")
    if tentative==0 and GagnerPartie(Mot,LettresTrouver)!=True :
       message.set("Vous avez perdu, retentez votre chance")

def Rejouer():#Fonction qui permet de relancer une autre partie
    global Mot,LettresTrouver,LettresFausses,tentative
    Mot=ChoixMot(MotsFichier)
    LettresTrouver=[Mot[0]]
    LettresFausses=[]
    tentative = 7
    Pendu()
    return Mot,LettresTrouver,LettresFausses,tentative

def Score(scoremax,tentative):
    if GagnerPartie==True:
        if scoremax < tentative:
            scoremax = tentative
            score.set("Score max: "+str(Score(scoremax,tentative)))
    return scoremax
        
Mot=ChoixMot(MotsFichier())
LettresTrouver=[Mot[0]]#On indique à l'utilsateur la première lettre du mot
LettresFausses=[]
tentative = 7
scoremax=0 

#Création de la fenêtre où va se lancer le jeu
Mafenetre=Tk()
Mafenetre.title('Jeu du pendu')

#Création du message qui va indiquer à l'utilisateur si la lettre entrée est juste ou fausse, et si la partie est gagnée ou perdue
message=StringVar()
console=Label(Mafenetre, textvariable=message)

#Liste des images qui vont s'afficher lors de la partie
image1=PhotoImage(master=Mafenetre, file='bonhomme1.gif')
image2=PhotoImage(master=Mafenetre, file='bonhomme2.gif')
image3=PhotoImage(master=Mafenetre, file='bonhomme3.gif')
image4=PhotoImage(master=Mafenetre, file='bonhomme4.gif')
image5=PhotoImage(master=Mafenetre, file='bonhomme5.gif')
image6=PhotoImage(master=Mafenetre, file='bonhomme6.gif')
image7=PhotoImage(master=Mafenetre, file='bonhomme7.gif')
image8=PhotoImage(master=Mafenetre, file='bonhomme8.gif')

#Création du Canvas

Canevas=Canvas(Mafenetre, height= 300, width=300)
item = Canevas.create_image(150,150,image=image8)

#Création de l'emplacement où l'utilisateur va saisir les lettres
Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)

#Création du bouton proposer
BoutonProposer=Button(Mafenetre,text='Proposer',command = Pendu)

#Création du bouton rejouer
BoutonRejouer=Button(Mafenetre,text='Rejouer',command=Rejouer)

#Création du bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Création label qui va indiquer le mot recherché
Vrai=StringVar()
Vrai.set(AffichageMot(Mot,LettresTrouver))
LabelMotRech=Label(Mafenetre,textvariable=Vrai)

#Création label qui va indiquer le nombre de tentatives disponibles
coup=StringVar()
coup.set("Nombre de coups restants: "+str(tentative))
LabelCoup=Label(Mafenetre,text="Nombre de coups restants :",textvariable=coup)

#Création label lettres fausses
Faux=StringVar()
LabelLettresFausses=Label(Mafenetre,textvariable=Faux,fg='red')


#Création du label qui va afficher le Score Max
score=StringVar()
score.set("Score max: "+str(Score(scoremax,tentative)))
LabelScoreMax=Label(Mafenetre,textvariable=score)


#Mise en page
LabelCoup.grid(row=1)
LabelMotRech.grid(row=2)
BoutonEntry.grid(row=3)
BoutonProposer.grid(row=4)
BoutonRejouer.grid(row=2,column=3)
BoutonQuitter.grid(row=3,column=3)
LabelLettresFausses.grid(row=5)
LabelScoreMax.grid(row=8,column=3)
Canevas.grid(row=1,column=2,rowspan=4)
console.grid(row=7, column=2)

Rejouer()

Mot=Rejouer()[0]
LettresTrouver=Rejouer()[1]
LettresFausses=Rejouer()[2]
vie=Rejouer()[3]

Mafenetre.mainloop()
