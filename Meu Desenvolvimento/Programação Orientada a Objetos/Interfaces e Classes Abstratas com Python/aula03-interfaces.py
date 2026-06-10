""" 
O que são interfaces?

Interfaces são um conceito fundamental na programação orientada a objetos (POO) que define um contrato ou um conjunto de métodos que uma classe deve implementar. 
Elas permitem que diferentes classes possam ser tratadas de maneira uniforme, desde que implementem a mesma interface.
Em Python, as interfaces podem ser implementadas usando classes abstratas do módulo `abc` (Abstract Base Classes). 
Uma classe abstrata é uma classe que não pode ser instanciada e pode conter métodos abstratos, que são métodos declarados, mas sem implementação. 
As classes que herdam de uma classe abstrata devem implementar todos os métodos abstratos definidos na classe base.

Exemplo de interface usando classes abstratas em Python:

```pythonfrom abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def metodo_abstrato(self):
        pass

class ClasseQueImplementa(Interface):
    def metodo_abstrato(self):
        return "Implementação do método abstrato"

```
"""
from abc import ABC, abstractmethod

class Computacional(ABC):
    @abstractmethod
    def processar(self):
        pass
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Notebook(Computacional):
    def __init__(self, marca, modelo, processador, ram):
        self.marca = marca
        self.modelo = modelo
        self.processador = processador
        self.ram = ram
        
    def processar(self):
        if self.ram > 0:
            return "Processando dados no notebook"
        return "Não é possível processar dados - memória insuficiente"

    def ligar(self):
        if self.processador and self.ram > 0:
            return "Ligando o notebook"
        return "Não é possível ligar o notebook"

    def desligar(self):
        while self.processador and self.ram > 0:
            self.ram -= 1
        return "Desligando o notebook"

notebook = Notebook("Dell", "XPS 13", "Intel Core i7", 16)
print(notebook.ligar())
print(notebook.processar())
print(notebook.desligar())