'''

Juego del Snake

Importación de Librerías: Importa las librerías necesarias (readchar, os, random).

Definición de Constantes y Variables Iniciales: Establece las dimensiones del mapa (MAP_WIDTH, MAP_HEIGHT), 
la posición inicial (my_position), y la longitud de la cola (tail_leght).

Objetos en el Mapa: Inicializa una lista de objetos (map_objects) que se ubicarán de forma aleatoria en el mapa.

Bucle Principal: Un bucle while True que se encarga de las siguientes tareas:

a. Limpiar Pantalla: Limpia la consola antes de dibujar un nuevo cuadro del juego.

b. Dibujar el Mapa: Dibuja el mapa, el personaje y los objetos. Si el personaje se cruza con un objeto, 
éste desaparece y la longitud de la cola aumenta (tail_leght += 1).

c. Recoger Entrada del Usuario: Solicita que el usuario introduzca una dirección (W, A, S, D) para mover el personaje o Q 
para salir del juego.

d. Mover el Personaje: Según la tecla presionada, se actualiza la posición del personaje y su cola. Si eliges "W", 
por ejemplo, la posición en Y disminuirá en 1, y la cabeza de la cola se actualizará para que coincida con la posición anterior del personaje.

e. Verificar Colisión con la Cola: Después de mover al personaje, el código verifica si la nueva posición de 
la cabeza choca con algún segmento de la cola (tail[1:]). Si es así, el juego termina y se muestra un mensaje de "¡Has chocado con tu propia cola! 😢 Fin del juego".

f. Salir del Juego: Si se presiona "Q", se rompe el bucle y el juego termina.
'''

# Se importan las librerías necesarias
import readchar
import os
import random

# Se definen las constantes
POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

NUM_OBJECTS = 11

# Posición inicial y tamaño de la cola.
my_position = [3, 1]
tail_leght = 0 
tail = []

# Se definen los objetos en el mapa de forma aleatoria.
map_objects = []
while len(map_objects) < NUM_OBJECTS:
    new_object = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
    if new_object not in map_objects and new_object != my_position:
        map_objects.append(new_object)

# Bucle principal del juego
while True:
    # Limpia la pantalla
    if os.name == 'posix':  # Para sistemas Unix (macOS, Linux)
        os.system('clear')
    else:  # Para Windows
        os.system('cls')
        
    # Dibuja el mapa
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = "@"
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_leght += 1
                    # Cuando se come un objeto se añade uno más de forma aleatoria. 
                    while True:
                        new_object = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
                        if new_object not in map_objects and new_object != my_position:
                            map_objects.append(new_object)
                            break
            print(" {} " .format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Solicita una dirección al usuario
    while True:
        print("Señala en qué dirección deseas moverte, utiliza [WASD] o [Q] para salir del juego. \n> ", end="")
        direction = readchar.readchar().upper()

        if direction in ["W", "S", "A", "D", "Q"]:
            break
        else:
            print("Dirección no válida ❌. Por favor, intenta de nuevo.")

    if direction == "W":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_leght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "S":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_leght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "A":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_leght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "D":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_leght]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "Q":
        break

    # Verificar si choca con su cola
    if my_position in tail[1:]:
        os.system('clear') if os.name == 'posix' else os.system('cls')
        print("¡Has chocado con tu propia cola! 😢 Fin del juego.")
        break
