import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4
    
def poser_question():
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    o = random.randint(0,1)
    #si 0 -> addition
    #si 1 -> multiplication
    operateur_str = "+"
    if o == 1 :
        operateur_str = "*"
    question_str = input(f"calculez: {a} {operateur_str} {b} = ")
    question_int = int(question_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if question_int == calcul:
        return True
    
    return False
    

nb_points = 0  
      
for i in  range (0,NB_QUESTION) :
    print(f"question n°{i + 1} sur {NB_QUESTION} : ")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrect")
    print()    
        
        
#boucler le nb de fois de question
# print question n°1 sur 4:


print(f'Votre note est {nb_points} / {NB_QUESTION} : ')

calc_moyenne = int(NB_QUESTION/2)

if nb_points == NB_QUESTION:
    print("Excellent !")
    print()
elif nb_points == 0:
    print("révisez vos math")
    print()
elif nb_points > calc_moyenne :
    print("Pas mal !")
    print()
else:
    print("peu mieux faire")
    print()
    

# si note max : Excellent !
#si note min : révisez vos math

# calc moyenne = int(NB_QUESTION)/2
# si sup moyenne : pas mal
#si en dessous de moyenne : peu mieux faire