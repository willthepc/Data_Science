import os
os.system('cls')

print('Seja bem-vindo a Ficha de Alunos.')

alunos = {}

def cadastro():
    try:
        num_alunos = int(input('Digite aqui quantos alunos vão ser cadastrados: '))
        for i in range(num_alunos):
            nome = input('\nDigite o nome do aluno: ')
            idade = int(input('Digite a idade do aluno: '))
            curso = input('1 - Análise e Desenvolvimento de Sistemas(ADS)\n2 - Engenharia da Computação(EC)\n3 - Ciência da Computação(CC)\n\nDigitar curso pela abreviação: ')
            nota = float(input('Digite a nota do aluno: '))
            alunos[nome] = {
                'nome': nome,
                'idade': idade,
                'curso': curso,
                'nota': nota
            }
    except ValueError:
        print('Erro: Você deve digitar um número válido.')
        
    finally:
        print('Entrada de quantidade finalizada.')

def listar():
    x = int(input('\n1 - Listar todos\n2 - Listar nome e nota\n\nEscolha o campo que deseja listar: '))
    if x == 1:
        for i, j in alunos.items():
            print(f'Aluno: {i} | Info: {j}')
    elif x == 2:
        for i,j in alunos.items():
            print(f"Aluno: {j['nome']} | Nota: {j['nota']}")
            print('')
    else:
        print('Opção indísponivel...')
        
def listarAP():
    print('Aqui está a lista dos Aprovados de todos o cursos: ')
    for i, j in alunos.items():
        if j['nota'] >= 7:
            print(f"- {i} -> {j['nota']}")
            
def esp():
    curso_escolhido = input('Digite o curso (ADS, EC, CC): ').upper()
    print(f'Aprovados no curso {curso_escolhido}:')
    encontrou = False
    for i, j in alunos.items():
        if j['curso'] == curso_escolhido and j['nota'] >= 7:
            print(f"- {j['nome']} -> {j['nota']}")
            encontrou = True
    if not encontrou:
        print('Nenhum aprovado nesse curso ou curso inexistente.')
            
        

while True:
    print('Selecione uma das opções a seguir:')
    print('0 - Sair')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Listar aprovados')
    print('4 - Listar aprovados por curso')
    
    xe = int(input('\nDigite aqui: '))
    if xe == 0:
        print('Programa encerrado.')
        break
    elif xe == 1:
        cadastro()
        print('Aluno cadastrado.')
    elif xe == 2:
        listar()
    elif xe == 3:
        listarAP()
    elif xe == 4:
        esp()
    else:
        print('Opção indísponivel.')