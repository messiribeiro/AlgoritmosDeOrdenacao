import time
import random

def gerar_lista(tamanho, tipo):
    if tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'inversa':
        return list(range(tamanho, 0, -1))
    else:  # aleatória
        return random.sample(range(tamanho * 2), tamanho)

def testar_algoritmo(nome_algoritmo, funcao, tamanho, tipo_lista):
    lista = gerar_lista(tamanho, tipo_lista)
    comparacoes = [0]
    trocas = [0]

    inicio = time.time()
    funcao(lista[:], comparacoes, trocas)
    fim = time.time()

    tempo_execucao = fim - inicio
    
    # Verificar se o tempo é maior que 60 segundos (1 minuto)
    if tempo_execucao > 60:
        tempo_execucao = tempo_execucao / 60  # Converte para minutos
        unidade = "minutos"
    else:
        unidade = "segundos"
    
    print(f"{nome_algoritmo} | Tipo: {tipo_lista:<9} | Tamanho: {tamanho:>6} | "
          f"Tempo: {tempo_execucao:.6f} {unidade} | "  # Mostrando o tempo
          f"Comparações: {comparacoes[0]} | Trocas: {trocas[0]}")

def bubble_sort(arr, comparacoes, trocas):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes[0] += 1
            if arr[j] > arr[j + 1]:
                trocas[0] += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr, comparacoes, trocas):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes[0] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            trocas[0] += 1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr, comparacoes, trocas):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes[0] += 1
            if arr[j] > chave:
                trocas[0] += 1
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = chave


tamanhos = [1000, 10000, 50000, 100000]
tipos = ['aleatoria', 'ordenada', 'inversa']
algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort)
]

for nome_algoritmo, func in algoritmos:
    for tipo in tipos:
        for tamanho in tamanhos:
            testar_algoritmo(nome_algoritmo, func, tamanho, tipo)
