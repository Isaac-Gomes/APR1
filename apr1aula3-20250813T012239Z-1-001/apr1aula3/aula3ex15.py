n = int(input('digite quantos numeros tera a progressao: '))
r = int(input('digite a razao da progressao: '))
a1 = int(input('digite o primeiro termo da progressao: '))
i = 1
soma = 0
print('A progressao aritmetica e:')
while i <= n:
    an = a1 + (i - 1) * r
    print(an, end=', ')
    soma+=an
    i += 1
print(f'a soma é {soma}')