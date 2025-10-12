def montar_listas(l,n):
    print(f'digite {n} termos da lista: ')
    for i in range(n):
        num = int(input(''))
        l.append(num)
def main():
    lista1=[]
    lista2=[]
    num = int(input('digite quantos numeros tera suas listas'))
    montar_listas(lista1,num)
    montar_listas(lista2,num)

def uniao(l1,l2):
    uniao = []
    for i in range(len(l1)):
        if l1[i] not in uniao:
            uniao.append(l1[i])
    for i in range(len(l2)):
        if l2[i] not in uniao:
            uniao.append(l2[i])
    return uniao

def interseccao(l1,l2):
    inter = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] not in inter:
            inter.append(l1[i])
    return inter

def diferença(l1,l2):
    dif = []
    for i in range(len(l1)):
        if l1[i] not in l2 and l1[i] not in dif:
            dif.append(l1[i])