'''
Este código en Python permite al usuario ingresar una lista de números y luego encuentra el número más grande 
y el número más pequeño de esa lista.

En primer lugar, se crea una lista vacía llamada "numero_usuario" para almacenar los números ingresados por el usuario.

A continuación, se le pide al usuario que ingrese un número 
y se agrega a la lista "numero_usuario" mediante la función "append()".

Luego, se inicializan dos variables llamadas "numero_grande" y "numero_pequenio" con el valor del primer 
número ingresado por el usuario.

Después, se inicia un bucle "while" que continúa pidiendo al usuario si desea ingresar otro número 
("S" para sí y "N" para no). Si el usuario responde "S", se le pide ingresar otro número 
y se verifica si ese número ya ha sido ingresado previamente. Si el número ya está en la lista "numero_usuario", 
se muestra un mensaje indicando que ese número ya ha sido ingresado. De lo contrario, se agrega el nuevo número a la lista.

Una vez que el usuario ha terminado de ingresar números, se itera sobre la lista "numero_usuario" a partir del 
segundo elemento (índice 1). Dentro de este bucle, se compara cada número con las variables "numero_pequenio" y "numero_grande". 
Si el número es menor que "numero_pequenio", se actualiza el valor de "numero_pequenio" con ese número. Si el número es mayor que "numero_grande", 
se actualiza el valor de "numero_grande" con ese número.

Finalmente, se muestra en pantalla el número más grande y el número más pequeño 
utilizando la función "format()" para insertar esos valores en el mensaje de salida.
'''

numero_usuario = []
numero_introducido = int(input("Ingresa un número > "))
numero_usuario.append(numero_introducido)

numero_grande = numero_usuario[0]
numero_pequenio = numero_usuario[0]

while input("Deseas instroducir otro número [S/N] > ").upper() == "S":
    numero_introducido = int(input("Ingresa un número > "))
    if numero_introducido in numero_usuario:
        print("{} ya lo ingresaste." .format(numero_introducido))
    else:
        numero_usuario.append(numero_introducido)

for numero in numero_usuario[1:]:
    if numero < numero_pequenio:
        numero_pequenio = numero
    if numero > numero_grande:
        numero_grande = numero
    

print("El numero más grande es {} y el más pequeño es {}" .format(numero_grande, numero_pequenio))