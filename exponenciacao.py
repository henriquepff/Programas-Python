def potencia(base, expoente):
    if expoente == 0:
        return 1
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

    


def main():
    x = input("\nDigite o valor de x (base): ")

    while not(x.isdigit()):
        print("\nPor favor, entre com um número inteiro!")
        x = input("\nDigite o valor de x (base): ")

    y = input("\nDigite o valor de y (expoente): ")

    while not(y.isdigit()):
        print("\nPor favor, entre com um número inteiro!")
        y = input("\nDigite o valor de y (expoente): ")

    resultado = potencia(int(x), int(y))

    print(f"\n{x}^{y} = {resultado}\n")

if __name__ == "__main__":
    main()
