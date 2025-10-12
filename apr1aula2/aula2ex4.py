lado1=(int(input('digite o valor do lado 1')))
lado2=(int(input('digite o valor do lado 2')))
lado3=(int(input('digite o valor do lado 3')))
if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1 + lado2:
    if lado1==lado2 and lado2==lado3:
        print('é um triangulo equilatero')
    elif lado1 != lado2 and lado1 != lado3 and lado3!= lado2:
        print('é um triangulo escaleno')
    else:
        print ('é um triangulo isosceles' )