contatos = []
nome = input('digite o nome do contato')
while nome != '':
    pessoa = []
    pessoa.append(nome)
    fone = input('digite o telefone de contato')
    pessoa.append(fone)
    contatos.append(pessoa)
    nome = input('digite outro nome ou enter para parar')
i = 0
while i < len(contatos):
    print(contatos[i][0],contatos[i][1])
    i+=1

    