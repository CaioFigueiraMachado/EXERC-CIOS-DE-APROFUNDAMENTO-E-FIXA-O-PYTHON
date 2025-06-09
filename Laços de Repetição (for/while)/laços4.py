#Caio Machado   2BDEV
valor = int(input("Digite o valor para saque (múltiplo de 10): "))


if valor % 10 != 0:
    print("Valor inválido. O valor deve ser múltiplo de 10.")
else:

    notas_50 = valor // 50
    valor %= 50

    notas_20 = valor // 20
    valor %= 20

    notas_10 = valor // 10
    valor %= 10

    print("Notas fornecidas:")
    if notas_50 > 0:
        print(f"R$50: {notas_50} nota(s)")
    if notas_20 > 0:
        print(f"R$20: {notas_20} nota(s)")
    if notas_10 > 0:
        print(f"R$10: {notas_10} nota(s)")
