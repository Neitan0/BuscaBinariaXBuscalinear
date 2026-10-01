import matplotlib.pyplot as plt
import csv
import matplotlib
matplotlib.use("Agg")

tamanhos = []
linear_iterativa = []
linear_recursiva = []
binaria_iterativa = []
binaria_recursiva = []

with open("resultados/resultados.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        tamanhos.append(int(linha["tamanho"]))
        linear_iterativa.append(float(linha["linear_iterativa"]))
        linear_recursiva.append(float(linha["linear_recursiva"]))
        binaria_iterativa.append(float(linha["binaria_iterativa"]))
        binaria_recursiva.append(float(linha["binaria_recursiva"]))


# Gráfico 1: escala normal
plt.figure(figsize=(10, 6))

plt.plot(tamanhos, linear_iterativa, marker="o", label="Linear Iterativa")
plt.plot(tamanhos, linear_recursiva, marker="o", label="Linear Recursiva")
plt.plot(tamanhos, binaria_iterativa, marker="o", label="Binária Iterativa")
plt.plot(tamanhos, binaria_recursiva, marker="o", label="Binária Recursiva")

plt.xlabel("Tamanho da entrada")
plt.ylabel("Tempo (segundos)")
plt.title("Comparação dos Algoritmos de Busca")
plt.legend()
plt.grid(True)

plt.savefig("graficos/comparacao_buscas.png")
plt.close()


# Gráfico 2: escala logarítmica
plt.figure(figsize=(10, 6))

plt.plot(tamanhos, linear_iterativa, marker="o", label="Linear Iterativa")
plt.plot(tamanhos, linear_recursiva, marker="o", label="Linear Recursiva")
plt.plot(tamanhos, binaria_iterativa, marker="o", label="Binária Iterativa")
plt.plot(tamanhos, binaria_recursiva, marker="o", label="Binária Recursiva")

plt.xscale("log")
plt.yscale("log")

plt.xlabel("Tamanho da entrada")
plt.ylabel("Tempo (segundos)")
plt.title("Comparação dos Algoritmos - Escala Logarítmica")
plt.legend()
plt.grid(True)

plt.savefig("graficos/comparacao_log.png")
plt.close()

print("Gráficos gerados com sucesso!")
