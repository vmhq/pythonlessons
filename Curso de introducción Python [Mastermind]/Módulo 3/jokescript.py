import os
import time
from random import randrange


def temporizador():
    horas = randrange(1, 4)
    segundos = horas * 60 * 60
    print ("El temporizador comenzará en {} horas.".format(horas))
    time.sleep(segundos)


def main():
    temporizador()
    desktop_path = "/Users/vicente/Desktop/"  # Cambié a forward slashes
    file_path = os.path.join(desktop_path, "leeme.txt")
    with open(file_path, "w") as file:  # Usar with asegura que el archivo se cierre
        file.write("Hello")  # Esto es opcional, escribiría un archivo vacío.

if __name__ == "__main__":
    main()
