""" 
Operadores de identidade são usados para comparar objetos, verificando se eles são o mesmo objeto na memória.
Eles retornam True ou False.
- `is`: Retorna True se ambos os operandos referirem-se ao mesmo objeto.
- `is not`: Retorna True se ambos os operandos não referirem-se ao mesmo objeto.

Exemplo:

"""
cursos = "Curso de Python"
escola = "Faculdade Libano"

print(cursos is escola)  # False, pois são objetos diferentes
print(cursos is not escola)  # True, pois são objetos diferentes

# Criando duas variáveis que referenciam o mesmo objeto
curso1 = "Curso de Python"
curso2 = curso1
print(curso1 is curso2)  # True, pois ambos referenciam o mesmo objeto
print(curso1 is not curso2)  # False, pois ambos referenciam o mesmo objeto
# Verificando com objetos mutáveis
lista1 = [1, 2, 3]
lista2 = lista1
print(lista1 is lista2)  # True, pois ambos referenciam o mesmo objeto
print(lista1 is not lista2)  # False, pois ambos referenciam o mesmo objeto
# Criando uma nova lista com os mesmos valores
lista3 = [1, 2, 3]
print(lista1 is lista3)  # False, pois são objetos diferentes, mesmo com os mesmos valores
print(lista1 is not lista3)  # True, pois são objetos diferentes