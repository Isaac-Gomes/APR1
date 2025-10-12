num = int(input('Digite quantos numeros primos deseja mostrar: '))
cont=0
i=2
while cont <= num:
    primo = True
    x=2
    while x <i:
        if i % x == 0 and primo == True:
            primo = False
        x+=1
    if primo:
     print(i, end=', ')
     cont+=1 
    i+=1
print('FIM')