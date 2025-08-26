estoque = {}

def criacao():
    codigo = int(input('Digite o identificador: '))
    nome = input('Digite o nome do produto: ')
    preco_produto = int(input('Digite o preço do produto: '))
    qtd_produto = int(input('Digite a quantidade do produto: '))
    estoque[codigo] = {
            'nome': nome,
            'preco': preco_produto,
            'quantidade': qtd_produto
        }
    print(estoque.keys())
    
def listar():
    for codigo, dados in estoque.items():
        print(f'{codigo} -> {dados}')
        
def buscar():
    y = input('Digite as três primeiras letras: ')
    for codigo, dados in estoque.items():
        if dados['nome'].lower().startswith(y.lower()):
            print(f'{codigo} -> {dados}')
            
def vender():
    venda = int(input('Digite o produto: '))
    if venda in estoque:
        qnt_venda = int(input(f'Digite quantas vendas ocorreram: '))
        if estoque[venda]['quantidade'] >= qnt_venda:
            estoque[venda]['quantidade'] -= qnt_venda
            print(f'Venda realizada! {estoque[venda]['quantidade']}')
        else:
            print('Produtos indisponíveis.')
    else:
        print(f'Erro: Produto não encontrado.')
        
def repor():
    reposicao = int(input('Digite o produto: '))
    if reposicao in estoque:
        qnt_venda = int(input(f'Digite quantos produtos chegaram: '))
        if estoque[reposicao]['quantidade'] >= qnt_venda:
            estoque[reposicao]['quantidade'] += qnt_venda
            print(f'Reposição realizada! {estoque[reposicao]['quantidade']}')
        else:
            print('Produtos indisponíveis.')
    else:
        print(f'Erro: Produto não encontrado.')
    

while True:
    x = int(input('Escolha uma das opções:\n0 - Sair\n1 - Cadastrar produto\n2 - Listar produtos\n3 - Buscar produto\n4 - Vender produto\n5 - Repor estoque\n\n'))
    if x == 0:
        print('Saindo da operação...')
        break
    if x == 1:
        criacao()
    if x == 2:
        listar()
    if x == 3:
        buscar()
    if x == 4:
        vender()
    if x == 5:
        repor()