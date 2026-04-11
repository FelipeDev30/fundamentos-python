""" 
# Programação Orientada a Objetos (POO) - Aula 01: Primeiro Programa

    João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
    Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!

1. Definição da Estrutura de Dados (A Classe)
O coração do programa é a classe Bicicleta. Ela serve como um "molde" para criar objetos que representam bicicletas reais no sistema
.
Atributos: No método __init__, definimos as características de cada bicicleta: cor, modelo, ano e valor
.
Comportamentos: Embora a definição completa dos métodos não apareça no texto, o código utiliza métodos como buzinar(), correr(), parar() e exibir_informacoes() para interagir com o objeto
.
2. Gerenciamento de Persistência (Salvando e Lendo Arquivos)
Para evitar que os dados se percam ao fechar o programa, o código utiliza a biblioteca json
.
Salvando: A função salvar_estoque percorre a lista de bicicletas, converte cada objeto em um dicionário (via to_dict()) e grava no arquivo "estoque.json" com indentação para facilitar a leitura
.
Carregando: A função carregar_estoque verifica se o arquivo existe usando os.path.exists
. Se existir, ele lê o arquivo e reconstrói os objetos Bicicleta a partir dos dados salvos usando um método de fábrica (from_dict)
.
3. Entrada de Dados e Criação de Objetos
A função comprar_bicicleta (que no contexto do sistema significa "adicionar ao estoque") gerencia a interação com o usuário
.
Validação: O código utiliza um bloco try-except para capturar erros de entrada (como digitar letras onde deveriam ser números no ano ou valor), evitando que o programa trave
.
Instanciação: Após coletar cor, modelo, ano e valor, ele cria uma nova instância da classe Bicicleta e a retorna
.
4. Lógica de Vendas e Manipulação de Listas
O sistema trata o estoque como uma lista de objetos
.
Venda: Na função vender_bicicleta, o programa exibe o estoque e pede ao usuário o índice (número) da bicicleta
.
Remoção: Se o índice for válido, o método estoque.pop(indice) é usado para remover a bicicleta da lista de estoque e o valor dela é somado ao total_vendas
.
Registro: A função lançar_venda apenas exibe uma confirmação visual de que a venda foi processada com sucesso
.
5. Visualização e Relatórios
Existem funções dedicadas a mostrar o estado atual do sistema:
Exibir Estoque: Percorre a lista, mostra as informações de cada bicicleta e calcula o valor total em estoque acumulando o atributo bike.valor em uma variável
.
Exibir Comportamentos: Demonstra a funcionalidade do objeto chamando seus métodos internos
.
6. O Fluxo Principal (Loop de Execução)
Toda a lógica é orquestrada pela função main() e o bloco if __name__ == "__main__":
.
Menu Interativo: Um loop while True mantém o programa rodando, apresentando seis opções ao usuário (comprar, vender, exibir estoque, etc.)
.
Persistência Automática: Ao iniciar, o estoque é carregado do arquivo
. (Nota: Para um estudo completo, seria ideal que o salvar_estoque fosse chamado após cada alteração no estoque, embora essa chamada específica não apareça no trecho final do menu fornecido).

"""
import json
import os

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def exibir_informacoes(self):
        return f"Bicicleta: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Valor: R$: {self.valor:.2f}"
    
    def buzinar(self):
        return f"{self.modelo} está buzinando: BEEP BEEP!"
    
    def parar(self):
        return f"{self.modelo} parou de se mover."
    
    def correr(self):
        return f"{self.modelo} está correndo pela estrada!"
    
    def to_dict(self):
        return {
            "cor": self.cor,
            "modelo": self.modelo,
            "ano": self.ano,
            "valor": self.valor
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["cor"], data["modelo"], data["ano"], data["valor"])

def salvar_estoque(estoque, arquivo="estoque.json"):
    with open(arquivo, "w") as f:
        json.dump([bike.to_dict() for bike in estoque], f, indent=4)

def carregar_estoque(arquivo="estoque.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            data = json.load(f)
            return [Bicicleta.from_dict(item) for item in data]
    return []
    

def comprar_bicicleta():
    print("Bem-vindo à bicicletaria do João!")
    try:
        cor = input("Digite a cor da bicicleta: ")
        modelo = input("Digite o modelo da bicicleta: ")
        ano = int(input("Digite o ano da bicicleta: "))
        valor = float(input("Digite o valor da bicicleta: "))
        bicicleta = Bicicleta(cor, modelo, ano, valor)
        return bicicleta
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return None

def lançar_venda(bicicleta):
    print("\n--- Detalhes da Venda ---")
    print(bicicleta.exibir_informacoes())
    print("Venda registrada com sucesso!")

def exibir_comportamentos(bicicleta):
    print("\n--- Comportamentos da Bicicleta ---")
    print(bicicleta.buzinar())
    print(bicicleta.correr())
    print(bicicleta.parar())

def exibir_estoque(estoque):
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\n--- Estoque de Bicicletas ---")
        total_valor = 0
        for i, bike in enumerate(estoque):
            print(f"{i+1}. {bike.exibir_informacoes()}")
            total_valor += bike.valor
        print(f"\nTotal de bicicletas: {len(estoque)}")
        print(f"Valor total do estoque: R$ {total_valor:.2f}")

def vender_bicicleta(estoque, total_vendas):
    exibir_estoque(estoque)
    if not estoque:
        return total_vendas
    try:
        indice = int(input("Digite o número da bicicleta a vender: ")) - 1
        if 0 <= indice < len(estoque):
            bike = estoque.pop(indice)
            lançar_venda(bike)
            total_vendas += bike.valor
            print(f"Valor adicionado às vendas: R$ {bike.valor:.2f}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
    return total_vendas

def main():
    estoque = carregar_estoque()
    total_vendas = 0  # Pode ser carregado também, mas para simplicidade, inicia em 0
    while True:
        print("\n--- Sistema de Compra e Venda de Bicicletas ---")
        print("1. Comprar bicicleta (adicionar ao estoque)")
        print("2. Vender bicicleta")
        print("3. Exibir estoque")
        print("4. Exibir comportamentos de uma bicicleta")
        print("5. Ver total de vendas")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            bike = comprar_bicicleta()
            if bike:
                estoque.append(bike)
                print("Bicicleta adicionada ao estoque!")
        elif opcao == "2":
            total_vendas = vender_bicicleta(estoque, total_vendas)
        elif opcao == "3":
            exibir_estoque(estoque)
        elif opcao == "4":
            exibir_estoque(estoque)
            if estoque:
                try:
                    indice = int(input("Digite o número da bicicleta para exibir comportamentos: ")) - 1
                    if 0 <= indice < len(estoque):
                        exibir_comportamentos(estoque[indice])
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")
        elif opcao == "5":
            print(f"\nTotal de vendas: R$ {total_vendas:.2f}")
        elif opcao == "6":
            salvar_estoque(estoque)
            print("Estoque salvo. Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()