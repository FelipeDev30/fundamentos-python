# O que são list comprehension?
# List comprehension é uma forma concisa de criar listas em Python. 
# Ela permite que você crie uma nova lista aplicando uma expressão a cada item de um iterável, opcionalmente filtrando os itens usando uma condição.

numeros = [1, 30, 21, 2, 9, 65, 34]
pares_comprehension = [numero for numero in numeros if numero % 2 == 0]
print(f"Numeros pares (comprehension): {pares_comprehension}")