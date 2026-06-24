def adicionar_time(campeonato):
    time = input("\nNome do time a adicionar: ").strip().lower()

    if time in campeonato:
        print("\nEste time já está cadastrado.\n")
    else:
        campeonato[time] = 0
        print(f"\nTime '{time}' adicionado com 0 pontos.\n")

def registrar_resultado(campeonato):
    time1 = input("\nNome do primeiro time: ").strip().lower()
    time2 = input("\nNome do segundo time: ").strip().lower()

    if time1 not in campeonato or time2 not in campeonato:
        print("\nAmbos os times devem estar cadastrados.\n")
        return
    
    gols1 = input(f"\nGols do {time1}: ")
    while not (gols1.isdigit()):
        print("\nGols deve ser um número inteiro\n")
        gols1 = input(f"\nGols do {time1}: ")

    gols2 = input(f"\nGols do {time2}: ")
    while not (gols2.isdigit()):
        print("\nGols deve ser um número inteiro\n")
        gols2 = input(f"\nGols do {time2}: ")

    gols1n = int(gols1)
    gols2n = int(gols2)

    if gols1n > gols2n:
        campeonato[time1] += 3
        print(f"\n{time1} venceu e ganhou 3 pontos.\n")
    elif gols2n > gols1n:
        campeonato[time2] += 3
        print(f"\n{time2} venceu e ganhou 3 pontos.\n")
    else:
        campeonato[time1] += 1
        campeonato[time2] += 1
        print("\nEmpate. Cada time ganhou 1 ponto.\n")

def obter_pontos(item):
    return item[1]

def mostrar_classificacao(campeonato):
    if not campeonato:
        print("\nNenhuma time cadastrado.\n")
        return

    classificacao = sorted(campeonato.items(), key=obter_pontos, reverse=True)

    print(classificacao)
    print("\nClassificação: ")
    for posicao, (time, pontos) in enumerate(classificacao, start=1):
        print(f"{posicao} - {time}: {pontos} ponto(s)")
    print()


def remover_time(campeonato):
    time = input("\nNome do time a remover: ").strip().lower()

    if time in campeonato:
        del campeonato[time]
        print(f"\nTime {time} removido do campeonato.\n")
    else:
        print("\nTime não encontrado1\n")


def main():
    campeonato = {}

    while True:
        print("\n===Menu de Campeonato===")
        print("\n1 - Adicionar time")
        print("2 - Registrar resultado de partida")
        print("3 - Mostrar classificação")
        print("4 - Remover time")
        print("5 - Sair\n")

        escolha = input("\nEscolha uma opção (1-5): ")

        if escolha == "1":
            adicionar_time(campeonato)
        elif escolha == "2":
            registrar_resultado(campeonato)
        elif escolha == "3":
            mostrar_classificacao(campeonato)
        elif escolha == "4":
            remover_time(campeonato)
        elif escolha == "5":
            print("\nSaindo do programa. Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()