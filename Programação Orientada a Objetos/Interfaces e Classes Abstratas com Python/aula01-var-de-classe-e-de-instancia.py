class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, (n°: {self.numero}) - {self.escola}"

def mostrar_dados(*objs):
    for obj in objs:
        print(obj)
    

# Atributo de instância não altera o atributo da classe, ou seja, outra instância não é afetada.
estudante1 = Estudante("Felipe", 1) 
estudante2 = Estudante("Maria", 2)

estudante1.nome = "João"
estudante2.nome = "Ana"

mostrar_dados(estudante1, estudante2)

print("_" * 50 + "\n")

# Atributo de classe é compartilhado entre instâncias
estudante1.escola = "Fundação Bradesco" # Se alterar em uma instância, altera em todas

mostrar_dados(estudante1, estudante2)

