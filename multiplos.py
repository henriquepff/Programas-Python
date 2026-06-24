def imprimir_multiplos(x):
    print(f"\nMúltiplos de {x} entre 1 e 100: ")
    for num in range(1,101):
        if num % x == 0:
            print(num, end = " ")
    print()
    print()


def main():
    x = input("\nDigite um número inteiro entre 1 e 100: ")

    while not (x.isdigit() and 1 <= int(x) <= 100):
        print("\nPor favor, digite um número inteiro entre 1 e 100!\n")
        x = input("\nDigite um número inteiro entre 1 e 100: ")

    imprimir_multiplos(int(x))


if __name__ == "__main__":
    main()