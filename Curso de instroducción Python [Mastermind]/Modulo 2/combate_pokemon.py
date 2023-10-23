from random import randint
import os

#Configuración de la vida y de barra de vida
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANIO_BARA_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

#Valores de los ataques
#Pickachu
BOLA_VOLTIO = 10
ONDA_TRUENO = 12

#Squirtle
PLACAJE = 10
AGUA_CHORRO = 12
BURBUJA = 9

while vida_pikachu > 0 and vida_squirtle > 0:
    # Comienza el ciclo de combate. 

    #Turno de PikachU
    print("Turno de Pikachu. \n")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola voltio
        print("Pikachu ataca con Bola Voltio. \n")
        vida_squirtle -= BOLA_VOLTIO
    else:
        #Onda Trueno
        print("Pikachu ataca con Onda Trueno. \n" )
        vida_squirtle -= ONDA_TRUENO

    numero_barras_pikachu = int(vida_pikachu * TAMANIO_BARA_VIDA / VIDA_INICIAL_PIKACHU)
    numero_barras_squirtle = int(vida_squirtle * TAMANIO_BARA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Pikachu:    [{}{}] ({}/{})" .format("#" * numero_barras_pikachu, 
                                               " " * (TAMANIO_BARA_VIDA - numero_barras_pikachu), 
                                               max(0, vida_pikachu), VIDA_INICIAL_PIKACHU))
    
    print("Squirtle:    [{}{}] ({}/{})" .format("#" * numero_barras_squirtle, 
                                                " " * (TAMANIO_BARA_VIDA - numero_barras_squirtle), 
                                                max(0, vida_squirtle), VIDA_INICIAL_SQUIRTLE))
    
    input("presiona enter para continuar... \n\n")
    sistema = os.name
    if sistema == 'posix':  # Para sistemas Unix (macOS, Linux)
        os.system('clear')
    else:  # Para Windows
        os.system('cls')

    #Turno Squirtle
    print("Turno de Squirtle \n")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "N":
        ataque_squirtle = input("¿Qué ataque deseas realizar? \n"
                            "[P]lacaje \n"
                            "[A]gua chorro \n"
                            "[B]urbuja \n"
                            "[N]o atacar \n\n").upper()
    if ataque_squirtle == "P":
        print("Squirtle utiliza placaje \n")
        vida_pikachu -= PLACAJE
    elif ataque_squirtle == "A":
        print("Squirtle utiliza agua chorro \n")
        vida_pikachu -= AGUA_CHORRO
    elif ataque_squirtle == "B":
        print("Squirtle utiliza Burbuja \n")
        vida_pikachu -= BURBUJA
    elif ataque_squirtle == "N":
        print("Squirtle no ataca \n")
    
    numero_barras_pikachu = int(vida_pikachu * TAMANIO_BARA_VIDA / VIDA_INICIAL_PIKACHU)
    numero_barras_squirtle = int(vida_squirtle * TAMANIO_BARA_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Pikachu:    [{}{}] ({}/{})" .format("#" * numero_barras_pikachu, 
                                               " " * (TAMANIO_BARA_VIDA - numero_barras_pikachu), 
                                               max(0, vida_pikachu), VIDA_INICIAL_PIKACHU))
    
    print("Squirtle:    [{}{}] ({}/{})" .format("#" * numero_barras_squirtle, 
                                                " " * (TAMANIO_BARA_VIDA - numero_barras_squirtle), 
                                                max(0, vida_squirtle), VIDA_INICIAL_SQUIRTLE))
    
    input("presiona enter para continuar... \n\n")
    sistema = os.name
    if sistema == 'posix':  # Para sistemas Unix (macOS, Linux)
        os.system('clear')
    else:  # Para Windows
        os.system('cls')


if vida_pikachu > vida_squirtle:
    print("¡Pikachu gana el combate! 🎉\n")
else:
    print("¡Squirtle gana el combate! 🎉\n")