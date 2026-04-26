class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.motor = "ligado"
    
    def ligar_e_desligar_motor(self):
        if self.motor == "ligado":
            print("O motor está ligado.")
        else:
            print("O motor está desligado.")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Carro(Veiculo):
    def __init__(self, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)

class Motocicleta(Veiculo):
    def __init__(self, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, está carregado.")

moto = Motocicleta("vermelha", "ABC-1234", 2)
print(f" {moto}\n")


carro = Carro("azul", "XYZ-5678", 4)
print(f" {carro}\n")


caminhao = Caminhao("preto", "DEF-9012", 6, True)
print(f" {caminhao}\n")

caminhao.esta_carregado()