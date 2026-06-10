"""
Aula 01 - Parte 3: Métodos de Listas em Python

Esta aula explora os métodos mais comuns para manipular listas em Python.
Cada método é explicado com exemplos práticos para facilitar o aprendizado.

Objetivos de aprendizagem:
- Entender o que são métodos de listas
- Aprender a usar métodos como append, clear, extend, etc.
- Praticar com exemplos e exercícios
"""

# =============================================================================
# INTRODUÇÃO AOS MÉTODOS DE LISTAS
# =============================================================================

# Métodos de listas são funções integradas que permitem modificar e consultar listas.
# Eles facilitam operações comuns sem precisar implementar algoritmos do zero.

# Lista inicial para demonstrações
lista = [1, "dois", 3.0, True]
print("Lista inicial:", lista)
print()

# =============================================================================
# 1. APPEND() - Adiciona um elemento ao final da lista
# =============================================================================

print("=== 1. APPEND() ===")
print("Adiciona um elemento ao final da lista.")
lista.append("novo valor")
print("Após append('novo valor'):", lista)
print()

# =============================================================================
# 2. CLEAR() - Remove todos os elementos da lista
# =============================================================================

print("=== 2. CLEAR() ===")
print("Remove todos os elementos da lista, deixando-a vazia.")
lista.clear()
print("Após clear():", lista)
print()

# =============================================================================
# 3. EXTEND() - Adiciona múltiplos elementos ao final da lista
# =============================================================================

print("=== 3. EXTEND() ===")
print("Adiciona múltiplos elementos (de outra lista ou iterável) ao final.")
lista = [1, "dois", 3.0, True]  # Recriando a lista
lista.extend(["quatro", 5])
print("Após extend(['quatro', 5]):", lista)
print()

# =============================================================================
# 4. COPY() - Retorna uma cópia da lista
# =============================================================================

print("=== 4. COPY() ===")
print("Cria uma cópia superficial da lista (não afeta a original se modificada).")
l2 = lista.copy()
print("Lista original:", lista)
print("Lista copiada (l2):", l2)
l2.append("outro valor")
print("Após modificar l2:", l2)
print("Lista original permanece:", lista)
print()

# =============================================================================
# 5. COUNT() - Conta ocorrências de um elemento
# =============================================================================

print("=== 5. COUNT() ===")
print("Conta quantas vezes um elemento específico aparece na lista.")
print("Contagem de 'dois':", lista.count("dois"))
print("Contagem de 3.0:", lista.count(3.0))

# Exemplo com lista de cores
cores = ["vermelho", "verde", "azul", "vermelho"]
print("Lista de cores:", cores)
print("Contagem de 'vermelho':", cores.count("vermelho"))
print()

# =============================================================================
# 6. INDEX() - Retorna o índice da primeira ocorrência
# =============================================================================

print("=== 6. INDEX() ===")
print("Retorna o índice da primeira ocorrência de um elemento.")
print("Lista de cores:", cores)
print("Índice de 'azul':", cores.index("azul"))
print("Índice de 'vermelho':", cores.index("vermelho"))  # Primeira ocorrência
print()

# =============================================================================
# 7. POP() - Remove e retorna o último elemento
# =============================================================================

print("=== 7. POP() ===")
print("Remove e retorna o último elemento da lista (ou um índice específico).")
linguagens = ["Python", "Java", "C++", "Python"]
print("Lista de linguagens:", linguagens)
removido = linguagens.pop()
print("Elemento removido:", removido)
print("Após pop():", linguagens)
print()

# =============================================================================
# 8. REMOVE() - Remove a primeira ocorrência de um elemento
# =============================================================================

print("=== 8. REMOVE() ===")
print("Remove a primeira ocorrência de um elemento específico.")
print("Lista atual:", linguagens)
linguagens.remove("Java")
print("Após remove('Java'):", linguagens)
print()

# =============================================================================
# 9. REVERSE() - Inverte a ordem dos elementos
# =============================================================================

print("=== 9. REVERSE() ===")
print("Inverte a ordem dos elementos na lista.")
print("Lista atual:", linguagens)
linguagens.reverse()
print("Após reverse():", linguagens)
print()

# =============================================================================
# 10. SORT() - Ordena os elementos da lista
# =============================================================================

print("=== 10. SORT() ===")
print("Ordena os elementos da lista em ordem crescente (ou decrescente).")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print("Lista de números:", numeros)
numeros.sort()
print("Após sort() (crescente):", numeros)
numeros.sort(reverse=True)
print("Após sort(reverse=True) (decrescente):", numeros)
print()

# =============================================================================
# 11. LAMBDA E SORT() - Ordenação personalizada
# =============================================================================

print("=== 11. LAMBDA E SORT() ===")
print("Ordena os elementos da lista com uma função personalizada.")
nomes = ["Alice", "Bob", "Charlie", "David"]
print("Lista de nomes:", nomes)
nomes.sort(key=lambda x: len(x))  # Ordena por comprimento
print("Após sort(key=lambda x: len(x)):", nomes)
print()

# =============================================================================
# 12. SPLIT() - Divide uma string em uma lista
# =============================================================================

print("=== 12. SPLIT() ===")
print("Divide uma string em uma lista de substrings.")
frase = "Python é uma linguagem de programação"
palavras = frase.split()
print("Lista de palavras:", palavras)
print()

# =============================================================================
# 13. JOIN() - Junta elementos de uma lista em uma string
# =============================================================================

print("=== 13. JOIN() ===")
print("Junta elementos de uma lista em uma string.")
palavras = ["Python", "é", "uma", "linguagem", "de", "programação"]
frase = " ".join(palavras)
print("Frase resultante:", frase)
print()

# =============================================================================
# 14. LEN() - Retorna o número de elementos na lista
# =============================================================================
print("=== 14. LEN() ===")
print("Retorna o número de elementos na lista.")
print("Lista de palavras:", palavras)
print("Número de palavras:", len(palavras))

# =============================================================================
# 15. SORTED() - Retorna uma nova lista ordenada
# =============================================================================
print("=== 15. SORTED() ===")
print("Retorna uma nova lista ordenada, sem modificar a original.")
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print("Lista de números:", numeros)
numeros_ordenados = sorted(numeros)
print("Nova lista ordenada:", numeros_ordenados)
print("Lista original permanece:", numeros)

lista.first()

# =============================================================================
# EXERCÍCIOS PARA PRÁTICA
# =============================================================================

print("=== EXERCÍCIOS ===")
print("1. Crie uma lista com 5 frutas e use append() para adicionar mais uma.")
print("2. Use count() para contar quantas vezes 'Python' aparece em ['Python', 'Java', 'Python'].")
print("3. Use sort() para ordenar uma lista de nomes em ordem alfabética.")
print("4. Experimente remove() e pop() em uma lista própria.")
print()

# =============================================================================
# CONCLUSÃO
# =============================================================================

print("=== CONCLUSÃO ===")
print("Estes são os métodos fundamentais de listas em Python.")
print("Pratique-os para se familiarizar com a manipulação de dados em listas.")
print("Para mais detalhes, consulte a documentação oficial do Python.")