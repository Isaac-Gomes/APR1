lista=[]
alt = []
n=0
while n>=0:
    n=int(input('digite um numero inteiro positivo: '))
    lista.append(n)
del lista[-1]
for i in range(len(lista)):
    if lista[i]%2 == 0:
        alt.append(1)
    else:
        alt.append(-1)
print('a lista alterada é')
for j in range (len(alt)):
    print(alt[j], end=', ')
