"""
O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora.

Esse modo é chamado de modo interativo, e pode ser acessado através do terminal ou prompt de comando, digitando o comando "python" ou "python3", dependendo da instalação.

Exemplo:

$ python3
>>>
>>> print("Olá, Mundo!")
Olá, Mundo!
>>>
>>> 2 + 2
4

"""
# Função dir() . Mostra os atributos e métodos disponíveis para um determinado tipo ou objeto.
print(dir(int))
print("-----------------------------------------------------------------------------------------------")
print() 
print(dir(str))
print("-----------------------------------------------------------------------------------------------")
print()
print(dir(float))
print("-----------------------------------------------------------------------------------------------")
print()
print(dir(list))
print("-----------------------------------------------------------------------------------------------")
print()
print(dir(dict))

print("-----------------------------------------------------------------------------------------------")
print()
# Função help() . Mostra a documentação de um determinado tipo ou objeto.
print(help(int))
print(help(str))
print(help(float))
print(help(list))
print(help(dict))

print("-----------------------------------------------------------------------------------------------")
print()
# Podemos criar nossos próprios tipos (classes) e ver seus atributos e métodos.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
pessoa = Pessoa("Ana", 30)
print(dir(pessoa))
print(help(pessoa))
