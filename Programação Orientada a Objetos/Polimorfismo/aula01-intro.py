""" 
O que é Polimorfismo?
Polimorfismo é um conceito fundamental na programação orientada a objetos que permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum. O termo "polimorfismo" vem do grego e significa "muitas formas". 
Em outras palavras, o polimorfismo permite que uma única interface seja usada para representar diferentes tipos de objetos, e o comportamento específico do objeto é determinado em tempo de execução. Isso é alcançado por meio de métodos que podem ser redefinidos em subclasses, permitindo que cada classe tenha sua própria implementação do método, mesmo que compartilhem a mesma assinatura.
O polimorfismo é frequentemente implementado por meio de herança e interfaces, onde uma classe base define um método que pode ser sobrescrito por classes derivadas. Isso permite que o código seja mais flexível e reutilizável, pois você pode usar a mesma interface para trabalhar com diferentes tipos de objetos sem se preocupar com suas implementações específicas.

Exemplo de Polimorfismo em Python:

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau"

def emitir_som(animal):
    print(f"{animal.nome} diz: {animal.fazer_som()}")

cachorro = Cachorro("Rex")
gato = Gato("Whiskers")
emitir_som(cachorro)  # Saída: Rex diz: Au Au
emitir_som(gato)      # Saída: Whiskers diz: Miau

Neste exemplo, a função `emitir_som` pode aceitar qualquer objeto que seja uma instância da classe `Animal` ou de suas subclasses. O método `fazer_som` é implementado de maneira diferente em cada subclass, mas a função `emitir_som` pode chamar esse método sem se preocupar com a implementação específica, demonstrando o polimorfismo em ação.

"""
# Exemplo de polimorfismo com a função len()

curso = "python"
print(len(curso))  # Saída: 6

numeros = [1, 10, 11, 20]
print(len(numeros))  # Saída: 4