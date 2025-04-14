def double_sort(array):
    print("Lista antes de ordenar: ", array)
    t = len(array)
    fim = t - 1
    comeco = 0
    
    while comeco < fim:
        maior = array[comeco]
        maiorp = comeco
        menor = array[comeco]
        menorp = comeco
        
        for i in range(comeco, fim + 1):
            if array[i] > maior:
                maior = array[i]
                maiorp = i
            if array[i] < menor:
                menor = array[i]
                menorp = i
        
        
        if menorp == fim and maiorp == comeco:
            array[comeco], array[fim] = array[fim], array[comeco]
        else:
            array[comeco], array[menorp] = array[menorp], array[comeco]
            if maiorp == comeco:
                maiorp = menorp
            array[fim], array[maiorp] = array[maiorp], array[fim]

        comeco += 1
        fim -= 1

    print("Lista depois de ordenar: ", array)


double_sort([2,5,23,7,12,9,45,21,11,1])