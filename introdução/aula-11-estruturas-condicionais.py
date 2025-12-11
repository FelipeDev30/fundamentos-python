""" 
# O que são estruturas condicionais?
Estruturas condicionais são usadas para tomar decisões no código com base em certas condições. Elas permitem que o programa execute diferentes blocos de código dependendo do valor de uma expressão booleana (verdadeiro ou falso).
# Exemplo de estrutura condicional em Python

"""
import sys

idade = int(input("Digite sua idade: "))
if idade >= 18: 
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

opcao =int(input("Escolha uma opção ([1] sacar, \n[2] Extrto: "))

def sacar(valor, saldo):
    valor = float(input("Digite o valor para saque: "))
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    else:
        saldo -= valor
    print("Saque realizado com sucesso!")
    exibir_extrato(saldo, f"Saque: R$ {valor:.2f}")

def exibir_extrato(saldo, extrato):
    print("\nExtrato:")
    print("Saldo: R$", saldo)
    print("Movimentações:")
    print(extrato)

if opcao == 1:
    saldo = 1000.0  # Exemplo de saldo inicial
    sacar(0, saldo)
elif opcao == 2:
    saldo = 1000.0  # Exemplo de saldo inicial
    extrato = "Saque: R$ 200.00\nDepósito: R$ 500.00"  # Exemplo de extrato
    exibir_extrato(saldo, extrato)
else:
    sys.exit("Opção inválida, encerrando o programa.")

