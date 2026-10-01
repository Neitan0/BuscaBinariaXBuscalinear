from busca import (
    busca_linear_iterativa,
    busca_linear_recursiva,
    busca_binaria_iterativa,
    busca_binaria_recursiva
)
import time
import csv
import sys

sys.setrecursionlimit(2000000)


# Tamanhos das entradas que serão testadas
tamanhos = [100, 1000, 10000, 100000, 1000000]

# Número de repetições para reduzir variações de tempo
repeticoes = 10


def medir_tempo(funcao, lista, alvo):
    inicio = time.perf_counter()

    for _ in range(repeticoes):
        funcao(lista, alvo)

    fim = time.perf_counter()

    return (fim - inicio) / repeticoes


# Arquivo onde os resultados serão armazenados
with open("resultados/resultados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "tamanho",
        "linear_iterativa",
        "linear_recursiva",
        "binaria_iterativa",
        "binaria_recursiva"
    ])

    for tamanho in tamanhos:

        # Lista ordenada, necessária para a busca binária
        lista = list(range(tamanho))

        # Pior caso: elemento que não existe
        alvo = -1

        tempo_linear_i = medir_tempo(
            busca_linear_iterativa,
            lista,
            alvo
        )

        tempo_linear_r = medir_tempo(
            busca_linear_recursiva,
            lista,
            alvo
        )

        tempo_binaria_i = medir_tempo(
            busca_binaria_iterativa,
            lista,
            alvo
        )

        tempo_binaria_r = medir_tempo(
            busca_binaria_recursiva,
            lista,
            alvo
        )

        escritor.writerow([
            tamanho,
            tempo_linear_i,
            tempo_linear_r,
            tempo_binaria_i,
            tempo_binaria_r
        ])

        print(f"Tamanho: {tamanho}")
        print(f"  Linear iterativa:  {tempo_linear_i:.8f} s")
        print(f"  Linear recursiva:  {tempo_linear_r:.8f} s")
        print(f"  Binária iterativa: {tempo_binaria_i:.8f} s")
        print(f"  Binária recursiva: {tempo_binaria_r:.8f} s")
        print()
