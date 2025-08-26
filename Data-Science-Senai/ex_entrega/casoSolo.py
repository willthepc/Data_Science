import os
os.system('cls')
nome = 'William'
idade = 18
nota =  9.5

print(f'O {nome} tem {idade} anos e tirou nota {nota}')

################################################################################################

x = int(input('Quantidade de alunos: '))
nomes = []
presencas = []
notas = []

for i in range(x):
    addNome = input('Digite o nome do aluno: ')
    addPresenca = input('Aluno presente (s/n): ').lower() == 's'
    addNotas = float(input('Nota do aluno: '))
    
    nomes.append(addNome)
    presencas.append(addPresenca)
    notas.append(addNotas)
    
################################################################################################

turma = []

for i in range(x):
    aluno = {
        'nome': nomes[i],
        'presenca': presencas[i],
        'nota': notas[i]
    }
    turma.append(aluno)
    
################################################################################################

presentes = []
ausentes = []

for i in turma:
    if i['presenca'] == True:
        presentes.append(i['nome'])
    elif i['presenca'] == False:
        ausentes.append(i['nome'])
    else:
        print(':)')
        
################################################################################################

while True:
    print('0 - Sair')
    print('1 - Listar presentes')
    print('2 - Listar ausenças')
    print()
    x = int(input('Selecione uma das opções: '))
    
    if x == 0:
        print('Programa encerrado.')
        break
    if x == 1:
        for i in presentes:
            print(f'- {i}')
    if x == 2:
        for i in ausentes:
            print(f'- {i}')