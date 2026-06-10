class Passaro:
    def voar(self):
        pass

class Pinguim(Passaro):
    def voar(self):
        print("Pinguins não podem voar")

class Pardal(Passaro):
    def voar(self):
        print("Pardais podem voar")
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruzes não podem voar")

def plano_de_voo(passaro): # A função plano_de_voo aceita um objeto do tipo Passaro ou suas subclasses
    passaro.voar() # O método voar é chamado, e o comportamento específico é determinado em tempo de execução, dependendo da classe do objeto passado.
    
pardal = Pardal()
plano_de_voo(pardal)  # Saída: Pardais podem voar

pinguim = Pinguim()
plano_de_voo(pinguim)  # Saída: Pinguins não podem voar

avestruz = Avestruz()
plano_de_voo(avestruz)  # Saída: Avestruzes não podem voar