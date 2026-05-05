""" 
O que é Polimorfismo com Herança?

O polimorfismo com herança é um conceito que permite que objetos de classes derivadas sejam tratados como objetos da classe base. 
Isso é possível porque as classes derivadas herdam os métodos e atributos da classe base, e podem sobrescrever esses métodos para fornecer uma implementação específica.
O polimorfismo com herança é uma forma poderosa de reutilização de código, pois permite que você escreva código que pode trabalhar com objetos de diferentes classes sem se preocupar com suas implementações específicas.

Exemplo de Polimorfismo com Herança em Python:

"""
class Forma:
    def area(self):
        pass
    
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.14 * self.raio ** 2
    
def calcular_area(formas):
    for forma in formas:
        print(f"A área da {forma.__class__.__name__} é: {forma.area()}")
        
retangulo = Retangulo(5, 3)
circulo = Circulo(4)
formas = [retangulo, circulo]

calcular_area(formas)

""" 

Neste exemplo, a função `calcular_area` pode aceitar uma lista de objetos que são instâncias da classe `Forma` ou de suas subclasses. O método `area` é implementado de maneira diferente em cada subclass, mas a função `calcular_area` pode chamar esse método sem se preocupar com a implementação específica, demonstrando o polimorfismo com herança em ação.

"""
