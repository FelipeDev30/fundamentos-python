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

Quer que eu também **explique operações comuns com listas** (como adicionar, remover, ordenar, percorrer) e **crie um mini-guia com exemplos práticos**?  
Posso até gerar um **PDF bem formatado** com esse conteúdo para você usar como material de estudo ou compartilhar. Quer que eu faça isso?

"""

frutas = ['maçã', 'banana', 'cereja', 'damasco']
print(frutas[0])  # Output: maçã
print(frutas[2])  # Output: cereja

numeros = list(range(1, 6))  # Cria uma lista [1, 2, 3, 4, 5]
print(numeros[4])  # Output: 5
print(numeros[-1]) # Output: 5
print(numeros[-3]) # Output: 3