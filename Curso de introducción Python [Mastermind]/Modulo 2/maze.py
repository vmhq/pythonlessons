'''
Este código es un pequeño juego de consola en Python que permite mover un personaje representado por 
el símbolo "@" en un mapa. Aquí te explico sus partes principales:

Importación de librerías: Se importan readchar para leer un solo carácter del teclado 
y os para limpiar la pantalla.

Constantes: Se definen algunas constantes como POS_X, POS_Y, MAP_WIDTH y MAP_HEIGHT para manejar las dimensiones del mapa 
y la posición.

Posición inicial: Se establece la posición inicial del personaje en [3,1].

Bucle while True:: Este es el corazón del juego. Hace lo siguiente:

Limpia la pantalla.

Dibuja el mapa y coloca el personaje en su posición actual.

Pide al usuario una dirección para mover el personaje usando las teclas WASD o salir con Q.

Movimiento: Dependiendo de la tecla presionada, se actualiza la posición del personaje. 

Se usa el operador % para que el mapa sea "cíclico", es decir, si sales por un lado, apareces en el opuesto.
'''

# Se importan las librerías necesarias
import readchar # Importa la librería readchar.
import os  # Importa la librería os

# Se definen las constantes
POS_X = 0 
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

# Posición inicial.
my_position = [3,1]

# Se comienza a construir el mapa. 
while True:
    # Limpia la pantalla antes de imprimir el mapa
    if os.name == 'posix':  # Para sistemas Unix (macOS, Linux)
        os.system('clear')
    else:  # Para Windows
        os.system('cls')

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Se le solicita al usuario que ingrese una dirección para mover al jugador
    print("Señala en que dirección deseas moverte, utiliza [WASD] o [Q] para salir del juego. \n> ", end=(""))
    direction = readchar.readchar().upper()

    if direction == "W":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "S":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "A":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "D":
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "Q":
        break
