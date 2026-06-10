"""
O que é o break?

O break é uma palavra-chave em Python que é usada para interromper a execução de um loop (for ou while) antes que ele tenha percorrido toda a sequência ou antes que a condição do loop seja falsa.
Quando o break é executado, o controle do programa é transferido para a primeira linha de código após o bloco do loop.

Sintaxe do break:

for item in sequência:
    if condição_de_parada:
        break
    # bloco de código a ser repetido
    ação(item)

Exemplo de uso do break em um loop for:

for i in range(10):
    if i == 5:
        break
    print("Número:", i)

Neste exemplo, o loop for irá imprimir os números de 0 a 4. Quando i for igual a 5, o break será executado, e o loop será interrompido, não imprimindo mais números.

Exemplo de uso do break em um loop while:

contador = 0

while True:
    print("Contador:", contador)
    contador += 1
    if contador >= 5:
        break

Neste exemplo, o loop while irá imprimir os valores do contador de 0 a 4. Quando o contador atingir 5, o break será executado, e o loop será interrompido, não imprimindo mais valores.


"""

opcao = -1

while True:
    numero = int(input("Digite um número: "))

    if numero == 10:
        print("Você digitou:", numero)
        break
    else:
        print("Você digitou:", numero)