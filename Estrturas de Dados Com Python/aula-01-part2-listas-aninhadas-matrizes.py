""" 
O que são listas aninhadas (matrizes) em Python?
Listas aninhadas, também conhecidas como matrizes, são listas que contêm outras listas como seus elementos. Isso permite a criação de estruturas de dados mais complexas, como tabelas ou grades, onde cada sublista pode representar uma linha ou coluna.
Elas são úteis para representar dados bidimensionais, como uma planilha ou um tabuleiro de jogo.
Exemplo de criação e acesso a listas aninhadas (matrizes) em Python:

"""
# Autor: Felipe Lamas
# Data: 2024-06-15
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
