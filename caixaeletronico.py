saldo = 0.0

print("\n=== Bem-vindo ao Caixa Eletrônico ===")

while True:
    print("\n[ MENU ]")
    print("1 - Consultar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    
    elif opcao == "2":
        valor = float(input("\nValor a depositar: "))
        if valor > 0:
            saldo += valor
            print("\nDeposito realizado com sucesso!")
        else:
            print("\nValor inválido. Digite um valor positivo.")
    
    elif opcao == "3":
        valor = float(input("\nValor a sacar: "))
        if valor <= 0:
            print("\nValor inválido. Digite um valor positivo.")
        elif valor > saldo:
            print("\nSaldo insuficiente para o saque.")
        else:
            saldo -= valor
            print("\nSaque realizado com sucesso!")
    
    elif opcao == "4":
        print("\nObrigado por usar nosso sistema. Até logo!\n")
        break

    else:
        print("\nOpção Inválida! Tente novamente.")