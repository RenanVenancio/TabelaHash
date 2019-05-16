from aluno import *

aluno = Aluno(2321, 'RENAN', 43)

tabela = [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ]

def getEndereco(matricula):  #Função que calcula o endreço hash
    return matricula % 10

def buscar(**kwargs):  #sem parametros, traz todos, ou passe endereço ou matricula
    if(kwargs.get('endereco')):
        index = kwargs.get('endereco')
        for i in tabela[index]:
            print(tabela[index][i])

    if (kwargs.get('matricula')):
        matricula = kwargs.get('matricula')
        endereco = getEndereco(matricula)
        print(tabela[endereco][matricula])


    for i, endereco in enumerate(tabela):
        print('ENDEREÇO: ' + str(i))
        for j in endereco:
            print(endereco[j])

optMenu = 0
while optMenu == 0:
    print('1-> Cadastrar Aluno \n2-> Buscar aluno')
    optMenu = int(input('DIGITE A OPÇÃO DESEJADA: \n*******************'))

    if(optMenu == 1):
        sairCadastro = 0
        while sairCadastro == 0:
            matriculaAluno = int(input('MATRICULA DO ALUNO: '))
            nomeAluno = input('DIGITE O NOME DO ALUNO: ')
            idadeALuno = int(input('DIGITE A IDADE DO ALUNO: '))

            aluno = Aluno(matriculaAluno, nomeAluno, idadeALuno)

            tabela[getEndereco(matriculaAluno)][matriculaAluno] = aluno

            sairCadastro = int(input('DESEJA ADICIONAR MAIS ALUNOS? 1=NÃO, 0=SIM: '))
            if(sairCadastro == 1):
                optMenu = 0

    if(optMenu == 2):
        print('1-> Buscar \n2-> Remover \n3-> Mostrar tabela Hash')
        sairBusca = int(input('DIGITE A OPÇÃO DESEJADA: \n*******************'))
        optBusca = 0
        while sairBusca == 0:
            if optBusca == 1:
                busca = int(input('INFOME A MATRICULA: '))
                buscar(busca)
                optBusca = 0

            elif optBusca == 2:
                print('Remover')
                optBusca = 0

            elif optBusca == 3:
                buscar()
                optBusca = 0

            if(sairBusca == 1):
                optMenu = 0









