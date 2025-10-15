'''Um anagrama é uma palavra que é feita a partir da transposição das
letras de outra palavra ou frase. Por exemplo, “Iracema” é um
anagrama para “America”. Escreva um programa que decida se uma
string é um anagrama de outra string, ignorando os espaços em branco.
O programa deve considerar maiúsculas e minúsculas como sendo
caracteres iguais, ou seja, “a” = “A”.'''
str1 = input("Entre com a primeira string:")
str2 = input("Entre com a segunda string:")
str1 = str1.lower().replace(' ','')
str2 = str2.lower().replace(' ','')
if len(str1) == len(str2):
    anagrama = True
    i = 0
    while i < len(str1) and anagrama:
        cont_str1 = 0 #conta qtas vezes a letra aparece em str1
        cont_str2 = 0 #conta qtas vezes a letra aparece em str2
        #conta o total de vezes que a letra da posição i de str1
        #se repete na mesma string
        for j in range(len(str1)): 
            if str1[i] == str1[j]:
                cont_str1+=1
        #conta o total de vezes que a letra da posição i de str1
        #ocorre em str2
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cont_str2+=1
        if cont_str1 != cont_str2:
            anagrama = False
        i+=1
    if anagrama:
        print("É anagrama!")
    else:
        print("Não é anagrama!")
else:
    print("Não é anagrama!")
