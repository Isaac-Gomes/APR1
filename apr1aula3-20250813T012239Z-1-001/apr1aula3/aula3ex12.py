al=int(input('quantos alunos são'))
i=0
notas = []
while i < al:
    n1=float(input('qual a primeira nota'))
    n2=float(input('qual a segunda nota'))
    n3=float(input('qual a terceira nota'))
    media = (n1*2+n2*4+n3*3)/10
    print(f'a media é {media}')
    notas.append(media)
    if media >= 6:
        print ('aprovado')
    else:
        print ('Reprovado')
    i+=1
j=0
while j < len(notas):
    mediaf= notas[j]/len(notas)
    j+=1
print (f'a media final é {mediaf}')
