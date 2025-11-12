def soma_lista(numeros, k):
    if k>= len(numeros):
        return 0
    return numeros[k]+soma_lista(numeros, k+1)

cont = 0
num = [1,2,3,4,5,6,7,8,9]
print(f'A soma dos elementos é: {soma_lista(num, cont)}')