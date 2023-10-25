import string

texto_usuario = input("¿Cuál es tu texto? > ")

mayusculas = 0 

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        mayusculas += 1

print("Hay {} letras mayusculas" .format(mayusculas))
