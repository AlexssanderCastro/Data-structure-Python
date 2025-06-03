import random;
import time;


def quicksort(array, left=0, right=None):
    if right is None:
        right=len(array)-1
    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

def quicksort_iterativo(array):
    
    pilha = []
    left,right = 0,len(array) -1

    pilha.append((left,right))


    while pilha:
        left, right = pilha.pop()

        if left < right:
            pivot_index = partition(array, left, right)

            
            pilha.append((left, pivot_index - 1))
            pilha.append((pivot_index + 1, right))

def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


array = [random.randint(1, 100000) for _ in range(101)]
lista = array

inicio= time.time()
quicksort_iterativo(array)
fim = time.time()
print("Tempo versão iterativa:",fim-inicio)

inicio= time.time()
quicksort(lista)
fim = time.time()
print("Tempo versão recursiva:",fim-inicio)



#   As comparações demonstraram que quanto maior o vetor melhor ambos os algoritmos
#   se apresentam, mas a versão iterativa acaba se saindo melhor que a recursiva conforme o vetor aumenta