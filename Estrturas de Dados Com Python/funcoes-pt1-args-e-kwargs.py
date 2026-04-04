""" 
# O que são *args e **kwargs?
*args e **kwargs são formas de passar um número variável de argumentos para uma função em Python.
# *args
*args é usado para passar um número variável de argumentos posicionais para uma função. Ele é representado por um asterisco (*) seguido de um nome de variável, geralmente "args". Os argumentos passados para a função usando *args são armazenados em uma tupla.
# **kwargs
**kwargs é usado para passar um número variável de argumentos nomeados (keyword arguments) para uma função. Ele é representado por dois asteriscos (**) seguidos de um nome de variável, geralmente "kwargs". Os argumentos passados para a função usando **kwargs são armazenados em um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores correspondentes.
# Exemplo de uso de *args e **kwargs

"""
""" def exemplo_args(*args):
    for arg in args:
        print(arg)

def exemplo_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Usando *args
print("Exemplo de *args:")
exemplo_args(1, 2, 3, "quatro", "cinco")
# Usando **kwargs  
print("\nExemplo de **kwargs:")
exemplo_kwargs(nome="Alice", idade=30, cidade="São Paulo")
# Combinando *args e **kwargs
print("\nExemplo combinando *args e **kwargs:")
def exemplo_combinado(*args, **kwargs):
    print("Argumentos posicionais (*args):")
    for arg in args:
        print(arg)
    print("\nArgumentos nomeados (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
exemplo_combinado(1, 2, 3, nome="Alice", idade=30, cidade="São Paulo") """

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python",
    "Beautiful is better than ugly.", "Explicit is better than implicit.", "Simple is better than complex.", "Complex is better than complicated.", "Flat is better than nested.", "Sparse is better than dense.", "Readability counts.", "Special cases aren't special enough to break the rules.", "Although practicality beats purity.", "Errors should never pass silently.", "Unless explicitly silenced.", "In the face of ambiguity, refuse the temptation to guess.", "There should be one-- and preferably only one --obvious way to do it.", "Although that way may not be obvious at first unless you're Dutch.", "Now is better than never.", "Although never is often better than *right* now.", "If the implementation is hard to explain, it's a bad idea.", "If the implementation is easy to explain, it may be a good idea.", "Namespaces are one honking great idea -- let's do more of those.",
    autor="Tim Peters", ano=1999, idioma="Inglês")

