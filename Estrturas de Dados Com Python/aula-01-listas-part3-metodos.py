lista = [1, "dois", 3.0, True]

lista.append("novo valor")  # Adiciona um novo valor ao final da lista
print("Após append:", lista)

lista.clear()
print("Após clear:", lista)  # Remove todos os elementos da lista

lista = [1, "dois", 3.0, True]  # Re-adiciona os elementos para demonstração
lista.extend(["quatro", 5])  # Adiciona múltiplos valores ao final da lista
print("Após extend:", lista)

l2 = lista.copy()
print("Após copy:", l2)  # Retorna uma cópia da lista

l2.append("outro valor")
print("Lista original:", lista)
print("Lista copiada:", l2)

print("Contagem de 'dois':", lista.count("dois"))  # Conta quantas vezes "dois" aparece na lista