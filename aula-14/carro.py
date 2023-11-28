class Carro:
    def __init__(self, marca: str, modelo: str, cor: str, combustivel: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = False
        self.velocidade = 0
    
    def ligar(self):
        if self.ligado:
            print(f'{self.modelo} já está ligado')
        else:
            self.ligado = True
            print(f'{self.modelo} ligado')

    def desligar(self):
        if not(self.ligado):
            print(f'{self.modelo} já está desligado')
        else:
            self.ligado = False
            print(f'{self.modelo} desligado')

    def acelerar(self):
        if not(self.ligado):
            return print(f'Não é possivel acelerar com o {self.modelo} desligado')
        
        self.velocidade += 10
        print(f'{self.modelo} acelerando, velocidade: {self.velocidade}km/h')

    def frear(self):
        if not(self.ligado):
            return print(f'Não é possível frear com o {self.modelo} desligado')
    
        self.velocidade -= 10
        print(f'{self.modelo} freando, velocidade: {self.velocidade}km/h')
