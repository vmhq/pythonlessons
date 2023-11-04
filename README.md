# Python 🐍

Python es uno de los lenguajes de programación más populares y versátiles en la actualidad. Su simplicidad y legibilidad hacen que sea un lenguaje ideal para principiantes, pero también es poderoso y ampliamente utilizado en la industria para desarrollar aplicaciones web, análisis de datos, inteligencia artificial y muchas otras áreas. Aprender Python es una inversión valiosa, ya que abre puertas a una variedad de oportunidades en el mundo de la tecnología y más allá.


## Tabla de contenidos
- [Acerca de este repositorio](#acerca-de-este-repositorio)
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
- [Definición de Funciones con `def`](#definición-de-funciones-con-def)
- [Extracción de Datos con `requests-html`](#extracción-de-datos-con-requests-html)

## Acerca de este repositorio
Este repositorio contiene todos los códigos escritos en Python durante el proceso de aprendizaje de este lenguaje de programación.

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

## Definición de Funciones con `def`
En Python, se pueden crear funciones personalizadas utilizando la palabra clave `def`. Una función es un bloque de código reutilizable que realiza una acción específica. Al definir una función, puedes optar por establecer parámetros que la función usará durante su ejecución.

### Sintaxis básica

```python
def nombre_de_funcion(parametro1, parametro2, ...):
    # Código de la función
    return valor_de_retorno
```

### Ejemplo 🌈
Aquí hay un ejemplo simple que muestra cómo definir una función para calcular el área de un rectángulo.

```python
def area_rectangulo(base, altura):
    return base * altura

# Usando la función
base = 5
altura = 10
area = area_rectangulo(base, altura)
print(f"El área del rectángulo con base {base} y altura {altura} es {area}.")
```

Este código define una función llamada `area_rectangulo` que toma dos parámetros: `base` y `altura`. La función calcula el área multiplicando estos dos valores y luego devuelve el resultado.

Por supuesto, aquí tienes la sección añadida sobre cómo usar `requests-html` en Python, para incluirla en tu archivo README:

## Extracción de Datos con `requests-html`

La biblioteca `requests-html` es una poderosa herramienta en Python para realizar solicitudes web y manipular datos de HTML/XML. Es especialmente útil para web scraping, es decir, extraer datos de sitios web de forma programática.

### Instalación
Primero, necesitas instalar el paquete usando `pip`:
```bash
pip install requests-html
```

### Uso Básico
Para comenzar a usar `requests-html`, primero debes importar la clase `HTMLSession` del módulo:

```python
from requests_html import HTMLSession
```

Luego, crea una sesión y realiza una solicitud a la URL deseada:

```python
session = HTMLSession()
respuesta = session.get('https://ejemplo.com')
```

Puedes acceder al contenido de la respuesta y realizar búsquedas de elementos HTML utilizando selectores CSS:

```python
# Acceder al texto completo de la página
texto_de_la_pagina = respuesta.text

# Encontrar un elemento con su ID
elemento_con_id = respuesta.html.find('#id_del_elemento', first=True)

# Buscar todos los elementos de una clase específica
elementos_con_clase = respuesta.html.find('.clase_del_elemento')
```

Para interactuar con JavaScript en sitios web dinámicos, puedes utilizar el método `.render()` que ejecuta JavaScript en la página:

```python
respuesta.html.render()
```

Ten en cuenta que `render()` requiere instalaciones adicionales como Chromium, que `requests-html` intentará descargar la primera vez que se ejecute.

### Ejemplo Práctico
Aquí hay un ejemplo simple de cómo extraer títulos de un blog:

```python
# Crea una sesión
session = HTMLSession()

# Realiza una solicitud GET a la página del blog
respuesta = session.get('https://blog.ejemplo.com')

# Renderiza la página para ejecutar JavaScript
respuesta.html.render()

# Busca todos los elementos que contienen los títulos de las publicaciones
titulos = respuesta.html.find('h1.titulo_del_post')

# Imprime los títulos encontrados
for titulo in titulos:
    print(titulo.text)
```

Este script imprime los títulos de las publicaciones de un blog ficticio, buscando en la página los `h1` con la clase `titulo_del_post`.