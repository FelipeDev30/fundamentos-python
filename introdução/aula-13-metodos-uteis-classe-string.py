""" 
O que são strings em Python? 
Strings em Python são sequências de caracteres usadas para armazenar e manipular texto. Elas são delimitadas por aspas simples (' '), aspas duplas (" "), ou aspas triplas (''' ''' ou """ """) para strings multilinha.
Elas são imutáveis, o que significa que uma vez criadas, seus valores não podem ser alterados diretamente. No entanto, Python oferece uma variedade de métodos úteis para manipular e trabalhar com strings de maneira eficiente.

Aqui estão alguns dos métodos mais comuns e úteis da classe string em Python:

1. .lower(): Converte todos os caracteres da string para minúsculas.
   Exemplo:
   texto = "Hello World"
   print(texto.lower())  # Output: hello world

2. .upper(): Converte todos os caracteres da string para maiúsculas.
   Exemplo:
    texto = "Hello World"
    print(texto.upper())  # Output: HELLO WORLD

3. .strip(): Remove espaços em branco do início e do fim da string.
   Exemplo:
    texto = "   Hello World   "
    print(texto.strip())  # Output: Hello World

4. .replace(old, new): Substitui todas as ocorrências de uma substring por outra.
   Exemplo:
    texto = "Hello World"
    print(texto.replace("World", "Python"))  # Output: Hello Python

5. .split(sep=None): Divide a string em uma lista de substrings com base em um separador.
    Exemplo:
     texto = "Hello World"
     print(texto.split())  # Output: ['Hello', 'World']

6. .join(iterable): Junta uma lista de strings em uma única string, usando a string original como separador.
   Exemplo:
    palavras = ['Hello', 'World']
    print(' '.join(palavras))  # Output: Hello World

7. .find(sub): Retorna o índice da primeira ocorrência de uma substring. Retorna -1 se não for encontrada.
   Exemplo:
    texto = "Hello World"
    print(texto.find("World"))  # Output: 6

8. .count(sub): Conta o número de ocorrências de uma substring na string.
   Exemplo:
    texto = "Hello World World"
    print(texto.count("World"))  # Output: 2

Esses métodos são apenas uma amostra das muitas funcionalidades que a classe string oferece em Python. Eles facilitam a manipulação de texto e tornam o código mais legível e eficiente.

"""
""" 
nome = "Felipe Lamas"

print(nome.lower())
print(nome.upper())
print(nome.strip())
print(nome.replace("Lamas", "Silva"))
print(nome.split())
print('-'.join(nome))
print(nome.find("Lamas"))
print(nome.count("a"))
print(nome.title())
print(nome.capitalize())
print(nome.startswith("F"))
print(nome.endswith("s"))
print(nome.isalpha()) 

"""