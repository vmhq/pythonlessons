def preguntar_producto_usuario():
    return input("Introduce un producto o LISTA para ver los productos disponibles o SALIR:\n> ").strip()

def guardar_en_archivo(lista_compra):
    nombre_archivo = input("Por favor, introduce el nombre del archivo donde deseas guardar (sin extensión): ")
    with open(nombre_archivo + ".txt", "w") as archivo:
        archivo.write("\n".join(lista_compra))
    print("¡Lista guardada exitosamente en {}! 📝".format(nombre_archivo))

def main():
    PRODUCTOS_DISPONIBLES = ["pan", "pollo", "pipas", "carne", "harina"]
    SALIDA = "salir"
    
    lista_compra = []
    input_usuario = preguntar_producto_usuario().lower()

    while input_usuario != SALIDA:
        if input_usuario == "lista":
            print("Productos disponibles:", ", ".join(PRODUCTOS_DISPONIBLES))
        elif input_usuario in PRODUCTOS_DISPONIBLES:
            lista_compra.append(input_usuario.capitalize())
            print("Producto añadido:", input_usuario.capitalize())
        else:
            print("El producto {} no está disponible para añadir a la lista. 😅".format(input_usuario.capitalize()))
        
        input_usuario = preguntar_producto_usuario().lower()

    guardar_en_archivo(lista_compra)

if __name__ == "__main__":
    main()
