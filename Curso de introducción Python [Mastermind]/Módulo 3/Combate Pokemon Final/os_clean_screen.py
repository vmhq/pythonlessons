import os


def clean_screen():
    os.system('clear') if os.name == 'posix' else os.system('cls') #Limpia la pantalla 


if __name__ == "__main__":
    clean_screen()
    