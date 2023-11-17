def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Función principal que ejecuta la calculadora
def calculadora():
    while True:
        print("Operaciones disponibles:\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")

        opcion = input("Elige una operación (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo de la calculadora.")
            break

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print("Resultado:", sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", dividir(num1, num2))
        else:
            print("Opción no válida")

# Ejecutar la calculadora
calculadora()
