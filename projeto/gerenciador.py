tarefas = []


def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")

    return


def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    print(tarefas)


while True:
    print("\nMenu do gerenciador de Lista de Tarefas:")
    print("1.   Adicionar tarefa")
    print("2.   Ver tarefas")
    print("3.   Atualizar tarefa")
    print("4.   Completar tarefa")
    print("5.   Deletar tarefas completadas")
    print("6.   Sair")

    escolha = input("Digite a sua escolha: ")

    match escolha:
        case "1":
            nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
            adicionar_tarefa(tarefas, nome_tarefa)
        case "2":
            ver_tarefas(tarefas)
        case "6":
            break




print("Programa finalizado")
