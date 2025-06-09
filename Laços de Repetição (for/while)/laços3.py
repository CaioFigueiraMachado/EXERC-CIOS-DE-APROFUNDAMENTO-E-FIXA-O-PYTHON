
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso em kg: "))


imc = peso / (altura ** 2)


print(f"Seu IMC é: {imc:.2f}")


if imc < 18.5:
    print("Classificação: Baixo peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade Grau I")
elif imc < 40:
    print("Classificação: Obesidade Grau II")
else:
    print("Classificação: Obesidade Grau III (obesidade mórbida)")
