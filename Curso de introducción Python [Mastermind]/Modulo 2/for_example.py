vocales = ["a", "e", "i", "o", "u"]
frase = "hola, hoy estoy aprendiendo Python en Linux"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        print("He encontrado una '{}'".format(letra))
        vocales_encontradas += 1

print("Vocales encontradas: {}".format(vocales_encontradas))
