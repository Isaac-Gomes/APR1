lista = []
cubo  = []
i=1
while i != 0:
    i = int(input('digite um numero ou zero para parar'))
    lista.append(i)
for j in range(0, len(lista)):
    c = lista[j]**3
    cubo.append(c)
del cubo[-1]
print('a lista ao cubo é')
for k in range(0, len(cubo)):
    print(cubo[k], end=', ')