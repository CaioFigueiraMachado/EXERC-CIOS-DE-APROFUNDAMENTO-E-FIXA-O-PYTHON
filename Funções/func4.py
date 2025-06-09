def maior_numero(lista):
    return max(lista)



if __name__ == "__main__":
    numeros = input("Digite os números separados por espaço: ")
    lista = [float(num) for num in numeros.split()]
    print("Maior número:", maior_numero(lista))
