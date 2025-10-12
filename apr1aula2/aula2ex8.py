P = int(input( 'Um numero, se P = 0 então Alice gritou "par", ao passo que se P=1 então Bob gritou "par": '))
D1= int(input('Quantos dedos Alice levantou? '))
D2= int(input('Quantos dedos Bob levantou? '))
if P==0 and (D1+D2)%2==0:
    print ('0, Alice ganhou')
elif P==1 and (D1+D2)%2>0:
    print ('0, Alice ganhou')
else:
    print ('1, Bob ganhou')

