produtos = {}

for _ in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    produtos[nome] = preco

mais_caro = max(produtos, key=produtos.get)
mais_barato = min(produtos, key=produtos.get)

print(f"Mais caro: {mais_caro} - R${produtos[mais_caro]:.2f}")
print(f"Mais barato: {mais_barato} - R${produtos[mais_barato]:.2f}")
