def calculadora(n1, n2):
    """
    Retorna um dicionário com várias operações matemáticas entre dois números.
    
    :param n1: Primeiro número
    :param n2: Segundo número
    :return: Dicionário com os resultados das operações
    
    Operações incluídas:
    - Soma: n1 + n2
    - Subtração: n1 - n2
    - Multiplicação: n1 * n2
    - Divisão inteira: n1 // n2 (retorna None se n2 for zero)
    - Divisão: n1 / n2 (retorna None se n2 for zero
    - Módulo: n1 % n2 (retorna None se n2 for zero)
    - Exponenciação: n1 ** n2

    Ordem de precedência:
    1. Parênteses
    2. Exponenciação
    3. Multiplicação, Divisão, Divisão inteira, Módulo (da esquerda para a direita)
    4. Adição, Subtração (da esquerda para a direita)

    """
    # Tratamento de divisão por zero
    if n2 == 0:
        div_inteira = None
        div = None
        mod_div = None
    else:
        div_inteira = n1 // n2
        div = n1 / n2
        mod_div = n1 % n2

    resultados = {
        "soma": n1 + n2,
        "subtracao": n1 - n2,
        "multiplicacao": n1 * n2,
        "divisao_inteira": div_inteira,
        "divisao": div,
        "modulo": mod_div,
        "exponenciacao": n1 ** n2
    }

    return resultados


# Exemplo de uso:
res = calculadora(10, 2)
for operacao, valor in res.items():
    print(f"{operacao}: {valor}")