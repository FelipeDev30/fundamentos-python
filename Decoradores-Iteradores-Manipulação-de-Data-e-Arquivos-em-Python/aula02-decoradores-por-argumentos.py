def meu_decorador(funcao):
    def wrapper(*args, **kwargs):
        return funcao(*args, **kwargs)
    return wrapper

@meu_decorador
def saudacao(nome="", idade=0):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print(f"Olá, {nome}! Você tem {idade} anos.")

saudacao()