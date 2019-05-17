import os
from aluno import *

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

#As constantes abaixo apenas controlam a cor da mensagens no console
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


tabela = [ {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} ]

def getEndereco(matricula):  #Função que calcula o endreço hash
    return matricula % 11
'''
A função abaixo é utilizada para fazer as buscas
buscar(endereco) Lista os alunos em um determinado endreço
buscar(matricula) Traz o aluno cadastrado conforme a matricula informada no parametro | Retorna True se encontrar, 
False se não.
buscar() Lista toda a tabela hash
'''
def buscar(**kwargs):
    if(kwargs.get('endereco')):
        index = kwargs.get('endereco')
        for i in tabela[index]:
            print(tabela[index][i])


    elif (kwargs.get('matricula')):
        matricula = kwargs.get('matricula')
        endereco = getEndereco(matricula)
        try:    #Tratando erro quando o index não é localizado
            print(tabela[endereco][matricula])
        except KeyError:
            return False
        return True

    else:
        for i, endereco in enumerate(tabela):
            print(BOLD + 'ENDEREÇO: ' + str(i) + RESET)
            for j in endereco:
                print('***' + GREEN + str(endereco[j]) + RESET)

def remover(matriculaAluno):
    try:
        buscar(matricula=matriculaAluno)
        tabela[getEndereco(matriculaAluno)].pop(matriculaAluno)
        print(BLUE + 'Removido!' + RESET)
    except KeyError:
        print(RED + 'Matricula não encontrada!' + RESET)


def cadastrar(matricula, nome, idade):
    aluno = Aluno(matricula, nome, idade)

    if (buscar(matricula=matricula) == False):
        tabela[getEndereco(matricula)][matricula] = aluno
        print(BLUE + 'Aluno cadastrado!' + RESET)

    else:
        print(RED + 'Já existe um aluno com essa matricula cadastrado' + RESET)



'''
Menu de opções
'''
optMenuBusca = 0
menuCentral = 1
while menuCentral == 1:

    print(BLUE + '1-> Cadastrar \n2-> Buscar \n3-> Remover\n4-> Mostrar tabela Hash\n5-> Sair' + RESET)
    try:
        optMenuBusca = int(input('DIGITE A OPÇÃO DESEJADA: \n*******************\n'))
        limpar()
    except:
        print(RED + 'Opção Inválida' + RESET)
        input()
        limpar()

    if optMenuBusca == 1: # Cadastrar
        try:
            matriculaAluno = int(input('MATRICULA DO ALUNO: '))
            nomeAluno = input('DIGITE O NOME DO ALUNO: ')
            idadeALuno = int(input('DIGITE A IDADE DO ALUNO: '))
            cadastrar(matriculaAluno, nomeAluno, idadeALuno)
            input()

        except:
            print(RED + 'Era esperado um número inteiro' + RESET)
            input()
        limpar()

    elif optMenuBusca == 2: # Buscar
        try:
            busca = int(input('INFOME A MATRICULA: '))
            print(RED + 'Não localizado' + RESET) if buscar(matricula=busca) == False else print(
                BLUE + 'Encontrado' + RESET)

        except:
            print(RED + 'Era esperado um número inteiro' + RESET)

        optBusca = 0
        input()
        limpar()

    elif optMenuBusca == 3: # Remover
        try:
            matriculaAluno = int(input('Digite a matricula: '))
            remover(matriculaAluno)
        except:
            print(RED + 'Era espardo um valor inteiro!' + RESET)

        optBusca = 0
        input()
        limpar()

    elif optMenuBusca == 4: # Mostrar tabela
        buscar()
        optBusca = 0
        input()
        limpar()

    elif optMenuBusca == 5:
        menuCentral = 0









