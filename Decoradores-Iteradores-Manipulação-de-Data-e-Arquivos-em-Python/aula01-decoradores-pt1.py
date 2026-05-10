""" 
O que são decoradores?

Decoradores são funções que "envolvem" ou "decoram" outras funções, alterando 
o comportamento delas sem modificar o código fonte da função decorada.

Em essência, um decorador é uma função que recebe outra função como argumento, 
adiciona alguma funcionalidade e retorna outra função, tudo isso sem alterar 
o código da função original.

# Sintaxe básica

@decorador
def minha_funcao():
    pass

# Equivalente a:

def minha_funcao():
    pass

minha_funcao = decorador(minha_funcao)

# Exemplo simples: um decorador que imprime uma mensagem antes e depois da função

def meu_decorador(funcao):
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper

@meu_decorador
def saudacao():
    print("Olá!")

saudacao()

# Outro exemplo:

def repetir(n):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def falar(texto):
    print(texto)

falar("Oi!")

"""
""" 
Inner Functions

São funções que são definidas dentro de outra função.

"""

def mensagem(nome):
    print('Executando mensagem!')
    return print(f"Olá, {nome}")

def mensagem_longa(nome):
    print('Executando mensagem longa!')
    return print(f"Olá {nome}, tudo bem com você hoje?")

def executar(funcao):
    print(f"Executando a função executar!\n")
    nome = input("Informe seu nome: ")
    funcao(nome)

executar(mensagem)
print("-" * 30)
executar(mensagem_longa)


# Note que ambas as funções executam a mesma linha de código 'Executando mensagem!'
# E ambas retornam um valor. O objetivo é criar um decorador que execute
# 'Executando mensagem' para ambas as funções sem repetir o código.
