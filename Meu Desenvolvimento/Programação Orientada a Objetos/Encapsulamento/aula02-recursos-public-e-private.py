""" 
Recursos públicos: São aqueles que podem ser acessados de qualquer lugar, 
sem restrições. São definidos sem nenhum prefixo especial.

Recursos privados: São aqueles que só podem ser acessados dentro da classe 
onde são definidos. São definidos com um prefixo duplo de underscore (__).

"""

class Conta:
    def __init__(self, titular, saldo=0):
        self._saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")
            
    def obter_saldo(self):
        return self._saldo

# Criando uma conta
conta1 = Conta("João", 1000)

# Acessando recursos públicos
print(f"Titular: {conta1.titular}")  # Acessando recurso público
conta1.depositar(500)  # Acessando método público
print(f"Saldo após depósito: {conta1.obter_saldo()}")  # Acessando método público

# Acessando recurso privado (não recomendado)
# print(conta1._saldo)  # Acessando recurso privado (não recomendado)

# Acessando recurso privado usando método público
print(f"Saldo atual: {conta1.obter_saldo()}")  # Acessando recurso privado através de método público