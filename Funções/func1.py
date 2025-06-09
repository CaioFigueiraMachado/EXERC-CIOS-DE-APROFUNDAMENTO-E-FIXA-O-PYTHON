def boas_vindas(nome, idade):
    if idade > 60:
        print(f"Bem-vindo, {nome}! Você tem prioridade no atendimento.")
    else:
        print(f"Bem-vindo, {nome}!")

boas_vindas("Maria", 65)
boas_vindas("João", 30)