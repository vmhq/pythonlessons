'''
Ejercicio 2

Crea un programa que contenga una función que calcule la potencia de un numero introducido como argumento, por ejemplo:

print(potencia(3))

> 9

print(potencia(5))

> 25
'''

# Definir la función potencia
def potencia(base):
    return base ** 2

# Definir la función principal del programa
def main():
    base_usuario = int(input("Introduce el número base:\n> "))
    resultado = potencia(base_usuario)
    print("El resultado de {} al cuadrado es {}".format(base_usuario, resultado))

# Verificar si el script se ejecuta como programa principal
if __name__ == "__main__":
    main()
