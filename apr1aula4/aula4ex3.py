num = []
n = 1
impares = []
pares = []
while n!= 0:
    n= int(input('digite um numero inteiro e zero para parar'))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
del num[-1]
print('elementos da lista=', end=' ')
for i in range (0, len(num)):
    print(num[i], end= ', ')
soma=0
mult=1
for i in range(0, len(pares)):
    soma+=pares[i]
for i in range (0, len(impares)):
    mult*=impares[i]
print(f' a soma dos pares é {soma}, e a multiplicaçao dos impares é {mult}')