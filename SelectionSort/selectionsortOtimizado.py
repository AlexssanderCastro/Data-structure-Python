import time

def selection_sort_otimizado(array):
    n = len(array)
    print("Vetor antes da ordenação:", array)
    
    inicio_tempo = time.time()
    
    for i in range(n):
        menorP = i
        troca_ocorreu = False  # Flag para verificar se houve troca
        
        for j in range(i + 1, n):
            if array[j] < array[menorP]:
                menorP = j
        
        if menorP != i:
            array[i], array[menorP] = array[menorP], array[i]
            troca_ocorreu = True
            print(f"Iteração {i + 1}: {array} (Trocou {array[menorP]} com {array[i]})")
        else:
            print(f"Iteração {i + 1}: {array} (Sem troca)")
        
        if not troca_ocorreu:
            break
    
    fim_tempo = time.time()
    print("Vetor depois da ordenação:", array)
    print(f"Tempo de execução: {fim_tempo - inicio_tempo:.6f} segundos")