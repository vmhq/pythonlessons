titulo = "Bienvenido a la app para escoger teléfono iOS o Android"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("\n" "¿Qué prefieres? \n" 
      "A: Android \n" 
      "B: iOS \n")

preferencia_os = input("Selecciona tu preferencia: \n").upper()

if preferencia_os == "A":
    print("¿Tienes dinero? \n" 
          "A: No \n" 
          "B: Si \n")
    dinero = input("Escoge tu respuesta: \n").upper()
    if dinero == "A":
        print("Debes comprar un Android Chino de 80.000 CLP.")
    elif dinero == "B":
        print("Te improta la cámara del teléfono? \n" 
              "A: Si \n" 
              "B: No me importa \n")
        camara = input("Escoge tu respuesta: \n").upper()
        if camara == "A":
            print("Debes comprar un Google Pixel Supercamara.")
        elif camara == "B":
            print("Debes comprar un Android calidad-precio.")

elif preferencia_os == "B":
    print("¿Tienes dinero? \n"
          "A: No \n"
          "B: Si \n")
    dinero = input("Escoge tu respuesta: \n").upper()
    if dinero == "A":
        print("Debes comprar un iPhone de segunda mano.")
    elif dinero == "B":
        print("Debes comprar un iPhone Ultra Pro Max.")

