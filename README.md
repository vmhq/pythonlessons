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
- [Machine Learning y Tipos de Modelos](#machine-learning-y-tipos-de-modelos)
- [Red Neuronal Artificial](#red-neuronal-artificial)
  - [Perceptrón en Redes Neuronales](#perceptrón-en-redes-neuronales)

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

## Machine Learning y Tipos de Modelos
Al trabajar con Machine Learning (ML) y Python, elegimos diferentes tipos de modelos basándonos en la naturaleza de nuestro problema. Para predecir si un dispositivo es reparable, aplicaríamos modelos de clasificación ya que buscamos una respuesta binaria: reparable o no reparable. Aquí hay una breve descripción de tres tipos comunes de modelos:

- **Regresión Lineal**: A pesar de que no se aplica directamente a problemas de clasificación, es importante mencionarla. Se utiliza para predecir valores continuos, pero no categorías. Aun así, es la base sobre la que se construyen otros modelos como la regresión logística.

- **Regresión Logística**: Es un modelo de clasificación que estima la probabilidad de que una instancia pertenezca a una clase. Aunque su nombre sugiere una relación con la regresión lineal, se utiliza para clasificación binaria y es efectiva cuando la relación entre la variable dependiente y las independientes es logística o sigmoidea.

- **Árboles de Decisión**: Son modelos versátiles que se pueden utilizar tanto para clasificación como para regresión. Son particularmente útiles cuando las relaciones entre los predictores no son lineales y hay interacciones complejas. Los árboles de decisión dividen el conjunto de datos en subconjuntos basados en el valor de las características, lo que hace que el modelo sea fácil de interpretar.

La elección entre estos modelos depende de varios factores como la linealidad de los datos, la necesidad de interpretabilidad y la complejidad del problema. La regresión logística es a menudo una primera línea de ataque para problemas de clasificación debido a su simplicidad y eficiencia. Por otro lado, los árboles de decisión son más flexibles y fáciles de interpretar, lo que puede ser invaluable en ciertas aplicaciones empresariales.

La programación en ML es intrínsecamente diferente de la programación convencional. En lugar de codificar reglas específicas y lógica de programación, entrenamos a los modelos con datos para que aprendan patrones. Este enfoque requiere una comprensión profunda de los datos y estadísticas, ya que la calidad de los datos y la selección del modelo afectan directamente el rendimiento y la precisión. Además, los modelos de ML raramente alcanzan una precisión del 100% debido a la presencia de ruido en los datos, la posibilidad de sobreajuste y la naturaleza a menudo probabilística de las predicciones.

## Red Neuronal Artificial

Una **red neuronal artificial** (RNA) es un sistema de procesamiento de información que se inspira en la forma en que las redes neuronales biológicas del cerebro humano procesan la información. Una RNA está compuesta de un número de **perceptrones** (neuronas artificiales) organizados en capas: capa de entrada, una o más capas ocultas y una capa de salida.

### Estructura de una Red Neuronal

- **Capa de Entrada**: Recibe las señales de entrada (características o datos brutos) y las pasa a la siguiente capa.

- **Capas Ocultas**: Realizan la mayoría de los cálculos necesarios y están compuestas por perceptrones como los descritos anteriormente. Cada capa extrae características de nivel más alto que la anterior.

- **Capa de Salida**: Produce la salida final del modelo, que puede ser un valor continuo (en el caso de la regresión) o una clase (en el caso de la clasificación).

### Funcionamiento

1. **Propagación hacia adelante**: Las entradas se introducen en la red y se procesan capa por capa, a través de los pesos y funciones de activación, hasta generar una salida.

2. **Retropropagación y Aprendizaje**: Utiliza algoritmos como el de descenso del gradiente para ajustar los pesos de la red en función del error de la salida obtenida comparada con la salida deseada.

3. **Iteración**: El proceso de propagación y retropropagación se repite muchas veces, y en cada iteración, la RNA ajusta sus pesos internos con el objetivo de minimizar el error de sus predicciones.

Las redes neuronales son capaces de aprender y modelar relaciones no lineales complejas entre los datos de entrada y salida, lo que las hace muy efectivas para tareas como reconocimiento de voz, imagen y patrones, traducción de idiomas y muchas otras aplicaciones de inteligencia artificial.

### Perceptrón en Redes Neuronales

El **perceptrón** es un tipo de neurona artificial y es el bloque constructivo básico de una red neuronal. Se compone de varias partes:

- **Entradas (X1, X2, X3)**: Son los datos de entrada que recibe la neurona. En una red neuronal, estas podrían ser características o señales de entrada.

- **Pesos (W)**: Cada entrada está asociada con un peso que modifica la señal de entrada. Los pesos son ajustables y se optimizan durante el entrenamiento de la red.

- **Sesgo**: Es un término adicional en la neurona que permite ajustar la salida además de los pesos. Funciona como un umbral que determina cuán fácil es que la neurona se active.

- **Suma ponderada**: Las entradas multiplicadas por sus pesos se suman junto con el sesgo. Esto se puede representar como `suma ponderada = (X1 * W1) + (X2 * W2) + (X3 * W3) + sesgo`.

- **Función de Activación**: La suma ponderada se pasa a través de una función de activación, que determina la salida de la neurona. Las funciones de activación comunes incluyen la sigmoide, tanh y ReLU.

- **Salida**: Es el resultado final de la neurona después de aplicar la función de activación. Esta salida puede ser utilizada directamente o ser la entrada a otra neurona en una red de múltiples capas.

El perceptrón es un modelo lineal, lo que significa que toma una decisión de clasificación basada en una combinación lineal de los pesos y entradas. Los perceptrones pueden manejar problemas de clasificación binaria y son la base sobre la cual se construyen redes neuronales más complejas.

