def media_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print(f"Média: {media:.2f} - Aprovado")
    elif media >= 5:
        print(f"Média: {media:.2f} - Recuperação")
    else:
        print(f"Média: {media:.2f} - Reprovado")

if __name__ == "__main__":
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media_situacao(n1, n2, n3)