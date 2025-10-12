A=[]
At=[]
n = int(input("digite o numero de linhas e colunas que tera sua matriz quadrada: "))
for i in range(n):
    linha = []
    linhat = []
    for j in range(n):
        num=int(input(f'digite o elemento {j} da linha {i}: '))
        linha.append(num)
        linhat.append(0)
    A.append(linha)
    At.append(linhat)
print(A, At)
for i in range(len(At)):
    for j in range(len(At[i])):
        At[i][j]=A[j][i]
print('Matriz original: ')
print()
for i in range(len(A)):
    for j in range(len(A[i])):
        print (A[i][j], end=' ')
    print()
print('Matriz transposta: ')
print()
for i in range(len(At)):
    for j in range(len(At[i])):
        print (At[i][j], end=' ')
    print()
print()
simetrica = True
for i in range(n):
    for j in range(n):
        if A[i][j]==At[i][j] and simetrica == True:
            simetrica = True
        else:
            simetrica = False
if simetrica:
    print("a Matriz eh simetrica")
else:
    print('A Matriz nao eh simetrica')
