def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        print("Iteração: ", i, array)
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]