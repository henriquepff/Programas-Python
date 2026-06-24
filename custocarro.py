custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

distribuidor = custo_fabrica * 0.12
imposto = custo_fabrica * 0.30
custo_consumidor = custo_fabrica + distribuidor + imposto

print(f"\nValor de Fábrica: R$ {custo_fabrica:.2f}")
print(f"Valor do Distribuidor: R$ {distribuidor:.2f}")
print(f"Valor do Imposto: R$ {imposto:.2f}")
print(f"Valor do Carro para o Consumidor: R$ {custo_consumidor:.2f}\n")