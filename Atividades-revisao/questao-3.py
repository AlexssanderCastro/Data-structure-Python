def insertion_sort_rec(arr, n):
    
    if n <= 1:
        return

    insertion_sort_rec(arr, n - 1)

    ultimo = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > ultimo:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = ultimo

lista = [5, 2, 9, 1, 3]
insertion_sort_rec(lista, len(lista))
print(lista)
