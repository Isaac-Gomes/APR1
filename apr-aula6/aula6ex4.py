string = input("Digite uma string: ")

palindromo = True
i = 0
j = len(string) - 1

while i < j:
    if string[i] != string[j]:
        palindromo = False
        i = j
    i += 1
    j -= 1

if palindromo:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")