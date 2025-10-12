matriz = []
n = int(input('digite a quantidade de linhas: '))
m = int(input('digite a quantidade de colunas: '))
for i in range(n):
    linha = []
    for j in range(m):
        num = int(input(f'digite o elemento {j} da linha {i}: '))
        linha.append(num)
    matriz.append(linha)
print('Matriz:')
for i in range(n):
    for j in range(m):
        print(matriz[i][j], end=' ')
    print()
maior = matriz[0][0]
for i in range(len(matriz)):
     for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
print(f'o maior numero da matriz eh: {maior}')
menor = matriz[0][0]
for i in range(len(matriz)):
     for j in range(len(matriz[i])):
        if matriz[i][j] < menor:
            menor = matriz[i][j]
print(f'o menor numero da matriz eh: {menor}')
