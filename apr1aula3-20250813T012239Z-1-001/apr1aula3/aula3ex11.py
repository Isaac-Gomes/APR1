i=0
soma=0
num=int(input('digite ate onde voce quer somar: '))
while i <= num:
    if i % 2 != 0 and i % 3 == 0:
        print(i,end=", ")
        soma+=i
    i+=1
print(f' a soma é: {soma}')