def contador_de_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador
# Solicite ao usuário que insira um texto
texto_usuario = input("Por favor, insira um texto: ")
print(f"O número de vogais no texto é: {contador_de_vogais(texto_usuario)}")

