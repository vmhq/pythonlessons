#Este codigo cuenta con modificaciones realizadas por ChatGPT para creación de barra vida para ambos pokemones. 

from random import randint

vida_inicial_pikachu = 80
vida_actual_pikachu = vida_inicial_pikachu

vida_inicial_squirtle = 90
vida_actual_squirtle = vida_inicial_squirtle

while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:
    # Turno de Pikachu
    print("Turno de Pikachu. \n")
    porcentaje_vida_pikachu = vida_actual_pikachu / vida_inicial_pikachu
    num_barras_pikachu = int(porcentaje_vida_pikachu * 10)
    barra_vida_pikachu = '[' + '#' * num_barras_pikachu + ' ' * (10 - num_barras_pikachu) + ']'
    print("Pikachu", barra_vida_pikachu, vida_actual_pikachu)
    
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio. \n")
        vida_actual_squirtle -= 10
    else:
        # Onda Trueno
        print("Pikachu ataca con Onda Trueno. \n")
        vida_actual_squirtle -= 11

    input("Presiona enter para continuar... 🔄\n\n")

    # Turno de Squirtle
    print("Turno de Squirtle \n")
    porcentaje_vida_squirtle = vida_actual_squirtle / vida_inicial_squirtle
    num_barras_squirtle = int(porcentaje_vida_squirtle * 10)
    barra_vida_squirtle = '[' + '#' * num_barras_squirtle + ' ' * (10 - num_barras_squirtle) + ']'
    print("Squirtle", barra_vida_squirtle, vida_actual_squirtle)

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("¿Qué ataque deseas realizar? \n"
                                "[P]lacaje \n"
                                "Pistola de [A]gua \n"
                                "[B]urbuja \n").upper()

    if ataque_squirtle == "P":
        print("Squirtle utiliza placaje \n")
        vida_actual_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle utiliza pistola de agua \n")
        vida_actual_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle utiliza Burbuja \n")
        vida_actual_pikachu -= 9

    input("Presiona enter para continuar... 🔄\n\n")

if vida_actual_pikachu > vida_actual_squirtle:
    print("¡Pikachu gana el combate! 🎉")
else:
    print("¡Squirtle gana el combate! 🎉")
