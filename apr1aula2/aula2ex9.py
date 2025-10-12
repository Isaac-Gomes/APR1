C =int(input('Digite o numero de competidores '))
P =int(input('Digite a quantidade de papel comprado pela diretora '))
F =int(input('Digite a quantidade de papel que cada participante ira receber '))

if C*F <= P:
    print('S')
else:
    print('N')