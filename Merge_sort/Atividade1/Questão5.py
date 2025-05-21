import random
import time

def merge_sort_recursivo(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort_recursivo(left_half)
    sorted_right = merge_sort_recursivo(right_half)

    return merge(sorted_left, sorted_right)

def merge(a, b):
    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    return c

def merge_sort_iterativo(arr):
    step = 1
    length = len(arr)
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            merged = merge(left, right)

            for j, val in enumerate(merged):
                if i + j < len(arr):
                    arr[i + j] = val
        step *= 2
    return arr



# Escolha o tamanho do vetor de teste no range
array_original = [random.randint(1, 10000) for _ in range(10000000)]

# Tempo para Recursiva
array1 = array_original.copy()
inicio_rec = time.time()
merge_sort_recursivo(array1)
fim_rec = time.time()
print("Tempo versão recursiva:", fim_rec - inicio_rec, "segundos")

# Tempo para Iterativa
array2 = array_original.copy()
inicio_it = time.time()
merge_sort_iterativo(array2)
fim_it = time.time()
print("Tempo versão iterativa:", fim_it - inicio_it, "segundos")
