num = int(input('digite um numero'))
x=2
primo = True
if num <= 1:
     primo = False
while  x < num:
    if num % x == 0 and primo == True:
        primo = False
    x+=1
if primo:
     print('é primo') 
if primo == False:
     print('nao é primo')        