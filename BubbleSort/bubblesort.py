import time

def bubble_sort(array):
    n = len(array)
    start_time = time.time() 
    for i in range(n-1):
        print("Iteração:", i, array)
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    end_time = time.time()  
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")