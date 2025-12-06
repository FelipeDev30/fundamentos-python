"""
# Porque usamos tipos?

# Os tipos servem para definir as caracteristicas e comportamentos de um valor (objeto) para o interpretador.
Por exemplo:

Com esse tipo eu sou capaz de realizar perações matemáticas.

Esse tipo para ser armazenado em memória irá consumir 24 bytes.

"""
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    def media(self, n1, n2, n3):
        return (n1 + n2 + n3) / 3
    
# Exemplo de uso dos tipos
idade = int(input("Digite a idade do aluno: "))
aluno = Aluno(nome=input("Digite o nome do aluno: "), idade=idade)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
nome = aluno.nome   
media = aluno.media(n1, n2, n3)

aluno.apresentar()

if media >= 7:
    print(f"O aluno {aluno.nome} foi aprovado com a média {media:.2f}!")
elif (media < 7) and (media >= 5):
    print(f"O aluno {aluno.nome} está de recuperação com a média {media:.2f}!")
elif media < 5:
    print(f"O aluno {aluno.nome} está reprovado com a média {media:.2f}!")
