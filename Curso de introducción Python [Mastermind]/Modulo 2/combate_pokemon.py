'''
El código es un juego simple de combate entre dos Pokémon: Pikachu y Squirtle.

Importación de módulos:

Se importa la función randint del módulo random para generar números aleatorios.
Se importa el módulo os para interactuar con el sistema operativo.
Configuración inicial:

Se establecen las vidas iniciales de Pikachu y Squirtle.
Se define el tamaño de la barra de vida.
Se definen los daños de los ataques de ambos Pokémon.
Inicio del combate:

Mientras ambos Pokémon tengan vida, el combate continúa.
Turno de Pikachu:

Pikachu elige un ataque al azar entre "Bola Voltio" y "Onda Trueno".
Se resta la vida de Squirtle según el ataque elegido.
Se muestra la barra de vida de ambos Pokémon.
Se espera a que el jugador presione Enter para continuar.
Luego, se limpia la pantalla.
Turno de Squirtle:

El jugador elige el ataque que Squirtle usará.
Se resta la vida de Pikachu según el ataque elegido.
Se muestra nuevamente la barra de vida de ambos Pokémon.
Se espera a que el jugador presione Enter para continuar.
Se limpia la pantalla nuevamente.
Fin del combate:

Una vez que uno de los Pokémon se queda sin vida, se determina el ganador y se muestra un mensaje correspondiente.
El código utiliza barras de vida (representadas con el símbolo #) para mostrar gráficamente la salud restante de cada Pokémon. 
Además, se utiliza la función os.system para limpiar la pantalla después de cada turno, 
lo que permite que la interfaz del juego sea más limpia y amigable.

'''

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
    while ataque_squirtle not in ["P", "A", "B", "N"]:
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