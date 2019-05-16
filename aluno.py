class Aluno:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


    def printar(self):
        print(self.matricula, self.nome, self.idade)


    def __str__(self):
        return 'MAT: ' + str(self.matricula) + ' - NOME: ' + str(self.nome) + ' - IDADE: ' + str(self.idade)