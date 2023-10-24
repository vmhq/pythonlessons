# Este es un programa que permitirá crear una lista de compras con los elementos que el usuario ingrese. 

import os

titulo = "✨ Bienvenido a List, tu programa organizador de compras ✨"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

# Se define la variable de la lista, se encuentra vacía para que el usuario ingrese sus elementos. 
lista_compra = []

while True:
    producto = input("¿Qué desea comprar? ([Q] para salir, [B] para borrar lista) > ").capitalize()
    
    # Limpiamos la pantalla aquí
    if os.name == 'posix':  # Para sistemas Unix (macOS, Linux)
        os.system('clear')
    else:  # Para Windows
        os.system('cls')

    if producto == 'Q':
        break
    elif producto == 'B':
        confirmar_borrado = input("¿Está seguro de que quiere borrar toda la lista? [S/N] > ").upper()
        if confirmar_borrado == 'S':
            lista_compra.clear()
            print("¡Lista borrada!")
            continue
        else:
            print("Operación cancelada.")
            continue
    
    if producto in lista_compra:
        print("{} ya está en la lista!" .format(producto))
        continue

    confirmar = input("¿Seguro que quiere añadir \"{}\"? [S/N] > " .format(producto)).upper()
    
    if confirmar == 'S':
        lista_compra.append(producto)
        print("{} añadido!" .format(producto))
    else:
        print("{} no fue añadido  ❌" .format(producto))

print("\n La lista de la compra es: \n")
print(lista_compra)
