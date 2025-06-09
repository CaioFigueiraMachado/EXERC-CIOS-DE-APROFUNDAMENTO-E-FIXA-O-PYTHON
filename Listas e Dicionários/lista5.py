#Caio Machado   2BDEV
carrinho = {}

while True:
    nome = input("Nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    preco = float(input("Preço do produto: "))
    carrinho[nome] = preco

total = sum(carrinho.values())

print("Produtos no carrinho:")
for produto, preco in carrinho.items():
    print(f"{produto}: R${preco:.2f}")

print(f"Total da compra: R${total:.2f}")
