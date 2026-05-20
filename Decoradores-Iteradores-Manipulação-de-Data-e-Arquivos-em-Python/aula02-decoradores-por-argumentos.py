def meu_decorador(funcao):
    def funcao_decorada(*args, **kwargs):
        print("Antes da função ser chamada.")
        resultado = funcao(*args, **kwargs)
        print("Depois da função ser chamada.")
        return resultado
    return funcao_decorada

@meu_decorador
def ola_mundo(nome = ""):
    if not nome:
        nome = input("Digite seu nome: ")
    print(f"Olá, {nome.upper()}! Bem-vindo ao mundo dos decoradores!")
    return nome

ola_mundo()

print("\n" + "-"*50 + "\n")

def duplicar(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    
    return wrapper

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}!")
    
aprender("Python")
