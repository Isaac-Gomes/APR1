A = []
for i in range(4):
    linha = []
    for j in range(5):
        num = int(input(f'digite o elemento {j+1} da linha {i+1}: '))
        linha.append(num)
    A.append(linha)
menor = A[0][0]
for i in range(len(A)):
     for j in range(len(A[i])):
        if A[i][j] < menor:
            menor = A[i][j]
i=0
achou = False
linha = 0
coluna = 0
while i < 4:
    j=0
    while j < 5 and not achou:
        if A[i][j] == menor:
            linha = i
            coluna = j
            achou = True
        j += 1
    i+=1
maior = A[linha][0]
for j in range(5):
    if A[linha][j]>maior:
        maior = A[linha][j]
print(f'O min max eh o elemento: {maior} na linha {linha+1} e coluna {coluna}')
