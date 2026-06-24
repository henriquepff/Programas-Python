nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota 1: "))
peso1 = float(input("Digite o peso da nota 1: "))

nota2 = float(input("Digite a nota 2: "))
peso2 = float(input("Digite o peso da nota 2: "))

nota3 = float(input("Digite a nota 3: "))
peso3 = float(input("Digite o peso da nota 3: "))

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)

print(f"\nNome do Aluno: {nome}")
print(f"Nota 1: {nota1} (possui peso {peso1})")
print(f"Nota 2: {nota2} (possui peso {peso2})")
print(f"Nota 3: {nota3} (possui peso {peso3})")
print(f"Média Final: {media}\n")


