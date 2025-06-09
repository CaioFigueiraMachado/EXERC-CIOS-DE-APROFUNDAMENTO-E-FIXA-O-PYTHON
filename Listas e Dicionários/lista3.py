#Caio Machado   2BDEV
alunos = {}

for _ in range(5):
    nome = input("Nome do aluno: ")
    media = float(input("Média do aluno: "))
    alunos[nome] = media

media_turma = sum(alunos.values()) / len(alunos)

for nome, media in alunos.items():
    if media > media_turma:
        print(f"{nome} está acima da média com {media:.2f}")
