""" 
# O que são conjuntos (sets)?

# Conjuntos são estruturas de dados que armazenam elementos únicos e não ordenados. Eles são definidos usando chaves {} ou a função set().

"""
numeros = set([1, 2, 3, 4])
print(numeros)  # Output: {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # Output: {'a', 'b', 'c', 'x', 'i'}

carros = set(["palio", "gol", "celta", "palio"])
print(carros)  # Output: {'palio', 'gol', 'celta'}

linguagens = {"Python", "Java", "C++", "Python"}
print(linguagens)  # Output: {'Python', 'Java', 'C++

linguagens = list(linguagens)  # Convertendo o conjunto para uma lista
linguagens.sort() # Ordenando a lista (opcional, pois conjuntos não têm ordem definida) d
print(linguagens[0])  # Output: 'Java' (a ordem pode variar, pois conjuntos não são ordenados)

# Iterando sobre um conjunto
for carro in carros:
    print(carro)  # Output: 'gol', 'palio', 'celta' (a ordem pode variar)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")