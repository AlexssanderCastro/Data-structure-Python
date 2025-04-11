def selection_sort(array):
    n = len(array)
    print("Vetor antes da ordenação:", array)
    
    
    for i in range(n):
        maiorP = i
        for j in range(i + 1, n):
            if array[j] > array[maiorP]:
                maiorP = j
        
        if i != maiorP:
            array[i], array[maiorP] = array[maiorP], array[i]
            print(f"Iteração {i + 1}: {array} (Trocou {array[maiorP]} com {array[i]})")
        else:
            print(f"Iteração {i + 1}: {array} (Sem troca)")
    
    
    print("Vetor depois da ordenação:", array)
    

selection_sort([20,50,10,21,11,12,13,15])