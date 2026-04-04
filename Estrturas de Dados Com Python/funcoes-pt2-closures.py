""" 
# O que são closures?
Closures são funções que "lembram" do ambiente em que foram criadas, mesmo depois de terem sido executadas. Isso significa que uma função interna pode acessar e modificar variáveis da função externa, mesmo após a função externa ter sido concluída.

# Exemplo de closure

"""
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")

exibir_resultado(5, 3, somar)
exibir_resultado(5, 3, subtrair)

op = somar
print(op(10, 20)) # Saída: 30