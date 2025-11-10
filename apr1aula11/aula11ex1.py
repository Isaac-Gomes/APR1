def obter_potencia(x,n):
    try:
        if n == 1:
            return x
        if x != 0 and n == 0:
            return 1
        else:
            return x * obter_potencia(x, n-1)
    except:
        print ('nao é possivel elevar 0 a 0')
        return False

X = int(input('Digite a base: '))
N = int(input('Digite  o expoente: '))
if obter_potencia:
    print (f'O resultado é: {obter_potencia(X,N)}')


