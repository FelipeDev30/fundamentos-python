""" 
O que são listas aninhadas (matrizes) em Python?
Listas aninhadas, também conhecidas como matrizes, são listas que contêm outras listas como seus elementos. Isso permite a criação de estruturas de dados mais complexas, como tabelas ou grades, onde cada sublista pode representar uma linha ou coluna.
Elas são úteis para representar dados bidimensionais, como uma planilha ou um tabuleiro de jogo.
Exemplo de criação e acesso a listas aninhadas (matrizes) em Python:

"""
# Autor: Felipe Lamas
# Data: 2026-03-29
# Descrição: Demonstra criação e acesso a listas aninhadas (matrizes) em Python
# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos da matriz
elemento_1 = matriz[0][0]  # 1
elemento_2 = matriz[1][2]  # 6
elemento_3 = matriz[2][1]  # 8
print("Elemento [0][0]:", elemento_1)  # Output: 1
print("Elemento [1][2]:", elemento_2)  # Output: 6
print("Elemento [2][1]:", elemento_3)  # Output: 8

# Exemplo de uma tabela usando listas aninhadas:

tabela = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 30, "São Paulo"],
    ["Bob", 25, "Rio de Janeiro"],
    ["Charlie", 35, "Belo Horizonte"]
]

print(tabela[0][0])  # "Nome"
print(tabela[1][0])  # "Alice"
print(tabela[2][0])  # "Bob"
print(tabela[3][0])  # "Charlie"

""" 
Exemplo de fatiamento em listas aninhadas (matrizes):

O fatiamento em listas aninhadas funciona da mesma forma que em listas comuns, mas você pode aplicar o fatiamento tanto na lista externa quanto nas sublistas internas. Isso permite extrair partes específicas da matriz ou criar novas matrizes a partir de seções da original.

"""

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # Pega os elementos do índice 2 até o final (t, h, o, n)
print(lista[:2]) # Pega os elementos do início até o índice 1 (p, y)
print(lista[1:3]) # Pega os elementos do índice 1 ao 2 (y, t)
print(lista[0:3:2]) # Pega os elementos do índice 0 ao 2, pulando de 2 em 2 (p, t)
print(lista[::]) # Retorna a lista completa
print(lista[::-1]) # Espelha a lista