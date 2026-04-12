""" 
# O que é herança?

- Herança é um dos pilares da programação orientada a objetos (POO) que permite criar novas classes com base em classes existentes. 

A classe existente é chamada de "classe base" ou "superclasse", enquanto a nova classe é chamada de "classe derivada" ou "subclasse". 
A subclasse herda os atributos e métodos da superclasse, permitindo reutilizar código e criar hierarquias de classes.

# Vantagens da herança:

1. Reutilização de código: A herança permite que as subclasses reutilizem o código da superclasse, evitando a duplicação de código e facilitando a manutenção.
2. Extensibilidade: As subclasses podem adicionar novos atributos e métodos ou modificar os existentes, permitindo que as classes sejam estendidas e adaptadas às necessidades específicas.
3. Polimorfismo: A herança facilita o polimorfismo, onde objetos de diferentes classes podem ser tratados como objetos da mesma classe base, permitindo a flexibilidade na programação.

# Exemplo de herança em Python:

"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"
class Gato(Animal):
    def falar(self):
        return "Miau!"
    
# Criando objetos das subclasses
cachorro = Cachorro("Rex")
gato = Gato("Mingal")
# Usando os métodos herdados
print(f"{cachorro.nome} diz: {cachorro.falar()}")
print(f"{gato.nome} diz: {gato.falar()}")

# Neste exemplo, a classe `Animal` é a superclasse que define um método `falar()`, que é implementado pelas subclasses `Cachorro` e `Gato`. 
# As subclasses herdam o atributo `nome` da superclasse e implementam o método `falar()` de maneira diferente, demonstrando a reutilização de código e a extensão das funcionalidades.

""" 
# Herança múltipla

- A herança múltipla ocorre quando uma classe pode herdar de mais de uma classe base. 

Isso pode ser útil para combinar funcionalidades de diferentes classes, mas também pode levar a ambiguidades se as classes base tiverem métodos ou atributos com o mesmo nome.

# Exemplo de herança múltipla em Python:

"""
class A:
    def metodo_a(self):
        return "Método da classe A"
class B:
    def metodo_b(self):
        return "Método da classe B"
class C(A, B):
    pass

# Criando um objeto da classe C
c = C()

# Usando os métodos herdados
print(c.metodo_a())  # Saída: Método da classe A
print(c.metodo_b())  # Saída: Método da classe B

# Neste exemplo, a classe `C` herda de ambas as classes `A` e `B`, permitindo que ela acesse os métodos de ambas as classes.
# No entanto, é importante ter cuidado ao usar herança múltipla para evitar conflitos de nomes e garantir que a hierarquia de classes seja clara e compreensível.

