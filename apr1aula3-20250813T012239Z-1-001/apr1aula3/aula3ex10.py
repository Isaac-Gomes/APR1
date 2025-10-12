i=0
N = 1
M = 1
soma=0
num=int(input('quantos membros da serie voce quer'))
while i < num:
    print (f'{N}/{M} +')
    soma+=N/M
    N+=1
    M+=2
    i+=1
print(f'a soma é:{soma}')