""" class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)
foo.x = 5
print(foo.x)
del foo.x
print(foo.x) """

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        nome = input("Digite o nome da pessoa: ")
        ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        ano_atual = int(input("Digite o ano atual: "))
        return ano_atual - self._ano_nascimento
    
    
if __name__ == "__main__":
    pessoa = Pessoa(f"{Pessoa.nome}", Pessoa.idade)
    print(f"Olá, meu nome é {pessoa.nome} e minha idade é {pessoa.idade}.")
    