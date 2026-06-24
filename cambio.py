while True:
    print("\n=== MENU CONVERSÃO ===")
    print("\n1 - Dólar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Iene")
    print("5 - Sair")

    opcao = input("\nEscolha a moeda para conversão (1-4): ")

    if opcao == "1":
        taxa = 0.19
        moeda = "Dólar"
    elif opcao == "2":
        taxa = 0.17
        moeda = "Euro"
    elif opcao == "3":
        taxa = 0.15
        moeda = "Libra"
    elif opcao == "4":
        taxa = 25.0
        moeda = "Iene"
    elif opcao == "5":
        print("\nSaindo do programa...\n")
        break
    else:
        taxa = None

    if taxa is not None:
        valor_reais = float(input("\nDigite o valor em reais (R$): "))
        valor_convertido = valor_reais * taxa
        print(f"\n{valor_reais:.2f} reais equivalem a {valor_convertido:.2f} {moeda}\n")
    else:
        print("\nOpção Inválida!\n")
