def resto_divisao(a,b):
    if b == 0:
        print('Nao é possivel dividir por zero')
        return False
    if a == b:
        return 0
    if a < b:
        return a
    else:
        return resto_divisao(a-b,b)

dividendo = int(input('digite o dividendo: '))
divisor = int(input('Digite o divisor: '))
print (f'o resto da divisao inteira é: {resto_divisao(dividendo,divisor)}')
