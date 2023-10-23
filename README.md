# Proceso de aprendizaje de Python

Repositorio con todos los códigos escritos en Python durante el proceso de aprendizaje de este lenguaje de programación.

# Guía de Python: Funciones y Estructuras de Control

## Funciones de Python

### Funciones Numéricas
- `abs(x)`: Devuelve el valor absoluto de `x`.
- `round(x)`: Redondea `x` al número entero más cercano.
- `max(x, y, ...)`: Devuelve el valor máximo entre `x`, `y`, etc.
- `min(x, y, ...)`: Devuelve el valor mínimo entre `x`, `y`, etc.

### Funciones de Cadena
- `len(s)`: Longitud de la cadena `s`.
- `str(x)`: Convierte `x` a una cadena.

### Funciones de Lista
- `len(l)`: Longitud de la lista `l`.
- `sorted(l)`: Devuelve una lista ordenada de `l`.

### Funciones de Tipo
- `type(x)`: Devuelve el tipo de `x`.

### Input/Output
- `input(s)`: Muestra una cadena `s` y espera una entrada del usuario.
- `print(x)`: Imprime `x`.

### Importación de Módulos y Comandos del Sistema
- `import [module_name]`: Importa un módulo llamado `module_name`.
- `os.system(command)`: Ejecuta un comando del sistema operativo.

### Conversión de Tipo
- `int(x)`: Convierte `x` a un entero.
- `float(x)`: Convierte `x` a un número de coma flotante.

### Otros
- `range(x, y, z)`: Genera una secuencia de números desde `x` hasta `y-1`, incrementando en `z`.
- `help()`: Invoca el sistema de ayuda integrado.

## Estructuras de Control en Python

### While
Loop que se ejecuta mientras una condición sea verdadera.
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### If
Evalúa una condición y ejecuta un bloque de código si es verdadera.
```python
x = 10
if x > 5:
    print("x es mayor que 5")
```

### Elif
Se utiliza después de un `if` para evaluar otra condición si la primera es falsa.
```python
x = 3
if x > 5:
    print("x es mayor que 5")
elif x == 3:
    print("x es igual a 3")
```

### Else
Se ejecuta si todas las condiciones anteriores son falsas.
```python
x = 1
if x > 5:
    print("x es mayor que 5")
elif x == 3:
    print("x es igual a 3")
else:
    print("x es menor que 5 y diferente de 3")
```