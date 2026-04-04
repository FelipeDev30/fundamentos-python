""" 
# O que são parâmetros especiais?

Por padrão, argumentos podem ser passados para uma fução Python tanto por posição quanto explicitamente pelo nome. 
Para uma melhor legilibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam se passados,
assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição,
por posição e nome, ou por nome.

# Parâmetros posicionais obrigatórios são definidos antes da barra (/) na definição da função. Eles devem ser passados por posição e não podem ser passados por nome.
# Parâmetros de palavra-chave obrigatórios são definidos após o asterisco (*) na definição da função. Eles devem ser passados por nome e não podem ser passados por posição.
# Parâmetros de palavra-chave ou posicionais são definidos entre a barra (/) e o asterisco (*) na definição da função. Eles podem ser passados por posição ou por nome, oferecendo flexibilidade ao chamar a função.

"""
def criar_carros(modelo, ano, placa, / , marca, *, motor, combustivel):
    print(f"Modelo: {modelo}")
    print(f"Ano: {ano}")
    print(f"Placa: {placa}")
    print(f"Marca: {marca}")
    print(f"Motor: {motor}")
    print(f"Combustível: {combustivel}")
    print(f"Motor: {motor}")

criar_carros("Civic", 2020, "ABC-1234", marca="Honda",motor="2.0", combustivel="Gasolina") # Válido
criar_carros("Civic", 2020, "ABC-1234", "Honda", motor="2.0", combustivel="Gasolina") # Válido

""" 
criar_carros(modelo="Civic", ano=2020, placa="ABC-1234", marca="Honda", motor="2.0", combustivel="Gasolina") # Inválido
criar_carros("Civic", 2020, "ABC-1234", "Honda", "2.0", "Gasolina") # Inválido 

"""


