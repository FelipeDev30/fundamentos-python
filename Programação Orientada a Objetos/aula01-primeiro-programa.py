""" 
# Programação Orientada a Objetos (POO) - Aula 01: Primeiro Programa

"""
class Bicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor = input("Digite a cor da bicicleta: ")
        self.modelo = modelo = input("Digite o modelo da bicicleta: ")
        self.ano = ano = int(input("Digite o ano da bicicleta: "))
        self.valor = valor = float(input("Digite o valor da bicicleta: "))
        
    def exibir_informacoes(self):
        return f"Bicicleta: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Valor: R$: {self.valor:.2f}"
    
    def buzinar(self):
        return f"{self.modelo} está buzinando: BEEP BEEP!"
    
    def parar(self):
        return f"{self.modelo} parou de se mover."
    
    def correr(self):
        return f"{self.modelo} está correndo pela estrada!"

# Criando um objeto da classe Bicleta
bicicleta1 = Bicleta("", "", 0, 0.0)
# Usando os métodos do objeto bicicleta1
print("\n--- Exemplo com a classe Bicleta ---\n")
print(bicicleta1.exibir_informacoes())  # Saída: Bicicleta: Mountain Bike, Cor: Vermelha, Ano: 2022, Valor: R$1500.00
print(bicicleta1.buzinar())  # Saída: Mountain Bike está buzinando: BEEP BEEP!
print(bicicleta1.correr())  # Saída: Mountain Bike está correndo pela estrada!
print(bicicleta1.parar())  # Saída: Mountain Bike parou de se mover.

