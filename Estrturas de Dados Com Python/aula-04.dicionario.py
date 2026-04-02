""" 
# O que são dicionários (dict)?
# Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são definidos usando chaves {} e os pares são separados por dois pontos :.

"""
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

pokemons = dict(pikachu="Elétrico", charmander="Fogo", squirtle="Água")
print(pessoa)  # Output: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
print(pokemons)  # Output: {'pikachu': 'Elétrico', 'charmander': 'Fogo', 'squirtle': 'Água'}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "9876-5432"},
    "joao@gmail.com": {"nome": "João", "telefone": "5678-1234"},
    "ana@gmail.com": {"nome": "Ana", "telefone": "1111-2222"}
}

print(contatos["guilherme@gmail.com"]["telefone"])

""" Iterando sobre um dicionário
- Para iterar sobre um dicionário, podemos usar o método items() para obter as chaves e valores, ou o método keys() para obter apenas as chaves, ou o método values() para obter apenas os valores.
"""
for email, info in contatos.items():
    print(f"Email: {email}, Nome: {info['nome']}, Telefone: {info['telefone']}")