""" 
# O que é Programação Orientada a Objetos (POO)?

A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de "objetos", que são instâncias de "classes". Uma classe é como um molde ou uma estrutura que define as características (atributos) e comportamentos (métodos) que os objetos criados a partir dela terão. A POO permite que os programadores criem código mais modular, reutilizável e fácil de manter.
# Conceitos-chave da POO:

1. **Classe**: Uma definição ou molde para criar objetos. Ela define os atributos e métodos que os objetos terão.
2. **Objeto**: Uma instância de uma classe. Ele possui os atributos e métodos definidos pela classe.
3. **Encapsulamento**: O processo de esconder os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Isso ajuda a proteger os dados e a garantir que o objeto seja usado corretamente.

"""
# Exemplo de código em Python para ilustrar os conceitos de POO:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."  # Método de instância
# Criando objetos a partir da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
# Usando o método apresentar para cada objeto
print("\n--- Exemplo com a classe Pessoa ---\n")
print(pessoa1.apresentar())  # Saída: Olá, meu nome é Alice e tenho 30 anos.
print(pessoa2.apresentar())  # Saída: Olá, meu nome é Bob e tenho 25 anos.

print("\n--- Exemplo com a classe Cachorro ---\n")

class Cachoroo:
    def __init__(self, nome, cor, acordado):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        if self.acordado:
            return f"{self.nome} está latindo!"
        else:
            return f"{self.nome} está dormindo e não pode latir."
    
    def dormir(self):
        self.acordado = False
        return f"{self.nome} agora está dormindo."
    
    def acordar(self):
        self.acordado = True
        return f"{self.nome} agora está acordado."
    
# Criando um objeto da classe Cachorro
cachorro1 = Cachoroo("Rex", "Marrom", True)
# Usando os métodos do objeto cachorro1
print(cachorro1.latir())  # Saída: Rex está latindo!
print(cachorro1.dormir())  # Saída: Rex agora está dormindo.
print(cachorro1.latir())  # Saída: Rex está dormindo e não pode latir.
print(cachorro1.acordar())  # Saída: Rex agora está acordado.
print(cachorro1.latir())  # Saída: Rex está latindo!

class Bicicleta: 
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("Buzinando: Biiiiiiiiiip!")
    def parar(self):
        print("Parando a bicicleta...")
        print("A bicicleta parou!")
    def correr(self):
        print("A bicicleta está correndo pela estrada!")
        
    def __str__(self):
        return f"{self.__class__.__name__} : `{', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Mountain Bike", 2020, 1500.00)
print("--- Exemplo com a classe Bicicleta ---\n")
print(b1)