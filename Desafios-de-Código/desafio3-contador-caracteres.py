""" 
Descrição
O desafio consiste em adicionar à função contar_caracteres um dicionário vazio chamado contador para armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string string. Para cada caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries

Entrada
A função espera receber uma única string como entrada. Neste desafio, consideramos como casos de teste apenas strings textuais.

Saída
A função retorna um dicionário onde cada chave é um caractere presente na string de entrada e o valor associado a cada chave é a quantidade de vezes que o caractere ocorre na string.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
collections	{'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1}
numpy	{'n': 1, 'u': 1, 'm': 1, 'p': 1, 'y': 1}
datetime	{'d': 1, 'a': 1, 't': 2, 'e': 2, 'i': 1, 'm': 1}
ATENÇÃO

As entradas e saídas dos desafios de código devem ser idênticas às definidas na descrição do desafio.

print(resultado)


TESTES
Teste #1

Teste #2

Teste #3

Teste #4

Dúvidas ?

"""
def contar_caracteres(string):
    contador = {}
    
    for char in string:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador

entrada = input("Digite uma string: ")
resultado = contar_caracteres(entrada)
print(resultado)

