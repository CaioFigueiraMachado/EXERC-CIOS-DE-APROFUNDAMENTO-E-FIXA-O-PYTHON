def inverter_string(palavra):
    return palavra[::-1]



if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    print("Invertida:", inverter_string(palavra))
