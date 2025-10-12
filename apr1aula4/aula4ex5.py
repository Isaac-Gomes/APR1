lista1= [3,4,5]
lista2= [5,8,7]
soma  = []
i = 0
while i < len(lista1):
    j= lista1[i] + lista2[i]
    soma.append(j)
    i+=1
print('a soma dos elementos das listas é:')
for k in range (0, len(soma)):
    print(soma[k], end=', ')