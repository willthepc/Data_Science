class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplina = {}
        
    def adicionarAluno(self):
        nome = input('Digite o nome do aluno: ')
        matricula = int(input('Digite o número da matrícula: '))
        aluno = Aluno(nome, matricula)
                
    def adicionar_disciplina(self, nome_disciplina, nota):
        self.disciplinas[nome_disciplina] = nota
        
while True:
    print('Selecione uma das opções: ')
    print('')
    print('')
    print('')