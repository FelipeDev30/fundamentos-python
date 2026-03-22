saldo = 0

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Depósito de R${valor} realizado. Saldo atual: R${saldo}")
def sacar(valor):    
    global saldo
    if valor > saldo:
        print("Saldo insuficiente para saque.")    
    else:
        saldo -= valor
        print(f"Saque de R${valor} realizado. Saldo atual: R${saldo}")

def consultar_saldo():    
    print(f"Saldo atual: R${saldo}")
# Exemplo de uso
depositar(100)
sacar(30)
consultar_saldo()

