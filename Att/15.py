numeros = {}

def add():
    nome = input('Digite o nome do contato:\n')
    numero = int(input('Digite o número de telefone:\n'))
    numeros[nome] = {'numero': numero}
    
def listar():
    print(numeros)
    
def buscar():
    busc = input('Digite o nome do contato: ')
    print(numeros[busc])
    
def remover():
    nom = input('Digite o nome do contato para apagar: ')
    if nom in numeros:
        del numeros[nom]
        print(numeros)
    else:
        print('Contato não encontrado.')
    
while True:
    x = int(input(f'Escolha uma das opções:\n0 - Sair do menu\n1 - Adicionar contato\n2 - Listar contatos\n3 - Buscar contato\n4 - Excluir contato\n\n'))
    if x == 0:
        print('Operação finalizada.')
        break
    if x == 1:
        add()
    if x == 2:
        listar()
    if x == 3:
        buscar()
    if x == 4:
        remover()

