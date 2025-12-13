""" 
For loop em Python

Este código demonstra como usar um loop 'for' em Python para repetir uma ação várias vezes.

O for é muito utilizado para iterar sobre sequências (como listas, tuplas, dicionários, conjuntos e strings) ou para repetir um bloco de código um número específico de vezes.

Sintaxe básica do for loop:

for item in sequência:
    # bloco de código a ser repetido
    ação(item)

Exemplo de uso do for loop para repetir uma ação 5 vezes:
for i in range(5):
    print("Repetição número:", i)

"""

for i in range(0, 51, 5):
    print("Tabulada de 5 contagem:", i)

print()

texto = input("Digite um texto: ")
VOGAIS = "aeiouAEIOU"

for letra in texto:
    if letra in VOGAIS:
        print(letra, end=" ")
else:
    print("\nFim do programa.")

print()

# Exemplo de uso do while loop para criar um menu interativo
opcao = -1

while opcao != 0:
    opcao = int(input("Digite um número (\n[1] Sacar \n[2] Extrato e \n[0] para sair): "))
    if opcao != 0:
        print("Você digitou:", opcao)
        if opcao == 1:
            print("Saque realizado com sucesso!")
        elif opcao == 2:
            print("Exibindo extrato...")
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção inválida, tente novamente.")
print("Fim do programa.")


