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

def duplicar(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}!")
    return tecnologia.upper()

tecnologia = aprender("Python")
print(tecnologia)