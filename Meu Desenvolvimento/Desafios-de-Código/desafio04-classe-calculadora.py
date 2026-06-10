class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def exibir_resultado(self, resultado):
        print(f"O resultado da soma é: {resultado}")

calculadora = Calculadora()

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado = calculadora.soma(a, b)
calculadora.exibir_resultado(resultado)