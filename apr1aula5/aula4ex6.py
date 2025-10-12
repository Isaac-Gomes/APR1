A = []
for i in range(3):
    linha = []
    for j in range(3):
        num = int(input(f'digite o elemento {j} da linha {i}: '))
        linha.append(num)
    A.append(linha)
soma = True
if A[0][0] + A[0][1] + A[0][2] == A[1][0] + A[1][1] + A[1][2] and A[1][0] + A[1][1] + A[1][2] == A[2][0] + A[2][1] + A[2][2]:
    soma = True
else: 
    soma = False
if A[1][0] + A[1][1] + A[1][2] == A[0][0] + A[1][0] + A[2][0]  and A[0][1] + A[1][1] + A[2][1] == A[0][0] + A[1][0] + A[2][0] and A[0][1] + A[1][1] + A[2][1] == A[0][2] + A[1][2] + A[2][2] and soma:
    soma = True
else: 
    soma = False
if A[0][1] + A[1][1] + A[2][1] == A[0][0]+A[1][1]+A[2][2] and A[0][2]+A[1][1]+A[2][0] == A[0][0]+A[1][1]+A[2][2] and soma:
    soma = True
else:
    soma = False
if soma:
    print(f'a matriz eh um quadrado magico')
else:
    print(f'a matriz nao eh um quadrado magico')