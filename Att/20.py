import os
os.system('cls')

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    
class Lista:
    def __init__(self):
        self.funcionarios = {}
        
    def adicionarFuncionario(self):
        nome = input('Digite o nome do novo funcionário: ')
        cargo = input('Digite o cargo: ')
        salario = float(input('Digite o salário previsto: '))
        funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios[nome] = funcionario
        
    def listarFuncionario(self):
        print(f'Aqui está os funcionários da empresa: ')
        for i,j in self.funcionarios.items():
            print(f'Nome: {i} | Salário: {j.salario} | Cargo: {j.cargo}')
            
    def listarMaiorSalario(self):
        maior_n = float('-inf')
        fun_maior = None
        for k in self.funcionarios.items():
            if k.salario > maior_n:
                maior_n = k.salario
                fun_maior = k
        print(f'Maior salário: {fun_maior.nome} | Cargo: {fun_maior.cargo} | R$ {fun_maior.salario:.2f} | ')
            
lista = Lista()
            
while True:
    print('0 - Sair')
    print('1 - Adicionar funcionário')
    print('2 - Listar funcionários')
    print('3 - Listar maior salário')
    x = int(input('\n'))
    
    if x == 0:
        print(f'Programa encerrado!')
        break
    elif x == 1:
        lista.adicionarFuncionario()
        print(f'\nFuncionário adicionado!\n')
    elif x == 2:
        lista.listarFuncionario()
    elif x == 3:
        lista.listarMaiorSalario()
    else:
        print('Opção não disponível.')