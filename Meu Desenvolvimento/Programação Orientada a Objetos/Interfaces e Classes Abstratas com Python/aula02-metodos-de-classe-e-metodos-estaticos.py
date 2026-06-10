""" 
O que são métodos de classe e métodos estáticos?

- Métodos de instância: recebem self
- Métodos de classe: recebem cls
- Métodos estáticos: não recebem cls nem self

Os métodos de classe recebem cls como primeiro parâmetro em vez de self. Isso significa que eles operam na classe em vez de em uma instância específica da classe.

Os métodos estáticos não recebem cls nem self como primeiro parâmetro. Isso significa que eles não operam em nenhuma instância da classe.

Exemplo:

class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        print("Au!")

    @classmethod
    def criar_cachorro(cls, nome):
        return cls(nome)

    @staticmethod
    def latir_static():
        print("Au!")

cachorro1 = Cachorro("Rex")
cachorro2 = Cachorro.criar_cachorro("Bob")
cachorro1.latir()
cachorro2.latir()
cachorro1.latir_static()
cachorro2.latir_static()

"""
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano_nascimento, ano_atual, mes, dia, nome):
        idade = ano_atual - ano_nascimento        
        return cls(nome, idade)

    @staticmethod
    def permissao_acesso(self):
        if self.idade < 18:
            print(f"Olá, {self.nome} você tem {self.idade} anos.\nNão podemos permitir o acesso.\nVolte quando tiver 18 anos! ")
        else:
            print(f"Olá, {self.nome} seja bem-vindo! ")

p1 = Pessoa.criar_de_data_nascimento(2020, 2026, 3, 9, "Felipe")

p1.permissao_acesso(p1)