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
    
""" 
Métodos úteis para dicionários:
- keys(): Retorna uma visão das chaves do dicionário.
- values(): Retorna uma visão dos valores do dicionário.
- items(): Retorna uma visão dos pares chave-valor do dicionário.
- get(chave, valor_padrao): Retorna o valor associado à chave ou um valor padrão se a chave não existir.
- pop(chave): Remove a chave e retorna seu valor.
- update(outro_dicionário): Atualiza o dicionário com os pares chave-valor de outro dicionário.
- clear(): Remove todos os itens do dicionário.
- copy(): Retorna uma cópia rasa do dicionário.
- fromkeys(chaves, valor): Cria um novo dicionário com as chaves fornecidas e um valor padrão.
- setdefault(chave, valor): Retorna o valor da chave se ela existir, caso contrário, insere a chave com o valor fornecido e retorna esse valor.

"""

# Exemplo didático adicional - uso conjunto de métodos de dict
print('\n=== Exemplo didático de dicionários ===')
# Cria um dicionário de aluno com campos nome, idade e notas
aluno = {
    'nome': 'Beatriz',
    'idade': 21,
    'notas': [8.5, 9.0, 7.8]
}

# Acessa valor por chave (fast lookup O(1))
print('Nome:', aluno['nome'])

# get evita KeyError e aceita valor padrão
print('Email:', aluno.get('email', 'não informado'))

# Atualiza/insere campo
aluno['curso'] = 'ADS'
aluno['idade'] = 22

# Itera sobre itens com for
for chave, valor in aluno.items():
    print(f'{chave} -> {valor}')

# remove chave e retorna valor
idade_removida = aluno.pop('idade', None)
print('Idade removida:', idade_removida)

# setdefault: mantém existente ou adiciona novo
curso = aluno.setdefault('curso', 'Cursos Livres')
print('Curso (setdefault):', curso)

# popitem retira último item inserido (LIFO comportamento 3.7+)
ultimo = aluno.popitem()
print('Item removido por popitem:', ultimo)

# copia e atualiza
aluno_copia = aluno.copy()
aluno_copia.update({'status': 'matriculado'})
print('Cópia atualizada:', aluno_copia)

# clear para esvaziar
a_prestado = aluno.copy()
a_prestado.clear()
print('Dicionário original:', aluno)
print('Cópia esvaziada:', a_prestado)
