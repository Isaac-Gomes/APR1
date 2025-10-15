def menu():

    print('menu de opcoes')
    print('1 inserir contato')
    print('2. inserir telefone')
    print('3. excluir telefone')
    print('4. excluir contato')
    print('5. consultar contato')
    print('6. imprimir todos os contatos')
    print('7. sair do programa')
    opc = input('escolha uma opçao entre 1 e 6 e 7 para sair do programa')
    return opc 

def inserir_contato(nome,agenda):
    if nome in agenda:
        return False
    else:
        agenda[nome]= []
        continuar = 'sim'
        while continuar == 'sim' or continuar =='Sim':
            num = input('qual o numero do contato: ')
            continuar = input('deseja continuar?')
            agenda[nome].append(num)

def inserir_telefone(nome,agenda):
    if nome not in agenda:
        return False
    else:
        numero = input('digite o numero de contato: ')
        agenda[nome].append(numero)
        return True

def del_telefone(nome,num,agenda):
    if nome not in agenda:
        return False
    elif num not in agenda[nome]:
        return False
    else:
        for nome in agenda:
            if len(agenda[nome])==1:
                if num in agenda[nome]:
                    del agenda[nome]
                    return True
                else:
                    return False
            for i in range(len(agenda[nome])):
                if agenda [nome][i]==num:
                    del agenda[nome][i]
                    return True
            return False
                
        
def del_contato(nome, agenda):
    if nome not in agenda:
        return False
    else:
        del agenda[nome]
        return True
    
def consultar_contato(nome,agenda):
    if nome in agenda:
        print(f'nome: {nome}')
        print('telefones: ')
        for i in range(len(agenda[nome])):
            print(agenda[nome][i])
    else:
        print('O nome nao foi encontrado na agenda')

def imprimir_todos(agenda):
    print('Contatos da agenda:')
    for nome in agenda:
        print(f'Nome: {nome}')
        print('Telefones:')
        for telefone in agenda[nome]:
            print(telefone)


def main():
    Agenda = dict()
    opcao = 1
    while opcao != 7:
        opcao = int(menu())
        if opcao == 1: 
            nome = input('digite o nome do contato: ')
            if inserir_contato(nome,Agenda):
                print('contato inserido com sucesso')
            else:
                print('contato ja na agenda')
        elif opcao == 2:
            nome = input('digite o nome do contato: ')
            if inserir_telefone(nome,Agenda):
                print('numero adicionado com sucesso')
            else:
                print('contato nao encontrado')

        elif opcao == 3:
            nome = input('qual o nome do contato: ')
            numero = input ('Qual o numero do contato: ')
            if del_telefone(nome,numero,Agenda,):
                print('numero excluido com sucesso')
            else:
                print('o numero ou o contato nao existe')
        elif opcao == 4:
            nome = input('digite o nome do contato que voce deseja excluir:')
            if del_contato(nome, Agenda):
                print('contato excluido')
            else:
                print('esse contato nao existe')
        elif opcao == 5:
            nome = input('qual o nome do contato')
            consultar_contato(nome,Agenda)
        elif opcao == 6:
            imprimir_todos(Agenda)
        elif opcao == 7:
            print('encerrando o programa')
        else:
            print('Opcao invalida')
main()
