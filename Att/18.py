class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def Ligar(self):
        print(f'{self.marca} está ligando...')
        
    def Desligar(self):
        print(f'{self.marca} está desligando...')
        
    def Trancar(self):
        print(f'{self.marca} trancado.')
        
        
carro1 = Carro('Hyundai', 'HB20', 2025)
carro2 = Carro('Fiat', 'MOBI', 2025)

carro1.Ligar()
carro1.Trancar()

carro2.Desligar()