class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(self):
        if self.acordado:
            return f"{self.nome} está latindo: Au Au!"
        else:
            return f"{self.nome} está dormindo e não pode latir."
    
    def dormir(self):
        self.acordado = False
        return f"{self.nome} agora está dormindo."
    
    def acordar(self):
        self.acordado = True
        return f"{self.nome} agora está acordado."
    
    def __del__(self):
        print(f"{self.nome} foi deletado da memória.")
    
# Criando um cachorro
meu_cachorro = Cachorro("Rex", "Marrom")
print(meu_cachorro.latir())  # Rex está latindo: Au Au!
print(meu_cachorro.dormir())  # Rex agora está dormindo.
print(meu_cachorro.latir())  # Rex está dormindo e não pode latir.
print(meu_cachorro.acordar())  # Rex agora está acordado.
print(meu_cachorro.latir())  # Rex está latindo: Au Au!

# Deletando o cachorro
del meu_cachorro

print(meu_cachorro) # Isso causará um erro, pois meu_cachorro foi deletado.