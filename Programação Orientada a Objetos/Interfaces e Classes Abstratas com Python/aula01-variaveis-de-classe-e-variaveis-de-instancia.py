""" 
O que são variáveis de classe e variáveis de instância?
Variáveis de classe são compartilhadas por todas as instâncias de uma classe, enquanto variáveis de instância são específicas para cada objeto criado a partir da classe. 
As variáveis de classe são definidas dentro da classe, mas fora de qualquer método, e são acessíveis por todas as instâncias. 
Já as variáveis de instância são definidas dentro do método __init__ e são únicas para cada objeto. 
As variáveis de classe são úteis para armazenar informações que devem ser compartilhadas entre todas as instâncias, como um contador de objetos criados. 
Por outro lado, as variáveis de instância são usadas para armazenar informações específicas de cada objeto, como o nome ou a idade de uma pessoa.

"""
class Pessoa:
    contador_pessoas = 0
    
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
        Pessoa.contador_pessoas += 1

p1 = Pessoa(input("Digite o nome da pessoa 1: "), int(input("Digite a idade da pessoa 1: ")))
p2 = Pessoa(input("Digite o nome da pessoa 2: "), int(input("Digite a idade da pessoa 2: ")))
print(f"Pessoa 1: {p1.name}, Idade: {p1.idade}")
print(f"Pessoa 2: {p2.name}, Idade: {p2.idade}")
print(f"Total de pessoas criadas: {Pessoa.contador_pessoas}")

class Carro:
    def __init__(self, marca, modelo, placa, ano, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.valor = valor
    
    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Ano: {self.ano}, Cor: {self.cor}, Valor: {self.valor}"
    
carro = Carro(input("Digite a marca do carro: "), input("Digite o modelo do carro: "), input("Digite a placa do carro: "), int(input("Digite o ano do carro: ")), input("Digite a cor do carro: "), float(input("Digite o valor do carro: ")))
print(carro.exibir_informacoes())

def calcular_valor_total(carro, quantidade):
    return carro.valor * quantidade
