""" 
Encapsulamento - Aula 03 - Property

O que é property?
Property é uma função decoradora (decorator) que tem a função de transformar métodos em atributos, ou seja, podemos acessar um método como se fosse um atributo, sem a necessidade de usar os parênteses.
Isso é útil para criar atributos calculados, ou seja, atributos que são calculados a partir de outros atributos, sem a necessidade de criar um método para isso.

Exemplo:

"""
class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value
    
    @x.deleter
    def x(self):
        self._x = 1

foo = Foo(10)
print(foo.x) # 10
foo.x = 5
print(foo.x) # 15
del foo.x
print(foo.x) # 1