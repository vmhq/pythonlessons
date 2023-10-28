titulo = "¿Cuánto amas a tu chico?"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
print("Comenzamos con las preguntas" + "\n")

puntuacion = 0

print("Pregunta número 1: ¿Cuánto piensas en esta persona durante el día? \n" 
      "A: Rara vez \n" "B: A veces \n" "C: Todo el tiempo \n")

opcion = (input("Ingresa tu respuesta" + "\n"))

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las posibles opciones son solo A, B y C")
    exit()

print("Pregunta número 2:  Si esta persona necesita ayuda, ¿hasta qué punto estarías dispuesto a ayudar? \n" 
      "A: Solo si es conveniente para mí \n" 
      "B: Ayudaría, pero con ciertos límites \n" 
      "C: Haría lo que fuera necesario \n")

opcion = (input("Ingresa tu respuesta" + "\n"))

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las posibles opciones son solo A, B y C")
    exit()

print("Pregunta número 3: ¿Qué sientes cuando están juntos? \n" 
      "A: Nada especial \n" 
      "B: Felicidad \n" 
      "C: Un sentimiento indescriptible de alegría y completitud \n")

opcion = (input("Ingresa tu respuesta" + "\n"))

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las posibles opciones son solo A, B y C")
    exit()

print("Pregunta número 4: ¿Te ves construyendo un futuro con esta persona? \n" 
      "A: No lo he considerado \n" 
      "B: Podría ser \n" 
      "C: Absolutamente \n")

opcion = (input("Ingresa tu respuesta" + "\n"))

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las posibles opciones son solo A, B y C")
    exit()

print("La puntuación obtenida es {} \n" .format(puntuacion))

if puntuacion > 25:
    print("Estás ultra mega enamorade, lo lógico es que pidas matrimonio chiquitito.")
elif puntuacion >= 15:
    print("Mas  o menos: Solo te gusta.")
else:
    print("Muy muy mal, no estás enamorade. Deja de engañar.")
