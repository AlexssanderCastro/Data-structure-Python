def quicksort(array, left=0, right=None, depth=0):
    if right is None:
        right = len(array) - 1

    # imprime os espaços antes da chamada
    print("    " * depth + f"quicksort({left+1}, {right+1})")  # +1 para simular índice iniciando em 1

    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1, depth + 1)
        quicksort(array, pivot_index + 1, right, depth + 1)


def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


# Teste
array = [55, 44, 22, 11, 66, 33]
print("Array desordenado:", array)
quicksort(array)
print("Array ordenado:", array)


#O resultado das chamadas de recursão nessa função ficou assim:
# quicksort(1, 6)
#     quicksort(1, 3)
#         quicksort(1, 2)
#             quicksort(1, 1)
#             quicksort(3, 2)
#         quicksort(4, 3)
#     quicksort(5, 6)
#         quicksort(5, 5)
#         quicksort(7, 6)