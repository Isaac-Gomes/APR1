m = 2
n = 3
q = 2
A=[]
B=[]
C=[]
for i in range(m):
    linha=[]
    for j in range(n):
        num = int(input(f'Digite o elemento {j} da linha {i} da matriz A: '))
        linha.append(num)
    A.append(linha)
for i in range(n):
    linha=[]
    for j in range(q):
        num = int(input(f'Digite o elemento {j} da linha {i} da matriz B: '))
        linha.append(num)
    B.append(linha)
for i in range(m):
    linha = []
    for j in range(q):
        soma = 0
        for k in range(n):
            soma += A[i][k]*B[k][j]
        linha.append(soma)
    C.append(soma)
        
