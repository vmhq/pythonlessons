import random

titulo = "Escape del borde exterior Galáctico"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

#Se presenta al jugador la introducción a la historia.
print("Al levantar la vista luego del impacto,"
      "te das cuenta que te encuentras en la superficie de un planeta desconocido, tomando conocimiento de que \n"
      "tu nave espacial se estrellado." + "\n")
print("Observas a tu alrededor, a lo lejos observas un bosque frondoso, el cual podrías explorar \n" 
      "o podrías explorar los alrededor de la nave en busca de suministros para reparar las comunicaciones \n")

#Se presente al jugador la primera desición que debe tomar.
print("Tienes dos caminos \n" 
      "A: Te adentras en bosque para explorarlo \n" 
      "B: Explorar los alrededores en busca de suministros \n")

opcion = input("¿Qué escoges? [A/B] \n").upper()

#Se desprenden las condiciones de acuerdo al camino que haya escogido el jugador.
if opcion == "A":
      print("Te adrentas en el bosque, en donde observas una edificación antigua, a la cual ingresas. \n" 
            "Al interior encuentras una especie de dispositivo de comunicaciones. \n" 
            "Tienes dos opciones: \n" 
            "A: Activas el dispositivo \n" 
            "B: No activas el dispositivo \n")
      opcion_caminoa = input("¿Qué escoges? [A/B] \n").upper()
      if opcion_caminoa == "A":
            print("Al activar el dispositivo, este comienza a emitir una luz brillante. \n"
                  "Está luz se intensifica de tal forma que emite un destello... \n"
                  "¡Estás muerto! \n")
      elif opcion_caminoa == "B":
            print("Al no activar el dispositivo de comunicaciones, no logras tomar contacto con su receptor. \n"
                  "Te quedas en planeta, al no tener suminsitros finalmente al paso del tiempo y mueres de hambre. \n")

#Se desprenden las condiciones para el segundo camino posible.
elif opcion == "B":
      print("Al expLorar los alrededores de la nave, encuentras un artefacto el cual tiene el aspecto de un \n"
            "Traductor universal, pero al no conocer su origen dudas si tomarlo o no: \n"
            "A: Tomas el artefacto \n"
            "B: No tomas el artefacto \n")
      artefacto_inventario = input("¿Lo tomas? [A/B] \n").upper()

      panel_numero_random = random.randint (1, 10)
      print("Al seguir buscando en los alrededores, encuentras una estructura la cual cuenta con un panel \n"
            "En el panel alienigina te muestra un problema matemático para desbloquearlo \n"
            "Cuanto es 5 * {}" .format(panel_numero_random))
      resultado_puzzle = int(input("¿Cuál es el resultado? \n"))

      if resultado_puzzle == 5 * panel_numero_random and artefacto_inventario == "A":
            print("El panel se abre y despliega un mapa. \n"
                  "Como cuentas con el artefacto de traducción, logras decifrar el mapa, \n" ""
                  "lo que te permite ubicar una estación de comunicación cercana y asi salir del planeta \n")
      elif resultado_puzzle == 5 * panel_numero_random and artefacto_inventario == "B":
            print("El panel se abre y despliega un mapa, pero al no tomar el artefacto de traducción, \n"
                  "no cuentas con una herramienta para decifrarlo, por lo que te quedas sin suministros. \n"
                  "Al final del paso dle tiempo mueres. \n")
      elif resultado_puzzle != 5 * panel_numero_random and artefacto_inventario == "A":
            print("Al no lograr desbloquear el panel, no obtienes lo que este almacena, por lo que decides forzarlo. \n"
                  "Al forzarlo el panel emite una descarga eléctrica, la cual te mata al instante. \n")
      elif resultado_puzzle != 5 * panel_numero_random and artefacto_inventario == "B":
            print("Al no contar con el artefacto de traducción y no lograr desbloquer el panel, \n"
                  "Implica que te quedes sin suministros, por lo que al paso del tiempo mueres de inanición. \n")
      else:
            print("Mueres repentinamente...")
            exit()

else:
      print("No has escogido una respuesta válida, por lo que no queda mas que morir.")
      exit()
