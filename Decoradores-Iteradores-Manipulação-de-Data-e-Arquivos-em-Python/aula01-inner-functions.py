""" 
O que são inner functions?

Inner functions é a possibilidade de definir funções dentro de outras funções. 
Tais funções são chamadas de funções internas

"""

nome = input("Digite seu nome: ")

def dizer_oi(nome):
    return f"Oi {nome}"

def incentivar_aprender(nome):
    return f"Oi {nome}, vamos aprender Pyhton juntos!"

def mensagem_para_pessoa(funcao_mensagem):
    return funcao_mensagem(nome)

print(mensagem_para_pessoa(incentivar_aprender))

""" 
def pai():
    print("Escrevendo da pai() função")
    
    def filho1():
        print("Escrevendo da filho1() função")
    
    def filho2():
        print("Escrevendo da filho2() função")
    
    filho2()
    filho1()

pai()
"""
def calcular(operacoes):
    def soma(n1, n2):
        return n1 + n2
    
    def sub(n1, n2):
        return n1 - n2
    
    def mul(n1, n2):
        return n1 * n2
    
    def div(n1, n2):
        return n1 / n2
    
    match operacoes:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        case "":
            return f"Operação inválida!"

resultado = calcular("/")(1, 3)
print(resultado)