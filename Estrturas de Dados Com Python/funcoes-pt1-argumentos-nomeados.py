""" 
# Argumentos nomeados o que são?
Argumentos nomeados são uma forma de passar argumentos para uma função usando o nome do parâmetro em vez de sua posição. Isso torna o código mais legível e fácil de entender, especialmente quando a função tem muitos parâmetros ou quando os parâmetros têm valores padrão.

# Exemplo de função com argumentos nomeados
def saudacao(nome, idade):
    return f"Olá, {nome}! Você tem {idade} anos."
# Usando argumentos nomeados
print(saudacao(nome="Alice", idade=30))

# Argumentos nomeados também permitem que você altere a ordem dos argumentos
print(saudacao(idade=25, nome="Bob"))

"""

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso: {marca} {modelo} ({ano}) - Placa: {placa}")

# Usando argumentos nomeados

salvar_carro("Fiat", "Uno", 2018, "XYZ-5678") # Usando argumentos posicionais, a ordem dos argumentos é importante e pode ser confusa
salvar_carro(marca="Chevrolet", modelo="Onix", ano=2020, placa="ABC-1234") # Usando argumentos nomeados para melhorar a legibilidade
salvar_carro(**{"modelo": "Civic", "marca": "Honda", "ano": 2019, "placa": "DEF-5678"}) # Usando um dicionário para passar os argumentos nomeados



