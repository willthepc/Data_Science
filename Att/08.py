def venda():
    codigo = int(input('Digite agora o codigo: '))
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preco: '))
    quantidade = int(input('Digite a quantidade: '))
    addrem = int(input('Digite pra rem: '))
    quantidade += addrem
    
    codigo = {
        nome: {preco, quantidade}
    }
    print(codigo)
    
venda()