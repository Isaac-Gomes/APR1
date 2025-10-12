D = float(input('de qual distancia o robo jogou (em cm): '))
if D <= 800:
    print('sua cesta marcou 1 ponto')
elif D> 800 and D<= 1400:
    print('sua cesta marcou 2 pontos')
else:
    print('sua cesta marcou 3 pontos')