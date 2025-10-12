matriz = []
nula = []
n = int(input('digite a quantidade de linhas: '))
m = int(input('digite a quantidade de colunas: '))
for i in range(n):
    linha = []
    linhanula=[]
    for j in range(m):
        num = int(input(f'digite o elemento {j} da linha {i}: '))
        linha.append(num)
        linhanula.append(0)
    matriz.append(linha)
    nula.append(linhanula)
lnula=0
for i in range(n):
    if matriz[i]==nula[i]:
        lnula+=1
print(f'{lnula} linhas nulas')
cnula = 0
j = 0
while j < m:
    i = 0
    ehnula = True
    while i < n:
        if matriz[i][j] != 0:
            ehnula = False
        i+=1
    if ehnula:
        cnula +=1
    j+=1
print(f'{cnula} colunas nulas')



