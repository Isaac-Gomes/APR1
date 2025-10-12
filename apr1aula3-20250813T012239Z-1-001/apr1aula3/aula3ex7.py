nota=float(input('digite um numero maior ou igual a 0 para começar'))
n6 = []
n64 = []
n4 = []
notas = []
while nota >=0:
    nota= float(input('digite a nota, ou -1 para parar'))
    if nota >=0:
        notas.append(nota)
    if nota >= 6:
        n6.append(nota)
    elif nota >=4 and nota < 6:
        n64.append(nota)
    elif nota < 4 and nota >=0:
        n4.append(nota)
    else:
        break
print(f'as notas maiores que 6 sao: {n6}  de 4 a 6 sao: {n64} e as menores que 4 sao: {n4}')
i=0
soma=0
while i < len(notas):
    soma+= notas[i]
    i+=1
media= soma/len(notas)
print(f'a média das notas é: {media}')
