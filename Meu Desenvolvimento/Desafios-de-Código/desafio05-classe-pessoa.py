class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))

pessoa = Pessoa(nome, idade)
informacoes = pessoa.exibir_informacoes()
print(informacoes)