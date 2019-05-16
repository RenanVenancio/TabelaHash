from aluno import *

aluno = Aluno(2321, 'RENAN', 43)

def getEndereco(matricula):
    return matricula % 10

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
print(tabela[0])

sair = 0
while sair == 0:
    matriculaAluno = int(input('MATRICULA DO ALUNO: '))
    nomeAluno = input('DIGITE O NOME DO ALUNO: ')
    idadeALuno = int(input('DIGITE A IDADE DO ALUNO: '))

    aluno = Aluno(matriculaAluno, nomeAluno, idadeALuno)

    tabela[getEndereco(matriculaAluno)][matriculaAluno] = aluno

    sair = int(input('DESEJA ADICIONAR MAIS ALUNOS? 1=NÃO, 0=SIM: '))


print(tabela)





