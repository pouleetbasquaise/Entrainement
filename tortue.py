import turtle

t = turtle.Turtle()
def escalier(taille,nb):
    for i in range(nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)

#t.forward(30)

def carre(taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90)

def carres(taille_depart, nb):
    for i in range(0,nb):
        taille = (i+1) * taille_depart
        carre(taille*2)
        
carres(10,25)
#escalier(30,5)
#carre(200)
turtle.done()