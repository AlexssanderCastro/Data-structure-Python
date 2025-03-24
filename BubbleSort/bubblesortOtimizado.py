import time

def bubble_sort_otimizado(array):
    n = len(array)
    start_time = time.time()  
    for i in range(n-1):
        troca_ocorreu = False  
        print("Iteração:", i, array)
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                troca_ocorreu = True  

        if not troca_ocorreu:  
            break  
    
    end_time = time.time()  
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")