def adicionar_nota(notas):
    nome = input("\nNome do aluno: ")

    nota = input("Nota do aluno: ")
    
    while not (1.0 <= float(nota) <= 10.0):
        print("\nNota inválida!\n")
        nota = input("Nota do aluno: ")

    disciplina = input("Disciplina: ")

    notas.append((nome,float(nota),disciplina))

    print("\nNota adicionada com sucesso.\n")

def melhor_por_disciplina(notas):
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return
     
    disciplinas = []

    for n in notas:
         if n[2] not in disciplinas:
             disciplinas.append(n[2])

    print("\nMelhor aluno por disciplina: ")

    for d in disciplinas:
        melhor_aluno = ""
        melhor_nota = -1
        for n in notas:
            if n[2] == d and n[1] > melhor_nota:
                melhor_nota = n[1]
                melhor_aluno = n[0]
            
        print(f"\n{d}: {melhor_aluno} ({melhor_nota})")
    print()

def consulta_por_aluno(notas):
    nome_busca = input("\nDigite o nome do aluno: ")
    
    encontrou = False

    for n in notas:
        if n[0].lower().strip() == nome_busca.lower().strip():
            print(f"\n{n[2]} : {n[1]}\n")
            encontrou = True

    if not encontrou:
        print("\nNenhuma nota encontrada para este aluno.\n")


def obter_nota(tupla):
    return tupla[1]

def exibir_ordenadas(notas):
    if len(notas) == 0:
        print("\nNenhuma nota cadastrada.\n")
        return

    ordenadas = sorted(notas, key=obter_nota, reverse=True)

    print("\nNotas ordenadas (decrescente): ")
    for n in ordenadas:
        print(f"{n[1]:.2f}, {n[0]}, {n[2]} ")

def main():
    notas = []

    while True:
        print("\n===Menu de Notas===")
        print("\n1 - Adicionar nota")
        print("2 - Mostrar melhor aluno por disciplina")
        print("3 - Consultar notas por aluno")
        print("4 - Exibir notas ordenadas (decrescente)")
        print("5 - Sair\n")

        escolha = input("\nEscolha uma opção (1-5): ")

        if escolha == "1":
            adicionar_nota(notas)
        elif escolha == "2":
            melhor_por_disciplina(notas)
        elif escolha == "3":
            consulta_por_aluno(notas)
        elif escolha == "4":
            exibir_ordenadas(notas)
        elif escolha == "5":
            print("\nSaindo do programa. Até mais!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()