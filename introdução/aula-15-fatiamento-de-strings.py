""" 
# O que é fatiamento de strings?
Fatiamento de strings é uma técnica utilizada para extrair partes específicas de uma string em Python

# Como funciona o fatiamento de strings??
Em Python, as strings são sequências imutáveis de caracteres, e cada caractere possui um índice associado. O fatiamento permite que você extraia uma substring especificando um intervalo de índices.
A sintaxe básica para fatiamento de strings é:
string[início:fim:passo]
onde:
- início: o índice inicial (inclusivo) da substring.
- fim: o índice final (exclusivo) da substring.
- passo: o incremento entre os índices (opcional).

# Exemplos de fatiamento de strings
```python
texto = "Olá, mundo!"

# Extrair os primeiros 5 caracteres
parte1 = texto[0:5]  # Resultado: 'Olá, '
print(parte1)

# Extrair do índice 7 até o final
parte2 = texto[7:]    # Resultado: 'mundo!'
print(parte2)

# Extrair do início até o índice 4
parte3 = texto[:4]    # Resultado: 'Olá,'
print(parte3)

# Extrair caracteres com passo 2
parte4 = texto[::2]   # Resultado: 'Oámno'
print(parte4)

# Fatiamento com índices negativos
parte5 = texto[-6:-1] # Resultado: 'mundo'
print(parte5)

# Conclusão
O fatiamento de strings é uma ferramenta poderosa em Python que permite manipular e extrair partes específicas de strings de maneira eficiente e flexível.

"""