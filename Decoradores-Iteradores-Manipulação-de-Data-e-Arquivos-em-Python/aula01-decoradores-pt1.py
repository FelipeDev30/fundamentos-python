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

"""
def meu_decorador(funcao):
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper

@meu_decorador
def saudacao():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}!")

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