import os
os.system('cls')

class Banco:
    def __init__(self, saldo):
        self.saldo = saldo
        
class Att:
    def verSaldo(self):
        saldo = float(input('Digite o saldo atual da conta: '))
        banco = Banco(saldo)
        print(f'Saldo atual: {banco}')
    
    def saque(self):
        x = float(input('Digite quanto vai sacar: '))
        

bancoo = Att()
while True:
    x = int(input('Escolha uma das opções:\n0 - Sair\n1 - Ver saldo\n2 - Sacar\n3 - Depositar\n\n'))
    
    if x == 0:
        print('Programa encerrado!')
        break
    elif x == 1:
        bancoo.verSaldo()
    else:
        print('Opção não disponível.')