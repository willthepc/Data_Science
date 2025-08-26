class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def vender(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade -= qtd
            print(f"Venda realizada! Quantidade restante: {self.quantidade}")
        else:
            print("Estoque insuficiente.")

    def repor(self, qtd):
        self.quantidade += qtd
        print(f"Reposição feita. Quantidade atual: {self.quantidade}")

    def __str__(self):
        return f"Código: {self.codigo} | Nome: {self.nome} | Preço: R${self.preco:.2f} | Quantidade: {self.quantidade}"


class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar(self):
        codigo = int(input("Código do produto: "))
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        self.produtos[codigo] = Produto(codigo, nome, preco, quantidade)
        print("Produto cadastrado com sucesso!\n")

    def listar(self):
        if not self.produtos:
            print("Estoque vazio.\n")
        else:
            for produto in self.produtos.values():
                print(produto)

    def buscar(self):
        trecho = input("Digite as três primeiras letras do nome: ").lower()
        achou = False
        for produto in self.produtos.values():
            if produto.nome.lower().startswith(trecho):
                print(produto)
                achou = True
        if not achou:
            print("Produto não encontrado.\n")

    def vender(self):
        codigo = int(input("Código do produto: "))
        if codigo in self.produtos:
            qtd = int(input("Quantidade a vender: "))
            self.produtos[codigo].vender(qtd)
        else:
            print("Produto não encontrado.\n")

    def repor(self):
        codigo = int(input("Código do produto: "))
        if codigo in self.produtos:
            qtd = int(input("Quantidade a repor: "))
            self.produtos[codigo].repor(qtd)
        else:
            print("Produto não encontrado.\n")


# === Execução do Programa ===
estoque = Estoque()

while True:
    print("\nMenu:")
    print("0 - Sair")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Vender produto")
    print("5 - Repor produto")

    op = input("Escolha uma opção: ")

    if op == "0":
        print("Encerrando...")
        break
    elif op == "1":
        estoque.cadastrar()
    elif op == "2":
        estoque.listar()
    elif op == "3":
        estoque.buscar()
    elif op == "4":
        estoque.vender()
    elif op == "5":
        estoque.repor()
    else:
        print("Opção inválida. Tente novamente.")
