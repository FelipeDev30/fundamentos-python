""" 
# Aula 4 - Convertendo Tipos

# Para que converter tipos?
# Em Python, às vezes precisamos converter tipos de dados para realizar operações específicas. Por exemplo, se temos um número armazenado como string e queremos fazer cálculos com ele, precisamos convertê-lo para um tipo numérico.
# Tipos de conversão comuns:
# - str(): Converte um valor para string.
# - int(): Converte um valor para inteiro.
# - float(): Converte um valor para ponto flutuante (decimal).
# Exemplo prático:
# Convertendo uma string que representa um número decimal para float, depois para inteiro e finalmente de volta para string.

# Convertendo string para float
# Convertendo float para integer
# Convertendo float para string
# Exemplo de código:

"""

preco = "19.99"
preco_float = float(preco)
print(preco_float)

preco = int(preco_float)
print(preco)

preco_str = str(preco_float)
print(preco_str)