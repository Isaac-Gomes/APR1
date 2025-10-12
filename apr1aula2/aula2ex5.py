import math
a = float(input('digite o valor de a'))
b = float(input('digite o valor de b'))
c = float(input('digite o valor de c'))
delta = b**2-4*a*c
if delta > 0:
    x1= -b + math.sqrt(delta)/2*a
    x2= -b - math.sqrt(delta)/2*a
    print(f'o valor de x1{x1} é e o de x2 é {x2}')
elif delta==0:
    x= -b/2*a
    print(f' o valor de x é {x}')
else:
    print ('essa equaçao nao possui raizes reais')