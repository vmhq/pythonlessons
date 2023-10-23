from random import randint

vida_pikachu = 80
vida_squirtle = 90

while vida_pikachu > 0 and vida_squirtle > 0:
    # Comienza el ciclo de combate. 

    #Turno de Pikachi
    print("Turno de Pikachu. \n")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola voltio
        print("Pikachu ataca con Bola Voltio. \n")
        vida_squirtle -= 10
    else:
        #Onda Trueno
        print("Pikachu ataca con Onda Trueno. \n" )
        vida_squirtle -= 11

    print("La vida de Pikachu es {} y la vida de Squirtle es {} \n" .format(vida_pikachu, vida_squirtle))
    input("presiona enter para continuar... \n\n")

    #Turno Squirtle
    print("Turno de Squirtle \n")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("¿Qué ataque deseas realizar? \n"
                            "[P]lacaje \n"
                            "Pistola de [A]gua \n"
                            "[B]urbuja \n").upper()
    if ataque_squirtle == "P":
        print("Squirtle utiliza placaje \n")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle utiliza pistola de agua \n")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle utiliza Burbuja \n")
        vida_pikachu -= 9
    
    print("La vida de Pikachu es {} y la vida de Squirtle es {} \n" .format(vida_pikachu, vida_squirtle))
    input("presiona enter para continuar... \n\n")

if vida_pikachu > vida_squirtle:
    print("¡Pikachi gana el combate! \n")
else:
    print("¡Squirtle gana el combate! \n")