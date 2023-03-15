def demander_nom():
    reponse_nom=''
    while reponse_nom == '':
        reponse_nom = input("quel est ton nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    reponse_age=0
    while reponse_age == 0:
        age_str = input(nom_personne +' quel est ton age ? ')
        try:
            reponse_age = int(age_str)
        except ValueError:
            print("ERREUR VALUE")
    return reponse_age


def afficher_informations_personne(nom,age,taille=0):
    #print()
    #print(f'Votre nom est {nom}, votre age est de {age} ans')
    #print(f'Votre nom est {nom}, votre age est de {age} ans')
    
    if age == 17:
        print("bientot majeur !")
    elif 12 <= age <18 :
        print("vous etes ado ")   
    elif age == 18:
        print("tout juste majeur !") 
    elif age > 18:
        print("vous êtes majeur ")
    elif age ==1 or age == 2:
        print("Vous êtes bébé, comment vous arrivez à lire et ecrire ? ")       
    else :
        print("retourne à l'école ")
    print("L'an prochain vous aurez %s ans" %(age+1))
    print("Votre nom est %s, votre age est de %s ans"%(nom,age))
    #afficher la taille
    if not taille == 0:
        print("votre taille : " +str(taille) + "m")
    
    
    
#nom_1 = demander_nom()
#nom_2 = demander_nom()
#
#age_1 = demander_age(nom_1)
#age_2 = demander_age(nom_2)
#
#
#afficher_informations_personne(nom_1,age_1)
#afficher_informations_personne(nom_2,age_2)
#
#print(f'Votre nom est {nom_1}, votre age est de {age_1} ans')
#print(f'Votre nom est {nom_2}, votre age est de {age_2} ans')

NB_PERSONNES=1

for i in range(0,NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_informations_personne(nom,age,1.6)
    
print("""
      
Vous      
    Mettez  
        Ce que vous voulez
      
      
      
      
      """)
print( "toto", 20, "ans", "taille", 1.70)