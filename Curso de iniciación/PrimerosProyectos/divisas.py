dolar_euro = 0.95
libra_euro = 1.15

print("¿Qué deseas convertir:\n" 
      "A: Dolar a euro \n" 
      "B: Libra a euro \n")

respuesta = (input("Ingresa tu respuesta: \n"))

if respuesta == "A":
    dolares = (float(input("Ingresa la cantidad de dolares: \n")))
    conversion = dolar_euro * dolares
    print(("¨{} euros son {} dolares" .format(dolares, conversion)))
elif respuesta == "B":
    libras = (float(input("Ingresa la cantidad de libras: \n")))
    conversion = libra_euro * libras
    print("{} libras son {} euros" .format(libras, conversion))
else:
    print("No ha escogido ninguna opción valida.")
