class Conta:
    def __init__(self, titular,nro_agencia, nro_conta, saldo=0):
        self.titular = titular
        self.nro_agencia = nro_agencia
        self.nro_conta = nro_conta
        self._saldo = saldo
    
    def depositar(self, valor):
        self._saldo += valor
        return self._exibir_saldo()

    def _exibir_saldo(self):
        return f"Saldo atual: {self._saldo}"
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return self._exibir_saldo()
        else:
            return f"{self._exibir_saldo()}. Saldo insuficiente ou valor inválido!"
    
# Criando uma conta
conta1 = Conta("João", "1234", "56789-0", 1000)
# Acessando recursos públicos
print(f"Titular: {conta1.titular}")  # Acessando recurso público
print(f"Número da Agência: {conta1.nro_agencia}")  # Acessando recurso público
print(f"Número da Conta: {conta1.nro_conta}")  # Acessando recurso público
print(conta1.depositar(500))  # Acessando método público
print(conta1.sacar(200))  # Acessando método público