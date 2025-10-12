def preencher_lista(L,n):
    i=0
    print(f'Digite {n} inteiros para adicionar na lista')
    while i < n:
        num = int(input(''))
        L.append(num)
        i+=1

def printar(L):
    for i in range(len(L)):
        print(L[i], end=', ')

def maior(L):
    maior = L[0]
    for i in range(len(L)):
        if L[i]> maior:
            maior = L[i]
    print(f'o maior numero é {maior}')

def main():
    num = int(input('Quantos elementos tera sua lista'))
    lista = []
    preencher_lista(lista,num)
    printar(lista)
    maior(lista)
main()