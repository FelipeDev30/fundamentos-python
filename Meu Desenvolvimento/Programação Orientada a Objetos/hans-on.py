class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_desligar_motor(self):
        if self.motor == 1:
            return "O motor está ligado. Partiu rolê!"
        else:
            return "O motor está desligado. Chegamos em casa!"
    
    
class Carro(Veiculo):
    def __init__(self, cor, placa, numero_rodas, marca):
        super().__init__(cor, placa, numero_rodas)
        self.marca = marca
        self.motor = int(input("Digite 1 para ligar o motor ou 0 para desligar o motor: "))

carro1 = Carro("Vermelha", "ABC-1234", 4, "Toyota")
print(f"Meu carro é um {carro1.marca}, de cor {carro1.cor} e placa {carro1.placa}.")
print(carro1.ligar_desligar_motor())

