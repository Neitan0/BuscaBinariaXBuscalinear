# ============================================================
# ALGORITMOS DE BUSCA
# Busca Linear e Busca Binária
# Versões Iterativa e Recursiva
# ============================================================


# ------------------------------------------------------------
# 1. BUSCA LINEAR ITERATIVA
# ------------------------------------------------------------
def busca_linear_iterativa(lista, alvo):
    # Percorre todos os elementos da lista
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i

    # -1 indica que o elemento não foi encontrado
    return -1


# ------------------------------------------------------------
# 2. BUSCA LINEAR RECURSIVA
# ------------------------------------------------------------
def busca_linear_recursiva(lista, alvo, indice=0):
    # Caso base: chegamos ao final da lista
    if indice >= len(lista):
        return -1

    # Elemento encontrado
    if lista[indice] == alvo:
        return indice

    # Continua a busca a partir do próximo índice
    return busca_linear_recursiva(lista, alvo, indice + 1)


# ------------------------------------------------------------
# 3. BUSCA BINÁRIA ITERATIVA
# ------------------------------------------------------------
def busca_binaria_iterativa(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio

        # O alvo está na metade direita
        elif lista[meio] < alvo:
            inicio = meio + 1

        # O alvo está na metade esquerda
        else:
            fim = meio - 1

    return -1


# ------------------------------------------------------------
# 4. BUSCA BINÁRIA RECURSIVA
# ------------------------------------------------------------
def busca_binaria_recursiva(lista, alvo, inicio=0, fim=None):

    # Na primeira chamada, define o fim da lista
    if fim is None:
        fim = len(lista) - 1

    # Caso base: intervalo vazio
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    # Elemento encontrado
    if lista[meio] == alvo:
        return meio

    # Procura na metade direita
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(
            lista, alvo, meio + 1, fim
        )

    # Procura na metade esquerda
    else:
        return busca_binaria_recursiva(
            lista, alvo, inicio, meio - 1
        )


# ============================================================
# TESTES
# ============================================================

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]

alvo = 70

print("Lista:", lista)
print("Alvo:", alvo)

print("\nBusca Linear Iterativa:")
print(busca_linear_iterativa(lista, alvo))

print("\nBusca Linear Recursiva:")
print(busca_linear_recursiva(lista, alvo))

print("\nBusca Binária Iterativa:")
print(busca_binaria_iterativa(lista, alvo))

print("\nBusca Binária Recursiva:")
print(busca_binaria_recursiva(lista, alvo))
