""" 
### ✅ O que é uma lista em Python?

Uma **lista** em Python é uma coleção **ordenada** e **mutável** que permite armazenar múltiplos itens em uma única variável.  
Características principais:

*   Pode conter elementos de diferentes tipos (números, strings, outras listas, etc.).
*   É **mutável**, ou seja, seus valores podem ser alterados após a criação.
*   Mantém a ordem dos elementos.

***

### ✅ Como criar listas em Python?

Existem várias formas:

*   Usando colchetes:
    ```python
    minha_lista = [10, 20, 30]
    ```
*   Usando o construtor `list()`:
    ```python
    outra_lista = list(range(5))  # [0, 1, 2, 3, 4]
    ```

***

### ✅ Como acessar elementos?

*   Pelo índice (começa em 0):
    ```python
    primeiro = minha_lista[0]    # 10
    segundo = minha_lista[1]     # 20
    ultimo = minha_lista[-1]     # 50
    ```

***

### ✅ Exemplo completo:

```python
# Autor: Felipe Lamas
# Data: 2024-06-15
# Descrição: Demonstra criação e acesso a listas em Python

# Criação da lista
minha_lista = [10, 20, 30, 40, 50]

# Acesso aos elementos
primeiro_elemento = minha_lista[0]   # 10
segundo_elemento = minha_lista[1]    # 20
ultimo_elemento = minha_lista[-1]    # 50

print("Primeiro:", primeiro_elemento)
print("Segundo:", segundo_elemento)
print("Último:", ultimo_elemento)
```

***

"""
frutas = ["laranja", "maca", "banana", "uva"]

frutas = []

letras = list("python")

numeros = list(range(1, 11))

carro = ["fusca", 1970, "azul", 4]

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