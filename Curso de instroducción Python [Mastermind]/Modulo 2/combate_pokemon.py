from random import randint

vida_pikachu = 80
vida_squirtle = 90

while vida_pikachu > 0 and vida_squirtle > 0:
    # Comienza el ciclo de combate. 

    #Turno de Pikachi
    print("Turno de Pukachu. \n")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola voltio
        print("Pikachi ataca con Bola Voltio. \n")
        vida_squirtle -= 10
    else:
        #Onda Trueno
        print("Pikachu ataca con Onda Trueno. \n" )
        vida_squirtle -= 11

    #Turno Squirtle
    print("Turno de Squirtle \n")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
    ataque_squirtle = input("¿Qué ataque deseas realizar? \n"
                            "[P]lacaje \n"
                            "Pistolo de [A]gua \n"
                            "[B]urbuja \n").upper()
    
