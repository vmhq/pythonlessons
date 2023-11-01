# Se importan las librerías necesarias
import os
import random
import readchar

# Se definen las constantes.
POS_X = 0
POS_Y = 1
NUM_TRAINERS = 4
TRAINERS = [[22, 8], [20, 2], [9, 10], [15, 15]]
TRAINER_1 = [22, 8]
TRAINER_2 = [20, 2]
TRAINER_3 = [9, 10]
TRAINER_4 = [15, 15]

VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_CHARMANDER = 98
VIDA_INICIAL_SQUIRTLE = 89
VIDA_INICIAL_TREECKO = 80
VIDA_INICIAL_ZUBAT = 79
TAM_BARRA_VIDA = 20

# VARIABLES
my_position = [12, 10]
quit_game = False
end_game = False
died = None
vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_charmander = VIDA_INICIAL_CHARMANDER
vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE
vida_actual_treecko = VIDA_INICIAL_TREECKO
vida_actual_zubat = VIDA_INICIAL_ZUBAT

# Mapa
obstacle_definition = """\
##############################
###########                  #
##############               #
##################           #
#####################        #
###################         ##
###################       ####
##############           #####
#######                 ######
####                  ########
#######                    ###
###########                 ##
################             #
#####################       ##
##################         ###
###############         ######
###########           ########
#####               ##########
##############################\
"""

# Creación de bostaculos en el mapa
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

