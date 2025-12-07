n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if(media >= 7):
    print(f"Aluno aprovado com média {media:.2f}")
elif(media < 7 and media >= 5):
    print(f"Aluno em recuperação com média {media:.2f}")
elif(media < 5):
    print(f"Aluno reprovado com média {media:.2f}") 