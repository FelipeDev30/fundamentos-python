""" 

Operadores de associação

O quê são operadores de associação?
São operadores que verificam se um valor existe ou não em uma sequência (string, lista, tupla, etc).

in -> Verifica se o valor existe na sequência
not in -> Verifica se o valor não existe na sequência

Exemplos:

"""

cursos = "Curso de Python"
frutas = ["uva", "Pera", "Banana"]

print("laranja" in frutas)
print("Python" in cursos)
print("laranja" not in frutas)
print("Python" not in cursos)
print("uva" in frutas)
print("uva" not in frutas)