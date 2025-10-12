A=[]
At=[[0,0,0],[0,0,0]]
for i in range(3):
    linha=[]
    for j in range(2):
        num = int(input(f'digite o elemento {j} da linha {i}: '))
        linha.append(num)
    A.append(linha)
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
