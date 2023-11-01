def saludo_secreto(nombre):
    print("Hola {}" .format(nombre[::-1]))


saludo_secreto(input("Introduce un nombre "))

