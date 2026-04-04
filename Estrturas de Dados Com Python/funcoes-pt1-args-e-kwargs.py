""" 
# O que são *args e **kwargs?
*args e **kwargs são formas de passar um número variável de argumentos para uma função em Python.
# *args
*args é usado para passar um número variável de argumentos posicionais para uma função. Ele é representado por um asterisco (*) seguido de um nome de variável, geralmente "args". Os argumentos passados para a função usando *args são armazenados em uma tupla.
# **kwargs
**kwargs é usado para passar um número variável de argumentos nomeados (keyword arguments) para uma função. Ele é representado por dois asteriscos (**) seguidos de um nome de variável, geralmente "kwargs". Os argumentos passados para a função usando **kwargs são armazenados em um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores correspondentes.
# Exemplo de uso de *args e **kwargs

"""

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args) # Junta os argumentos posicionais em um único texto, separando-os por quebras de linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # Formata os argumentos nomeados como "Chave: Valor" e os junta em um único texto, separando-os por quebras de linha
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # Formata a mensagem final, incluindo a data, o texto do poema e os metadados, separados por quebras de linha
    print(mensagem)

exibir_poema("Sabádo, 04 de abril de 2026", "Zen of Python",
    "Beautiful is better than ugly.", "Explicit is better than implicit.", "Simple is better than complex.", "Complex is better than complicated.", "Flat is better than nested.", "Sparse is better than dense.", "Readability counts.", "Special cases aren't special enough to break the rules.", "Although practicality beats purity.", "Errors should never pass silently.", "Unless explicitly silenced.", "In the face of ambiguity, refuse the temptation to guess.", "There should be one-- and preferably only one --obvious way to do it.", "Although that way may not be obvious at first unless you're Dutch.", "Now is better than never.", "Although never is often better than *right* now.", "If the implementation is hard to explain, it's a bad idea.", "If the implementation is easy to explain, it may be a good idea.", "Namespaces are one honking great idea -- let's do more of those.",
    autor="Tim Peters", ano=1999, idioma="Inglês") # Chama a função exibir_poema, passando a data, o texto do poema como argumentos posicionais e os metadados como argumentos nomeados. A função formata e exibe a mensagem final.