'''
Ejercicio 1: La string más larga

Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas

Ejemplo:

string_mas_larga("hola", "como", "estas")

> "estas"



Ejercicio 2: Sumando la lista

Crea una función que sume una lista de números, no se vale usar la función sum()

Ejemplo:

suma([1, 2, 3, 4, 5])

> 15



Ejercicio 3: Par o impar

Crea una función que te de True como resultado si el número pasado como argumento es impar

Ejemplo:

es_impar(3)

> True

es_impar(24)

> False



Ejercicio 4: Pregunta algo

Crea una función que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False" 
dependiendo de si el usuario está seguro.



Ejercicio 5: A mayus

Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()



Ejercicio 6: Adivina el número

Crea una función que reciba como argumento un número del 1 al 100 a adivinar y que le pregunte al usuario que adivine el número. 
El código se ejecutará hasta que el usuario adivine.



Ejercicio 7: Lista de la compra

Crea una función que dada una lista de la compra definida fuera de la función, 
permita al usuario añadir un nuevo item asegurandose que no exista anteriormente en la lista.
'''

# Ejercicio 1
def string_mas_larga(lista_de_strings):
    mas_larga = ""
    for palabra in lista_de_strings:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
    return mas_larga

# Uso de la función
resultado = string_mas_larga(["hola", "como", "estas"])
print("La palabra más larga es: {}".format(resultado))  # Debería imprimir "estas"

# Ejercicio 2
def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total 

resultado = suma([4, 3, 6, 7, 9, 10])
print("La suma de todos los números es: {}".format(resultado))

# Ejercicio 3
def es_impar(numero):
    return numero % 2 != 0  # Devuelve True si el número es impar, False en caso contrario

# Uso de la función
print(es_impar(3))  # Debería imprimir True
print(es_impar(24))  # Debería imprimir False

# Ejercicio 4
def esta_seguro():
    respuesta = input("¿Estás seguro? [sí/no]:\n> ").lower()
    if respuesta == 'sí' or respuesta == 'si' or respuesta == 's':
        return True
    else:
        return False

# Uso de la función
resultado = esta_seguro()
print(resultado)  # Debería imprimir True si el usuario dijo que está seguro, y False en caso contrario

# Ejercicio 5
def a_mayus(cadena):
    resultado = ""
    for caracter in cadena:
        if 'a' <= caracter <= 'z':  # Verifica si el carácter es una letra minúscula
            caracter_mayus = chr(ord(caracter) - 32)  # Convierte a mayúscula usando el código ASCII
        else:
            caracter_mayus = caracter  # Si no es una letra minúscula, lo deja igual
        resultado += caracter_mayus  # Añade el carácter al resultado final
    return resultado

# Uso de la función
print(a_mayus("Hola Mundo"))  # Debería imprimir "HOLA MUNDO"

# Ejercicio 6
def adivina_numero(numero_a_adivinar):
    acertado = False
    while not acertado:
        numero_usuario = int(input("Intenta adivinar el número del 1 al 100:\n> "))
        
        if numero_usuario == numero_a_adivinar:
            print("¡Has acertado! 🎉")
            acertado = True
        elif numero_usuario < numero_a_adivinar:
            print("El número es más grande. 📈 Intenta otra vez.")
        else:
            print("El número es más pequeño. 📉 Intenta otra vez.")

# Uso de la función
adivina_numero(42)  # Puedes cambiar el número a adivinar

# Ejercicio 7
def agregar_item(lista_compra):
    nuevo_item = input("Introduce el nuevo ítem que quieres añadir a la lista de la compra:\n> ")
    
    if nuevo_item.lower() in [item.lower() for item in lista_compra]:
        print("Este ítem ya existe en la lista. 😅")
    else:
        lista_compra.append(nuevo_item)
        print("¡Ítem {} añadido a la lista! 🎉".format(nuevo_item))

# Lista de la compra definida fuera de la función
mi_lista_compra = ["pan", "leche", "huevos"]

# Uso de la función
agregar_item(mi_lista_compra)
print("Lista de la compra actualizada:", mi_lista_compra)

