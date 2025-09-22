tarefas = []


def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")

    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start = 1):

        status = "🗸" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]

        print(f"{indice}:   [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print('Índice de tarefa inválido.')
    return

def completar_tarefas(tarefas, indice_tarefa):
    print(f"Tarefa {indice_tarefa} marcada como completada!")
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["completada"]=True
    return

def deletar_tarefas_completadas(tarefas):
   
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas.")
    return
    
    
while True:
    print("\nMenu do gerenciador de Lista de Tarefas:")
    print("1.   Adicionar tarefa")
    print("2.   Ver tarefas")
    print("3.   Atualizar tarefa")
    print("4.   Completar tarefa")
    print("5.   Deletar tarefas completadas")
    print("6.   Sair")

    escolha = input("\nDigite a sua escolha: ")

    match escolha:
        case "1":
            nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
            adicionar_tarefa(tarefas, nome_tarefa)

        case "2":
            ver_tarefas(tarefas)

        case "3":
            ver_tarefas(tarefas)
            indice_tarefa = input("Digite o número da tarefa: ")
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome)

        case "4":
            ver_tarefas(tarefas)
            indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
            completar_tarefas(tarefas, indice_tarefa)

        case "5":
            deletar_tarefas_completadas(tarefas)
            ver_tarefas(tarefas)

        case "6":
            break


print("Programa finalizado")
