import time

def selection_sort(array):
    n = len(array)
    print("Vetor antes da ordenação:", array)
    
    inicio_tempo = time.time()
    
    for i in range(n):
        menorP = i
        for j in range(i + 1, n):
            if array[j] < array[menorP]:
                menorP = j
        
        if i != menorP:
            array[i], array[menorP] = array[menorP], array[i]
            print(f"Iteração {i + 1}: {array} (Trocou {array[menorP]} com {array[i]})")
        else:
            print(f"Iteração {i + 1}: {array} (Sem troca)")
    
    fim_tempo = time.time()
    print("Vetor depois da ordenação:", array)
    print(f"Tempo de execução: {fim_tempo - inicio_tempo:.6f} segundos")