""" 
Exercício 1: Crie uma classe abstrata chamada "ControleRemoto" com métodos abstratos "ligar" e "desligar". 
Em seguida, crie duas classes concretas, "ControleTv" e "ControleArCondicionado", que herdam de "ControleRemoto" e implementam os métodos abstratos. 
Por fim, crie instâncias de ambas as classes e chame os métodos para ligar e desligar os dispositivos.

"""

from abc import ABC, abstractmethod, abstractproperty


class ControleRemeto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def status(self):
        pass

class ControleTv(ControleRemeto):
    @property
    def status(self):
        return 'Ligado' if self._ligado else 'Desligado'
    
    def __init__(self):
        self._ligado = False

    def ligar(self):
        self._ligado = True
        
    
    def desligar(self):
        self._ligado = False
        

class ControleArCondicionado(ControleRemeto):
    @property
    def status(self):
        return 'Ligado' if self._ligado else 'Desligado'

    def __init__(self):
        self._ligado = False

    def ligar(self):
        self._ligado = True
        
    
    def desligar(self):
        self._ligado = False
        

controle = ControleTv()

control_ar = ControleArCondicionado()

print(f"Status da TV: {controle.status}")
print(f"Status do Ar Condicionado: {control_ar.status}")

print("\n" + "---" * 10 + "\n")

controle.ligar()
control_ar.ligar()

print(f"Status da TV: {controle.status}")
print(f"Status do Ar Condicionado: {control_ar.status}")