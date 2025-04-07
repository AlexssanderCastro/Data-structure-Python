
import time

def insertion_sort(array):    
    print("Vetor antes da ordenação:", array)
    
    inicio = time.time()  # Início da contagem do tempo
    
    n = len(array)
    for i in range(1, n):
        num = array[i]  
        j = i - 1
        while j >= 0 and array[j] > num:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = num
        
        print(f"Iteração {i}: {array}")  # Mostra o vetor após cada iteração

    fim = time.time()  # Fim da contagem do tempo

    print("Vetor depois da ordenação:", array)
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")
