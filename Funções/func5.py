#Caio Machado   2BDEV
def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]



if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    print("É palíndromo?", eh_palindromo(palavra))
