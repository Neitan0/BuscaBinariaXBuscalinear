import csv
import time




# =========================
# BUSCA LINEAR ITERATIVA
# =========================

def busca_linear_iterativa(lista, alvo):

    for i in range(len(lista)):

        if lista[i] == alvo:
            return i

    return -1


# =========================
# BUSCA LINEAR RECURSIVA
# =========================

def busca_linear_recursiva(lista, alvo, indice=0):

    if indice >= len(lista):
        return -1

    if lista[indice] == alvo:
        return indice

    return busca_linear_recursiva(
        lista,
        alvo,
        indice + 1
    )


# =========================
# BUSCA BINÁRIA ITERATIVA
# =========================

def busca_binaria_iterativa(lista, alvo):

    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        elif lista[meio] < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1


# =========================
# BUSCA BINÁRIA RECURSIVA
# =========================

def busca_binaria_recursiva(
    lista,
    alvo,
    inicio=0,
    fim=None
):

    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio

    elif lista[meio] < alvo:
        return busca_binaria_recursiva(
            lista,
            alvo,
            meio + 1,
            fim
        )

    else:
        return busca_binaria_recursiva(
            lista,
            alvo,
            inicio,
            meio - 1
        )


# =========================
# MEDIÇÃO DE TEMPO
# =========================

def medir_tempo(funcao, lista, alvo):

    inicio = time.perf_counter()

    funcao(lista, alvo)

    fim = time.perf_counter()

    return fim - inicio


# =========================
# TESTE DAS FUNÇÕES
# =========================

lista_teste = [
    10, 20, 30, 40, 50,
    60, 70, 80, 90
]

alvo_teste = 70

print("Lista:", lista_teste)
print("Alvo:", alvo_teste)
print()

print("Busca Linear Iterativa:")
print(busca_linear_iterativa(lista_teste, alvo_teste))
print()

print("Busca Linear Recursiva:")
print(busca_linear_recursiva(lista_teste, alvo_teste))
print()

print("Busca Binária Iterativa:")
print(busca_binaria_iterativa(lista_teste, alvo_teste))
print()

print("Busca Binária Recursiva:")
print(busca_binaria_recursiva(lista_teste, alvo_teste))
print()


# =========================
# EXPERIMENTO
# =========================

tamanhos = [
    10,
    50,
    100,
    200,
    500,
    900
]


# True  -> salva os resultados em CSV
# False -> apenas mostra no terminal

SALVAR_CSV = False


if SALVAR_CSV:

    arquivo = open(
        "resultados/resultados.csv",
        "w",
        newline=""
    )

    escritor = csv.writer(arquivo)

    escritor.writerow([
        "tamanho",
        "linear_iterativa",
        "linear_recursiva",
        "binaria_iterativa",
        "binaria_recursiva"
    ])


for tamanho in tamanhos:

    # Lista ordenada
    # Necessária para a busca binária
    lista = list(range(tamanho))

    # Elemento que não existe na lista
    # Representa o pior caso
    alvo = -1


    # Busca linear iterativa
    tempo_linear_i = medir_tempo(
        busca_linear_iterativa,
        lista,
        alvo
    )


    # Busca linear recursiva
    tempo_linear_r = medir_tempo(
        busca_linear_recursiva,
        lista,
        alvo
    )


    # Busca binária iterativa
    tempo_binaria_i = medir_tempo(
        busca_binaria_iterativa,
        lista,
        alvo
    )


    # Busca binária recursiva
    tempo_binaria_r = medir_tempo(
        busca_binaria_recursiva,
        lista,
        alvo
    )


    # Salva no CSV somente se estiver habilitado
    if SALVAR_CSV:

        escritor.writerow([
            tamanho,
            tempo_linear_i,
            tempo_linear_r,
            tempo_binaria_i,
            tempo_binaria_r
        ])


    # Mostra os resultados no terminal
    print(f"Tamanho: {tamanho}")

    print(
        f"  Linear iterativa:  "
        f"{tempo_linear_i:.8f} s"
    )

    print(
        f"  Linear recursiva:  "
        f"{tempo_linear_r:.8f} s"
    )

    print(
        f"  Binária iterativa: "
        f"{tempo_binaria_i:.8f} s"
    )

    print(
        f"  Binária recursiva: "
        f"{tempo_binaria_r:.8f} s"
    )

    print()


if SALVAR_CSV:
    arquivo.close()