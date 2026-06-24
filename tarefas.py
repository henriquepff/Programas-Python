def adicionar_tarefa(tarefas):
    descricao = input("\nDescrição da tarefa: ")
    prioridade = input("Prioridade (1-5, 1 = mais alta): ")

    while not (prioridade.isdigit() and 1 <= int(prioridade) <= 5):
        print("\nPor favor, digite um número inteiro de 1 a 5.\n")
        prioridade = input("Prioridade (1-5, 1 = mais alta): ")

    tarefa = {
        "descrição":descricao,
        "prioridade":int(prioridade),
        "status":"pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa adicionada com sucesso!\n")

def pegar_prioridade(tarefa):
    return tarefa["prioridade"]

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    tarefas.sort(key=pegar_prioridade)

    print("\nTAREFAS: \n")
    for i, t in enumerate(tarefas):
        print(f"{i + 1}. {t["descrição"]} (Prioridade: {t["prioridade"]}) | Status: {t["status"]}\n")

def marcar_concluida(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa para marcar.\n")
        return
    
    listar_tarefas(tarefas)
    escolha = input("\nDigite o número da tarefa concluída: ")

    while not (escolha.isdigit() and 1 <= int(escolha) <= len(tarefas)):
        print("\nNúmero inválido, tente novamente.\n")
        escolha = input("\nDigite o número da tarefa concluída: ")

    indice = int(escolha) - 1
    tarefas[indice]["status"] = "concluído"
    print("\nTarefa marcada como concluída!\n")

def excluir_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\nNenhuma tarefa para excluir.\n")
        return
    
    listar_tarefas(tarefas)
    escolha = input("\nDigite o número da tarefa a ser excluída: ")

    while not (escolha.isdigit() and 1 <= int(escolha) <= len(tarefas)):
        print("\nNúmero inválido, tente novamente.\n")
        escolha = input("\nDigite o número da tarefa a ser excluída: ")

    indice = int(escolha) - 1
    del tarefas[indice]
    print("\nTarefa excluída com sucesso!\n")

def main():
    tarefas = []

    while True:
        print("\nMENU:")
        print("\n1 - Adicionar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Marcar Tarefa como Concluída")
        print("4 - Excluir Tarefa")
        print("5 - Sair\n")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            marcar_concluida(tarefas)
        elif escolha == "4":
            excluir_tarefa(tarefas)
        elif escolha == "5":
            print("\nSaindo do programa. Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()