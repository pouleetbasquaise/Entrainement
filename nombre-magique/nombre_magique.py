

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = 5

def demander_nombre(nb_min,nb_max):
    nombre_str=(input (f"Quel est le nombre magique (entre {nb_min} et {nb_max} ? " ) )
    nombre_int = int(nombre_str)
    while not nombre_int == NOMBRE_MAGIQUE: 
        if nombre_int < NOMBRE_MAGIQUE:
            print("trop petit")
        elif nombre_int > NOMBRE_MAGIQUE:
            print("trop grand")
        elif nombre_int == NOMBRE_MAGIQUE:
            print("bravo, c'est le bon nombre !")
        else:
            print(f" j'ai dis entre {nb_min} et {nb_max} !")
        return nombre_int
    
nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
