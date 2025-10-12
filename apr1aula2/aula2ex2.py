idade = int(input('digite sua idade'))
if idade<18 and idade>16:
    print ('seu voto é facultativo')
elif idade>65:
    print ('esta dispensado de votar')
else:
    print ('seu voto é obrigatorio')