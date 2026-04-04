""" 
# O que são funções?
- Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas são definidas usando a palavra-chave def seguida do nome da função e parênteses ().
- As funções podem receber parâmetros, que são valores de entrada, e podem retornar um valor usando a palavra-chave return.

# Exemplo de função simples

"""
def saudacao():
    print("Olá, seja bem-vindo!")
saudacao()  # Output: Olá, seja bem-vindo!

# Exemplo de função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")
saudacao("Maria")  # Output: Olá, Maria! Seja bem-vindo!

# Exemplo de função com retorno
def soma(a, b):
    return a + b
resultado = soma(5, 3)
print(resultado)  # Output: 8

def calcular_total(numeros):
    return sum(numeros)
total = calcular_total([1, 2, 3, 4, 5])
print(total)  # Output: 15

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

antecessor, sucessor = retorna_antecessor_sucessor(10)
print(f"Antecessor: {antecessor}, Sucessor: {sucessor}")  # Output: Antecessor: 9, Sucessor: 11