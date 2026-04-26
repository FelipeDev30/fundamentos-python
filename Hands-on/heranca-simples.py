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
        return f"Veículo: {self.cor}, Placa: {self.placa}, Rodas: {self.numero_rodas}"

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
print(f"moto: {moto}\n")
moto.ligar_e_desligar_motor()

carro = Carro("azul", "XYZ-5678", 4)
print(f"carro: {carro}\n")
carro.ligar_e_desligar_motor()

caminhao = Caminhao("preto", "DEF-9012", 6, True)
print(f"caminhao: {caminhao}\n")
caminhao.ligar_e_desligar_motor()
caminhao.esta_carregado()