# Exercício 1 —  Aquecimento

# nome = 'William'
# idade = 17
# nota = 10
# print(f'Olá! Meu nome é {nome}, tenho {idade} anos e tirei nota {nota} na última atividade.')

##########################################################################################################

# Exercício 2 – Cadastro sequencial

# qtd_alunos = int(input('Quantos alunos serão cadastrados? '))

# nomes = []
# presencas = []
# notas = []

# for i in range(qtd_alunos):
#     nome_aluno = input(f'Nome do aluno {i+1}: ')
#     presente = input(f'O aluno {nome_aluno} está presente? (s/n): ').lower() == 's'
#     nota_aluno = float(input(f'Nota do aluno {nome_aluno}: '))

#     nomes.append(nome_aluno)
#     presencas.append(presente)
#     notas.append(nota_aluno)

##########################################################################################################

# Exercício 3 —  Conversão em dicionários
# turma = []

# for i in range(qtd_alunos):
#     aluno = {
#         'nome': nomes[i],
#         'presente': presencas[i],
#         'nota': notas[i]
#     }
#     turma.append(aluno)
    
#     # Exercício 4 – Relatório de presença
# presentes = []
# ausentes = []

# for aluno in turma:
#     if aluno['presente']:
#         presentes.append(aluno['nome'])
#     else:
#         ausentes.append(aluno['nome'])

# print(f'\nTotal de presentes: {len(presentes)}')
# print(f'Total de ausentes: {len(ausentes)}')

##########################################################################################################

# Exercício 5 – Menu while
# opcao = -1

# while opcao != 0:
#     print('\n Menu')
#     print('1 - Listar presentes')
#     print('2 - Listar ausentes')
#     print('3 - Mostrar estatísticas de notas')
#     print('4 - Mostrar alunos destaque (nota ≥ 9)')
#     print('0 - Sair')
    
#     opcao = int(input('Escolha uma opção: '))

#     if opcao == 1:
#         print('\nAlunos presentes:')
#         for aluno in turma:
#             if aluno['presente']:
#                 print(f"- {aluno['nome']}")
    
#     elif opcao == 2:
#         print('\nAlunos ausentes:')
#         for aluno in turma:
#             if not aluno['presente']:
#                 print(f"- {aluno['nome']}")

#     elif opcao == 3:
#         soma = 0
#         maior = -1
#         menor = 11
#         nome_maior = ''
#         nome_menor = ''

#         for aluno in turma:
#             nota = aluno['nota']
#             soma += nota
#             if nota > maior:
#                 maior = nota
#                 nome_maior = aluno['nome']
#             if nota < menor:
#                 menor = nota
#                 nome_menor = aluno['nome']

#         media = soma / len(turma)
#         print(f'\nMédia das notas: {media:.2f}')
#         print(f'Maior nota: {maior} (Aluno: {nome_maior})')
#         print(f'Menor nota: {menor} (Aluno: {nome_menor})')

#     elif opcao == 4:
#         print('\n Alunos destaque (nota ≥ 9):')
#         for aluno in turma:
#             if aluno['nota'] >= 9:
#                 print(f'- {aluno['nome']} (Nota: {aluno['nota']})')

#     elif opcao == 0:
#         print('Saindo...')

#     else:
#         print('Opção inválida!')

# ##########################################################################################################

# # Exercício 6 – Estatísticas rápidas
# print('\n Estatísticas de notas:')

# soma_notas = 0
# maior_nota = -1
# menor_nota = 11
# aluno_maior_nota = ''
# aluno_menor_nota = ''

# for aluno in turma:
#     nota = aluno['nota']
#     nome = aluno['nome']
#     soma_notas += nota

#     if nota > maior_nota:
#         maior_nota = nota
#         aluno_maior_nota = nome

#     if nota < menor_nota:
#         menor_nota = nota
#         aluno_menor_nota = nome

# media = soma_notas / len(turma)

# print(f'Média das notas: {media:.2f}')
# print(f'Maior nota: {maior_nota} (Aluno: {aluno_maior_nota})')
# print(f'Menor nota: {menor_nota} (Aluno: {aluno_menor_nota})')