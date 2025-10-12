import random 
num = random.randint(1, 100)
acerto = False
while not acerto:
    palpite = int(input('Digite um numero entre 1 e 100: '))
    if palpite < num:
        print('Muito baixo!')
    elif palpite > num:
        print('Muito alto!')
    else:
        acerto = True
        print('Parabens! Voce acertou o numero:', num)
print('Fim do jogo!')