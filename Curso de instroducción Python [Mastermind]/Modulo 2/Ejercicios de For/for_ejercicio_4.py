'''
Explicación del código

1. `numero_usuario = int(input("¿De qué número desea la tabla de multiplicar > "))`
   - `input()`: Esta función recoge una entrada (texto) del usuario.
   - `int()`: Esta función convierte el texto recogido a un número entero.
   - Así que, en esta línea, el programa le pide al usuario un número y lo guarda en la variable `numero_usuario`.

2. `for n in range(1, 11):`
   - Esto inicia un bucle `for` que se ejecutará con valores de `n` desde 1 hasta 10 (el segundo argumento en `range()` es exclusivo).

3. `if n % 2 == 0:`
   - Esta es una condición que verifica si el número `n` es par. Si el residuo de la división de `n` entre 2 es 0, entonces el número es par.

4. `print("{} * {} = {}" .format(n, numero_usuario, n * numero_usuario))`
   - Esta línea imprime la multiplicación. Si `n` es par (debido a la condición anterior), se mostrará el resultado de multiplicar ese número par `n` por `numero_usuario`.
   - `.format(n, numero_usuario, n * numero_usuario)` sustituye las `{}` en el string con los valores proporcionados en orden.

En resumen, el código le pide al usuario un número y luego imprime la tabla de multiplicar de ese número, pero solo para números pares entre 1 y 10.
'''

numero_usuario = int(input("¿De qué número desea la tabla de multiplicar > "))

for n in range(1, 11):
    if n % 2 == 0:
        print("{} * {} = {}" .format(n, numero_usuario, n * numero_usuario))