while len(TRAINERS) > 0:
    os.system('clear') if os.name == 'posix' else os.system('cls') #Limpia la pantalla 
    if end_game:
        break

    # Se dibuja el mapa
    print("+" + ("-" * MAP_WIDTH * 2) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            coach_in_myself = None

            for trainer in TRAINERS:
                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    coach_in_myself = trainer

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                if coach_in_myself:
                    os.system('clear') if os.name == 'posix' else os.system('cls')  # Limpia la pantalla l
                    TRAINERS.remove(coach_in_myself)
                    input("\n🚨 Has encontrado a un entrenador pokemon, preparate para combatir. 👉 Enter para continuar... \n")

                    # Se define cual entrenador debes combatir
                    name = None
                    first_attack = None
                    second_attack = None
                    vida_actual_enemigo = None
                    VIDA_INICIAL_ENEMIGO = 0
                    DANO_PRIMER_ATAQUE = None
                    DANO_SEGUNDO_ATAQUE = None

                    if my_position[POS_X] == TRAINER_1[POS_X] and my_position[POS_Y] == TRAINER_1[POS_Y]:
                        name = "Charmander"
                        first_attack = "Lanza llamas"
                        second_attack = "Nitro carga"
                        vida_actual_enemigo = vida_actual_charmander
                        VIDA_INICIAL_ENEMIGO = vida_actual_charmander
                        DANO_PRIMER_ATAQUE = 10
                        DANO_SEGUNDO_ATAQUE = 13

                    elif my_position[POS_X] == TRAINER_2[POS_X] and my_position[POS_Y] == TRAINER_2[POS_Y]:
                        name = "Squirtle"
                        first_attack = "Burbuja"
                        second_attack = "Ataque rapido"
                        vida_actual_enemigo = vida_actual_squirtle
                        VIDA_INICIAL_ENEMIGO = vida_actual_squirtle
                        DANO_PRIMER_ATAQUE = 14
                        DANO_SEGUNDO_ATAQUE = 12

                    elif my_position[POS_X] == TRAINER_3[POS_X] and my_position[POS_Y] == TRAINER_3[POS_Y]:
                        name = "Treecko"
                        first_attack = "Drenadoras"
                        second_attack = "Latigazo"
                        vida_actual_enemigo = vida_actual_treecko
                        VIDA_INICIAL_ENEMIGO = vida_actual_treecko
                        DANO_PRIMER_ATAQUE = 10
                        DANO_SEGUNDO_ATAQUE = 11

                    elif my_position[POS_X] == TRAINER_4[POS_X] and my_position[POS_Y] == TRAINER_4[POS_Y]:
                        name = "Zubat"
                        first_attack = "Mordisco"
                        second_attack = "Bomba lodo"
                        vida_actual_enemigo = vida_actual_zubat
                        VIDA_INICIAL_ENEMIGO = vida_actual_zubat
                        DANO_PRIMER_ATAQUE = 12
                        DANO_SEGUNDO_ATAQUE = 13

                    # Bucle Combate
                    while vida_actual_pikachu > 0 and vida_actual_enemigo > 0:
                        # Turno del enemigo
                        print("👉 Turno de {} \n".format(name))
                        ataque_enemigo = random.randint(1, 2)
                        if ataque_enemigo == 1:
                            print("{} ataca con {} \n".format(name, first_attack))
                            vida_actual_pikachu -= DANO_PRIMER_ATAQUE
                        else:
                            print("{} ataca con {} \n".format(name, second_attack))
                            vida_actual_pikachu -= DANO_SEGUNDO_ATAQUE

                        # Vida de los pokemones
                        if vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0
                        if vida_actual_enemigo < 0:
                            vida_actual_enemigo = 0

                        barra_pikachu = int(vida_actual_pikachu * TAM_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:    [{}{}][{}/{}]".format("#" * barra_pikachu,
                                                                 " " * (TAM_BARRA_VIDA - barra_pikachu),
                                                                 vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_enemigo = int(vida_actual_enemigo * TAM_BARRA_VIDA / VIDA_INICIAL_ENEMIGO)
                        print("{}:    [{}{}][{}/{}] \n".format(name, "#" * barra_enemigo,
                                                            " " * (TAM_BARRA_VIDA - barra_enemigo),
                                                            vida_actual_enemigo, VIDA_INICIAL_ENEMIGO))

                        input("Enter para continuar...")
                        os.system('clear') if os.name == 'posix' else os.system('cls') #Limpia la pantalla 

                        # Turno Pikachu
                        print("👉 Turno de pikachu \n")

                        ataque_pikachu = None
                        primer_ataque_pikachu = 21
                        segundo_ataque_pikachu = 24

                        while ataque_pikachu not in ["V", "T"]:
                            ataque_pikachu = input("Elige tu ataque: [Bola [V]oltio, Onda [T]rueno] \n>").upper()

                        if ataque_pikachu == "V":
                            print("Pikachu ataca con Bola Voltio ⚡️ \n")
                            vida_actual_enemigo -= primer_ataque_pikachu
                        elif ataque_pikachu == "T":
                            print("Pikachu ataca con Onda Trueno ⚡️ \n")
                            vida_actual_enemigo -= segundo_ataque_pikachu

                        if vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0
                        if vida_actual_enemigo < 0:
                            vida_actual_enemigo = 0

                        barra_pikachu = int(vida_actual_pikachu * TAM_BARRA_VIDA / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:    [{}{}][{}/{}]".format("#" * barra_pikachu,
                                                                 " " * (TAM_BARRA_VIDA - barra_pikachu),
                                                                 vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_enemigo = int(vida_actual_enemigo * TAM_BARRA_VIDA / VIDA_INICIAL_ENEMIGO)
                        print("{}:    [{}{}][{}/{}] \n".format(name, "#" * barra_enemigo,
                                                            " " * (TAM_BARRA_VIDA - barra_enemigo),
                                                            vida_actual_enemigo, VIDA_INICIAL_ENEMIGO))

                        input("Enter para continuar...")
                        os.system('clear') if os.name == 'posix' else os.system('cls') #Limpia la pantalla 

                    if vida_actual_pikachu > vida_actual_enemigo:
                        print("✨ Pikachu gana \n")
                        print("💪 Se te ha regenerado la vida")
                        vida_actual_pikachu = VIDA_INICIAL_PIKACHU
                        input("Enter para continuar...")
                        os.system('clear') if os.name == 'posix' else os.system('cls') #Limpia la pantalla 
                    elif vida_actual_enemigo > vida_actual_pikachu:
                        print("{} gana, has perdido ❌".format(name))
                        end_game = True
                        died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + ("-" * MAP_WIDTH * 2) + "+")

    # Movimientos del jugador
    print("Señala en qué dirección deseas moverte, utiliza [WASD] o [Q] para salir del juego. \n> ", end="")
    direction = readchar.readchar().upper()
    new_position = None

    if direction == "W":
        new_position = my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH

    elif direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "Q":  
        end_game = True
        quit_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

# Término del juego
if died:
    print("\n❌ ¡Has muerto! ❌")
elif quit_game:
    print("\n👋 Has salido del juego 👋")
else:
    os.system('clear') if os.name == 'posix' else os.system('cls') #Limpia la pantalla 
    print("\n✨¡Felicidades, derrotaste a todos los pokemon, has ganado!✨")