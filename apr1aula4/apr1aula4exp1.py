L = ['laranja', 'melancia', 'maça', 'melao', 'uva']
fruta = input('qual fruta voce deseja procurar: ')
i=0
achou = False
while i < len(L) and not achou:
    if L[i]==fruta:
        print(f'{fruta} esta na lista')
        achou = True
    i+=1
if achou:
    print (f'{fruta} esta na lista')
else:
    print(f'{fruta} nao esta na lista')