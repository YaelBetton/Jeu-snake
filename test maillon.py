from maillon import Maillon
from random import randint

maListe= Maillon(10,None)

#Construit une liste chaînee maListe de 10 maillons contenant des valeurs aleatoires

for i in range(10) : maListe = Maillon(randint(0,100),maListe)    
 
#########################   Fonctions a completer   ######################################        
def supprime_queue(m) :
    if m.suivant.suivant == None :
        m.suivant = None
    else : supprime_queue(m.suivant)
        
    
def longueur_liste(m) :
    if m.suivant==None : return 1
    else : return 1+longueur_liste(m.suivant)
        

def test_valeur(val,m) :
    if m.valeur == val : return True
    elif m.suivant == None : return False
    else : return test_valeur(val,m.suivant)
        

        
        