"""

# O que são escopos global e local?
# Escopo global: é o escopo onde estão as variáveis globais, ou seja, aquelas que podem ser acessadas de qualquer parte do código.
# Escopo local: é o escopo onde estão as variáveis locais, ou seja, aquelas que só podem ser acessadas dentro de uma função ou bloco de código específico.

"""
# Exemplo de escopo global

salario = 2000 # Variável global

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))  # Saída: 2500
print(salario)  # Saída: 2500

# Exemplo de escopo local
def calcular_area_circulo(raio):
    pi = 3.14  # Variável local
    area = pi * (raio ** 2)
    return area
print(calcular_area_circulo(5))  # Saída: 78.5
# print(pi)  # Isso causará um erro, pois 'pi' é uma variável local e não pode ser acessada fora da função.
