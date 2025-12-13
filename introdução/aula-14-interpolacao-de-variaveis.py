""" 
# interpolação de Variáveis em Python

Em Python, a interpolação de variáveis permite inserir valores de variáveis dentro de strings de maneira fácil e legível. 
Existem várias maneiras de fazer isso, incluindo o uso do operador `%`, o método `str.format()` e as f-strings (disponíveis a partir do Python 3.6).

"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
# Usando o operador %%
mensagem1 = "Olá, %s! Você tem %d anos." % (nome, idade)
print(mensagem1)

# Usando o método str.format()
mensagem2 = "Olá, {}! Você tem {} anos.".format(nome, idade)
print(mensagem2)

# Usando f-strings
mensagem3 = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem3)

