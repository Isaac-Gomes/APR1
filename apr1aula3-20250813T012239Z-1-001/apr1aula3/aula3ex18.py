numpos = 0
numneg = 0 
soma   = 0
percentpos = 1
percentneg = 1
contador = 0
while True:
    num = int(input('digite um numero, e 0 para parar'))
    soma+= num
    if num!=0: 
        contador+=1
    if num > 0:
        numpos +=1
    elif num < 0:
        numneg+=1
    else:
        media = soma/contador
        percentpos = numpos*100/contador
        percentneg = numneg*100/contador
        print(f'foram {numpos}; ({percentpos})% numeros positivos, {numneg}; ({percentneg})% numeros negativos e media {media}')
        break       