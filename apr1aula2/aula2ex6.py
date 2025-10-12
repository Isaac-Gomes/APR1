valor = float(input('quanto o cliente gastou: '))
if valor <=100:
    valor= valor - valor*0.05
    print(f'o valor da compra ficará {valor}')
elif valor >100 and valor < 200:
    valor = valor - valor*0.1
    print(f'o valor da compra ficará {valor}')
else:
    valor = valor - valor*0.2
    print(f'o valor da compra ficará {valor}')