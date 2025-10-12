notas=[]
soma=0
num = float(input('digite uma nota'))
while num >=0:
    soma+=num
    notas.append(num)
    num=float(input('digite uma nota ou um numero negativo para parar: '))
media=soma/len(notas)
print(f'as notas sao: ')
for i in range (0, len(notas)):
    print(notas[i], end=', ')
print()
print(f'a media é: {media}')