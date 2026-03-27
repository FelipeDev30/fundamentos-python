""" 
# interpolação de Variáveis em Python

Em Python, a interpolação de variáveis permite inserir valores de variáveis dentro de strings de maneira fácil e legível. 
Existem várias maneiras de fazer isso, incluindo o uso do operador `%`, o método `str.format()` e as f-strings (disponíveis a partir do Python 3.6).

"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
profissao = input("Digite sua profissão: ")
linguagem = input("Digite sua linguagem de programação favorita: ")

dados = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": linguagem
}

# Usando o operador %%
mensagem1 = "Olá, %s! Você tem %d anos, trabalha como %s e gosta de programar em %s." % (dados["nome"], dados["idade"], dados["profissao"], dados["linguagem"])
print(mensagem1)

# Usando o método str.format()
mensagem2 = "Olá, {}! Você tem {} anos, trabalha como {} e gosta de programar em {}.".format(dados["nome"], dados["idade"], dados["profissao"], dados["linguagem"])
print(mensagem2)

# Usando f-strings
mensagem3 = f"Olá, {dados['nome']}! Você tem {dados['idade']} anos, trabalha como {dados['profissao']} e gosta de programar em {dados['linguagem']}."
print(mensagem3) 