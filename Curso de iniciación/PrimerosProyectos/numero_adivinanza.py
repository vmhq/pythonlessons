import random

print("Bienvenido al juego de adivina el número")
print("Adivina un número entero entre 1 al 10")

import random
a = random.randint(1, 10)
b = int(input("Ingresa el número que crees que es el correcto: "))

if b == a:
    print("Correcto el número es {}" .format(a))

if b > 10:
    print("Te has pasado, es entre 1 y 10")

if b < 1:
    print("No puede ser menor a 1, es entre 1 y 10")

if b != a:
    print("El número ganador es {}" .format(a))

