# Python 🐍

Este repositorio contiene todos los códigos escritos en Python durante mi proceso de aprendizaje de este lenguaje de programación.

## Tabla de contenidos
- [Funciones en Python](#funciones-en-python)
  - [Numéricas](#funciones-numéricas)
  - [Cadenas](#funciones-de-cadena)
  - [Listas](#funciones-de-lista)
  - [Tipo](#funciones-de-tipo)
  - [Input/Output](#inputoutput)
  - [Importación y Sistema](#importación-de-módulos-y-comandos-del-sistema)
  - [Conversión de Tipo](#conversión-de-tipo)
  - [Otros](#otros)
- [Listas](#listas-en-python)
- [Operaciones Booleanas](#operaciones-booleanas-en-python)
- [Estructuras de Control](#estructuras-de-control-en-python)

## Funciones en Python
Resumen y ejemplos de funciones comunes en Python.

### Funciones Numéricas
- `abs(x)`: Valor absoluto de `x`.
- `round(x)`: Redondeo de `x`.
- `max(x, y, ...)`: Valor máximo.
- `min(x, y, ...)`: Valor mínimo.

### Funciones de Cadena
- `len(s)`: Longitud de `s`.
- `str(x)`: Convierte a cadena.

### Funciones de Lista
- `len(l)`: Longitud de `l`.
- `sorted(l)`: Lista ordenada.

### Funciones de Tipo
- `type(x)`: Tipo de `x`.

### Input/Output
- `input(s)`: Entrada del usuario.
- `print(x)`: Imprimir `x`.

### Importación de Módulos y Comandos del Sistema
- `import [module_name]`: Importar módulo.
- `os.system(command)`: Comando del SO.

### Conversión de Tipo
- `int(x)`: A entero.
- `float(x)`: A número flotante.

### Otros
- `range(x, y, z)`: Secuencia de números.
- `help()`: Ayuda integrada.

---

## Listas en Python
Definición, ejemplos y operaciones básicas con listas.

```python
mi_lista = [1, 2, 3, "hola"]
```

---

## Operaciones Booleanas en Python
Ejemplos y explicaciones de operaciones booleanas.

```python
True and False # Devuelve False
```

---

## Estructuras de Control en Python
Explicación y ejemplos de estructuras de control comunes.

### While
Loop que continúa mientras se cumple una condición.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### If, Elif, Else
Condiciones y bloques de código condicional.

```python
x = 1
if x > 5:
    print("x es mayor que 5")
elif x == 3:
    print("x es igual a 3")
else:
    print("x es menor que 5 y diferente de 3")
```

### Continue
Salta a la siguiente iteración del bucle.

```python
contador = 0
while contador < 5:
    if contador == 2:
        contador += 1
        continue
    print(contador)
    contador += 1
```

### Break
Sale del bucle actual.

```python
contador = 0
while contador < 5:
    if contador == 3:
        break
    print(contador)
    contador += 1
```