""" 
Exercício 1: Crie uma classe abstrata chamada "ControleRemoto" com métodos abstratos "ligar" e "desligar". 
Em seguida, crie duas classes concretas, "ControleTv" e "ControleArCondicionado", que herdam de "ControleRemoto" e implementam os métodos abstratos. 
Por fim, crie instâncias de ambas as classes e chame os métodos para ligar e desligar os dispositivos.

"""

from abc import ABC, abstractmethod


class ControleRemeto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    def status(self):
        return 'Ligado' if self._ligado else 'Desligado'

class ControleTv(ControleRemeto):
    def __init__(self):
        self._ligado = False

    def ligar(self):
        self._ligado = True
        
    
    def desligar(self):
        self._ligado = False
        

class ControleArCondicionado(ControleRemeto):
    def __init__(self):
        self._ligado = False

    def ligar(self):
        self._ligado = True
        
    
    def desligar(self):
        self._ligado = False
        

controle = ControleTv()


print("\n" + "---" * 10 + "\n")

control_ar = ControleArCondicionado()

print(f"Status da TV: {controle.status}")
print(f"Status do Ar Condicionado: {control_ar.status}")

controle.ligar()
control_ar.ligar()

print(f"Status da TV: {controle.status}")
print(f"Status do Ar Condicionado: {control_ar.status}")