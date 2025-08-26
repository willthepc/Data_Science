print('0 - Sair\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
def soma(x,y):
    print(x + y)
def sub(x,y):
    print(x - y)
def multi(x,y):
    print(x * y)
def div(x,y):
    print(x / y)
while True:
    user = int(input('Digite qual opção você deseja: '))
    if user == 0:
        print('Programa encerrando...')
        break
    elif user == 1:
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        soma(x,y)
    elif user == 2:
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        sub(x,y)
    elif user == 3:
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        multi(x,y)
        break
    elif user == 4:
        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        div(x,y)
    else:
        print('Opção não encontrada.')