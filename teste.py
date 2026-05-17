class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def sacar(self,saldo, valor):
        if saldo <= valor:
            return f"Saque efetuado!"
        else:
            return "Saldo insuficiente!"
    