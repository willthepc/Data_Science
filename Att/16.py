import os
os.system('cls')

tarefas = {}

def add():
    ide = int(input('Digite o identificador: '))
    status = input('Digite o status: ')
    trf = input('Digite a tarefa: ')
    tarefas[ide] = {'status': status, 'tarefas': trf}
    
def concluido():
    try:
        x = int(input('Digite a IDE da tarefa para ser alterada: '))
        if x in tarefas:
            tarefas[x]['status'] = 'C'
            print(f'ID: {x}\nStatus Alterado com sucesso!')
            print(f'{tarefas[x]}')
    except ValueError:
        print('Digite um valor válido.')
        
def listar():
    for stt, tarefa in tarefas.items():
        print(f'ID: {stt}\nStatus + Tarefa: {tarefa}\n')
    
def listar_concluido():
    print(f'Aqui está as tarefas concluídas!')
    for ide, dados in tarefas.items():
        if dados['status'].upper() == 'C':
            print(f'ID: {ide}\nTarefa: {dados["tarefas"]}\nStatus: {dados["status"]}\n')
        
def listar_pendente():
    print(f'Aqui está as tarefas pendentes!')
    for ide, dados in tarefas.items():
        if dados['status'].upper() == 'P':
            print(f'ID: {ide}\nTarefa: {dados["tarefas"]}\nStatus: {dados["status"]}\n')
    
def remover_tarefa():
    x = int(input('Digite o ID da tarefa a ser removida: '))
    del tarefas[x]
    print(tarefas)
    
while True:
    x = int(input('Digite a opção:\n0 - Sair\n1 - Adicionar tarefa\n2 - Marcar como concluído\n3 - Listar todas\n4 - Listar concluídas\n5 - Listar pendentes\n6 - Remover tarefa\n\n'))
    
    if x == 0:
        print('Programa encerrado!')
        break
    if x == 1:
        add()
        print('\nTarefa adicionada!')
    if x == 2:
        concluido()
        print('Status Alterado.')
    if x == 3:
        listar()
    if x == 4:
        listar_concluido()
    if x == 5:
        listar_pendente()
    if x == 6:
        remover_tarefa()