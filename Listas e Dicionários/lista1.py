#Caio Machado   2BDEV
contatos = {}

for _ in range(3):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    contatos[nome] = telefone

busca = input("Digite o nome para buscar: ")

if busca in contatos:
    print(f"Telefone de {busca}: {contatos[busca]}")
else:
    print("Nome não encontrado.")
