frase = input('digite uma frase: ')
conta = 0
conte = 0
conti = 0
conto = 0
contu = 0
esp = 0
frase = frase.lower()
for i in range(len(frase)):
    if frase[i]== 'a':
        conta+=1
    elif frase[i]== 'e':
        conte+=1
    elif frase[i]== 'i':
        conti+=1
    elif frase[i]== 'o':
        conto+=1
    elif frase[i]== 'u':
        contu+=1
    elif frase[i]== ' ':
        esp+=1

print("Quantidade de 'a':", conta)
print("Quantidade de 'e':", conte)
print("Quantidade de 'i':", conti)
print("Quantidade de 'o':", conto)
print("Quantidade de 'u':", contu)
print("Quantidade de espaços: ", esp)