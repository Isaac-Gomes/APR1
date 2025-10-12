lista1 = [0,1,2,3,4,5,4,5,7,2,3,6,7,8]
repetidos = []
for i in range(0, len(lista1)):
    for j in range(0, len(lista1)):
        if lista1[i]==lista1[j]:
            repetidos.append(i)
i=0
semrep=[]
while i < len(lista1):
    j = 0
    repetido = False
    while j < len(semrep): #os numeros sem repetiçao uma unica vez
        if lista1[i] == semrep[j]:
            repetido = True
        if not repetido:
            semrep.append(lista1[i])
        j+=1
    i+=1
print(f'A primeira lista é:')
for i in range(0, len(lista1)):
    print(f'{lista1[i]}', end=', ')
print()
print(f'A lista de repetidos é:')
for i in range(0,len(repetidos) ):
    print(repetidos[i], end=', ')
print()
print(f'A lista de elementos unicos é:')
for i in range(0, len(semrep)):
    print(f'{semrep[i]}', end=', ')