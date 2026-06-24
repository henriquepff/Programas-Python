p1 = float(input("\nDigite a nota da prova 1: "))
p2 = float(input("\nDigite a nota da prova 2: "))
t1 = float(input("\nDigite a nota do trabalho 1: "))
t2 = float(input("\nDigite a nota do trabalho 2: "))

mp = (p1 + p2)/2
mt = (t1 + t2)/2
mf = (0.8 * mp) + (0.2 * mt)

print(f"\nMédia Final: {mf:.2f}")

if mf >= 6.0:
    print("\nSituação: APROVADO\n")
else:
    print("\nSituação: REPROVADO\n")
