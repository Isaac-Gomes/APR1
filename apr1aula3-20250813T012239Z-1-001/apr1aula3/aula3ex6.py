base = int(input('Digite sua base'))
exp  = int(input('Digite seu expoente'))
resultado = 1
while exp > 0:
    resultado *= base
    exp-=1
print(f' = {resultado}')
