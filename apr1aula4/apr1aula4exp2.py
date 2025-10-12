L = []
cont=1
print('informe 10 valores inteiros')
while cont<=10:
    num = int(input())
    L.append(num)
    cont +=1
i=0
while i<len(L):
    print(f'{L[i]}', end=", ")
    i+=1
print()
maior = L[0]
j = 0
while j<len(L):
    if L[j] > maior:
        maior = L[j]
    j+=1
print (f'maior= {maior}')
menor = L[0]
j = 0
while j<len(L):
    if L[j] < menor:
        menor = L[j]
    j+=1
print (f'menor= {menor}')
soma=0
j=0
while j<len(L):
    soma+=L[j]
    j+=1
print(f'soma= {soma}')
impar = 0
j =0
print('numeros impares', end="=")
while j < len(L):
    if L[j]%2 > 0:
        print(L[j], end=', ')
    j+=1
print()
j=0
print('numeros maiores que 18', end="= ")
while j < len(L):
    if L[j] > 18:
        print(L[j], end=', ')
    j+=1
