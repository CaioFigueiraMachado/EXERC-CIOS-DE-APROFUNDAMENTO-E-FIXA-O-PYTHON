#Caio Machado   2BDEV
def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


if __name__ == "__main__":
    ano = int(input("Digite o ano: "))
    if eh_bissexto(ano):
        print(f"{ano} é bissexto.")
    else:
        print(f"{ano} não é bissexto.")
