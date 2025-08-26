def cadastro():
    codigo = int(input('Digite agora o codigo: '))
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preco: '))
    quantidade = int(input('Digite a quantidade: '))
    
    codigo = {
        nome: {preco, quantidade}
    }
    
    print(codigo)
    
cadastro()
