""" 
# O que é indentação e blocos em Python?
# Indentação refere-se ao espaço em branco no início de uma linha de código. 
# Blocos são grupos de linhas de código que pertencem a uma mesma estrutura de controle, como funções, loops ou condicionais.
# Em Python, a indentação é crucial para definir a estrutura do código. Diferente de outras linguagens que usam chaves ou palavras-chave para delimitar blocos, Python utiliza a indentação para esse propósito.

# Exemplo de bloco de código com indentação correta:
def saudacao(nome):
    if nome:
        print(f"Olá, {nome}!")
    else:
        print("Olá, mundo!")
saudacao("Alice")

# Exemplo de bloco de código com indentação incorreta:
def saudacao(nome):
if nome:
print(f"Olá, {nome}!")
else:
print("Olá, mundo!")
# O código acima gerará um erro de indentação.


"""