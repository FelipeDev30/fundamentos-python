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
print(pessoa1.apresentar())  # Saída: Olá, meu nome é Alice e tenho 30 anos.
print(pessoa2.apresentar())  # Saída: Olá, meu nome é Bob e tenho 25 anos.