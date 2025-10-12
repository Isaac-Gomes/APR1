lista=[]
invert = []
n = 1
while n != 0:
    n = int(input('digite um numero inteiro e zero para parar'))
    lista.append(n)
del lista[-1]
i=1
while i <= len(lista):
    invert.append(lista[-i])
    i+=1
print('a lista invertida é: ')
for i in range(0, len(invert)):
    print(invert[i], end=', ')