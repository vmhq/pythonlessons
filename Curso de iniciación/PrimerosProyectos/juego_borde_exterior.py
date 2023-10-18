titulo = "Escape del borde exterior galáctico"

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
            "Al interior encuentras una especie de dispositivo de comunicaciones \n" 
            "Tienes dos opciones: \n" 
            "A: Activas el dispositivo \n" 
            "B: No activas el dispositivo \n")
      opcion = input("¿Qué escoges? [A/B]")
      if opcion == "A":
            print("Al activar el dispositivo, este comienza a emitir una luz brillante. \n"
                  "Está luz se intensifica de tal forma que emite un detello... \n"
                  "¡Estás muerto! \n")
      elif opcion == "B":
            print("Al no activar el dispositivo no logras tomar contacto ")
