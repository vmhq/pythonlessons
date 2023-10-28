texto_usuario = input("¿Cuál es tu texto? > ")

espacios = 0
puntos = 0
comas = 0

for caracter in texto_usuario:
    if caracter == ' ':
        espacios += 1
    elif caracter == '.':
        puntos += 1
    elif caracter == ',':
        comas += 1

print("Hay {} espacios" .format(espacios))
print("Hay {} puntos" .format(puntos))
print("Hay {} comas" .format(comas))
