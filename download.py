#lê o tamanho do arquivo em MB
tamanho_arquivo = float(input("\nDigite o tamanho do arquivo para download (MB): "))

#lê a velocidade do link em Mbps
velocidade_link = float(input("Digite a velocidade do link de Internet (Mbps): "))

#converte a velocidade do link em MBps
velocidade_MBps = velocidade_link / 8

#calcula o tempo em segundos
tempo_segundos = tamanho_arquivo / velocidade_MBps

#converte para minutos
tempo_minutos = tempo_segundos / 60

#imprime resultado
print(f"\nTamanho do Arquivo (MB): {tamanho_arquivo:.2f}")
print(f"Velocidade do link de Internet (Mbps): {velocidade_link:.2f}")
print(f"Tempo aproximado de download: {tempo_segundos:.2f} segundos")
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos\n")