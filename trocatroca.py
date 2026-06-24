#lê os valores de A e B
a = int(input("\nDigite o valor de A: "))
b = int(input("\nDigite o valor de B: "))

#imprime os valores antes da troca
print("\n===Valores antes da troca===")
print(f"A = {a}")
print(f"B = {b}")

#faz a troca dos valores
temp = a
a = b
b = temp

#imprime os valores trocados
print("\n===Valores depois da troca===")
print(f"A = {a}")
print(f"B = {b}\n")

