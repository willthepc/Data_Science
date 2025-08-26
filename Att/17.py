import os
os.system('cls')

alunos = {}

def add():
    nome = input('Digite o nome do Aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos[nome] = {'nome':nome,'nota1': nota1, 'nota2': nota2, 'media': media}

def listar():
    for i,o,u,k in alunos.items():
        print(f'\nAluno: {i}\nNota 1: {o['nota1']}\nNota 2: {u['nota2']}\nMédia: {k['media']}\n')
        
def listar_aluno():
    x = input('Digite o nome do aluno: ')
    print(f'Essa é a primeira nota: {alunos[x]['nota1']}')
    print(f'Essa é a segunda nota: {alunos[x]['nota2']}')
    
while True:
    x = int(input('Selecione o serviço:\n0 - Sair\n1 - Adicionar aluno\n2 - Listar alunos\n3 - Listar aluno específico\n'))
    
    if x == 0:
        print('Programa encerrado!')
        break
    if x == 1:
        add()
        print('Aluno + Notas -> Adicionado com sucesso.')
    if x == 2:
        listar()
    if x == 3:
        listar_aluno()