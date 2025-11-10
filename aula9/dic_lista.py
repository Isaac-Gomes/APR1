def menu():
    print('Menu de opçoes')
    print('1- incluir aluno')
    print('2- incluir prova de aluno')
    print('3- consultar notas de um aluno')
    print('4- exibir todas as medias')
    print('5- excluir prova')
    print('6- exibir menor nota')
    print('7- exibir maior media')
    print('8- sair do programa')
    num = input()
    return num

def consultar_notas(alunos, ra):
    if ra not in alunos:
        return False    
    provas = alunos[ra][2]
    if not provas:
        return False    
    print('nome do aluno:', alunos[ra][0])
    for i in range(len(provas)):
        disciplina = provas[i][0]
        nota = provas[i][1]
        print(f'{disciplina}: {nota}')
    print(f'media: {media_aluno(alunos, ra)}')
    return True


def media_aluno(alunos, ra):
    if ra not in alunos:
        return False
    provas = alunos[ra][2]
    if not provas:
        return False
    i = 0
    soma = 0.0
    total = len(provas)
    while i < total:
        soma += provas[i][1]  
        i += 1
    return soma / total

def incluir_aluno(alunos, ra):
    if ra in alunos:
        return False
    nome = input('digite o nome do aluno: ').strip()
    email = input('digite o email do aluno: ').strip()
    provas = []
    tem = input('O aluno já tem provas registradas? (s/n): ').strip().lower()
    if tem == 's':
        disc = input('Nome da disciplina (ENTER para terminar): ').strip()
        
        while disc != '':
            nota_str = input('Nota: ').strip()
         
            nota = float(nota_str)
            provas.append([disc, nota])
            disc = input('Nome da disciplina (ENTER para terminar): ').strip()
    alunos[ra] = [nome, email, provas]
    return True

def incluir_prova(alunos, ra):
    if ra not in alunos:
        return False
    provas = alunos[ra][2]
    materia = input('qual o nome da materia ou enter para parar: ').strip()
    while materia != '':
        nota = float(input('qual a nota: '))
        mat = [materia, nota] 
        provas.append(mat)
        materia = input('qual o nome da materia ou enter para parar: ').strip()
    return True

def main():
    alunos = {}
    num = menu()
    while num != '8':
        if num == '1':
            ra = input('digite o ra do aluno: ').strip()
            if incluir_aluno(alunos, ra):
                print('Aluno inserido com sucesso.')
            else:
                print('RA já existe na base.')
        elif num == '2':
            ra=input('qual o prontuario do aluno')
            if not incluir_prova(alunos,ra):
                print('Aluno nao encontrado')
        elif num == '3':
            num=input('qual o ra do aluno')
            if not consultar_notas(alunos,num):
                print('aluno sem provas')
        elif num == '4':
            print('Opção 4 não implementada')
        elif num == '5':
            print('Opção 5 não implementada')
        elif num == '6':
            print('Opção 6 não implementada')
        elif num == '7':
            print('Opção 7 não implementada')
        else:
            print('digite um numero valido')
        num = menu()
    print('encerrando')

main()