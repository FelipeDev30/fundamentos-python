""" 
Escreva uma solução que informe se um determinado ano é bissexto. Um ano é considerado bissexto se ele for divisível por 4. No entanto, anos que são divisíveis por 100 não são bissextos, a menos que também sejam divisíveis por 400. Esta regra é usada para corrigir o calendário, de modo que ele fique em conformidade com o ano solar.

"""
# Solicite ao usuário que insira um ano
def verificador_ano_bissexto(ano):
    # Verifique se o ano é bissexto
    if(ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

ano = int(input("Por favor, insira um ano: "))
verificador_ano_bissexto(ano)
