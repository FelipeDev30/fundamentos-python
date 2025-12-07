def calculadora(n1, n2):
    """Retorna um dicionário com várias operações matemáticas entre dois números."""
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
