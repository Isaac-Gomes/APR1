frase = input("Digite uma frase: ")

contador = 0
em_palavra = False

for caractere in frase:
    if caractere != ' ' and not em_palavra:
        contador += 1
        em_palavra = True
    elif caractere == ' ':
        em_palavra = False

print("Número de palavras:", contador)