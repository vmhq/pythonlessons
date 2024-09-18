'''
Este es un programa de conversión de divisas creado con Python. El usuario puede elegir entre varias opciones para convertir 
entre diferentes divisas. Las tasas de cambio se definen al principio del código. 
El programa solicita al usuario que elija una opción de conversión y luego solicita la cantidad de dinero 
que desea convertir. Finalmente, realiza la conversión y muestra el resultado al usuario.
'''

dolar_euro = 0.85
libra_euro = 1.15
dolar_clp = 925
euro_clp = 900
ars_clp = 2.65

print("¿Qué deseas convertir: \n"
      "A: Dólar a euro \n"
      "B: Libra a euro \n"
      "C: Dólar a peso chileno \n"
      "D: Euro a peso chileno\n"
      "E: Peso argentino a peso chileno\n")

respuesta = input("Ingresa tu respuesta > ").upper()

while respuesta not in ["A", "B", "C", "D", "E"]:
    print("Respuesta inválida. Por favor, ingresa una opción válida.")
    respuesta = input("Ingresa tu respuesta > ").upper()
if respuesta == "A":
        dolares = float(input("Ingresa la cantidad de dólares: "))
        conversion = dolares * dolar_euro
        print("{} dólares son {} euros".format(dolares, conversion))
elif respuesta == "B":
    libras = float(input("Ingresa la cantidad de libras: "))
    conversion = libras * libra_euro
    print("{} libras son {} euros".format(libras, conversion))
elif respuesta == "C":
    dolares = float(input("Ingresa la cantidad de dólares: "))
    conversion = dolares * dolar_clp
    print("{} dólares son {} pesos chilenos".format(dolares, conversion))
elif respuesta == "D":
    euros = float(input("Ingresa la cantidad de euros: "))
    conversion = euros * euro_clp
    print("{} euros son {} pesos chilenos".format(euros, conversion))
elif respuesta == "E":
    pesos_argentinos = float(input("Ingresa la cantidad de pesos argentinos: "))
    conversion = pesos_argentinos * ars_clp
    print("{} pesos argentinos son {} pesos chilenos".format(pesos_argentinos, conversion))


    