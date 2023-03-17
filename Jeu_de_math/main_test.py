import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4
    
def poser_question():
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    question_str = input(f"calculez: {a} + {b} = ")
    question_int = int(question_str)
    if question_int == a+b:
        print("réponse correct")
    else:
        print("réponse incorrect")
        
    for i in  range (0,NB_QUESTION) :
        print(f"question n°{i} sur {NB_QUESTION} : ")
        poser_question()
        
        
        
#boucler le nb de fois de question
# print question n°1 sur 4:
