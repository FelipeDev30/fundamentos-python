import json
import os

class Bicicleta: # Define a classe Bicicleta, que representa o "molde" para criação de objetos do tipo bicicleta com seus atributos e comportamentos.
    def __init__(self, cor, modelo, ano, valor): # Método construtor que inicializa os atributos de cada objeto criado a partir da classe Bicicleta.
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def exibir_informacoes(self): # Método que retorna uma string formatada com as informações da bicicleta, facilitando a visualização dos detalhes do objeto.
        return f"Bicicleta: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Valor: R$: {self.valor:.2f}"
    
    def buzinar(self):
        return f"{self.modelo} está buzinando: BEEP BEEP!"
    
    def parar(self):
        return f"{self.modelo} parou de se mover."
    
    def correr(self):
        return f"{self.modelo} está correndo pela estrada!"
    
    def to_dict(self): # Método que converte os atributos do objeto em um dicionário, facilitando a serialização para formatos como JSON.
        return {
            "cor": self.cor,
            "modelo": self.modelo,
            "ano": self.ano,
            "valor": self.valor
        }
    
    @classmethod
    def from_dict(cls, data): # Método de classe que cria um objeto Bicicleta a partir de um dicionário, permitindo a desserialização de dados armazenados em formatos como JSON.
        return cls(data["cor"], data["modelo"], data["ano"], data["valor"])

def salvar_estoque(estoque, arquivo="estoque.json"): # Função que salva o estoque de bicicletas em um arquivo JSON, convertendo cada objeto Bicicleta em um dicionário usando o método to_dict.
    with open(arquivo, "w") as f:
        json.dump([bike.to_dict() for bike in estoque], f, indent=4)

def carregar_estoque(arquivo="estoque.json"): # Função que carrega o estoque de bicicletas a partir de um arquivo JSON, verificando se o arquivo existe e, em caso afirmativo, lendo os dados e convertendo cada dicionário em um objeto Bicicleta usando o método from_dict.
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            data = json.load(f)
            return [Bicicleta.from_dict(item) for item in data]
    return []
    

def comprar_bicicleta(): # Função que simula a compra de uma bicicleta, solicitando ao usuário as informações necessárias para criar um objeto Bicicleta e retornando esse objeto. A função também inclui tratamento de exceções para garantir que as entradas sejam válidas.
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

def lançar_venda(bicicleta): # Função que simula o lançamento de uma venda, exibindo os detalhes da bicicleta vendida e confirmando que a venda foi registrada com sucesso.
    print("\n--- Detalhes da Venda ---")
    print(bicicleta.exibir_informacoes())
    print("Venda registrada com sucesso!")

def exibir_comportamentos(bicicleta): # Função que exibe os comportamentos de uma bicicleta específica, chamando os métodos de comportamento (buzinar, correr e parar) do objeto Bicicleta e exibindo suas respostas.
    print("\n--- Comportamentos da Bicicleta ---")
    print(bicicleta.buzinar())
    print(bicicleta.correr())
    print(bicicleta.parar())

def exibir_estoque(estoque): # Função que exibe o estoque de bicicletas, listando cada bicicleta com suas informações e calculando o valor total do estoque. Se o estoque estiver vazio, uma mensagem apropriada é exibida.
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

def vender_bicicleta(estoque, total_vendas): # Função que simula a venda de uma bicicleta, permitindo ao usuário escolher uma bicicleta do estoque para vender. A função remove a bicicleta do estoque, lança a venda e atualiza o total de vendas, adicionando 30% ao valor da bicicleta vendida. A função também inclui tratamento de exceções para garantir que as entradas sejam válidas.
    exibir_estoque(estoque)
    if not estoque:
        return total_vendas
    try:
        indice = int(input("Digite o número da bicicleta a vender: ")) - 1 
        if 0 <= indice < len(estoque):
            bike = estoque.pop(indice)
            lançar_venda(bike)
            bike.valor = bike.valor + (bike.valor * 0.3)  # Adiciona 30% ao valor da bicicleta
            total_vendas += bike.valor
            print(f"Valor adicionado às vendas: R$ {bike.valor:.2f}")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
    return total_vendas

def main(): # Função principal que gerencia o fluxo do programa, incluindo a exibição do menu, a manipulação do estoque de bicicletas e o controle das vendas. A função utiliza um loop para permitir que o usuário interaja com o sistema até que decida sair, e inclui chamadas para as funções de compra, venda, exibição de estoque e comportamentos das bicicletas.
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

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (em vez de importado como um módulo) e, nesse caso, chama a função main para iniciar o programa.
    main()