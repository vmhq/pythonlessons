# Se importan las librerías necesarias
import readchar
import os  # Importa la librería os

# Se definen las constantes
POS_X = 0 
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [7,6]

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
    print("señala en que dirección deseas moverte, utiliza [WASD] > ")
    direction = readchar.readchar().upper()

    if direction == "W":
        my_position[POS_Y] -= 1
    elif direction == "S":
        my_position[POS_Y] += 1
    elif direction == "A":
        my_position[POS_X] -= 1
    elif direction == "D":
        my_position[POS_X] += 1
