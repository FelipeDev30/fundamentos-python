"""
Encapsulamento - Aula 03 - Property

A função `property` transforma métodos em um atributo público.
Isso permite controlar leitura, escrita e deleção de valores internos
sem mudar a forma como o objeto é usado.

Exemplo de uso:
    pessoa.nome
    pessoa.idade = 35
    del pessoa.idade
"""

class Pessoa:
    def __init__(self, nome, idade):
        # A convenção do underscore indica que os atributos são de uso interno.
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        self._nome = nome 
        self._idade = idade 

    @property
    def nome(self):
        """Nome público. Não há setter, então este atributo é somente leitura."""
        return self._nome

    @property
    def idade(self):
        """Idade pública. O valor é retornado a partir do atributo interno _idade."""
        return self._idade

    @idade.setter
    def idade(self, valor):
        """Setter para idade com validação simples."""
        if valor < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = valor

    @idade.deleter
    def idade(self):
        """Deleter para idade. Mantemos o objeto consistente definindo idade como 0."""
        self._idade = 0

    def saudacao(self):
        """Método normal que usa as propriedades nome e idade."""
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


if __name__ == "__main__":
    pessoa = Pessoa(f"{Pessoa.nome}", Pessoa.idade) # O construtor agora solicita os valores de nome e idade.
    print(pessoa.saudacao())  # Olá, meu nome é ? e tenho ? anos.

    pessoa.idade = 35
    print(pessoa.saudacao())  # Olá, meu nome é ? e tenho ? anos.

    del pessoa.idade
    print(pessoa.saudacao())  # Olá, meu nome é ? e tenho 0 anos.