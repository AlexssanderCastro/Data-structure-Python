def conferirOrdem(array):
    t=len(array)
    res="Seu vetor está ordenado"
    for i in range(1,t):
        if(array[i]<array[i-1]):
            res="Vetor desordenado"
    
    print(res)


conferirOrdem([10,2,3,4,5,6,7,8])