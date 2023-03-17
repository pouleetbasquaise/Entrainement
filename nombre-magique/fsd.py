

def demander_nombre(nb_min,nb_max):
    nombre_str = input(f"quel est le nombre magique (entre {NOMBRE_MIN} et {NOMBRE_MAX}) ")
    try:
        nombre_int = int(nombre_str)
    except:
        print('ERREUR : rentre valeur correct de type int')
    return nombre_int
    
    
nombre = 0    
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = 5

while not nombre == NOMBRE_MAGIQUE:
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print('Bravo ! ')
    elif nombre < NOMBRE_MAGIQUE:
        print('trop petit, dommage ! ')
    else:
        print('trop grand, dommage ! ')
        
