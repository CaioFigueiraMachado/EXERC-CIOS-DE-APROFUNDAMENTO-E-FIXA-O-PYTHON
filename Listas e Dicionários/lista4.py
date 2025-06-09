tarefas = []

while True:
    tarefa = input("Digite uma tarefa (ou 'fim' para parar): ")
    if tarefa.lower() == 'fim':
        break
    tarefas.append(tarefa)

remover = input("Digite o nome da tarefa a remover: ")

if remover in tarefas:
    tarefas.remove(remover)
    print("Tarefa removida.")
else:
    print("Tarefa não encontrada.")

print("Tarefas restantes:")
for t in tarefas:
    print(t)
