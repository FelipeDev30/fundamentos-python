""" 
# Criando tuplas

Tuplas são estruturas de dados imutáveis, ou seja, uma vez criadas, seus elementos não podem ser alterados. 
Elas são definidas usando parênteses () e os elementos são separados por vírgulas.

"""
# Criando uma tupla
minha_tupla = (1, 2, 3, "Python", True)
print("Minha tupla:", minha_tupla)

# Acessando elementos da tupla
print("Primeiro elemento:", minha_tupla[0])  # Acessa o primeiro elemento
print("Último elemento:", minha_tupla[-1])  # Acessa o último elemento

# Matriz de tuplas
matriz_tuplas = (
    ("nome", "idade", "cidade"),
    ("Alice", 30, "São Paulo"),
    ("Bob", 25, "Rio de Janeiro"),
    ("Charlie", 35, "Belo Horizonte")
)

print("Matriz de tuplas:", matriz_tuplas)

# Desempacotamento de tuplas
nome, idade, cidade = matriz_tuplas[1]  # Desempacota a segunda linha da matriz
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)