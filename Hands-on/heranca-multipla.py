""" 
O que é herança múltipla?

Herança múltipla é um conceito em programação orientada a objetos onde uma classe pode herdar características e comportamentos de mais de uma classe base. Isso permite que uma classe derive funcionalidades de várias classes, 
promovendo a reutilização de código e a flexibilidade na modelagem de objetos.

Exemplo de herança múltipla em Python:

"""
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_pena, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_pena = cor_pena
        self.cor_bico = cor_bico
    
class Ornitorrinco(Mamifero, Ave):
    pass 

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="marrom", cor_pena="cinza", cor_bico="preto")
print(ornitorrinco)   